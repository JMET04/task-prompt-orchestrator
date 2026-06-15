# Professional Scenario Expansion Matrix

Use this after `professional_subworkflow_matrix.md` when the first five subworkflows under a P-code are too broad. This expansion adds P01.6-P30.10 for higher-coverage professional routing.

Selection rule:

1. Pick the primary P-code from `professional_workflow_library.md`.
2. Check `professional_subworkflow_matrix.md` for Pxx.1-Pxx.5.
3. If the request needs a more specific product, read this file and choose Pxx.6-Pxx.10.
4. Convert the selected row into prompt packets with explicit inputs, procedure, output, and checks.

## P01 Source-Backed Research - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P01.6 | Expert interview synthesis | Interview notes -> themes -> quotes -> evidence map | Interview insight report | Quotes traceable to notes |
| P01.7 | Dataset/source inventory | Source discovery -> metadata -> license/access -> sample | Source inventory | Access and licensing stated |
| P01.8 | Fact-check article | Claim extraction -> source search -> verdict -> correction | Fact-check brief | Verdict per claim |
| P01.9 | Policy/standard lookup | Authority hierarchy -> current version -> obligations -> summary | Policy/standard brief | Version/date cited |
| P01.10 | Research-to-action brief | Findings -> implications -> recommendations -> next tests | Action brief | Recommendations tied to evidence |

## P02 Literature Review / Academic Paper - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P02.6 | Systematic review scoping | Question -> inclusion/exclusion -> search strings -> screening plan | Review protocol | Criteria explicit |
| P02.7 | Method comparison | Methods -> assumptions -> strengths/limits -> fit matrix | Method comparison | Fit to question |
| P02.8 | Dataset benchmark survey | Datasets -> tasks -> metrics -> limitations | Dataset benchmark map | Licenses/limits noted |
| P02.9 | Peer review response | Reviewer comments -> response strategy -> edits -> cover letter | Response-to-reviewers draft | Each comment addressed |
| P02.10 | Abstract/title optimization | Paper -> claims -> title variants -> abstract polish | Title/abstract set | Accurate; no overclaim |

## P03 Competitive / Market Analysis - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P03.6 | Pricing benchmark | Competitor plans -> value metric -> packaging -> gaps | Pricing benchmark | Dates/source links |
| P03.7 | Customer review mining | Reviews -> pain themes -> quotes -> opportunity map | Review mining report | Sample size stated |
| P03.8 | Feature gap analysis | Jobs -> features -> gaps -> parity/differentiation | Feature gap matrix | Buyer relevance |
| P03.9 | Category narrative | Market forces -> old way/new way -> category thesis | Category narrative | Plausible evidence |
| P03.10 | TAM/SAM/SOM rough sizing | Segment -> assumptions -> sources -> ranges | Market sizing memo | Assumptions transparent |

## P04 Product Discovery / PRD - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P04.6 | North-star metric design | Product goal -> user value -> metric candidates -> instrumentation | Metric brief | Metric not vanity |
| P04.7 | Experiment design | Hypothesis -> variants -> success metric -> guardrails | Product experiment spec | Measurable hypothesis |
| P04.8 | Onboarding flow spec | Activation event -> steps -> friction -> UX requirements | Onboarding spec | Activation defined |
| P04.9 | Churn/retention diagnosis | Cohorts -> behavior -> exit reasons -> interventions | Retention diagnosis | Segments clear |
| P04.10 | Backlog grooming | Raw ideas -> dedupe -> scoring -> sprint-ready items | Groomed backlog | Acceptance criteria |

## P05 Requirements Engineering - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P05.6 | Stakeholder interview guide | Stakeholder map -> question themes -> scripts | Interview guide | Covers goals/risks |
| P05.7 | Use-case specification | Actors -> preconditions -> main/alternate flows | Use-case spec | Edge flows included |
| P05.8 | Business rules catalog | Policy/process -> rules -> exceptions -> owners | Rules catalog | Conflicts flagged |
| P05.9 | Data requirements | Entities -> fields -> quality -> retention/privacy | Data requirement spec | Data owners/constraints |
| P05.10 | Integration requirements | Systems -> interfaces -> contracts -> failure modes | Integration spec | Error cases defined |

