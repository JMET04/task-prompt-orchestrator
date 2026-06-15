# AI Full-Domain Activation Directory

Use this as the front door when the user wants an AI all-domain skill/workflow system, beginner-friendly AI control, prompt/workflow routing, capability selection, plugin installation support, or low-token activation of the right prompt area.

This directory exists to keep activation cheap. Do not load the full workflow dimension index or many workflow matrices for an ordinary task. Classify the user's intent first, then read the smallest exact reference that can move the task forward.

## Mission

Help a beginner or non-specialist control AI precisely by routing their goal into:

- the right existing capability: skill, plugin, connector, visible tool, MCP/app ability, local script, or bundled reference
- the smallest suitable workflow: beginner loop, professional matrix, plugin directory, or prompt pattern
- an execution-ready prompt packet with inputs, outputs, constraints, safety boundary, and verification

Image2 is one important creative-generation domain. It is not the center of the system unless the user explicitly asks for image, visual, rendering, CAD, or packaging generation.

## Activation Tiers

For a quick first-pass route without loading more reference text, run:

```bash
scripts/route_ai_workflow.py "<user request>"
```

For a beginner-friendly activation packet with required inputs, output contract, safety boundary, verification, and a copyable prompt, run:

```bash
scripts/route_ai_workflow.py "<user request>" --packet
```

For a human-readable packet, run:

```bash
scripts/route_ai_workflow.py "<user request>" --packet --format markdown
```

Use the result as a shortlist, then verify with the selected reference or visible capability.

For beginner-facing work, prefer `ai_beginner_starter_packs.md` for ready-to-run prompt packs. Use `ai_beginner_workflows.md` when the user wants to learn the underlying method.

After changing routes, starter packs, or front-door links, run:

```bash
scripts/validate_activation_surface.py --json
```

| Tier | Use when | Read next | Stop when |
|---|---|---|---|
| T0 Quick route | The request is simple or the domain is obvious. | This file only, plus visible session capabilities. | You can produce a prompt packet or execute directly. |
| T1 Target index | The request needs routing but not full expansion. | One target reference from the map below. | You have the exact workflow, plugin candidate, or prompt zone. |
| T2 Workflow matrix | The task is professional, high-stakes, repeatable, or multi-step. | One exact `professional_workflow_*_matrix.md` file, rarely two. | You have workflow code, steps, acceptance checks, and boundaries. |
| T3 Coverage audit | The user asks to design, audit, expand, or measure the whole library. | `professional_workflow_dimension_index.md` and validator outputs. | Coverage, gaps, and counts are verified. |

## Capability-First Pass

Before inventing a workflow, check:

1. Visible skills and plugin-provided skills in the current session.
2. Visible tools, MCP/app tools, and dynamic tool discovery when available.
3. Local helper scripts such as `scripts/capability_inventory.py`.
4. Bundled references and exact workflow matrices.
5. Plugin install candidates only when the user explicitly asked to use or install a missing plugin.

Use `common_plugin_directory.md` for broad sparse-plugin routing. Use `github_codex_common_plugin_directory.md` for GitHub, Codex, OpenAI, repository, coding, security, delivery, and automation plugin decisions.

## Domain Route Map

