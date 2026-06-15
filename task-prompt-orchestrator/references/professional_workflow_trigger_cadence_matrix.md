# Professional Workflow Trigger and Cadence Matrix

Use this when a workflow must define what starts it, when it repeats, what pauses it, what escalates it, and how often it should run. Trigger and cadence rules prevent workflows from depending on vague human memory.

Selection rule:

1. Identify whether the workflow is request-driven, event-driven, scheduled, monitored, approval-driven, batch-driven, or recovery-driven.
2. Select the closest trigger/cadence code.
3. Add trigger condition, cadence, owner, and stop condition to the prompt packet.
4. If the trigger is unclear, route to planning or blocked state before automation.

## REQT Request-Driven Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| REQT01 | Direct user ask | Run once per explicit request | Intake brief | User request satisfied |
| REQT02 | Follow-up request | Resume from current state | Resume handoff | Follow-up answered |
| REQT03 | Correction request | Re-run affected workflow segment | Updated brief | Correction accepted |
| REQT04 | Expansion request | Add coverage without rewriting stable parts | Coverage delta | New scope covered |
| REQT05 | Clarification answer | Continue after missing input arrives | Clarification note | Blocker resolved |
| REQT06 | Review request | Inspect artifact against criteria | Review criteria | Findings delivered |
| REQT07 | Optimization request | Improve existing artifact or process | Baseline artifact | Improvement verified |
| REQT08 | Conversion request | Transform artifact into new format | Source and target spec | Target artifact ready |
| REQT09 | Search request | Find or index relevant material | Search scope | Results indexed |
| REQT10 | Execution request | Move from plan to action | Approved plan or low-risk assumption | Action completed |

## TIMT Time / Schedule Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| TIMT01 | One-time deadline | Run before specified date/time | Deadline and deliverable | Deadline passed or delivered |
| TIMT02 | Daily cadence | Run once per day at defined time | Owner and daily checklist | Cadence retired |
| TIMT03 | Weekly cadence | Run once per week with summary | Week boundary and report format | No longer needed |
| TIMT04 | Monthly cadence | Run monthly for review/reporting | Month close rule | Review completed |
| TIMT05 | Quarterly cadence | Run quarterly for strategy, finance, or governance | Quarter calendar | Quarter package delivered |
| TIMT06 | Annual cadence | Run yearly for planning, audit, or renewal | Year-end trigger | Annual cycle closed |
| TIMT07 | Rolling window | Run over last N hours/days/weeks | Window definition | Window processed |
| TIMT08 | Countdown trigger | Run when time remaining reaches threshold | Threshold and action | Countdown action done |
| TIMT09 | Timezone trigger | Run relative to locale-specific time | Timezone and region | Local window closed |
| TIMT10 | Grace-period trigger | Run after waiting period expires | Grace duration | Grace action done |

## EVNT Event-Driven Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| EVNT01 | New file appears | Run per new file or bundle | Watch path and file type | File processed |
| EVNT02 | File changed | Run when watched artifact changes | Change detection rule | Change reconciled |
| EVNT03 | New message/comment | Run per message, thread, or feedback item | Channel and filter | Response posted or logged |
| EVNT04 | New issue/ticket | Run per issue creation | Ticket source and triage rule | Ticket triaged |
| EVNT05 | Status changed | Run when status enters target state | Status field mapping | Transition handled |
| EVNT06 | Form submitted | Run per submitted form | Form schema | Submission processed |
| EVNT07 | Order/transaction event | Run per order, payment, refund, or invoice event | Event type and system | Event reconciled |
| EVNT08 | Build/deploy event | Run on build, test, release, or deploy status | CI/CD event source | Event validated |
| EVNT09 | Dataset refresh | Run when source data updates | Source freshness rule | Data checked |
| EVNT10 | External milestone | Run when partner/client/vendor milestone occurs | Milestone owner | Milestone processed |

## MONT Monitoring Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| MONT01 | Threshold crossed | Run when metric exceeds or falls below threshold | Metric and threshold | Metric handled |
| MONT02 | Anomaly detected | Run when metric deviates from expected range | Baseline and anomaly rule | Cause recorded |
| MONT03 | Error rate spike | Run when errors exceed limit | Error source and limit | Spike mitigated |
| MONT04 | Quality score drop | Run when QA or eval score drops | Score source and minimum | Quality restored |
| MONT05 | SLA breach | Run when time or service target is missed | SLA definition | Breach resolved |
| MONT06 | Freshness breach | Run when data/source/artifact is stale | Freshness threshold | Source refreshed |
| MONT07 | Cost/budget alert | Run when spend or resource use crosses threshold | Budget threshold | Cost action taken |
| MONT08 | Security alert | Run when suspicious access, secret, or vulnerability appears | Alert source | Security triaged |
| MONT09 | Compliance watch | Run when policy or regulation trigger appears | Rule source | Compliance reviewed |
| MONT10 | Sentiment/feedback alert | Run when feedback pattern crosses threshold | Feedback metric | Response plan made |

