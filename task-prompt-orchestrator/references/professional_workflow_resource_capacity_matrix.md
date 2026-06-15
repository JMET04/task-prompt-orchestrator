# Professional Workflow Resource and Capacity Matrix

Use this when a workflow needs explicit planning for time, people, budget, tools, data, infrastructure, capacity, bottlenecks, scheduling, or resource constraints. Resource capacity rules prevent workflows from being logically correct but operationally impossible.

Selection rule:

1. Identify the resource that constrains workflow execution.
2. Select the closest resource/capacity code.
3. Add capacity assumption, allocation rule, limit, and fallback to the prompt packet.
4. Recheck resource feasibility before committing to schedule, automation, or delivery.

## TIME Time Resources

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| TIME01 | Deadline | When must the output be ready? | Work backward from fixed deadline | Deadline plan |
| TIME02 | Timebox | How much time may this phase consume? | Limit exploration and report result | Timebox note |
| TIME03 | Cycle time | How long does one run take? | Measure start-to-finish duration | Cycle metric |
| TIME04 | Lead time | How long from request to delivery? | Include queue and approval waits | Lead-time estimate |
| TIME05 | Review time | How long does human review need? | Reserve review window before closeout | Review schedule |
| TIME06 | Refresh time | How often must sources/data update? | Set freshness cadence | Refresh plan |
| TIME07 | Retry time | How much time for failed attempts? | Budget bounded retry window | Retry budget |
| TIME08 | Handoff time | When must next owner receive output? | Schedule handoff before dependency needs it | Handoff timing |
| TIME09 | Maintenance time | How often must workflow be maintained? | Add recurring maintenance slot | Maintenance cadence |
| TIME10 | Grace time | How much buffer exists before escalation? | Define grace period and trigger | Grace rule |

## PEOP People Capacity

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| PEOP01 | Owner capacity | Who owns the outcome and has bandwidth? | Assign owner with capacity note | Owner capacity |
| PEOP02 | Reviewer capacity | Who can review and when? | Match reviewer to domain and timing | Reviewer schedule |
| PEOP03 | Approver capacity | Who can approve before deadline? | Identify backup approver if needed | Approval capacity |
| PEOP04 | SME capacity | Which expert is needed? | Use SME only for material domain risk | SME request |
| PEOP05 | Operator capacity | Who runs the workflow repeatedly? | Assign operator and runbook | Operator assignment |
| PEOP06 | Support capacity | Who handles user/client questions? | Define support owner and SLA | Support plan |
| PEOP07 | Escalation capacity | Who can unblock? | Assign escalation owner and threshold | Escalation map |
| PEOP08 | Training capacity | Who needs training to execute workflow? | Provide minimal training packet | Training plan |
| PEOP09 | Coverage capacity | Is there enough human coverage for volume? | Segment, batch, or automate | Coverage plan |
| PEOP10 | Backup capacity | Who takes over when owner unavailable? | Name backup and handoff rule | Backup plan |

## BUD Budget Resources

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| BUD01 | Fixed budget | What spend ceiling constrains work? | Fit scope/tooling to budget | Budget note |
| BUD02 | Variable cost | What cost grows with volume? | Estimate per item/run | Unit cost |
| BUD03 | Tool cost | Which paid tools/APIs are used? | Use paid tools only where value/risk warrants | Tool cost plan |
| BUD04 | Review cost | How much expert/reviewer time costs? | Reserve review for high-impact areas | Review cost note |
| BUD05 | Rework cost | What failure costs if output is wrong? | Invest QA where rework cost is high | Rework risk |
| BUD06 | Opportunity cost | What work is displaced? | Prioritize highest value path | Priority rationale |
| BUD07 | Maintenance cost | What ongoing upkeep costs? | Add owner/cadence or avoid overbuilding | Maintenance cost |
| BUD08 | Automation cost | Is automation worth setup cost? | Automate above repeatability threshold | Automation ROI |
| BUD09 | Approval cost | What delay/cost comes from approval? | Use risk-tiered approvals | Approval cost |
| BUD10 | Cost escalation | When must budget be re-approved? | Escalate above threshold | Budget gate |

## TOOLCAP Tool Capacity

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| TOOLCAP01 | Tool availability | Is the required tool available now? | Check availability before planning around it | Tool readiness |
| TOOLCAP02 | Tool capability | Can the tool actually perform the task? | Test on small input if uncertain | Tool fit check |
| TOOLCAP03 | Tool throughput | How many items can it process? | Batch within safe rate/limits | Throughput note |
| TOOLCAP04 | Tool reliability | How often does it fail or vary? | Add QA/retry for unreliable tools | Reliability note |
| TOOLCAP05 | Tool permission | Does workflow have access rights? | Confirm access or fallback | Permission status |
| TOOLCAP06 | Tool version | Which version affects behavior? | Record version for reproducibility | Version note |
| TOOLCAP07 | Tool fallback | What if the tool fails? | Define alternate manual/tool path | Fallback path |
| TOOLCAP08 | Tool safety | Could the tool modify/delete/publish? | Add preview/approval gate | Safety gate |
| TOOLCAP09 | Tool integration | Does output feed next step cleanly? | Validate IO contract | Integration check |
| TOOLCAP10 | Tool observability | Can runs be inspected? | Capture logs, IDs, outputs | Tool log |

