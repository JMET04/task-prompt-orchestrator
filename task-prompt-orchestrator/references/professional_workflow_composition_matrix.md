# Professional Workflow Composition Matrix

Use this when the user wants a real workflow rather than a single prompt or isolated task. This matrix defines reusable end-to-end workflow recipes: phases, branching points, gates, outputs, and handoffs.

Selection rule:

1. Select scenario axes first: P-code, operation, input, audience, constraints, lifecycle, verification, and prompt pattern.
2. Choose one workflow composition code here when the task spans multiple steps, people, tools, or deliverables.
3. Convert the workflow recipe into prompt packets with `Step ID`, `Inputs`, `Procedure`, `Output`, `Done when`, and `Handoff`.
4. Never call a workflow complete until its gates pass or residual risks are explicitly reported.

## END End-to-End Delivery Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| END01 | Intake-to-delivery | Intake -> optimized brief -> plan -> execute -> verify -> handoff | Delivery package | Scope, QA, handoff |
| END02 | Brief-to-production | Brief -> references -> draft/asset -> review -> final export | Production-ready artifact | Brief alignment |
| END03 | Request-to-decision | Clarify decision -> options -> criteria -> evidence -> recommendation | Decision memo | Criteria and tradeoffs |
| END04 | Problem-to-solution | Problem frame -> root cause -> options -> selected fix -> validation | Solution plan | Cause evidence |
| END05 | Raw-material-to-report | Inventory -> extract -> analyze -> synthesize -> QA | Report | Evidence and structure |
| END06 | Idea-to-prototype | Idea -> requirements -> prototype -> test -> iterate | Prototype package | Test feedback |
| END07 | Draft-to-publication | Draft -> edit -> fact/rights check -> approval -> publish | Publication package | Approval and rights |
| END08 | Data-to-insight | Source -> clean -> analyze -> visualize -> recommendation | Insight report | Data QA |
| END09 | Asset-to-campaign | Asset pool -> concept -> variants -> channel specs -> launch | Campaign pack | Channel fit |
| END10 | Issue-to-closeout | Issue -> triage -> fix/action -> verify -> document closeout | Closeout note | Resolution evidence |

## RSW Research Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| RSW01 | Quick research brief | Question -> source scan -> evidence notes -> synthesis -> caveats | Quick brief | Freshness boundary |
| RSW02 | Deep research dossier | Scope -> source map -> evidence table -> themes -> implications | Research dossier | Source authority |
| RSW03 | Literature review workflow | Research question -> search protocol -> screening -> synthesis -> gaps | Literature review | Reproducible search |
| RSW04 | Fact-check workflow | Claim extraction -> source verification -> verdict -> correction -> confidence | Fact-check report | Verdict per claim |
| RSW05 | Competitive research workflow | Market frame -> competitor set -> dimensions -> matrix -> plays | Competitive report | Comparable basis |
| RSW06 | Policy/regulatory research | Jurisdiction -> authority tree -> obligations -> implementation notes | Policy brief | Version/date |
| RSW07 | Expert interview synthesis | Interview guide -> notes/transcript -> themes -> quotes -> recommendations | Interview report | Quote trace |
| RSW08 | Dataset discovery workflow | Source discovery -> metadata -> access/license -> sample -> fit score | Dataset inventory | License/access |
| RSW09 | Trend scan workflow | Signals -> drivers -> evidence -> impact -> watchlist | Trend report | Dated signals |
| RSW10 | Research-to-action workflow | Findings -> implications -> options -> recommendation -> next tests | Action brief | Evidence-linked |

## CRW Creative Production Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| CRW01 | Creative brief-to-routes | Brief -> audience insight -> 3 routes -> rationale -> selection | Concept routes | Distinct routes |
| CRW02 | Image2 production workflow | Reference -> invariants -> prompt -> variants -> repair -> final | Image prompt/asset pack | Invariants preserved |
| CRW03 | Packaging visual workflow | Product -> structure -> panels -> visual system -> mockup -> QA | Packaging concept pack | Print/structure caveat |
| CRW04 | CAD prompt workflow | Object -> views -> line rules -> dimensions/callouts -> output QA | Technical prompt pack | No decorative drift |
| CRW05 | Campaign asset workflow | Message -> master KV -> channel variants -> copy -> publish checks | Campaign asset pack | Channel specs |
| CRW06 | Brand identity workflow | Strategy -> attributes -> visual system -> rules -> examples | Identity system brief | Consistency |
| CRW07 | Video creative workflow | Hook -> storyboard -> script -> shot list -> edit brief -> QA | Video production brief | Timing and CTA |
| CRW08 | UGC workflow | Creator angle -> script -> shot list -> compliance -> variants | UGC brief | Natural and compliant |
| CRW09 | Design critique-to-repair | Output -> critique -> prioritized fixes -> revised prompt/spec -> QA | Repair plan | One issue per pass |
| CRW10 | Asset library workflow | Assets -> naming -> metadata -> rights -> variants -> archive | Asset library index | Rights and retrieval |

