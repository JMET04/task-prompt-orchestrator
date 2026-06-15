# Professional Workflow Communication and Reporting Matrix

Use this when a workflow needs explicit status updates, stakeholder communication, decision messages, risk reporting, approval requests, handoff messages, incident updates, client communication, training notes, retrospectives, change notices, or archive announcements. Communication rules make workflow state visible and actionable.

Selection rule:

1. Identify who needs to know what, when, and why.
2. Select the closest communication/reporting code.
3. Add audience, message purpose, required content, and timing to the prompt packet.
4. Do not overclaim completion; communicate evidence, limits, next action, and owner.

## STAT Status Reporting

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| STAT01 | Quick progress update | User/requester | Done, doing, next | During active work |
| STAT02 | Milestone update | Stakeholders | Milestone reached, evidence, next gate | At phase boundary |
| STAT03 | Daily status | Team/operator | Completed, planned, blockers | Daily cadence |
| STAT04 | Weekly status | Team/executive | Progress, risks, decisions, asks | Weekly cadence |
| STAT05 | Batch status | Operator/reviewer | Processed, failed, pending, sample QA | During/after batch |
| STAT06 | Automation status | Owner/operator | Last run, errors, next run, alerts | After scheduled run |
| STAT07 | Research status | Writer/decision owner | Sources checked, gaps, confidence | During research |
| STAT08 | Build/test status | Developer/reviewer | Commands/tests, pass/fail, failures | After validation |
| STAT09 | Coverage status | Library owner | Current count, added gaps, remaining areas | After expansion |
| STAT10 | Closeout status | User/stakeholder | Final outcome, checks, risks, next action | At delivery |

## BLOCK Blocker Communication

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| BLOCK01 | Missing input ask | User/source owner | Needed input, why, smallest answer | When blocker appears |
| BLOCK02 | Missing source notice | User/source owner | Missing source, impact, fallback options | Source readiness failure |
| BLOCK03 | Permission blocker | User/approver/admin | Action needing permission, risk, alternative | Before restricted action |
| BLOCK04 | Tool blocker | User/operator | Tool failure, attempted fixes, fallback | Tool unavailable |
| BLOCK05 | Dependency blocker | Downstream/upstream owner | Dependency, owner, due date, impact | Dependency delay |
| BLOCK06 | Review blocker | Reviewer/owner | Review needed, artifact, criteria, deadline | Review queue |
| BLOCK07 | Approval blocker | Approver/requester | Approval needed, options, consequence | Before gate |
| BLOCK08 | Evidence blocker | Decision owner | Unsupported claim/action, needed evidence | Before recommendation |
| BLOCK09 | Safety blocker | User/owner | Unsafe part, reason, safe alternative | Safety boundary |
| BLOCK10 | Repeated blocker | Goal owner | Attempts, repeated condition, needed external change | Repeated impasse |

## RISKCOM Risk Communication

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| RISKCOM01 | Risk alert | Owner/stakeholder | Risk, impact, likelihood, mitigation | Risk identified |
| RISKCOM02 | Residual risk note | User/approver | Remaining risk, owner, acceptance | Closeout or approval |
| RISKCOM03 | Privacy risk notice | Data owner/compliance | Data involved, exposure, control | Sensitive data use |
| RISKCOM04 | Security risk notice | Security/technical owner | Asset, threat, control, urgency | Security concern |
| RISKCOM05 | Legal/compliance caveat | User/compliance | Rule/jurisdiction, uncertainty, escalation | Regulated output |
| RISKCOM06 | Financial risk note | Business/finance owner | Assumption, exposure, sensitivity | Financial decision |
| RISKCOM07 | Reputation risk note | Brand/comms owner | Claim, audience, evidence, approval need | Public content |
| RISKCOM08 | Safety risk notice | Safety owner/user | Hazard, stop condition, safe path | Physical/user safety |
| RISKCOM09 | IP/licensing notice | Legal/content owner | Asset, rights status, allowed use | External assets |
| RISKCOM10 | Risk escalation | Escalation owner | Severity, evidence, ask, deadline | Risk above threshold |

