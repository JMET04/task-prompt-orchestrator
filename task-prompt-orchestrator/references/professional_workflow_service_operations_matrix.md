# Professional Workflow Service Operations Matrix

Use this when a workflow operates as an ongoing service, request queue, support function, automation, operational runbook, or production process. Service operations rules define intake, queueing, SLA, incident, problem, change, release, runbook, monitoring, escalation, capacity, and continuity management.

Selection rule:

1. Identify the operational function the workflow must support.
2. Select the closest service operation code.
3. Add owner, intake channel, priority, SLA/threshold, runbook, and reporting cadence to the prompt packet.
4. For recurring operations, define monitoring and exception handling before scaling.

## SERVREQ Service Request Management

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| SERVREQ01 | Standard request | Intake form/fields and expected output | Route by request type | Request record |
| SERVREQ02 | Urgent request | Urgency criteria and owner | Expedite only when criteria met | Urgency note |
| SERVREQ03 | Complex request | Scoping and decomposition | Split into work items | Work breakdown |
| SERVREQ04 | Repeated request | Template and reusable response | Standardize workflow | Template use |
| SERVREQ05 | High-risk request | Risk gate and approver | Hold until risk reviewed | Risk gate |
| SERVREQ06 | Incomplete request | Required input checklist | Ask/assume/block by rule | Intake gap |
| SERVREQ07 | External request | Client/vendor/public source | Confirm audience and authority | External record |
| SERVREQ08 | Internal request | Team/user/department source | Confirm owner and priority | Internal record |
| SERVREQ09 | Request cancellation | Cancellation reason and state | Close open loops | Cancellation note |
| SERVREQ10 | Request closeout | Done criteria and evidence | Close only with proof | Closeout record |

## QUEUE Queue / Backlog Management

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| QUEUE01 | Queue intake | Queue source and item schema | Add every item to manifest | Queue manifest |
| QUEUE02 | Queue prioritization | Priority criteria | Sort by SLA/risk/value | Priority queue |
| QUEUE03 | Queue aging | Age threshold | Escalate stale items | Aging report |
| QUEUE04 | Queue deduplication | Duplicate detection rule | Merge or close duplicates | Dedup log |
| QUEUE05 | Queue batching | Batch window/size | Process by batch manifest | Batch record |
| QUEUE06 | Queue exception | Failed item handling | Move to exception queue | Exception queue |
| QUEUE07 | Queue reassignment | Owner availability | Reassign with handoff | Reassignment log |
| QUEUE08 | Queue status | Visible state labels | Update status per transition | Status report |
| QUEUE09 | Queue capacity | Workload vs available resources | Throttle or add capacity | Capacity report |
| QUEUE10 | Queue closure | Done/duplicate/cancelled rules | Close with reason | Closure reason |

## SLAOPS SLA / Service Level Operations

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| SLAOPS01 | Response SLA | Response target by priority | Track time to first response | SLA report |
| SLAOPS02 | Resolution SLA | Completion target by priority | Track time to resolution | Resolution report |
| SLAOPS03 | Review SLA | Reviewer turnaround target | Escalate missed review | Review SLA |
| SLAOPS04 | Approval SLA | Approver turnaround target | Escalate missed approval | Approval SLA |
| SLAOPS05 | Freshness SLA | Source/data age threshold | Refresh before breach | Freshness SLA |
| SLAOPS06 | Quality SLA | Minimum QA/acceptance threshold | Rework below threshold | Quality SLA |
| SLAOPS07 | Availability SLA | Tool/service uptime target | Monitor and fallback | Availability report |
| SLAOPS08 | Batch SLA | Batch completion window | Track batch completion | Batch SLA |
| SLAOPS09 | Communication SLA | Update cadence during waiting/incidents | Send scheduled updates | Comms SLA |
| SLAOPS10 | SLA exception | Approved deviation reason | Record and communicate exception | SLA exception |

## INCOPS Incident Operations

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| INCOPS01 | Incident detection | Alert/source and severity rule | Create incident record | Incident ticket |
| INCOPS02 | Incident triage | Impact, urgency, owner | Assign severity and lead | Triage note |
| INCOPS03 | Incident stabilization | Immediate containment actions | Stabilize before root cause | Stabilization log |
| INCOPS04 | Incident communication | Audience and update cadence | Facts only, no speculation | Incident updates |
| INCOPS05 | Incident workaround | Temporary safe path | Record limitations | Workaround note |
| INCOPS06 | Incident recovery | Restore normal operation | Verify recovery | Recovery proof |
| INCOPS07 | Incident escalation | Severity/threshold owner | Escalate when criteria met | Escalation log |
| INCOPS08 | Incident postmortem | Timeline, cause, impact, actions | Capture prevention | Postmortem |
| INCOPS09 | Incident closure | Recovery and actions accepted | Close with residual risks | Incident closeout |
| INCOPS10 | Incident trend | Repeated incident types | Feed problem management | Incident trend |

