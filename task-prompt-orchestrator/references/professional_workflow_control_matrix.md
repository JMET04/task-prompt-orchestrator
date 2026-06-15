# Professional Workflow Control Matrix

Use this when a workflow needs explicit control logic: gates, branching, sequencing, parallel work, loops, escalation, fallback, rollback, dependencies, service levels, risk controls, handoffs, or evidence checkpoints. This file is about how the workflow runs, not what domain it belongs to.

Selection rule:

1. Select the workflow composition code first when the task is multi-step.
2. Add one or more control codes here to define how steps advance, split, merge, fail, recover, or escalate.
3. Put control logic into prompt packets as `Gate`, `Branch`, `Fallback`, `Handoff`, and `Done when`.
4. Do not hide failed gates; report the stop reason, residual risk, or next required input.

## GAT Gate / Stage-Gate Controls

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| GAT01 | Intake gate | Do not plan until goal, inputs, constraints, and output are known | Intake checklist | No blocking unknowns |
| GAT02 | Scope gate | Freeze in/out scope before execution | Scope note | Scope accepted or assumed |
| GAT03 | Evidence gate | Do not conclude until evidence sufficiency is checked | Evidence table | Unsupported claims labeled |
| GAT04 | Design gate | Do not generate final assets until brief and invariants are fixed | Design gate note | Invariants clear |
| GAT05 | Data gate | Do not analyze until schema, grain, and quality are profiled | Data gate report | Grain and defects known |
| GAT06 | Build gate | Do not implement until affected files, test path, and risk are known | Build plan | Verification path exists |
| GAT07 | Review gate | Do not finalize until review criteria are applied | Review checklist | Findings resolved or accepted |
| GAT08 | Approval gate | Do not publish/launch until approver and decision status are clear | Approval record | Approval or draft label |
| GAT09 | Release gate | Do not release until rollback and monitoring are defined | Release gate | Rollback and health check |
| GAT10 | Closeout gate | Do not close until artifact, evidence, handoff, and residual risks are reported | Closeout note | Handoff complete |

## BRN Branch / Conditional Routing

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| BRN01 | Missing-input branch | If critical input is missing, produce assumption-based draft or ask targeted question | Branch note | Missing input named |
| BRN02 | High-risk branch | If high-risk domain detected, add safety/risk validation before output | Risk branch | Gate selected |
| BRN03 | Source-needed branch | If facts may be stale, browse or mark source-limited | Source branch | Freshness handled |
| BRN04 | User-only-source branch | If user forbids external sources, limit conclusions to provided material | Scope branch | Source limitation stated |
| BRN05 | Creative-vs-technical branch | Route visual requests to creative, production, or technical drawing path | Route note | Output type chosen |
| BRN06 | Draft-vs-final branch | If constraints prevent final quality, label as draft and list finalization steps | Quality branch | Status label |
| BRN07 | Tool-available branch | Use specialized tool when available; otherwise use documented fallback | Tool branch | Tool/fallback stated |
| BRN08 | Approval-needed branch | If external publication/regulated content, route to approval packet | Approval branch | Reviewer identified |
| BRN09 | Error-found branch | If verification fails, route to repair loop before final | Repair branch | Failure captured |
| BRN10 | Multi-audience branch | If audiences conflict, produce layered or separate outputs | Audience branch | Versions separated |

## SEQ Sequencing / Ordering

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| SEQ01 | Extract-before-analyze | Parse fields/claims/entities before analysis | Extraction table | Inputs structured |
| SEQ02 | Research-before-write | Gather evidence before drafting source-backed content | Evidence pack | Sources available |
| SEQ03 | Define-before-build | Define requirements and acceptance before implementation | Requirement spec | Testable criteria |
| SEQ04 | Prototype-before-polish | Build rough version before final styling or copy polish | Prototype | Core idea works |
| SEQ05 | Data-QA-before-chart | Validate data before visualization | Data QA note | Data issues handled |
| SEQ06 | Review-before-approval | Run QA/review before signoff request | Review report | Findings triaged |
| SEQ07 | Approval-before-publish | Confirm approval before public or external release | Approval log | Approval status |
| SEQ08 | Launch-before-monitor | Define monitoring before launch and run it after launch | Monitoring plan | Metrics and owners |
| SEQ09 | Fix-before-retrospective | Stabilize issue before root-cause documentation | Stabilization note | Impact contained |
| SEQ10 | Handoff-before-close | Prepare docs and owners before closing work | Handoff pack | Owner can resume |

