#!/usr/bin/env python3
"""Validate the professional workflow library indexes.

Checks global structured-code uniqueness, workflow matrix counts, optional
expected totals, and the dimension index assembly-order sequence.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CODE_RE = re.compile(r"^[A-Z][A-Z0-9-]*(?:\d{2}|\d{2}\.\d+)$")
ASSEMBLY_RE = re.compile(r"^(\d+)\. \*\*")


def default_skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def collect_codes(files: list[Path]) -> tuple[dict[str, list[tuple[str, int]]], dict[str, int]]:
    locations: dict[str, list[tuple[str, int]]] = {}
    per_file: dict[str, int] = {}
    for path in files:
        count = 0
        for line_no, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
            if not line.startswith("|"):
                continue
            parts = [part.strip() for part in line.strip().strip("|").split("|")]
            if not parts or parts[0].lower() in {"code", "subcode", "---"}:
                continue
            if CODE_RE.match(parts[0]):
                count += 1
                locations.setdefault(parts[0], []).append((path.name, line_no))
        per_file[path.name] = count
    return locations, per_file


def read_assembly_order(index_path: Path) -> list[int]:
    nums: list[int] = []
    in_section = False
    for line in index_path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("## Recommended Assembly Order"):
            in_section = True
            continue
        if in_section and line.startswith("## Minimal Workflow Packet"):
            break
        match = ASSEMBLY_RE.match(line)
        if in_section and match:
            nums.append(int(match.group(1)))
    return nums


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate task-prompt-orchestrator workflow library integrity.")
    parser.add_argument("--skill-root", default=str(default_skill_root()), help="Path to task-prompt-orchestrator.")
    parser.add_argument("--production-index", default=r"D:/image2专业提示词库/indexes/IMAGE2_PRODUCTION_SCENARIO_INDEX.md")
    parser.add_argument("--expect-workflow-matrices", type=int)
    parser.add_argument("--expect-workflow-codes", type=int)
    parser.add_argument("--expect-total-codes", type=int)
    parser.add_argument("--expect-assembly-max", type=int)
    parser.add_argument("--json", action="store_true", help="Print JSON summary.")
    args = parser.parse_args()

    skill_root = Path(args.skill_root)
    references = skill_root / "references"
    production_index = Path(args.production_index)
    files = sorted(references.glob("professional_*_matrix.md"))
    if production_index.exists():
        files.append(production_index)

    locations, per_file = collect_codes(files)
    duplicates = {code: places for code, places in locations.items() if len(places) > 1}
    workflow_files = [
        path for path in sorted(references.glob("professional_workflow_*_matrix.md"))
        if path.name != "professional_workflow_library.md"
    ]
    workflow_codes = sum(per_file.get(path.name, 0) for path in workflow_files)
    total_codes = sum(per_file.values())
    assembly = read_assembly_order(references / "professional_workflow_dimension_index.md")
    expected_assembly = list(range(1, (args.expect_assembly_max or (max(assembly) if assembly else 0)) + 1))

    errors: list[str] = []
    if duplicates:
        sample = {code: places for code, places in list(duplicates.items())[:20]}
        errors.append(f"duplicate codes found: {sample}")
    if args.expect_workflow_matrices is not None and len(workflow_files) != args.expect_workflow_matrices:
        errors.append(f"workflow matrix count {len(workflow_files)} != expected {args.expect_workflow_matrices}")
    if args.expect_workflow_codes is not None and workflow_codes != args.expect_workflow_codes:
        errors.append(f"workflow code count {workflow_codes} != expected {args.expect_workflow_codes}")
    if args.expect_total_codes is not None and total_codes != args.expect_total_codes:
        errors.append(f"total code count {total_codes} != expected {args.expect_total_codes}")
    if expected_assembly and assembly != expected_assembly:
        errors.append(
            "assembly order is not contiguous: "
            f"got_start={assembly[:5]} got_end={assembly[-5:]} expected_end={expected_assembly[-5:]}"
        )

    summary = {
        "workflow_matrices": len(workflow_files),
        "workflow_codes": workflow_codes,
        "total_codes": total_codes,
        "duplicate_codes": len(duplicates),
        "assembly_count": len(assembly),
        "assembly_max": max(assembly) if assembly else 0,
        "ok": not errors,
        "errors": errors,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        for key, value in summary.items():
            if key != "errors":
                print(f"{key}: {value}")
        if errors:
            print("errors:")
            for error in errors:
                print(f"- {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
