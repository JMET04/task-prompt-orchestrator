# Professional Audience and Context Matrix

Use this when the final output must be adapted to a specific reader, decision maker, user group, or communication context. Audience changes language, evidence depth, risk framing, action granularity, and format.

Selection rule:

1. Select the normal P-code plus any input, industry, deliverable, risk, deep-domain, and lifecycle codes first.
2. Select the closest audience/context code here.
3. Add its framing and checks to the prompt packet under `Audience / use case`, `Output format`, and `Quality checks`.
4. If multiple audiences exist, produce separate versions or a layered output: executive summary, practitioner detail, and appendix.

## EXC Executive / Decision Maker

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| EXC01 | CEO/owner decision | Context -> options -> tradeoffs -> recommendation -> ask | Executive decision memo | Clear ask |
| EXC02 | Board audience | Metrics -> narrative -> risks -> decisions -> appendix | Board brief | Decision-focused |
| EXC03 | Department head | Objective -> constraints -> impact -> resources -> next step | Department brief | Operational impact |
| EXC04 | Investor/LP update | Performance -> milestones -> risks -> asks | Investor update | Honest, concise |
| EXC05 | Crisis leadership | Facts -> impact -> options -> comms -> next update | Crisis leadership brief | No speculation |
| EXC06 | Budget approver | Need -> cost -> benefit -> alternatives -> risk | Budget request | Assumptions visible |
| EXC07 | Strategy review | Market -> options -> criteria -> recommendation | Strategy memo | Tradeoffs explicit |
| EXC08 | M&A/partnership decision | Fit -> value -> risks -> diligence gaps | Deal decision brief | Unknowns flagged |
| EXC09 | Product leadership | User value -> roadmap impact -> metrics -> risks | Product leadership note | Outcome-linked |
| EXC10 | Final signoff | Summary -> evidence -> open risks -> approval ask | Signoff packet | Go/no-go clear |

## FRO Frontline / Operations User

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| FRO01 | Operator instruction | Trigger -> steps -> tools -> checks -> escalation | Work instruction | Actionable on shift |
| FRO02 | Support agent | Customer issue -> script -> policy -> resolution -> escalation | Support playbook | Empathy and accuracy |
| FRO03 | Sales rep | Buyer context -> talk track -> objections -> next ask | Sales enablement note | Call-ready |
| FRO04 | Warehouse/logistics user | Task -> location -> scan/check -> exception path | Ops checklist | Exceptions clear |
| FRO05 | Field technician | Symptom -> diagnosis -> tools -> safety -> report | Field guide | Safety warnings |
| FRO06 | Retail staff | Product -> talking points -> demo -> FAQ | Retail quick guide | Short and scannable |
| FRO07 | Manufacturing worker | Operation -> setup -> steps -> QC -> defects | Production instruction | Visual/step clarity |
| FRO08 | Customer success manager | Account -> usage -> risk -> value proof -> next action | CSM brief | Account-specific |
| FRO09 | Moderator/community manager | Situation -> rule -> response -> escalation | Moderation guide | Fair enforcement |
| FRO10 | On-call responder | Alert -> impact -> runbook -> mitigation -> handoff | On-call brief | Time-critical order |

## NOV Beginner / Non-Expert

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| NOV01 | First-time learner | Goal -> simple model -> first action -> practice | Beginner guide | No jargon overload |
| NOV02 | Nontechnical stakeholder | Concept -> analogy -> implications -> questions | Plain-language explainer | Accurate simplification |
| NOV03 | New employee | Context -> role -> workflows -> first week tasks | Onboarding brief | Next steps concrete |
| NOV04 | AI beginner | Goal -> one workflow -> prompt -> review step | AI starter workflow | Low cognitive load |
| NOV05 | Student | Objective -> explanation -> examples -> practice -> feedback | Learning note | Checks understanding |
| NOV06 | Customer unfamiliar with product | Problem -> value -> steps -> support | Customer explainer | No assumed knowledge |
| NOV07 | Policy beginner | Rule -> who it affects -> what to do -> examples | Plain policy guide | Obligations clear |
| NOV08 | Data beginner | Metric -> meaning -> caveats -> action | Data explainer | No false precision |
| NOV09 | Safety beginner | Hazard -> safe steps -> stop conditions -> help | Safety quick guide | Caution prominent |
| NOV10 | Tool beginner | Setup -> basic command/action -> verify -> next | Tool quickstart | Reproducible |