## PAR Parallelization / Workstreams

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| PAR01 | Parallel discovery | Run source, file, and tool discovery in parallel when independent | Discovery bundle | No dependency conflict |
| PAR02 | Parallel research streams | Split market, technical, legal, and user research streams | Research workstream map | Merge criteria |
| PAR03 | Parallel creative routes | Generate multiple concept routes from same brief | Route set | Same constraints |
| PAR04 | Parallel review | Run factual, design, compliance, and usability review separately | Review bundle | Findings merged |
| PAR05 | Parallel build/test | Build one path while tests/docs are prepared when safe | Workstream board | Dependencies clear |
| PAR06 | Parallel data checks | Run schema, null, duplicate, and reconciliation checks independently | Data QA pack | Checks complete |
| PAR07 | Parallel audience versions | Produce versions for exec, technical, and public readers | Audience pack | Version labels |
| PAR08 | Parallel localization | Localize by locale with shared glossary and QA merge | Locale workstream map | Glossary applied |
| PAR09 | Parallel vendor evaluation | Score vendors independently, then normalize results | Vendor score pack | Comparable criteria |
| PAR10 | Parallel asset production | Produce channel variants from approved master asset | Asset variant pack | Master invariants |

## LOP Loop / Iteration Controls

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| LOP01 | Draft-review-revise loop | Iterate until review findings are resolved or accepted | Revision log | Findings addressed |
| LOP02 | Generate-select-refine loop | Generate variants, select winner, refine, QA | Variant log | Winner passes criteria |
| LOP03 | Test-fix-retest loop | Run test, fix failure, rerun until pass or blocked | Test loop log | Pass or residual risk |
| LOP04 | Prompt-repair loop | Identify failure mode, revise prompt, retest on same case | Prompt repair log | Failure reduced |
| LOP05 | Data-cleaning loop | Profile, clean, validate, repeat until quality threshold | DQ loop note | Threshold met |
| LOP06 | Stakeholder-feedback loop | Collect feedback, classify, decide, revise, log | Feedback log | Decisions recorded |
| LOP07 | Experiment-learning loop | Hypothesis, test, analyze, decide next experiment | Experiment log | Learning captured |
| LOP08 | Design-critique loop | Critique, repair, compare, choose final | Design iteration log | Brief fit |
| LOP09 | Ops-improvement loop | Monitor, find bottleneck, improve, measure again | Improvement loop | Metric movement |
| LOP10 | Learning-practice loop | Attempt, feedback, drill, reassess | Learning loop | Progress shown |

## ESC Escalation / Human Review

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| ESC01 | Legal escalation | Escalate legal conclusions, filing, or disputes to counsel | Counsel questions | Legal boundary |
| ESC02 | Medical escalation | Escalate diagnosis/treatment/emergency to clinician or emergency care | Clinician prep | No diagnosis |
| ESC03 | Financial escalation | Escalate tax, investment, or debt decisions to qualified advisor | Advisor packet | Assumptions shown |
| ESC04 | Security escalation | Escalate active incident or exploitability to authorized security owner | Security escalation | Authorization |
| ESC05 | Privacy escalation | Escalate personal data processing risk to privacy owner | Privacy review note | Data mapped |
| ESC06 | Engineering escalation | Escalate production-risk changes to maintainer/reviewer | Eng review ask | Risk described |
| ESC07 | Compliance escalation | Escalate regulated claims or obligations to compliance reviewer | Compliance packet | Rule references |
| ESC08 | Executive escalation | Escalate blocked decisions, budget, or priority conflicts | Exec decision ask | Options clear |
| ESC09 | Customer escalation | Escalate severe customer harm, SLA breach, or churn risk | Customer escalation | Owner/update time |
| ESC10 | Safety escalation | Escalate physical safety/manufacturing uncertainty to qualified expert | Safety review ask | Hazard stated |

