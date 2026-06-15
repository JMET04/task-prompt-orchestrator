# Professional Lifecycle Stage Matrix

Use this when the user request depends on project phase, maturity, or operating context. The same task needs different prompts at intake, discovery, strategy, planning, production, review, approval, launch, operations, monitoring, troubleshooting, optimization, and retirement.

Selection rule:

1. Select the normal P-code plus any industry, deliverable, high-risk, or deep-domain code first.
2. Select one lifecycle code here to set the phase-specific procedure and acceptance checks.
3. Put the lifecycle row into the prompt packet under `Procedure`, `Done when`, and `Handoff`.
4. When phase is unclear, infer from the user's wording; ask only if the phase changes the deliverable materially.

## INI Intake / Scoping

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INI01 | Vague request intake | Goal -> known inputs -> unknowns -> assumptions -> first deliverable | Intake brief | Blocking unknowns separated |
| INI02 | Stakeholder goal capture | Stakeholders -> outcomes -> constraints -> success criteria | Goal brief | Success criteria testable |
| INI03 | File/material intake | Inventory -> relevance -> gaps -> access issues -> next reads | Material inventory | Missing inputs listed |
| INI04 | Scope boundary | Request -> in scope -> out of scope -> risks -> handoff | Scope note | Boundary explicit |
| INI05 | Tool/capability selection | Task -> available tools -> fit -> fallback -> execution path | Tool plan | Existing capability preferred |
| INI06 | Prompt optimization before work | Raw ask -> sharpened brief -> output shape -> quality bar | Optimized prompt brief | Original intent preserved |
| INI07 | Quick feasibility check | Desired output -> constraints -> blockers -> viable path | Feasibility note | Go/no-go reason |
| INI08 | Data/privacy intake | Inputs -> sensitive fields -> minimization -> handling rules | Data handling note | Sensitive data protected |
| INI09 | Time/budget triage | Deadline -> effort -> tradeoffs -> priority path | Triage plan | Tradeoffs visible |
| INI10 | First milestone definition | Goal -> milestone -> evidence -> owner -> next step | Milestone definition | Completion evidence named |

## DSC Discovery / Research

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| DSC01 | Background discovery | Topic -> source map -> facts -> uncertainties -> synthesis | Background brief | Sources scoped |
| DSC02 | User/customer discovery | Target users -> questions -> evidence -> themes | Discovery plan | Questions non-leading |
| DSC03 | Competitor discovery | Category -> competitors -> dimensions -> evidence -> gaps | Competitive scan | Comparables fair |
| DSC04 | Technical discovery | System -> dependencies -> constraints -> risks -> options | Technical discovery note | Unknowns flagged |
| DSC05 | Policy/regulatory discovery | Jurisdiction -> authority -> obligations -> versions | Regulatory scan | Date/version shown |
| DSC06 | Data discovery | Tables/files -> fields -> quality -> joins -> limitations | Data discovery report | Data limits stated |
| DSC07 | Asset discovery | Existing assets -> quality -> rights -> reuse potential | Asset inventory | Rights status noted |
| DSC08 | Stakeholder discovery | Actors -> interests -> influence -> risks -> messages | Stakeholder map | Power/interest clear |
| DSC09 | Problem framing | Symptoms -> causes -> evidence -> core problem | Problem statement | Cause not assumed |
| DSC10 | Opportunity discovery | Pain -> underserved need -> constraints -> wedge | Opportunity brief | Evidence-backed |

## STR Strategy / Direction

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| STR01 | Strategic options | Context -> options -> criteria -> tradeoffs -> recommendation | Options memo | Criteria explicit |
| STR02 | Positioning strategy | Audience -> alternatives -> differentiators -> message | Positioning brief | Differentiation specific |
| STR03 | Roadmap strategy | Goals -> bets -> sequencing -> dependencies -> metrics | Roadmap brief | Sequencing justified |
| STR04 | Channel strategy | Audience -> channels -> message fit -> resources -> plan | Channel strategy | Fit to audience |
| STR05 | Risk strategy | Objectives -> risks -> mitigations -> owners -> triggers | Risk strategy | Triggers defined |
| STR06 | Pricing/packaging direction | Segments -> value metric -> packages -> constraints | Packaging strategy | Margin/risk considered |
| STR07 | Data/measurement strategy | Decisions -> metrics -> instrumentation -> cadence | Measurement strategy | Metrics decision-linked |
| STR08 | Brand/content strategy | Audience -> voice -> pillars -> formats -> governance | Content strategy | Pillars actionable |
| STR09 | Partnership strategy | Goals -> partner types -> value exchange -> outreach | Partnership strategy | Mutual value |
| STR10 | Exit/stop strategy | Current effort -> signals -> sunset path -> communication | Stop strategy | Stop criteria clear |