## EXP Expert / Reviewer

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| EXP01 | Domain expert review | Assumptions -> method -> evidence -> limitations | Expert review packet | Technical depth |
| EXP02 | Peer reviewer | Contribution -> method -> results -> weaknesses | Peer review response | Claims precise |
| EXP03 | Senior engineer | Architecture -> tradeoffs -> edge cases -> tests | Engineering review note | Failure modes |
| EXP04 | Legal counsel | Facts -> clauses -> questions -> risk options | Counsel packet | No legal conclusion |
| EXP05 | Clinician/scientist | Population -> evidence -> uncertainty -> questions | Clinical/science brief | Limits explicit |
| EXP06 | Auditor | Control -> evidence -> exception -> remediation | Audit evidence pack | Traceability |
| EXP07 | Security reviewer | Threats -> controls -> exploitability -> fixes | Security review packet | Severity justified |
| EXP08 | Finance reviewer | Model -> assumptions -> sensitivities -> checks | Finance review packet | Calculations auditable |
| EXP09 | Design critic | Objective -> constraints -> rationale -> alternatives | Design review packet | Rationale visible |
| EXP10 | Standards/certification expert | Clauses -> evidence -> gaps -> test plan | Standards review packet | Clause mapped |

## BUY Buyer / Customer / End User

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| BUY01 | B2B buyer | Pain -> value -> proof -> risk reduction -> next step | Buyer brief | Business outcome |
| BUY02 | Consumer shopper | Need -> benefits -> proof -> comparison -> CTA | Consumer copy | Clear and truthful |
| BUY03 | Existing customer | Usage -> value -> new capability -> action | Customer update | No surprise obligations |
| BUY04 | Churn-risk customer | Issue -> empathy -> fix -> value proof -> follow-up | Save message | Customer-centered |
| BUY05 | Technical buyer | Requirements -> architecture -> security -> integration | Technical buyer brief | Integration specifics |
| BUY06 | Procurement buyer | Requirements -> compliance -> pricing -> risks | Procurement response | Requirements answered |
| BUY07 | Enterprise stakeholder group | Personas -> value map -> objections -> mutual plan | Enterprise account brief | Stakeholders distinct |
| BUY08 | Marketplace shopper | Listing -> trust -> reviews -> delivery/returns | Listing copy | Platform-safe claims |
| BUY09 | Community/user base | Change -> impact -> benefits -> support path | User announcement | Impact clear |
| BUY10 | Dissatisfied customer | Facts -> apology/clarity -> remedy -> prevention | Customer response | No false promise |

## DEV Developer / Technical Implementer

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| DEV01 | API implementer | Use case -> endpoints -> auth -> examples -> errors | API implementation guide | Runnable examples |
| DEV02 | Maintainer | Change -> rationale -> files -> tests -> risks | Maintainer handoff | Code references |
| DEV03 | DevOps engineer | Service -> deploy -> monitor -> rollback -> runbook | Ops implementation brief | Rollback clear |
| DEV04 | Data engineer | Source -> schema -> transform -> validation -> refresh | Data pipeline spec | Grain and checks |
| DEV05 | QA engineer | Risk -> cases -> data -> automation -> reporting | QA implementation plan | Testable cases |
| DEV06 | Security engineer | System -> threats -> controls -> evidence -> fixes | Security implementation brief | Control mapping |
| DEV07 | Frontend engineer | Screens -> states -> data -> interactions -> a11y | Frontend spec | States complete |
| DEV08 | Backend engineer | Domain -> data model -> services -> errors -> tests | Backend spec | Edge cases |
| DEV09 | Integration engineer | Systems -> contracts -> auth -> failure modes | Integration spec | Idempotency/errors |
| DEV10 | Technical writer | Feature -> audience -> examples -> caveats -> docs | Docs handoff | Accurate API behavior |