## FBK Fallback / Degraded Mode

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| FBK01 | No-network fallback | Use local/provided sources and mark freshness limits | Offline note | Limits clear |
| FBK02 | No-tool fallback | Use manual process and report verification limits | Manual fallback | Feasible path |
| FBK03 | Missing-file fallback | Use available context, request exact file, or create scaffold | Missing-file note | Missing item named |
| FBK04 | Low-evidence fallback | Provide framework plus evidence gaps, not firm conclusion | Low-evidence brief | Gaps visible |
| FBK05 | Timebox fallback | Deliver minimum viable answer and list deferred checks | Timebox output | Deferred work |
| FBK06 | Budget fallback | Use lower-cost method and state tradeoffs | Lean plan | Quality floor |
| FBK07 | Tool-error fallback | Capture error, retry safe alternative, report failure | Tool fallback log | Error preserved |
| FBK08 | Data-quality fallback | Use partial data with caveats or stop analysis | Data fallback note | Caveats |
| FBK09 | Model-output fallback | If output poor, switch prompt pattern or reduce scope | Model fallback | Failure mode |
| FBK10 | Approval-delay fallback | Keep artifact as draft and prepare approval packet | Draft fallback | Not published |

## ROL Rollback / Reversibility

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| ROL01 | Code rollback | Define revert path before risky code/deploy change | Rollback note | Revert command/path |
| ROL02 | Content rollback | Keep prior published version and restore plan | Content rollback plan | Prior version known |
| ROL03 | Data rollback | Backup/source snapshot before transformation | Data rollback note | Snapshot identified |
| ROL04 | Config rollback | Record previous config and validation step | Config rollback plan | Old value known |
| ROL05 | Automation rollback | Disable trigger, stop job, restore manual path | Automation rollback | Manual path |
| ROL06 | Campaign rollback | Pause campaign, remove assets, issue correction if needed | Campaign rollback | Pause owner |
| ROL07 | Design rollback | Preserve previous design asset and compare changes | Design rollback note | Versioned asset |
| ROL08 | Vendor rollback | Define exit, transition, and data retrieval path | Vendor rollback plan | Exit criteria |
| ROL09 | Policy rollback | Communicate reversal, effective date, and interim rule | Policy rollback | Stakeholders notified |
| ROL10 | Release rollback | Health check -> rollback trigger -> restore -> communicate | Release rollback | Trigger defined |

## DEP Dependency / Prerequisite Controls

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| DEP01 | Input dependency | Identify required files/data before execution | Dependency list | Inputs available |
| DEP02 | Tool dependency | Identify required tools, permissions, and fallbacks | Tool dependency note | Tool ready |
| DEP03 | People dependency | Identify reviewers, owners, and approvers | People dependency map | Owner named |
| DEP04 | Data dependency | Identify source freshness, schema, access, and joins | Data dependency note | Access/grain |
| DEP05 | Legal dependency | Identify legal/compliance review before publication | Legal dependency | Review gate |
| DEP06 | Design dependency | Identify brand assets, templates, dimensions, specs | Design dependency note | Assets available |
| DEP07 | Engineering dependency | Identify services, env vars, build/test systems | Eng dependency note | Environment ready |
| DEP08 | Timeline dependency | Identify predecessor tasks and critical path | Timeline dependency | Critical path |
| DEP09 | Vendor dependency | Identify external deliverables and SLA risks | Vendor dependency | SLA/owner |
| DEP10 | Approval dependency | Identify decision makers and required evidence | Approval dependency | Decision criteria |