## CTW Content / Document Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| CTW01 | Outline-to-draft | Audience -> outline -> evidence -> draft -> edit -> final | Draft document | Completeness |
| CTW02 | Source-to-summary | Source inventory -> extraction -> summary -> caveats -> QA | Summary | Source boundary |
| CTW03 | Long-form content workflow | Thesis -> structure -> sections -> examples -> polish -> publish | Long-form article | Flow and proof |
| CTW04 | Technical documentation workflow | Product/API -> user tasks -> steps -> examples -> troubleshooting | Technical docs | Runnable examples |
| CTW05 | Proposal writing workflow | Requirements -> win themes -> solution -> proof -> compliance matrix | Proposal draft | Requirement coverage |
| CTW06 | Case study workflow | Customer -> problem -> solution -> results -> proof -> approval | Case study | Outcome evidence |
| CTW07 | SOP workflow | Trigger -> roles -> steps -> exceptions -> records -> review | SOP | Operator-ready |
| CTW08 | Localization content workflow | Source -> glossary -> translation -> cultural QA -> final | Localized content | Terminology |
| CTW09 | Executive memo workflow | Decision -> context -> options -> recommendation -> risks | Executive memo | Clear ask |
| CTW10 | Multi-channel content workflow | Master message -> platform variants -> schedule -> QA -> publish | Content pack | Platform fit |

## DAW Data / Analytics Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| DAW01 | Data profiling workflow | Source -> schema -> quality checks -> sample -> risks | Data profile | Types/missingness |
| DAW02 | KPI reporting workflow | Metric definitions -> query -> QA -> visualization -> narrative | KPI report | Definition trace |
| DAW03 | Funnel analysis workflow | Stages -> data extraction -> dropoff analysis -> segments -> actions | Funnel report | Stage logic |
| DAW04 | Cohort workflow | Cohort definition -> retention table -> segment cuts -> drivers | Cohort report | Cohort grain |
| DAW05 | Experiment readout workflow | Design -> data QA -> stats -> guardrails -> decision | Experiment readout | Assignment/guardrails |
| DAW06 | Dashboard build workflow | Audience -> decisions -> metrics -> layout -> validation -> handoff | Dashboard spec/report | Decision fit |
| DAW07 | Forecast workflow | Target -> features -> baseline -> model/scenarios -> error report | Forecast brief | Error metric |
| DAW08 | Data discrepancy workflow | Metric mismatch -> source trace -> reconciliation -> fix | Discrepancy report | Variance explained |
| DAW09 | Survey analysis workflow | Instrument -> cleaning -> coding -> tables -> insights | Survey report | Sample caveat |
| DAW10 | Semantic layer workflow | Terms -> metric formulas -> dimensions -> joins -> governance | Metric dictionary | Unambiguous definitions |

## ENW Engineering / Build Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| ENW01 | Repo-orientation workflow | Files -> architecture -> commands -> risks -> plan | Repo map | Commands verified |
| ENW02 | Feature build workflow | Requirement -> design -> implementation -> tests -> docs -> handoff | Feature change | Tests pass/caveat |
| ENW03 | Bug fix workflow | Repro -> trace -> patch -> test -> regression note | Bug fix | Repro and retest |
| ENW04 | Refactor workflow | Current behavior -> target design -> small patches -> tests | Refactor plan/change | Behavior preserved |
| ENW05 | Migration workflow | Current -> target -> compatibility -> steps -> rollback | Migration plan | Rollback path |
| ENW06 | Performance workflow | Baseline -> bottleneck -> change -> benchmark -> report | Performance patch/plan | Before/after |
| ENW07 | Security fix workflow | Finding -> exploitability -> remediation -> validation -> note | Security fix | Risk reduced |
| ENW08 | API integration workflow | Contract -> auth -> client/server changes -> error handling -> tests | Integration change | Edge cases |
| ENW09 | CI/CD workflow | Pipeline -> failing gate -> config/secret review -> fix -> rerun | CI/CD fix | Gate result |
| ENW10 | Release workflow | Change list -> risk -> build/test -> deploy plan -> monitor | Release checklist | Health/rollback |