| User intent signal | Prompt/workflow zone | Read next |
|---|---|---|
| "I don't know how to ask AI", "teach me", "help a beginner", "make my AI workflow better" | Beginner AI control | `ai_beginner_starter_packs.md`, then `ai_beginner_workflows.md` if teaching the method |
| "choose the right plugin", "scan installed skills", "install missing capability", "plugins are few" | Capability and plugin routing | `professional_workflow_capability_discovery_matrix.md`, `professional_workflow_plugin_skill_scan_auto_install_matrix.md`, `common_plugin_directory.md` |
| GitHub, Codex, OpenAI API, Agents SDK, repo, PR, CI, security review, developer workflow | GitHub/Codex/OpenAI plugin directory | `github_codex_common_plugin_directory.md` |
| Code, app build, bug fix, frontend/backend, tests, local repo implementation | Code/app build workflow | `professional_workflow_testing_simulation_matrix.md`, `professional_workflow_release_distribution_matrix.md`, `github_codex_common_plugin_directory.md` |
| "make this prompt professional", "build prompt library", "template", "prompt packet" | Prompt engineering and reusable templates | `professional_prompt_pattern_matrix.md`, then `prompt_templates.md` if needed |
| Image2, visual generation, packaging, CAD drawing, design asset, media generation | Creative/image/multimodal production | `professional_workflow_brand_creative_design_asset_production_matrix.md`, relevant CAD/design references, and image/media skills or plugins if available |
| Coding, app building, agent tools, automation runner, tool calls, RAG, evals, model ops | AI application and agentic systems | `professional_workflow_ai_llm_application_model_ops_matrix.md`, `professional_workflow_agentic_automation_tool_governance_matrix.md` |
| Web/app UI, frontend, deployment, browser testing | App build and delivery | Relevant build/deploy skills or plugins, plus coding workflow matrices when needed |
| Research, source-backed answer, citations, market/competitive/literature analysis | Research and evidence synthesis | `professional_workflow_source_evidence_matrix.md`, `professional_workflow_research_analysis_knowledge_synthesis_matrix.md` |
| Spreadsheet, dataset, KPI, dashboard, BI, semantic layer, analytics report | Data and analytics | `professional_workflow_data_lifecycle_retention_matrix.md`, `professional_workflow_data_product_bi_semantic_governance_matrix.md` |
| Writing, documents, slides, email, meeting notes, office output | Knowledge work and document production | `ai_beginner_workflows.md` W04/W08, then exact document/presentation/spreadsheet skill if available |
| Product, marketing, sales, customer success, business strategy | Business growth workflows | Product, GTM, sales, customer-success, content, or brand workflow matrices |
| Legal, compliance, finance, tax, health, safety, immigration, regulated decision | High-stakes boundary workflow | Exact legal/compliance/finance/personal admin matrix plus source/evidence routing |
| Personal life admin, household, records, travel, benefits, donations, family logistics | Personal workflow systems | Exact personal `professional_workflow_personal_*_matrix.md` file |
| Education, tutoring, training, learning plan, study workflow | Learning and training | `ai_beginner_workflows.md` W10, then education/training matrices |
| Project management, operations, vendor, release, incident, QA, standards | Execution governance | Exact project/operations/vendor/release/testing/standards matrix |
| "expand coverage", "how complete is this", "index everything", "audit workflows" | Library coverage and architecture | `professional_workflow_dimension_index.md`, then `scripts/validate_workflow_library.py` |
| Exact route is unclear after this front door | Detailed route fallback | `detailed_template_routing_directory.md`, then one exact target reference |

## Beginner Control Loop

For beginners, translate the request into this compact loop:

```text
Goal:
Context:
Inputs:
Task:
Output format:
Constraints:
Examples:
Tool/skill/plugin route:
Verification:
Next iteration:
```

Show only the next 1-3 actions unless the user asks for the full system. Prefer a reusable prompt packet over a long theory explanation.

## Activation Packet

Use this packet before execution when routing matters:

```text
User intent:
Skill/tool/plugin already available:
Activation tier:
Read next:
Target workflow(s):
Prompt zone:
Required inputs:
Output contract:
Safety/authority boundary:
Verification:
Fallback:
```

If the request is direct and low-risk, keep the packet internal and execute. If the task is broad, high-stakes, or the user asked for workflow design, show the packet briefly before action.

## Plugin Sparse-Session Rule

When the user has few plugins installed or says Codex should install missing capabilities:

1. Inspect current session plugins, skills, visible tools, apps, and MCP abilities.
2. Search dynamic tools for the exact named capability when available.
3. Run `scripts/capability_inventory.py --include-common-plugin-directory` when local skill/cache coverage matters.
4. Read `common_plugin_directory.md` for broad routing.
5. Read `github_codex_common_plugin_directory.md` for GitHub/Codex/OpenAI engineering decisions.
6. Check install candidates only when the user explicitly asked to use or install the missing plugin.
7. Request installation only for an exact match, then re-scan before using it.

Never silently install a broad profile, claim private access before a callable connector is visible, or replace the platform consent/authentication gate.

## Directory Design Rule

Keep this file as the small front door. Keep `SKILL.md` as the orchestration contract. Keep domain-specific indexes and workflow matrices in `references/`, and load them only after the intent is classified.

Future physical restructuring can shard `references/` into domain folders, but the current low-cost path is logical routing:

```text
SKILL.md
-> ai_full_domain_activation_directory.md
-> one target plugin directory, beginner workflow, prompt pattern, or exact professional matrix
-> execution packet and verification
```
