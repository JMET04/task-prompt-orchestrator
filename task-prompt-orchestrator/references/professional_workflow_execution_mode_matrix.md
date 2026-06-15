# Professional Workflow Execution Mode Matrix

Use this when a workflow needs a specific operating mode. Composition defines the end-to-end recipe; control defines gates and branches; execution mode defines how the workflow is run in practice: autonomous, human-in-loop, batch, real-time, async, tool-driven, exploratory, deterministic, governed, or recovery-oriented.

Selection rule:

1. Select workflow composition and workflow control codes first.
2. Select one or more execution mode codes here.
3. Add the mode's cadence, supervision, logging, and stop conditions to each prompt packet.
4. If execution mode conflicts with risk, choose the more supervised and verifiable mode.

## AUTX Autonomous Execution

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| AUTX01 | Single-agent autonomous | Agent plans, executes, verifies, and reports within one scope | Plan, outputs, verification | Blocking unknown or failed gate |
| AUTX02 | Autonomous research | Agent searches, screens, synthesizes, and cites sources | Source log, evidence table | Source insufficiency |
| AUTX03 | Autonomous code fix | Agent inspects repo, patches, tests, and summarizes | Diff, test result | Test cannot run or unsafe change |
| AUTX04 | Autonomous document production | Agent drafts, edits, verifies claims, and delivers artifact | Draft, QA note | Missing evidence/approval |
| AUTX05 | Autonomous data analysis | Agent profiles data, analyzes, visualizes, and reports | Query/code, output, caveats | Data access/quality blocker |
| AUTX06 | Autonomous image prompt pack | Agent selects template, writes variants, negative prompts, QA | Prompt pack | Missing product/reference facts |
| AUTX07 | Autonomous cleanup/organization | Agent inventories, classifies, reorganizes with safe boundary | Manifest, action log | Destructive risk |
| AUTX08 | Autonomous triage | Agent classifies, prioritizes, and proposes next actions | Triage table | Need owner approval |
| AUTX09 | Autonomous QA pass | Agent applies checks and fixes safe issues | QA report, fixes | High-risk unresolved finding |
| AUTX10 | Autonomous handoff | Agent creates final package and next-step note | Handoff pack | Owner/action missing |

## HITL Human-in-the-Loop

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| HITL01 | Clarification checkpoint | Ask only blocking questions before execution | Question list | User answer required |
| HITL02 | Review checkpoint | Produce draft, then route to human reviewer | Review packet | Reviewer decision needed |
| HITL03 | Approval checkpoint | Hold publication/release until approver signs off | Approval packet | Approval absent |
| HITL04 | Expert checkpoint | Use expert review for legal, medical, finance, safety, security | Expert questions | Expert unavailable |
| HITL05 | Preference checkpoint | Ask user to choose among materially different routes | Options brief | Choice changes output |
| HITL06 | Risk acceptance checkpoint | Ask owner to accept residual risk before final | Risk acceptance note | Risk not accepted |
| HITL07 | Creative selection checkpoint | Generate routes, then let user choose direction | Creative route board | Direction not selected |
| HITL08 | Data interpretation checkpoint | Show caveats and ask stakeholder before decision | Analysis review note | Business context missing |
| HITL09 | Scope change checkpoint | Pause when requested work exceeds agreed scope | Scope change note | Scope not approved |
| HITL10 | Final confirmation checkpoint | Present final summary and verification before external action | Final approval note | External action not confirmed |

## BATX Batch / Bulk Execution

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| BATX01 | Batch prompt generation | Generate prompts from one template across variables | Batch prompt table | Variable gaps |
| BATX02 | Batch asset variants | Produce variants with controlled variables and naming | Variant manifest | Naming/QA failure |
| BATX03 | Batch classification | Classify many items with label rules and confidence | Classification table | Ambiguous labels |
| BATX04 | Batch extraction | Extract fields from many documents/items with confidence | Extraction table | Low OCR/source quality |
| BATX05 | Batch localization | Translate/localize many items with glossary and QA | Locale batch pack | Glossary conflict |
| BATX06 | Batch review | Review many artifacts against one rubric | Findings matrix | Rubric mismatch |
| BATX07 | Batch data QA | Run repeated checks across tables/files | QA summary | Critical defect |
| BATX08 | Batch content adaptation | Adapt master content for channels/audiences | Content variant pack | Channel constraints missing |
| BATX09 | Batch file processing | Transform many files with manifest and rollback | Processing log | File corruption risk |
| BATX10 | Batch handoff | Package many outputs with index, owners, and status | Batch handoff index | Missing artifact |