## BATT Batch / Queue Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| BATT01 | Queue reaches size | Run when item count reaches threshold | Queue and threshold | Queue drained |
| BATT02 | Batch window opens | Run all items collected in window | Window and manifest | Batch closed |
| BATT03 | Manual batch submitted | Run user-provided list | Item manifest | All items processed |
| BATT04 | Backlog cleanup | Run oldest or highest-priority backlog items | Priority rule | Backlog target reached |
| BATT05 | Bulk generation | Run variants/items from a source table | Source table and naming rule | Outputs generated |
| BATT06 | Bulk validation | Validate many artifacts against same rule | Validation rule | Exceptions logged |
| BATT07 | Bulk migration | Move or convert many assets | Source/target map | Migration reconciled |
| BATT08 | Bulk indexing | Add many prompts/files/items to index | Index schema | Index updated |
| BATT09 | Batch retry | Re-run failed items only | Failure manifest | Failed items resolved |
| BATT10 | Batch sampling QA | QA sample after bulk processing | Sampling rule | Sample accepted |

## APPT Approval / Gate Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| APPT01 | Review requested | Run when artifact is ready for review | Review criteria | Review complete |
| APPT02 | Approval requested | Run when final signoff is needed | Approver and packet | Approved or rejected |
| APPT03 | Gate passed | Move to next phase only after gate pass | Gate evidence | Next phase started |
| APPT04 | Gate failed | Run rework or escalation | Failure reason | Rework path chosen |
| APPT05 | Conditional approval | Run condition cleanup before release | Conditions list | Conditions met |
| APPT06 | Exception request | Run exception approval workflow | Exception rationale | Exception decided |
| APPT07 | Compliance gate | Run before regulated/public/high-risk output | Compliance checklist | Compliance decision |
| APPT08 | Budget gate | Run before spend/resource commitment | Budget packet | Budget decision |
| APPT09 | Launch gate | Run before publish/deploy/go-live | Launch checklist | Launch decision |
| APPT10 | Archive gate | Run before final archive or deletion | Archive/retention rule | Archive action done |

## DATAT Data / Source Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| DATAT01 | New source available | Run when source material is added | Source inventory | Source processed |
| DATAT02 | Source version changed | Run when version/date changes | Version tracking | Impact assessed |
| DATAT03 | Data schema changed | Run when columns/types/grain change | Schema watch | Schema reconciled |
| DATAT04 | Data quality issue | Run when missing, duplicate, or invalid data appears | Quality rule | Issue handled |
| DATAT05 | Citation broken | Run when source/citation no longer resolves | Citation ledger | Citation repaired |
| DATAT06 | File format changed | Run when source format differs from expected | Format map | Format handled |
| DATAT07 | Access changed | Run when permissions or availability changes | Access rule | Access restored or fallback |
| DATAT08 | Data retention date | Run when retention/disposal date arrives | Retention schedule | Keep/delete decided |
| DATAT09 | Source conflict detected | Run when sources contradict | Conflict rule | Conflict resolved |
| DATAT10 | Source lock requested | Run when user wants source set frozen | Lock rule | Source set locked |

## LIFE Lifecycle Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| LIFE01 | Project kickoff | Run at beginning of project | Goal and stakeholders | Kickoff packet |
| LIFE02 | Discovery complete | Run transition from discovery to strategy | Discovery findings | Strategy brief |
| LIFE03 | Plan approved | Run transition from planning to production | Approved plan | Production started |
| LIFE04 | Draft ready | Run review/QA workflow | Draft artifact | Draft reviewed |
| LIFE05 | Pre-launch | Run readiness checks before release | Launch criteria | Ready or blocked |
| LIFE06 | Post-launch | Run monitoring and feedback loop | Launch record | Post-launch report |
| LIFE07 | Operational cycle | Run periodic ops review | Ops cadence | Ops review complete |
| LIFE08 | Optimization cycle | Run improvement workflow after baseline | Baseline and metric | Improvement logged |
| LIFE09 | Retirement trigger | Run archive/deprecation workflow | Retirement criteria | Retired or archived |
| LIFE10 | Renewal trigger | Run renewal, refresh, or re-approval workflow | Renewal date | Renewal decision |

