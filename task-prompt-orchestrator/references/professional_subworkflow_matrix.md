# Professional Subworkflow Matrix

Use this after selecting a primary workflow in `professional_workflow_library.md`. Pick the closest subworkflow, then create prompt packets from its steps, product output, and checks.

Expansion index: if Pxx.1-Pxx.5 are too broad, continue in `professional_scenario_expansion_matrix.md` for Pxx.6-Pxx.10.

Format:

- `Trigger`: user language or task shape that should route here.
- `Best workflow`: the professional process to follow.
- `Product`: the artifact to produce.
- `Checks`: completion criteria.

## P01 Source-Backed Research

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P01.1 | "Find reliable sources", "what is true" | Question scope -> authoritative search -> evidence table -> synthesis | Source-backed answer | Every key claim has source/date |
| P01.2 | "Latest news / current status" | Freshness boundary -> recent sources -> compare dates -> timeline | Current-state brief | Event dates separated from publish dates |
| P01.3 | "Compare claims" | Claim list -> source verification -> contradiction map -> confidence rating | Claim verification matrix | Unsupported claims labeled |
| P01.4 | "Build a research dossier" | Entity scope -> source pack -> facts/issues/risks -> summary | Research dossier | Covers background, evidence, open questions |
| P01.5 | "Summarize many links" | Link inventory -> extract claims -> cluster themes -> cite synthesis | Multi-source synthesis | No uncited material conclusions |

## P02 Literature Review / Academic Paper

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P02.1 | "Related work" | Research question -> paper clusters -> contribution/limits -> synthesis | Related work section | Thematic, not paper-by-paper |
| P02.2 | "Annotated bibliography" | Search -> screen -> annotate method/findings/relevance | Annotated bibliography | Each entry has relevance note |
| P02.3 | "Citation audit" | Claim extraction -> citation matching -> gap list -> replacement search | Citation audit report | Unsupported claims flagged |
| P02.4 | "Research proposal" | Problem -> gap -> method -> feasibility -> risks | Proposal draft | Research question and method align |
| P02.5 | "Paper expansion" | Existing draft -> weak sections -> literature chain -> rewrite | Expanded section | New claims supported by sources |

## P03 Competitive / Market Analysis

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P03.1 | "Competitor analysis" | Market definition -> competitor list -> feature/pricing/channel matrix | Competitor matrix | Claims sourced |
| P03.2 | "Market map" | Segment axes -> players -> substitutes -> whitespace | Market landscape map | Axes meaningful to buyer |
| P03.3 | "Positioning" | Audience -> alternatives -> differentiators -> message hierarchy | Positioning brief | Differentiation is specific |
| P03.4 | "Trend scan" | Trend query -> signals -> drivers -> impact -> watchlist | Trend report | Signals dated and sourced |
| P03.5 | "Opportunity analysis" | Customer pain -> unmet need -> competitor gap -> wedge strategy | Opportunity memo | Opportunity tied to evidence |

## P04 Product Discovery / PRD

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P04.1 | "Write PRD" | Problem -> users -> goals -> requirements -> metrics -> risks | PRD | Scope, non-goals, acceptance criteria present |
| P04.2 | "MVP plan" | Jobs -> assumptions -> thin slice -> release plan -> learning goals | MVP plan | Small enough to ship |
| P04.3 | "Roadmap" | Strategy -> themes -> dependencies -> sequencing -> milestones | Roadmap | Priorities justified |
| P04.4 | "User journey" | Persona -> scenario -> steps -> pains -> opportunities | Journey map | Pain points mapped to product decisions |
| P04.5 | "Feature prioritization" | Backlog -> scoring criteria -> ranked list -> tradeoffs | Prioritization table | Criteria explicit |

## P05 Requirements Engineering

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P05.1 | "Clarify requirements" | Stakeholders -> elicitation questions -> assumptions -> requirements | Requirements brief | Ambiguities surfaced |
| P05.2 | "User stories" | Capability -> actor/goal/value -> acceptance criteria -> edge cases | User story set | Testable stories |
| P05.3 | "Acceptance criteria" | Requirement -> scenarios -> Given/When/Then -> negative cases | Acceptance criteria | Includes boundary cases |
| P05.4 | "Traceability matrix" | Source needs -> requirements -> tests -> owners | Traceability matrix | Every item linked |
| P05.5 | "Non-functional requirements" | Quality attributes -> constraints -> measurement -> thresholds | NFR spec | Metrics measurable |

