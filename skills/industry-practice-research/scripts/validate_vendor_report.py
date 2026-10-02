#!/usr/bin/env python3
"""Deterministic checks for industry-practice research reports.

No third-party dependencies. This script checks document structure and obvious
source/citation hygiene. It does NOT judge semantic correctness.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

URL_RE = re.compile(r"https?://[^\s)\]>"']+")
STRONG_RE = re.compile(
    r"(行业标准|最佳实践|普遍|所有|必须|一定|唯一|保证|完全解决|已经解决|"
    r"best practice|industry standard|always|never|guarantee)",
    re.IGNORECASE,
)
DATE_RE = re.compile(r"(研究日期|research cutoff|cutoff|202\d-\d\d-\d\d)", re.IGNORECASE)

CORE_GROUPS = {
    "problem_or_conclusion": ["结论", "problem", "business meaning"],
    "abstraction": ["抽象", "abstraction", "semantic", "ontology"],
    "representation": ["保存", "representation", "storage", "持久"],
    "retrieval": ["检索", "retrieval", "access", "search"],
    "runtime": ["runtime", "运行时", "context"],
    "governance": ["governance", "权限", "permission", "entitlement"],
    "lifecycle": ["lifecycle", "freshness", "provenance", "版本"],
    "limitations": ["limitation", "限制", "边界"],
    "sources": ["sources", "官方资料", "参考资料", "source"],
}

def load(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def heading_text(text: str) -> list[str]:
    return [m.group(2).strip().lower() for m in re.finditer(r"^(#{1,6})\s+(.+)$", text, re.M)]

def urls(text: str) -> list[str]:
    return URL_RE.findall(text)

def check_one(path: Path, strict: bool) -> dict:
    text = load(path)
    lower = text.lower()
    headings = heading_text(text)
    all_urls = urls(text)

    errors: list[str] = []
    warnings: list[str] = []
    checks: dict[str, bool] = {}

    checks["has_title"] = bool(re.search(r"^#\s+", text, re.M))
    checks["has_research_date_or_cutoff"] = bool(DATE_RE.search(text))
    checks["has_sources"] = any(any(term in h for term in CORE_GROUPS["sources"]) for h in headings)
    checks["has_limitations"] = any(any(term in h for term in CORE_GROUPS["limitations"]) for h in headings)

    for name, terms in CORE_GROUPS.items():
        if name in {"problem_or_conclusion", "sources", "limitations"}:
            continue
        checks[f"has_{name}"] = any(any(term in h for term in terms) for h in headings)

    if not checks["has_title"]:
        errors.append("missing top-level title")
    if not checks["has_research_date_or_cutoff"]:
        warnings.append("missing explicit research date/cutoff")
    if not checks["has_sources"]:
        errors.append("missing a Sources/reference section")
    if not checks["has_limitations"]:
        warnings.append("missing explicit limitations/boundary section")

    for key in (
        "has_abstraction",
        "has_representation",
        "has_retrieval",
        "has_runtime",
        "has_governance",
        "has_lifecycle",
    ):
        if not checks.get(key, False):
            warnings.append(f"missing expected research dimension: {key.removeprefix('has_')}")

    duplicates = sorted({u for u in all_urls if all_urls.count(u) > 1})
    if duplicates:
        warnings.append(f"duplicate URLs: {len(duplicates)}")

    malformed = []
    for u in all_urls:
        parsed = urlparse(u.rstrip(".,;"))
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            malformed.append(u)
    if malformed:
        errors.append(f"malformed URLs: {len(malformed)}")

    strong_lines = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if STRONG_RE.search(line) and URL_RE.search(line) is None and "[" not in line:
            strong_lines.append(line_no)
    if strong_lines:
        warnings.append(
            "strong industry/generalization wording without an obvious inline citation "
            f"on lines: {strong_lines[:12]}"
        )

    result = {
        "file": str(path),
        "ok": not errors and (not strict or not warnings),
        "errors": errors,
        "warnings": warnings,
        "url_count": len(all_urls),
        "unique_url_count": len(set(all_urls)),
        "checks": checks,
    }
    return result

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    results = []
    exit_code = 0
    for path in args.files:
        if not path.exists():
            results.append({"file": str(path), "ok": False, "errors": ["file not found"], "warnings": []})
            exit_code = 2
            continue
        result = check_one(path, args.strict)
        results.append(result)
        if not result["ok"]:
            exit_code = 1

    if args.json:
        print(json.dumps({"results": results}, ensure_ascii=False, indent=2))
    else:
        for result in results:
            status = "PASS" if result["ok"] else "FAIL"
            print(f"[{status}] {result['file']}")
            for item in result["errors"]:
                print(f"  ERROR: {item}")
            for item in result["warnings"]:
                print(f"  WARN:  {item}")
        print(f"checked={len(results)}")

    return exit_code

if __name__ == "__main__":
    raise SystemExit(main())
