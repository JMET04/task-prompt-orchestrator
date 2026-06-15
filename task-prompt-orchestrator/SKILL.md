---
name: task-prompt-orchestrator
description: Intake messy or detailed user goals, collect the needed input information, scan installed skills/plugins/tools, select the best professional workflow, improve the prompt before execution, split the task into executable prompt packets, and hand the packets to execution with verification. Use when the user asks to plan-and-execute, turn a vague request into a workflow, build a repeatable prompting pipeline, orchestrate multiple subtasks, improve prompts before execution, teach beginners to control AI, route an AI all-domain skill/workflow request with low token cost, generate a professional deliverable, scan available plugins/skills, auto-install or recommend common GitHub/Codex/OpenAI plugins when sparse, or quickly route a task to an expert workflow, especially for prompt-library, image2, design, research, coding, document, data, marketing, automation, legal, finance, compliance, product, business, education, or review tasks.
---

# Task Prompt Orchestrator

## Core Contract

Turn a user request into an execution-ready workflow:

0. Scan existing usable capabilities first: installed skills, enabled plugins/connectors, visible tools, MCP/app abilities, local scripts, and bundled references.
1. Collect or infer the minimum input information needed to execute well.
2. Clarify only blocking unknowns.
3. Rewrite the user request into a sharper execution brief.
4. Select the best professional workflow pattern before writing prompts.
5. Split the brief into small executable steps.
6. Select or compose a high-quality prompt template for each step.
7. Hand each step to execution with inputs, output shape, tools, dependencies, and verification.
8. Teach a beginner-friendly workflow when the user is learning AI or lacks process.
9. Execute when the user requested action, not only planning.

Use this skill as an orchestration layer. Do not replace specialized skills; route to them when a step clearly matches an existing skill or tool.

Capability-first rule: before inventing a workflow or generic prompt, check whether an installed skill, plugin, connector, visible tool, MCP/app capability, local script, index, or bundled reference already solves the job. Use `scripts/capability_inventory.py` for local skill inventory, use current session tool/plugin context for session-scoped abilities, then record selected capability, rejected alternatives, limits, fallback, and validation evidence when the workflow is reusable or high stakes.

Low-cost activation rule: for broad AI-control, beginner workflow, prompt-system, plugin-selection, or all-domain routing requests, start with `references/ai_full_domain_activation_directory.md`, then load only the smallest exact index, plugin directory, or workflow matrix needed for the active task. Treat image2 as one creative-generation domain inside the broader AI workflow system unless the user explicitly asks for image/image2 work.

## Workflow

### 1. Intake

Identify:

- final deliverable
- user-provided inputs and files
- constraints, deadlines, style, format, and quality bar
- known reusable assets, skills, tools, indexes, or prompt libraries
- blockers that would make execution risky or impossible

If the user gave enough context, proceed. Ask at most 1-3 short questions only when a missing answer changes the output materially.

### 1A. Input Information Contract

Before planning, normalize whatever the user gave into this compact intake shape. Do this internally unless the workflow artifact itself needs to show it:

```text
Goal:
Raw user request:
Inputs supplied: files, folders, links, screenshots, examples, data, code, prior outputs
Workspace state: cwd, repo, relevant local scripts, existing artifacts
Capability state: installed skills, plugins/connectors, MCP/app tools, CLI tools, missing useful tools
Output target: file, repo, image, document, dashboard, code change, prompt packet, decision, or handoff
Constraints: format, style, scope, budget, deadline, policy, safety, compliance, language
Acceptance checks: tests, validation commands, visual review, citations, counts, links, user-visible proof
Execution permissions: whether to execute, install, browse, create repos, push, deploy, or only plan
Open questions: only blockers that materially change the output
Assumptions:
```

For plugin/skill discovery tasks, explicitly record what is installed, what is callable in the current session, what can be installed, and which capability should be used first. If the user has few plugins installed and asks for a task that would benefit from common GitHub, Codex, OpenAI, data, browser, design, or deployment plugins, read `references/github_codex_common_plugin_directory.md` and propose or install only exact matches allowed by the current tool policy.

### 2. Optimized Brief

Before execution, restate the request as a precise brief:

```text
Goal:
Inputs:
Audience / use case:
Constraints:
Output format:
Quality bar:
Execution mode:
```

Keep this brief short. It is the source of truth for downstream step prompts.

### 3. Task Breakdown

Break work into atomic steps. Each step must have:

- `id`: stable short id, such as `S1`
- `purpose`: why this step exists
- `inputs`: exact files, data, user facts, or prior outputs needed
- `action`: one executable action
- `prompt_template`: selected template name or custom template
- `output`: concrete artifact or decision
- `done_when`: observable completion condition
- `handoff`: what the next step receives