## P06 UX / Content Design

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P06.1 | "UX copy" | User intent -> screen state -> copy variants -> tone/accessibility review | UX copy set | Clear action, plain language |
| P06.2 | "Information architecture" | Content inventory -> user tasks -> grouping -> navigation model | IA map | Supports core user tasks |
| P06.3 | "Conversation flow" | User goal -> intents -> turns -> fallback/escalation | Conversation script | Handles failure states |
| P06.4 | "Error states" | Failure modes -> user impact -> recovery action -> copy | Error/help states | Actionable, non-blaming |
| P06.5 | "Content system" | Content types -> fields -> governance -> workflow | Content model | Ownership and lifecycle defined |

## P07 Image2 / Visual Production

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P07.1 | "Edit this image" | Inspect target -> preserve/change list -> prompt -> edit -> visual QA | Edited image | Invariants preserved |
| P07.2 | "Generate product visual" | Product facts -> scene/style -> prompt -> variants -> pick | Product visual | Product identity plausible |
| P07.3 | "Character refinement" | Identity references -> key traits -> style constraints -> edit | Character image | Required traits visible |
| P07.4 | "Poster / KV" | Campaign goal -> layout -> visual hierarchy -> prompt -> QA | Poster/KV | Space for copy, strong focal point |
| P07.5 | "Visual audit" | Image -> criteria -> issue list -> fix prompts | Visual audit + prompts | Issues actionable |

## P08 Packaging / CAD / Industrial Design

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P08.1 | "Packaging dieline" | Package type -> dimensions -> line types -> prompt -> QA | Dieline prompt/reference | Cut/fold/bleed/safe lines specified |
| P08.2 | "CAD technical drawing" | Object -> views -> annotations -> line style -> prompt | CAD-style drawing prompt | Views and dimensions specified |
| P08.3 | "Exploded view" | Assembly -> components -> spacing -> labels -> prompt | Exploded technical visual | Component logic clear |
| P08.4 | "CMF board" | Product -> color/material/finish options -> presentation | CMF concept board | Materials and finishes differentiated |
| P08.5 | "Industrial concept" | User scenario -> ergonomics -> manufacturable form -> render spec | Product concept prompt | Function and form plausible |

## P09 Marketing Campaign

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P09.1 | "Launch campaign" | ICP -> offer -> promise/proof -> channels -> calendar | Launch plan | CTA and proof clear |
| P09.2 | "Ad creative" | Audience -> hook -> visual/copy -> variants -> test plan | Ad set | Channel-native variants |
| P09.3 | "Landing page" | Audience pain -> value prop -> sections -> proof -> CTA | Landing page copy/wire | Above-fold message clear |
| P09.4 | "Email sequence" | Lead magnet/offer -> sequence logic -> emails -> segmentation | Email sequence | Each email has job and CTA |
| P09.5 | "Messaging strategy" | Audience -> alternatives -> differentiation -> message map | Messaging framework | Avoids vague claims |

## P10 Sales / GTM Pipeline

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P10.1 | "ICP" | Market -> firmographics -> pains -> triggers -> disqualifiers | ICP profile | Includes exclusion criteria |
| P10.2 | "Cold outreach" | Target research -> relevance -> message -> CTA -> follow-up | Outreach sequence | Personalized and concise |
| P10.3 | "Discovery script" | Buyer role -> hypotheses -> questions -> qualification | Discovery guide | Questions uncover pain/budget/timing |
| P10.4 | "Proposal" | Need -> solution -> proof -> scope -> next steps | Sales proposal | Maps pain to offer |
| P10.5 | "Objection handling" | Objections -> root cause -> response -> proof -> next question | Objection playbook | Non-defensive, evidence-led |

## P11 Social Content System

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P11.1 | "LinkedIn post" | Audience -> thesis -> hook -> story/proof -> CTA | LinkedIn post | One clear idea |
| P11.2 | "Carousel" | Topic -> slide arc -> headlines -> visual notes -> CTA | Carousel outline/copy | Save-worthy structure |
| P11.3 | "Twitter/X thread" | Hook -> claims -> proof/examples -> takeaway | Thread | Each post advances argument |
| P11.4 | "Short video script" | Hook -> scenes -> narration -> captions -> CTA | Short-video script | Visual beats included |
| P11.5 | "Content calendar" | Pillars -> cadence -> formats -> repurposing -> metrics | Calendar | Balanced pillars and channels |