## P06 UX / Content Design - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P06.6 | Voice and tone guide | Brand/user context -> principles -> examples -> do/don't | Tone guide | Examples cover edge cases |
| P06.7 | Accessibility content audit | Screens/content -> plain language -> WCAG copy checks | Accessibility copy audit | Issues actionable |
| P06.8 | Taxonomy/navigation labels | Content set -> mental model -> label options -> testing plan | Label taxonomy | Labels user-centered |
| P06.9 | Microcopy system | Components -> states -> copy patterns -> governance | Microcopy library | Consistent states |
| P06.10 | Localization UX review | Source copy -> locale constraints -> cultural fit -> glossary | Localization brief | Avoids literal-only translation |

## P07 Image2 / Visual Production - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P07.6 | Reference sheet creation | Subject -> views -> traits -> style notes | Character/product reference sheet | Consistency anchors |
| P07.7 | Batch variant generation | Brief -> variables -> prompt set -> naming -> QA | Variant prompt pack | Variables isolated |
| P07.8 | Style transfer | Source style -> target content -> invariants -> prompt | Style transfer prompt | Subject preserved |
| P07.9 | Image repair prompt | Output defects -> root cause -> targeted correction | Repair prompt | One failure per iteration |
| P07.10 | Asset delivery pack | Final images -> formats -> naming -> usage notes | Asset pack spec | Paths and formats clear |

## P08 Packaging / CAD / Industrial Design - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P08.6 | Label/sticker layout | Container -> label area -> hierarchy -> print constraints | Label prompt/spec | Legibility zones |
| P08.7 | Retail display / POSM | Product -> shelf context -> structure -> visual hierarchy | POSM concept prompt | Shopper view clear |
| P08.8 | Patent-style drawing | Object -> views -> reference numerals -> clean line art | Patent drawing prompt | No decorative shading |
| P08.9 | Furniture/fixture drawing | Dimensions -> materials -> joints -> exploded view | Furniture tech prompt | Joinery plausible |
| P08.10 | Manufacturing callout board | Product -> materials -> processes -> detail callouts | Production board prompt | Callouts tied to parts |

## P09 Marketing / Growth / Brand - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P09.6 | SEO content brief | Keyword -> intent -> SERP pattern -> outline -> entities | SEO brief | Search intent matched |
| P09.7 | Webinar campaign | Audience -> topic -> registration -> nurture -> follow-up | Webinar campaign plan | Funnel complete |
| P09.8 | Influencer/UGC brief | Audience -> creator angle -> shot list -> compliance | UGC brief | Usage rights noted |
| P09.9 | Brand narrative | Origin -> audience belief -> proof -> story arc | Brand story | Avoids generic slogans |
| P09.10 | Conversion audit | Page/funnel -> friction -> evidence -> prioritized fixes | CRO audit | Fixes prioritized |

## P10 Sales / GTM / Customer Success - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P10.6 | Account plan | Target account -> stakeholders -> initiatives -> entry points | Account plan | Source-backed context |
| P10.7 | Call prep | Meeting goal -> personas -> hypotheses -> questions | Call prep brief | Next ask clear |
| P10.8 | MEDDICC/BANT qualification | Opportunity -> criteria -> gaps -> next steps | Qualification sheet | Gaps explicit |
| P10.9 | Mutual action plan | Buyer goal -> milestones -> owners -> dates | MAP | Mutual commitments |
| P10.10 | Renewal/expansion plan | Usage -> value proof -> risks -> expansion plays | Renewal plan | Risk signals included |

## P11 Social / Community / Content Ops - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P11.6 | Newsletter issue | Audience -> theme -> sections -> CTA | Newsletter draft | Scannable structure |
| P11.7 | Repurpose long-form content | Source -> atomize -> channel variants | Repurposing pack | Each variant native |
| P11.8 | Community engagement plan | Audience -> rituals -> prompts -> moderation | Community plan | Engagement loops |
| P11.9 | Content performance review | Posts -> metrics -> patterns -> recommendations | Content retro | Insights tied to metrics |
| P11.10 | Thought leadership POV | Expertise -> contrarian insight -> proof -> examples | POV memo/posts | Specific stance |

