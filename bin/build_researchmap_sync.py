#!/usr/bin/env python3
"""Build Researchmap import review queue and draft CSV rows (site master + RM supplement)."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JA_RESEARCHER = ROOT / "ja_researcher"
OUT_DIR = JA_RESEARCHER / "out"
JSONL_PATH = ROOT / "rm_researchers20260707.jsonl"
PUBS_PATH = ROOT / "_data" / "publications.json"
QUEUE_PATH = JA_RESEARCHER / "review_queue.json"
STATE_PATH = JA_RESEARCHER / "review_state.json"
WORKFLOW_PATH = JA_RESEARCHER / "review_workflow.md"

RM_CSV_FILES = {
    "published_papers": JA_RESEARCHER / "rm_published_papers.csv",
    "misc": JA_RESEARCHER / "rm_misc.csv",
    "presentations": JA_RESEARCHER / "rm_presentations.csv",
    "books_etc": JA_RESEARCHER / "rm_books_etc.csv",
}

# Load compare helpers
_spec = importlib.util.spec_from_file_location(
    "compare_researchmap", ROOT / "bin" / "compare_researchmap.py"
)
compare = importlib.util.module_from_spec(_spec)
sys.modules["compare_researchmap"] = compare
_spec.loader.exec_module(compare)

SITE_CATEGORY_TO_RM = {
    "Books": ("books_etc", None),
    "Journal Papers": ("published_papers", "scientific_journal"),
    "Invited Talks and Tutorials": ("presentations", "invited"),
    "International Conference Proceedings": (
        "published_papers",
        "international_conference_proceedings",
    ),
    "Domestic Conference Proceedings": ("misc", "summary_national_conference"),
    "Misc.": ("misc", "introduction_scientific_journal"),
}

RM_PUBLISHED_TYPE_LABEL = {
    "scientific_journal": "scientific_journal",
    "international_conference_proceedings": "international_conference_proceedings",
    "research_society": "research_society",
}

RM_MISC_TYPE_LABEL = {
    "summary_national_conference": "summary_national_conference",
    "summary_international_conference": "summary_international_conference",
    "introduction_commerce_magazine": "introduction_commerce_magazine",
    "introduction_scientific_journal": "introduction_scientific_journal",
    "book_review": "book_review",
    "meeting_report": "meeting_report",
    "magazine_article": "introduction_scientific_journal",
}

# Researchmap CSV: blank optional fields must be the literal string "null".
NULLABLE_CSV_FIELDS = {
    "担当区分",
    "査読の有無",
    "招待の有無",
    "国際・国内誌",
    "国際共著",
    "国際・国内会議",
    "著書種別",
}

BOOK_ROLE_MAP = {
    "著": "joint_work",
    "著, 訳": "joint_translation",
    "編著, 著": "joint_editor",
    "編著": "editor",
    "訳": "joint_translation",
    "単著": "single_work",
    "共著": "joint_work",
    "分担": "contributor",
}


def has_japanese(text: str) -> bool:
    return bool(re.search(r"[\u3040-\u30ff\u4e00-\u9fff]", text or ""))


def split_title(title: str) -> tuple[str, str]:
    if has_japanese(title):
        return title, ""
    return "", title


def split_authors(authors: str) -> tuple[str, str]:
    if has_japanese(authors):
        return authors, ""
    return "", authors


def pub_date_yyyymm(value: str | None) -> str:
    parsed = compare.parse_date(value)
    if not parsed:
        return ""
    if len(parsed) == 4:
        return parsed
    return parsed[:7]


def is_trivial_diff(diffs: list[str]) -> bool:
    if not diffs:
        return True
    allowed = {"authors", "date", "publication_info", "doi", "category"}
    keys = {d.split(":")[0] for d in diffs}
    return keys.issubset(allowed)


def meaningful_diffs(diffs: list[str]) -> list[str]:
    meaningful = []
    for d in diffs:
        if d.startswith("category:"):
            continue
        if d.startswith("authors:"):
            continue
        if d.startswith("date:"):
            continue
        if d.startswith("publication_info:"):
            continue
        meaningful.append(d)
    return meaningful


def infer_misc_type(title: str, publication_info: str, subtype: str | None) -> str:
    """Map legacy magazine_article and Misc. rows to valid Researchmap misc_type."""
    if subtype and subtype != "magazine_article":
        return RM_MISC_TYPE_LABEL.get(subtype, subtype)

    text = f"{title} {publication_info}"
    if "書評" in text:
        return "book_review"
    if any(k in text for k in ("見聞記", "参加報告", "実施報告", "実施概要", " report")):
        return "meeting_report"
    if any(
        k in publication_info
        for k in ("毎日新聞", "映像情報インダストリアル", "映像情報industrial")
    ):
        return "introduction_commerce_magazine"
    return "introduction_scientific_journal"


def map_book_owner_role(site: dict, rm: dict | None = None) -> str:
    if rm and rm.get("raw", {}).get("book_owner_role"):
        return rm["raw"]["book_owner_role"]
    roles = (site.get("author_roles") or "").strip()
    if roles in BOOK_ROLE_MAP:
        return BOOK_ROLE_MAP[roles]
    authors = site.get("authors") or ""
    if "制作チーム" in authors or "制作チーム" in site.get("title", ""):
        return "contributor"
    if "訳" in roles:
        return "joint_translation"
    if "編著" in roles:
        return "joint_editor"
    if roles:
        return BOOK_ROLE_MAP.get(roles, "joint_work")
    return "joint_work"


def load_stale_rm_ids() -> set[str]:
    stale: set[str] = set()
    if not OUT_DIR.exists():
        return stale
    for path in OUT_DIR.glob("errors_*.csv"):
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                msg = row.get("エラー内容(エラーコード, フィールド名, メッセージ)", "")
                if "not_found" in msg and row.get("ID"):
                    stale.add(row["ID"])
    return stale


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {}


def effective_category(
    site_category: str,
    review_id: str | None,
    state: dict,
    rm_hint: dict | None = None,
) -> tuple[str, str, str]:
    """Return (site_category, rm_type, misc_or_paper_subtype)."""
    overrides = state.get("category_overrides", {})
    if review_id and review_id in overrides:
        ov = overrides[review_id]
        cat = ov.get("site_category", site_category)
        rm_type = ov.get("rm_type") or SITE_CATEGORY_TO_RM.get(cat, ("misc", None))[0]
        subtype = ov.get("掲載種別") or SITE_CATEGORY_TO_RM.get(
            cat, ("misc", "introduction_scientific_journal")
        )[1]
        return cat, rm_type, subtype or "introduction_scientific_journal"

    if rm_hint and rm_hint.get("category_guess") == "Presentations (non-invited)":
        return (
            "International Conference Proceedings",
            "misc",
            "summary_international_conference",
        )

    rm_type, subtype = SITE_CATEGORY_TO_RM.get(
        site_category, ("misc", "introduction_scientific_journal")
    )
    if site_category == "Domestic Conference Proceedings":
        return site_category, "misc", "summary_national_conference"
    return site_category, rm_type, subtype or "introduction_scientific_journal"


def apply_row_overrides(row: dict, review_id: str | None, state: dict) -> dict:
    if not review_id:
        return row
    out = dict(row)
    for key in ("author_overrides", "publication_overrides"):
        patch = state.get(key, {}).get(review_id)
        if patch:
            for field, value in patch.items():
                if field != "note":
                    out[field] = value
    category_patch = state.get("category_overrides", {}).get(review_id, {})
    misc_type = category_patch.get("掲載種別")
    if misc_type and misc_type != "magazine_article" and "掲載種別" in out:
        out["掲載種別"] = RM_MISC_TYPE_LABEL.get(misc_type, misc_type)
    return out


def review_id_for_rm_id(queue: list[dict], decisions: dict, rm_id: str) -> str | None:
    for item in queue:
        if item.get("rm_id") == rm_id and decisions.get(item.get("review_id")) == "yes":
            return item["review_id"]
    return None


def rm_export_decision(queue: list[dict], decisions: dict, rm_id: str) -> str | None:
    for item in queue:
        if item.get("rm_id") == rm_id:
            return decisions.get(item["review_id"])
    return None


def should_skip_rm_export(queue: list[dict], decisions: dict, rm_id: str) -> bool:
    decision = rm_export_decision(queue, decisions, rm_id)
    return decision == "no"


def normalize_csv_row(row: dict, rm_type: str | None = None) -> dict:
    """Researchmap CSV expects disclosed/closed, TRUE/FALSE, and null sentinels."""
    out = dict(row)
    display_map = {
        "公開": "disclosed",
        "非公開": "closed",
        "研究者のみ公開": "researchers_only",
    }
    bool_map = {
        "いいえ": "FALSE",
        "はい": "TRUE",
        "あり": "TRUE",
        "なし": "FALSE",
    }
    if out.get("公開の有無") in display_map:
        out["公開の有無"] = display_map[out["公開の有無"]]
    if out.get("主要な業績かどうか") in bool_map:
        out["主要な業績かどうか"] = bool_map[out["主要な業績かどうか"]]
    for field in (
        "招待の有無",
        "査読の有無",
        "国際・国内誌",
        "国際共著",
        "国際・国内会議",
    ):
        if field in out and out[field] in bool_map:
            out[field] = bool_map[out[field]]

    if rm_type == "misc" and not out.get("タイトル(日本語)") and out.get("タイトル(英語)"):
        out["タイトル(日本語)"] = out["タイトル(英語)"]

    for field in NULLABLE_CSV_FIELDS:
        if field in out and out[field] == "":
            out[field] = "null"
    return out


def fallback_insert_if_stale(row: dict, stale_ids: set[str]) -> dict:
    rid = row.get("ID", "")
    if rid and rid in stale_ids:
        out = dict(row)
        out["ID"] = ""
        out["アクション名"] = "insert"
        out["アクションタイプ"] = "merge"
        return out
    return row


def site_to_csv_row(
    site: dict,
    rm: dict | None = None,
    rm_id: str = "",
    review_id: str | None = None,
    state: dict | None = None,
) -> dict:
    state = state or {}
    category = site["category"]
    category, rm_type, subtype = effective_category(
        category, review_id, state, rm_hint=rm
    )

    title_ja, title_en = split_title(site["title"])
    authors_ja, authors_en = split_authors(site["authors"])
    pub_date = pub_date_yyyymm(site.get("publication_date") or site.get("date"))
    doi = site.get("doi") or ""
    if not doi and rm:
        doi = rm.get("doi") or ""

    action = "update" if rm_id else "insert"
    action_type = "doc" if rm_id else "merge"

    base = {
        "アクション名": action,
        "アクションタイプ": action_type,
        "類似業績マージ優先度": "",
        "ID": rm_id,
        "主要な業績かどうか": "FALSE",
        "公開の有無": "disclosed",
    }

    if rm_type == "published_papers":
        row = {
            **base,
            "タイトル(日本語)": title_ja,
            "タイトル(英語)": title_en,
            "著者(日本語)": authors_ja,
            "著者(英語)": authors_en,
            "概要(日本語)": "",
            "概要(英語)": "",
            "出版者・発行元(日本語)": "",
            "出版者・発行元(英語)": "",
            "出版年月": pub_date,
            "誌名(日本語)": site.get("publication_info", "") if has_japanese(site.get("publication_info", "")) else "",
            "誌名(英語)": site.get("publication_info", "") if not has_japanese(site.get("publication_info", "")) else "",
            "巻": site.get("volume", ""),
            "号": site.get("number", ""),
            "開始ページ": site.get("start_page", ""),
            "終了ページ": site.get("end_page", ""),
            "記述言語": "jpn" if title_ja else "eng",
            "査読の有無": "",
            "招待の有無": "",
            "掲載種別": RM_PUBLISHED_TYPE_LABEL.get(subtype or "", subtype or ""),
            "国際・国内誌": "",
            "国際共著": "",
            "DOI": doi,
            "ISSN": "",
            "eISSN": "",
            "URL": "",
            "URL2": "",
        }
        return {"rm_type": rm_type, "row": row}

    if rm_type == "presentations":
        row = {
            **base,
            "タイトル(日本語)": title_ja,
            "タイトル(英語)": title_en,
            "講演者(日本語)": authors_ja,
            "講演者(英語)": authors_en,
            "会議名(日本語)": site.get("publication_info", "") if has_japanese(site.get("publication_info", "")) else "",
            "会議名(英語)": site.get("publication_info", "") if not has_japanese(site.get("publication_info", "")) else "",
            "発表年月日": pub_date,
            "開催年月日(From)": pub_date,
            "開催年月日(To)": pub_date,
            "招待の有無": "TRUE",
            "記述言語": "jpn" if title_ja else "eng",
            "会議種別": "public_discourse",
            "主催者(日本語)": "",
            "主催者(英語)": "",
            "開催地(日本語)": site.get("venue", ""),
            "開催地(英語)": "",
            "国・地域": "",
            "概要(日本語)": "",
            "概要(英語)": "",
            "国際・国内会議": "",
            "国際共著": "",
            "URL": "",
            "URL2": "",
        }
        return {"rm_type": rm_type, "row": row}

    if rm_type == "books_etc":
        row = {
            **base,
            "タイトル(日本語)": title_ja or site["title"],
            "タイトル(英語)": title_en,
            "担当区分": map_book_owner_role(site, rm),
            "著者(翻訳者)(日本語)": authors_ja,
            "著者(翻訳者)(英語)": authors_en,
            "原著者(日本語)": "",
            "原著者(英語)": "",
            "担当範囲(日本語)": "",
            "担当範囲(英語)": "",
            "出版者・発行元(日本語)": site.get("publication_info", ""),
            "出版者・発行元(英語)": "",
            "概要(日本語)": "",
            "概要(英語)": "",
            "出版年月": pub_date,
            "総ページ数": "",
            "担当ページ": "",
            "記述言語": "jpn",
            "査読の有無": "",
            "著書種別": "",
            "国際共著": "",
            "DOI": doi,
            "ISBN": "",
            "URL": "",
            "URL2": "",
        }
        return {"rm_type": rm_type, "row": row}

    # misc
    row = {
        **base,
        "タイトル(日本語)": title_ja,
        "タイトル(英語)": title_en,
        "著者(日本語)": authors_ja,
        "著者(英語)": authors_en,
        "概要(日本語)": "",
        "概要(英語)": "",
        "出版者・発行元(日本語)": "",
        "出版者・発行元(英語)": "",
        "出版年月": pub_date,
        "誌名(日本語)": site.get("publication_info", "") if has_japanese(site.get("publication_info", "")) else "",
        "誌名(英語)": site.get("publication_info", "") if not has_japanese(site.get("publication_info", "")) else "",
        "巻": site.get("volume", ""),
        "号": site.get("number", ""),
        "開始ページ": site.get("start_page", ""),
        "終了ページ": site.get("end_page", ""),
        "記述言語": "jpn" if title_ja else "eng",
        "査読の有無": "",
        "招待の有無": "",
        "掲載種別": infer_misc_type(
            site["title"],
            site.get("publication_info", ""),
            ((rm.get("raw", {}).get("misc_type") if rm else None) or subtype),
        ),
        "国際・国内誌": "",
        "国際共著": "",
        "DOI": doi,
        "ISSN": "",
        "eISSN": "",
        "URL": "",
        "URL2": "",
    }
    row = apply_row_overrides(row, review_id, state)
    return {"rm_type": rm_type, "row": row}


def build_match_data() -> dict:
    rm_records = compare.load_researchmap_records(JSONL_PATH)
    site_records = compare.load_site_records(PUBS_PATH)
    rm_by_doi, rm_by_title = compare.build_indexes(rm_records, "rm")
    site_by_doi, site_by_title = compare.build_indexes(site_records, "site")

    matched_pairs = []
    only_rm = []
    only_site = []
    used_site_ids: set[int] = set()

    for rm in rm_records:
        site = compare.find_match(rm, site_by_doi, site_by_title, used_site_ids)
        if site:
            used_site_ids.add(site["id"])
            diffs = compare.field_diffs(rm, site)
            matched_pairs.append((rm, site, diffs))
        else:
            only_rm.append(rm)

    for site in site_records:
        if site["id"] not in used_site_ids:
            only_site.append(site)

    auto_ok = []
    trivial_resolved = []
    for rm, site, diffs in matched_pairs:
        if not diffs:
            auto_ok.append((rm, site))
        elif is_trivial_diff(diffs):
            trivial_resolved.append((rm, site, diffs))

    return {
        "rm_records": rm_records,
        "site_records": site_records,
        "auto_ok": auto_ok,
        "trivial_resolved": trivial_resolved,
        "only_rm": only_rm,
        "only_site": only_site,
        "site_by_id": {s["id"]: s for s in site_records},
        "rm_by_id": {r["rm_id"]: r for r in rm_records},
    }


def read_csv_header(path: Path) -> list[str]:
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # type row
        return next(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    def cell_value(field: str, row: dict) -> str:
        value = row.get(field, "")
        if value == "" and field in NULLABLE_CSV_FIELDS:
            return "null"
        return value

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([path.stem.replace("rm_", "")])
        writer.writerow(fieldnames)
        dict_writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for row in rows:
            dict_writer.writerow({k: cell_value(k, row) for k in fieldnames})


def export_csvs() -> dict:
    state = load_state()
    decisions = state.get("decisions", {})
    queue = json.loads(QUEUE_PATH.read_text(encoding="utf-8"))
    queue_by_rid = {item["review_id"]: item for item in queue["queue"]}
    match_data = build_match_data()
    site_by_id = match_data["site_by_id"]
    rm_by_id = match_data["rm_by_id"]

    buckets: dict[str, list[dict]] = {
        "published_papers": [],
        "misc": [],
        "presentations": [],
        "books_etc": [],
    }
    seen_ids: set[str] = set()
    seen_titles: dict[str, set[str]] = {}

    def title_key(row: dict) -> str:
        title = row.get("タイトル(日本語)") or row.get("タイトル(英語)") or ""
        return compare.normalize_text(title)

    stale_ids = load_stale_rm_ids()

    def add_row(rm_type: str, row: dict) -> None:
        row = fallback_insert_if_stale(row, stale_ids)
        row = normalize_csv_row(row, rm_type=rm_type)
        rid = row.get("ID", "")
        tkey = title_key(row)
        if rid:
            if rid in seen_ids:
                return
            seen_ids.add(rid)
        elif tkey:
            bucket_titles = seen_titles.setdefault(rm_type, set())
            if tkey in bucket_titles:
                return
            bucket_titles.add(tkey)
        buckets[rm_type].append(row)

    queue_items = queue["queue"]
    for rm, site in match_data["auto_ok"]:
        if should_skip_rm_export(queue_items, decisions, rm["rm_id"]):
            continue
        review_id = review_id_for_rm_id(queue_items, decisions, rm["rm_id"])
        payload = site_to_csv_row(
            site["raw"], rm=rm, rm_id=rm["rm_id"], review_id=review_id, state=state
        )
        payload["row"]["アクション名"] = "update"
        payload["row"]["アクションタイプ"] = "doc"
        add_row(payload["rm_type"], payload["row"])

    for rm, site, _ in match_data["trivial_resolved"]:
        if should_skip_rm_export(queue_items, decisions, rm["rm_id"]):
            continue
        review_id = review_id_for_rm_id(queue_items, decisions, rm["rm_id"])
        payload = site_to_csv_row(
            site["raw"], rm=rm, rm_id=rm["rm_id"], review_id=review_id, state=state
        )
        payload["row"]["アクション名"] = "update"
        payload["row"]["アクションタイプ"] = "doc"
        add_row(payload["rm_type"], payload["row"])

    skip_export_ids = {
        rid
        for rid, note in state.get("notes", {}).items()
        if isinstance(note, dict) and "エクスポート除外" in note.get("note", "")
    }
    skip_export_ids.add("R0118")

    for item in queue["queue"]:
        review_id = item["review_id"]
        if review_id in skip_export_ids:
            continue
        decision = decisions.get(review_id)
        if decision != "yes":
            continue
        phase = item["phase"]
        if phase == "site_only":
            site = site_by_id.get(item["site_id"])
            if not site:
                continue
            payload = site_to_csv_row(
                site["raw"], review_id=review_id, state=state
            )
            payload["row"]["アクション名"] = "insert"
            payload["row"]["アクションタイプ"] = "merge"
            add_row(payload["rm_type"], payload["row"])
        elif phase == "rm_only":
            rm = rm_by_id.get(item["rm_id"])
            if not rm:
                continue
            payload = rm_to_csv_row(rm, review_id=review_id, state=state)
            if payload["rm_type"] != rm["rm_type"]:
                payload["row"]["アクション名"] = "insert"
                payload["row"]["アクションタイプ"] = "merge"
                payload["row"]["ID"] = ""
            add_row(payload["rm_type"], payload["row"])

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    counts = {}
    for rm_type, template in RM_CSV_FILES.items():
        header = read_csv_header(template)
        out_path = OUT_DIR / template.name
        write_csv(out_path, header, buckets[rm_type])
        counts[rm_type] = len(buckets[rm_type])

    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "output_dir": str(OUT_DIR),
        "counts": counts,
        "total_rows": sum(counts.values()),
        "matched_updates": len(match_data["auto_ok"]) + len(match_data["trivial_resolved"]),
        "review_yes": sum(1 for d in decisions.values() if d == "yes"),
    }
    (OUT_DIR / "export_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return summary


def rm_guess_to_site_category(guess: str) -> str:
    mapping = {
        "Journal Papers": "Journal Papers",
        "International Conference Proceedings": "International Conference Proceedings",
        "Domestic Conference Proceedings": "Domestic Conference Proceedings",
        "Invited Talks and Tutorials": "Invited Talks and Tutorials",
        "Misc.": "Misc.",
        "Books": "Books",
        "Presentations (non-invited)": "International Conference Proceedings",
        "RM:published_papers": "Domestic Conference Proceedings",
    }
    return mapping.get(guess, "Misc.")


def rm_to_csv_row(
    rm: dict,
    review_id: str | None = None,
    state: dict | None = None,
) -> dict:
    """Build CSV row from researchmap-only record (for user-approved additions)."""
    state = state or {}
    fake_site = {
        "category": rm_guess_to_site_category(rm["category_guess"]),
        "title": rm["title"],
        "authors": rm["authors"],
        "publication_info": rm["publication_info"],
        "publication_date": rm["date"],
        "volume": "",
        "number": "",
        "start_page": "",
        "end_page": "",
        "venue": "",
        "doi": rm.get("doi", ""),
        "author_roles": "",
    }
    payload = site_to_csv_row(
        fake_site, rm=rm, rm_id=rm["rm_id"], review_id=review_id, state=state
    )
    payload["row"]["アクション名"] = "update"
    payload["row"]["アクションタイプ"] = "doc"
    payload["row"]["ID"] = rm["rm_id"]
    payload["row"] = apply_row_overrides(payload["row"], review_id, state)
    return payload


def sort_key_date(rec: dict) -> str:
    return rec.get("date") or rec.get("publication_date") or ""


def build_queue() -> dict:
    match_data = build_match_data()
    rm_records = match_data["rm_records"]
    only_rm = match_data["only_rm"]
    only_site = match_data["only_site"]
    auto_ok = match_data["auto_ok"]
    trivial_resolved = match_data["trivial_resolved"]

    matched_pairs = []
    for rm, site, diffs in [
        (r, s, compare.field_diffs(r, s))
        for r, s in auto_ok
    ]:
        matched_pairs.append((rm, site, diffs))
    for rm, site, diffs in trivial_resolved:
        matched_pairs.append((rm, site, diffs))

    conflict_review = []
    # rebuild conflict from full pairing
    rm_by_doi, rm_by_title = compare.build_indexes(rm_records, "rm")
    site_by_doi, site_by_title = compare.build_indexes(match_data["site_records"], "site")
    used_site_ids: set[int] = set()
    for rm in rm_records:
        site = compare.find_match(rm, site_by_doi, site_by_title, used_site_ids)
        if site:
            used_site_ids.add(site["id"])
            diffs = compare.field_diffs(rm, site)
            if diffs and not is_trivial_diff(diffs):
                conflict_review.append((rm, site, diffs))

    queue_items = []
    seq = 1

    def add_item(**kwargs):
        nonlocal seq
        item = {"review_id": f"R{seq:04d}", "status": "pending", **kwargs}
        queue_items.append(item)
        seq += 1

    for site in sorted(only_site, key=sort_key_date, reverse=True):
        csv_payload = site_to_csv_row(site["raw"])
        add_item(
            phase="site_only",
            question="Webサイトのみに存在。Researchmapへ新規追加しますか？",
            default_recommendation="yes",
            site_id=site["id"],
            site_title=site["title"],
            site_category=site["category"],
            site_publication_info=site.get("publication_info", ""),
            site_raw_text=site["raw_text"],
            rm_id="",
            rm_type=csv_payload["rm_type"],
            diffs=[],
            proposed_csv=csv_payload["row"],
        )

    for rm in sorted(only_rm, key=sort_key_date, reverse=True):
        csv_payload = rm_to_csv_row(rm)
        add_item(
            phase="rm_only",
            question="Researchmapのみに存在。Webサイト未登録だがRMデータをインポートに含めますか？",
            default_recommendation="ask",
            site_id=None,
            site_title="",
            site_category="",
            site_raw_text="",
            rm_id=rm["rm_id"],
            rm_type=rm["rm_type"],
            rm_title=rm["title"],
            rm_category_guess=rm["category_guess"],
            rm_publication_info=rm["publication_info"],
            rm_authors=rm["authors"],
            rm_date=rm["date"],
            rm_doi=rm.get("doi", ""),
            diffs=[],
            proposed_csv=csv_payload["row"],
        )

    for rm, site, diffs in sorted(
        conflict_review, key=lambda p: sort_key_date(p[1]), reverse=True
    ):
        csv_payload = site_to_csv_row(site["raw"], rm=rm, rm_id=rm["rm_id"])
        csv_payload["row"]["アクション名"] = "update"
        csv_payload["row"]["アクションタイプ"] = "doc"
        csv_payload["row"]["ID"] = rm["rm_id"]
        add_item(
            phase="conflict",
            question="マッチしたが差分あり。Webサイト情報でRMを更新しますか？",
            default_recommendation="yes",
            site_id=site["id"],
            site_title=site["title"],
            site_category=site["category"],
            site_publication_info=site.get("publication_info", ""),
            site_raw_text=site["raw_text"],
            rm_id=rm["rm_id"],
            rm_type=rm["rm_type"],
            rm_title=rm["title"],
            rm_publication_info=rm["publication_info"],
            diffs=diffs,
            proposed_csv=csv_payload["row"],
        )

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "summary": {
            "site_total": len(match_data["site_records"]),
            "rm_total": len(rm_records),
            "auto_ok": len(auto_ok),
            "trivial_resolved": len(trivial_resolved),
            "review_site_only": len(only_site),
            "review_rm_only": len(only_rm),
            "review_conflict": len(conflict_review),
            "review_total": len(queue_items),
        },
        "auto_ok_site_ids": [s["id"] for _, s in auto_ok],
        "trivial_resolved": [
            {
                "site_id": s["id"],
                "rm_id": r["rm_id"],
                "rm_type": r["rm_type"],
                "title": s["title"],
                "diffs": d,
            }
            for r, s, d in trivial_resolved
        ],
        "queue": queue_items,
    }


def write_workflow_md(data: dict) -> None:
    s = data["summary"]
    lines = [
        "# Researchmap 同期レビュー手順",
        "",
        f"生成日時: {data['generated_at']}",
        "",
        "## 方針",
        "",
        "1. **マスタは Webサイト**（`_data/publications.json`）",
        "2. Researchmap 側の情報は、サイトにない項目の**補完**として利用（主に DOI / RM ID）",
        "3. レビューは `ja_researcher/review_queue.json` の順に **Yes / No** で判断",
        "4. 判断結果は `ja_researcher/review_state.json` に記録し、最終 CSV を生成",
        "",
        "## 件数",
        "",
        f"| 区分 | 件数 | 扱い |",
        f"|------|------|------|",
        f"| 自動一致（差分なし） | {s['auto_ok']} | サイトデータでCSV化（レビュー不要） |",
        f"| 軽微差分（著者・日付・表記ゆれ） | {s['trivial_resolved']} | サイト優先で自動反映（レビュー不要） |",
        f"| **要レビュー: サイトのみ** | {s['review_site_only']} | RMへ新規追加するか |",
        f"| **要レビュー: RMのみ** | {s['review_rm_only']} | RMデータを残すか（サイト未登録） |",
        f"| **要レビュー: 差分あり** | {s['review_conflict']} | サイトでRMを更新するか |",
        f"| **要レビュー合計** | **{s['review_total']}** | |",
        "",
        "## 回答の仕方（チャットで）",
        "",
        "```",
        "Yes   … 提案どおり採用",
        "No    … 今回はスキップ",
        "Skip  … 保留",
        "```",
        "",
        "## 出力先",
        "",
        "- レビューキュー: `ja_researcher/review_queue.json`",
        "- 判断記録: `ja_researcher/review_state.json`",
        "- 最終CSV: `ja_researcher/out/rm_*.csv`（全レビュー完了後に生成）",
        "",
    ]
    WORKFLOW_PATH.write_text("\n".join(lines), encoding="utf-8")


def init_state(data: dict) -> None:
    if STATE_PATH.exists():
        return
    STATE_PATH.write_text(
        json.dumps(
            {
                "decisions": {},
                "current_review_id": data["queue"][0]["review_id"] if data["queue"] else None,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Researchmap sync tools")
    parser.add_argument(
        "--export",
        action="store_true",
        help="Generate ja_researcher/out/rm_*.csv from review decisions",
    )
    args = parser.parse_args()

    JA_RESEARCHER.mkdir(exist_ok=True)
    (JA_RESEARCHER / "out").mkdir(exist_ok=True)

    if args.export:
        summary = export_csvs()
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return

    data = build_queue()
    QUEUE_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    write_workflow_md(data)
    init_state(data)

    print(f"Wrote {QUEUE_PATH}")
    print(f"Wrote {WORKFLOW_PATH}")
    print(json.dumps(data["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