## CRE Creative / Brand / Design Stakeholder

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| CRE01 | Creative director | Brief -> concept routes -> rationale -> risks | Creative route deck | Distinct routes |
| CRE02 | Brand manager | Brand rules -> message -> assets -> governance | Brand-ready brief | Brand consistency |
| CRE03 | Graphic designer | Layout -> hierarchy -> assets -> constraints | Design production brief | Production specs |
| CRE04 | Photographer/visual producer | Shot goal -> subject -> lighting -> props -> deliverables | Shot brief | Shot list complete |
| CRE05 | Video editor | Story -> footage -> selects -> pacing -> captions | Edit brief | Timeline and assets |
| CRE06 | Copywriter | Audience -> promise -> proof -> tone -> variants | Copy brief | Voice aligned |
| CRE07 | UX designer | User goal -> flow -> states -> copy -> constraints | UX brief | User task centered |
| CRE08 | Packaging designer | Product -> panels -> claims -> print/process limits | Packaging creative brief | Print-safe |
| CRE09 | Motion designer | Key frames -> timing -> transitions -> export specs | Motion brief | Timing clear |
| CRE10 | Agency/vendor creative | Scope -> references -> deliverables -> review gates | Vendor creative brief | Approval path |

## EDU Educator / Trainer / Coach

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| EDUA01 | Teacher | Objective -> explanation -> activity -> assessment | Lesson material | Objective measurable |
| EDUA02 | Trainer | Role -> skill -> scenario -> practice -> debrief | Training module | Practice included |
| EDUA03 | Coach | Goal -> current state -> blocker -> drill -> reflection | Coaching plan | Next action |
| EDUA04 | Curriculum designer | Outcomes -> modules -> sequence -> assessments | Curriculum map | Prerequisites |
| EDUA05 | Tutor | Learner output -> misconception -> explanation -> practice | Tutoring response | Misconception addressed |
| EDUA06 | Workshop facilitator | Outcome -> agenda -> activity -> materials -> timing | Facilitation guide | Timeboxed |
| EDUA07 | Certification prep user | Exam objectives -> plan -> drills -> review | Prep plan | Objective coverage |
| EDUA08 | Corporate enablement | Role -> behavior -> scenarios -> job aids -> metrics | Enablement pack | Transfer to work |
| EDUA09 | Parent/guardian support | Learner context -> safe support -> practice -> escalation | Support guide | Age-appropriate |
| EDUA10 | Self-learner | Goal -> sequence -> resources -> feedback loop | Self-study plan | Progress checks |

## REG Regulator / Auditor / Compliance Reader

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| REGA01 | External auditor | Scope -> evidence -> controls -> exceptions -> remediation | Audit packet | Evidence trace |
| REGA02 | Regulator | Requirement -> response -> evidence -> commitments | Regulator response | Precise commitments |
| REGA03 | Internal compliance | Policy -> control -> gap -> owner -> deadline | Compliance memo | Owner/date |
| REGA04 | Privacy officer | Data flow -> purpose -> controls -> risks | Privacy review | Data minimization |
| REGA05 | Legal reviewer | Claims -> substantiation -> rights -> caveats | Legal review packet | Claims supported |
| REGA06 | Quality auditor | Process -> records -> nonconformity -> CAPA | Quality audit brief | Standard clauses |
| REGA07 | Safety officer | Hazard -> controls -> training -> records | Safety review | Stop conditions |
| REGA08 | Procurement compliance | Requirements -> supplier evidence -> exceptions | Procurement compliance matrix | Requirement coverage |
| REGA09 | Ethics/review board | Study/use case -> risks -> consent -> safeguards | Ethics review brief | Participant/user protection |
| REGA10 | Records manager | Records -> retention -> access -> disposition | Records plan | Retention basis |

