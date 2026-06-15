# Professional Workflow Agentic Automation Tool Governance Matrix

Use this matrix when a workflow uses an AI agent, automation runner, tool-calling loop, plugin connector, MCP tool, script, multi-step autonomous execution, or human-in-the-loop approval process. The matrix defines when an agent may act, which tools it may call, how it plans and records state, where humans approve, how side effects are controlled, and how the run is evaluated and audited.

## Agentic Automation Scope

| Code | Workflow question | Workflow use |
|---|---|---|
| AGSCOPE01 | What agentic workflow is in scope? | Define assistant, coding agent, research agent, browser agent, data agent, creative agent, ops automation, or connector workflow. |
| AGSCOPE02 | What business or user outcome should automation produce? | Tie agent work to deliverable, decision, file change, message, deployment, analysis, media asset, or operational action. |
| AGSCOPE03 | What autonomy level is allowed? | Choose advise-only, draft-only, propose actions, execute read-only, execute with approval, or execute bounded side effects. |
| AGSCOPE04 | What environment will the agent operate in? | Capture local filesystem, repo, browser, cloud, SaaS connector, database, design tool, media tool, or production system. |
| AGSCOPE05 | What actor is accountable for the run? | Assign user, agent owner, reviewer, approver, operator, platform owner, data owner, or incident owner. |
| AGSCOPE06 | What tasks are explicitly out of scope? | Block financial transactions, destructive changes, external messages, publishing, credential handling, legal advice, or production actions when not authorized. |
| AGSCOPE07 | What capability baseline exists? | Record visible tools, enabled plugins, installed skills, local scripts, MCP resources, credentials, and fallback routes. |
| AGSCOPE08 | What risk level does automation carry? | Classify low, moderate, high, regulated, irreversible, public-facing, financial, security-sensitive, or reputation-sensitive. |
| AGSCOPE09 | What run artifact is required? | Produce agent run brief, tool plan, approval log, trace, output packet, verification report, or audit summary. |
| AGSCOPE10 | What evidence proves the automation was successful? | Use completed action, validated output, tests, user acceptance, trace integrity, cost report, and no unresolved safety findings. |

## Goal Authorization And Boundaries

| Code | Workflow question | Workflow use |
|---|---|---|
| GOALAUTH01 | What user goal is the agent authorized to pursue? | Restate objective, constraints, deliverables, success criteria, and stopping conditions before acting. |
| GOALAUTH02 | What authority did the user grant? | Distinguish ask, inspect, draft, edit, run, install, send, publish, deploy, purchase, delete, or schedule permissions. |
| GOALAUTH03 | What ambiguity needs clarification before action? | Ask only for missing facts that change risk, scope, external effects, ownership, or acceptance criteria. |
| GOALAUTH04 | What policy or platform rule limits action? | Apply safety, privacy, tool, app, connector, data, copyright, financial, medical, legal, or employment boundaries. |
| GOALAUTH05 | What sensitive data may be used? | Define allowed files, accounts, tokens, private messages, customer data, regulated data, and redaction needs. |
| GOALAUTH06 | What irreversible action is prohibited without approval? | Gate deletes, overwrites, sends, purchases, deployments, permissions, billing, and public publishing. |
| GOALAUTH07 | What time or budget budget bounds the run? | Set token, compute, API, cloud cost, rate limit, elapsed time, and retry limits where relevant. |
| GOALAUTH08 | What external system access must be verified? | Check connection, authentication, account scope, workspace, tenant, repo, project, and read/write ability. |
| GOALAUTH09 | What stop condition should halt the agent? | Stop on uncertainty, repeated failure, missing approval, safety risk, tool limitation, cost limit, or acceptance completion. |
| GOALAUTH10 | What authorization artifact is required? | Produce goal brief, permission map, stop-rule note, clarification log, or approval boundary record. |

## Tool Capability Selection