## PROBOPS Problem Management

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| PROBOPS01 | Recurring issue | Failure pattern and examples | Open problem record | Problem log |
| PROBOPS02 | Root cause analysis | Evidence, timeline, hypotheses | Validate cause before fix | RCA note |
| PROBOPS03 | Known error | Cause known but not fixed | Document workaround | Known error entry |
| PROBOPS04 | Permanent fix | Root cause and change plan | Test before rollout | Fix validation |
| PROBOPS05 | Problem prioritization | Impact/frequency/cost | Rank problem backlog | Problem priority |
| PROBOPS06 | Problem ownership | Owner and action plan | Assign accountable owner | Owner note |
| PROBOPS07 | Problem prevention | Control added to prevent recurrence | Link control to failure | Prevention note |
| PROBOPS08 | Problem communication | Stakeholders and status | Report progress/caveats | Problem update |
| PROBOPS09 | Problem closure | Fix verified and monitored | Close after recurrence window | Closure note |
| PROBOPS10 | Problem knowledge | Lesson reusable elsewhere | Add KB/workflow update | Knowledge entry |

## CHGOPS Operational Change

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| CHGOPS01 | Standard change | Pre-approved low-risk change | Follow standard checklist | Change record |
| CHGOPS02 | Normal change | Impact, approval, schedule | Review before execution | Change approval |
| CHGOPS03 | Emergency change | Urgent risk/incident need | Execute with post-review | Emergency record |
| CHGOPS04 | Change impact | Affected users/systems/data | Run impact matrix | Impact assessment |
| CHGOPS05 | Change schedule | Planned window and owner | Avoid conflicts/deadlines | Change calendar |
| CHGOPS06 | Change communication | Stakeholders and message | Notify before/after | Change notice |
| CHGOPS07 | Change test | Validation before/after change | Run test plan | Test result |
| CHGOPS08 | Change rollback | Backout plan and trigger | Prepare rollback | Rollback plan |
| CHGOPS09 | Change audit | What changed, why, by whom | Preserve evidence | Change audit |
| CHGOPS10 | Change closure | Result, verification, lessons | Close after validation | Change closeout |

## RELOPS Release Operations

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| RELOPS01 | Release planning | Scope, date, owner, dependencies | Define release checklist | Release plan |
| RELOPS02 | Release readiness | QA, approval, rollback, monitor | Gate release | Readiness check |
| RELOPS03 | Release packaging | Files/assets/docs/version | Verify package manifest | Release package |
| RELOPS04 | Release notes | Changes, risks, migration | Communicate clearly | Release notes |
| RELOPS05 | Release approval | Approver and criteria | Approve versioned artifact | Approval record |
| RELOPS06 | Release deployment | Execution steps and owner | Follow runbook | Deployment log |
| RELOPS07 | Release monitoring | Metrics and alert window | Monitor after release | Monitor report |
| RELOPS08 | Release rollback | Trigger and backout steps | Restore prior state if needed | Rollback proof |
| RELOPS09 | Release adoption | Users/operators informed/trained | Track adoption | Adoption report |
| RELOPS10 | Release retrospective | Success, failures, lessons | Improve next release | Retro note |

## RUNOPS Runbook Operations

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| RUNOPS01 | Runbook creation | Trigger, steps, owner, expected result | Write executable steps | Runbook |
| RUNOPS02 | Runbook execution | Operator and inputs | Follow steps and log deviations | Run log |
| RUNOPS03 | Runbook validation | Sample execution | Verify steps work | Validation note |
| RUNOPS04 | Runbook exception | Failure or unexpected state | Use exception path | Exception log |
| RUNOPS05 | Runbook escalation | Threshold and owner | Escalate with packet | Escalation note |
| RUNOPS06 | Runbook update | Drift/failure/change detected | Version and communicate update | Runbook update |
| RUNOPS07 | Runbook training | New operator/user | Train with practice | Training record |
| RUNOPS08 | Runbook audit | Evidence and compliance check | Preserve logs | Audit note |
| RUNOPS09 | Runbook archive | Retired or superseded runbook | Archive with version | Archive record |
| RUNOPS10 | Runbook simplification | Operator friction/low-value steps | Remove or automate steps | Simplification note |