## RTX Real-Time / Live Response

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| RTX01 | Live incident response | Prioritize containment, facts, owner, next update | Incident log | Safety/security escalation |
| RTX02 | Live meeting support | Capture decisions, actions, risks, and follow-ups | Live notes | Ambiguous owner/action |
| RTX03 | Live customer support | Triage issue, respond, escalate, record | Support note | SLA/severity escalation |
| RTX04 | Live debugging | Observe logs/state, hypothesize, test minimal fix | Debug log | Unsafe change |
| RTX05 | Live event monitoring | Track agenda, issues, comms, and attendee needs | Event ops log | Critical blocker |
| RTX06 | Live launch monitoring | Watch metrics, issues, rollback triggers, comms | Launch monitor | Rollback trigger |
| RTX07 | Live creative direction | Give rapid feedback during production/review | Direction notes | Brief conflict |
| RTX08 | Live data watch | Monitor metric movement and annotate anomalies | Metric watch log | Data outage |
| RTX09 | Live workshop facilitation | Guide activities, capture outputs, adjust agenda | Facilitation log | Objective drift |
| RTX10 | Live executive briefing | Provide concise status, decisions, and risks | Live brief | Unknown critical fact |

## ASYN Async / Distributed Collaboration

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| ASYN01 | Async review | Provide context, criteria, comments, and decision deadline | Review doc | Missing criteria |
| ASYN02 | Async handoff | Package state, artifacts, decisions, and next actions | Handoff note | Next owner missing |
| ASYN03 | Async planning | Build plan with owners, dependencies, and update cadence | Async plan | Dependency unresolved |
| ASYN04 | Async content workflow | Route draft through comments, revisions, approvals | Content tracker | Approval missing |
| ASYN05 | Async engineering workflow | Issue -> branch/diff -> review -> CI -> merge handoff | Engineering tracker | CI/review failure |
| ASYN06 | Async research workflow | Assign subtopics, collect notes, merge synthesis | Research tracker | Source gaps |
| ASYN07 | Async stakeholder feedback | Collect feedback, classify, decide, respond | Feedback log | Conflicting feedback |
| ASYN08 | Async vendor workflow | Send brief, track deliverables, QA, accept/reject | Vendor tracker | Acceptance gap |
| ASYN09 | Async governance workflow | Record decisions, evidence, approvals, exceptions | Governance log | Audit gap |
| ASYN10 | Async learning workflow | Assign drills, collect attempts, give feedback | Learning tracker | Missing learner output |

## TOOL Tool-Driven Execution

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| TOOL01 | Shell-driven workflow | Use shell/scripts for deterministic file/code checks | Commands, outputs | Command failure |
| TOOL02 | Browser-driven workflow | Use browsing for current facts or page verification | URLs, citations | Source unavailable |
| TOOL03 | Data-tool workflow | Use query/execution tools for analysis and visualization | Query, results | Data access failure |
| TOOL04 | Design/media tool workflow | Use image/video/design tools and inspect outputs | Asset, QA note | Render/output failure |
| TOOL05 | Document tool workflow | Use document/spreadsheet/deck tools and validate file | File path, validation | File invalid |
| TOOL06 | Code-tool workflow | Use build/test/lint tools for implementation | Test/build logs | Unsafe failure |
| TOOL07 | Search-index workflow | Use local indexes/search scripts before broad reading | Search log | Index missing |
| TOOL08 | Plugin/connector workflow | Use specialized plugin when task matches capability | Tool call result | Tool unavailable |
| TOOL09 | Multi-tool chain | Sequence tools with typed handoffs and validation | Tool chain log | Handoff mismatch |
| TOOL10 | Tool fallback workflow | If tool fails, use safe fallback and report limits | Fallback log | No safe fallback |

