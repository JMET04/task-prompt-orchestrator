# Task Prompt Orchestrator

`task-prompt-orchestrator` is a Codex skill for turning messy user requests into execution-ready workflows. It collects the task inputs, scans available skills/plugins/tools, selects the smallest useful professional workflow, improves prompts before execution, emits prompt packets, and verifies outputs.

## What It Does

- Normalizes user goals, files, links, constraints, workspace state, and acceptance checks into a compact intake packet.
- Scans installed skills, plugins, MCP/app tools, CLI tools, local scripts, and bundled references before inventing a new workflow.
- Routes broad AI, prompt-library, image2, research, coding, document, data, marketing, automation, legal, finance, compliance, product, business, education, and review tasks.
- Supports capability/plugin discovery, including sparse-plugin sessions and GitHub/Codex/OpenAI common-plugin routing.
- Produces step-level prompt packets with role, objective, inputs, procedure, output shape, constraints, checks, and handoff.
- Executes when the user asked for action, and verifies deliverables before claiming completion.

## Install

Copy the skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force ".\task-prompt-orchestrator" "$env:USERPROFILE\.codex\skills\task-prompt-orchestrator"
```

Then restart or refresh Codex so the skill list is reloaded.

## Use

Example prompt:

```text
Use $task-prompt-orchestrator to collect my goal, inputs, constraints, available skills/plugins, and acceptance checks, then route it through the smallest useful workflow and execute or produce prompt packets.
```

## Package Layout

```text
task-prompt-orchestrator/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
```

The skill folder intentionally contains only skill-runtime files. Repository-level docs live outside the skill folder.

## Validation

From this repository root:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\task-prompt-orchestrator"
python ".\task-prompt-orchestrator\scripts\validate_activation_surface.py" --json
python ".\task-prompt-orchestrator\scripts\route_ai_workflow.py" "扫描已安装插件和skill，推荐GitHub和Codex常用插件并生成工作流" --packet --top 2 --format markdown
```

Expected high-level result:

- `Skill is valid`
- activation surface returns `"ok": true`
- route output includes `capability-plugin-routing` and `github-codex-openai`

## Latest Intake Update

This version improves the skill's receiving/intake behavior:

- Adds an explicit `Input Information Contract`.
- Records supplied files, folders, links, screenshots, examples, prior outputs, workspace state, capability state, output target, constraints, acceptance checks, execution permissions, assumptions, and blocking questions.
- Strengthens plugin/skill discovery and common GitHub/Codex/OpenAI plugin routing.
- Updates `agents/openai.yaml` so the UI default prompt asks for goal, inputs, constraints, available skills/plugins, and acceptance checks.

