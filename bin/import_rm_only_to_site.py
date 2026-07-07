#!/usr/bin/env python3
"""Add review-approved RM-only records to _data/publications.json."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSONL_PATH = ROOT / "rm_researchers20260707.jsonl"
PUBS_PATH = ROOT / "_data" / "publications.json"
STATE_PATH = ROOT / "ja_researcher" / "review_state.json"
QUEUE_PATH = ROOT / "ja_researcher" / "review_queue.json"
REPORT_PATH = ROOT / "ja_researcher" / "rm_only_site_import.json"

# RM titles that already exist on the site (near-duplicate / same work).
SKIP_REVIEW_IDS = {
    "R0091",
    "R0105",
    "R0116",
    "R0117",
    "R0118",
    "R0147",
    "R0156",
    "R0163",
}

CATEGORY_ID = {
    "Books": 1,
    "Journal Papers": 2,
    "Invited Talks and Tutorials": 3,
    "International Conference Proceedings": 4,
    "Domestic Conference Proceedings": 5,
    "Misc.": 6,
}

RM_GUESS_TO_SITE = {
    "Journal Papers": "Journal Papers",
    "International Conference Proceedings": "International Conference Proceedings",
    "Domestic Conference Proceedings": "Domestic Conference Proceedings",
    "Invited Talks and Tutorials": "Invited Talks and Tutorials",
    "Misc.": "Misc.",
    "Books": "Books",
    "Presentations (non-invited)": "International Conference Proceedings",
    "RM:published_papers": "International Conference Proceedings",
}

PUBLISHED_TYPE_TO_SITE = {
    "scientific_journal": "Journal Papers",
    "international_conference_proceedings": "International Conference Proceedings",
    "research_society": "Domestic Conference Proceedings",
}

_spec = importlib.util.spec_from_file_location(
    "compare_researchmap", ROOT / "bin" / "compare_researchmap.py"
)
compare = importlib.util.module_from_spec(_spec)
sys.modules["compare_researchmap"] = compare
_spec.loader.exec_module(compare)


def load_json(path: Path) -> dict | list:
    return json.loads(path.read_text(encoding="utf-8"))


def site_category_for_item(
    review_id: str,
    queue_item: dict,
    rm_record: dict,
    state: dict,
) -> str:
    override = state.get("category_overrides", {}).get(review_id, {})
    if override.get("site_category"):
        return override["site_category"]

    guess = queue_item.get("rm_category_guess", "")
    if guess == "RM:published_papers":
        paper_type = rm_record.get("raw", {}).get("published_paper_type")
        return PUBLISHED_TYPE_TO_SITE.get(paper_type, "International Conference Proceedings")
    return RM_GUESS_TO_SITE.get(guess, "Misc.")


def pick_title(merge: dict, rm_type: str, overrides: dict) -> str:
    if overrides.get("タイトル(日本語)"):
        return overrides["タイトル(日本語)"]
    if overrides.get("タイトル(英語)"):
        return overrides["タイトル(英語)"]
    if rm_type == "presentations":
        key = "presentation_title"
    elif rm_type == "books_etc":
        key = "book_title"
    else:
        key = "paper_title"
    title_obj = merge.get(key, {})
    if isinstance(title_obj, dict):
        return (title_obj.get("ja") or title_obj.get("en") or "").strip()
    return str(title_obj or "").strip()


def pick_authors(merge: dict, rm_type: str, overrides: dict) -> str:
    if overrides.get("著者(日本語)"):
        return overrides["著者(日本語)"]
    if overrides.get("著者(英語)"):
        return overrides["著者(英語)"]
    if rm_type == "presentations":
        for key in ("presenters", "presenters_text", "authors"):
            if key in merge:
                if key == "presenters_text":
                    return compare.pick_localized(merge[key])
                return compare.pick_people(merge[key])
        return ""
    return compare.pick_people(merge.get("authors"))


def pick_publication_info(merge: dict, rm_type: str, overrides: dict) -> str:
    if overrides.get("誌名(日本語)"):
        return overrides["誌名(日本語)"]
    if overrides.get("誌名(英語)"):
        return overrides["誌名(英語)"]
    if overrides.get("会議名(日本語)"):
        return overrides["会議名(日本語)"]
    if overrides.get("会議名(英語)"):
        return overrides["会議名(英語)"]
    if rm_type == "presentations":
        return compare.pick_localized(merge.get("event"))
    if rm_type == "books_etc":
        return compare.pick_localized(merge.get("publisher"))
    return compare.pick_localized(merge.get("publication_name"))


def pick_venue(merge: dict, rm_type: str) -> str:
    if rm_type == "presentations":
        return compare.pick_localized(merge.get("event_place"))
    return ""


def clean_page(value: str | None) -> str:
    if not value:
        return ""
    text = str(value).strip()
    text = re.sub(r"^pp?\.?\s*", "", text, flags=re.IGNORECASE)
    return text


def to_site_datetime(value: str | None) -> str:
    parsed = compare.parse_date(value)
    if not parsed:
        return ""
    if len(parsed) == 4:
        return f"{parsed}-01-01T00:00:00"
    if len(parsed) == 7:
        return f"{parsed}-01T00:00:00"
    return f"{parsed}T00:00:00"


def format_date_label(value: str | None) -> str:
    parsed = compare.parse_date(value)
    if not parsed:
        return ""
    if len(parsed) == 4:
        return parsed
    year, month = parsed.split("-")
    return f"{year}.{int(month)}"


def join_authors_for_raw(authors: str, category: str) -> str:
    parts = [a.strip() for a in authors.split(",") if a.strip()]
    if not parts:
        return ""
    if category in {"International Conference Proceedings", "Journal Papers"}:
        if len(parts) == 1:
            return parts[0]
        return ", ".join(parts[:-1]) + " and " + parts[-1]
    return ", ".join(parts)


def build_raw_text(entry: dict) -> str:
    authors = join_authors_for_raw(entry["authors"], entry["category"])
    title = entry["title"]
    info = entry.get("publication_info", "")
    date = format_date_label(entry.get("publication_date"))
    vol = entry.get("volume", "")
    num = entry.get("number", "")
    sp = entry.get("start_page", "")
    ep = entry.get("end_page", "")
    venue = entry.get("venue", "")
    doi = entry.get("doi", "")
    extra = entry.get("additional_info", "")

    category = entry["category"]
    if category == "Journal Papers":
        parts = [f'{authors}, "{title}", {info}']
        if vol:
            parts.append(f"Vol.{vol}")
        if num:
            parts.append(f"No.{num}")
        if sp:
            pages = f"pp.{sp}-{ep}" if ep and ep != sp else f"p.{sp}"
            parts.append(pages)
        if date:
            parts.append(f"({date})")
        text = ", ".join(parts)
        if doi:
            text += f" DOI: {doi}"
        return text

    if category == "International Conference Proceedings":
        parts = [f'{authors}, "{title}", {info}']
        if sp:
            pages = f"pp. {sp}-{ep}" if ep and ep != sp else f"p. {sp}"
            parts.append(pages)
        if venue:
            parts.append(venue)
        if date:
            parts.append(f"({date})")
        return ", ".join(parts)

    if category == "Domestic Conference Proceedings":
        parts = [f'{authors}, "{title}", {info}']
        if extra:
            parts.append(extra)
        if venue:
            parts.append(venue)
        if date:
            parts.append(f"({date})")
        return ", ".join(parts)

    if category == "Invited Talks and Tutorials":
        parts = [f'{authors}, "{title}", {info}']
        if date:
            parts.append(f"({date})")
        return ", ".join(parts)

    # Misc.
    parts = [f'{authors}, "{title}", {info}']
    if vol:
        parts.append(f"Vol.{vol}")
    if num:
        parts.append(f"No.{num}")
    if sp:
        pages = f"pp.{sp}-{ep}" if ep and ep != sp else f"p.{sp}"
        parts.append(pages)
    if date:
        parts.append(f"({date})")
    return ", ".join(parts)


def build_entry(
    review_id: str,
    queue_item: dict,
    rm_record: dict,
    state: dict,
    new_id: int,
    now: str,
) -> dict:
    merge = rm_record["raw"]
    rm_type = rm_record["rm_type"]
    pub_overrides = state.get("publication_overrides", {}).get(review_id, {})
    auth_overrides = state.get("author_overrides", {}).get(review_id, {})
    overrides = {**pub_overrides, **auth_overrides}

    category = site_category_for_item(review_id, queue_item, rm_record, state)
    title = pick_title(merge, rm_type, overrides) or queue_item["rm_title"]
    authors = pick_authors(merge, rm_type, overrides) or queue_item.get("rm_authors", "")
    publication_info = (
        pick_publication_info(merge, rm_type, overrides)
        or queue_item.get("rm_publication_info", "")
    )
    pub_date = pub_overrides.get("出版年月") or merge.get("publication_date") or merge.get(
        "from_event_date"
    ) or queue_item.get("rm_date")
    doi = compare.extract_doi(merge) or queue_item.get("rm_doi", "")

    entry = {
        "id": new_id,
        "category_id": CATEGORY_ID[category],
        "category": category,
        "title": title,
        "authors": authors,
        "author_roles": None,
        "publication_info": publication_info,
        "volume": str(pub_overrides.get("巻") or merge.get("volume") or ""),
        "number": str(pub_overrides.get("号") or merge.get("number") or ""),
        "start_page": clean_page(pub_overrides.get("開始ページ") or merge.get("starting_page")),
        "end_page": clean_page(pub_overrides.get("終了ページ") or merge.get("ending_page")),
        "publication_date": to_site_datetime(pub_date),
        "doi": doi,
        "venue": pick_venue(merge, rm_type),
        "venue_date": None,
        "additional_info": None,
        "source_url": "https://www.uranishi.me/publications",
        "created_at": now,
        "updated_at": now,
    }
    entry["raw_text"] = build_raw_text(entry)
    return entry


def collect_candidates(state: dict, queue: dict, rm_by_id: dict) -> tuple[list[dict], list[dict]]:
    queue_by_id = {item["review_id"]: item for item in queue["queue"]}
    to_add = []
    skipped = []

    for review_id, decision in state.get("decisions", {}).items():
        if decision != "yes":
            continue
        item = queue_by_id.get(review_id)
        if not item or item.get("phase") != "rm_only":
            continue
        if review_id in SKIP_REVIEW_IDS:
            skipped.append(
                {
                    "review_id": review_id,
                    "rm_id": item.get("rm_id"),
                    "title": item.get("rm_title"),
                    "reason": "already_on_site_near_duplicate",
                }
            )
            continue
        rm = rm_by_id.get(item["rm_id"])
        if not rm:
            skipped.append(
                {
                    "review_id": review_id,
                    "rm_id": item.get("rm_id"),
                    "title": item.get("rm_title"),
                    "reason": "rm_record_not_found",
                }
            )
            continue
        to_add.append({"review_id": review_id, "queue_item": item, "rm_record": rm})

    to_add.sort(
        key=lambda row: compare.parse_date(row["queue_item"].get("rm_date")) or "",
        reverse=True,
    )
    return to_add, skipped


def main() -> None:
    parser = argparse.ArgumentParser(description="Import RM-only yes records to publications.json")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write publications.json (default: dry-run report only)",
    )
    parser.add_argument(
        "--export-bib",
        action="store_true",
        help="Run bin/export_publications.py after applying",
    )
    args = parser.parse_args()

    state = load_json(STATE_PATH)
    queue = load_json(QUEUE_PATH)
    pubs = load_json(PUBS_PATH)
    rm_by_id = {
        r["rm_id"]: r for r in compare.load_researchmap_records(JSONL_PATH)
    }

    existing_titles = {compare.normalize_text(p["title"]) for p in pubs}
    candidates, skipped = collect_candidates(state, queue, rm_by_id)

    planned = []
    dup_skipped = []
    next_id = max(p["id"] for p in pubs) + 1
    now = datetime.now().isoformat()

    for row in candidates:
        review_id = row["review_id"]
        entry = build_entry(
            review_id,
            row["queue_item"],
            row["rm_record"],
            state,
            next_id,
            now,
        )
        norm_title = compare.normalize_text(entry["title"])
        if norm_title in existing_titles:
            dup_skipped.append(
                {
                    "review_id": review_id,
                    "title": entry["title"],
                    "reason": "title_already_exists",
                }
            )
            continue
        planned.append(
            {
                "review_id": review_id,
                "rm_id": row["queue_item"]["rm_id"],
                "new_id": next_id,
                "category": entry["category"],
                "title": entry["title"],
                "publication_date": entry["publication_date"],
                "entry": entry,
            }
        )
        existing_titles.add(norm_title)
        next_id += 1

    report = {
        "generated_at": now,
        "apply": args.apply,
        "planned_count": len(planned),
        "skipped_review_ids": skipped,
        "skipped_title_duplicates": dup_skipped,
        "planned": [
            {
                "review_id": p["review_id"],
                "rm_id": p["rm_id"],
                "new_id": p["new_id"],
                "category": p["category"],
                "title": p["title"],
                "publication_date": p["publication_date"],
            }
            for p in planned
        ],
    }
    REPORT_PATH.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(json.dumps(report, ensure_ascii=False, indent=2))

    if not args.apply:
        print(f"\nDry-run only. Review {REPORT_PATH} then run with --apply")
        return

    if not planned:
        print("Nothing to add.")
        return

    pubs.extend(p["entry"] for p in planned)
    pubs.sort(
        key=lambda item: compare.parse_date(item.get("publication_date")) or "",
        reverse=True,
    )
    PUBS_PATH.write_text(
        json.dumps(pubs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Wrote {len(planned)} entries to {PUBS_PATH}")

    if args.export_bib:
        import subprocess

        subprocess.run(
            [sys.executable, str(ROOT / "bin" / "export_publications.py")],
            check=True,
        )
        print("Regenerated papers.bib and publication_stats.json")


if __name__ == "__main__":
    main()
