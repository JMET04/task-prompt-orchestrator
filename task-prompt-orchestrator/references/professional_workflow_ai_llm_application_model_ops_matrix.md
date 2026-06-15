# Professional Workflow AI LLM Application Model Ops Matrix

Use this matrix when a workflow must design, build, evaluate, deploy, monitor, govern, or improve an AI/LLM application, model-powered feature, prompt system, RAG workflow, tool-calling product, multimodal generation pipeline, or AI model operations process.

## AI Application Scope

| Code | Workflow question | Workflow use |
|---|---|---|
| AISCOPE01 | What AI-powered outcome is in scope? | Define assistant, classifier, extractor, generator, recommender, analyst, agent, search assistant, visual generator, or workflow copilot. |
| AISCOPE02 | What user job should AI perform? | Map task, user intent, decision support need, content generation need, automation need, or expert augmentation role. |
| AISCOPE03 | What business or operational value matters? | Choose speed, quality, coverage, cost reduction, personalization, accuracy, consistency, availability, or new capability. |
| AISCOPE04 | What AI product boundary applies? | Separate model behavior, prompt layer, retrieval layer, tool layer, UI, backend, data store, evaluation, and operations. |
| AISCOPE05 | What risk level applies to the AI use case? | Classify low-risk drafting, internal support, customer-facing advice, regulated decision support, safety-critical, or autonomous action. |
| AISCOPE06 | What user control is required? | Define edit, approve, reject, regenerate, cite, inspect, override, appeal, or escalate controls. |
| AISCOPE07 | What modality is involved? | Identify text, image, audio, video, code, structured data, CAD, document, spreadsheet, multimodal input, or multimodal output. |
| AISCOPE08 | What latency and interaction pattern applies? | Choose interactive chat, batch run, background job, streaming, webhook, scheduled process, or human-reviewed queue. |
| AISCOPE09 | What AI application artifact is required? | Produce AI feature brief, use-case canvas, architecture sketch, prompt spec, evaluation plan, or launch checklist. |
| AISCOPE10 | What proves the AI workflow is worth operating? | Require user value, measurable quality, acceptable risk, cost envelope, support readiness, and monitoring plan. |

## Model Selection And Provider Strategy

| Code | Workflow question | Workflow use |
|---|---|---|
| MODELSEL01 | What model capability is required? | Select reasoning, coding, extraction, summarization, vision, image generation, speech, embeddings, reranking, or tool use. |
| MODELSEL02 | What model quality bar applies? | Define benchmark score, domain accuracy, instruction following, format reliability, factuality, creativity, or safety threshold. |
| MODELSEL03 | What provider or deployment option fits? | Compare hosted API, local model, cloud marketplace, fine-tuned model, open-weight model, or managed platform. |
| MODELSEL04 | What context window and memory need exists? | Match input size, document set, conversation length, retrieved context, tool outputs, and state compression. |
| MODELSEL05 | What output modality and schema support is needed? | Check JSON, function calling, image, audio, video, code, tables, citations, bounding boxes, or structured extraction. |
| MODELSEL06 | What data boundary constrains model choice? | Account for privacy, residency, vendor policy, retention, training use, encryption, and regulated-data handling. |
| MODELSEL07 | What reliability or availability requirement applies? | Consider uptime, rate limits, quotas, fallback model, regional availability, and degradation behavior. |
| MODELSEL08 | What cost-performance tradeoff is acceptable? | Balance token cost, latency, quality, batching, caching, smaller model routing, and premium model escalation. |
| MODELSEL09 | What vendor lock-in risk exists? | Abstract provider calls, preserve prompt portability, track model versions, and plan migration tests. |
| MODELSEL10 | What model-selection artifact is required? | Produce model scorecard, provider comparison, routing policy, fallback plan, or model decision record. |

## Prompt System And Instruction Design

