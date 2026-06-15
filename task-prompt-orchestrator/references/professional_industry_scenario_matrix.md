# Professional Industry Scenario Matrix

Use this after choosing a primary P-code and subworkflow when the user request is industry-specific. This file maps common professional verticals to concrete deliverables, so the agent can turn a broad workflow into a domain-ready prompt packet.

Selection rule:

1. Choose the P-code and subworkflow from the professional workflow files first.
2. If the user names an industry, business function, regulated domain, or production context, select a vertical code here.
3. Combine the P-code procedure with the vertical row's domain inputs, artifact, and checks.
4. If a specialized skill/tool exists for the selected vertical, use that tool for execution and keep this row as the checklist.

## EC E-commerce / Retail

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| EC01 | Marketplace listing optimization | SKU facts -> platform rules -> title/bullets/media -> compliance check | Optimized listing pack | Claims match product evidence |
| EC02 | Detail page copy and modules | Buyer intent -> selling points -> module order -> CTA | PDP copy brief | Scannable, benefit-led |
| EC03 | Product image brief | Product specs -> required angles -> props/background -> image prompts | Image production brief | Platform-safe and accurate |
| EC04 | Review mining | Reviews -> pain/benefit clusters -> quote evidence -> fixes | Review insight report | Sample size and source stated |
| EC05 | Competitor shelf audit | Competitors -> price/media/copy/promo -> gap map | Shelf audit | Comparable SKUs only |
| EC06 | Promotion calendar | Seasonality -> inventory -> margin -> channel plan | Promo calendar | Margin and stock constraints |
| EC07 | Bundle strategy | Basket data -> use cases -> bundle options -> pricing | Bundle plan | Cannibalization noted |
| EC08 | Return reason diagnosis | Returns -> reason clusters -> root cause -> fixes | Returns diagnosis | Operational causes separated |
| EC09 | Marketplace ad brief | SKU goal -> keywords -> creative -> budget guardrails | Ad campaign brief | Search intent aligned |
| EC10 | Customer Q&A expansion | Common questions -> answer policy -> evidence -> page updates | Q&A bank | No unsupported promises |

## LEG Legal / Contracts

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| LEG01 | Contract issue spotting | Agreement -> clause map -> risks -> negotiation asks | Issue list | Clause references included |
| LEG02 | Clause comparison | Versions -> changed terms -> business impact -> recommendation | Redline summary | Material changes separated |
| LEG03 | NDA review | Confidentiality scope -> exclusions -> term -> remedies | NDA review table | Mutuality and duration checked |
| LEG04 | Vendor terms review | Terms -> obligations -> data/payment/SLA risks -> asks | Vendor terms memo | Operational owners named |
| LEG05 | Privacy policy summary | Policy -> data categories -> rights -> duties -> gaps | Privacy summary | Not legal advice; uncertainty flagged |
| LEG06 | Regulatory obligation map | Jurisdiction -> rules -> obligations -> evidence/control | Obligation register | Source date/version recorded |
| LEG07 | Litigation chronology | Documents -> events -> parties -> disputed facts | Chronology | Dates and source docs traceable |
| LEG08 | IP/license scan | Assets -> ownership -> licenses -> restrictions -> risks | IP risk scan | License terms cited |
| LEG09 | Legal intake pack | Matter type -> facts -> documents -> questions -> next steps | Intake checklist | Counsel-ready facts |
| LEG10 | Plain-language legal brief | Legal text -> stakeholder impact -> options -> caveats | Plain-language brief | No legal conclusion overstated |

## FIN Finance / Accounting / Investment

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| FIN01 | Budget variance analysis | Actuals -> budget -> drivers -> actions | Variance memo | Driver math reconciles |
| FIN02 | Cash runway forecast | Cash -> burn -> inflows -> scenarios -> runway | Runway forecast | Assumptions visible |
| FIN03 | Unit economics | Revenue/cost events -> cohort/segment -> contribution margin | Unit economics model | Metric definitions explicit |
| FIN04 | Pricing sensitivity | Segments -> willingness/value -> scenarios -> margin | Pricing sensitivity brief | Margin impact shown |
| FIN05 | Board KPI update | KPIs -> variance -> risks -> asks | Board finance note | Trend and cause separated |
| FIN06 | Fundraising metrics pack | Growth -> retention -> margin -> use of funds | Fundraising metrics brief | No vanity-only metrics |
| FIN07 | Investment memo | Company -> market -> financials -> risks -> thesis | Investment memo | Upside/downside balanced |
| FIN08 | Procurement savings | Spend -> suppliers -> levers -> risk -> plan | Savings plan | Service risk included |
| FIN09 | Invoice/payment reconciliation | Records -> mismatches -> causes -> resolution | Reconciliation report | Exceptions traceable |
| FIN10 | Financial policy drafting | Policy goal -> controls -> approval -> audit trail | Finance SOP | Roles and thresholds clear |

