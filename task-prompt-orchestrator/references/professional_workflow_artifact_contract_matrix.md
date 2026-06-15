# Professional Workflow Artifact Contract Matrix

Use this when a workflow needs explicit intermediate artifacts, handoff packets, evidence bundles, logs, or acceptance packages. Artifact contracts make a workflow inspectable, repeatable, and easier to resume.

Selection rule:

1. Identify the workflow phase that needs a concrete artifact.
2. Select one or more artifact contract codes.
3. Add the artifact's required fields to the prompt packet.
4. Verify the artifact exists before moving to the next workflow step.

## BRFC Brief / Intake Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| BRFC01 | Goal brief | Goal, audience, output, constraints, deadline | Request is broad or ambiguous | Goal and output are testable |
| BRFC02 | Scope boundary brief | In scope, out of scope, assumptions, risks | Scope creep is likely | Boundaries explicit |
| BRFC03 | Stakeholder brief | Requester, approver, users, reviewers, owners | Multiple people depend on output | Roles named |
| BRFC04 | Success criteria brief | Acceptance criteria, quality bar, failure cases | Delivery must be evaluated | Criteria observable |
| BRFC05 | Context brief | Background, source material, prior decisions, open questions | Context is fragmented | Key context preserved |
| BRFC06 | Constraint brief | Time, budget, tools, format, policy limits | Execution options are constrained | Constraints actionable |
| BRFC07 | Risk brief | Known risks, severity, mitigations, stop points | Work has legal, financial, safety, or reputation impact | Stop points named |
| BRFC08 | Data handling brief | Data source, sensitivity, retention, redaction | Inputs may contain private or regulated data | Sensitive fields handled |
| BRFC09 | Output-spec brief | Format, length, structure, file type, channel | Final deliverable shape matters | Output spec complete |
| BRFC10 | Reusable prompt brief | Variables, defaults, examples, tests | The workflow becomes a template | Variables reusable |

## ARTSRC Source / Evidence Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| ARTSRC01 | Source inventory | Source name, path/link, date, relevance, status | Research or file-based work starts | Every source listed |
| ARTSRC02 | Evidence table | Claim, evidence, source, confidence, caveat | Claims need backing | Claims traceable |
| ARTSRC03 | Citation ledger | Citation, quote/paraphrase note, usage location | Formal writing or research | Citations close |
| ARTSRC04 | Data provenance note | Origin, owner, transforms, freshness, caveats | Data is analyzed or transformed | Lineage visible |
| ARTSRC05 | Visual reference sheet | Image/file, visible facts, style traits, invariants | Image2 or design work uses references | Facts separated from interpretation |
| ARTSRC06 | Requirements source map | Requirement, source, priority, acceptance link | Specs, RFPs, or product requirements | No orphan requirement |
| ARTSRC07 | Web research log | Query, source, date, selection rule, exclusion rule | Current or internet-backed claims matter | Search reproducible |
| ARTSRC08 | File inspection log | File path, purpose, read result, decision | Code/doc/file workflows need auditability | Paths exact |
| ARTSRC09 | Assumption ledger | Assumption, reason, risk, validation path | Missing inputs cannot block progress | Assumptions disclosed |
| ARTSRC10 | Conflict map | Conflicting sources, difference, resolution, owner | Sources disagree | Conflict resolved or escalated |

## WBS Work Breakdown Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| WBS01 | Task breakdown | Steps, dependencies, owner, output per step | Work spans multiple actions | Steps executable |
| WBS02 | Phase plan | Phase, objective, entry criteria, exit criteria | Work needs staged delivery | Gates defined |
| WBS03 | Dependency map | Upstream, downstream, blockers, order | Parallel or complex work | Critical dependencies visible |
| WBS04 | Tool plan | Tool, purpose, input, output, fallback | Tools or scripts are required | Tool path chosen |
| WBS05 | Parallelization plan | Independent lanes, merge point, conflict checks | Work can run concurrently | Merge rule explicit |
| WBS06 | Batch manifest | Item list, operation, output naming, failure handling | Bulk processing is needed | All items accounted |
| WBS07 | Decision tree | Condition, branch, action, fallback | Workflow has branches | Branches exhaustive enough |
| WBS08 | Review schedule | Reviewer, artifact, criteria, timing | Human review is required | Reviewer and artifact named |
| WBS09 | Milestone map | Milestone, deliverable, date, acceptance | Delivery spans time | Milestones measurable |
| WBS10 | Resume plan | Current state, completed, pending, next action | Work may pause or transfer | Next action unambiguous |