| Code | Workflow question | Workflow use |
|---|---|---|
| PROMPTOPS01 | What prompt role and authority structure applies? | Define system, developer, user, tool, retrieved context, examples, and output policy precedence. |
| PROMPTOPS02 | What task decomposition is needed? | Split reasoning, extraction, search, transformation, generation, review, and final synthesis into reliable steps. |
| PROMPTOPS03 | What context must be packed into the prompt? | Include goals, constraints, source excerpts, schemas, examples, rubrics, user preferences, and state summaries. |
| PROMPTOPS04 | What examples or counterexamples are needed? | Add few-shot cases, edge cases, bad-output examples, format examples, and domain-specific acceptance patterns. |
| PROMPTOPS05 | What output contract must the model follow? | Specify JSON schema, markdown section, table, citation format, file patch, checklist, or tool input shape. |
| PROMPTOPS06 | What ambiguity-handling rule is needed? | Decide when to ask, assume, branch, label uncertainty, or continue with a safe default. |
| PROMPTOPS07 | What prompt injection or instruction conflict must be handled? | Separate trusted instructions from untrusted content, cite conflicts, and ignore malicious source directives. |
| PROMPTOPS08 | What prompt variant should be tested? | Compare concise, verbose, chain, tool-first, retrieval-first, rubric-first, or example-heavy prompts. |
| PROMPTOPS09 | What prompt maintainability rule applies? | Version prompts, name variables, avoid hidden assumptions, document dependencies, and preserve reusable snippets. |
| PROMPTOPS10 | What prompt-system artifact is required? | Produce prompt spec, prompt packet, variable map, test cases, version log, or prompt change record. |

## Retrieval Knowledge And RAG Operations

| Code | Workflow question | Workflow use |
|---|---|---|
| RAGOPS01 | What knowledge source should ground the answer? | Select docs, web, database, codebase, tickets, PDFs, spreadsheets, transcripts, images, or curated knowledge base. |
| RAGOPS02 | What ingestion workflow is needed? | Define parsing, chunking, metadata extraction, deduplication, cleaning, embedding, indexing, and refresh cadence. |
| RAGOPS03 | What chunking and metadata strategy applies? | Choose semantic chunks, sections, tables, code symbols, timestamps, product IDs, jurisdiction, owner, and source date. |
| RAGOPS04 | What retrieval method should be used? | Use keyword, vector, hybrid, reranking, filters, graph traversal, SQL, API lookup, or tool-assisted search. |
| RAGOPS05 | What source authority and freshness rule applies? | Rank official, recent, primary, approved, licensed, internal, or user-provided sources by context. |
| RAGOPS06 | What citation or evidence format is required? | Return links, file paths, quote spans, page numbers, row IDs, commit hashes, or evidence tables. |
| RAGOPS07 | What retrieval failure mode must be handled? | Detect no hits, stale hits, conflicting hits, low confidence, inaccessible source, or hallucinated citation. |
| RAGOPS08 | What knowledge update process is needed? | Schedule refresh, invalidation, source deprecation, index rebuild, content owner review, and drift alert. |
| RAGOPS09 | What retrieval privacy boundary applies? | Enforce tenant filters, access controls, redaction, least-privilege connectors, and secure cache handling. |
| RAGOPS10 | What RAG artifact is required? | Produce source manifest, ingestion map, retrieval policy, citation contract, eval set, or refresh runbook. |

## Tool Calling And Function Orchestration

| Code | Workflow question | Workflow use |
|---|---|---|
| TOOLCALL01 | What tool or function should the model call? | Select search, shell, database, API, calculator, file editor, browser, image generator, deployment tool, or connector. |
| TOOLCALL02 | What tool schema is required? | Define input fields, types, required values, defaults, validation, idempotency, and expected output. |
| TOOLCALL03 | What tool-call trigger should be used? | Call tools for current facts, local state, calculations, file changes, external actions, or evidence retrieval. |
| TOOLCALL04 | What tool permission boundary applies? | Restrict read-only, write, publish, purchase, delete, deploy, message-send, or credential-access actions. |
| TOOLCALL05 | What tool result must be verified? | Check status code, row count, file existence, schema match, checksum, screenshot, log line, or diff. |
| TOOLCALL06 | What retry and fallback rule is needed? | Define safe retries, backoff, alternate tool, manual path, degraded answer, or escalation. |
| TOOLCALL07 | What side effect needs approval? | Require confirmation before modifying files, charging money, sending messages, publishing, deleting, or deploying. |
| TOOLCALL08 | What multi-tool dependency exists? | Sequence search, read, transform, write, test, deploy, monitor, and report steps with handoff contracts. |
| TOOLCALL09 | What tool trace should be preserved? | Record tool name, inputs, outputs, timestamps, target scope, validation, and user-facing summary. |
| TOOLCALL10 | What tool orchestration artifact is required? | Produce tool plan, schema spec, permission map, run trace, approval log, or fallback plan. |