## PLN Planning / Design

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| PLN01 | Work breakdown | Goal -> workstreams -> tasks -> dependencies -> owners | Work plan | Dependencies visible |
| PLN02 | Project schedule | Milestones -> durations -> blockers -> review gates | Schedule plan | Critical dates clear |
| PLN03 | Requirements planning | Users -> needs -> requirements -> acceptance tests | Requirement plan | Testable requirements |
| PLN04 | Experiment planning | Hypothesis -> design -> metrics -> guardrails -> sample | Experiment plan | Hypothesis measurable |
| PLN05 | Content plan | Audience -> topics -> formats -> cadence -> owners | Content calendar | Cadence realistic |
| PLN06 | Production plan | Assets -> process -> roles -> timeline -> QA | Production plan | QA gate included |
| PLN07 | Resource plan | Scope -> people/tools/budget -> constraints -> gaps | Resource plan | Gaps visible |
| PLN08 | Change plan | Change -> stakeholders -> training -> comms -> adoption | Change plan | Adoption measured |
| PLN09 | Test plan | Risks -> cases -> data -> environments -> gates | Test plan | Risk coverage |
| PLN10 | Review plan | Artifacts -> reviewers -> criteria -> timing -> decisions | Review plan | Decision rights clear |

## PRD Production / Creation

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| PRD01 | Draft creation | Brief -> outline -> draft -> self-check -> handoff | Draft artifact | Matches brief |
| PRD02 | Asset generation | Brief -> prompt -> variants -> selection -> repair | Asset set | Variants named |
| PRD03 | Code/build implementation | Requirement -> code changes -> tests -> verification | Implemented change | Tests/risk noted |
| PRD04 | Document production | Structure -> sections -> evidence -> edits -> final | Document draft | Claims supported |
| PRD05 | Deck production | Story -> slides -> visuals -> notes -> QA | Slide deck | Narrative coherent |
| PRD06 | Data product build | Source -> transform -> model/chart -> QA -> export | Data artifact | Logic validated |
| PRD07 | Campaign production | Message -> creative -> variants -> channel specs | Campaign assets | Channel-native |
| PRD08 | SOP/process creation | Trigger -> steps -> exceptions -> controls -> records | SOP draft | Operator-ready |
| PRD09 | Training material creation | Objectives -> content -> practice -> assessment | Training pack | Learner action clear |
| PRD10 | Batch generation | Variables -> template -> batch -> naming -> QA | Batch output pack | Variables isolated |

## REV Review / QA

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| REV01 | Editorial review | Draft -> clarity -> structure -> tone -> edits | Edit report | Meaning preserved |
| REV02 | Technical review | Artifact -> requirements -> edge cases -> risks -> fixes | Technical review | Evidence specific |
| REV03 | Compliance review | Artifact -> rules -> gaps -> remediation -> owner | Compliance review | Rule references |
| REV04 | Design review | Objective -> hierarchy -> usability -> brand -> fixes | Design critique | Actionable fixes |
| REV05 | Data QA | Data -> definitions -> calculations -> anomalies -> fixes | Data QA report | Reproducible checks |
| REV06 | Security review | System/content -> threats -> controls -> gaps | Security review | Risk severity |
| REV07 | Accessibility review | Artifact -> WCAG/plain language -> barriers -> fixes | Accessibility review | User-impact framed |
| REV08 | Legal/risk review | Claims -> evidence -> rights -> caveats -> review gate | Risk review | Claims substantiated |
| REV09 | Test execution | Test plan -> run -> failures -> fixes -> retest | Test report | Pass/fail trace |
| REV10 | Final polish | Artifact -> consistency -> formatting -> references -> final | Polished artifact | No obvious defects |

