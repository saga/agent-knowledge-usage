#!/usr/bin/env python3
"""Validate a paper registry using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

YEAR_RE = re.compile(r"^(19|20)\d{2}$")
REQUIRED = ("title", "year", "abstract_url", "pdf_url", "category", "relevance")
STATUS_VALUES = {"preprint", "published", "unknown", "retracted", "withdrawn"}


def load_records(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        records = payload
    elif isinstance(payload, dict) and isinstance(payload.get("papers"), list):
        records = payload["papers"]
    else:
        raise ValueError("registry must be a JSON list or an object with a 'papers' list")
    if not all(isinstance(item, dict) for item in records):
        raise ValueError("every registry entry must be a JSON object")
    return records


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def run(path: Path, strict: bool) -> tuple[dict, int]:
    try:
        records = load_records(path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return {"file": str(path), "ok": False, "errors": [str(exc)], "warnings": []}, 2

    errors: list[str] = []
    warnings: list[str] = []
    id_seen: dict[str, int] = {}
    title_seen: dict[str, list[int]] = defaultdict(list)
    category_counts = Counter()
    status_counts = Counter()
    duplicate_orders: list[tuple[str, str, int]] = []

    for index, item in enumerate(records, 1):
        for field in REQUIRED:
            value = item.get(field)
            if value is None or (isinstance(value, str) and not value.strip()):
                errors.append(f"entry {index}: missing required field '{field}'")

        title = str(item.get("title", "")).strip()
        if title:
            title_seen[normalize_title(title)].append(index)

        year = str(item.get("year", "")).strip()
        if year and not YEAR_RE.fullmatch(year):
            errors.append(f"entry {index}: invalid year '{year}'")

        for field in ("abstract_url", "pdf_url"):
            value = str(item.get(field, "")).strip()
            if value and not valid_url(value):
                errors.append(f"entry {index}: invalid {field} URL")

        category = str(item.get("category", "")).strip()
        directory = str(item.get("directory", "")).strip()
        if category:
            category_counts[category] += 1

        arxiv_id = str(item.get("arxiv_id", "")).strip().lower()
        doi = str(item.get("doi", "")).strip().lower()
        for label, identifier in (("arxiv_id", arxiv_id), ("doi", doi)):
            if identifier:
                key = f"{label}:{identifier}"
                if key in id_seen:
                    errors.append(
                        f"entry {index}: duplicate {label} also used by entry {id_seen[key]}"
                    )
                else:
                    id_seen[key] = index

        if not str(item.get("authors", "")).strip():
            warnings.append(f"entry {index}: authors is empty")

        status = str(item.get("status", "unknown")).strip().lower() or "unknown"
        if status not in STATUS_VALUES:
            errors.append(f"entry {index}: unsupported status '{status}'")
        status_counts[status] += 1

        order = item.get("order")
        if directory and order is not None:
            duplicate_orders.append((directory, str(order), index))

    for normalized_title, indexes in title_seen.items():
        if normalized_title and len(indexes) > 1:
            warnings.append(f"duplicate normalized title across entries: {indexes}")

    order_seen: dict[tuple[str, str], int] = {}
    for directory, order, index in duplicate_orders:
        key = (directory, order)
        if key in order_seen:
            errors.append(
                f"duplicate order '{order}' in directory '{directory}' at entries "
                f"{order_seen[key]} and {index}"
            )
        else:
            order_seen[key] = index

    result = {
        "file": str(path),
        "ok": not errors and (not strict or not warnings),
        "entries": len(records),
        "errors": errors,
        "warnings": warnings,
        "categories": dict(category_counts),
        "statuses": dict(status_counts),
        "unique_identifier_count": len(id_seen),
    }
    return result, 1 if not result["ok"] else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    result, code = run(args.registry, args.strict)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"[{'PASS' if result.get('ok') else 'FAIL'}] {result.get('file')}")
        print(f"entries={result.get('entries', 0)}")
        for item in result.get("errors", []):
            print(f"  ERROR: {item}")
        for item in result.get("warnings", []):
            print(f"  WARN:  {item}")
        if result.get("categories"):
            print(f"categories={len(result['categories'])}")
        if result.get("statuses"):
            print(f"statuses={result['statuses']}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