## DAT Data / BI / Analytics

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| DAT01 | KPI definition | Business question -> metric formula -> dimensions -> caveats | Metric spec | Numerator/denominator clear |
| DAT02 | Funnel diagnosis | Events -> stages -> dropoffs -> segment cuts -> actions | Funnel report | Stage logic validated |
| DAT03 | Cohort retention | Cohort grain -> retention table -> drivers -> interventions | Cohort analysis | Cohort definition stable |
| DAT04 | Experiment readout | Hypothesis -> design -> results -> guardrails -> decision | A/B readout | Statistical caveats stated |
| DAT05 | Dashboard requirements | Audience -> decisions -> KPIs -> filters -> layout | Dashboard spec | Every chart has user decision |
| DAT06 | SQL logic review | Question -> SQL -> joins/filters -> edge cases | SQL review | Duplicates and nulls checked |
| DAT07 | Data quality audit | Tables -> completeness/validity -> anomalies -> fixes | DQ audit | Severity and owner assigned |
| DAT08 | Attribution analysis | Channels -> touch model -> assumptions -> results | Attribution memo | Model limitations clear |
| DAT09 | Forecast model brief | Target -> features -> horizon -> evaluation -> risks | Forecast brief | Baseline and error metric |
| DAT10 | Semantic layer map | Terms -> metrics -> dimensions -> joins -> governance | Semantic layer draft | Business definitions unambiguous |

## ENG Software / Product Engineering

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| ENG01 | Architecture decision | Requirements -> options -> tradeoffs -> decision | ADR | Constraints and consequences clear |
| ENG02 | API design | Use cases -> resources -> auth/errors -> examples | API spec | Edge cases and status codes |
| ENG03 | Migration plan | Current -> target -> phases -> rollback -> validation | Migration plan | Backward compatibility covered |
| ENG04 | Performance triage | Baseline -> bottleneck -> hypothesis -> benchmark | Perf plan | Before/after metric defined |
| ENG05 | Bug reproduction | Symptoms -> environment -> steps -> logs -> expected | Repro ticket | Deterministic enough to test |
| ENG06 | Test strategy | Risk areas -> unit/integration/e2e -> data -> CI | Test plan | Critical journeys covered |
| ENG07 | Refactor plan | Smells -> target design -> small steps -> tests | Refactor plan | Behavior preservation clear |
| ENG08 | Release checklist | Changes -> risks -> gates -> rollout -> rollback | Release checklist | Owners and gates named |
| ENG09 | Developer docs | Feature -> setup -> usage -> examples -> troubleshooting | Dev docs | Runnable commands included |
| ENG10 | Code review | Diff -> behavior risks -> tests -> findings | Review findings | File/line evidence |

## SEC Security / Privacy / Trust

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| SEC01 | Threat model | System -> assets -> actors -> trust boundaries -> mitigations | Threat model | Controls mapped to threats |
| SEC02 | API security review | Endpoints -> auth -> validation -> rate/data exposure | API security report | Evidence per endpoint |
| SEC03 | Vulnerability triage | Findings -> exploitability -> impact -> fix priority | Triage report | False positives labeled |
| SEC04 | Privacy data-flow review | Data categories -> purposes -> sharing -> retention | Privacy review | Minimization checked |
| SEC05 | Incident response plan | Scenario -> roles -> detection -> containment -> recovery | IR runbook | Timelines and owners |
| SEC06 | Access review | Users/roles -> privileges -> exceptions -> remediation | Access review | Least privilege assessed |
| SEC07 | Secure design checklist | Feature -> abuse cases -> controls -> monitoring | Secure design checklist | Abuse paths included |
| SEC08 | Vendor security review | Vendor -> data/access -> controls -> gaps -> requests | Vendor security memo | Evidence requested |
| SEC09 | Security awareness scenario | Risk -> role -> scenario -> correct action -> quiz | Training scenario | Behavior tested |
| SEC10 | Compliance control evidence | Control -> evidence -> owner -> gap -> remediation | Evidence pack | Audit trail complete |