| Code | Workflow question | Workflow use |
|---|---|---|
| TOOLSEL01 | What tool can perform the next action most directly? | Choose shell, web, browser, image tool, code tool, data tool, connector, plugin, MCP tool, or local script. |
| TOOLSEL02 | What tool is safest for the action? | Prefer read-only, deterministic, scoped, reversible, official, or validator-backed tools over manual or broad actions. |
| TOOLSEL03 | What tool requires discovery before use? | Use lazy tool search for named plugins, MCP tools, app connectors, platform-specific APIs, or hidden capabilities. |
| TOOLSEL04 | What tool has side effects? | Label edit, delete, move, send, publish, install, deploy, purchase, permission, or external-write tools before calling. |
| TOOLSEL05 | What tool input schema must be respected? | Validate arguments, channels, path formats, JSON schema, freeform syntax, authentication, and required fields. |
| TOOLSEL06 | What fallback exists if the preferred tool is unavailable? | Select local CLI, official docs, web source, manual file edit, exported data, or user-provided material. |
| TOOLSEL07 | What tool result needs verification? | Verify generated media, search results, code edits, connector writes, installed plugins, deployments, and data exports. |
| TOOLSEL08 | What tool should not be used? | Avoid tools outside scope, untrusted third parties, broad filesystem edits, stale APIs, or action-capable connectors without need. |
| TOOLSEL09 | What tool-use evidence should be captured? | Record selected tool, reason, inputs, key outputs, limitations, errors, and validation result. |
| TOOLSEL10 | What capability routing artifact is required? | Produce tool plan, capability comparison, fallback map, tool trace, or install request packet. |

## Plan And Task Decomposition

| Code | Workflow question | Workflow use |
|---|---|---|
| AGPLAN01 | What decomposition is needed before execution? | Split goal into steps with inputs, actions, tools, outputs, dependencies, done criteria, and handoffs. |
| AGPLAN02 | What step should run first? | Start with state inspection, capability discovery, source loading, risk check, or reversible prototype before side effects. |
| AGPLAN03 | What steps can run in parallel? | Parallelize independent reads, searches, validations, and inspections without conflicting writes or state assumptions. |
| AGPLAN04 | What dependency order is required? | Sequence authorization, source gathering, design, execution, QA, approval, handoff, and archive gates. |
| AGPLAN05 | What checkpoint should be reported to the user? | Send progress after meaningful discoveries, long-running work, risk changes, approvals, blockers, and completion. |
| AGPLAN06 | What plan should change after new evidence? | Update steps when files, tests, tool output, user reply, errors, or external state contradict assumptions. |
| AGPLAN07 | What minimal viable action reduces uncertainty? | Use small test, sample, dry run, prototype, read-only query, or narrow patch before full-scale execution. |
| AGPLAN08 | What acceptance criteria guide each step? | Attach observable output, test, validation, reviewer signoff, or state change to each action. |
| AGPLAN09 | What plan record should remain for resume? | Store current step, completed steps, decisions, pending approvals, artifacts, and next action. |
| AGPLAN10 | What plan artifact is required? | Produce workflow plan, step table, task graph, checklist, dispatch packet, or continuation note. |

## Context Prompt And Memory Control

| Code | Workflow question | Workflow use |
|---|---|---|
| CTXPACK01 | What context must be loaded for the agent? | Include goal, constraints, relevant files, source excerpts, tool outputs, current state, and acceptance criteria. |
| CTXPACK02 | What context should be excluded? | Avoid unrelated files, secrets, stale assumptions, noisy logs, excessive source text, and hidden reasoning. |
| CTXPACK03 | What prompt boundary prevents drift? | State role, task, scope, outputs, forbidden actions, validation, and stop conditions in the execution packet. |
| CTXPACK04 | What state must be refreshed before action? | Refresh repo status, current file contents, live docs, connector state, account permissions, and running processes when unstable. |
| CTXPACK05 | What memory or prior context is trustworthy? | Use memory only when relevant, cite or verify drift-prone facts, and prefer current workspace state. |
| CTXPACK06 | What source excerpts should be quoted or summarized? | Provide minimal, relevant, source-attributed excerpts with provenance and word-limit compliance. |
| CTXPACK07 | What output schema should the agent follow? | Define fields, markdown shape, JSON schema, file path, dashboard manifest, test report, or handoff packet. |
| CTXPACK08 | What context handoff is needed between agents or tools? | Pass concise brief, artifact paths, assumptions, evidence, open questions, and expected output shape. |
| CTXPACK09 | What context safety issue exists? | Redact credentials, PII, secrets, private messages, customer data, and privileged legal/security content. |
| CTXPACK10 | What context artifact is required? | Produce context packet, prompt brief, memory note, source bundle, redaction log, or handoff summary. |