## DECC Decision / Rationale Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| DECC01 | Decision log | Decision, options, criteria, reason, owner | Choices affect outcome | Rationale recorded |
| DECC02 | Tradeoff table | Option, benefit, cost, risk, recommendation | Multiple viable paths exist | Tradeoffs comparable |
| DECC03 | Prioritization matrix | Items, criteria, weights, score, order | Backlogs or ideas need ranking | Criteria stated |
| DECC04 | Recommendation memo | Context, options, recommendation, risks, next steps | User needs a decision | Recommendation actionable |
| DECC05 | Exception decision | Rule, exception, justification, approval | Normal process is bypassed | Approval or risk noted |
| DECC06 | Design rationale | Design choice, alternatives, constraints, evidence | Design/CAD/product decisions matter | Choice justified |
| DECC07 | Technical rationale | Approach, constraints, failure modes, tests | Engineering work is nontrivial | Tests mapped |
| DECC08 | Policy rationale | Requirement, interpretation, uncertainty, reviewer | Governance or compliance decisions matter | Uncertainty visible |
| DECC09 | Model/prompt rationale | Prompt choice, variables, expected behavior, tests | Prompt architecture matters | Behavior testable |
| DECC10 | Closeout rationale | What changed, why accepted, residual risks | Work is finished with caveats | Residual risks disclosed |

## PKTC Prompt Packet Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| PKTC01 | Single-step prompt packet | Role, task, inputs, output schema, checks | One task needs a strong prompt | Prompt executable |
| PKTC02 | Multi-step prompt packet | Step, prompt, input, output, dependency | Workflow has chained prompts | Dependencies valid |
| PKTC03 | Image2 prompt packet | Source invariants, target changes, style, negatives, output specs | Image editing/generation | Invariants protected |
| PKTC04 | Research prompt packet | Question, sources, inclusion rule, citation format | Research or sourcing is needed | Source rule explicit |
| PKTC05 | Coding prompt packet | Repo context, files, change goal, tests, constraints | Code changes are requested | Tests named |
| PKTC06 | Review prompt packet | Artifact, criteria, severity, evidence, output format | Audit or critique is requested | Findings evidence-based |
| PKTC07 | Data prompt packet | Dataset, grain, metrics, filters, validation | Data work is requested | Metric logic explicit |
| PKTC08 | Creative prompt packet | Brief, audience, style, variants, selection criteria | Creative routes are generated | Criteria included |
| PKTC09 | Compliance prompt packet | Rule, jurisdiction, evidence, caveat, escalation | Regulated claims or advice appear | Escalation rule present |
| PKTC10 | Reusable template packet | Variables, defaults, examples, checks, failure modes | Prompt should be reused | Variables complete |

## RUNC Runbook / Execution Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| RUNC01 | Manual runbook | Steps, commands/actions, inputs, expected result | Human operator executes | Steps runnable |
| RUNC02 | Automated runbook | Script/tool, parameters, preconditions, outputs | Automation is available | Parameters defined |
| RUNC03 | Deployment runbook | Build, deploy, verify, rollback, owners | Release or publishing occurs | Rollback included |
| RUNC04 | Data runbook | Extract, transform, validate, load, reconcile | Data pipeline work occurs | Reconciliation included |
| RUNC05 | Content production runbook | Draft, edit, approve, publish, archive | Content moves to production | Approval step included |
| RUNC06 | Design production runbook | Assets, specs, variants, export, QA | Design/image2/CAD delivery occurs | Export specs verified |
| RUNC07 | Incident runbook | Triage, stabilize, communicate, restore, postmortem | Incident or failure occurs | Stabilization path clear |
| RUNC08 | Batch runbook | Item intake, processing, naming, QA, exception handling | Bulk work repeats | Exceptions handled |
| RUNC09 | Review runbook | Reviewer role, artifact, checklist, decision | Review needs consistency | Decision states defined |
| RUNC10 | Maintenance runbook | Schedule, checks, owners, thresholds, update path | Ongoing operation exists | Thresholds measurable |

