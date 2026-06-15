# Professional Workflow Recovery and Resilience Matrix

Use this when a workflow is broken, degraded, blocked, producing unsafe output, missing critical evidence, or operating under incident pressure. Recovery and resilience rules define how to detect, triage, contain, diagnose, restore, retry, roll back, communicate, learn, and prevent recurrence.

Selection rule:

1. Identify whether the problem is active incident, degraded workflow, blocked dependency, bad output, lost context, tool failure, or risky release.
2. Select the closest recovery code.
3. Add severity, owner, containment action, evidence, restoration path, communication, and prevention action to the prompt packet.
4. Do not resume normal operation until restoration evidence or accepted degraded-mode evidence exists.

## RECALERT Recovery Detection

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| RECALERT01 | User-reported failure | User says output failed, broke, or is wrong | Capture exact symptom and expected state | Failure report |
| RECALERT02 | Test failure alert | Test, validator, or QA gate fails | Stop promotion and inspect failing gate | Test alert |
| RECALERT03 | Monitor alert | Metric, log, or heartbeat breaches threshold | Open incident and record signal | Alert record |
| RECALERT04 | Data anomaly alert | Source, metric, schema, or distribution changes unexpectedly | Freeze dependent output | Data anomaly |
| RECALERT05 | Missing evidence alert | Required proof, source, or artifact is absent | Block completion claim | Evidence gap |
| RECALERT06 | Quality degradation alert | Output is less accurate, complete, readable, or useful | Route to QA recovery | Quality alert |
| RECALERT07 | Deadline breach alert | Work or queue misses expected time window | Escalate timing risk | Breach note |
| RECALERT08 | Security/privacy alert | Sensitive data, secret, permission, or exposure risk appears | Contain exposure immediately | Security alert |
| RECALERT09 | Dependency alert | Upstream file, API, tool, person, or approval is unavailable | Switch to dependency recovery | Dependency alert |
| RECALERT10 | Customer impact alert | External user, client, buyer, or public audience is affected | Start impact communication | Impact alert |

## RECTRIAGE Recovery Triage

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| RECTRIAGE01 | Severity triage | Failure impact is unclear | Assign severity by user impact, risk, and urgency | Severity note |
| RECTRIAGE02 | Scope triage | Unknown which outputs or users are affected | Map affected artifacts, users, systems, and time window | Scope map |
| RECTRIAGE03 | Ownership triage | No clear recovery owner | Assign incident owner and backup | Owner record |
| RECTRIAGE04 | Domain triage | Failure may require expert/legal/security review | Route to SME or approver | Expert route |
| RECTRIAGE05 | Safety triage | Harm, compliance, privacy, or physical risk possible | Hold execution pending safety review | Safety gate |
| RECTRIAGE06 | Repro triage | Failure cannot yet be reproduced | Capture steps, inputs, versions, and environment | Repro packet |
| RECTRIAGE07 | Business triage | Need to decide whether to continue, pause, or roll back | Prepare stop/continue recommendation | Decision note |
| RECTRIAGE08 | Evidence triage | Logs/sources are incomplete or inconsistent | Preserve available evidence before changes | Evidence lock |
| RECTRIAGE09 | Dependency triage | Failure depends on another owner/system | Identify dependency owner and workaround | Dependency route |
| RECTRIAGE10 | Communication triage | Audience needs status but facts are incomplete | Send factual holding update | Holding update |