## SLA Time / Service-Level Controls

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| SLA01 | Response-time SLA | Define expected response/update timing | SLA note | Next update time |
| SLA02 | Review SLA | Define reviewer deadline and escalation | Review SLA | Deadline/owner |
| SLA03 | Incident SLA | Severity -> response -> resolution target -> comms cadence | Incident SLA | Severity mapped |
| SLA04 | Support SLA | Ticket class -> owner -> response -> resolution | Support SLA | SLA visible |
| SLA05 | Data refresh SLA | Source -> refresh cadence -> freshness threshold | Data SLA | Freshness stated |
| SLA06 | Production turnaround SLA | Deliverable -> timeline -> QA windows -> handoff | Production SLA | Gates scheduled |
| SLA07 | Approval SLA | Approval type -> deadline -> fallback if late | Approval SLA | Fallback |
| SLA08 | Vendor SLA | Vendor deliverable -> due date -> acceptance -> penalty/escalation | Vendor SLA | Acceptance |
| SLA09 | Monitoring SLA | Metric -> threshold -> check cadence -> owner | Monitoring SLA | Owner/cadence |
| SLA10 | Closeout SLA | Completion -> archive -> summary -> next action deadline | Closeout SLA | Closeout date |

## RCT Risk Control / Safeguards

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| RCT01 | High-risk safeguard | Add explicit risk gate before final answer | Risk control note | Risk handled |
| RCT02 | PII safeguard | Minimize, redact, and limit sharing | Privacy control | PII protected |
| RCT03 | Claim safeguard | Require substantiation for public or regulated claims | Claim control | Evidence linked |
| RCT04 | Safety safeguard | Add hazard warning and expert review for physical safety | Safety control | Hazard named |
| RCT05 | Security safeguard | Remove secrets/abuse detail and keep defensive scope | Security control | No secret leakage |
| RCT06 | Financial safeguard | Use scenarios and caveats, avoid personal advice | Finance control | Assumptions |
| RCT07 | Legal safeguard | Provide issue spotting and counsel questions | Legal control | Boundary visible |
| RCT08 | Quality safeguard | Use verification matrix before final handoff | QA control | Checks selected |
| RCT09 | Reputation safeguard | Check tone, facts, stakeholders, and approval | Reputation control | Approval path |
| RCT10 | Accessibility safeguard | Add plain-language/accessibility checks | Accessibility control | User access |

## HOF Handoff / Ownership Controls

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| HOF01 | Step handoff | Each step outputs exact artifact for next step | Step handoff | Artifact named |
| HOF02 | Owner handoff | Assign owner, next action, and deadline | Owner handoff | Owner/date |
| HOF03 | Reviewer handoff | Provide artifact, criteria, questions, and context | Reviewer packet | Reviewable |
| HOF04 | Developer handoff | Provide requirements, files, tests, risks | Dev handoff | Implementable |
| HOF05 | Designer handoff | Provide brief, assets, dimensions, constraints | Design handoff | Production-ready |
| HOF06 | Data handoff | Provide schema, query, assumptions, caveats | Data handoff | Reproducible |
| HOF07 | Ops handoff | Provide runbook, triggers, escalation, records | Ops handoff | Runnable |
| HOF08 | Customer handoff | Provide clear next step, support path, expectations | Customer handoff | No ambiguity |
| HOF09 | Archive handoff | Provide index, versions, retention, access | Archive handoff | Retrievable |
| HOF10 | Resume handoff | Provide current state, completed work, blockers, next step | Resume note | Future agent can continue |

## EVD Evidence / Audit Trail Controls

| Code | Control | Workflow rule | Gate output | Pass condition |
|---|---|---|---|---|
| EVD01 | Decision evidence | Record decision, rationale, options, owner, date | Decision record | Rationale captured |
| EVD02 | Source evidence | Record source URL/path, date, claim, confidence | Source log | Traceable |
| EVD03 | Test evidence | Record command/test, result, failure, fix | Test log | Result visible |
| EVD04 | Review evidence | Record reviewer, findings, disposition, residual risk | Review log | Disposition |
| EVD05 | Approval evidence | Record approver, date, conditions, version | Approval log | Audit-ready |
| EVD06 | Change evidence | Record changed files/assets, reason, verification | Change log | Traceable |
| EVD07 | Data evidence | Record query, dataset version, row counts, caveats | Data evidence note | Reproducible |
| EVD08 | Production evidence | Record specs, samples, inspection, disposition | Production evidence | Acceptance proof |
| EVD09 | Incident evidence | Record timeline, impact, actions, owners | Incident evidence | Timeline clear |
| EVD10 | Handoff evidence | Record final artifacts, paths, owners, next actions | Handoff evidence | Complete handoff |