## LOGC Logging / Trace Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| LOGC01 | Action log | Action, time, actor/tool, result, next step | Work needs traceability | Actions sequenced |
| LOGC02 | Change log | File/artifact, change, reason, verification | Artifacts are modified | Verification linked |
| LOGC03 | Command log | Command, path, output summary, exit result | Local execution matters | Result captured |
| LOGC04 | Prompt run log | Prompt version, input, output, evaluation | Prompt workflows iterate | Version linked |
| LOGC05 | Tool call log | Tool, input, result, limitation | External tools are used | Limitation noted |
| LOGC06 | Error log | Error, cause, attempted fix, status | Failures happen | Status clear |
| LOGC07 | Approval log | Artifact, approver, date, decision, notes | Approvals are required | Decision recorded |
| LOGC08 | Data quality log | Check, result, exception, fix, owner | Data quality matters | Exceptions owned |
| LOGC09 | Source update log | Source, old/new status, date, impact | Sources may change | Impact assessed |
| LOGC10 | Audit trail | Evidence, decisions, owners, timestamps | High-risk or regulated work | Trail complete enough |

## QAC QA / Verification Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| QAC01 | QA checklist | Criteria, method, pass/fail, evidence | Any deliverable needs review | All criteria checked |
| QAC02 | Acceptance test pack | Test, input, expected output, actual output | Output must meet specs | Tests pass or fail noted |
| QAC03 | Rubric scorecard | Dimension, score, evidence, improvement | Quality is subjective | Scores justified |
| QAC04 | Regression check | Prior behavior, new behavior, risk, test | Changes may break existing work | Regression risk tested |
| QAC05 | Visual QA sheet | Layout, text, alignment, brand, artifacts | Image/design/UI work is delivered | Visible issues checked |
| QAC06 | Data validation pack | Schema, totals, samples, anomalies, reconciliation | Data outputs are delivered | Totals reconcile |
| QAC07 | Citation QA pack | Claim, citation, page/link, quote/paraphrase | Research writing is delivered | Unsupported claims flagged |
| QAC08 | Compliance QA pack | Rule, evidence, decision, reviewer, caveat | Regulated output is delivered | Noncompliance resolved |
| QAC09 | Usability QA pack | User task, friction, outcome, recommendation | Product/workflow usability matters | Task outcome captured |
| QAC10 | Final readiness check | Required artifacts, blockers, risks, handoff | Delivery is about to close | No hidden blockers |

## RISKC Risk / Control Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| RISKC01 | Risk register | Risk, likelihood, impact, mitigation, owner | Work has meaningful uncertainty | Owners assigned |
| RISKC02 | Control map | Risk, control, evidence, frequency, owner | Governance controls matter | Evidence named |
| RISKC03 | Privacy impact note | Data, purpose, minimization, access, retention | Personal data is involved | Data minimized |
| RISKC04 | Security review note | Asset, threat, control, residual risk | Systems, code, or secrets involved | Critical risk addressed |
| RISKC05 | Legal caveat note | Jurisdiction, rule, caveat, escalation | Legal/regulatory exposure exists | Caveat and escalation present |
| RISKC06 | Financial assumption note | Assumption, source, sensitivity, owner | Financial output is created | Assumptions visible |
| RISKC07 | Safety stop card | Hazard, stop condition, escalation, safe alternative | Physical or user safety matters | Stop condition explicit |
| RISKC08 | Brand/reputation risk note | Claim, audience, evidence, approval, risk | Public-facing output exists | Claims supported |
| RISKC09 | IP rights note | Asset/source, license, usage, restriction | External assets or IP appear | Usage allowed or flagged |
| RISKC10 | Residual risk closeout | Remaining risk, reason accepted, owner, follow-up | Work closes with known risks | Acceptance explicit |