## DECCOM Decision Communication

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| DECCOM01 | Decision summary | Stakeholders | Decision, reason, alternatives, owner | After decision |
| DECCOM02 | Recommendation memo | Decision owner | Options, criteria, recommendation, risk | Before decision |
| DECCOM03 | Tradeoff explanation | User/stakeholder | Tradeoffs, chosen balance, caveats | When options compete |
| DECCOM04 | Prioritization note | Team/owner | Ranked items, criteria, next action | Backlog/batch planning |
| DECCOM05 | Go/no-go message | Release/approval team | Criteria, result, blockers, decision | Gate decision |
| DECCOM06 | Exception decision note | Owner/auditor | Exception, rationale, approval, risk | Exception path |
| DECCOM07 | Reversal notice | Affected stakeholders | Prior decision, new evidence, change | Decision reversed |
| DECCOM08 | Deferral notice | Requester/owner | Decision deferred, reason, needed input | Evidence not ready |
| DECCOM09 | Conditional decision | Receiver/owner | Conditions, owner, due date, risk | Conditional approval |
| DECCOM10 | Decision archive note | Future users/auditors | Decision, date, evidence, location | Archive/closeout |

## APRCOM Approval Communication

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| APRCOM01 | Approval request | Approver | Artifact, criteria, evidence, options | Before gated action |
| APRCOM02 | Review request | Reviewer | Artifact, checklist, severity scale, deadline | Before review |
| APRCOM03 | Compliance request | Compliance/legal | Regulated issue, evidence, question, caveat | Compliance gate |
| APRCOM04 | Security request | Security owner | Threat/access/secret issue, context, ask | Security gate |
| APRCOM05 | Budget request | Budget owner | Cost, benefit, alternative, threshold | Budget gate |
| APRCOM06 | Launch approval request | Launch owner | Readiness, rollback, monitor, risks | Pre-launch |
| APRCOM07 | Exception approval request | Exception approver | Deviation, reason, risk, duration | Exception needed |
| APRCOM08 | Conditional approval follow-up | Owner/approver | Conditions, progress, evidence | Conditions pending |
| APRCOM09 | Rejection response | Requester/executor | Failed criteria, revision path, owner | Approval rejected |
| APRCOM10 | Signoff record | Owner/auditor | Approver, artifact, date, conditions | After approval |

## HANDCOM Handoff Communication

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| HANDCOM01 | User handoff | User/requester | What changed, how to use, limits, next step | Delivery |
| HANDCOM02 | Developer handoff | Developer/maintainer | Files, changes, tests, risks, TODOs | Technical transfer |
| HANDCOM03 | Designer handoff | Designer/producer | Assets, specs, variants, constraints | Design transfer |
| HANDCOM04 | Ops handoff | Operator/support | Runbook, thresholds, owners, escalation | Operational transfer |
| HANDCOM05 | Research handoff | Writer/decision owner | Findings, sources, gaps, confidence | Research transfer |
| HANDCOM06 | Review handoff | Reviewer | Artifact, criteria, context, decision ask | Review transfer |
| HANDCOM07 | Agent handoff | Next agent/thread | Objective, state, evidence, next action | Continuation |
| HANDCOM08 | Client handoff | Client-facing owner | Deliverable, caveats, talking points, asks | External delivery |
| HANDCOM09 | Archive handoff | Librarian/future user | Location, version, tags, retrieval path | Archive |
| HANDCOM10 | Resume handoff | Future self/agent | Completed, pending, blockers, next command/action | Pause/compaction |