## OPS Operations / Process / SOP

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| OPS01 | SOP creation | Process -> roles -> steps -> exceptions -> controls | SOP | Owner and trigger clear |
| OPS02 | Process improvement | Current flow -> bottlenecks -> root causes -> future flow | Improvement plan | Measurable improvement |
| OPS03 | RACI design | Workstream -> decisions -> roles -> handoffs | RACI matrix | Accountability singular |
| OPS04 | Runbook creation | Service/process -> normal ops -> alerts -> escalation | Runbook | Usable under pressure |
| OPS05 | Incident postmortem | Timeline -> impact -> causes -> actions -> owners | Postmortem | Blameless, action-oriented |
| OPS06 | Capacity planning | Demand -> capacity -> constraints -> thresholds -> plan | Capacity plan | Assumptions stated |
| OPS07 | Vendor operations | Vendor scope -> SLA -> reporting -> escalation | Vendor ops plan | SLA measurable |
| OPS08 | Quality control checklist | Output standard -> checks -> sampling -> defects | QC checklist | Defect categories clear |
| OPS09 | Change management | Change -> stakeholders -> comms -> training -> adoption | Change plan | Resistance addressed |
| OPS10 | Operating cadence | Goals -> meetings -> artifacts -> decisions -> metrics | Cadence design | Each meeting has purpose |

## EDU Education / Training / Coaching

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| EDU01 | Lesson plan | Learner -> objective -> activity -> assessment | Lesson plan | Objective measurable |
| EDU02 | Study plan | Exam/goal -> time -> topics -> drills -> review | Study plan | Spaced review included |
| EDU03 | Quiz generation | Objectives -> item types -> difficulty -> answers | Quiz set | Answers and rationales |
| EDU04 | Rubric creation | Task -> criteria -> levels -> examples | Rubric | Levels observable |
| EDU05 | Feedback on work | Submission -> criteria -> strengths -> fixes -> next drill | Feedback note | Specific and actionable |
| EDU06 | Curriculum map | Outcomes -> modules -> sequence -> assessments | Curriculum map | Prerequisites respected |
| EDU07 | Coaching session | Goal -> current behavior -> blockers -> practice plan | Coaching plan | One next action clear |
| EDU08 | Skill drill design | Skill -> micro-drills -> feedback loop -> progression | Drill ladder | Difficulty ramps |
| EDU09 | Misconception diagnosis | Learner output -> misconception -> cause -> remediation | Diagnostic memo | Evidence from work |
| EDU10 | Training evaluation | Training -> learner data -> transfer -> improvements | Training eval | Measures beyond satisfaction |

## HLT Health / Wellness / Care

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| HLT01 | Health information summary | Question -> authoritative sources -> caveats -> next steps | Health info brief | Not diagnosis; sources current |
| HLT02 | Symptom prep for clinician | Symptoms -> timeline -> triggers -> questions -> records | Visit prep note | Encourages professional care |
| HLT03 | Medication question prep | Medication -> purpose -> concerns -> interactions questions | Medication discussion brief | No dosing invention |
| HLT04 | Wellness habit plan | Goal -> baseline -> constraints -> habit loop -> tracking | Habit plan | Safe, gradual steps |
| HLT05 | Nutrition planning brief | Preference -> constraints -> pattern -> shopping ideas | Nutrition brief | Avoids medical claims |
| HLT06 | Fitness plan brief | Goal -> baseline -> limitations -> progression -> recovery | Fitness brief | Injury caution included |
| HLT07 | Mental health support guide | Situation -> support options -> grounding -> escalation | Support guide | Crisis boundary stated |
| HLT08 | Caregiver checklist | Patient context -> daily tasks -> warning signs -> records | Care checklist | Escalation signs clear |
| HLT09 | Medical literature lay summary | Paper -> population -> findings -> limitations -> relevance | Lay summary | No overgeneralization |
| HLT10 | Appointment question list | Concern -> evidence -> priorities -> questions | Clinician question list | Prioritized and concise |

