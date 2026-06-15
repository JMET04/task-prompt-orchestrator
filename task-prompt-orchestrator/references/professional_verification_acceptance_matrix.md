# Professional Verification and Acceptance Matrix

Use this when a task needs explicit completion criteria, QA, acceptance tests, evidence checks, or handoff validation. This matrix turns "looks good" into observable pass/fail checks.

Selection rule:

1. Select the normal P-code plus operation, input, industry, deliverable, audience, constraint, risk, lifecycle, and domain codes first.
2. Select one or more verification codes here.
3. Add the row's checks to `Done when`, `Quality checks`, and final reporting.
4. If a check cannot be performed, say so and report the residual risk instead of claiming completion.

## FAC Fact / Evidence Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| FAC01 | Claim support check | Extract claims -> match sources -> flag gaps | Claim evidence table | Every key claim covered |
| FAC02 | Freshness check | Identify time-sensitive facts -> verify current source -> date boundary | Freshness note | Date stated |
| FAC03 | Source authority check | Rank sources -> prefer primary/official -> caveat weak sources | Source quality note | Authority visible |
| FAC04 | Citation integrity | Citation -> claim -> page/section -> mismatch flag | Citation audit | No fake citations |
| FAC05 | Quote verification | Quote -> source location -> context -> length compliance | Quote check | Accurate and brief |
| FAC06 | Numeric fact check | Metric -> denominator -> period -> method -> recalc | Numeric check | Units and period |
| FAC07 | Contradiction check | Sources -> conflicting claims -> confidence -> resolution | Contradiction map | Conflict explicit |
| FAC08 | Scope boundary check | Output -> source scope -> unsupported inference -> caveat | Scope check | No overreach |
| FAC09 | Legal/regulatory version check | Rule -> jurisdiction -> version/effective date -> source | Version check | Current version |
| FAC10 | Evidence sufficiency check | Standard -> available evidence -> missing evidence -> next ask | Evidence gap list | Missing proof named |

## STRU Structure / Format Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| STRU01 | Required sections check | Spec -> section list -> output scan -> missing parts | Section checklist | All required sections |
| STRU02 | Table/schema check | Required columns -> row values -> types -> completeness | Table QA | Columns complete |
| STRU03 | JSON validity check | Schema -> output -> parse -> field validation | JSON QA | Valid parse |
| STRU04 | Template fill check | Variables -> filled values -> placeholders -> examples | Template QA | No raw placeholders |
| STRU05 | Naming convention check | Assets/files -> naming rule -> consistency -> collisions | Naming QA | Unique and clear |
| STRU06 | Length/word-count check | Requirement -> count -> trim/expand -> final | Length QA | Within limit |
| STRU07 | Heading hierarchy check | Outline -> heading levels -> flow -> links | Structure QA | Logical hierarchy |
| STRU08 | Cross-reference check | References -> links/figures/tables -> validity | Reference QA | No broken refs |
| STRU09 | Delivery format check | Requested format -> artifact type -> export/open test | Format QA | Opens correctly |
| STRU10 | Final handoff checklist | Deliverables -> paths -> summary -> verification | Handoff QA | User can locate output |

## COD Code / Software Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| CODV01 | Build check | Install/build command -> run -> capture errors -> fix/report | Build result | Build status stated |
| CODV02 | Unit test check | Relevant tests -> run -> failures -> fix/report | Test result | Tests cited |
| CODV03 | Integration test check | Service/dependency -> scenario -> run -> verify | Integration result | End-to-end path |
| CODV04 | Lint/type check | Project command -> run -> issues -> fix/report | Static check result | No new issues or caveat |
| CODV05 | Regression check | Changed behavior -> old path -> compare -> report | Regression note | Behavior preserved |
| CODV06 | Manual QA check | User flow -> steps -> observed result -> evidence | Manual QA note | Repro steps |
| CODV07 | Performance check | Baseline -> change -> benchmark -> compare | Performance result | Before/after metric |
| CODV08 | Security check | Changed surface -> auth/input/secrets -> scan/review | Security QA | Sensitive risks checked |
| CODV09 | Accessibility code check | Keyboard/screen reader/semantic checks -> fixes | A11y QA | Key flows covered |
| CODV10 | Deployment readiness check | Env vars -> build -> health check -> rollback | Deploy QA | Rollback/health path |

## DATV Data / Analytics Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| DATV01 | Row/record count check | Source -> transform -> output -> count compare | Count check | Counts reconciled |
| DATV02 | Null/missingness check | Fields -> null rates -> impact -> handling | Missingness report | Handling explicit |
| DATV03 | Duplicate check | Keys -> duplicate scan -> cause -> resolution | Duplicate report | Key defined |
| DATV04 | Join logic check | Tables -> join keys -> cardinality -> duplicates | Join QA | Grain preserved |
| DATV05 | Metric definition check | Metric -> formula -> filters -> dimensions | Metric QA | Formula clear |
| DATV06 | Outlier/anomaly check | Distribution -> anomalies -> explanation -> action | Outlier report | Outliers reviewed |
| DATV07 | Reconciliation check | Output -> source/control total -> variance -> cause | Reconciliation | Variance explained |
| DATV08 | Visualization check | Chart -> data mapping -> labels -> insight | Chart QA | No misleading scale |
| DATV09 | Sample/denominator check | Population -> sample -> denominator -> limits | Sample QA | Limitations stated |
| DATV10 | Reproducibility check | Query/code -> data version -> parameters -> rerun | Repro note | Rerun path clear |