## Evaluation Datasets And Benchmarks

| Code | Workflow question | Workflow use |
|---|---|---|
| EVALSET01 | What quality dimensions need evaluation? | Measure accuracy, completeness, factuality, citation quality, format validity, safety, helpfulness, latency, and cost. |
| EVALSET02 | What representative test cases are needed? | Include common cases, edge cases, adversarial cases, multilingual cases, long-context cases, and domain-specific tasks. |
| EVALSET03 | What golden answers or rubrics are required? | Create expected outputs, scoring criteria, expert annotations, tolerances, and unacceptable failure examples. |
| EVALSET04 | What automated checks can be deterministic? | Validate schema, regex, JSON, citations, groundedness signals, unit tests, snapshot tests, and policy flags. |
| EVALSET05 | What human review is required? | Use SMEs, safety reviewers, legal reviewers, QA, customer support, or target users for subjective quality. |
| EVALSET06 | What regression baseline should be tracked? | Compare current prompt/model against previous version, fallback model, manual workflow, or production benchmark. |
| EVALSET07 | What sample size is enough? | Set coverage by risk, traffic, task diversity, cost, confidence, and business criticality. |
| EVALSET08 | What acceptance threshold gates release? | Define minimum score, maximum critical failures, latency ceiling, cost ceiling, and manual signoff. |
| EVALSET09 | What evaluation drift must be watched? | Monitor new user intents, source changes, model updates, prompt edits, abuse attempts, and changing standards. |
| EVALSET10 | What evaluation artifact is required? | Produce eval dataset, benchmark report, rubric, regression dashboard, failure taxonomy, or release gate record. |

## Safety Guardrails And Policy Controls

| Code | Workflow question | Workflow use |
|---|---|---|
| SAFEGUARD01 | What unsafe output must be prevented? | Define prohibited advice, disallowed content, privacy leaks, harmful instructions, policy violations, or brand risks. |
| SAFEGUARD02 | What sensitive input must be protected? | Detect credentials, personal data, regulated records, private documents, copyrighted content, or confidential business data. |
| SAFEGUARD03 | What refusal or safe-completion style applies? | Provide refusal, redirection, high-level help, professional referral, escalation, or safer alternative. |
| SAFEGUARD04 | What human oversight gate is required? | Add review before high-impact decisions, external publication, legal claims, medical advice, financial advice, or destructive action. |
| SAFEGUARD05 | What abuse or adversarial behavior should be detected? | Watch prompt injection, jailbreaks, data exfiltration, spam, impersonation, fraud, or malicious automation. |
| SAFEGUARD06 | What content filter or classifier is needed? | Use pre-checks, post-checks, moderation, PII detection, toxicity checks, hallucination checks, or domain policy checks. |
| SAFEGUARD07 | What transparency notice is needed? | Disclose AI assistance, limitations, source basis, uncertainty, user controls, and appeal or correction path. |
| SAFEGUARD08 | What audit evidence must be retained? | Save policy version, model version, prompt version, input class, decision outcome, reviewer, and escalation record. |
| SAFEGUARD09 | What safety fallback should run? | Route to safer model, constrained prompt, human queue, read-only mode, or refusal template when risk is high. |
| SAFEGUARD10 | What guardrail artifact is required? | Produce safety spec, policy map, filter design, oversight plan, abuse response playbook, or audit log schema. |

## Cost Latency And Performance Optimization

| Code | Workflow question | Workflow use |
|---|---|---|
| COSTLAT01 | What cost unit should be optimized? | Track token cost, image cost, audio minutes, requests, compute, storage, vector search, human review, or retries. |
| COSTLAT02 | What latency target applies? | Set response, first-token, job completion, batch window, queue wait, or end-to-end SLA. |
| COSTLAT03 | What routing optimization is possible? | Use small model first, premium model escalation, cached answers, retrieval filters, batch mode, or offline preprocessing. |
| COSTLAT04 | What context compression is needed? | Summarize history, trim retrieval, dedupe sources, compress tool outputs, and preserve only decision-relevant state. |
| COSTLAT05 | What caching strategy applies? | Cache embeddings, retrieval results, prompt prefixes, generated assets, user sessions, or deterministic tool results. |
| COSTLAT06 | What throughput constraint exists? | Plan rate limits, quotas, concurrency, queueing, streaming, sharding, and backpressure. |
| COSTLAT07 | What expensive failure should be reduced? | Minimize retries, long irrelevant context, invalid JSON, unnecessary tool calls, failed generations, and reviewer rework. |
| COSTLAT08 | What quality-cost tradeoff must be visible? | Report quality score, cost per successful task, latency, failure rate, and user impact by route. |
| COSTLAT09 | What budget guardrail is required? | Set per-user, per-workflow, per-day, per-project, or per-customer budget limits and alerts. |
| COSTLAT10 | What optimization artifact is required? | Produce cost model, latency budget, routing policy, cache plan, quota plan, or optimization report. |