## P12 Writing / Editing / Translation

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P12.1 | "Write article" | Brief -> outline -> draft -> critique -> final | Article | Structure and evidence fit audience |
| P12.2 | "Rewrite/polish" | Goal -> diagnose issues -> targeted rewrite -> explain changes | Polished copy | Preserves meaning |
| P12.3 | "Summarize" | Source -> audience -> extract -> compress -> key takeaways | Summary | No important distortion |
| P12.4 | "Translate" | Source -> audience/locale -> translation -> terminology check | Translation | Tone and terminology consistent |
| P12.5 | "Executive memo" | Decision -> context -> options -> recommendation -> risks | Memo | Decision-ready |

## P13 Legal Document Workflow

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P13.1 | "Contract summary" | Document -> parties/terms -> obligations -> deadlines | Contract summary | Exact clauses referenced |
| P13.2 | "Clause risk review" | Clause -> standard concern areas -> risk rank -> questions | Clause risk table | Not legal advice |
| P13.3 | "Legal memo" | Issue -> facts -> rules/sources -> analysis -> caveats | Legal-style memo | Jurisdiction limits stated |
| P13.4 | "Due diligence" | Document set -> issue checklist -> evidence -> red flags | Diligence issue list | Material risks prioritized |
| P13.5 | "Redline suggestions" | Business goal -> clause gaps -> proposed edits -> rationale | Redline suggestion list | Counsel review required |

## P14 Regulatory / Compliance

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P14.1 | "Gap analysis" | Regulation -> requirements -> current evidence -> gaps | Compliance gap report | Requirement-to-evidence mapping |
| P14.2 | "Audit checklist" | Scope -> controls -> evidence -> owner -> status | Audit checklist | Owners and evidence named |
| P14.3 | "Policy mapping" | Policy -> obligations -> controls -> exceptions | Policy map | Ambiguities flagged |
| P14.4 | "Risk assessment" | Asset/process -> threats -> likelihood/impact -> mitigations | Risk register | Scoring criteria explicit |
| P14.5 | "Regulatory submission prep" | Product -> jurisdiction -> required docs -> readiness | Submission readiness pack | Missing evidence listed |

## P15 Finance / Budgeting / Investment Memo

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P15.1 | "Budget plan" | Goals -> cost categories -> assumptions -> scenarios | Budget plan | Assumptions explicit |
| P15.2 | "Expense analysis" | Expense data -> categories -> anomalies -> policy check | Expense report | Exceptions evidenced |
| P15.3 | "Investment memo" | Thesis -> market -> financials -> risks -> recommendation | Investment memo | Not financial advice |
| P15.4 | "Valuation" | Inputs -> method -> assumptions -> sensitivity | Valuation analysis | Formulas and caveats shown |
| P15.5 | "Unit economics" | Revenue/cost drivers -> cohort/unit model -> scenarios | Unit economics model brief | Drivers traceable |

## P16 Data Analysis / Dashboard

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P16.1 | "Analyze CSV" | Inspect -> clean -> metrics -> findings -> caveats | Data analysis report | Schema and filters stated |
| P16.2 | "Dashboard" | Users -> KPIs -> data model -> visuals -> interactions | Dashboard spec/artifact | KPIs defined |
| P16.3 | "Metric movement" | Metric -> baseline -> segments -> drivers -> explanation | Metric diagnostic | Driver evidence shown |
| P16.4 | "Forecast" | History -> assumptions -> model -> scenarios -> risks | Forecast | Uncertainty stated |
| P16.5 | "Data quality" | Schema -> missing/duplicates/outliers -> impact -> fixes | Data quality report | Issues quantified |

## P17 Software Feature Build

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P17.1 | "Build feature" | Inspect -> spec -> plan -> implement -> test | Feature implementation | Acceptance checks pass |
| P17.2 | "Fix bug" | Reproduce -> root cause -> patch -> regression test | Bug fix | Reproduction and fix verified |
| P17.3 | "Refactor" | Current behavior -> constraints -> scoped refactor -> tests | Refactor diff | Behavior preserved |
| P17.4 | "API integration" | API docs -> auth/data model -> implementation -> error handling | Integration | Handles failure cases |
| P17.5 | "Prototype app" | User flow -> stack -> scaffold -> core loop -> run | Prototype | Runnable first screen |

## P18 Code Review / Security Audit

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P18.1 | "PR review" | Diff -> behavior risk -> findings -> test gaps | Review findings | File/line evidence |
| P18.2 | "Security review" | Threat model -> code paths -> vulnerabilities -> mitigations | Security audit | OWASP/CWE where relevant |
| P18.3 | "Performance review" | Hot paths -> complexity -> IO -> bottlenecks -> fixes | Performance report | Measurable impact |
| P18.4 | "Dependency review" | Dependencies -> versions -> advisories -> upgrade path | Dependency risk report | Sources cited |
| P18.5 | "Architecture review" | Goals -> structure -> tradeoffs -> risks -> recommendations | Architecture review | Risks prioritized |