## P12 Writing / Editing / Documentation - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P12.6 | Grant/proposal writing | Funder/client -> requirements -> narrative -> budget/risk | Proposal draft | Requirements covered |
| P12.7 | Technical documentation | Product/API -> audience -> steps -> examples -> errors | Docs draft | Runnable examples |
| P12.8 | Case study | Customer -> problem -> solution -> results -> proof | Case study | Outcome evidence |
| P12.9 | Speech/script | Audience -> message -> structure -> cadence | Speech/script | Spoken rhythm |
| P12.10 | Style guide enforcement | Existing copy -> style rules -> corrections -> rationale | Style edit report | Rules cited |

## P13 Legal / Contract / Regulatory Reading - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P13.6 | NDA review | NDA -> confidentiality scope -> exclusions -> term -> issues | NDA issue table | Clause references |
| P13.7 | Terms/privacy summary | Document -> obligations -> user/business impacts | Plain-language summary | Not legal advice |
| P13.8 | Litigation timeline | Pleadings/events -> chronology -> issues -> evidence | Litigation timeline | Dates/source docs |
| P13.9 | IP risk scan | Asset/product -> ownership -> licenses -> infringement risks | IP risk memo | Uncertainties flagged |
| P13.10 | Legal intake questionnaire | Matter type -> facts needed -> documents -> next steps | Intake checklist | Counsel-ready |

## P14 Compliance / Governance / Risk - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P14.6 | Privacy impact assessment | Data flow -> purposes -> risks -> controls | PIA draft | Data categories mapped |
| P14.7 | Vendor risk review | Vendor -> data/access -> controls -> gaps | Vendor risk report | Evidence requested |
| P14.8 | SOP compliance check | SOP -> requirement -> evidence -> deviation | SOP check report | Deviations clear |
| P14.9 | AI governance review | AI use case -> risks -> controls -> monitoring | AI governance checklist | Human oversight |
| P14.10 | Training compliance pack | Rules -> roles -> scenarios -> quiz | Training pack | Assessment included |

## P15 Finance / Accounting / Investment - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P15.6 | Cash flow forecast | Inflows/outflows -> timing -> scenarios -> runway | Cash flow forecast | Assumptions stated |
| P15.7 | Pricing model | Costs -> value metric -> segments -> scenarios | Pricing model brief | Margin implications |
| P15.8 | Board finance update | KPIs -> variance -> drivers -> asks | Finance board memo | Variance explained |
| P15.9 | Procurement savings analysis | Spend -> vendors -> levers -> risk | Savings memo | Risks to service |
| P15.10 | Fundraising narrative | Metrics -> market -> use of funds -> milestones | Fundraising finance narrative | Credible assumptions |

## P16 Data Analysis / BI / Metrics - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P16.6 | Cohort analysis | Cohort definition -> retention/behavior -> drivers | Cohort report | Cohort grain clear |
| P16.7 | Funnel analysis | Stages -> conversion -> dropoffs -> segments | Funnel diagnosis | Stages defined |
| P16.8 | A/B test analysis | Design -> sample -> results -> stats/caveats | Experiment analysis | Guardrails checked |
| P16.9 | SQL query review | Question -> SQL -> logic -> edge cases -> optimization | SQL review | Logic validated |
| P16.10 | Semantic metric layer | Business terms -> metric definitions -> dimensions | Metric dictionary | Definitions unambiguous |

## P17 Coding / Engineering Implementation - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P17.6 | Architecture plan | Requirements -> constraints -> components -> tradeoffs | Architecture plan | Decisions justified |
| P17.7 | Migration plan | Current -> target -> steps -> compatibility -> rollback | Migration plan | Rollback path |
| P17.8 | Performance optimization | Baseline -> bottleneck -> fix -> benchmark | Performance patch plan | Benchmark before/after |
| P17.9 | Accessibility implementation | UI -> WCAG gaps -> fixes -> tests | A11y implementation plan | Keyboard/screen reader checks |
| P17.10 | Documentation update | Changed behavior -> docs affected -> examples -> changelog | Docs update | Docs match code |

## P18 Security / Privacy / Audit - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P18.6 | Threat model | System -> assets -> actors -> threats -> mitigations | Threat model | Controls mapped |
| P18.7 | Privacy/security design review | Data flow -> trust boundaries -> risks -> controls | Design review | Data minimization |
| P18.8 | Static analysis triage | Tool findings -> dedupe -> exploitability -> fix plan | Triage report | False positives labeled |
| P18.9 | API security review | Auth -> input validation -> rate limits -> data exposure | API security report | Endpoint evidence |
| P18.10 | Postmortem quality review | Incident/RCA -> gaps -> action quality -> owners | RCA review | Actions measurable |

