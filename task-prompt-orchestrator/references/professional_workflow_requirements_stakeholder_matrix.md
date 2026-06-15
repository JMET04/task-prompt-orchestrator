# Professional Workflow Requirements and Stakeholder Discovery Matrix

Use this when a workflow must discover, clarify, align, prioritize, or validate what should be built, produced, changed, analyzed, or delivered before execution begins. Requirements and stakeholder discovery rules define who matters, what they need, why it matters, what constraints apply, how requirements are prioritized, and what proves shared agreement.

Selection rule:

1. Identify the decision, deliverable, process, product, service, or change being requested.
2. Select the closest requirement/stakeholder discovery code.
3. Add stakeholder, need, problem, success criteria, scope, priority, constraint, acceptance, dependency, and agreement evidence to the prompt packet.
4. Do not start high-cost execution until the requirement boundary and decision owner are explicit.

## STKMAP Stakeholder Mapping

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| STKMAP01 | Requester mapping | Identify who asked and why | Confirm requester authority | Requester note |
| STKMAP02 | End-user mapping | Identify who will use output | Separate user from buyer/owner | User map |
| STKMAP03 | Decision-owner mapping | Identify who can decide tradeoffs | Assign accountable owner | Owner record |
| STKMAP04 | Reviewer mapping | Identify who checks quality/domain fit | Match reviewer to risk area | Reviewer map |
| STKMAP05 | Approver mapping | Identify who signs off | Define approval threshold | Approval map |
| STKMAP06 | Operator mapping | Identify who runs workflow later | Include runbook needs | Operator map |
| STKMAP07 | Support mapping | Identify who handles questions/issues | Include support handoff | Support map |
| STKMAP08 | Impacted-party mapping | Identify people affected indirectly | Add change-impact review | Impact map |
| STKMAP09 | External stakeholder mapping | Identify clients/vendors/regulators/public | Define communication boundary | External map |
| STKMAP10 | Missing stakeholder mapping | Stakeholder set is incomplete | Ask/assume/escalate by risk | Stakeholder gap |

## REQINT Requirement Intake

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| REQINT01 | Raw request capture | Capture exact user wording | Preserve original ask before rewrite | Raw request |
| REQINT02 | Goal capture | Convert request into testable goal | Require observable outcome | Goal brief |
| REQINT03 | Deliverable capture | Define output artifact and format | Avoid vague "help me" scope | Deliverable spec |
| REQINT04 | Use-case capture | Define where output will be used | Link to audience/context | Use-case note |
| REQINT05 | Urgency capture | Capture deadline and time sensitivity | Match depth to urgency | Urgency note |
| REQINT06 | Constraint capture | Capture format, budget, platform, policy | Make constraints explicit | Constraint list |
| REQINT07 | Source capture | Capture files, links, data, references | Inventory source readiness | Source intake |
| REQINT08 | Quality bar capture | Capture depth, polish, evidence, QA level | Define quality standard | Quality bar |
| REQINT09 | Decision capture | Capture decision needed from output | Separate analysis from decision | Decision ask |
| REQINT10 | Intake completeness | Check required intake fields | Mark blockers vs safe assumptions | Intake checklist |

## PROBFR Problem Framing

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| PROBFR01 | Symptom framing | Separate symptom from problem | Ask what failure or opportunity exists | Symptom note |
| PROBFR02 | Root problem framing | Identify underlying problem | Use evidence, not assumption | Problem statement |
| PROBFR03 | Jobs-to-be-done framing | Define user job/outcome | Link to user context | JTBD note |
| PROBFR04 | Opportunity framing | Define upside being pursued | State value hypothesis | Opportunity note |
| PROBFR05 | Risk framing | Define harm being avoided | Link to risk owner | Risk frame |
| PROBFR06 | Cause framing | Distinguish cause from correlation | Require causal evidence or caveat | Cause note |
| PROBFR07 | Problem boundary | Define what is not the problem | Avoid solution sprawl | Boundary note |
| PROBFR08 | Evidence framing | Identify proof that problem exists | Capture source/metric/observation | Evidence note |
| PROBFR09 | Alternative framing | Compare possible problem definitions | Choose frame by decision value | Frame options |
| PROBFR10 | Problem agreement | Confirm shared problem statement | Owner accepts framing | Problem signoff |

## GOALAL Goal Alignment

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| GOALAL01 | Business goal alignment | Link work to business objective | Avoid detached deliverables | Business goal |
| GOALAL02 | User goal alignment | Link work to user outcome | Check user journey impact | User goal |
| GOALAL03 | Operational goal alignment | Link work to process/service result | Check operator feasibility | Ops goal |
| GOALAL04 | Learning goal alignment | Link work to skill/knowledge outcome | Define practice/evaluation | Learning goal |
| GOALAL05 | Compliance goal alignment | Link work to control/regulatory need | Define evidence requirement | Compliance goal |
| GOALAL06 | Quality goal alignment | Link work to quality standard | Define measurable pass rule | Quality goal |
| GOALAL07 | Strategic goal alignment | Link work to roadmap/strategy | Check tradeoff with priorities | Strategy goal |
| GOALAL08 | Metric goal alignment | Link work to measurable KPI | Define denominator and cadence | Metric goal |
| GOALAL09 | Conflicting goal alignment | Goals conflict across stakeholders | Resolve or escalate tradeoff | Goal conflict |
| GOALAL10 | Goal freeze | Goal stable enough for execution | Record change rule | Goal freeze |