## P19 QA / Test Planning

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P19.1 | "Test plan" | Requirements -> risks -> strategy -> coverage -> schedule | Test plan | Requirement coverage |
| P19.2 | "Test cases" | User flows -> positive/negative/boundary -> expected results | Test case suite | Clear expected results |
| P19.3 | "Automation plan" | Stable flows -> tool choice -> test data -> CI strategy | Automation plan | ROI and maintenance considered |
| P19.4 | "API testing" | Endpoints -> contracts -> status/error cases -> data | API test matrix | Edge cases included |
| P19.5 | "Accessibility QA" | UI scope -> WCAG checks -> keyboard/screen reader -> issues | Accessibility report | WCAG references |

## P20 DevOps / Release / Incident

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P20.1 | "Release checklist" | Change scope -> dependencies -> tests -> rollback -> comms | Release checklist | Rollback explicit |
| P20.2 | "Incident RCA" | Timeline -> impact -> root cause -> actions -> owners | RCA | Evidence vs hypothesis separated |
| P20.3 | "Deployment plan" | Environment -> steps -> validation -> rollback -> monitoring | Deployment runbook | Safe commands |
| P20.4 | "Observability plan" | System -> SLIs/SLOs -> logs/metrics/traces -> alerts | Observability plan | Alert actionability |
| P20.5 | "Cloud cost review" | Usage -> services -> waste -> savings -> tradeoffs | Cost optimization report | Savings assumptions stated |

## P21 Automation Discovery

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P21.1 | "What can I automate" | Process inventory -> scoring -> shortlist -> first pilot | Automation shortlist | Low-risk pilot selected |
| P21.2 | "SOP automation" | Current SOP -> inputs/outputs -> AI steps -> human review | AI-assisted SOP | Review gates included |
| P21.3 | "No-code workflow" | Trigger -> apps -> data -> actions -> exceptions | No-code workflow spec | Failure handling |
| P21.4 | "Agent workflow" | Goal -> tools -> permissions -> loop -> guardrails | Agent workflow design | Scope bounded |
| P21.5 | "Prompt automation" | Repeated prompt -> variables -> examples -> eval -> template | Reusable prompt template | Variables clear |

## P22 Business Process Optimization

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P22.1 | "Process map" | Inputs -> steps -> handoffs -> outputs -> pain points | Current-state map | Handoffs visible |
| P22.2 | "Bottleneck analysis" | Flow data -> constraints -> root causes -> options | Bottleneck report | Evidence tied to bottleneck |
| P22.3 | "Lean waste reduction" | Process -> waste categories -> redesign -> KPI | Waste reduction plan | Practical changes |
| P22.4 | "KPI design" | Business goal -> process levers -> metrics -> cadence | KPI system | Metrics actionable |
| P22.5 | "Change rollout" | Stakeholders -> change plan -> risks -> comms -> training | Rollout plan | Adoption risks addressed |

## P23 Strategy / Decision Memo

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P23.1 | "Decision memo" | Decision -> criteria -> options -> analysis -> recommendation | Decision memo | Criteria drive recommendation |
| P23.2 | "Scenario planning" | Uncertainties -> scenarios -> implications -> signposts | Scenario plan | Signposts observable |
| P23.3 | "SWOT / strategic analysis" | Objective -> internal/external factors -> implications | Strategy analysis | Not just lists |
| P23.4 | "OKR strategy" | Mission -> objectives -> key results -> initiatives | OKR set | KRs measurable |
| P23.5 | "Risk tradeoff" | Options -> risks -> mitigations -> reversibility | Tradeoff memo | Reversibility noted |

## P24 Presentation / Deck

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P24.1 | "Pitch deck" | Audience -> story -> slides -> proof -> ask | Pitch deck outline | Clear ask |
| P24.2 | "Board update" | Metrics -> narrative -> risks -> decisions needed | Board deck | Executive-level clarity |
| P24.3 | "Training deck" | Learners -> outcomes -> modules -> exercises -> quiz | Training deck | Learning outcomes measurable |
| P24.4 | "Proposal deck" | Client pain -> solution -> plan -> proof -> next step | Proposal deck | Maps solution to pain |
| P24.5 | "Visual redesign brief" | Existing deck -> issues -> layout system -> redesign notes | Redesign brief | One message per slide |