## HAND Handoff / Transfer Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| HAND01 | User handoff | What changed, how to use, limitations, next steps | User receives a deliverable | Next steps clear |
| HAND02 | Developer handoff | Files, changes, tests, risks, TODOs | Engineering work transfers | Files and tests named |
| HAND03 | Designer handoff | Assets, specs, variants, constraints, export notes | Design work transfers | Specs complete |
| HAND04 | Operations handoff | Runbook, owners, thresholds, escalation | Ops team takes over | Escalation path clear |
| HAND05 | Research handoff | Question, sources, findings, gaps, citations | Research transfers | Gaps visible |
| HAND06 | Compliance handoff | Evidence, decisions, approvals, caveats | Compliance review follows | Reviewer can audit |
| HAND07 | Sales/client handoff | Client context, deliverable, talking points, risks | Client-facing team follows up | Message ready |
| HAND08 | Training handoff | Learning objective, materials, exercises, checks | Teaching or onboarding follows | Practice included |
| HAND09 | Maintenance handoff | Current state, schedule, monitoring, update path | Ongoing upkeep follows | Owner named |
| HAND10 | Resume handoff | Completed, pending, blockers, next command/action | Agent or thread resumes later | Resume action precise |

## ARCC Archive / Reuse Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| ARCC01 | Final archive package | Final artifact, sources, logs, decisions, checks | Work should be preserved | Package complete |
| ARCC02 | Template extraction note | Reusable pattern, variables, examples, limits | Workflow should become reusable | Template variables clear |
| ARCC03 | Lessons learned note | What worked, what failed, improvement, next trial | Workflow should improve | Lesson actionable |
| ARCC04 | Version snapshot | Version, date, artifacts, change summary | Outputs evolve over time | Snapshot identifiable |
| ARCC05 | Knowledge base entry | Problem, solution, steps, evidence, tags | Reuse by future users matters | Search terms included |
| ARCC06 | Prompt library entry | Use case, prompt, variables, tests, category | Prompt should join library | Category and tests present |
| ARCC07 | Dataset/archive manifest | Files, purpose, provenance, checksum/status | Data or files are archived | Inventory complete |
| ARCC08 | Design system entry | Component/asset, usage, variants, rules | Design output becomes standard | Usage rules clear |
| ARCC09 | Runbook update note | Changed step, reason, validation, owner | Procedure changes after execution | Updated step named |
| ARCC10 | Retention/disposal note | Keep/delete, reason, date, owner, recovery path | Cleanup or compliance retention matters | Recovery path clear |

## ACCC Acceptance / Closeout Contracts

| Code | Artifact | Required fields | Best used when | Completion check |
|---|---|---|---|---|
| ACCC01 | Delivery summary | Deliverables, changes, checks, location | Work is delivered | User can find output |
| ACCC02 | Acceptance record | Criteria, result, evidence, approver | Formal acceptance is needed | Approval captured |
| ACCC03 | Open issue list | Issue, severity, owner, next step | Work closes with remaining items | Issues owned |
| ACCC04 | Residual risk statement | Risk, impact, mitigation, acceptance | Output has caveats | Risks explicit |
| ACCC05 | Verification summary | Checks run, results, failures, skipped checks | User needs confidence | Skips disclosed |
| ACCC06 | Change summary | What changed, why, files/artifacts, tests | Code/content/design changed | Changes traceable |
| ACCC07 | User instruction note | How to run/use/review, limits, next action | User must operate output | Instructions actionable |
| ACCC08 | Signoff packet | Deliverable, evidence, approver, date, notes | Approval workflow closes | Signoff present |
| ACCC09 | Post-delivery monitor | Metric, threshold, owner, review date | Outcome must be watched | Monitoring defined |
| ACCC10 | Final closeout | Done, not done, evidence, risks, follow-up | Workflow ends | Closure honest |