Prefer 3-9 steps for normal tasks. Use more only when the work has genuinely separate deliverables.

### 4. Template Selection

Read `references/prompt_templates.md` when composing prompts for more than one step, when the domain is unclear, or when no stronger project-local template is already loaded.

Template routing:

- AI full-domain activation front door: read `references/ai_full_domain_activation_directory.md` first for AI all-domain skills/workflows, beginner AI control, prompt/workflow routing, low-cost activation, directory optimization, capability selection, sparse-plugin sessions, or choosing the smallest workflow/prompt area to load.
- Fast route helper: run `scripts/route_ai_workflow.py "<user request>"` when a short user request needs a quick first-pass route before loading reference files. Add `--packet` when the user is a beginner or needs a copyable activation packet, and add `--format markdown` when the packet should be shown directly to a human. Treat the result as a shortlist, then verify against the chosen reference or visible capability.
- Activation surface validator: run `scripts/validate_activation_surface.py --json` after changing `route_ai_workflow.py`, `ai_beginner_starter_packs.md`, `ai_full_domain_activation_directory.md`, or low-cost routing links, so route references, starter-pack anchors, and front-door mentions stay intact.
- Capability and plugin routing: use `references/professional_workflow_capability_discovery_matrix.md`, `references/professional_workflow_plugin_skill_scan_auto_install_matrix.md`, `references/common_plugin_directory.md`, and `references/github_codex_common_plugin_directory.md` when the task needs installed skill/plugin/tool discovery, exact plugin selection, or GitHub/Codex/OpenAI engineering capability.
- Professional coverage routing: use `references/professional_workflow_library.md` for a professional domain workflow, `references/professional_workflow_dimension_index.md` for broad design/audit/coverage work, and one exact `references/professional_workflow_*_matrix.md` file for a selected domain.
- Prompt and artifact routing: use `references/professional_prompt_pattern_matrix.md`, `references/professional_task_operation_matrix.md`, `references/professional_input_material_matrix.md`, `references/professional_media_deliverable_matrix.md`, `references/professional_audience_context_matrix.md`, `references/professional_constraint_context_matrix.md`, and `references/professional_verification_acceptance_matrix.md` when the route depends on prompt shape, operation, source material, deliverable, audience, constraints, or acceptance checks.
- Beginner AI onboarding: read `references/ai_beginner_starter_packs.md` for ready-to-run prompt packs, or `references/ai_beginner_workflows.md` when teaching the underlying workflow loop.
- Image2 / visual generation: inspect `D:\image2专业提示词库\indexes\IMAGE2_VERTICAL_PROMPT_INDEX.md`, then the relevant file in `D:\image2专业提示词库\prompts\`. For packaging, CAD, engineering drawings, manufacturing callouts, or industrial design, also inspect `D:\image2专业提示词库\indexes\IMAGE2_PRODUCTION_SCENARIO_INDEX.md`.
- Detailed route fallback: read `references/detailed_template_routing_directory.md` only when the short menu above is insufficient or when maintaining exact legacy route coverage.

If an excellent domain template exists locally, adapt it instead of inventing a generic prompt.

### 5. Prompt Packet

For each step, produce or internally use a prompt packet:

```text
Step ID:
Role:
Objective:
Context:
Inputs:
Procedure:
Output format:
Constraints:
Quality checks:
Handoff:
```

The packet must be specific enough that another agent, tool, or later turn can execute it without rediscovering the whole problem.

### 6. Execution

After generating the workflow, execute it unless the user explicitly asked only for a plan.

- Run independent discovery or file-read steps in parallel when safe.
- Keep the visible plan current for multi-step work.
- Use specialized tools/skills for each step rather than manually simulating them.
- Preserve user changes and current project state.
- Verify each deliverable against its `done_when` before marking the step complete.

### 7. Final Handoff

Finish with:

- what was created or changed
- where the outputs live
- which steps were executed
- what was verified
- remaining gaps, if any

If the workflow itself is the requested deliverable, provide the task breakdown and prompt packets in a copyable format.

## Quality Rules

- Do not make a vague plan. Every step needs an executable action and a testable output.
- Do not write prompts before choosing the workflow. The workflow determines which context, tools, checks, and outputs are needed.
- Do not use one generic prompt for all steps. Match the prompt to the step's domain.
- Do not ask for clarification when a reasonable, low-risk assumption lets work continue.
- Do not stop at prompt optimization when the user asked for execution.
- Do not claim completion until current evidence proves the deliverable exists and passes its checks.
- For beginners, reduce cognitive load: choose one workflow, show the next action, and provide a reusable prompt packet rather than a theory dump.