## RVW Review / QA Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| RVW01 | Finding-first review | Artifact -> criteria -> findings -> severity -> fixes | Review findings | Evidence references |
| RVW02 | Acceptance test workflow | Requirement -> test cases -> execution -> pass/fail -> gaps | Acceptance report | Testable criteria |
| RVW03 | Fact/citation audit workflow | Claims -> sources -> mismatch -> replacements -> caveats | Citation audit | No unsupported claims |
| RVW04 | Design QA workflow | Brief -> visual check -> accessibility -> variants -> repair | Design QA report | Actionable fixes |
| RVW05 | Data QA workflow | Schema -> counts -> joins -> metrics -> anomalies | Data QA report | Reconciled counts |
| RVW06 | Compliance QA workflow | Requirements -> evidence -> gaps -> remediation owners | Compliance QA | Clause/control trace |
| RVW07 | Code review workflow | Diff -> behavior risks -> tests -> findings -> summary | Code review | File/line evidence |
| RVW08 | Publication QA workflow | Content -> facts -> rights -> tone -> final approval | Publication checklist | Rights/facts |
| RVW09 | Production QA workflow | Spec -> prototype/sample -> inspection -> disposition | Production QA | Acceptance criteria |
| RVW10 | Handoff readiness workflow | Deliverable -> docs -> owner -> next actions -> archive | Handoff checklist | User can resume |

## APW Approval / Governance Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| APW01 | Approval packet workflow | Artifact -> decision needed -> evidence -> risks -> ask | Approval packet | Decision clear |
| APW02 | Multi-stakeholder signoff | Stakeholders -> criteria -> conflicts -> review cadence -> log | Signoff plan | Decision rights |
| APW03 | Legal/compliance approval | Claims -> rules -> evidence -> caveats -> review status | Review checklist | Status explicit |
| APW04 | Budget approval workflow | Need -> cost -> alternatives -> ROI/risk -> ask | Budget request | Assumptions |
| APW05 | Change control workflow | Change -> impact -> rollback -> approvals -> communication | Change record | Rollback defined |
| APW06 | Vendor approval workflow | Vendor -> evidence -> risks -> controls -> recommendation | Vendor approval memo | Evidence requested |
| APW07 | Data access approval | Purpose -> data -> roles -> controls -> expiry -> audit | Access request | Least privilege |
| APW08 | Publication approval workflow | Content -> facts -> rights -> brand/legal -> schedule | Publication approval | Final gate |
| APW09 | Governance log workflow | Decisions -> rationale -> owners -> dates -> follow-up | Decision log | Audit trail |
| APW10 | Exception approval workflow | Exception -> risk -> compensating control -> expiry -> owner | Exception record | Time-bound |

## OPW Operations / Run Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| OPW01 | Runbook workflow | Trigger -> steps -> verification -> escalation -> record | Runbook | Usable during incident |
| OPW02 | SOP rollout workflow | Draft SOP -> training -> pilot -> feedback -> final | SOP rollout pack | Adoption checked |
| OPW03 | Support workflow | Intake -> triage -> response -> resolution -> follow-up | Support playbook | SLA/quality |
| OPW04 | Vendor operations workflow | SLA -> reporting -> issue log -> escalation -> review | Vendor ops pack | SLA measurable |
| OPW05 | Inventory operations workflow | Demand -> stock -> reorder -> exceptions -> review | Inventory ops plan | Exception path |
| OPW06 | Content operations workflow | Intake -> production -> review -> publish -> archive | Content ops workflow | Status visible |
| OPW07 | Data operations workflow | Refresh -> validation -> exceptions -> distribution -> monitor | Data ops checklist | Freshness |
| OPW08 | Access operations workflow | Request -> approval -> provisioning -> review -> revoke | Access workflow | Audit trail |
| OPW09 | Quality operations workflow | Standard -> inspection -> defect log -> CAPA -> trend | Quality ops workflow | Defect taxonomy |
| OPW10 | Operating cadence workflow | Goals -> meetings -> metrics -> decisions -> artifacts | Cadence system | Purpose per meeting |