## Deployment Runtime And Versioning

| Code | Workflow question | Workflow use |
|---|---|---|
| MODELDEP01 | What AI component is being deployed? | Identify prompt, model route, retrieval index, tool schema, guardrail, eval set, fine-tune, or full application release. |
| MODELDEP02 | What environment should receive the change? | Use local, dev, staging, preview, canary, production, region, tenant, or internal-only deployment. |
| MODELDEP03 | What version identifiers must be tracked? | Record model, prompt, retrieval corpus, embeddings, tool schema, guardrail policy, eval set, and app code versions. |
| MODELDEP04 | What release strategy should be used? | Choose canary, A/B test, shadow mode, dark launch, feature flag, cohort rollout, or manual promotion. |
| MODELDEP05 | What compatibility issue could occur? | Check schema changes, prompt variable changes, model behavior shifts, index rebuilds, API versions, and client expectations. |
| MODELDEP06 | What rollback path is needed? | Restore previous prompt, model route, index, tool schema, policy, feature flag, or app version. |
| MODELDEP07 | What migration or backfill is required? | Re-embed corpus, migrate conversation memory, update stored outputs, regenerate cached artifacts, or re-score evals. |
| MODELDEP08 | What release approval applies? | Require product, engineering, security, legal, Responsible AI, support, or customer owner signoff. |
| MODELDEP09 | What post-release validation should run? | Execute smoke prompts, tool checks, retrieval checks, eval subset, monitoring checks, and user journey tests. |
| MODELDEP10 | What deployment artifact is required? | Produce AI release note, version manifest, deployment checklist, rollback plan, or post-release report. |

## Monitoring Observability And Feedback

| Code | Workflow question | Workflow use |
|---|---|---|
| AIMON01 | What AI runtime signals should be captured? | Track requests, latency, errors, token use, cost, tool calls, retrieval hits, safety flags, and user actions. |
| AIMON02 | What quality signals should be monitored? | Watch thumbs, edits, retries, escalations, complaint rate, citation failures, format failures, and task completion. |
| AIMON03 | What drift signal matters? | Detect model behavior changes, source freshness changes, user intent shift, prompt regression, or tool failure pattern. |
| AIMON04 | What privacy-safe logging rule applies? | Redact sensitive data, sample safely, separate metadata from content, respect retention, and control access. |
| AIMON05 | What dashboard should operators see? | Show quality, safety, latency, cost, volume, failures, model route, retrieval performance, and feedback trends. |
| AIMON06 | What alert threshold should trigger action? | Alert on cost spike, error spike, safety violation, hallucination reports, latency breach, tool outage, or source drift. |
| AIMON07 | What feedback loop should improve the system? | Convert user feedback, reviewer notes, support tickets, and eval failures into prompt, model, RAG, or UX changes. |
| AIMON08 | What trace should support debugging? | Preserve prompt version, model, context sources, tool calls, outputs, guardrail events, and final user action. |
| AIMON09 | What monitoring governance is needed? | Assign owner, review cadence, retention, dashboard access, incident thresholds, and improvement backlog path. |
| AIMON10 | What monitoring artifact is required? | Produce AI observability plan, dashboard spec, alert policy, trace schema, feedback report, or improvement backlog. |

## Human Review And Expert Escalation