## CONTAIN Recovery Containment

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| CONTAIN01 | Stop bad output | Workflow is producing incorrect deliverables | Pause generation or distribution | Pause record |
| CONTAIN02 | Freeze source set | Sources may be corrupt, stale, or shifting | Lock current source snapshot | Source lock |
| CONTAIN03 | Quarantine item | One batch item, file, ticket, or artifact is suspect | Move to exception area | Quarantine log |
| CONTAIN04 | Revoke access | Access or secret exposure is suspected | Remove temporary access or rotate credential path | Access action |
| CONTAIN05 | Disable automation | Scheduled or event job is causing harm | Disable trigger or switch to manual mode | Automation pause |
| CONTAIN06 | Limit audience | Public/client exposure must be reduced | Withdraw, unpublish, or restrict output | Audience limit |
| CONTAIN07 | Preserve state | Debugging may destroy evidence | Copy logs, diffs, artifacts, and timestamps | Preservation bundle |
| CONTAIN08 | Cap volume | High-volume process amplifies failure | Throttle, cap, or drain queue | Volume cap |
| CONTAIN09 | Isolate integration | External system boundary may propagate issue | Disconnect or sandbox integration | Isolation note |
| CONTAIN10 | Hold approval | Approval/release path may accept unsafe output | Pause signoff until recovery complete | Approval hold |

## DIAG Recovery Diagnosis

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| DIAG01 | Root-cause hypothesis | Cause is unknown | Create ranked hypotheses and test plan | Hypothesis list |
| DIAG02 | Input diagnosis | Bad input may have caused bad output | Inspect input completeness, format, and constraints | Input audit |
| DIAG03 | Prompt diagnosis | Prompt or workflow instruction may be wrong | Compare prompt to expected task contract | Prompt audit |
| DIAG04 | Tool diagnosis | Tool/API/model/script may have failed | Check tool version, output, errors, and fallback | Tool log |
| DIAG05 | Data diagnosis | Data transform, schema, or metric may be wrong | Reprofile data and reconcile samples | Data audit |
| DIAG06 | State diagnosis | Resume or context state may be stale | Compare current state to latest authoritative evidence | State audit |
| DIAG07 | Human-process diagnosis | Review, approval, handoff, or ownership may have failed | Inspect responsibility chain | Process audit |
| DIAG08 | Environment diagnosis | Runtime, file path, permissions, or platform may differ | Record environment and reproduce | Environment note |
| DIAG09 | Regression diagnosis | New change may have broken old behavior | Compare before/after outputs or tests | Regression trace |
| DIAG10 | Multi-cause diagnosis | More than one cause may be present | Separate primary, contributing, and latent causes | Cause map |

## RESTORE Recovery Restoration

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| RESTORE01 | Restore known-good output | A previous valid artifact exists | Revert to or republish known-good output | Restore record |
| RESTORE02 | Restore source access | Needed file/link/API is unavailable | Reconnect, replace, or document fallback source | Access restored |
| RESTORE03 | Restore workflow state | Work can continue from a stable checkpoint | Resume from checkpoint with state proof | Resume note |
| RESTORE04 | Restore automation | Job was paused or disabled | Re-enable after dry run and monitoring | Automation restore |
| RESTORE05 | Restore integration | External connection was isolated | Validate handshake/import/export before reconnect | Integration restore |
| RESTORE06 | Restore data quality | Bad data affected outputs | Re-run clean/reconcile/validate steps | Data restore |
| RESTORE07 | Restore user trust | User/client confidence is damaged | Provide corrected output and clear caveat | Trust update |
| RESTORE08 | Restore schedule | Incident consumed delivery time | Replan milestones and communicate revised ETA | Schedule reset |
| RESTORE09 | Restore documentation | Runbook or instructions were wrong | Patch docs and verify operator can follow | Doc restore |
| RESTORE10 | Restore service level | SLA or operational target was breached | Confirm queue, owner, and monitoring recovered | SLA restore |

## RETRY Recovery Retry

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| RETRY01 | Bounded retry | Failure may be transient | Retry with maximum attempts and stop condition | Retry log |
| RETRY02 | Backoff retry | Service/tool is rate-limited or overloaded | Use delay/backoff and record attempt timing | Backoff log |
| RETRY03 | Alternative path retry | Primary path failed but fallback exists | Run fallback workflow and compare output | Fallback result |
| RETRY04 | Clean-input retry | Input may be malformed or noisy | Normalize input before rerun | Clean retry |
| RETRY05 | Smaller-scope retry | Large task failed due to size/complexity | Retry a minimal representative slice | Slice result |
| RETRY06 | Deterministic retry | Need reproducibility | Fix seed/version/input snapshot where possible | Repro retry |
| RETRY07 | Human-assisted retry | Automation cannot resolve ambiguity | Insert human review or correction | HITL retry |
| RETRY08 | Tool-swapped retry | Tool failure blocks progress | Use alternate tool and note difference | Tool swap |
| RETRY09 | Source-refreshed retry | Stale or missing source caused failure | Refresh source set and rerun impacted step | Source retry |
| RETRY10 | No-retry decision | Retry would amplify harm or waste | Stop and escalate with reason | No-retry note |