## Human Approval And Oversight

| Code | Workflow question | Workflow use |
|---|---|---|
| HITLAG01 | What human approval gate is required? | Gate high-risk, irreversible, external, public, financial, legal, security, or account-affecting actions. |
| HITLAG02 | Who can approve the action? | Identify user, owner, reviewer, admin, legal, security, finance, product, engineering, or executive approver. |
| HITLAG03 | What information does the approver need? | Provide action, reason, diff, risk, impact, rollback, alternatives, cost, and deadline. |
| HITLAG04 | What can proceed while waiting for approval? | Continue read-only analysis, drafting, validation, planning, or local preparation without side effects. |
| HITLAG05 | What approval should be explicit versus implied? | Require explicit approval for installs, sends, public posts, purchases, deletes, deployments, and permission changes. |
| HITLAG06 | What reviewer should inspect output quality? | Route to SME, code reviewer, data owner, design reviewer, legal, safety, or customer owner as needed. |
| HITLAG07 | What escalation path exists if approval is delayed? | Ask concise question, provide default safe path, defer action, or continue fallback work. |
| HITLAG08 | What human override can stop the agent? | Respect pause, stop, scope change, newest user instruction, revoked approval, and safety override. |
| HITLAG09 | What approval evidence should be retained? | Record approver, timestamp, action, scope, conditions, version, and resulting execution. |
| HITLAG10 | What oversight artifact is required? | Produce approval request, review checklist, signoff log, exception memo, or oversight summary. |

## Safe Execution And Side Effects

| Code | Workflow question | Workflow use |
|---|---|---|
| SAFEACT01 | What side effect could the action create? | Identify file edits, deletes, network writes, account changes, external messages, billing, deployments, or data movement. |
| SAFEACT02 | What preflight check is required? | Inspect current state, backups, git status, target paths, permissions, dry-run options, and affected systems. |
| SAFEACT03 | What scope limit should constrain execution? | Restrict paths, records, accounts, rows, batches, API calls, recipients, environments, and time windows. |
| SAFEACT04 | What reversible method can be used? | Prefer patch, branch, preview, draft, transaction, feature flag, snapshot, backup, or staged rollout. |
| SAFEACT05 | What destructive command must be avoided or gated? | Gate recursive delete, overwrite, reset, checkout, schema migration, permission revocation, and public publishing. |
| SAFEACT06 | What secret-handling rule applies? | Never print, store, exfiltrate, commit, or pass secrets beyond required scoped tool use. |
| SAFEACT07 | What external communication guardrail applies? | Review recipients, content, attachments, tone, confidentiality, approval, and send timing. |
| SAFEACT08 | What production environment guardrail applies? | Verify environment, tenant, project, region, deployment target, rollback, monitoring, and authorization. |
| SAFEACT09 | What post-action verification is required? | Confirm changed files, API response, record state, deployment health, message delivery, or absence of unintended changes. |
| SAFEACT10 | What safe-execution artifact is required? | Produce preflight checklist, action log, diff, rollback note, side-effect register, or verification report. |

## State Memory And Resume

| Code | Workflow question | Workflow use |
|---|---|---|
| AGSTATE01 | What state must persist across turns or runs? | Save objective, plan, completed work, files changed, tests run, artifacts, blockers, and next action. |
| AGSTATE02 | What state can be recomputed instead of stored? | Recompute cheap, deterministic, non-sensitive facts such as counts, searches, and current file contents. |
| AGSTATE03 | What state is stale and needs refresh? | Refresh live web data, plugin availability, running services, repo status, generated files, and external account state. |
| AGSTATE04 | What checkpoint supports interruption recovery? | Keep latest validated artifact, command evidence, current step, pending approval, and known risks. |
| AGSTATE05 | What resume rule should be followed? | Continue from current evidence, not memory alone, and inspect files before editing after a pause. |
| AGSTATE06 | What state conflict must be resolved? | Handle user edits, regenerated outputs, concurrent changes, changed plugin state, and stale summaries. |
| AGSTATE07 | What private state should not be persisted? | Avoid storing secrets, sensitive personal data, private connector content, and unnecessary raw logs. |
| AGSTATE08 | What progress metric should be tracked? | Track completed steps, coverage count, tests passed, artifacts delivered, unresolved risks, and remaining scope. |
| AGSTATE09 | What handoff should another agent receive? | Provide concise context, current files, decisions, validation outputs, and exact next tasks. |
| AGSTATE10 | What state artifact is required? | Produce continuation summary, checkpoint note, resume packet, progress ledger, or state manifest. |