## SCOPEDEF Scope Definition

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| SCOPEDEF01 | In-scope definition | Define included work/items | Tie to acceptance criteria | In-scope list |
| SCOPEDEF02 | Out-of-scope definition | Define excluded work/items | Prevent implicit expansion | Out-scope list |
| SCOPEDEF03 | Non-goal definition | Define what success does not require | Avoid false expectations | Non-goal note |
| SCOPEDEF04 | Depth definition | Define shallow/standard/deep treatment | Match depth to value/risk | Depth note |
| SCOPEDEF05 | Variant scope | Define versions/audiences/locales | Bound variant count | Variant scope |
| SCOPEDEF06 | Phase scope | Define current phase vs later phases | Prevent future work leakage | Phase scope |
| SCOPEDEF07 | Data scope | Define data fields/time range/grain | Prevent source creep | Data scope |
| SCOPEDEF08 | Channel scope | Define platforms/formats/channels | Match deliverable specs | Channel scope |
| SCOPEDEF09 | Risk scope | Define high-risk areas needing gates | Route risk-specific review | Risk scope |
| SCOPEDEF10 | Scope change rule | Define how scope can change | Require owner decision | Scope rule |

## CONREQ Constraint Requirements

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| CONREQ01 | Time constraint | Capture deadline/timebox/cadence | Plan backward from limit | Time constraint |
| CONREQ02 | Budget constraint | Capture spend/resource ceiling | Fit scope to budget | Budget constraint |
| CONREQ03 | Tool constraint | Capture required/forbidden tools | Verify access and fallback | Tool constraint |
| CONREQ04 | Format constraint | Capture output format/spec | Validate before delivery | Format constraint |
| CONREQ05 | Brand constraint | Capture tone/style/visual rules | Add brand review if public | Brand constraint |
| CONREQ06 | Legal constraint | Capture jurisdiction/contract/claims limit | Route legal uncertainty | Legal constraint |
| CONREQ07 | Privacy constraint | Capture data sensitivity/access limits | Minimize and redact | Privacy constraint |
| CONREQ08 | Accessibility constraint | Capture inclusive access needs | Add accessibility check | Access constraint |
| CONREQ09 | Language/locale constraint | Capture locale/glossary/cultural limits | Localize appropriately | Locale constraint |
| CONREQ10 | Conflicting constraint | Constraints cannot all be satisfied | Ask owner to trade off | Constraint conflict |

## PRIORREQ Requirement Prioritization

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| PRIORREQ01 | Must-have priority | Identify non-negotiable requirements | Block delivery if unmet | Must-have list |
| PRIORREQ02 | Should-have priority | Identify important but negotiable items | Track if deferred | Should-have list |
| PRIORREQ03 | Could-have priority | Identify optional improvements | Include only if capacity exists | Could-have list |
| PRIORREQ04 | Won't-now priority | Identify deferred/out-of-scope items | Record future backlog | Won't-now list |
| PRIORREQ05 | Value priority | Rank by user/business value | Use explicit value criteria | Value ranking |
| PRIORREQ06 | Risk priority | Rank by risk reduction | Prioritize high-harm uncertainty | Risk ranking |
| PRIORREQ07 | Effort priority | Rank by effort/cost/time | Combine with value/risk | Effort ranking |
| PRIORREQ08 | Dependency priority | Rank prerequisite requirements first | Respect dependency order | Dependency ranking |
| PRIORREQ09 | Deadline priority | Rank by time-criticality | Protect urgent must-haves | Deadline ranking |
| PRIORREQ10 | Priority conflict | Stakeholders disagree on priority | Use decision owner and criteria | Priority decision |

## ACCREQ Acceptance Requirements

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| ACCREQ01 | Acceptance criteria | Define pass/fail conditions | Criteria must be observable | Acceptance list |
| ACCREQ02 | Definition of done | Define completion state | Include output, evidence, handoff | Done definition |
| ACCREQ03 | Quality acceptance | Define quality threshold | Use rubric/checklist | Quality acceptance |
| ACCREQ04 | Technical acceptance | Define build/test/schema requirements | Require test evidence | Technical acceptance |
| ACCREQ05 | Business acceptance | Define owner value criteria | Owner signs off | Business acceptance |
| ACCREQ06 | User acceptance | Define user task success | UAT/sample feedback | User acceptance |
| ACCREQ07 | Compliance acceptance | Define policy/legal/security gates | Gate owner signs off | Compliance acceptance |
| ACCREQ08 | Evidence acceptance | Define required proof artifacts | No proof, no completion | Evidence acceptance |
| ACCREQ09 | Partial acceptance | Define acceptable partial delivery | Track residual gaps | Partial acceptance |
| ACCREQ10 | Acceptance change | Criteria changed after work starts | Re-baseline scope and impact | Acceptance change |