## P19 QA / Testing / Evaluation - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P19.6 | Mobile test plan | Devices -> OS -> flows -> permissions -> network | Mobile QA matrix | Device coverage |
| P19.7 | E2E test design | Critical journeys -> selectors/data -> flake risks | E2E plan | Stable selectors |
| P19.8 | Regression suite pruning | Tests -> failures/value -> keep/remove/add | Regression strategy | Risk coverage maintained |
| P19.9 | Test data strategy | Scenarios -> data sets -> privacy -> reset | Test data plan | Reproducible data |
| P19.10 | UAT plan | Stakeholders -> scenarios -> criteria -> signoff | UAT pack | Business signoff |

## P20 DevOps / Cloud / Reliability - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P20.6 | Runbook creation | System -> routine ops -> alerts -> steps -> escalation | Ops runbook | Actionable during incident |
| P20.7 | Disaster recovery plan | RTO/RPO -> backups -> restore -> drills | DR plan | Restore tested |
| P20.8 | CI/CD pipeline review | Pipeline -> gates -> secrets -> artifacts -> rollback | CI/CD audit | Secret handling |
| P20.9 | Capacity planning | Demand -> resources -> limits -> scaling triggers | Capacity plan | Thresholds defined |
| P20.10 | Service onboarding | Service -> ownership -> SLOs -> dashboards -> runbooks | Service onboarding pack | Owner and SLO clear |

## P21 Automation / Agents / Workflow Design - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P21.6 | AI assistant SOP | Task -> prompt -> review -> escalation -> storage | Assistant SOP | Review gate |
| P21.7 | RPA candidate review | Process -> rule-based fit -> exceptions -> ROI | RPA assessment | Exceptions quantified |
| P21.8 | Knowledge-base bot | Content -> intents -> retrieval -> fallback -> eval | Bot workflow spec | Eval set included |
| P21.9 | Email/document automation | Inputs -> extraction -> generation -> approval | Doc automation flow | Approval before send |
| P21.10 | Automation governance | Automations -> owners -> logs -> monitoring -> change control | Governance plan | Audit trail |

## P22 Operations / Process / SOP - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P22.6 | Service blueprint | Customer actions -> backstage -> systems -> pain | Service blueprint | Front/backstage linked |
| P22.7 | Queue/workload optimization | Demand -> capacity -> rules -> SLA -> staffing | Workload plan | SLA impact |
| P22.8 | Handoff redesign | Teams -> inputs/outputs -> checklist -> escalation | Handoff SOP | Ownership clear |
| P22.9 | Root cause analysis | Problem -> causes -> evidence -> countermeasures | RCA | Causes evidence-backed |
| P22.10 | Operating cadence design | Goals -> meetings -> metrics -> decisions -> artifacts | Cadence system | Each meeting has purpose |

## P23 Strategy / Decision Memo - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P23.6 | Business model analysis | Value prop -> revenue/cost -> channels -> risks | Business model memo | Assumptions explicit |
| P23.7 | Partnership strategy | Goals -> partner types -> value exchange -> outreach | Partnership plan | Mutual value |
| P23.8 | Market entry strategy | Segment -> barriers -> channels -> wedge -> rollout | Market entry plan | Risks addressed |
| P23.9 | Build/buy/partner decision | Capability -> options -> costs/risks -> recommendation | Decision memo | Criteria weighted |
| P23.10 | Crisis response strategy | Event -> stakeholders -> messages -> actions -> monitoring | Crisis plan | Timeline and owners |

## P24 Presentation / Deck / Storytelling - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P24.6 | Investor update deck | Metrics -> narrative -> wins/risks -> asks | Investor update | Concise and honest |
| P24.7 | Sales enablement deck | Buyer pains -> proof -> talk track -> objections | Enablement deck | Usable by sales |
| P24.8 | Workshop deck | Objectives -> exercises -> timing -> materials | Workshop deck | Facilitation notes |
| P24.9 | Data storytelling deck | Insight -> chart logic -> narrative -> recommendation | Data story deck | Chart supports message |
| P24.10 | One-page executive summary | Problem -> insight -> recommendation -> next step | One-pager | Skimmable in 2 minutes |