## APR Approval / Governance

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| APR01 | Approval packet | Artifact -> decision needed -> evidence -> risks -> ask | Approval packet | Decision clear |
| APR02 | Executive signoff | Summary -> options -> recommendation -> implications | Signoff memo | Exec-readable |
| APR03 | Legal/compliance signoff | Artifact -> claims -> rules -> open issues -> owner | Review checklist | Review status explicit |
| APR04 | Brand approval | Asset -> guidelines -> deviations -> rationale -> fixes | Brand approval note | Guideline references |
| APR05 | Budget approval | Cost -> benefit -> alternatives -> risks -> decision | Budget request | Assumptions visible |
| APR06 | Change approval | Change -> impact -> rollback -> communication -> timing | Change approval record | Rollback defined |
| APR07 | Vendor approval | Vendor -> fit -> risks -> controls -> recommendation | Vendor approval memo | Evidence requested |
| APR08 | Publication approval | Content -> facts -> rights -> timing -> final gate | Publication checklist | Rights/facts checked |
| APR09 | Data access approval | Request -> purpose -> data -> controls -> expiration | Access request | Least privilege |
| APR10 | Governance log | Decisions -> owners -> dates -> rationale -> follow-up | Decision log | Audit trail |

## LAU Launch / Release

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| LAU01 | Launch plan | Goal -> audience -> channels -> timeline -> owners | Launch plan | Owners and dates |
| LAU02 | Release checklist | Changes -> gates -> monitoring -> rollback -> comms | Release checklist | Rollback path |
| LAU03 | Go-to-market activation | Segments -> messages -> offers -> channels -> KPIs | GTM activation plan | KPIs defined |
| LAU04 | Content publishing | Asset -> channel specs -> metadata -> schedule -> QA | Publishing plan | Channel fit |
| LAU05 | Training rollout | Audience -> materials -> sessions -> support -> measurement | Training rollout plan | Adoption measured |
| LAU06 | Customer announcement | News -> impact -> action -> FAQ -> support | Announcement pack | Clear action |
| LAU07 | Internal enablement | Change -> teams -> talk tracks -> objections -> assets | Enablement pack | Team-ready |
| LAU08 | Incident-ready launch | Launch -> risks -> monitoring -> response -> owner | Launch risk plan | Escalation paths |
| LAU09 | Localization launch | Locales -> assets -> QA -> timing -> market constraints | Local launch plan | Locale QA |
| LAU10 | Launch retrospective setup | Goals -> metrics -> data plan -> review date | Retro setup | Measurement ready |

## OPR Operations / Run

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| OPR01 | Runbook use | Alert/task -> context -> steps -> verification -> escalation | Runbook execution note | Steps verifiable |
| OPR02 | Routine operating cadence | Metrics -> meetings -> decisions -> owners -> records | Cadence plan | Meeting purpose clear |
| OPR03 | Service support | User issue -> triage -> response -> resolution -> follow-up | Support workflow | SLA considered |
| OPR04 | Process handoff | Source team -> receiving team -> inputs -> checklist | Handoff checklist | Ownership clear |
| OPR05 | Vendor operation | SLA -> reporting -> issues -> escalation -> review | Vendor ops note | SLA measurable |
| OPR06 | Content operations | Pipeline -> status -> blockers -> approvals -> publish | Content ops board | Status current |
| OPR07 | Data operations | Refresh -> validation -> exceptions -> distribution | Data ops checklist | Freshness stated |
| OPR08 | Inventory operations | Demand -> stock -> reorder -> exceptions -> owner | Inventory ops plan | Exceptions handled |
| OPR09 | Knowledge base upkeep | Feedback -> outdated articles -> refresh -> archive | KB maintenance plan | Owner/date |
| OPR10 | Access operations | Requests -> approvals -> provisioning -> review -> revoke | Access ops flow | Audit trail |

## MON Monitoring / Measurement

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| MON01 | KPI monitoring | Metrics -> thresholds -> changes -> drivers -> action | KPI monitor brief | Thresholds clear |
| MON02 | Campaign monitoring | Channel -> spend -> performance -> learnings -> next moves | Campaign monitor | Decisions tied to data |
| MON03 | Product usage monitoring | Events -> cohorts -> anomalies -> hypotheses | Usage monitor | Segment cuts |
| MON04 | System monitoring | SLOs -> alerts -> dashboards -> incidents -> trends | Reliability report | SLO basis |
| MON05 | Risk monitoring | Risk indicators -> triggers -> owner -> response | Risk monitor | Trigger/action linked |
| MON06 | Compliance monitoring | Controls -> evidence -> exceptions -> remediation | Compliance monitor | Exceptions tracked |
| MON07 | Customer feedback monitoring | Reviews/tickets -> themes -> severity -> action | VOC monitor | Volume and examples |
| MON08 | Quality monitoring | Defects -> rates -> causes -> containment -> prevention | Quality monitor | Defect taxonomy |
| MON09 | Financial monitoring | Actuals -> forecast -> variance -> drivers -> actions | Finance monitor | Variance math |
| MON10 | Learning monitoring | Progress -> assessment -> gaps -> remediation | Learning monitor | Next drill/action |