| Code | Workflow question | Workflow use |
|---|---|---|
| HUMANAI01 | When must a human review AI output? | Trigger review for low confidence, high risk, external publishing, customer harm, regulated advice, or unusual cases. |
| HUMANAI02 | Who is the right reviewer? | Route to domain expert, legal, security, QA, support, product owner, safety reviewer, or customer owner. |
| HUMANAI03 | What reviewer context is needed? | Provide user request, model output, sources, trace, risk flags, rubric, and decision options. |
| HUMANAI04 | What review decision can be made? | Approve, edit, reject, regenerate, escalate, request more evidence, change route, or block release. |
| HUMANAI05 | What reviewer workload constraint exists? | Manage queue, SLA, priority, sampling, expertise matching, handoff, and reviewer fatigue. |
| HUMANAI06 | What disagreement path is needed? | Resolve conflicts between model, reviewer, policy, user, and SME with arbitration and rationale. |
| HUMANAI07 | What feedback should return to the AI system? | Convert edits, comments, rejects, and escalations into training examples, eval cases, prompt changes, or policy updates. |
| HUMANAI08 | What user-facing explanation is needed? | Explain reviewed decision, uncertainty, limitations, escalation status, and next step without exposing private traces. |
| HUMANAI09 | What audit record should be kept? | Store reviewer, decision, rationale, source, model version, prompt version, risk flag, and timestamp. |
| HUMANAI10 | What human-review artifact is required? | Produce review queue design, rubric, escalation map, reviewer packet, decision log, or feedback loop plan. |

## Versioning Change And Knowledge Management

| Code | Workflow question | Workflow use |
|---|---|---|
| VERSIONAI01 | What AI asset needs version control? | Version prompts, eval sets, model routes, corpora, embeddings, tool schemas, guardrails, examples, and outputs. |
| VERSIONAI02 | What change type is being made? | Classify prompt edit, model upgrade, retrieval refresh, tool change, policy update, UI change, or data migration. |
| VERSIONAI03 | What compatibility promise must hold? | Preserve output schema, citation behavior, safety behavior, latency, cost, and user-facing contract. |
| VERSIONAI04 | What changelog entry is needed? | Record change reason, owner, affected routes, risk, tests, metrics, approval, and rollback note. |
| VERSIONAI05 | What reusable knowledge should be captured? | Save best prompts, failure cases, eval lessons, domain rules, user preferences, and operational runbooks. |
| VERSIONAI06 | What deprecation or retirement rule applies? | Retire stale prompts, old models, unsupported tools, outdated corpora, obsolete examples, and unsafe routes. |
| VERSIONAI07 | What migration testing is needed? | Compare old and new outputs, run regression set, test edge cases, verify schema, and inspect safety changes. |
| VERSIONAI08 | What documentation should be updated? | Update prompt spec, model card, source manifest, API docs, runbook, training guide, and support notes. |
| VERSIONAI09 | What ownership and review cadence applies? | Assign asset owner, review schedule, freshness trigger, and accountability for updates. |
| VERSIONAI10 | What versioning artifact is required? | Produce AI asset register, version manifest, changelog, migration report, or retirement record. |

## AI Incident Response And Continuous Improvement

| Code | Workflow question | Workflow use |
|---|---|---|
| AIINCIDENT01 | What AI incident type occurred? | Classify hallucination, unsafe output, privacy leak, tool misuse, cost spike, latency outage, retrieval failure, or model drift. |
| AIINCIDENT02 | What severity and impact apply? | Assess users affected, harm level, business impact, legal risk, safety risk, data exposure, and operational urgency. |
| AIINCIDENT03 | What containment action is needed? | Disable route, switch model, block tool, roll back prompt, remove source, enable human review, or pause automation. |
| AIINCIDENT04 | What evidence must be preserved? | Capture prompt version, model version, sources, tool trace, user report, logs, reviewer notes, and timestamps. |
| AIINCIDENT05 | What communication is required? | Notify operators, support, product, security, legal, customers, or status channel based on severity. |
| AIINCIDENT06 | What root cause should be investigated? | Analyze prompt flaw, model update, source drift, bad retrieval, guardrail gap, tool schema issue, or missing review. |
| AIINCIDENT07 | What corrective action should be taken? | Update prompt, eval set, source policy, guardrail, model route, tool permission, review gate, or user UX. |
| AIINCIDENT08 | What regression prevention is needed? | Add incident case to evals, monitoring alerts, safety tests, documentation, and release gates. |
| AIINCIDENT09 | What restart or re-enable gate applies? | Require passing tests, owner approval, monitoring check, support readiness, and rollback plan before restoring. |
| AIINCIDENT10 | What incident artifact is required? | Produce incident report, timeline, impact note, root-cause analysis, corrective-action plan, or prevention checklist. |