## ROLLBK Recovery Rollback

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| ROLLBK01 | Content rollback | Published content is wrong or risky | Restore previous content and notify impacted audience | Content rollback |
| ROLLBK02 | Prompt rollback | New prompt worsens output | Revert to prior prompt and record diff | Prompt rollback |
| ROLLBK03 | Data rollback | Dataset/schema/metric change breaks output | Revert source or transform version | Data rollback |
| ROLLBK04 | Code rollback | Implementation change breaks tests or behavior | Revert owned change or apply forward fix | Code rollback |
| ROLLBK05 | Automation rollback | Job/config trigger causes bad runs | Revert config and clear failed queue | Automation rollback |
| ROLLBK06 | Process rollback | New SOP/workflow harms operations | Return to previous process temporarily | Process rollback |
| ROLLBK07 | Access rollback | Permission change created risk | Revert permission and audit access | Access rollback |
| ROLLBK08 | Release rollback | Deployment or launch caused incident | Execute release rollback checklist | Release rollback |
| ROLLBK09 | Partial rollback | Only part of output/change is unsafe | Roll back affected slice only | Partial rollback |
| ROLLBK10 | Rollback impossible | No safe prior state exists | Switch to containment and forward repair | Rollback exception |

## DEGRADE Recovery Degraded Mode

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| DEGRADE01 | Manual mode | Automation unavailable | Operate manually with checklist | Manual log |
| DEGRADE02 | Read-only mode | Writes/changes are unsafe | Allow inspection only | Read-only note |
| DEGRADE03 | Reduced-scope mode | Full deliverable cannot be completed safely | Deliver critical subset with caveats | Scope caveat |
| DEGRADE04 | Lower-frequency mode | Cadence cannot be maintained | Reduce schedule and communicate | Cadence note |
| DEGRADE05 | Delayed mode | Deadline cannot be met without quality loss | Delay with revised plan | Delay note |
| DEGRADE06 | Best-effort mode | Evidence is incomplete but progress needed | Label confidence and limits | Best-effort caveat |
| DEGRADE07 | Offline mode | Web/API/tool unavailable | Use local cached sources or postpone live-dependent steps | Offline note |
| DEGRADE08 | Human-only mode | AI/tool path is unsafe or unreliable | Route to human expert/operator | Human route |
| DEGRADE09 | Pilot-only mode | Full rollout is risky | Limit to pilot cohort/sample | Pilot note |
| DEGRADE10 | Suspend mode | No degraded mode is safe | Stop workflow pending fix | Suspension record |

## ESCAL Recovery Escalation

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| ESCAL01 | Owner escalation | Primary owner cannot resolve | Escalate to accountable owner | Owner escalation |
| ESCAL02 | Technical escalation | Tool/code/data issue exceeds operator scope | Escalate to technical maintainer | Tech escalation |
| ESCAL03 | Security escalation | Secret, vulnerability, or exposure may exist | Escalate to security owner | Security escalation |
| ESCAL04 | Legal escalation | Rights, compliance, claim, or contract risk appears | Escalate to legal/compliance | Legal escalation |
| ESCAL05 | Finance escalation | Cost, budget, payment, or investment risk appears | Escalate to finance owner | Finance escalation |
| ESCAL06 | Executive escalation | High business impact or public risk appears | Escalate with concise impact brief | Exec escalation |
| ESCAL07 | Customer escalation | External commitment or SLA is at risk | Escalate through client/support path | Customer escalation |
| ESCAL08 | Vendor escalation | Third-party tool/service/vendor blocks recovery | Open vendor support path | Vendor case |
| ESCAL09 | SME escalation | Domain correctness cannot be judged internally | Request expert validation | SME escalation |
| ESCAL10 | Stop-work escalation | Continuing may cause harm | Require explicit go/no-go decision | Stop-work record |