## DESV Design / Visual Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| DESV01 | Visual hierarchy check | Objective -> focal point -> order -> clutter | Hierarchy QA | Primary message visible |
| DESV02 | Brand consistency check | Guidelines -> colors/type/logo -> deviations | Brand QA | Deviations flagged |
| DESV03 | Image prompt output check | Prompt -> output -> subject/style/constraints -> repair | Image QA | Subject preserved |
| DESV04 | Layout responsiveness check | Viewports -> layout -> text fit -> overlap | Responsive QA | No overlap |
| DESV05 | Print readiness check | Size -> bleed -> color -> resolution -> fonts | Print QA | Production specs |
| DESV06 | Packaging/CAD visual check | Views -> folds/cuts/dimensions -> callouts | Technical visual QA | Structure clear |
| DESV07 | Accessibility visual check | Contrast -> text size -> alt/labels -> focus | Visual a11y QA | Readable |
| DESV08 | Asset completeness check | Required formats -> sizes -> names -> exports | Asset QA | All assets present |
| DESV09 | Consistency across variants | Variant set -> invariants -> differences -> naming | Variant QA | Variables isolated |
| DESV10 | Creative brief alignment | Output -> brief -> audience -> message -> tone | Creative QA | Brief satisfied |

## DOCV Document / Writing Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| DOCV01 | Audience fit check | Audience -> tone -> detail level -> action | Audience QA | Reader-ready |
| DOCV02 | Logic flow check | Thesis -> sections -> transitions -> conclusion | Logic QA | Argument coherent |
| DOCV03 | Claim/risk language check | Claims -> evidence -> caveats -> safer wording | Risk-language QA | No overclaim |
| DOCV04 | Style guide check | Rules -> output -> violations -> fixes | Style QA | Consistent style |
| DOCV05 | Grammar/proof check | Text -> spelling -> punctuation -> formatting | Proof report | Clean final |
| DOCV06 | Completeness check | Requirements -> output -> missing items | Completeness QA | All asks answered |
| DOCV07 | Actionability check | Recommendations -> owners -> next steps -> criteria | Actionability QA | Next step clear |
| DOCV08 | Readability check | Complexity -> jargon -> sentence length -> rewrite | Readability QA | Appropriate level |
| DOCV09 | Localization check | Locale -> terminology -> cultural fit -> formatting | Localization QA | Locale natural |
| DOCV10 | Confidentiality check | Sensitive info -> redaction -> audience -> sharing | Confidentiality QA | No leakage |

## SLID Slide / Presentation Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| SLID01 | Storyline check | Audience -> narrative arc -> slide order -> ask | Storyline QA | Clear arc |
| SLID02 | Slide density check | Slide -> message -> text load -> visual balance | Density QA | One main idea |
| SLID03 | Chart/data slide check | Data -> chart -> labels -> takeaway | Chart slide QA | Insight visible |
| SLID04 | Speaker note check | Slide -> talking point -> transitions -> timing | Notes QA | Presenter-ready |
| SLID05 | Executive deck check | Summary -> decisions -> appendix -> risks | Exec deck QA | Decision-ready |
| SLID06 | Design consistency check | Theme -> type -> spacing -> components | Deck design QA | Consistent |
| SLID07 | Source/appendix check | Claims -> sources -> backup slides | Source QA | Backup available |
| SLID08 | Timing check | Agenda -> slide count -> speaking time | Timing QA | Fits time |
| SLID09 | Accessibility deck check | Contrast -> font size -> alt text -> reading order | Deck a11y QA | Accessible |
| SLID10 | Export/render check | Deck -> export -> open -> visual inspect | Export QA | Opens correctly |

## PRODV Production / Manufacturing Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| PRODV01 | Prototype gate | Concept -> prototype -> test criteria -> iteration | Prototype QA | Test required |
| PRODV02 | Material check | Material -> properties -> supplier -> constraints | Material QA | Fit to use |
| PRODV03 | Dimension/tolerance check | Drawing -> dimensions -> tolerance -> inspection | Dimension QA | Critical dims |
| PRODV04 | Print/packaging preflight | Dieline -> bleed -> colors -> folds -> marks | Packaging preflight | Print-safe |
| PRODV05 | Assembly check | Parts -> sequence -> tools -> failure modes | Assembly QA | Sequence clear |
| PRODV06 | Safety compliance check | Product/process -> hazards -> standards -> warnings | Safety QA | Review gate |
| PRODV07 | Supplier handoff check | Spec -> samples -> acceptance -> records | Supplier QA | Acceptance criteria |
| PRODV08 | Inspection sampling check | Lot -> sample -> test -> disposition | Inspection QA | Sampling method |
| PRODV09 | Labeling/marking check | Required labels -> language -> placement -> durability | Label QA | Mandatory marks |
| PRODV10 | Production readiness check | Specs -> process -> QC -> owners -> go/no-go | Production readiness | Go/no-go clear |

