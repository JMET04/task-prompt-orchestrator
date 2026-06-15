# Professional Workflow Capability Discovery Matrix

Use this matrix when a workflow should first scan available skills, plugins, connectors, MCP tools, local scripts, or built-in platform abilities before inventing a new implementation. The goal is to route work through the strongest existing capability, understand its limits, and leave an auditable capability-use decision.

For common plugin routing and install fallbacks, read `common_plugin_directory.md`. Use it when GitHub, Codex/OpenAI Developers, security, app building, deployment, documents, data, creative production, or research capabilities would materially improve the task. Plugin installation must be request-based: check install candidates only when a needed plugin is missing and the user explicitly asks to use/install it, then request installation only after an exact match.

## Capability Inventory

| Code | Capability question | Workflow use |
|---|---|---|
| CAPINV01 | What skills are installed and relevant to this task? | Build the first candidate list from available skill names, descriptions, and trigger language. |
| CAPINV02 | What plugins or connectors are enabled for this session? | Identify external app, SaaS, market, media, design, data, and workspace capabilities. |
| CAPINV03 | What callable tools are currently exposed? | Map visible tool namespaces, permissions, and execution channels before choosing an action path. |
| CAPINV04 | What local scripts or bundled resources already exist? | Prefer deterministic helper scripts, templates, references, and assets inside existing skills. |
| CAPINV05 | What workspace-specific capabilities are present? | Inspect project conventions, AGENTS instructions, package scripts, CLIs, and local runbooks. |
| CAPINV06 | What browser, web, file, image, or document abilities are available? | Match task media and source type to the strongest built-in or plugin capability. |
| CAPINV07 | What capability depends on authentication or user connection state? | Separate ready-to-use capabilities from installed but unavailable connectors. |
| CAPINV08 | What capability has current-data access? | Route news, prices, schedules, API docs, product specs, and unstable facts through live sources. |
| CAPINV09 | What capability has deterministic validation support? | Prefer validators, linters, tests, schema checkers, and audit scripts when correctness matters. |
| CAPINV10 | What capability inventory evidence should be kept? | Record selected candidates, rejected candidates, and the evidence used for routing. |

## Skill Mapping

| Code | Capability question | Workflow use |
|---|---|---|
| SKILLMAP01 | Which skill directly names this domain or action? | Trigger the most specific skill before using broad generic workflow logic. |
| SKILLMAP02 | Which skill has the clearest usage instructions for this task? | Read the relevant SKILL.md and only the needed referenced resources. |
| SKILLMAP03 | Which skill contains reusable references or matrices? | Use existing indexes, taxonomies, templates, checklists, and example packets. |
| SKILLMAP04 | Which skill contains scripts that reduce repeated manual work? | Run or patch skill scripts instead of retyping fragile code. |
| SKILLMAP05 | Which skill covers the required file format or artifact type? | Route DOCX, spreadsheets, slides, CAD, images, code, data, and dashboards correctly. |
| SKILLMAP06 | Which skill covers the required professional domain? | Pull in domain-specific workflow, evidence, risk, vocabulary, and acceptance criteria. |
| SKILLMAP07 | Which skill is too broad and needs a companion matrix? | Combine broad orchestration skills with domain, IO, risk, or verification matrices. |
| SKILLMAP08 | Which skill should be skipped because it is only adjacent? | Avoid forcing a skill when its scope does not truly fit the user intent. |
| SKILLMAP09 | What skill order should be used when several apply? | Sequence skill reading from governing workflow to domain, artifact, tool, and validation. |
| SKILLMAP10 | What skill gaps should be converted into new reusable material? | Capture missing reusable procedure, script, or reference as a future skill improvement. |

## Plugin And Connector Mapping

