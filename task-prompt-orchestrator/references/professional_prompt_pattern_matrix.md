# Professional Prompt Pattern Matrix

Use this when the task needs a specific prompt architecture: framing, context packing, evidence grounding, decomposition, templates, examples, rubrics, iteration, tools, batch generation, safety boundaries, or creative control. This matrix complements the scenario matrices by deciding how to write the actual prompt packet.

Selection rule:

1. Select task, operation, input, audience, constraint, verification, and domain codes first.
2. Choose one or more prompt pattern codes below.
3. Build the prompt packet using the selected pattern's structure and checks.
4. Prefer precise context, explicit output schemas, and observable quality checks over vague role-play.

## PRF Prompt Framing / Role and Objective

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| PRF01 | Expert role framing | Domain -> role -> responsibility -> boundaries | Role block | Role fits task |
| PRF02 | Objective-first prompt | Goal -> deliverable -> constraints -> success | Objective block | Goal unambiguous |
| PRF03 | Audience-first framing | Audience -> use case -> reading level -> tone | Audience block | Reader-specific |
| PRF04 | Task boundary framing | In scope -> out of scope -> assumptions -> risks | Boundary block | No hidden scope creep |
| PRF05 | Decision framing | Decision -> options -> criteria -> output | Decision prompt | Criteria explicit |
| PRF06 | Production framing | Asset/output -> specs -> handoff -> QA | Production prompt | Specs included |
| PRF07 | Review framing | Artifact -> criteria -> evidence -> findings | Review prompt | Finding-first |
| PRF08 | Teaching framing | Learner -> objective -> steps -> practice | Teaching prompt | Actionable practice |
| PRF09 | Crisis framing | Known facts -> unknowns -> safe message -> next update | Crisis prompt | No speculation |
| PRF10 | Multi-role framing | Roles -> responsibilities -> sequence -> final merge | Multi-role prompt | Roles do not overlap |

## CTX Context Packing / Input Organization

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| CTX01 | Brief packing | Goal -> inputs -> constraints -> output -> checks | Compact brief | All key fields |
| CTX02 | Source inventory packing | Sources -> relevance -> reliability -> gaps | Source pack | Gaps visible |
| CTX03 | File/path packing | Files -> purpose -> key excerpts -> actions | File context pack | Paths exact |
| CTX04 | Data schema packing | Tables -> columns -> grain -> caveats | Data context | Grain clear |
| CTX05 | Design asset packing | Assets -> dimensions -> style -> constraints | Design context | Visual facts |
| CTX06 | Conversation packing | Timeline -> decisions -> commitments -> open items | Conversation context | Speaker/action trace |
| CTX07 | Requirements packing | Stakeholders -> requirements -> acceptance -> risks | Requirements context | Testable |
| CTX08 | Long-context compression | Raw material -> summary -> important quotes -> unresolved | Context digest | No critical loss |
| CTX09 | Sensitive context packing | Minimized facts -> redactions -> audience boundary | Safe context pack | Sensitive data protected |
| CTX10 | Handoff context packing | Current state -> completed -> remaining -> next action | Handoff context | Resumable |

## GRD Grounded / Source-Backed Prompting

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| GRD01 | Cite-every-claim prompt | Claim types -> source rule -> citation format -> caveats | Grounded answer prompt | Key claims sourced |
| GRD02 | Evidence table prompt | Question -> sources -> evidence rows -> synthesis | Evidence table prompt | Source/date fields |
| GRD03 | Current-facts prompt | Freshness boundary -> browse/source -> date compare -> answer | Current-state prompt | Dates explicit |
| GRD04 | Source-limited prompt | Provided sources only -> scope -> unsupported label | Source-limited prompt | No outside inference |
| GRD05 | Contradiction prompt | Claims -> sources -> conflicts -> confidence | Contradiction prompt | Conflicts shown |
| GRD06 | Standards/regulation prompt | Authority -> version -> clauses -> obligations | Standards prompt | Version/date |
| GRD07 | Research synthesis prompt | Search strategy -> themes -> limits -> implications | Synthesis prompt | Limits stated |
| GRD08 | Fact-check prompt | Claim extraction -> verdict -> evidence -> correction | Fact-check prompt | Verdict per claim |
| GRD09 | Quote-safe prompt | Quote need -> max excerpt -> attribution -> summary | Quote-safe prompt | Copyright-safe |
| GRD10 | Uncertainty-aware prompt | Evidence -> confidence -> assumptions -> next verification | Uncertainty prompt | Confidence visible |

