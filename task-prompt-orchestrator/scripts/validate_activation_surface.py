#!/usr/bin/env python3
"""Validate low-cost activation routes, starter packs, and front-door links."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any


def default_skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_router(skill_root: Path) -> Any:
    router_path = skill_root / "scripts" / "route_ai_workflow.py"
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("route_ai_workflow", router_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load router script: {router_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def markdown_slug(heading: str) -> str:
    text = heading.strip().lower()
    text = re.sub(r"[^\w\u4e00-\u9fff\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def markdown_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            anchors.add(markdown_slug(match.group(2)))
    return anchors


def resolve_reference(skill_root: Path, ref: str) -> tuple[Path, str | None]:
    path_part, _, anchor = ref.partition("#")
    path = Path(path_part)
    if not path.is_absolute():
        path = skill_root / path_part
    return path, anchor or None


def validate_reference(skill_root: Path, ref: str, anchor_cache: dict[Path, set[str]]) -> list[str]:
    errors: list[str] = []
    path, anchor = resolve_reference(skill_root, ref)
    if not path.exists():
        errors.append(f"missing reference path: {ref}")
        return errors
    if anchor:
        if path.suffix.lower() != ".md":
            errors.append(f"anchor on non-markdown reference: {ref}")
            return errors
        if path not in anchor_cache:
            anchor_cache[path] = markdown_anchors(path)
        if anchor not in anchor_cache[path]:
            errors.append(f"missing markdown anchor: {ref}")
    return errors


def validate(skill_root: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}
    router = load_router(skill_root)

    routes = list(router.ROUTES)
    starter_packs = list(router.STARTER_PACKS)
    route_ids = [route.id for route in routes]
    starter_ids = [pack.id for pack in starter_packs]

    if len(route_ids) != len(set(route_ids)):
        errors.append("duplicate route ids")
    if len(starter_ids) != len(set(starter_ids)):
        errors.append("duplicate starter pack ids")

    for route in routes:
        if not route.read_next:
            warnings.append(f"route has no read_next: {route.id}")
        for ref in route.read_next:
            errors.extend(validate_reference(skill_root, ref, anchor_cache))

    for pack in starter_packs:
        errors.extend(validate_reference(skill_root, pack.read_next, anchor_cache))

    starter_file = skill_root / "references" / "ai_beginner_starter_packs.md"
    if starter_file.exists():
        starter_text = starter_file.read_text(encoding="utf-8")
        for pack in starter_packs:
            if f"## {pack.id} " not in starter_text:
                errors.append(f"starter pack section missing: {pack.id}")
    else:
        errors.append("missing starter pack file: references/ai_beginner_starter_packs.md")

    required_mentions = {
        "SKILL.md": [
            "references/ai_full_domain_activation_directory.md",
            "scripts/route_ai_workflow.py",
            "references/ai_beginner_starter_packs.md",
            "references/detailed_template_routing_directory.md",
        ],
        "references/ai_full_domain_activation_directory.md": [
            "scripts/route_ai_workflow.py",
            "ai_beginner_starter_packs.md",
            "github_codex_common_plugin_directory.md",
        ],
    }
    for rel_path, needles in required_mentions.items():
        path = skill_root / rel_path
        if not path.exists():
            errors.append(f"missing required activation file: {rel_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                errors.append(f"{rel_path} does not mention {needle}")

    regression_path = skill_root / "scripts" / "activation_route_regression_cases.json"
    regression_count = 0
    if regression_path.exists():
        cases = json.loads(regression_path.read_text(encoding="utf-8"))
        for case in cases:
            regression_count += 1
            packets = router.suggest_with_packets(case["query"], int(case.get("top", 3)))
            if not packets:
                errors.append(f"regression produced no packets: {case['name']}")
                continue
            first = packets[0]
            if "expected_first_route" in case and first["route_id"] != case["expected_first_route"]:
                errors.append(
                    f"regression {case['name']} first route {first['route_id']} != {case['expected_first_route']}"
                )
            first_starter = first["starter_pack"]["id"]
            if "expected_first_starter" in case and first_starter != case["expected_first_starter"]:
                errors.append(
                    f"regression {case['name']} first starter {first_starter} != {case['expected_first_starter']}"
                )
            if "expected_any_route" in case:
                route_ids = {packet["route_id"] for packet in packets}
                if case["expected_any_route"] not in route_ids:
                    errors.append(
                        f"regression {case['name']} missing route {case['expected_any_route']} in {sorted(route_ids)}"
                    )
    else:
        warnings.append("missing activation route regression cases")

    return {
        "ok": not errors,
        "route_count": len(routes),
        "starter_pack_count": len(starter_packs),
        "regression_count": regression_count,
        "checked_anchor_files": len(anchor_cache),
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate task-prompt-orchestrator low-cost activation surface.")
    parser.add_argument("--skill-root", default=str(default_skill_root()), help="Path to task-prompt-orchestrator.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    result = validate(Path(args.skill_root))
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"ok={result['ok']} routes={result['route_count']} starter_packs={result['starter_pack_count']}")
        for error in result["errors"]:
            print(f"ERROR: {error}")
        for warning in result["warnings"]:
            print(f"WARNING: {warning}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
