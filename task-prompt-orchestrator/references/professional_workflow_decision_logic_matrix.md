# Professional Workflow Decision Logic Matrix

Use this when a workflow needs explicit decision criteria, routing logic, prioritization, tradeoff analysis, thresholds, uncertainty handling, approval decisions, stop/go gates, or recommendation logic. Decision logic prevents hidden judgment from being buried inside vague workflow steps.

Selection rule:

1. Identify the decision point in the workflow.
2. Select the closest decision logic code.
3. Add decision inputs, criteria, possible outcomes, and evidence to the prompt packet.
4. Record the chosen decision and rationale before moving to the next state.

## DECTRIAGE Triage Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| DECTRIAGE01 | Request triage | Goal, domain, deliverable | Route to best workflow family | Workflow route |
| DECTRIAGE02 | Risk triage | Impact, likelihood, domain | Route low/medium/high risk | Risk tier |
| DECTRIAGE03 | Urgency triage | Deadline, dependency, impact | Route by time criticality | Urgency tier |
| DECTRIAGE04 | Source triage | Source type, quality, freshness | Route to source readiness state | Source route |
| DECTRIAGE05 | Tool triage | Needed action, tool availability | Route to tool or fallback | Tool choice |
| DECTRIAGE06 | Review triage | Artifact, impact, criteria | Decide reviewer type and depth | Review route |
| DECTRIAGE07 | Batch triage | Item type, count, variance | Decide single/batch/sample path | Batch route |
| DECTRIAGE08 | Automation triage | Frequency, repeatability, risk | Decide manual/template/automation | Automation tier |
| DECTRIAGE09 | Escalation triage | Blocker, owner, severity | Decide self-fix, ask, or escalate | Escalation route |
| DECTRIAGE10 | Closure triage | Evidence, remaining risks, scope | Decide complete, partial, blocked, or continue | Closure state |

## PRIO Prioritization Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| PRIO01 | Impact priority | Items, expected value, affected users | Rank by impact | Priority list |
| PRIO02 | Urgency priority | Items, deadlines, dependency chain | Rank by time sensitivity | Urgency order |
| PRIO03 | Risk priority | Risks, likelihood, impact | Rank by severity | Risk order |
| PRIO04 | Effort priority | Items, effort, constraints | Choose low-effort/high-value first when safe | Effort order |
| PRIO05 | Dependency priority | Upstream/downstream links | Do blockers before dependent steps | Dependency order |
| PRIO06 | Evidence priority | Claims, uncertainty, consequence | Verify high-consequence claims first | Evidence queue |
| PRIO07 | Review priority | Findings, severity, confidence | Fix blocking issues before minor issues | Review order |
| PRIO08 | Batch priority | Items, SLA, value, failure risk | Process by SLA/risk/value | Batch order |
| PRIO09 | Library priority | Gaps, reuse frequency, user demand | Expand high-reuse gaps first | Library backlog |
| PRIO10 | Optimization priority | Bottlenecks, cost, failure rate | Improve highest-friction workflow first | Optimization queue |

## TRADEOFF Tradeoff Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| TRADEOFF01 | Speed vs depth | Deadline, quality bar, risk | Pick depth that fits consequence and time | Depth choice |
| TRADEOFF02 | Automation vs control | Frequency, risk, variability | Automate stable low-risk work | Automation decision |
| TRADEOFF03 | Simplicity vs completeness | User level, scope, stakes | Keep simple unless coverage risk matters | Complexity choice |
| TRADEOFF04 | Creativity vs consistency | Brand, novelty need, production constraints | Balance variants with guardrails | Creative route |
| TRADEOFF05 | Precision vs flexibility | Schema need, downstream use | Use strict schema for machine handoff | Schema choice |
| TRADEOFF06 | Cost vs quality | Budget, expected value, failure cost | Spend more only where quality reduces real risk | Cost decision |
| TRADEOFF07 | Privacy vs usefulness | Sensitive data, purpose, output need | Minimize data while preserving utility | Data use choice |
| TRADEOFF08 | Reuse vs customization | Similarity, audience, domain | Reuse template with explicit adapters | Template choice |
| TRADEOFF09 | Human review vs autonomy | Impact, confidence, reversibility | Add HITL for high-impact/low-confidence steps | Review choice |
| TRADEOFF10 | Local evidence vs web evidence | Freshness need, source availability | Browse when current facts matter | Evidence choice |

