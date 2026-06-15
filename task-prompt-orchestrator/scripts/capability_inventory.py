#!/usr/bin/env python3
"""Export a local capability inventory for workflow routing.

The script scans installed Codex skills on disk and can attach a supplied
session capability note for plugins, connectors, or visible tools that only
exist in the current chat context.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Iterable


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*", re.DOTALL)


def default_roots() -> list[Path]:
    home = Path.home()
    roots = []
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        roots.append(Path(codex_home) / "skills")
    roots.extend(
        [
            home / ".codex" / "skills",
            home / ".codex" / "skills" / ".system",
            home / ".codex" / "plugins" / "cache",
        ]
    )
    seen: set[str] = set()
    unique = []
    for root in roots:
        key = str(root.resolve()) if root.exists() else str(root)
        if key not in seen:
            seen.add(key)
            unique.append(root)
    return unique


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data: dict[str, str] = {}
    lines = match.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" not in line:
            i += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if key not in {"name", "description"}:
            i += 1
            continue
        if value in {"|", "|-", ">", ">-"}:
            block: list[str] = []
            i += 1
            while i < len(lines):
                next_line = lines[i]
                if next_line and not next_line.startswith((" ", "\t")) and ":" in next_line:
                    break
                block.append(next_line.strip())
                i += 1
            joined = "\n".join(block).strip() if value.startswith("|") else " ".join(x for x in block if x).strip()
            data[key] = joined
            continue
        data[key] = value
        i += 1
    return data


def iter_skill_files(roots: Iterable[Path], include_backups: bool = False) -> Iterable[Path]:
    seen: set[Path] = set()
    for root in roots:
        if not root.exists():
            continue
        for skill_file in root.rglob("SKILL.md"):
            if not include_backups and any(part.startswith(".backup") for part in skill_file.parts):
                continue
            resolved = skill_file.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            yield skill_file


def collect_skills(roots: list[Path], query: str | None = None, include_backups: bool = False) -> list[dict[str, str]]:
    q = query.lower() if query else None
    skills = []
    for skill_file in iter_skill_files(roots, include_backups=include_backups):
        try:
            text = skill_file.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            text = skill_file.read_text(encoding="utf-8", errors="replace")
        meta = parse_frontmatter(text)
        name = meta.get("name") or skill_file.parent.name
        description = meta.get("description", "")
        haystack = f"{name}\n{description}\n{skill_file.parent.name}".lower()
        if q and q not in haystack:
            continue
        skills.append(
            {
                "name": name,
                "description": description,
                "path": str(skill_file),
                "root": str(next((r for r in roots if str(skill_file).startswith(str(r))), "")),
            }
        )
    return sorted(skills, key=lambda item: (item["name"].lower(), item["path"].lower()))


def read_json_file(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return {}


def collect_plugin_cache(roots: list[Path], query: str | None = None) -> list[dict[str, str]]:
    q = query.lower() if query else None
    seen: set[Path] = set()
    plugins = []
    for root in roots:
        if not root.exists():
            continue
        for plugin_json in root.rglob(".codex-plugin/plugin.json"):
            plugin_root = plugin_json.parent.parent
            resolved = plugin_root.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            data = read_json_file(plugin_json)
            interface = data.get("interface") if isinstance(data.get("interface"), dict) else {}
            app_data = read_json_file(plugin_root / ".app.json")
            mcp_data = read_json_file(plugin_root / ".mcp.json")
            apps = app_data.get("apps") if isinstance(app_data.get("apps"), dict) else {}
            mcp_servers = mcp_data.get("mcpServers") if isinstance(mcp_data.get("mcpServers"), dict) else {}
            skill_names = []
            skills_dir = plugin_root / "skills"
            if skills_dir.exists():
                for skill_file in skills_dir.glob("*/SKILL.md"):
                    meta = parse_frontmatter(skill_file.read_text(encoding="utf-8-sig", errors="replace"))
                    skill_names.append(meta.get("name") or skill_file.parent.name)
            item = {
                "name": str(data.get("name") or plugin_root.parent.name),
                "display_name": str(interface.get("displayName") or data.get("name") or plugin_root.parent.name),
                "version": str(data.get("version") or ""),
                "description": str(data.get("description") or interface.get("shortDescription") or ""),
                "category": str(interface.get("category") or ""),
                "capabilities": ", ".join(str(x) for x in interface.get("capabilities", []) if x),
                "apps": ", ".join(sorted(apps.keys())),
                "mcp_servers": ", ".join(sorted(mcp_servers.keys())),
                "skill_count": str(len(skill_names)),
                "skills": ", ".join(sorted(skill_names)),
                "path": str(plugin_root),
            }
            haystack = "\n".join(value for key, value in item.items() if key != "path").lower()
            if q and q not in haystack:
                continue
            plugins.append(item)
    return sorted(plugins, key=lambda item: (item["display_name"].lower(), item["path"].lower()))


def render_markdown(
    skills: list[dict[str, str]],
    plugins: list[dict[str, str]],
    session_note: str | None,
    plugin_directory: str | None,
) -> str:
    lines = [
        "# Capability Inventory",
        "",
        f"- Local skills found: {len(skills)}",
        f"- Local plugin cache entries found: {len(plugins)}",
        "- Session plugins/connectors/tools: use current chat context and tool discovery; include supplied notes below when provided.",
        "- Plugin cache entries prove local package presence, not session authentication or callable tool availability.",
        "",
    ]
    if session_note:
        lines.extend(["## Session Capability Notes", "", session_note.strip(), ""])
    if plugin_directory:
        lines.extend(["## Common Plugin Directory", "", plugin_directory.strip(), ""])
    if plugins:
        lines.extend(
            [
                "## Local Plugin Cache",
                "",
                "| Plugin | Version | Category | Capabilities | Apps | MCP servers | Skills | Path |",
                "|---|---|---|---|---|---|---|---|",
            ]
        )
        for item in plugins:
            row = [
                f"`{item['display_name']}`",
                item["version"],
                item["category"],
                item["capabilities"],
                item["apps"],
                item["mcp_servers"],
                item["skill_count"],
                f"`{item['path']}`",
            ]
            lines.append("| " + " | ".join(value.replace("|", "\\|") for value in row) + " |")
        lines.append("")
    lines.extend(["## Installed Skills", "", "| Skill | Description | Path |", "|---|---|---|"])
    for item in skills:
        desc = item["description"].replace("|", "\\|")
        path = item["path"].replace("|", "\\|")
        lines.append(f"| `{item['name']}` | {desc} | `{path}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Export installed skill capabilities for workflow routing.")
    parser.add_argument("--root", action="append", help="Skill root to scan. Can be passed multiple times.")
    parser.add_argument("--query", help="Filter skills by keyword across name, description, and path.")
    parser.add_argument("--session-note", help="Plain text note describing session-visible plugins, connectors, or tools.")
    parser.add_argument("--session-note-file", help="Path to a text file with session-visible capability notes.")
    parser.add_argument(
        "--include-common-plugin-directory",
        action="store_true",
        help="Append the bundled common plugin directory, including GitHub/Codex starter recommendations.",
    )
    parser.add_argument(
        "--no-local-plugin-cache",
        action="store_true",
        help="Do not scan cached local plugin packages.",
    )
    parser.add_argument("--include-backups", action="store_true", help="Include hidden backup skill folders in the scan.")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--output", help="Write output to this path instead of stdout.")
    args = parser.parse_args()

    roots = [Path(p) for p in args.root] if args.root else default_roots()
    session_note = args.session_note
    if args.session_note_file:
        session_note = Path(args.session_note_file).read_text(encoding="utf-8-sig")
    plugin_directory = None
    if args.include_common_plugin_directory:
        directory_path = Path(__file__).resolve().parent.parent / "references" / "common_plugin_directory.md"
        plugin_directory = directory_path.read_text(encoding="utf-8-sig")
        github_codex_path = Path(__file__).resolve().parent.parent / "references" / "github_codex_common_plugin_directory.md"
        if github_codex_path.exists():
            plugin_directory = plugin_directory.rstrip() + "\n\n" + github_codex_path.read_text(encoding="utf-8-sig")
    skills = collect_skills(roots, args.query, include_backups=args.include_backups)
    plugins = [] if args.no_local_plugin_cache else collect_plugin_cache(roots, args.query)

    if args.format == "json":
        payload = {
            "skill_count": len(skills),
            "plugin_cache_count": len(plugins),
            "skills": skills,
            "plugins": plugins,
            "session_note": session_note or "",
            "common_plugin_directory": plugin_directory or "",
        }
        output = json.dumps(payload, ensure_ascii=False, indent=2)
    else:
        output = render_markdown(skills, plugins, session_note, plugin_directory)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