## DEPENDREQ Dependency Discovery

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| DEPENDREQ01 | Upstream dependency | Identify needed input/source/approval | Assign owner and due date | Upstream map |
| DEPENDREQ02 | Downstream dependency | Identify who consumes output | Validate handoff contract | Downstream map |
| DEPENDREQ03 | System dependency | Identify tool/API/database/file dependency | Verify availability | System dependency |
| DEPENDREQ04 | Data dependency | Identify dataset/schema/freshness dependency | Define data contract | Data dependency |
| DEPENDREQ05 | Human dependency | Identify SME/reviewer/approver dependency | Reserve capacity | Human dependency |
| DEPENDREQ06 | Vendor dependency | Identify supplier/platform/vendor dependency | Define escalation path | Vendor dependency |
| DEPENDREQ07 | Schedule dependency | Identify timing/order dependency | Add milestone dependency | Schedule dependency |
| DEPENDREQ08 | Compliance dependency | Identify required policy/legal gate | Gate before release | Compliance dependency |
| DEPENDREQ09 | Dependency risk | Dependency may fail or delay | Add fallback/contingency | Dependency risk |
| DEPENDREQ10 | Dependency closure | Dependency resolved | Record evidence before proceeding | Dependency closure |

## ASSUMP Assumption Management

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| ASSUMP01 | Safe assumption | Missing info is low-risk | State assumption and proceed | Safe assumption |
| ASSUMP02 | Blocking assumption | Missing info changes output materially | Ask or block before execution | Blocker note |
| ASSUMP03 | Risky assumption | Assumption could cause harm/rework | Escalate or add review gate | Risk assumption |
| ASSUMP04 | Source assumption | Source quality/freshness unknown | Mark confidence and refresh rule | Source assumption |
| ASSUMP05 | User assumption | User/audience not fully known | Select default persona and caveat | User assumption |
| ASSUMP06 | Format assumption | Output spec missing | Choose standard format and note | Format assumption |
| ASSUMP07 | Scope assumption | Boundary unclear | Define provisional scope | Scope assumption |
| ASSUMP08 | Tool assumption | Tool availability uncertain | Define fallback path | Tool assumption |
| ASSUMP09 | Assumption validation | Assumption needs confirmation later | Add validation checkpoint | Validation note |
| ASSUMP10 | Assumption invalidation | Assumption proven wrong | Replan and update affected work | Invalidation note |

## CONSENS Consensus / Alignment

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| CONSENS01 | Alignment meeting | Stakeholders need shared view | Summarize goals, scope, decisions | Alignment note |
| CONSENS02 | Written confirmation | Need durable agreement | Send brief for confirmation | Confirmation record |
| CONSENS03 | Decision log | Decisions may be revisited | Record owner, rationale, date | Decision log |
| CONSENS04 | Tradeoff alignment | Choices involve cost/scope/quality | Present tradeoff options | Tradeoff decision |
| CONSENS05 | Conflict resolution | Stakeholders disagree | Escalate to decision owner | Conflict record |
| CONSENS06 | Approval alignment | Approval criteria unclear | Confirm approver and gate | Approval alignment |
| CONSENS07 | Expectation alignment | User expects more/different output | Clarify deliverable and limits | Expectation note |
| CONSENS08 | Handoff alignment | Receiver needs to continue work | Confirm handoff package | Handoff alignment |
| CONSENS09 | Change alignment | Requirements changed midstream | Record impact and re-baseline | Change alignment |
| CONSENS10 | Final alignment | Ready to execute/deliver | Confirm no blocking disagreement | Alignment signoff |

## REQTRACE Requirement Traceability

| Code | Discovery need | Workflow action | Control | Evidence |
|---|---|---|---|---|
| REQTRACE01 | Requirement ID | Requirement needs stable reference | Assign ID or row number | Requirement ID |
| REQTRACE02 | Source trace | Requirement comes from source/user | Link requirement to origin | Source trace |
| REQTRACE03 | Owner trace | Requirement has accountable owner | Record owner/approver | Owner trace |
| REQTRACE04 | Acceptance trace | Requirement maps to test/evidence | Link to acceptance criterion | Acceptance trace |
| REQTRACE05 | Artifact trace | Requirement maps to output section/file | Link to deliverable location | Artifact trace |
| REQTRACE06 | Change trace | Requirement changed | Record diff, reason, approver | Change trace |
| REQTRACE07 | Dependency trace | Requirement depends on other item | Link dependencies | Dependency trace |
| REQTRACE08 | Risk trace | Requirement has risk/compliance impact | Link risk/control | Risk trace |
| REQTRACE09 | Status trace | Requirement state must be visible | Track proposed/approved/done/deferred | Status trace |
| REQTRACE10 | Trace audit | Need prove no requirement lost | Review trace matrix completeness | Trace audit |