## IRW Incident / Recovery Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| IRW01 | Incident triage workflow | Alert -> impact -> severity -> owner -> first action | Triage note | Severity clear |
| IRW02 | Customer escalation workflow | Facts -> impact -> response -> owner -> next update | Escalation plan | Update time |
| IRW03 | Security incident workflow | Scope -> containment -> evidence -> remediation -> report | Security incident pack | Authorization/safety |
| IRW04 | Data incident workflow | Discrepancy/breach -> scope -> containment -> correction -> notice path | Data incident note | Facts separated |
| IRW05 | Production defect workflow | Defect -> containment -> disposition -> root cause -> CAPA | Defect response | Customer impact |
| IRW06 | Crisis comms workflow | Known/unknown -> holding statement -> approvals -> updates | Crisis comms pack | No speculation |
| IRW07 | Outage recovery workflow | Alert -> mitigation -> validation -> communication -> postmortem | Outage workflow | Service restored |
| IRW08 | Rollback workflow | Bad change -> rollback criteria -> execution -> validation -> record | Rollback plan | Recovery proof |
| IRW09 | Postmortem workflow | Timeline -> impact -> causes -> actions -> owners | Postmortem | Actions measurable |
| IRW10 | Lessons-to-prevention workflow | Incident -> patterns -> controls -> monitoring -> training | Prevention plan | Control owner |

## ATW Automation / Agent Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| ATW01 | Automation discovery workflow | Process -> triggers -> exceptions -> ROI -> candidate score | Automation assessment | Exceptions quantified |
| ATW02 | Agent workflow design | Goal -> tools -> memory -> steps -> review gates -> eval | Agent workflow spec | Human gates |
| ATW03 | Document automation workflow | Source -> extraction -> generation -> approval -> delivery | Doc automation spec | Approval before send |
| ATW04 | Reporting automation workflow | Metrics -> refresh -> validation -> distribution -> monitoring | Reporting automation | Freshness/QA |
| ATW05 | Support bot workflow | Intents -> retrieval -> answer policy -> fallback -> eval | Bot workflow spec | Escalation |
| ATW06 | QA automation workflow | Journeys -> test data -> selectors -> CI -> flake handling | QA automation plan | Stable tests |
| ATW07 | Data pipeline workflow | Sources -> transform -> validation -> load -> alerts | Pipeline workflow | Data checks |
| ATW08 | Approval automation workflow | Request -> rules -> approvers -> audit -> exceptions | Approval automation | Audit trail |
| ATW09 | Email automation workflow | Trigger -> segmentation -> content -> compliance -> logs | Email automation spec | Opt-out/compliance |
| ATW10 | Automation governance workflow | Inventory -> owners -> logs -> monitoring -> change control | Automation governance | Orphans flagged |

## LRW Learning / Enablement Workflows

| Code | Workflow | Recipe | Deliverables | Gates |
|---|---|---|---|---|
| LRW01 | Lesson workflow | Objective -> explanation -> examples -> practice -> assessment | Lesson plan | Objective measurable |
| LRW02 | Study-plan workflow | Goal/exam -> topics -> schedule -> drills -> review | Study plan | Coverage and cadence |
| LRW03 | Training module workflow | Role -> skill -> scenarios -> practice -> feedback | Training module | Transfer to work |
| LRW04 | Coaching workflow | Goal -> current state -> blocker -> drill -> reflection | Coaching plan | Next action |
| LRW05 | Rubric workflow | Task -> criteria -> levels -> examples -> feedback | Rubric | Levels distinct |
| LRW06 | Diagnostic workflow | Learner output -> misconception -> cause -> remediation | Diagnostic feedback | Evidence from work |
| LRW07 | Workshop workflow | Outcome -> agenda -> activities -> artifacts -> follow-up | Workshop plan | Timeboxed |
| LRW08 | Enablement workflow | Audience -> talk track -> job aids -> practice -> metrics | Enablement pack | Role-ready |
| LRW09 | Certification prep workflow | Objectives -> baseline -> plan -> questions -> review loop | Prep workflow | Objective coverage |
| LRW10 | Knowledge transfer workflow | Context -> concepts -> examples -> checklist -> handoff | KT package | Future user can resume |