## DCP Decomposition / Step Planning

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| DCP01 | Atomic task breakdown | Goal -> steps -> dependencies -> done_when | Task plan | Each step executable |
| DCP02 | Research decomposition | Question -> subquestions -> sources -> synthesis | Research plan prompt | Subquestions cover goal |
| DCP03 | Build decomposition | Feature -> files -> changes -> tests -> release | Build prompt | Verification per step |
| DCP04 | Content decomposition | Audience -> outline -> sections -> evidence -> polish | Content prompt | Section purpose |
| DCP05 | Design decomposition | Brief -> references -> variants -> QA -> handoff | Design workflow prompt | Variant gates |
| DCP06 | Data decomposition | Source -> clean -> transform -> analyze -> visualize | Data workflow prompt | Grain preserved |
| DCP07 | Review decomposition | Artifact -> criteria -> findings -> fixes -> retest | Review workflow prompt | Severity order |
| DCP08 | Automation decomposition | Trigger -> inputs -> actions -> exceptions -> logs | Automation prompt | Failure paths |
| DCP09 | Learning decomposition | Objective -> concepts -> drills -> feedback -> review | Learning prompt | Skill progression |
| DCP10 | Multi-deliverable decomposition | Deliverables -> order -> shared inputs -> final package | Multi-output plan | Handoff consistency |

## TMP Templates / Variables / Reuse

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| TMP01 | Variable prompt template | Fixed structure -> variables -> instructions -> example | Fillable prompt | Variables clear |
| TMP02 | Domain template | Domain fields -> workflow -> outputs -> checks | Domain prompt template | Domain-specific |
| TMP03 | Output schema template | Fields -> types -> examples -> validation | Schema prompt | Parseable |
| TMP04 | Style template | Voice -> examples -> do/don't -> QA | Style prompt | Style repeatable |
| TMP05 | Review template | Criteria -> severity -> evidence -> recommendation | Review template | Finding format |
| TMP06 | Image prompt template | Subject -> composition -> style -> constraints -> negative | Image template | Reusable |
| TMP07 | Data query template | Question -> tables -> filters -> metrics -> output | Query prompt template | Logic explicit |
| TMP08 | Email/message template | Recipient -> context -> ask -> tone -> follow-up | Message template | Clear ask |
| TMP09 | SOP/checklist template | Trigger -> steps -> exceptions -> owner -> records | SOP template | Operational |
| TMP10 | Batch template | Variables -> naming -> variants -> QA criteria | Batch prompt template | Isolated variables |

## EXM Examples / Few-Shot Guidance

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| EXM01 | Format example | Target format -> good example -> output | Format-example prompt | Format matched |
| EXM02 | Tone example | Desired tone -> sample -> rewrite target | Tone-example prompt | Tone transferred |
| EXM03 | Classification examples | Labels -> positive/negative examples -> classify | Classifier prompt | Label boundaries |
| EXM04 | Rubric examples | Quality levels -> examples -> scoring | Rubric-example prompt | Levels distinct |
| EXM05 | Code example | Existing pattern -> new task -> constraints | Code-pattern prompt | Style followed |
| EXM06 | Visual example | Reference traits -> invariants -> new output | Visual-reference prompt | Invariants preserved |
| EXM07 | Bad example avoidance | Failure examples -> anti-patterns -> corrected output | Anti-pattern prompt | Failure avoided |
| EXM08 | Edge-case examples | Normal cases -> edge cases -> behavior | Edge-case prompt | Edge cases handled |
| EXM09 | Localization examples | Source -> local examples -> glossary | Localization example prompt | Locale natural |
| EXM10 | Teaching examples | Concept -> worked examples -> practice | Example-led lesson prompt | Transferable |