| Code | Capability question | Workflow use |
|---|---|---|
| PLUGMAP01 | Which plugin provides the closest production capability? | Prefer the plugin whose purpose matches the task outcome, not just a related keyword. |
| PLUGMAP02 | Which connector can access the user's live workspace data? | Use connected apps for Drive, Gmail, Slack, Jira, Figma, databases, or dashboards when needed. |
| PLUGMAP03 | Which plugin has a skill that should govern the workflow? | Use plugin-provided skills for specialized platform workflows and constraints. |
| PLUGMAP04 | Which plugin exposes MCP tools that should be discovered lazily? | Use tool discovery when a named or implied plugin capability is not yet visible. |
| PLUGMAP05 | Which plugin output needs extra verification? | Add QA when plugin results may be delayed, incomplete, lossy, or presentation-oriented. |
| PLUGMAP06 | Which plugin requires user approval, connection, or install? | Detect when a plugin cannot be used immediately and choose a fallback. |
| PLUGMAP07 | Which plugin is read-only versus action-capable? | Separate information retrieval from editing, publishing, payment, deployment, or account actions. |
| PLUGMAP08 | Which plugin is best for media generation or editing? | Route images, video, audio, stock assets, product shots, and creative polish to the right tool. |
| PLUGMAP09 | Which plugin is best for deployment or app building? | Route web, mobile, database, cloud, and hosting tasks to the strongest platform workflow. |
| PLUGMAP10 | What plugin-use evidence should be recorded? | Keep selected plugin, reason, limits, actions taken, and verification result. |

## Tool Mapping

| Code | Capability question | Workflow use |
|---|---|---|
| TOOLMAP01 | Which visible tool can perform the task most directly? | Choose shell, web, image generation, browser, MCP, or app tools by concrete output need. |
| TOOLMAP02 | Which tool is safer than manual reasoning? | Use deterministic inspection, parsing, validation, finance, weather, sports, or time tools when appropriate. |
| TOOLMAP03 | Which tool should be used before web search? | Prefer local files, MCP resources, official docs, or project state when those are authoritative. |
| TOOLMAP04 | Which tool should be used for live or unstable facts? | Browse or query live APIs for current entities, prices, rules, schedules, and docs. |
| TOOLMAP05 | Which tool has side effects? | Separate read-only inspection from edits, installs, sends, deletes, purchases, or deployments. |
| TOOLMAP06 | Which tool needs a specific channel or syntax? | Respect tool channel, schema, freeform patch, app directive, and permission constraints. |
| TOOLMAP07 | Which tool can validate the final artifact? | Run tests, validators, screenshots, checksums, schema checks, or preview renderers. |
| TOOLMAP08 | Which tool can inspect visual output? | Use screenshots, image viewing, rendered previews, or canvas checks when visuals matter. |
| TOOLMAP09 | Which tool can parallelize safe reads? | Parallelize independent file reads, searches, and inspections to reduce latency. |
| TOOLMAP10 | What tool-use trace should be preserved? | Record commands, key outputs, validation status, and unresolved tool limitations. |

## Trigger Mapping

| Code | Capability question | Workflow use |
|---|---|---|
| TRIGMAP01 | Did the user explicitly name a plugin, skill, tool, or app? | Treat explicit naming as the strongest routing trigger unless impossible. |
| TRIGMAP02 | Did the task match a skill description? | Trigger the matching skill and follow progressive disclosure rules. |
| TRIGMAP03 | Did the task require current information? | Trigger web or live-data tools before answering. |
| TRIGMAP04 | Did the task involve a specific local workspace? | Trigger workspace inspection before generic advice. |
| TRIGMAP05 | Did the task involve editing an existing skill? | Trigger skill-creation/update guidance and validate the skill after changes. |
| TRIGMAP06 | Did the task involve visual generation or editing? | Trigger image/media tooling and visual QA. |
| TRIGMAP07 | Did the task involve documents, sheets, slides, or PDFs? | Trigger document/runtime dependencies and format-specific skills. |
| TRIGMAP08 | Did the task involve app, site, deployment, or code execution? | Trigger build, test, run, preview, and deployment workflows. |
| TRIGMAP09 | Did the task involve regulated, financial, medical, legal, or safety risk? | Trigger high-risk validation and source-backed verification. |
| TRIGMAP10 | Did the task ask for reusable workflow coverage? | Trigger dimension index, capability discovery, governance, and verification matrices. |

## Fit Selection

| Code | Capability question | Workflow use |
|---|---|---|
| FITSEL01 | Which candidate capability has the closest intent match? | Rank by outcome match before convenience or familiarity. |
| FITSEL02 | Which capability has the strongest source authority? | Prefer official docs, local project state, primary datasets, and native tools. |
| FITSEL03 | Which capability minimizes manual reconstruction? | Use tools that preserve structure, metadata, schemas, and provenance. |
| FITSEL04 | Which capability can be verified fastest? | Choose paths that have tests, previews, validation scripts, or deterministic checks. |
| FITSEL05 | Which capability respects user constraints? | Account for budget, time, privacy, offline needs, platform, language, and permissions. |
| FITSEL06 | Which capability handles the required scale? | Check batch size, rate limits, context size, file count, and automation suitability. |
| FITSEL07 | Which capability supports the desired artifact format? | Select tools that produce the actual requested file, prompt, index, app, or report. |
| FITSEL08 | Which capability has acceptable failure impact? | Prefer reversible, low-side-effect routes when uncertainty is high. |
| FITSEL09 | Which capability should be combined with another? | Compose skill plus plugin plus validator when no single capability is complete. |
| FITSEL10 | What fit rationale should be shown to the user? | Briefly explain selected capability, why it fits, and what remains uncertain. |

