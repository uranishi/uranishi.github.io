#!/usr/bin/env python3
"""Compare researchmap JSONL export with _data/publications.json."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSONL_PATH = ROOT / "rm_researchers20260707.jsonl"
PUBS_PATH = ROOT / "_data" / "publications.json"
REPORT_PATH = ROOT / "researchmap_diff_20260707.md"

RM_CATEGORY_MAP = {
    ("published_papers", "scientific_journal"): "Journal Papers",
    ("published_papers", "international_conference_proceedings"): "International Conference Proceedings",
    ("published_papers", "research_society"): "Domestic Conference Proceedings",
    ("misc", "summary_national_conference"): "Domestic Conference Proceedings",
    ("misc", "summary_international_conference"): "International Conference Proceedings",
    ("misc", "introduction_commerce_magazine"): "Misc.",
    ("books_etc", None): "Books",
}

PRESENTATION_TALK_TYPES = {
    "invited_oral_presentation",
    "public_discourse",
}


def parse_date(value: str | None) -> str | None:
    if not value:
        return None
    value = str(value).strip()
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d", "%Y-%m"):
        try:
            return datetime.strptime(value[: len(fmt.replace("%", "0"))], fmt).strftime("%Y-%m")
        except ValueError:
            pass
    m = re.match(r"^(\d{4})(?:-(\d{1,2}))?", value)
    if m:
        year, month = m.group(1), m.group(2)
        return f"{year}-{int(month):02d}" if month else year
    return value


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "")
    text = text.lower()
    text = re.sub(r"[\s\-–—_~～・:：/／,.，．;；!！?？\"'「」『』（）()【】\[\]{}]+", "", text)
    return text


def pick_localized(value) -> str:
    if isinstance(value, dict):
        return (value.get("ja") or value.get("en") or "").strip()
    return str(value or "").strip()


def pick_people(value) -> str:
    if not value:
        return ""
    if isinstance(value, dict):
        lang = value.get("ja") or value.get("en") or []
    else:
        lang = value
    names = []
    for person in lang:
        if isinstance(person, dict):
            names.append(person.get("name", "").strip())
        else:
            names.append(str(person).strip())
    return ", ".join(n for n in names if n)


def extract_doi(merge: dict) -> str:
    doi = (merge.get("identifiers") or {}).get("doi")
    if isinstance(doi, list) and doi:
        return doi[0].lower().strip()
    if isinstance(doi, str):
        return doi.lower().strip()
    for item in merge.get("see_also") or []:
        if item.get("label") == "doi" and item.get("@id"):
            return item["@id"].replace("https://doi.org/", "").lower().strip()
    return ""


def map_rm_category(rm_type: str, merge: dict) -> str:
    if rm_type == "presentations":
        if merge.get("invited") or merge.get("presentation_type") in PRESENTATION_TALK_TYPES:
            return "Invited Talks and Tutorials"
        return "Presentations (non-invited)"
    if rm_type == "misc" and "misc_type" not in merge:
        return "Misc."
    key = (rm_type, merge.get("misc_type") if rm_type == "misc" else merge.get("published_paper_type"))
    if rm_type == "books_etc":
        key = ("books_etc", None)
    return RM_CATEGORY_MAP.get(key, f"RM:{rm_type}")


def publication_info_from_rm(rm_type: str, merge: dict) -> str:
    if rm_type == "presentations":
        return pick_localized(merge.get("event"))
    if rm_type == "books_etc":
        return pick_localized(merge.get("publisher"))
    return pick_localized(merge.get("publication_name"))


def title_from_rm(rm_type: str, merge: dict) -> str:
    for key in ("paper_title", "presentation_title", "book_title"):
        if key in merge:
            return pick_localized(merge[key])
    return ""


def authors_from_rm(rm_type: str, merge: dict) -> str:
    for key in ("authors", "presenters", "presenters_text"):
        if key in merge:
            value = merge[key]
            if key == "presenters_text":
                return pick_localized(value)
            return pick_people(value)
    return ""


def load_researchmap_records(path: Path) -> list[dict]:
    records = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            rm_type = obj["insert"]["type"]
            if rm_type not in {
                "published_papers",
                "misc",
                "presentations",
                "books_etc",
            }:
                continue
            merge = obj["merge"]
            title = title_from_rm(rm_type, merge)
            if not title:
                continue
            records.append(
                {
                    "rm_id": obj["insert"]["id"],
                    "rm_type": rm_type,
                    "title": title,
                    "authors": authors_from_rm(rm_type, merge),
                    "category_guess": map_rm_category(rm_type, merge),
                    "publication_info": publication_info_from_rm(rm_type, merge),
                    "date": parse_date(
                        merge.get("publication_date")
                        or merge.get("from_event_date")
                    ),
                    "doi": extract_doi(merge),
                    "display": merge.get("display"),
                    "invited": merge.get("invited"),
                    "raw": merge,
                }
            )
    return records


def load_site_records(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        pubs = json.load(f)
    records = []
    for pub in pubs:
        doi = (pub.get("doi") or "").lower().strip()
        if doi.lower().startswith("doi:"):
            doi = doi[4:].strip()
        records.append(
            {
                "id": pub["id"],
                "title": pub.get("title", ""),
                "authors": pub.get("authors", ""),
                "category": pub.get("category", ""),
                "publication_info": pub.get("publication_info", ""),
                "date": parse_date(pub.get("publication_date")),
                "doi": doi,
                "raw_text": pub.get("raw_text", ""),
                "raw": pub,
            }
        )
    return records


def build_indexes(records: list[dict], prefix: str) -> tuple[dict, dict]:
    by_doi: dict[str, list[dict]] = defaultdict(list)
    by_title: dict[str, list[dict]] = defaultdict(list)
    for rec in records:
        if rec.get("doi"):
            by_doi[rec["doi"]].append(rec)
        norm = normalize_text(rec["title"])
        if norm:
            by_title[norm].append(rec)
    return by_doi, by_title


def find_match(
    rec: dict,
    by_doi: dict[str, list[dict]],
    by_title: dict[str, list[dict]],
    used_ids: set,
) -> dict | None:
    if rec.get("doi"):
        for cand in by_doi.get(rec["doi"], []):
            key = cand.get("id") or cand.get("rm_id")
            if key not in used_ids:
                return cand
    norm = normalize_text(rec["title"])
    for cand in by_title.get(norm, []):
        key = cand.get("id") or cand.get("rm_id")
        if key not in used_ids:
            return cand
    return None


def field_diffs(rm: dict, site: dict) -> list[str]:
    diffs = []
    if rm["category_guess"] != site["category"] and rm["category_guess"] != "Presentations (non-invited)":
        diffs.append(f"category: RM `{rm['category_guess']}` vs site `{site['category']}`")
    if normalize_text(rm["authors"]) != normalize_text(site["authors"]):
        diffs.append(f"authors: RM `{rm['authors']}` vs site `{site['authors']}`")
    if rm.get("date") and site.get("date") and rm["date"][:7] != site["date"][:7]:
        diffs.append(f"date: RM `{rm['date']}` vs site `{site['date']}`")
    if rm.get("publication_info") and site.get("publication_info"):
        if normalize_text(rm["publication_info"]) != normalize_text(site["publication_info"]):
            diffs.append(
                f"publication_info: RM `{rm['publication_info']}` vs site `{site['publication_info']}`"
            )
    if rm.get("doi") and site.get("doi") and rm["doi"] != site["doi"]:
        diffs.append(f"doi: RM `{rm['doi']}` vs site `{site['doi']}`")
    return diffs


def format_record_bullet(rec: dict, source: str) -> str:
    if source == "rm":
        return (
            f"- **{rec['title']}** (`rm:{rec['rm_type']}:{rec['rm_id']}`)\n"
            f"  - category (guess): {rec['category_guess']}\n"
            f"  - authors: {rec['authors'] or '—'}\n"
            f"  - date: {rec['date'] or '—'}\n"
            f"  - publication_info: {rec['publication_info'] or '—'}\n"
            f"  - doi: {rec['doi'] or '—'}"
        )
    return (
        f"- **{rec['title']}** (`site:id={rec['id']}`)\n"
        f"  - category: {rec['category']}\n"
        f"  - authors: {rec['authors'] or '—'}\n"
        f"  - date: {rec['date'] or '—'}\n"
        f"  - publication_info: {rec['publication_info'] or '—'}\n"
        f"  - doi: {rec['doi'] or '—'}\n"
        f"  - raw_text: {rec['raw_text']}"
    )


def main() -> None:
    rm_records = load_researchmap_records(JSONL_PATH)
    site_records = load_site_records(PUBS_PATH)

    rm_by_doi, rm_by_title = build_indexes(rm_records, "rm")
    site_by_doi, site_by_title = build_indexes(site_records, "site")

    matched_pairs: list[tuple[dict, dict, list[str]]] = []
    only_rm: list[dict] = []
    only_site: list[dict] = []
    used_site_ids: set[int] = set()
    used_rm_ids: set[str] = set()

    for rm in rm_records:
        site = find_match(rm, site_by_doi, site_by_title, used_site_ids)
        if site:
            used_site_ids.add(site["id"])
            used_rm_ids.add(rm["rm_id"])
            diffs = field_diffs(rm, site)
            matched_pairs.append((rm, site, diffs))
        else:
            only_rm.append(rm)

    for site in site_records:
        if site["id"] not in used_site_ids:
            only_site.append(site)

    diff_pairs = [p for p in matched_pairs if p[2]]
    clean_pairs = [p for p in matched_pairs if not p[2]]

    lines = [
        "# Researchmap vs publications.json 差分レポート",
        "",
        f"生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## 概要",
        "",
        f"| 項目 | 件数 |",
        f"|------|------|",
        f"| researchmap（業績系レコード） | {len(rm_records)} |",
        f"| publications.json | {len(site_records)} |",
        f"| マッチ（タイトル/DOI） | {len(matched_pairs)} |",
        f"| マッチかつフィールド差分あり | {len(diff_pairs)} |",
        f"| researchmap のみ | {len(only_rm)} |",
        f"| publications.json のみ | {len(only_site)} |",
        "",
        "## マッピング方針",
        "",
        "- `published_papers.scientific_journal` → Journal Papers",
        "- `published_papers.international_conference_proceedings` → International Conference Proceedings",
        "- `published_papers.research_society` → Domestic Conference Proceedings",
        "- `misc.summary_*` → Domestic / International Conference Proceedings",
        "- `misc`（misc_type なし）→ Misc.",
        "- `books_etc` → Books",
        "- `presentations`（invited 等）→ Invited Talks and Tutorials",
        "- マッチングキー: DOI 優先、なければ正規化タイトル",
        "",
    ]

    def section(title: str, items: list[str]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not items:
            lines.append("_（なし）_")
            lines.append("")
            return
        lines.extend(items)
        lines.append("")

    by_cat_rm = defaultdict(list)
    for rec in only_rm:
        by_cat_rm[rec["category_guess"]].append(rec)
    only_rm_lines = []
    for cat in sorted(by_cat_rm):
        only_rm_lines.append(f"### {cat} ({len(by_cat_rm[cat])})")
        only_rm_lines.append("")
        for rec in sorted(by_cat_rm[cat], key=lambda r: r.get("date") or "", reverse=True):
            only_rm_lines.append(format_record_bullet(rec, "rm"))
            only_rm_lines.append("")
    section(f"researchmap のみ（{len(only_rm)} 件）", only_rm_lines)

    by_cat_site = defaultdict(list)
    for rec in only_site:
        by_cat_site[rec["category"]].append(rec)
    only_site_lines = []
    for cat in sorted(by_cat_site):
        only_site_lines.append(f"### {cat} ({len(by_cat_site[cat])})")
        only_site_lines.append("")
        for rec in sorted(by_cat_site[cat], key=lambda r: r.get("date") or "", reverse=True):
            only_site_lines.append(format_record_bullet(rec, "site"))
            only_site_lines.append("")
    section(f"publications.json のみ（{len(only_site)} 件）", only_site_lines)

    diff_lines = []
    for rm, site, diffs in sorted(
        diff_pairs,
        key=lambda p: p[1].get("date") or "",
        reverse=True,
    ):
        diff_lines.append(f"### {site['title']}")
        diff_lines.append("")
        diff_lines.append(f"- site `id={site['id']}` / researchmap `{rm['rm_type']}:{rm['rm_id']}`")
        diff_lines.append("")
        for d in diffs:
            diff_lines.append(f"- {d}")
        diff_lines.append("")
    section(f"マッチしたが差分あり（{len(diff_pairs)} 件）", diff_lines)

    lines.append("## 補足")
    lines.append("")
    lines.append(
        f"- 一致とみなしたがフィールド差分なし: {len(clean_pairs)} 件（本レポートでは省略）"
    )
    lines.append(
        "- `presentations` の非招待発表はサイト側カテゴリと1対1で対応しない場合があります"
    )
    lines.append(
        "- researchmap の `misc`（misc_type なし）は雑誌寄稿・学会活動報告などが混在します"
    )
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {REPORT_PATH}")
    print(
        f"rm={len(rm_records)} site={len(site_records)} "
        f"only_rm={len(only_rm)} only_site={len(only_site)} diffs={len(diff_pairs)}"
    )


if __name__ == "__main__":
    main()