## TRB Troubleshooting / Recovery

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| TRB01 | Bug triage | Symptoms -> reproduce -> logs -> suspected cause -> fix path | Bug triage note | Repro steps |
| TRB02 | Incident triage | Impact -> scope -> timeline -> mitigation -> escalation | Incident triage | Severity clear |
| TRB03 | Data discrepancy | Metric -> source -> logic -> differences -> resolution | Data discrepancy report | Reconciliation path |
| TRB04 | Production defect | Defect -> containment -> root cause -> corrective action | Defect response | Customer impact |
| TRB05 | Campaign underperformance | Goal -> actual -> channel/creative/audience -> fixes | Campaign diagnosis | One variable at a time |
| TRB06 | Process breakdown | Intended flow -> actual -> failure point -> countermeasure | Process diagnosis | Root cause evidence |
| TRB07 | Customer escalation | Facts -> urgency -> owner -> response -> prevention | Escalation plan | Next update time |
| TRB08 | Model/prompt failure | Expected -> actual -> failure mode -> revised prompt/test | Prompt repair plan | Failure isolated |
| TRB09 | Compliance exception | Requirement -> deviation -> impact -> remediation -> evidence | Exception report | Owner and deadline |
| TRB10 | Recovery communication | Incident -> known facts -> action -> ETA -> follow-up | Recovery message | No speculation |

## OPT Optimization / Iteration

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| OPT01 | Conversion optimization | Funnel -> friction -> hypotheses -> tests -> priority | CRO plan | Impact/effort |
| OPT02 | Prompt optimization | Output defects -> variables -> constraints -> test set | Improved prompt | Measured against failures |
| OPT03 | Content optimization | Performance -> audience -> structure -> rewrite -> test | Content optimization | Before/after basis |
| OPT04 | Process optimization | Cycle time -> bottlenecks -> changes -> control | Process improvement plan | Metric target |
| OPT05 | Cost optimization | Spend -> drivers -> options -> risk -> plan | Cost optimization memo | Service risk |
| OPT06 | Performance optimization | Baseline -> bottleneck -> change -> benchmark | Performance plan | Benchmark defined |
| OPT07 | Model/analytics optimization | Baseline -> errors -> features/logic -> validation | Model improvement plan | Holdout/checks |
| OPT08 | Support optimization | Tickets -> drivers -> macros/KB/process -> measurement | Support improvement plan | SLA/CSAT impact |
| OPT09 | Design iteration | User feedback -> issues -> variants -> decision | Design iteration brief | User evidence |
| OPT10 | Learning iteration | Assessment -> gaps -> new drills -> feedback loop | Learning iteration plan | Progress measurable |

## RET Retirement / Archive / Handoff

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| RET01 | Project closeout | Goals -> deliverables -> open issues -> owners -> archive | Closeout report | Open items assigned |
| RET02 | Knowledge handoff | Context -> decisions -> artifacts -> runbook -> contacts | Handoff pack | Future user can resume |
| RET03 | Archive package | Files -> naming -> metadata -> retention -> access | Archive index | Retrieval possible |
| RET04 | Sunset plan | Asset/service -> users -> dependencies -> migration -> comms | Sunset plan | User impact handled |
| RET05 | Postmortem/retro | Timeline -> what worked -> issues -> actions -> owners | Retrospective | Actions measurable |
| RET06 | Compliance record retention | Records -> retention rule -> owner -> disposal date | Retention schedule | Rule basis |
| RET07 | Lessons learned | Project -> decisions -> results -> reusable rules | Lessons learned note | Reusable insight |
| RET08 | Asset reuse review | Outputs -> rights -> quality -> reuse conditions | Reuse catalog | Rights/status |
| RET09 | Decommission checklist | System/process -> backups -> access -> monitoring removal | Decommission checklist | Safe rollback/backup |
| RET10 | Final executive summary | Goal -> outcome -> metrics -> risks -> next recommendation | Final summary | Honest outcome |
