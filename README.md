# Task Prompt Orchestrator

`task-prompt-orchestrator` is a Codex skill for turning messy user requests into execution-ready workflows. It collects the task inputs, scans available skills/plugins/tools, selects the smallest useful professional workflow, improves prompts before execution, emits prompt packets, and verifies outputs.

![Task Prompt Orchestrator promotional poster](promo/task-prompt-orchestrator-poster-cn.png)

## 中文介绍

这个 skill 是一个低 token 消耗的任务提示词编排入口。它把用户随口说出的需求，转化成可执行、可验证、可交接的专业工作流。

它不会每次把完整提示词库读进上下文，而是先收集用户目标、输入材料、约束、可用插件/skill/工具和验收标准，再通过索引、脚本和专业矩阵选择最小可用工作流。它更像 Codex 的任务调度台：先扫描能力，再选择最小索引，最后生成专业提示词包并完成验收。

完整中文说明位于：

```text
task-prompt-orchestrator/references/chinese_introduction.md
```

其中包括 skill 功能定位、适用场景、任务接收信息结构、capability-first 能力扫描、prompt packet 工作流拆分、渐进式披露实现原理、索引优先策略、脚本快速路由，以及为什么不会每次读取完整提示词库。

宣传海报和 image2 生成提示词位于：

```text
promo/task-prompt-orchestrator-poster-cn.png
promo/poster_prompt.md
```

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
    chinese_introduction.md
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

## Latest Chinese Introduction Update

This version adds a detailed Chinese introduction explaining what the skill does, how it works internally, and how the low-token progressive-disclosure design avoids reading the full prompt library on every run.

## Latest Poster Update

This version adds a Chinese promotional poster generated through the image2 poster/KV workflow. The visual background was generated without readable fake text, then real Chinese copy was overlaid locally for clean typography.