## EXPX Exploratory / Discovery Mode

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| EXPX01 | Open-ended discovery | Explore broadly, map possibilities, then narrow | Discovery map | Direction selected |
| EXPX02 | Unknown repo exploration | Inspect structure, commands, patterns, and risks | Repo discovery note | Entry point found |
| EXPX03 | Source landscape exploration | Map source types, authority, gaps, and search strings | Source landscape | Enough coverage |
| EXPX04 | Problem framing exploration | Separate symptoms, causes, constraints, and goals | Problem frame | Core problem clear |
| EXPX05 | Opportunity exploration | Map pains, alternatives, gaps, and wedges | Opportunity map | Evidence threshold |
| EXPX06 | Creative exploration | Generate distinct routes before selecting one | Route board | Route chosen |
| EXPX07 | Data exploration | Profile, visualize, and form hypotheses | EDA note | Analysis question set |
| EXPX08 | Workflow exploration | Map current process, bottlenecks, and future flow | Workflow map | Future flow chosen |
| EXPX09 | Risk exploration | Identify risk classes, severity, and controls | Risk map | Critical risks handled |
| EXPX10 | Learning exploration | Diagnose level, goals, gaps, and best learning path | Learning map | Path selected |

## DET Deterministic / Reproducible Mode

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| DET01 | Scripted transformation | Use scripts/parser instead of ad hoc manual edits | Script, output | Script failure |
| DET02 | Repeatable data query | Store runnable query, parameters, and result snapshot | Query record | Query invalid |
| DET03 | Deterministic validation | Use explicit checks, counts, schemas, or tests | Validation log | Check fails |
| DET04 | Rule-based classification | Use fixed labels and decision rules | Label rule table | Rule ambiguity |
| DET05 | Template-driven generation | Use fixed template with variables and QA | Generated set | Placeholder remains |
| DET06 | Version-controlled change | Record exact file changes and verification commands | Change log | Dirty ambiguity |
| DET07 | Reproducible research | Store search strings, inclusion rules, and source list | Research protocol | Search not reproducible |
| DET08 | Audit-grade workflow | Preserve evidence, decisions, owners, and dates | Audit trail | Evidence gap |
| DET09 | Batch reproducibility | Manifest inputs, outputs, names, and failures | Batch manifest | Missing item |
| DET10 | Environment reproducibility | Record tools, versions, commands, and assumptions | Environment note | Env unknown |

## CREX Creative / Generative Mode

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| CREX01 | Divergent ideation | Generate multiple distinct directions before convergence | Idea routes | Routes too similar |
| CREX02 | Convergent refinement | Pick route, refine constraints, produce final | Refined concept | Selection missing |
| CREX03 | Style-controlled generation | Use style traits, references, and negative constraints | Style prompt | Style drift |
| CREX04 | Brand-safe creative | Enforce brand voice, claims, and visual identity | Brand QA | Brand mismatch |
| CREX05 | Production-aware creative | Include specs, dimensions, channel, handoff format | Production brief | Specs missing |
| CREX06 | Creative repair mode | Diagnose artifact issues, repair one class at a time | Repair log | Failure unclear |
| CREX07 | Campaign system mode | Maintain master idea across channel variants | Campaign system | Idea inconsistency |
| CREX08 | Image2 controlled mode | Preserve source invariants while changing target attributes | Image2 prompt pack | Invariants lost |
| CREX09 | Narrative mode | Structure hook, conflict, proof, payoff, CTA | Narrative draft | Arc weak |
| CREX10 | Experimental creative mode | Try bolder routes with explicit risk/fit notes | Experimental route pack | Risk unacceptable |