## RECCOMMS Recovery Communication

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| RECCOMMS01 | Internal status | Team needs current incident state | Send impact, owner, next update, ETA | Status update |
| RECCOMMS02 | User status | User needs what happened and what next | Send clear nontechnical update | User update |
| RECCOMMS03 | Client status | Client-facing commitment is affected | Send approved impact and recovery note | Client update |
| RECCOMMS04 | Executive status | Leadership needs decision-level view | Send risk, options, recommendation | Exec update |
| RECCOMMS05 | Support status | Support team needs response guidance | Provide FAQ, known issue, workaround | Support update |
| RECCOMMS06 | Public status | Public audience may be affected | Use approved public communication path | Public update |
| RECCOMMS07 | Correction notice | Earlier output was wrong | Explain correction without overclaim | Correction note |
| RECCOMMS08 | ETA update | Timeline changed during recovery | Provide revised ETA and dependency | ETA note |
| RECCOMMS09 | Resolution notice | Recovery is complete | State fix, validation, residual risk | Resolution note |
| RECCOMMS10 | No-update cadence | Recovery takes longer than expected | Send scheduled "still working" update | Cadence update |

## POSTM Recovery Postmortem

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| POSTM01 | Timeline reconstruction | Need to understand incident sequence | Build event timeline from evidence | Timeline |
| POSTM02 | Impact analysis | Need affected user/output/scope | Quantify impact and duration | Impact report |
| POSTM03 | Root cause analysis | Need durable explanation | Separate root, contributing, and detection gaps | RCA |
| POSTM04 | What-went-well | Need preserve effective actions | Capture useful response patterns | Positive notes |
| POSTM05 | What-went-wrong | Need identify response gaps | Capture failures without blame | Gap notes |
| POSTM06 | Action item creation | Need prevent repeat | Create owner, due date, acceptance evidence | Action list |
| POSTM07 | Control update | Existing control failed or was absent | Add or modify control/gate | Control patch |
| POSTM08 | Runbook update | Operator instructions were incomplete | Patch runbook and test sample | Runbook patch |
| POSTM09 | Training update | People did not know how to respond | Add training or example | Training action |
| POSTM10 | Postmortem closeout | Actions need closure proof | Verify each action or track residual risk | Postmortem closeout |

## PREVENT Recovery Prevention

| Code | Recovery need | Trigger | Required action | Evidence |
|---|---|---|---|---|
| PREVENT01 | Add early warning | Issue was detected late | Add alert, check, or review before failure point | Warning control |
| PREVENT02 | Add validation gate | Bad artifact passed unchecked | Add validator or reviewer gate | Validation gate |
| PREVENT03 | Add source lock | Moving sources caused drift | Lock or snapshot source set | Source snapshot |
| PREVENT04 | Add rollback plan | Rollback was slow or impossible | Define rollback asset and owner | Rollback plan |
| PREVENT05 | Add fallback path | Single dependency caused outage | Add alternate tool/source/process | Fallback plan |
| PREVENT06 | Add capacity buffer | Overload caused failure | Add buffer, queue cap, or schedule rule | Buffer rule |
| PREVENT07 | Add permission boundary | Access risk caused incident | Enforce least privilege and expiry | Access control |
| PREVENT08 | Add regression test | Change reintroduced old failure | Add regression sample/check | Regression test |
| PREVENT09 | Add decision threshold | Team hesitated on stop/go | Define threshold and approver | Decision rule |
| PREVENT10 | Add resilience drill | Recovery path is untested | Schedule drill or tabletop simulation | Drill record |