## P25 Meeting / Office Productivity

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P25.1 | "Meeting agenda" | Purpose -> decisions -> participants -> timeboxes | Agenda | Decision-oriented |
| P25.2 | "Meeting notes" | Transcript/notes -> decisions -> action items -> risks | Notes + tracker | Owners/deadlines present |
| P25.3 | "Follow-up email" | Meeting outcome -> audience -> commitments -> next steps | Follow-up email | No invented commitments |
| P25.4 | "Executive briefing" | Topic -> key facts -> implications -> asks | Briefing note | Skimmable |
| P25.5 | "Calendar optimization" | Goals -> meetings -> energy/time -> conflicts -> redesign | Calendar plan | Protects priorities |

## P26 Education / Training

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P26.1 | "Curriculum" | Outcome -> modules -> sequence -> assessments | Curriculum | Progressive structure |
| P26.2 | "Lesson plan" | Objective -> explanation -> activity -> assessment | Lesson plan | Objective measurable |
| P26.3 | "Study guide" | Exam/topic -> concepts -> timeline -> practice | Study plan | Practice included |
| P26.4 | "Tutor me" | Diagnose level -> explain -> ask -> feedback -> next | Tutoring script | Adapts to learner |
| P26.5 | "Quiz / assessment" | Objectives -> item types -> answer key -> rubric | Assessment | Aligned to objectives |

## P27 Hiring / Career / Job Workflow

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P27.1 | "Job description" | Role -> outcomes -> skills -> scorecard -> JD | JD | Requirements justified |
| P27.2 | "Interview kit" | Scorecard -> questions -> rubric -> signals | Interview kit | Reduces bias |
| P27.3 | "Resume tailoring" | Target role -> candidate facts -> gap map -> rewrite | Tailored resume | Truthful, role-aligned |
| P27.4 | "Career plan" | Goal -> current state -> gaps -> plan -> milestones | Career plan | Actionable milestones |
| P27.5 | "Candidate outreach" | Role -> candidate context -> value -> CTA | Outreach message | Personalized |

## P28 Customer Support / Knowledge Base

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P28.1 | "FAQ" | Issues -> categories -> answers -> links -> escalation | FAQ | Answers actionable |
| P28.2 | "Support macro" | Ticket type -> empathy -> steps -> resolution -> escalation | Macro set | Tone and steps clear |
| P28.3 | "Triage flow" | Symptoms -> decision tree -> priority -> owner | Triage workflow | Escalation rules |
| P28.4 | "Help article" | User goal -> steps -> screenshots/notes -> troubleshooting | Help article | Self-service ready |
| P28.5 | "Voice of customer" | Feedback -> themes -> severity -> product asks | VoC report | Themes evidenced |

## P29 Scientific / Technical Protocol

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P29.1 | "Experiment design" | Hypothesis -> variables -> controls -> protocol -> analysis | Experiment plan | Controls defined |
| P29.2 | "Lab protocol" | Objective -> materials -> steps -> safety -> data | Protocol | Safety included |
| P29.3 | "Technical procedure" | System -> prerequisites -> steps -> validation -> rollback | Procedure | Repeatable |
| P29.4 | "Data interpretation" | Data -> method -> results -> caveats -> next tests | Interpretation memo | Claims bounded |
| P29.5 | "Safety / ethics review" | Activity -> risks -> mitigations -> approvals | Safety/ethics checklist | Risks explicit |

## P30 Prompt Library / Skill Creation

| Subcode | Trigger | Best workflow | Product | Checks |
|---|---|---|---|---|
| P30.1 | "Collect prompt library" | Sources -> license -> taxonomy -> import -> index | Prompt library | Sources tracked |
| P30.2 | "Create skill" | User tasks -> trigger -> workflow -> references -> validation | Skill folder | quick_validate passes |
| P30.3 | "Prompt card" | Use case -> inputs -> template -> examples -> checks | Prompt card | Reusable and testable |
| P30.4 | "Workflow matrix" | Domains -> subworkflows -> prompts -> outputs -> checks | Workflow matrix | Each row routes a task |
| P30.5 | "Prompt eval" | Criteria -> test cases -> outputs -> failure analysis -> revision | Eval report | Failures drive changes |

## Selection Heuristics

- If user asks for a final artifact, route by product output first.
- If user asks for "best way/process/workflow", route by professional process.
- If user asks for prompts, route by intended product, not by prompt wording.
- If multiple subworkflows match, choose the one with the highest risk if done poorly.
- If no subworkflow fits, use the parent P-code workflow and add a new candidate row after execution.