## GOVX Governed / Compliance Mode

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| GOVX01 | Regulated content mode | Add legal/compliance gate before external use | Review packet | Approval missing |
| GOVX02 | Privacy-governed mode | Minimize data, map purpose, access, retention | Privacy note | PII risk unresolved |
| GOVX03 | Security-governed mode | Check secrets, access, abuse paths, controls | Security note | Unsafe detail |
| GOVX04 | Audit-governed mode | Maintain evidence, decisions, versions, owners | Audit log | Evidence gap |
| GOVX05 | Change-control mode | Require impact, approval, rollback, communication | Change record | Approval missing |
| GOVX06 | Brand-governed mode | Check guidelines, approvals, and asset rights | Brand approval | Brand issue |
| GOVX07 | Vendor-governed mode | Track SLA, evidence, risks, acceptance | Vendor governance note | SLA gap |
| GOVX08 | HR-governed mode | Ensure fairness, privacy, documentation, review | HR governance note | Fairness risk |
| GOVX09 | Financial-governed mode | Track assumptions, approvals, audit trail | Finance governance note | Assumption gap |
| GOVX10 | AI-governed mode | Add human oversight, eval set, logs, and review | AI governance note | No review/eval |

## RECX Recovery / Exception Mode

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| RECX01 | Blocked workflow mode | Identify blocker, attempted paths, next needed input | Blocker note | User/external input needed |
| RECX02 | Failed verification mode | Report failed checks, fixes tried, residual risks | Verification failure report | Risk unresolved |
| RECX03 | Incident recovery mode | Stabilize, communicate, restore, then postmortem | Recovery pack | Service not stable |
| RECX04 | Data recovery mode | Stop mutation, preserve source, reconcile, restore | Data recovery note | Source unavailable |
| RECX05 | Content correction mode | Correct inaccurate published content and document change | Correction note | Approval needed |
| RECX06 | Rollback mode | Restore prior state, verify, communicate | Rollback report | Rollback failed |
| RECX07 | Degraded-service mode | Provide reduced output with clear limits and path to full | Degraded output | Limits unclear |
| RECX08 | Rework mode | Identify rejection reason, revise plan, rerun QA | Rework plan | Rejection unresolved |
| RECX09 | Escalated exception mode | Prepare expert/owner packet with evidence and asks | Exception packet | Owner missing |
| RECX10 | Close-with-risk mode | Close only with residual risks and recommended follow-up | Risk closeout | Risk not disclosed |

## HYBX Hybrid / Multi-Mode Execution

| Code | Mode | Operating rule | Required artifacts | Stop condition |
|---|---|---|---|---|
| HYBX01 | Discovery-to-deterministic | Start exploratory, then lock repeatable criteria and steps | Mode transition note | Lock criteria missing |
| HYBX02 | Human-reviewed autonomy | Let the agent execute routine work and route gates to a human reviewer | Review checkpoints | Gate not reviewed |
| HYBX03 | Tool-plus-human workflow | Combine tool output with expert or user review before acceptance | Tool result and review note | Review finding unresolved |
| HYBX04 | Batch-with-sampling QA | Process items in bulk, then spot-check a representative sample | Batch manifest and sample QA | Sample failure unresolved |
| HYBX05 | Real-time-to-closeout | Respond live, then create async follow-up, evidence, or postmortem | Live log and closeout note | Follow-up missing |
| HYBX06 | Creative-to-production | Explore creative routes, then convert the chosen route into production specs | Creative route and production spec | Specs not locked |
| HYBX07 | Offline-to-online refresh | Draft from available context, then refresh with current sources when access exists | Draft and refresh log | Freshness not verified |
| HYBX08 | Low-risk autonomous / high-risk HITL | Automate low-risk steps and require human review for high-impact gates | Risk split plan | High-risk gate unreviewed |
| HYBX09 | Prototype-to-governed release | Build fast prototype, then add approval, QA, and release controls | Prototype and governance pack | Approval failed |
| HYBX10 | Degraded-to-full workflow | Deliver a limited useful output now and schedule or define the full-quality pass | Degraded output and full plan | Limits not disclosed |
