#!/usr/bin/env python3
"""Deterministic evidence/claim hygiene checks for Markdown research reports.

No network calls and no third-party dependencies. Semantic entailment still
requires a human/reviewer reading the cited source.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

URL_RE = re.compile(r"https?://[^\s)\]>"']+")
CITE_RE = re.compile(r"\[(?:S|R|REF)?\d+\]")
STRONG_RE = re.compile(
    r"(必须|一定|永远|绝对|唯一|只能|所有|任何|业界标准|最佳实践|普遍|"
    r"保证|消除|防止|完全解决|已经解决|industry standard|best practice|"
    r"guarantee|always|never)",
    re.IGNORECASE,
)
NUMBER_RE = re.compile(r"(?<![A-Za-z])\d+(?:\.\d+)?%?|\$\d+(?:\.\d+)?")
FRESHNESS_RE = re.compile(
    r"(当前|最新|目前|GA|Preview|deprecated|supported|recommended|pricing)",
    re.IGNORECASE,
)
BOUNDARY_PATTERNS = {
    "RAG_vs_entitlement": re.compile(r"RAG.{0,40}(权限|entitlement|authorization)", re.I),
    "memory_vs_business_truth": re.compile(r"(memory|记忆).{0,40}(business truth|业务真相|权威)", re.I),
    "prompt_vs_security": re.compile(r"(prompt|提示词).{0,40}(安全边界|security boundary|authorization)", re.I),
    "tool_vs_permission": re.compile(r"(tool|工具).{0,40}(permission|权限|授权)", re.I),
    "GA_vs_maturity": re.compile(r"GA.{0,40}(成熟|maturity|生产)", re.I),
    "benchmark_vs_production": re.compile(r"benchmark.{0,40}(production|生产)", re.I),
}

def urls(text: str) -> list[str]:
    return [u.rstrip(".,;") for u in URL_RE.findall(text)]

def citation_ids(text: str) -> list[str]:
    return CITE_RE.findall(text)

def source_section_lines(lines: list[str]) -> tuple[int | None, int]:
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^#{1,6}\s+(sources|参考资料|来源|references)\s*$", line, re.I):
            start = i
            break
    if start is None:
        return None, len(lines)
    return start, len(lines)

def audit(path: Path, strict: bool) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    all_urls = urls(text)
    cites = citation_ids(text)

    errors: list[str] = []
    warnings: list[str] = []
    findings: list[dict] = []

    if re.search(r"\]\(\s*\)", text):
        errors.append("empty Markdown link target found")

    duplicate_urls = sorted({u for u in all_urls if all_urls.count(u) > 1})
    if duplicate_urls:
        warnings.append(f"duplicate source URLs: {len(duplicate_urls)}")

    sources_start, _ = source_section_lines(lines)
    if sources_start is None and (all_urls or cites):
        warnings.append("no explicit Sources/References section detected")

    for idx, line in enumerate(lines, 1):
        if STRONG_RE.search(line):
            findings.append({
                "line": idx,
                "kind": "strong_wording",
                "text": line.strip(),
            })

        if NUMBER_RE.search(line) and (URL_RE.search(line) is None and not CITE_RE.search(line)):
            warnings.append(f"numeric claim without obvious citation on line {idx}")

        if FRESHNESS_RE.search(line) and URL_RE.search(line) is None and not CITE_RE.search(line):
            warnings.append(f"freshness-sensitive wording without obvious citation on line {idx}")

        for name, pattern in BOUNDARY_PATTERNS.items():
            if pattern.search(line):
                findings.append({
                    "line": idx,
                    "kind": "architecture_boundary_warning",
                    "rule": name,
                    "text": line.strip(),
                })

    # Citation IDs cannot be fully validated without a source registry, but we
    # can catch the common mismatch where ids are used but no Sources section exists.
    if cites and sources_start is None:
        errors.append("citation IDs are present but no Sources/References section was found")

    # If the report uses [S1]-style IDs, report ids for a human semantic audit.
    result = {
        "file": str(path),
        "ok": not errors and (not strict or not warnings),
        "errors": errors,
        "warnings": warnings,
        "citation_count": len(cites),
        "citation_ids": sorted(set(cites)),
        "url_count": len(all_urls),
        "unique_url_count": len(set(all_urls)),
        "findings": findings,
    }
    return result

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    results = []
    code = 0
    for path in args.files:
        if not path.exists():
            results.append({"file": str(path), "ok": False, "errors": ["file not found"], "warnings": []})
            code = 2
            continue
        result = audit(path, args.strict)
        results.append(result)
        if not result["ok"]:
            code = 1

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
            for item in result["findings"][:10]:
                print(f"  FINDING: {item}")
        print(f"checked={len(results)}")

    return code

if __name__ == "__main__":
    raise SystemExit(main())