## INCCOM Incident / Exception Communication

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| INCCOM01 | Incident acknowledgement | Affected stakeholders | What happened, known impact, next update | Incident start |
| INCCOM02 | Stabilization update | Owner/users | Current status, mitigation, remaining issue | During incident |
| INCCOM03 | Recovery update | Stakeholders | Restored state, verification, caveats | After recovery |
| INCCOM04 | Postmortem summary | Team/owner | Cause, impact, timeline, prevention | After incident |
| INCCOM05 | Error report | Technical owner | Error, command/tool, logs, attempted fixes | Execution failure |
| INCCOM06 | Validation failure report | User/reviewer | Failed checks, affected output, fix path | QA failure |
| INCCOM07 | Rollback notice | Stakeholders | Rolled back change, reason, verification | Rollback |
| INCCOM08 | Degraded-mode notice | User/owner | Reduced output, limits, path to full result | Fallback delivery |
| INCCOM09 | Exception queue update | Operator/owner | Failed items, owners, next retry | Batch/automation exception |
| INCCOM10 | Closure with risk | User/approver | What is closed, residual risk, follow-up | Risk closeout |

## CLIENT Client / External Communication

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| CLIENT01 | Client brief | Client/stakeholder | Goal, scope, timeline, needed input | Project start |
| CLIENT02 | Client status | Client/stakeholder | Progress, blockers, decisions, next step | Agreed cadence |
| CLIENT03 | Client question | Client/stakeholder | Specific ask, context, deadline | Missing input |
| CLIENT04 | Client deliverable note | Client/stakeholder | Deliverable, value, how to review | Delivery |
| CLIENT05 | Client approval ask | Client approver | Criteria, options, recommendation | Approval gate |
| CLIENT06 | Client risk note | Client/stakeholder | Risk, impact, mitigation, decision ask | Material risk |
| CLIENT07 | Client change request response | Client/stakeholder | Impact, cost/time, recommendation | Change request |
| CLIENT08 | Client issue response | Client/stakeholder | Acknowledgement, cause if known, action | Complaint/issue |
| CLIENT09 | Client renewal/follow-up | Client/stakeholder | Outcome, next opportunity, owner | Post-delivery |
| CLIENT10 | Client archive/receipt | Client/stakeholder | Final files, version, access path | Project close |

## TRAIN Training / Enablement Communication

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| TRAIN01 | Quick-start guide | Beginner/user | First action, inputs, expected output | First use |
| TRAIN02 | Runbook explanation | Operator | Steps, checks, failure handling | Before operation |
| TRAIN03 | Reviewer guidance | Reviewer | Criteria, severity, examples | Before review |
| TRAIN04 | Approver guidance | Approver | What to check, decision options | Before approval |
| TRAIN05 | Template usage guide | Reuser | Variables, examples, failure cases | Template release |
| TRAIN06 | Tool usage note | Executor | Tool, parameters, output, fallback | Tool handoff |
| TRAIN07 | QA training note | QA/reviewer | Checklist, evidence, pass/fail rule | QA rollout |
| TRAIN08 | Workflow onboarding | New team/agent | Workflow map, roles, artifacts | Team onboarding |
| TRAIN09 | Troubleshooting guide | Operator/support | Symptoms, causes, fixes, escalation | Recurring failures |
| TRAIN10 | Learning recap | User/team | What changed, why, reusable lesson | After iteration |

## RETRO Retrospective / Learning Communication

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| RETRO01 | Lessons learned | Team/future users | What worked, failed, changed | After workflow run |
| RETRO02 | Failure lesson | Workflow owner | Failure mode, cause, prevention | After recovery |
| RETRO03 | Quality trend report | QA/workflow owner | Findings, patterns, improvement | Periodic QA |
| RETRO04 | Rework analysis | Owner/team | Rework causes, cost, prevention | Repeated rework |
| RETRO05 | Automation candidate note | Workflow owner | Repeated manual step, ROI, risk | After repeated runs |
| RETRO06 | Template improvement note | Library owner | Template gap, update, tests | After reuse |
| RETRO07 | Source gap note | Research owner | Missing/weak sources, future rule | After research |
| RETRO08 | Handoff friction note | Process owner | Questions/confusion, fix | After handoff |
| RETRO09 | User feedback synthesis | Product/process owner | Themes, evidence, actions | Feedback cycle |
| RETRO10 | Maturity progress report | Workflow owner | Current maturity, upgrade, metric | Optimization cycle |