## Trace Observability And Audit

| Code | Workflow question | Workflow use |
|---|---|---|
| AGTRACE01 | What trace should be captured? | Record plan updates, tool calls, key commands, file changes, decisions, approvals, validation, and final artifacts. |
| AGTRACE02 | What trace is user-facing versus internal? | Share useful progress and outcomes while excluding hidden reasoning, secrets, and noisy raw logs. |
| AGTRACE03 | What audit question must be answerable? | Prove who requested, what was done, which tools ran, what changed, why, and how it was verified. |
| AGTRACE04 | What trace granularity is appropriate? | Use concise summaries for low-risk work and detailed logs for regulated, destructive, or production actions. |
| AGTRACE05 | What artifact provenance should be tracked? | Link source inputs, generated files, prompt variants, model/tool outputs, edits, and validation evidence. |
| AGTRACE06 | What monitoring signal should watch the agent? | Track errors, retries, tool failures, cost, latency, approval waits, drift, output quality, and safety findings. |
| AGTRACE07 | What exception should be highlighted? | Flag failed tests, skipped verification, missing approval, fallback path, incomplete source, or residual risk. |
| AGTRACE08 | What audit retention rule applies? | Keep traces according to privacy, compliance, project policy, retention, and deletion requirements. |
| AGTRACE09 | What final summary should include tool evidence? | Report changed files, validation commands, counts, tests, unresolved risks, and next recommended layer. |
| AGTRACE10 | What trace artifact is required? | Produce run log, audit trail, validation summary, provenance map, or evidence packet. |

## Failure Recovery And Rollback

| Code | Workflow question | Workflow use |
|---|---|---|
| AGRECV01 | What failure mode is most likely? | Identify tool error, missing auth, stale state, bad output, partial edit, timeout, rate limit, side effect, or wrong route. |
| AGRECV02 | What detection signal shows failure? | Use exit code, exception, test failure, diff mismatch, API error, validation failure, missing artifact, or user correction. |
| AGRECV03 | What retry policy is safe? | Retry transient reads, network calls, and idempotent actions; avoid repeating side effects without state check. |
| AGRECV04 | What fallback path should be used? | Switch tool, reduce scope, use local files, ask user, create draft, run manual validation, or defer side effect. |
| AGRECV05 | What rollback method is available? | Use reverse patch, backup restore, transaction rollback, feature flag off, version restore, or manual corrective action. |
| AGRECV06 | What partial completion should be preserved? | Keep valid artifacts, evidence, decisions, tests, and completed safe steps while isolating failed pieces. |
| AGRECV07 | What user communication is required after failure? | State failure, impact, attempted recovery, current safe state, needed approval, and next action. |
| AGRECV08 | What recurring failure should update the workflow? | Add preflight, validation, guardrail, better tool choice, or documentation after repeated issues. |
| AGRECV09 | What blocked condition requires stopping? | Stop after missing external access, repeated approval absence, unsafe side effect, or impossible requirement. |
| AGRECV10 | What recovery artifact is required? | Produce failure report, rollback note, retry log, corrective action, or updated runbook. |

## Cost Rate Limit And Capacity Control