## RUB Rubrics / Evaluation Criteria

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| RUB01 | Quality rubric | Criteria -> levels -> examples -> scoring | Quality rubric prompt | Levels observable |
| RUB02 | Acceptance criteria | Requirements -> pass/fail -> evidence -> owner | Acceptance prompt | Testable |
| RUB03 | Review scoring | Artifact -> criteria -> score -> fixes | Scorecard prompt | Evidence tied |
| RUB04 | Risk rubric | Risk types -> severity -> likelihood -> mitigation | Risk rubric prompt | Severity justified |
| RUB05 | Creative rubric | Brief -> originality -> brand fit -> execution | Creative rubric prompt | Brief aligned |
| RUB06 | Data quality rubric | Completeness -> validity -> consistency -> timeliness | DQ rubric prompt | Data checks |
| RUB07 | Prompt evaluation rubric | Output -> criteria -> failure modes -> revision | Prompt eval prompt | Iteration path |
| RUB08 | Learning rubric | Objective -> levels -> evidence -> feedback | Learning rubric prompt | Actionable feedback |
| RUB09 | Vendor/proposal rubric | Criteria -> weights -> evidence -> recommendation | Proposal rubric prompt | Weighted criteria |
| RUB10 | Compliance rubric | Requirements -> controls -> evidence -> gaps | Compliance rubric prompt | Traceability |

## ITR Iteration / Refinement Loops

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| ITR01 | Draft-review-rewrite | Draft -> critique -> revision -> final QA | Iterative writing prompt | Changes address critique |
| ITR02 | Generate-select-refine | Variants -> selection criteria -> refine winner | Variant refinement prompt | Winner rationale |
| ITR03 | Prompt repair loop | Output defects -> root cause -> prompt revision -> retest | Prompt repair prompt | Failure isolated |
| ITR04 | Debug loop | Repro -> hypothesis -> patch -> test -> repeat | Debug prompt | Test after change |
| ITR05 | Design iteration | User feedback -> issues -> variants -> decision | Design iteration prompt | Feedback evidence |
| ITR06 | Data analysis iteration | Initial result -> anomalies -> deeper cuts -> final | Data iteration prompt | Assumptions updated |
| ITR07 | Research narrowing | Broad scan -> promising paths -> deeper evidence | Research iteration prompt | Search rationale |
| ITR08 | Stakeholder feedback loop | Feedback -> accept/reject -> update -> log | Feedback loop prompt | Rationale recorded |
| ITR09 | QA fix loop | Findings -> fixes -> retest -> residual risk | QA loop prompt | Retest explicit |
| ITR10 | Learning feedback loop | Attempt -> feedback -> drill -> reassess | Coaching loop prompt | Progress checked |

## TLS Tool / Skill / Script Orchestration

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| TLS01 | Existing skill selection | Task -> matching skill -> read instructions -> execute | Skill-use prompt | Skill used when relevant |
| TLS02 | Tool schema prompt | Tool goal -> arguments -> call -> validate output | Tool-call prompt | Schema respected |
| TLS03 | Shell/script workflow | Need -> command/script -> run -> inspect -> report | Script prompt | Output verified |
| TLS04 | Browser/source workflow | Need current/source -> browse -> cite -> synthesize | Browse prompt | Sources linked |
| TLS05 | File transformation workflow | Input file -> parser/tool -> transform -> validate | File workflow prompt | Artifact exists |
| TLS06 | Data tool workflow | Dataset -> query/tool -> result -> chart/report | Data tool prompt | Query reviewed |
| TLS07 | Design/media tool workflow | Creative brief -> generation/edit tool -> QA | Media tool prompt | Asset checked |
| TLS08 | Multi-tool workflow | Steps -> tool per step -> dependencies -> handoff | Multi-tool prompt | Handoffs clear |
| TLS09 | Fallback workflow | Preferred tool unavailable -> fallback -> limits | Fallback prompt | Limits reported |
| TLS10 | Automation workflow | Trigger -> tools -> monitoring -> escalation | Automation prompt | Logs/review gate |

