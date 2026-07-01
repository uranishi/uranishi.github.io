#!/usr/bin/env python3
"""Generate Jekyll Scholar BibTeX from the publications master file."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB_PATH = ROOT / "_bibliography" / "papers.bib"
JSON_PATH = ROOT / "_data" / "publications.json"
STATS_PATH = ROOT / "_data" / "publication_stats.json"

CATEGORY_TYPE = {
    "Books": ("book", "BOOK"),
    "Journal Papers": ("article", "JOUR"),
    "Invited Talks and Tutorials": ("misc", "TALK"),
    "International Conference Proceedings": ("inproceedings", "INTL"),
    "International Conference Proceedings (Reviewed)": ("inproceedings", "INTL"),
    "International Conference Proceedings (Not Reviewed)": ("inproceedings", "INTL"),
    "Domestic Conference Proceedings": ("inproceedings", "DOM"),
    "Domestic Conference Proceedings (Reviewed)": ("inproceedings", "DOM"),
    "Domestic Conference Proceedings (Not Reviewed)": ("inproceedings", "DOM"),
    "Misc.": ("misc", "MISC"),
}


def parse_date(value) -> datetime | None:
    if not value:
        return None
    if isinstance(value, datetime):
        return value
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def sort_publications(items: list[dict]) -> list[dict]:
    return sorted(
        items,
        key=lambda item: parse_date(item.get("publication_date")) or datetime.min,
        reverse=True,
    )


def bib_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")


def normalize_authors(authors: str) -> str:
    text = authors.strip()
    text = text.replace(" and ", " __AND__ ")
    text = text.replace(", ", " and ")
    return text.replace(" __AND__ ", " and ")


def make_key(item: dict) -> str:
    pub_date = parse_date(item.get("publication_date"))
    year = pub_date.year if pub_date else "nodate"
    return f"uranishi{year}{item.get('id', 0):04d}"


def entry_type_and_abbr(category: str | None) -> tuple[str, str]:
    if not category:
        return "misc", "MISC"
    for name, value in CATEGORY_TYPE.items():
        if name in category:
            return value
    return "misc", "MISC"


def format_pages(start_page: str | None, end_page: str | None) -> str | None:
    if not start_page:
        return None
    if end_page and end_page != start_page:
        return f"{start_page}--{end_page}"
    return start_page


def build_bibtex_entry(item: dict, selected: bool = False) -> list[str]:
    entry_type, abbr = entry_type_and_abbr(item.get("category"))
    key = make_key(item)
    lines = [f"@{entry_type}{{{key},"]

    if item.get("title"):
        lines.append(f"  title = {{{bib_escape(item['title'])}}},")
    if item.get("authors"):
        lines.append(f"  author = {{{normalize_authors(item['authors'])}}},")

    publication_info = item.get("publication_info")
    if publication_info:
        if entry_type == "article":
            lines.append(f"  journal = {{{bib_escape(publication_info)}}},")
        elif entry_type == "book":
            lines.append(f"  publisher = {{{bib_escape(publication_info)}}},")
        elif entry_type == "inproceedings":
            lines.append(f"  booktitle = {{{bib_escape(publication_info)}}},")
        else:
            lines.append(f"  howpublished = {{{bib_escape(publication_info)}}},")

    if item.get("venue"):
        if entry_type == "inproceedings":
            lines.append(f"  address = {{{bib_escape(item['venue'])}}},")
        elif entry_type == "misc" and not item.get("additional_info"):
            lines.append(f"  note = {{{bib_escape(item['venue'])}}},")

    if item.get("volume"):
        lines.append(f"  volume = {{{item['volume']}}},")
    if item.get("number"):
        lines.append(f"  number = {{{item['number']}}},")

    pages = format_pages(item.get("start_page"), item.get("end_page"))
    if pages:
        lines.append(f"  pages = {{{pages}}},")

    pub_date = parse_date(item.get("publication_date"))
    if pub_date:
        lines.append(f"  year = {{{pub_date.year}}},")
        lines.append(f"  month = {{{pub_date.month}}},")

    if item.get("doi"):
        doi = str(item["doi"]).strip()
        if doi.lower().startswith("doi:"):
            doi = doi[4:].strip()
        if doi:
            lines.append(f"  doi = {{{doi}}},")

    if item.get("additional_info"):
        lines.append(f"  note = {{{bib_escape(item['additional_info'])}}},")

    if item.get("award"):
        lines.append(f"  award = {{{bib_escape(str(item['award']))}}},")
    if item.get("award_name"):
        lines.append(f"  award_name = {{{bib_escape(str(item['award_name']))}}},")

    lines.append(f"  abbr = {{{abbr}}},")
    if selected:
        lines.append("  selected = {true},")

    lines.append("}")
    return lines


def choose_selected_ids(items: list[dict], limit: int = 6) -> set[int]:
    explicit = {item["id"] for item in items if item.get("selected")}
    if explicit:
        return explicit

    journal = [
        item
        for item in items
        if item.get("category") == "Journal Papers" and item.get("doi")
    ]
    journal.sort(
        key=lambda item: parse_date(item.get("publication_date")) or datetime.min,
        reverse=True,
    )
    return {item["id"] for item in journal[:limit]}


def build_stats(items: list[dict]) -> dict:
    by_abbr: Counter[str] = Counter()
    by_year: Counter[str] = Counter()
    for item in items:
        _, abbr = entry_type_and_abbr(item.get("category"))
        by_abbr[abbr] += 1
        pub_date = parse_date(item.get("publication_date"))
        if pub_date:
            by_year[str(pub_date.year)] += 1
    years_desc = sorted(by_year.keys(), key=int, reverse=True)
    return {
        "total": len(items),
        "by_abbr": dict(sorted(by_abbr.items())),
        "by_year": dict(sorted(by_year.items(), key=lambda pair: int(pair[0]), reverse=True)),
        "years_desc": years_desc,
    }


def export_bibtex(items: list[dict], selected_ids: set[int]) -> str:
    header = [
        "% Auto-generated from _data/publications.json",
        "% Edit the JSON master file, then run: python3 bin/export_publications.py",
        "",
    ]
    body: list[str] = []
    for item in sort_publications(items):
        body.extend(build_bibtex_entry(item, selected=item["id"] in selected_ids))
        body.append("")
    return "\n".join(header + body)


def export_stats(items: list[dict]) -> None:
    STATS_PATH.write_text(
        json.dumps(build_stats(items), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def load_master(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON array")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate _bibliography/papers.bib from _data/publications.json"
    )
    parser.add_argument(
        "--input",
        default=str(JSON_PATH),
        help="Publications master JSON file (default: _data/publications.json)",
    )
    args = parser.parse_args()

    json_path = Path(args.input)
    if not json_path.exists():
        print(f"Master file not found: {json_path}", file=sys.stderr)
        return 1
    items = load_master(json_path)

    selected_ids = choose_selected_ids(items)
    bib = export_bibtex(items, selected_ids)

    BIB_PATH.parent.mkdir(parents=True, exist_ok=True)
    BIB_PATH.write_text(bib, encoding="utf-8")
    export_stats(items)
    print(f"Wrote {len(items)} entries to {BIB_PATH}")
    print(f"Wrote publication stats to {STATS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