## DATACAP Data / Source Capacity

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| DATACAP01 | Data availability | Is required data/source present? | Confirm before analysis/generation | Data inventory |
| DATACAP02 | Data volume | How much data must be processed? | Sample, batch, or automate by volume | Volume note |
| DATACAP03 | Data quality | Is data clean enough? | Profile before using | Quality profile |
| DATACAP04 | Data freshness | Is data current enough? | Refresh if freshness threshold fails | Freshness check |
| DATACAP05 | Data sensitivity | Is data private/regulated? | Minimize and gate access | Privacy note |
| DATACAP06 | Source diversity | Are enough source types represented? | Add missing source class if needed | Source coverage |
| DATACAP07 | Source reliability | Are sources authoritative? | Rank sources by reliability | Reliability note |
| DATACAP08 | Data transform load | How costly are transformations? | Automate repeated transforms | Transform plan |
| DATACAP09 | Data storage | Where are data/artifacts kept? | Define storage and retention | Storage plan |
| DATACAP10 | Data access continuity | Will data remain accessible later? | Archive or record access path | Access continuity |

## INFR Infrastructure Capacity

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| INFR01 | Compute capacity | Does task need significant CPU/GPU/runtime? | Estimate and choose environment | Compute note |
| INFR02 | Storage capacity | Are files/artifacts too large? | Check size and retention | Storage note |
| INFR03 | Network capacity | Does workflow depend on network/API? | Add offline fallback or retry | Network plan |
| INFR04 | Runtime capacity | Is required runtime installed/configured? | Validate before execution | Runtime check |
| INFR05 | Environment isolation | Could work affect active systems? | Use scoped workspace/safe paths | Isolation note |
| INFR06 | Concurrency capacity | Can multiple runs happen safely? | Add locks/idempotency if needed | Concurrency rule |
| INFR07 | Deployment capacity | Can release infrastructure handle change? | Check deploy/rollback readiness | Deployment note |
| INFR08 | Monitoring capacity | Can workflow status be observed? | Add logs/metrics/alerts | Monitoring setup |
| INFR09 | Backup capacity | Can state be restored? | Add backup/snapshot for risky change | Backup note |
| INFR10 | Portability capacity | Can workflow run elsewhere? | Record dependencies and versions | Portability note |

## LOAD Workload / Volume Capacity

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| LOAD01 | Single-item load | Is this a one-off task? | Keep workflow lightweight | Single-run note |
| LOAD02 | Small batch load | Are there several similar items? | Use manifest and sample QA | Small batch manifest |
| LOAD03 | Large batch load | Are there many items? | Automate, chunk, and track failures | Large batch plan |
| LOAD04 | Continuous load | Does work arrive constantly? | Add queue, cadence, and SLA | Queue plan |
| LOAD05 | Burst load | Does volume spike unpredictably? | Define surge handling | Burst plan |
| LOAD06 | Mixed load | Items vary in complexity | Segment by type/risk | Segmentation note |
| LOAD07 | Review load | Too many outputs need review | Sample or tier review by risk | Review load plan |
| LOAD08 | Error load | Too many failures appear | Categorize and prioritize errors | Error queue |
| LOAD09 | Maintenance load | Many templates/workflows need upkeep | Prune and assign owners | Maintenance backlog |
| LOAD10 | Library load | Prompt/workflow library grows large | Improve taxonomy/search | Library capacity |

## BOT Bottleneck Capacity

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| BOT01 | Intake bottleneck | Requests pile up before routing | Standardize intake and triage | Intake queue |
| BOT02 | Source bottleneck | Work waits for sources/data | Prebuild source inventory/fallback | Source wait note |
| BOT03 | Review bottleneck | Human review delays closeout | Risk-tier review or add reviewers | Review bottleneck |
| BOT04 | Approval bottleneck | Signoff blocks release | Define approver backup/criteria | Approval wait |
| BOT05 | Tool bottleneck | Tool rate/availability limits throughput | Batch, queue, or choose fallback | Tool bottleneck |
| BOT06 | QA bottleneck | Verification takes too long | Automate checks or sample | QA bottleneck |
| BOT07 | Handoff bottleneck | Work waits between roles | Add handoff packet and SLA | Handoff wait |
| BOT08 | Decision bottleneck | Options stall without owner | Assign decision owner and criteria | Decision wait |
| BOT09 | Rework bottleneck | Same failures recur | Add failure-mode prevention | Rework trend |
| BOT10 | Context bottleneck | Agent/user repeatedly rebuilds state | Add context memory/index | Context rebuild time |