## COMV Communication / Publication Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| COMV01 | Message clarity check | Audience -> message -> ask -> confusion points | Clarity QA | Ask obvious |
| COMV02 | Tone/sensitivity check | Context -> emotion -> risk -> rewrite | Tone QA | Respectful |
| COMV03 | Public claim check | Claims -> substantiation -> risk -> legal review | Claim QA | Claims supported |
| COMV04 | Channel fit check | Channel -> format -> length -> CTA -> timing | Channel QA | Native to channel |
| COMV05 | Crisis comms check | Facts -> unknowns -> next update -> approvals | Crisis QA | No speculation |
| COMV06 | Customer response check | Issue -> empathy -> resolution -> policy -> next step | Response QA | No false promise |
| COMV07 | Internal alignment check | Stakeholders -> message -> decisions -> actions | Internal QA | Consistent |
| COMV08 | PR/media check | News -> quote -> proof -> boilerplate -> contact | PR QA | Fact checked |
| COMV09 | Legal/compliance approval check | Content -> claims -> rights -> review status | Approval QA | Status explicit |
| COMV10 | Localization publication check | Locale -> translation -> cultural risk -> formatting | Local publish QA | Locale-ready |

## UXV Usability / User Experience Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| UXV01 | Task completion check | User goal -> steps -> success/failure -> fixes | Usability QA | Core task works |
| UXV02 | Navigation check | IA -> labels -> paths -> dead ends | Navigation QA | Findability |
| UXV03 | Form usability check | Fields -> validation -> errors -> completion | Form QA | Error recovery |
| UXV04 | Onboarding check | Activation -> steps -> friction -> guidance | Onboarding QA | Activation measurable |
| UXV05 | Mobile ergonomics check | Viewport -> touch targets -> layout -> text | Mobile UX QA | Usable on mobile |
| UXV06 | Accessibility usability check | Keyboard -> screen reader -> focus -> labels | A11y UX QA | Assistive tech |
| UXV07 | Empty/error state check | States -> message -> action -> recovery | State QA | Recovery path |
| UXV08 | User research evidence check | Findings -> quotes -> severity -> recommendations | Research QA | Evidence per finding |
| UXV09 | Conversion path check | Landing -> trust -> CTA -> checkout/lead | Conversion QA | Friction identified |
| UXV10 | Help/support check | Need -> help content -> escalation -> feedback | Support UX QA | User can recover |

## RSKV Risk / Compliance Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| RSKV01 | High-risk boundary check | Domain -> risk -> safer framing -> review gate | Risk boundary note | Boundary explicit |
| RSKV02 | Privacy check | Data -> purpose -> minimization -> retention | Privacy QA | PII controlled |
| RSKV03 | Security check | Access -> secrets -> abuse paths -> controls | Security risk QA | No secret exposure |
| RSKV04 | Legal advice check | Output -> legal conclusions -> caveats -> counsel questions | Legal boundary QA | Not legal advice |
| RSKV05 | Medical advice check | Output -> diagnosis/treatment risk -> clinician boundary | Medical boundary QA | No diagnosis |
| RSKV06 | Financial advice check | Output -> personal recommendation risk -> assumptions | Finance boundary QA | No guaranteed return |
| RSKV07 | IP/copyright check | Sources/assets -> rights -> quote limits -> attribution | Rights QA | Usage safe |
| RSKV08 | Employment fairness check | Criteria -> evidence -> protected-class risk | Fairness QA | Job-related |
| RSKV09 | Safety/manufacturing check | Instructions -> hazards -> professional review | Safety QA | Hazard warning |
| RSKV10 | Public reputation check | Message -> stakeholders -> facts -> escalation | Reputation QA | Tone/facts safe |

## HND Handoff / Maintainability Verification

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| HND01 | Owner handoff check | Artifact -> owner -> next action -> due date | Handoff checklist | Owner/date |
| HND02 | Reuse check | Template/assets -> variables -> examples -> limits | Reuse QA | Reusable |
| HND03 | Documentation check | Artifact -> instructions -> assumptions -> references | Documentation QA | Future reader can resume |
| HND04 | Versioning check | File/version -> changes -> date -> author/source | Version note | Version clear |
| HND05 | Archive check | Files -> index -> retention -> access | Archive QA | Retrievable |
| HND06 | Decision log check | Decisions -> rationale -> owner -> follow-up | Decision log QA | Rationale captured |
| HND07 | Dependency check | Inputs/tools -> dependencies -> risks -> alternatives | Dependency QA | Critical deps |
| HND08 | Monitoring check | Output/process -> metrics -> cadence -> owner | Monitoring QA | Ongoing owner |
| HND09 | Rollback/recovery check | Change -> rollback -> backup -> trigger | Recovery QA | Reversible |
| HND10 | Final user-readiness check | Deliverable -> open/read/use -> next step | User-readiness QA | User can act |