## ARC Architecture / Interior / Space

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| ARC01 | Interior concept brief | Space -> users -> style -> constraints -> references | Interior concept brief | Function before decoration |
| ARC02 | Floor plan critique | Plan -> circulation -> zoning -> issues -> alternatives | Plan critique | Scale and flow considered |
| ARC03 | Retail store layout | Customer journey -> zones -> display -> checkout -> ops | Store layout brief | Sales and operations balanced |
| ARC04 | Office planning | Teams -> work modes -> adjacencies -> meeting support | Office plan brief | Capacity and acoustics noted |
| ARC05 | Exhibition/booth concept | Brand -> visitor path -> displays -> lighting -> build | Booth concept brief | Build constraints named |
| ARC06 | Material palette | Use case -> durability -> finish -> color -> maintenance | Material board brief | Maintenance realistic |
| ARC07 | Lighting plan brief | Activities -> mood -> fixtures -> layers -> controls | Lighting brief | Task and ambient split |
| ARC08 | Renovation comparison | Existing -> pain -> proposed changes -> cost/risk | Renovation memo | Structural unknowns flagged |
| ARC09 | Accessibility review | Space -> paths -> reach -> signage -> barriers | Accessibility audit | User mobility considered |
| ARC10 | Architectural visualization prompt | Site -> massing -> materials -> light -> view | Visualization prompt | Realistic context and scale |

## HRP HR / People / Hiring

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| HRP01 | Job description | Role -> outcomes -> skills -> interview signals | JD | Must-have vs nice-to-have |
| HRP02 | Interview scorecard | Role -> competencies -> questions -> evidence scale | Scorecard | Criteria job-related |
| HRP03 | Candidate evaluation | Evidence -> scorecard -> risks -> decision | Evaluation memo | Evidence not vibes |
| HRP04 | Onboarding plan | Role -> 30/60/90 -> stakeholders -> checkpoints | Onboarding plan | Milestones measurable |
| HRP05 | Performance feedback | Situation -> impact -> expectation -> support -> follow-up | Feedback script | Specific, fair, documented |
| HRP06 | Career ladder | Role family -> levels -> behaviors -> examples | Career ladder | Observable expectations |
| HRP07 | Training needs analysis | Team goals -> skill gaps -> interventions -> metrics | TNA report | Gaps tied to work |
| HRP08 | Engagement survey analysis | Survey -> themes -> segments -> actions -> owners | Engagement memo | Confidentiality respected |
| HRP09 | Policy communication | Policy -> audience impact -> FAQ -> rollout | Policy comms pack | Clear, non-alarming |
| HRP10 | Workforce planning | Demand -> capacity -> skills -> hiring/learning plan | Workforce plan | Scenarios included |

## CXS Customer Support / Service / CX

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| CXS01 | Ticket triage taxonomy | Ticket history -> categories -> rules -> routing | Taxonomy | Categories mutually exclusive |
| CXS02 | Help center article | Issue -> user steps -> screenshots/examples -> escalation | Help article | Solves without support where possible |
| CXS03 | Macro/script writing | Scenario -> policy -> empathy -> resolution -> next step | Support macro | Accurate and human |
| CXS04 | Escalation playbook | Severity -> symptoms -> owner -> SLA -> comms | Escalation playbook | Severity rules explicit |
| CXS05 | Customer complaint response | Complaint -> facts -> empathy -> resolution -> prevention | Response draft | No blame or false promise |
| CXS06 | Churn risk diagnosis | Signals -> customer context -> root cause -> save plan | Save plan | Value and risk separated |
| CXS07 | Voice-of-customer report | Tickets/reviews -> themes -> volume -> product asks | VOC report | Evidence and frequency included |
| CXS08 | SLA performance review | Cases -> SLA misses -> causes -> fixes -> owners | SLA review | Causes actionable |
| CXS09 | Support QA rubric | Standards -> dimensions -> examples -> scoring | QA rubric | Fair and coachable |
| CXS10 | Customer journey map | Persona -> stages -> pain -> moments -> opportunities | Journey map | Frontstage/backstage linked |