## P25 Personal Productivity / Knowledge Work - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P25.6 | Decision log | Decisions -> rationale -> owner -> date -> follow-up | Decision log | Rationale captured |
| P25.7 | Project status report | Goals -> progress -> blockers -> risks -> next | Status report | R/Y/G clear |
| P25.8 | Inbox triage | Messages -> categories -> priority -> response drafts | Inbox triage pack | No commitments invented |
| P25.9 | Personal knowledge capture | Sources -> notes -> tags -> actions | Knowledge note pack | Retrievable tags |
| P25.10 | Document cleanup | Doc -> structure -> duplicates -> action items -> final | Cleaned document | Structure improved |

## P26 Education / Training / Coaching - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P26.6 | Competency map | Role/skill -> competencies -> levels -> evidence | Competency matrix | Levels observable |
| P26.7 | Practice drill generator | Skill -> drills -> feedback -> progression | Drill set | Deliberate practice |
| P26.8 | Rubric creation | Task -> criteria -> levels -> examples | Rubric | Levels distinguish quality |
| P26.9 | Learning diagnostic | Learner output -> misconception -> remediation | Diagnostic feedback | Actionable next step |
| P26.10 | Certification prep | Exam objectives -> plan -> questions -> review | Prep plan | Objective coverage |

## P27 HR / Hiring / People Ops - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P27.6 | Hiring pipeline design | Role -> stages -> criteria -> handoffs -> SLA | Hiring process | Fair and efficient |
| P27.7 | Candidate evaluation | Resume/interview -> scorecard -> evidence -> decision | Evaluation memo | Evidence-based |
| P27.8 | Offer negotiation prep | Candidate/company goals -> levers -> scripts -> risks | Negotiation prep | Respectful/legal |
| P27.9 | Employer brand content | Audience -> EVP -> proof -> content plan | Employer brand assets | Authentic proof |
| P27.10 | Onboarding plan | Role -> first 30/60/90 -> mentors -> checkpoints | Onboarding plan | Milestones clear |

## P28 Customer Support / Service / CX - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P28.6 | Ticket taxonomy | Ticket history -> categories -> routing -> SLAs | Taxonomy | Mutually exclusive categories |
| P28.7 | Escalation playbook | Issue types -> severity -> owner -> script | Escalation playbook | Severity rules clear |
| P28.8 | Churn/save playbook | Risk signal -> diagnosis -> offer -> follow-up | Save playbook | Customer value focus |
| P28.9 | Product feedback loop | Tickets -> themes -> product impact -> roadmap asks | Feedback report | Evidence and volume |
| P28.10 | Help center audit | Articles -> gaps -> search intent -> refresh plan | Help center audit | Prioritization |

## P29 Domain-Specific Expert Task - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P29.6 | Literature-to-protocol translation | Evidence -> protocol elements -> gaps -> safety | Protocol draft | Evidence trace |
| P29.7 | Technical standard interpretation | Standard -> requirements -> implementation steps | Standard implementation guide | Clauses mapped |
| P29.8 | Simulation plan | Objective -> model -> inputs -> validation -> outputs | Simulation plan | Validation method |
| P29.9 | Field test plan | Environment -> procedure -> measurements -> risks | Field test plan | Safety/logistics |
| P29.10 | Technical troubleshooting | Symptoms -> hypotheses -> tests -> fixes | Troubleshooting tree | Tests isolate causes |

## P30 Prompt Library / Skill Building - Extended

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P30.6 | Source harvesting plan | Target domains -> sources -> license -> import rules | Harvest plan | Legal/source boundaries |
| P30.7 | Taxonomy refinement | Corpus -> clusters -> labels -> routing rules | Taxonomy update | Categories actionable |
| P30.8 | Prompt normalization | Raw prompts -> variables -> structure -> checks | Normalized prompt set | Reusable variables |
| P30.9 | Skill forward test | Skill -> representative tasks -> outputs -> failures | Forward test report | Failures actionable |
| P30.10 | Workflow coverage audit | Matrix -> user scenarios -> gaps -> expansion plan | Coverage audit | Gaps tracked |