## CHGCOM Change Communication

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| CHGCOM01 | Scope change notice | Stakeholders | Old scope, new scope, impact | Scope change |
| CHGCOM02 | Schedule change notice | Stakeholders | Old date, new date, reason, risk | Schedule change |
| CHGCOM03 | Requirement change notice | Executor/reviewer | Changed requirement, source, acceptance | Requirement update |
| CHGCOM04 | Source change notice | Research/writing team | Source change, impact, rework needed | Source update |
| CHGCOM05 | Template change notice | Library users | Changed fields, examples, migration | Template update |
| CHGCOM06 | Workflow change notice | Operators | Changed steps, owners, checks | Process update |
| CHGCOM07 | Tool change notice | Executors/operators | Tool/version change, new instructions | Tool update |
| CHGCOM08 | Policy change notice | Affected users | Rule change, effective date, impact | Governance update |
| CHGCOM09 | Decision change notice | Stakeholders | Prior decision, new decision, rationale | Decision reversal |
| CHGCOM10 | Deprecation notice | Library/workflow users | Deprecated item, replacement, timeline | Retirement |

## ARCHCOM Archive / Knowledge Communication

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| ARCHCOM01 | Archive announcement | Future users/owner | Artifact, location, version, tags | Archive complete |
| ARCHCOM02 | Index update note | Library users | New entries, categories, paths | Index update |
| ARCHCOM03 | Reuse recommendation | Workflow owner | Candidate template, variables, tests | After successful run |
| ARCHCOM04 | Knowledge base entry | Team/future users | Problem, solution, steps, evidence | Reusable solution |
| ARCHCOM05 | Prompt library entry note | Prompt users | Use case, prompt, variables, checks | Prompt added |
| ARCHCOM06 | Workflow library entry note | Workflow users | Trigger, steps, artifacts, QA | Workflow added |
| ARCHCOM07 | Version snapshot note | Owners/auditors | Version, date, changes, retrieval | Snapshot |
| ARCHCOM08 | Retention notice | Owner/compliance | Keep/delete rule, date, recovery path | Retention action |
| ARCHCOM09 | Searchability note | Library owner | Tags, aliases, related items | Findability update |
| ARCHCOM10 | Archive gap notice | Owner | Missing archive fields/artifacts | Archive incomplete |

## EXECOM Executive / Summary Reporting

| Code | Communication type | Audience | Required content | Timing |
|---|---|---|---|---|
| EXECOM01 | Executive summary | Executive/decision owner | Outcome, impact, risk, ask | Decision/update |
| EXECOM02 | KPI report | Leadership/process owner | Metrics, trend, driver, action | Reporting cadence |
| EXECOM03 | Portfolio summary | Program owner | Workstreams, status, risks, decisions | Multi-project update |
| EXECOM04 | Investment memo summary | Investor/finance owner | Thesis, evidence, risks, recommendation | Finance decision |
| EXECOM05 | Compliance summary | Leadership/compliance | Status, exceptions, open risks | Governance review |
| EXECOM06 | Launch readiness summary | Leadership/release owner | Readiness, blockers, rollback, monitor | Pre-launch |
| EXECOM07 | Incident executive brief | Leadership | Impact, status, mitigation, next update | Major incident |
| EXECOM08 | Resource summary | Manager/owner | Capacity, bottleneck, allocation, ask | Planning review |
| EXECOM09 | Strategy summary | Leadership | Options, tradeoffs, recommendation | Strategy decision |
| EXECOM10 | Closeout executive summary | Sponsor/owner | Delivered, evidence, residual risk, next | Project close |