## FBKT Feedback Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| FBKT01 | User feedback arrives | Run feedback triage | Feedback source | Feedback categorized |
| FBKT02 | Reviewer comments arrive | Run comment resolution | Review thread | Comments resolved |
| FBKT03 | Customer complaint | Run issue diagnosis and response | Complaint record | Response plan |
| FBKT04 | Positive signal | Run amplification or learning capture | Success signal | Reuse note |
| FBKT05 | Low score/rating | Run root cause workflow | Rating source | Cause and action |
| FBKT06 | Feature request | Run prioritization workflow | Request context | Priority decided |
| FBKT07 | Bug report | Run repro and triage workflow | Bug evidence | Triage result |
| FBKT08 | Stakeholder change request | Run impact assessment | Change request | Impact decision |
| FBKT09 | Training question | Run teaching or documentation update | Question context | Answer or doc update |
| FBKT10 | Repeated feedback pattern | Run pattern analysis and systemic fix | Feedback cluster | Pattern action |

## RISK Risk / Exception Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| RISK01 | New risk identified | Run risk assessment | Risk description | Risk registered |
| RISK02 | Risk severity increases | Run escalation workflow | Severity rule | Escalated or mitigated |
| RISK03 | Compliance concern | Run compliance review | Concern and evidence | Compliance decision |
| RISK04 | Privacy concern | Run privacy impact workflow | Data fields and purpose | Privacy action |
| RISK05 | Security concern | Run security triage | Alert or finding | Security action |
| RISK06 | Safety concern | Stop or reroute workflow | Hazard and stop rule | Safe path chosen |
| RISK07 | Financial exposure | Run assumption and approval workflow | Exposure amount or decision | Finance decision |
| RISK08 | Reputation/public claim risk | Run claim and approval check | Claim and audience | Claim approved or changed |
| RISK09 | IP/licensing concern | Run rights check | Asset/source/license | Rights decision |
| RISK10 | Unknown high-impact effect | Pause and collect evidence | Unknown and impact | Evidence or escalation |

## DEPT Dependency Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| DEPT01 | Upstream complete | Start only after required upstream artifact exists | Upstream artifact | Downstream started |
| DEPT02 | Downstream waiting | Run handoff when another actor is blocked on output | Downstream owner | Handoff complete |
| DEPT03 | Vendor response | Resume after vendor/partner update | Vendor dependency | Response handled |
| DEPT04 | API/tool availability | Run when tool becomes available | Tool status check | Tool used or fallback |
| DEPT05 | Permission granted | Resume after access or approval granted | Permission record | Action performed |
| DEPT06 | Environment ready | Run after runtime, files, or repo become available | Environment check | Execution started |
| DEPT07 | Human owner available | Resume when required reviewer/approver is available | Owner and artifact | Review/approval done |
| DEPT08 | External date reached | Start when contractual or calendar milestone arrives | Date/milestone | Milestone handled |
| DEPT09 | Dependency failed | Run fallback or escalation | Failure evidence | Fallback chosen |
| DEPT10 | Dependency retired | Update workflow when dependency is removed | Replacement rule | Workflow updated |

## ADHT Ad Hoc / Manual Control Triggers

| Code | Trigger | Cadence rule | Required setup | Stop condition |
|---|---|---|---|---|
| ADHT01 | Manual override | Human intentionally changes normal path | Override reason | Override recorded |
| ADHT02 | Emergency run | Run immediately outside normal cadence | Emergency reason | Emergency resolved |
| ADHT03 | One-off experiment | Run once to test approach | Hypothesis and success rule | Experiment result |
| ADHT04 | Exploratory spike | Run limited discovery before commitment | Timebox and question | Spike conclusion |
| ADHT05 | Manual pause | Stop workflow until resumed | Pause reason | Resume trigger |
| ADHT06 | Manual resume | Continue after pause | Current-state check | Work resumed |
| ADHT07 | Manual cancellation | Stop workflow and close open loops | Cancellation reason | Cancellation note |
| ADHT08 | Manual re-prioritization | Change order or focus | New priority rule | Priority map updated |
| ADHT09 | Manual archive | Preserve or retire artifacts on command | Archive target | Archive complete |
| ADHT10 | Manual cleanup | Remove obsolete intermediate artifacts | Cleanup scope | Cleanup verified |