## Capability Limits

| Code | Capability question | Workflow use |
|---|---|---|
| LIMITS01 | What does this capability explicitly not do? | Avoid overstating plugin, skill, or tool ability. |
| LIMITS02 | What data can the capability not access? | Identify missing files, disconnected apps, private systems, or unavailable APIs. |
| LIMITS03 | What output quality limits are known? | Flag hallucination risk, low resolution, lossy conversion, schema loss, or stale docs. |
| LIMITS04 | What scale or rate limits apply? | Plan chunks, retries, batching, and sampling when volume is high. |
| LIMITS05 | What permission or approval limits apply? | Avoid blocked writes, installs, purchases, account actions, or unsafe side effects. |
| LIMITS06 | What platform or environment limits apply? | Account for OS, shell, local dependencies, browser, runtime, and network constraints. |
| LIMITS07 | What compliance or policy limits apply? | Add human review, citation, privacy, safety, or legal boundaries. |
| LIMITS08 | What reliability limits apply? | Add validation when a tool is beta, delayed, non-deterministic, or external. |
| LIMITS09 | What context-window limits apply? | Use indexes, search, resource routing, and summaries instead of loading everything. |
| LIMITS10 | What limit disclosure should be included? | Tell the user only the limits that affect the decision or final deliverable. |

## Fallback And Extension

| Code | Capability question | Workflow use |
|---|---|---|
| FALLBK01 | What is the best fallback if the ideal tool is unavailable? | Choose local/manual workflow, alternate plugin, official docs, or staged implementation. |
| FALLBK02 | What can be done with current access only? | Produce a partial but useful result with explicit missing data. |
| FALLBK03 | What should be deferred until the user connects or approves something? | Isolate blocked connector, auth, install, or destructive action steps. |
| FALLBK04 | What lightweight extension would unlock the task? | Add a reference file, script, template, index row, or validator when reusable. |
| FALLBK05 | What manual workaround is acceptable for one-off tasks? | Use a scoped manual path when building infrastructure would be wasteful. |
| FALLBK06 | What should not be attempted as a fallback? | Avoid risky scraping, fake tool output, destructive commands, or unsupported actions. |
| FALLBK07 | How should fallback output be labeled? | Mark partial, inferred, stale, unverified, or approximate sections clearly. |
| FALLBK08 | How should fallback be tested? | Validate the workaround with the same acceptance criteria as the primary path where possible. |
| FALLBK09 | When should fallback become a permanent capability? | Convert repeated workaround into skill, script, matrix, or plugin route. |
| FALLBK10 | What fallback decision should be recorded? | Record ideal capability, reason unavailable, chosen fallback, and residual risk. |

## Routing Plan

| Code | Capability question | Workflow use |
|---|---|---|
| ROUTEPLAN01 | What is the minimum capability route for this task? | Avoid overloading the workflow with unnecessary plugins or matrices. |
| ROUTEPLAN02 | What is the complete route for high-stakes work? | Combine discovery, domain, IO, governance, validation, and delivery layers. |
| ROUTEPLAN03 | What order should capabilities be invoked? | Sequence read-only discovery, planning, edits/actions, validation, and reporting. |
| ROUTEPLAN04 | What user clarification is truly required before routing? | Ask only for missing facts that cannot be reasonably inferred or discovered. |
| ROUTEPLAN05 | What prompt should be optimized before execution? | Convert user intent into a precise execution prompt or workflow packet. |
| ROUTEPLAN06 | What route can run in parallel safely? | Parallelize independent inspections and searches while keeping edits sequential. |
| ROUTEPLAN07 | What route needs a stop gate? | Insert user confirmation, human review, or approval before irreversible actions. |
| ROUTEPLAN08 | What route needs provenance capture? | Preserve sources, files, commands, tool outputs, and validation evidence. |
| ROUTEPLAN09 | What route needs resumability? | Save state, next actions, decisions, and checkpoints for long projects. |
| ROUTEPLAN10 | What final route summary should be given? | Report selected capabilities, artifacts changed, validation, and next useful work. |