## MONOPS Monitoring Operations

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| MONOPS01 | Health monitoring | Health signal and threshold | Track status | Health report |
| MONOPS02 | Quality monitoring | QA score/finding trend | Alert on quality drop | Quality monitor |
| MONOPS03 | Freshness monitoring | Source/data age threshold | Refresh or alert | Freshness monitor |
| MONOPS04 | Cost monitoring | Cost source and threshold | Alert on overrun | Cost monitor |
| MONOPS05 | Queue monitoring | Queue depth/age | Escalate backlog | Queue monitor |
| MONOPS06 | Error monitoring | Error type/rate | Trigger incident/problem | Error monitor |
| MONOPS07 | SLA monitoring | SLA target and status | Escalate breach | SLA dashboard |
| MONOPS08 | Adoption monitoring | Usage/search/reuse metric | Improve low adoption | Adoption monitor |
| MONOPS09 | Risk monitoring | Open risk/exception status | Escalate stale risk | Risk monitor |
| MONOPS10 | Outcome monitoring | Business/user outcome metric | Reassess value | Outcome monitor |

## ESCOPS Operational Escalation

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| ESCOPS01 | Functional escalation | Route to domain owner | Provide evidence and ask | Escalation packet |
| ESCOPS02 | Hierarchical escalation | Route to manager/sponsor | Include impact and options | Escalation note |
| ESCOPS03 | Technical escalation | Route to engineering/tool owner | Include logs/repro | Technical escalation |
| ESCOPS04 | Risk escalation | Route to risk/compliance/security | Include severity and mitigation | Risk escalation |
| ESCOPS05 | Client escalation | Route to client owner | Include timeline and ask | Client escalation |
| ESCOPS06 | Vendor escalation | Route to vendor owner | Include SLA and evidence | Vendor escalation |
| ESCOPS07 | Time escalation | Deadline/SLA at risk | Escalate before breach | Time escalation |
| ESCOPS08 | Approval escalation | Approver unavailable/delayed | Use backup/escalation path | Approval escalation |
| ESCOPS09 | Capacity escalation | Workload exceeds resources | Add capacity or reduce scope | Capacity escalation |
| ESCOPS10 | Escalation closure | Owner responds or issue resolved | Record decision/action | Escalation closeout |

## CAPOPS Capacity Operations

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| CAPOPS01 | Demand forecast | Expected request volume | Estimate resource need | Forecast |
| CAPOPS02 | Capacity plan | Available people/tools/time | Match demand to capacity | Capacity plan |
| CAPOPS03 | Load balancing | Multiple owners/lanes | Route by capacity and expertise | Load plan |
| CAPOPS04 | Throttling | Demand exceeds capacity | Limit intake or batch | Throttle rule |
| CAPOPS05 | Surge mode | Temporary spike | Activate surge process | Surge note |
| CAPOPS06 | Capacity bottleneck | Repeated wait point | Add resource/automation/scope cut | Bottleneck fix |
| CAPOPS07 | Reviewer capacity | Review queue exceeds limit | Add tiering/sampling/backup | Review capacity |
| CAPOPS08 | Tool capacity | Tool limits throughput | Queue/chunk/fallback | Tool capacity |
| CAPOPS09 | Budget capacity | Spend constrains service | Prioritize or request budget | Budget capacity |
| CAPOPS10 | Capacity review | Periodic capacity check | Update plan and thresholds | Capacity review |

## CONTOPS Continuity Operations

| Code | Operation | Required setup | Control | Evidence |
|---|---|---|---|---|
| CONTOPS01 | Backup owner | Primary unavailable | Use backup handoff | Backup record |
| CONTOPS02 | State preservation | Work may pause/transfer | Save current state | State packet |
| CONTOPS03 | Disaster fallback | Critical tool/system unavailable | Use alternate path | Continuity plan |
| CONTOPS04 | Data backup | Data/artifacts critical | Snapshot before risky change | Backup proof |
| CONTOPS05 | Recovery objective | Define acceptable recovery time/scope | Set recovery target | RTO/RPO note |
| CONTOPS06 | Manual fallback | Automation unavailable | Run manual runbook | Manual log |
| CONTOPS07 | Continuity test | Simulate outage/handoff | Recovery path works | Continuity test |
| CONTOPS08 | Knowledge continuity | Key knowledge concentrated in one person | Document and train backup | Knowledge handoff |
| CONTOPS09 | Archive continuity | Final artifacts must remain findable | Verify archive retrieval | Retrieval proof |
| CONTOPS10 | Service retirement | Service no longer needed | Close users, archive, deprecate | Retirement record |