## INV Investor / Analyst / Market Reader

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INV01 | VC investor | Market -> product -> traction -> risks -> ask | Investor memo | Thesis and risks |
| INV02 | Public equity analyst | Company -> financials -> catalysts -> valuation -> risks | Equity memo | Source-backed |
| INV03 | LP/fund stakeholder | Portfolio -> performance -> attribution -> outlook | LP update | Honest attribution |
| INV04 | Credit analyst | Borrower -> cash flow -> covenants -> downside | Credit brief | Downside case |
| INV05 | Strategic acquirer | Fit -> synergies -> diligence gaps -> integration | Acquisition brief | Synergy assumptions |
| INV06 | Startup founder investor-facing | Metrics -> narrative -> use of funds -> milestones | Fundraising narrative | Credible assumptions |
| INV07 | Market researcher | Category -> players -> drivers -> forecast -> risks | Market analysis | Method transparent |
| INV08 | Due diligence team | Documents -> issues -> evidence -> open requests | Diligence tracker | Open items |
| INV09 | Investment committee | Thesis -> evidence -> risks -> decision -> conditions | IC memo | Decision conditions |
| INV10 | Retail investor education | Concept -> risks -> examples -> questions | Investor education note | No personal advice |

## HRP People / HR / Employee Audience

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| HRPA01 | Hiring manager | Role -> scorecard -> interview plan -> decision criteria | Hiring brief | Job-related criteria |
| HRPA02 | Candidate | Role -> process -> expectations -> next steps | Candidate communication | Fair and clear |
| HRPA03 | Employee | Policy/change -> impact -> action -> support | Employee notice | Plain language |
| HRPA04 | Manager | Situation -> feedback -> documentation -> follow-up | Manager script | Specific behavior |
| HRPA05 | HRBP | Facts -> policy -> options -> risks -> recommendation | HR advisory note | Fair process |
| HRPA06 | New hire | Role -> first tasks -> contacts -> checkpoints | New hire guide | 30/60/90 clear |
| HRPA07 | Team | Goal -> norms -> roles -> cadence -> escalation | Team operating guide | Ownership clear |
| HRPA08 | Survey respondent group | Findings -> themes -> actions -> confidentiality | Engagement summary | Aggregated safely |
| HRPA09 | Performance review reader | Evidence -> impact -> growth -> goals | Review draft | Evidence-based |
| HRPA10 | Layoff/reorg audience | Facts -> support -> timeline -> FAQ -> contacts | Sensitive HR comms | Legal/HR review gate |

## PUB Public / Community / Media Audience

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| PUBA01 | General public | Message -> context -> impact -> action -> FAQ | Public explainer | Plain and accurate |
| PUBA02 | Press/media | News -> facts -> quote -> proof -> contact | Media release | Newsworthy and sourced |
| PUBA03 | Social audience | Hook -> point -> examples -> CTA -> moderation | Social post/thread | Platform fit |
| PUBA04 | Community members | Issue -> rules -> impact -> actions -> appeal path | Community update | Fairness clear |
| PUBA05 | Crisis-affected audience | Facts -> empathy -> action -> next update | Crisis update | No speculation |
| PUBA06 | Donors/supporters | Mission -> impact -> proof -> ask -> stewardship | Supporter message | Proof of impact |
| PUBA07 | Local community | Project -> impacts -> mitigation -> feedback path | Local community brief | Concerns addressed |
| PUBA08 | Event attendees | Agenda -> logistics -> expectations -> support | Attendee guide | Practical details |
| PUBA09 | Advocacy audience | Problem -> stakes -> action -> evidence -> urgency | Advocacy brief | Ethical urgency |
| PUBA10 | Reputation-sensitive audience | Stakeholders -> risk -> tone -> proof -> response | Reputation message | Tone and facts checked |