| Code | Workflow question | Workflow use |
|---|---|---|
| AGCOST01 | What resource budget matters? | Track tokens, API calls, compute, cloud spend, tool quota, time, human review capacity, and storage. |
| AGCOST02 | What rate limit or quota applies? | Identify platform quotas, connector limits, API throttles, model limits, batch size, and concurrency limits. |
| AGCOST03 | What work can be sampled before scaling? | Test on small files, few records, sample prompts, pilot batch, or dry run before full execution. |
| AGCOST04 | What caching or reuse can reduce cost? | Reuse source summaries, parsed data, embeddings, test fixtures, generated assets, and validated templates. |
| AGCOST05 | What parallelism is safe and useful? | Parallelize independent reads and validations while limiting write conflicts, API spikes, and hidden cost. |
| AGCOST06 | What stop threshold prevents runaway work? | Stop on cost ceiling, repeated retries, too many results, excessive tokens, long runtime, or low marginal value. |
| AGCOST07 | What quality-cost tradeoff is acceptable? | Choose depth, sample size, model/tool tier, manual review, batch coverage, and evidence level by risk. |
| AGCOST08 | What usage should be reported? | Summarize key token, runtime, API, compute, file, and human-review usage when meaningful or budgeted. |
| AGCOST09 | What optimization should follow repeated runs? | Add scripts, templates, indexes, caches, or deterministic validators to reduce future cost. |
| AGCOST10 | What cost artifact is required? | Produce budget note, quota plan, batch manifest, cost log, sample plan, or optimization backlog. |

## Evaluation QA And Acceptance

| Code | Workflow question | Workflow use |
|---|---|---|
| AGEVAL01 | What evaluation proves the agent output is correct? | Choose tests, validators, screenshots, source checks, diff review, schema validation, user acceptance, or expert review. |
| AGEVAL02 | What benchmark or rubric should be used? | Define criteria for accuracy, completeness, safety, usefulness, style, performance, cost, and traceability. |
| AGEVAL03 | What negative test should be run? | Test missing inputs, invalid data, prompt injection, permissions denial, tool failure, edge cases, and unsafe requests. |
| AGEVAL04 | What regression risk should be checked? | Compare before/after behavior, existing tests, snapshots, prior outputs, and downstream contracts. |
| AGEVAL05 | What source-grounding check is needed? | Verify citations, current facts, quoted limits, provenance, and evidence-to-claim alignment. |
| AGEVAL06 | What human review should complement automation? | Add reviewer judgment for legal, medical, financial, security, design, brand, ethical, and high-impact outputs. |
| AGEVAL07 | What acceptance threshold closes the run? | Define pass/fail criteria, allowed caveats, unresolved risks, user signoff, and final handoff requirements. |
| AGEVAL08 | What hallucination or overreach check applies? | Detect invented facts, unsupported claims, fake tool state, assumed permissions, and exaggerated completion. |
| AGEVAL09 | What evaluation result should update the workflow? | Capture failure patterns, stronger prompts, better tools, missing tests, and new matrix rows if needed. |
| AGEVAL10 | What evaluation artifact is required? | Produce QA report, rubric score, test log, validation table, acceptance note, or residual-risk summary. |

## Agent Operations And Governance

| Code | Workflow question | Workflow use |
|---|---|---|
| AGOPS01 | What operating model should run the agent? | Choose ad hoc assistant, scheduled automation, event-driven agent, monitored service, batch runner, or managed workflow. |
| AGOPS02 | What deployment or installation boundary applies? | Define local-only, workspace tool, plugin, connector, cloud job, CI action, internal app, or customer-facing agent. |
| AGOPS03 | What governance owner maintains the agent? | Assign product owner, engineering owner, security owner, data owner, operations owner, or model owner. |
| AGOPS04 | What policy review is needed before production use? | Check AI policy, privacy, security, legal, compliance, vendor, data retention, accessibility, and incident response. |
| AGOPS05 | What versioning and change management applies? | Version prompts, tools, models, configs, permissions, schemas, tests, and release notes. |
| AGOPS06 | What operational monitoring is required? | Monitor success rate, error rate, latency, cost, user satisfaction, safety incidents, tool failures, and drift. |
| AGOPS07 | What incident response path applies? | Define severity, containment, shutdown, customer communication, RCA, remediation, and restart criteria. |
| AGOPS08 | What user training or disclosure is needed? | Provide usage guidance, limitations, human oversight, data handling, escalation path, and AI disclosure where needed. |
| AGOPS09 | What retirement or deactivation rule applies? | Retire stale agents, unused tools, unsafe automations, deprecated connectors, or unsupported workflows. |
| AGOPS10 | What governance artifact is required? | Produce agent runbook, policy checklist, version manifest, monitoring dashboard, incident plan, or retirement note. |