## THRESH Threshold Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| THRESH01 | Quality threshold | Score/checklist/result | Pass only when minimum criteria met | Pass/fail |
| THRESH02 | Confidence threshold | Evidence strength, uncertainty | Escalate or caveat below threshold | Confidence status |
| THRESH03 | Risk threshold | Risk tier and severity | Require gate above threshold | Risk action |
| THRESH04 | Volume threshold | Item count and variance | Batch when count exceeds threshold | Batch decision |
| THRESH05 | Freshness threshold | Source date, volatility | Refresh when stale by rule | Freshness action |
| THRESH06 | Cost threshold | Cost estimate and budget | Require approval above threshold | Cost gate |
| THRESH07 | Time threshold | SLA/deadline remaining | Degrade/escalate when time below threshold | Time action |
| THRESH08 | Error threshold | Error count/rate | Trigger recovery above threshold | Recovery trigger |
| THRESH09 | Coverage threshold | Covered categories vs required scope | Continue expansion until threshold met | Coverage decision |
| THRESH10 | Automation threshold | Frequency and repeatability | Automate when repeated enough | Automation trigger |

## UNC Uncertainty Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| UNC01 | Assumption decision | Missing detail, impact | Assume only if low-risk and disclosed | Assumption note |
| UNC02 | Clarification decision | Missing answer, materiality | Ask when output would materially change | Clarification ask |
| UNC03 | Caveat decision | Evidence gap, consequence | Add caveat when useful answer still possible | Caveated output |
| UNC04 | Escalation decision | Unknown high-impact effect | Escalate to owner/SME | Escalation packet |
| UNC05 | Research decision | Uncertain fact, freshness risk | Search authoritative sources | Research route |
| UNC06 | Experiment decision | Unknown best approach | Run bounded experiment/spike | Experiment plan |
| UNC07 | Deferral decision | Current decision premature | Defer until prerequisite evidence exists | Deferral note |
| UNC08 | Sensitivity decision | Result depends on assumption | Show sensitivity or scenarios | Sensitivity note |
| UNC09 | Confidence label decision | Evidence mixed or limited | Mark high/medium/low confidence | Confidence label |
| UNC10 | Stop decision | Uncertainty makes action unsafe | Stop unsafe path and propose safe alternative | Stop note |

## RISKD Risk Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| RISKD01 | Accept risk | Risk, owner, mitigation | Accept only with explicit owner and caveat | Risk acceptance |
| RISKD02 | Mitigate risk | Risk and control options | Add control that reduces likely failure | Mitigation plan |
| RISKD03 | Transfer risk | External owner/vendor/approver | Transfer only with documented acceptance | Transfer note |
| RISKD04 | Avoid risk | Unsafe or unacceptable consequence | Change path to remove risk | Avoidance decision |
| RISKD05 | Monitor risk | Risk not immediate but possible | Add metric/trigger/owner | Risk monitor |
| RISKD06 | Escalate risk | Risk exceeds authority/confidence | Route to reviewer/approver | Risk escalation |
| RISKD07 | Gate risk | Risk requires approval before release | Insert approval gate | Risk gate |
| RISKD08 | Segment risk | Some steps/items higher risk than others | Apply different controls by tier | Risk segmentation |
| RISKD09 | Residual risk decision | Risk remains after mitigation | Decide disclose/continue/stop | Residual risk note |
| RISKD10 | Reassess risk | Context/source changes | Re-run risk triage | Risk update |

## APPD Approval Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| APPD01 | Approve | Artifact, criteria, evidence | Approve when criteria pass | Approval record |
| APPD02 | Reject | Artifact, failed criteria | Reject with concrete reasons | Rejection note |
| APPD03 | Conditional approve | Minor gaps with conditions | Approve only with conditions listed | Conditional signoff |
| APPD04 | Request revision | Fixable quality/fit issue | Send precise rework instructions | Revision request |
| APPD05 | Request evidence | Claims or tests insufficient | Ask for missing proof | Evidence request |
| APPD06 | Escalate approval | Approver lacks authority or domain | Route to higher/specialist approver | Approval escalation |
| APPD07 | Defer approval | Dependencies not ready | Hold until prerequisite complete | Deferral decision |
| APPD08 | Override approval path | Emergency/exception context | Require exception rationale | Override record |
| APPD09 | Revoke approval | New evidence invalidates signoff | Record change and notify | Revocation note |
| APPD10 | Archive approval | Final artifact accepted for storage/reuse | Move to archive/index | Archive decision |

## ROUTE Routing Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| ROUTE01 | Domain route | Topic, task, deliverable | Select domain matrix/workflow | Domain route |
| ROUTE02 | Operation route | Verb/action intent | Select task operation code | Operation route |
| ROUTE03 | Input route | Source material type | Select input-material code | Input route |
| ROUTE04 | Output route | Deliverable/media form | Select media/deliverable code | Output route |
| ROUTE05 | Audience route | Reader/user/reviewer | Select audience/context code | Audience route |
| ROUTE06 | Constraint route | Urgency, platform, format, budget | Select constraint/context code | Constraint route |
| ROUTE07 | Verification route | QA/acceptance need | Select verification code | QA route |
| ROUTE08 | Risk route | High-impact domain | Select high-risk validation code | Risk route |
| ROUTE09 | Workflow dimension route | Need for trigger/state/role/IO/etc. | Select workflow dimension matrix | Dimension route |
| ROUTE10 | Fallback route | Primary route blocked | Select degraded/recovery route | Fallback route |