## BAT Batch / Scale / Variants

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| BAT01 | Batch prompt generation | Items -> variables -> template -> naming | Batch prompt pack | Complete set |
| BAT02 | Multi-SKU generation | SKU attributes -> variants -> consistency -> QA | SKU batch prompt | SKU differences clear |
| BAT03 | Multi-channel adaptation | Master message -> channel specs -> variants | Channel variant pack | Channel-native |
| BAT04 | A/B creative variants | Hypothesis -> variants -> success criteria | A/B variant prompt | Variable isolated |
| BAT05 | Bulk classification | Items -> labels -> examples -> output table | Bulk tagging prompt | Label consistency |
| BAT06 | Bulk extraction | Documents -> fields -> confidence -> table | Bulk extraction prompt | Confidence fields |
| BAT07 | Batch localization | Source -> locales -> glossary -> QA | Localization batch prompt | Glossary applied |
| BAT08 | Batch review | Artifacts -> rubric -> findings table | Batch review prompt | Comparable severity |
| BAT09 | Dataset sampling prompt | Large set -> sample rules -> review -> extrapolate caveat | Sampling prompt | Sampling logic |
| BAT10 | Production package generation | Deliverables -> formats -> names -> handoff | Package prompt | All artifacts listed |

## SAF Safety / Boundary / Refusal-Safe Patterns

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| SAF01 | High-risk boundary prompt | Domain -> safe scope -> caveats -> professional review | Boundary prompt | Scope safe |
| SAF02 | Medical-safe prompt | Health request -> info only -> clinician questions | Medical-safe prompt | No diagnosis |
| SAF03 | Legal-safe prompt | Legal request -> issue spotting -> counsel questions | Legal-safe prompt | No legal advice |
| SAF04 | Finance-safe prompt | Finance request -> framework -> assumptions -> risks | Finance-safe prompt | No personal recommendation |
| SAF05 | Cyber-safe prompt | Security request -> authorization -> defensive steps | Cyber-safe prompt | No abuse guidance |
| SAF06 | Privacy-safe prompt | Data -> minimization -> redaction -> handling rules | Privacy-safe prompt | PII protected |
| SAF07 | IP-safe prompt | Sources/assets -> rights -> quote limits -> attribution | IP-safe prompt | Rights caveat |
| SAF08 | Minor-safe prompt | Audience age -> safe content -> guardian/escalation | Minor-safe prompt | Age-appropriate |
| SAF09 | Public-claim-safe prompt | Claim -> evidence -> softer wording -> review gate | Claim-safe prompt | Substantiation |
| SAF10 | Uncertainty-safe prompt | Unknowns -> assumptions -> confidence -> next verification | Uncertainty-safe prompt | No overclaim |

## CTV Creative / Style / Constraint Control

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| CTV01 | Style direction prompt | Mood -> references -> traits -> constraints | Style prompt | Style specific |
| CTV02 | Visual composition prompt | Subject -> framing -> camera -> lighting -> background | Composition prompt | Visual hierarchy |
| CTV03 | Brand voice prompt | Voice -> do/don't -> examples -> output | Brand voice prompt | On-brand |
| CTV04 | Narrative arc prompt | Audience -> hook -> conflict -> proof -> CTA | Story prompt | Arc clear |
| CTV05 | Concept route prompt | Insight -> routes -> rationale -> risks | Concept route prompt | Routes distinct |
| CTV06 | Negative prompt/control | Failure modes -> exclusions -> repair rules | Control prompt | Common failures blocked |
| CTV07 | Constraint-heavy creative | Brief -> hard constraints -> creative space -> QA | Constraint creative prompt | Constraints honored |
| CTV08 | Moodboard synthesis prompt | References -> shared traits -> palette -> direction | Moodboard prompt | Coherent direction |
| CTV09 | Campaign system prompt | Master idea -> variants -> channels -> consistency | Campaign prompt | Idea survives variants |
| CTV10 | Creative QA prompt | Output -> brief -> originality -> brand -> fixes | Creative QA prompt | Actionable critique |