## SCHED Scheduling Capacity

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| SCHED01 | Phase schedule | When does each phase start/end? | Map phase dates and gates | Phase schedule |
| SCHED02 | Dependency schedule | Which tasks wait on others? | Schedule upstream first | Dependency schedule |
| SCHED03 | Review schedule | When can review happen? | Reserve review slots | Review calendar |
| SCHED04 | Approval schedule | When is approval needed? | Send packet before deadline | Approval calendar |
| SCHED05 | Batch schedule | When should batch run? | Use window or volume trigger | Batch schedule |
| SCHED06 | Refresh schedule | When should data/source refresh? | Align with freshness need | Refresh calendar |
| SCHED07 | Maintenance schedule | When should workflow/template be updated? | Assign cadence and owner | Maintenance schedule |
| SCHED08 | Communication schedule | When should status updates happen? | Set reporting cadence | Comms calendar |
| SCHED09 | Launch schedule | When is release/publish/go-live? | Include readiness and rollback gates | Launch schedule |
| SCHED10 | Retirement schedule | When should workflow/artifact be archived? | Define retirement trigger | Retirement schedule |

## CONSTRAINT Resource Constraints

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| CONSTRAINT01 | Time constraint | What cannot fit in time? | Reduce scope or degrade output | Time tradeoff |
| CONSTRAINT02 | Budget constraint | What cannot fit in budget? | Prioritize high-value work | Budget tradeoff |
| CONSTRAINT03 | Skill constraint | What expertise is missing? | Add SME/review or caveat | Skill gap note |
| CONSTRAINT04 | Tool constraint | What tool capability is absent? | Use fallback/manual route | Tool gap note |
| CONSTRAINT05 | Data constraint | What data/source is unavailable? | Use proxy, request, or caveat | Data gap note |
| CONSTRAINT06 | Policy constraint | What rules limit action? | Add governance route | Policy note |
| CONSTRAINT07 | Access constraint | What permission is missing? | Request access or use safe subset | Access gap |
| CONSTRAINT08 | Scale constraint | What breaks at higher volume? | Batch/chunk/automate | Scale note |
| CONSTRAINT09 | Quality constraint | What quality bar cannot be met? | State limits and next needed resource | Quality gap |
| CONSTRAINT10 | Coordination constraint | What people/process dependency blocks work? | Add owner/escalation | Coordination note |

## ALLOC Allocation Decisions

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| ALLOC01 | Allocate effort | Where should effort go first? | Put effort on highest impact/risk bottleneck | Effort allocation |
| ALLOC02 | Allocate review | What needs human review? | Review high-risk/high-uncertainty output | Review allocation |
| ALLOC03 | Allocate automation | What should be automated? | Automate repeatable stable steps | Automation allocation |
| ALLOC04 | Allocate QA | What needs deepest checks? | QA critical and failure-prone steps | QA allocation |
| ALLOC05 | Allocate budget | What spend creates most value? | Fund high-value/risk-reduction items | Budget allocation |
| ALLOC06 | Allocate tools | Which tasks get specialized tools? | Match tool cost/capability to need | Tool allocation |
| ALLOC07 | Allocate experts | Where are SMEs necessary? | Use SMEs at material decisions/gates | SME allocation |
| ALLOC08 | Allocate data work | Where to clean/validate data? | Focus on downstream-critical fields | Data allocation |
| ALLOC09 | Allocate communication | Who needs updates and when? | Inform affected stakeholders at gates | Comms allocation |
| ALLOC10 | Allocate maintenance | Which artifacts need upkeep? | Maintain high-use/high-risk items first | Maintenance allocation |

## FEAS Feasibility Checks

| Code | Resource type | Planning question | Allocation rule | Evidence |
|---|---|---|---|---|
| FEAS01 | Scope feasible | Can scope be completed with available resources? | Match scope to time/capacity | Feasibility note |
| FEAS02 | Schedule feasible | Can timeline absorb dependencies/review? | Add buffer or reduce scope | Schedule check |
| FEAS03 | Technical feasible | Can tools/runtime support execution? | Validate small run | Technical check |
| FEAS04 | Data feasible | Are sources/data sufficient? | Check availability, quality, freshness | Data feasibility |
| FEAS05 | Review feasible | Can reviewers approve in time? | Confirm reviewer capacity | Review feasibility |
| FEAS06 | Cost feasible | Does budget cover chosen path? | Estimate and gate | Cost feasibility |
| FEAS07 | Compliance feasible | Can workflow meet rules? | Add compliance review | Compliance feasibility |
| FEAS08 | Scale feasible | Can workflow handle expected volume? | Test or estimate throughput | Scale feasibility |
| FEAS09 | Maintenance feasible | Can artifact stay current? | Assign owner/cadence | Maintenance feasibility |
| FEAS10 | User feasible | Can target user actually execute/use it? | Simplify or add training | User feasibility |