## EXPR Experiment Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| EXPR01 | Run spike | Unknown approach with bounded time | Timebox exploration | Spike result |
| EXPR02 | A/B compare | Two viable outputs/routes | Compare against criteria | Comparison result |
| EXPR03 | Prototype first | Requirements uncertain | Build small testable artifact | Prototype decision |
| EXPR04 | Sample before batch | Large batch with unknown quality | Run sample and QA before full batch | Sample result |
| EXPR05 | Pilot before rollout | Workflow affects many users/items | Test with limited group | Pilot report |
| EXPR06 | Benchmark prompt | Prompt quality uncertain | Run representative cases | Benchmark result |
| EXPR07 | Evaluate tool | Tool fit uncertain | Test tool on small input | Tool eval |
| EXPR08 | Sensitivity test | Output depends on parameter | Test parameter variants | Sensitivity result |
| EXPR09 | Stop experiment | Experiment fails criteria or timebox | Record result and choose fallback | Stop note |
| EXPR10 | Scale experiment | Pilot passes criteria | Move to broader execution | Scale decision |

## GOST Stop / Go Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| GOST01 | Go to execution | Brief, sources, plan ready | Proceed when entry criteria met | Go decision |
| GOST02 | Stop for clarification | Missing detail blocks correctness/safety | Ask or hold | Stop ask |
| GOST03 | Stop for risk | Risk exceeds allowed path | Escalate or safe alternative | Risk stop |
| GOST04 | Stop for source | Required evidence missing | Gather source or caveat | Source stop |
| GOST05 | Stop for QA failure | Checks fail | Rework before delivery | QA stop |
| GOST06 | Go with caveat | Useful output possible with limitation | Deliver with explicit caveat | Caveated go |
| GOST07 | Go degraded | Ideal path unavailable but partial value exists | Deliver reduced scope and next step | Degraded go |
| GOST08 | Stop automation | Automation unsafe or brittle | Switch to manual/HITL | Automation stop |
| GOST09 | Go to release | Approval, QA, rollback, monitor ready | Release/publish/deploy | Release go |
| GOST10 | Stop at closeout | Objective not proven complete | Continue or partial close | Closeout stop |

## EXCD Exception Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| EXCD01 | Exception classify | Deviation, failure, or blocker | Classify as blocked/error/risk/change | Exception class |
| EXCD02 | Exception owner | Exception and impacted artifact | Assign owner by impact/domain | Owner assignment |
| EXCD03 | Exception severity | Impact, urgency, reversibility | Tier severity | Severity tier |
| EXCD04 | Exception workaround | Primary path unavailable | Choose safe temporary path | Workaround note |
| EXCD05 | Exception rollback | Bad change or output | Restore prior valid state | Rollback decision |
| EXCD06 | Exception rework | Output rejected or failed | Choose rework path | Rework plan |
| EXCD07 | Exception escalation | Exception beyond authority | Route to approver/SME | Escalation packet |
| EXCD08 | Exception accept | Minor known issue acceptable | Record residual risk | Exception acceptance |
| EXCD09 | Exception monitor | Issue not fixed immediately | Add watch metric/owner | Monitor note |
| EXCD10 | Exception close | Issue resolved or accepted | Record evidence and lesson | Exception closeout |

## RECD Recommendation Decisions

| Code | Decision type | Inputs | Decision rule | Output |
|---|---|---|---|---|
| RECD01 | Single recommendation | Options, criteria, evidence | Pick best option and explain why | Recommendation |
| RECD02 | Ranked recommendation | Multiple viable options | Rank by weighted criteria | Ranked list |
| RECD03 | Conditional recommendation | Recommendation depends on assumptions | State if/then paths | Conditional memo |
| RECD04 | No recommendation | Evidence insufficient or decision unsafe | Explain gap and needed evidence | No-go memo |
| RECD05 | Conservative recommendation | High stakes or uncertainty | Choose lower-risk option | Conservative choice |
| RECD06 | Exploratory recommendation | Need discovery before commitment | Recommend experiment/spike | Exploration plan |
| RECD07 | Cost-aware recommendation | Budget/resource tradeoffs matter | Recommend value-efficient route | Cost-aware memo |
| RECD08 | User-fit recommendation | Skill level/audience matters | Recommend usable next action | User-fit path |
| RECD09 | Production recommendation | Release/operations constraints matter | Recommend production-ready path | Production memo |
| RECD10 | Reuse recommendation | Workflow likely repeats | Recommend template/index/automation | Reuse proposal |