## Capability Use

| Code | Capability question | Workflow use |
|---|---|---|
| EXECUSE01 | Has the selected skill been read before action? | Follow skill instructions and referenced resources before editing or executing. |
| EXECUSE02 | Has the selected plugin/tool been called with the right schema? | Build payloads from tool docs and app instructions, not guesses. |
| EXECUSE03 | Has the workflow used existing scripts or templates first? | Reduce duplicated code and keep outputs consistent with established patterns. |
| EXECUSE04 | Has execution respected file and git safety rules? | Preserve user changes, avoid destructive commands, and use scoped patches. |
| EXECUSE05 | Has execution respected live-data browsing rules? | Browse when facts may have changed or when the user asks for latest/source-backed detail. |
| EXECUSE06 | Has execution respected media-specific QA? | Inspect generated or edited visual artifacts before claiming success. |
| EXECUSE07 | Has execution respected local project conventions? | Use existing package scripts, tests, formatting, and architecture. |
| EXECUSE08 | Has execution left a usable artifact, not just analysis? | Produce the prompt, index, file, workflow, dashboard, app, or validation result. |
| EXECUSE09 | Has execution captured enough evidence to audit? | Keep key command outputs, counts, file paths, sources, and checks. |
| EXECUSE10 | Has execution avoided capability overreach? | Do not claim plugin access, installs, or actions that were not actually available or performed. |

## Capability Index Maintenance

| Code | Capability question | Workflow use |
|---|---|---|
| CAPINDEX01 | Where should capability knowledge be indexed? | Store durable routing in skill references, workflow indexes, or memory when explicitly asked. |
| CAPINDEX02 | What metadata should each capability entry include? | Capture name, trigger, use case, inputs, outputs, limits, validation, and fallback. |
| CAPINDEX03 | How should duplicate or overlapping capabilities be handled? | Prefer specific tools, mark alternates, and define tie-break rules. |
| CAPINDEX04 | How should stale capability entries be refreshed? | Add review cadence, version checks, and live discovery steps for plugins/tools. |
| CAPINDEX05 | How should newly installed plugins be incorporated? | Re-scan available tools, update routing rows, and add examples when useful. |
| CAPINDEX06 | How should removed or unavailable capabilities be handled? | Mark retired, unavailable, disconnected, or replaced rather than silently ignoring. |
| CAPINDEX07 | How should capability examples be captured? | Save concise successful task patterns, prompts, payload shapes, and validation methods. |
| CAPINDEX08 | How should user preferences affect capability routing? | Preserve user-specified preferred tools, safety boundaries, and workflow style. |
| CAPINDEX09 | How should capability indexes stay small enough to load? | Keep summary rows in the index and detailed instructions in referenced files. |
| CAPINDEX10 | How should index updates be validated? | Run skill validation, count checks, prefix checks, and targeted route checks. |

## Capability Audit

| Code | Capability question | Workflow use |
|---|---|---|
| CAPAUDIT01 | Did the workflow actually check existing capabilities first? | Audit compliance with capability-first execution rules. |
| CAPAUDIT02 | Was the chosen capability the best available fit? | Review rejected alternatives and route rationale. |
| CAPAUDIT03 | Were capability limits disclosed where they mattered? | Ensure the final answer does not hide stale data, missing access, or partial execution. |
| CAPAUDIT04 | Were tool calls or plugin actions verified? | Confirm outputs through tests, previews, source checks, or independent inspection. |
| CAPAUDIT05 | Were user instructions and AGENTS rules respected? | Check clarification, prompt optimization, planning, safety, and workflow-first behavior. |
| CAPAUDIT06 | Were side effects controlled and reversible? | Confirm edits, sends, deletes, deployments, or purchases had proper gates. |
| CAPAUDIT07 | Was evidence preserved for future continuation? | Verify paths, counts, sources, decisions, and next steps are recoverable. |
| CAPAUDIT08 | Did the workflow update reusable knowledge when explicitly requested? | Confirm memory or index updates were made only when allowed. |
| CAPAUDIT09 | Did the workflow avoid inventing unsupported capabilities? | Remove claims about tools, access, or outputs that were not actually present. |
| CAPAUDIT10 | What capability improvement should be proposed next? | Identify the next index, script, skill, or plugin route that would improve future work. |
