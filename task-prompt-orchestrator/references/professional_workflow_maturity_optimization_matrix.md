# Professional Workflow Maturity and Optimization Matrix

Use this when improving a workflow from ad hoc execution toward repeatable, scalable, monitored, governed, and continuously improving operation. Maturity codes help decide the next upgrade rather than adding complexity blindly.

Selection rule:

1. Identify the current maturity gap: reliability, speed, quality, scale, governance, cost, user experience, or reuse.
2. Select the closest maturity/optimization code.
3. Add the target improvement, evidence metric, and next upgrade action to the workflow packet.
4. Validate that the upgrade reduces real friction or risk instead of adding ceremony.

## ADHM Ad Hoc to Defined

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| ADHM01 | Capture repeatable goal | Same request is re-explained each time | Create reusable brief template | Brief reused |
| ADHM02 | Define minimum inputs | Work starts with inconsistent context | Add required input checklist | Missing inputs drop |
| ADHM03 | Define output standard | Deliverables vary by run | Add output schema or sample | Output consistency |
| ADHM04 | Define done criteria | Completion is subjective | Add acceptance criteria | Done test exists |
| ADHM05 | Define owner | Work depends on whoever notices | Assign accountable owner | Owner visible |
| ADHM06 | Define source rule | Evidence gathered differently each time | Add source inventory rule | Source trace |
| ADHM07 | Define QA rule | Review is optional or inconsistent | Add QA checklist | QA evidence |
| ADHM08 | Define handoff | Receiver repeatedly asks what next | Add handoff packet | Fewer follow-up gaps |
| ADHM09 | Define archive path | Prior work is hard to find | Add index/archive entry | Retrieval works |
| ADHM10 | Define escalation | Blockers linger without owner | Add escalation trigger | Blockers routed |

## REPM Repeatability

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| REPM01 | Reusable workflow template | Similar tasks rebuilt manually | Extract trigger, steps, artifacts, QA | Template reused |
| REPM02 | Reusable prompt packet | Prompt rewritten from scratch | Add variables, defaults, tests | Prompt reuse |
| REPM03 | Reusable checklist | Review misses vary by reviewer | Standardize criteria | Checklist pass rate |
| REPM04 | Reusable naming | Files/outputs hard to compare | Add naming convention | Names consistent |
| REPM05 | Reusable batch manifest | Bulk work loses item status | Standardize manifest | Item status trace |
| REPM06 | Reusable source ledger | Citations/sources recreated | Maintain source ledger | Source reuse |
| REPM07 | Reusable runbook | Execution steps depend on memory | Write runbook | Runbook followed |
| REPM08 | Reusable handoff | Transfers vary by person | Standardize handoff fields | Handoff completeness |
| REPM09 | Reusable QA pack | Verification repeats manually | Package validators/checks | QA repeatability |
| REPM10 | Reusable index taxonomy | Library grows without findability | Add category/tag rules | Search success |

## STDM Standardization

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| STDM01 | Standard intake | Different teams ask different questions | Standardize intake fields | Intake completeness |
| STDM02 | Standard workflow phases | Phase names/order drift | Define phase model | Phase consistency |
| STDM03 | Standard roles | Responsibility differs by run | Apply role/RACI matrix | Role clarity |
| STDM04 | Standard gates | Approvals happen unpredictably | Define gate criteria | Gate logs |
| STDM05 | Standard artifact set | Deliverables omit key evidence | Require artifact contract | Artifact presence |
| STDM06 | Standard data definitions | Metrics differ by report | Define metric dictionary | Metric consistency |
| STDM07 | Standard visual specs | Image/design/CAD outputs drift | Define production specs | Spec adherence |
| STDM08 | Standard risk treatment | Similar risks handled differently | Define risk routes | Risk consistency |
| STDM09 | Standard closeout | Final responses omit checks/risks | Define closeout template | Closeout quality |
| STDM10 | Standard reuse path | Good work is not converted to templates | Define reuse extraction step | Template growth |

## AUTM Automation

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| AUTM01 | Automate intake parsing | Manual sorting of repeated requests | Parse into brief fields | Intake speed |
| AUTM02 | Automate source inventory | Source lists built manually | Generate source ledger | Source coverage |
| AUTM03 | Automate batch processing | Many similar items handled one by one | Use manifest-driven execution | Throughput |
| AUTM04 | Automate validation | Checks are manual and skipped | Add validator/script/test | Validation rate |
| AUTM05 | Automate formatting | Output formatting consumes time | Generate schema/template output | Format pass |
| AUTM06 | Automate indexing | Library entries added inconsistently | Generate index rows | Index freshness |
| AUTM07 | Automate notifications | Status updates missed | Trigger status/handoff messages | Timely updates |
| AUTM08 | Automate monitoring | Issues found late | Add threshold or freshness monitor | Detection time |
| AUTM09 | Automate retry | Transient failures require manual rerun | Add retry/failure queue | Recovery rate |
| AUTM10 | Automate archive | Final artifacts scattered | Package and archive outputs | Archive completeness |

## MONM Monitoring and Observability

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| MONM01 | Track progress | Users ask what is done | Add progress metric/status | Progress visible |
| MONM02 | Track quality | Defects discovered after delivery | Add QA score trend | Quality trend |
| MONM03 | Track cycle time | Work feels slow but cause unknown | Measure phase durations | Bottleneck found |
| MONM04 | Track throughput | Batch capacity unknown | Count items per window | Throughput known |
| MONM05 | Track failure rate | Failures feel anecdotal | Categorize failure modes | Failure trend |
| MONM06 | Track source freshness | Stale data enters outputs | Monitor source age | Freshness status |
| MONM07 | Track cost | Automation/tool use cost unknown | Add cost metric | Cost visible |
| MONM08 | Track adoption | Reusable workflows may not be used | Count usage and searches | Adoption trend |
| MONM09 | Track handoff success | Receivers still ask clarifying questions | Measure handoff rework | Handoff quality |
| MONM10 | Track outcome | Workflow activity not tied to result | Define outcome metric | Outcome trend |

## GOVM Governance

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| GOVM01 | Add policy boundary | Workflow may violate rules unknowingly | Add policy/risk route | Boundary visible |
| GOVM02 | Add approval gate | High-impact outputs ship unchecked | Add approver and criteria | Approval log |
| GOVM03 | Add audit trail | Decisions cannot be reconstructed | Preserve evidence and decisions | Audit trail |
| GOVM04 | Add privacy control | Sensitive data copied too broadly | Add minimization/redaction | Privacy evidence |
| GOVM05 | Add security control | Secrets/access risks not checked | Add security review | Security evidence |
| GOVM06 | Add compliance review | Regulated claims lack review | Add compliance packet | Compliance signoff |
| GOVM07 | Add change control | Process changes silently | Add changelog/versioning | Change record |
| GOVM08 | Add exception policy | Bypasses occur informally | Add exception approver | Exception log |
| GOVM09 | Add retention rule | Artifacts kept/deleted arbitrarily | Define keep/delete policy | Retention note |
| GOVM10 | Add accountability review | Owners exist but are not accountable | Review RACI and closeout | Accountability proof |

## SCAM Scalability

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| SCAM01 | Scale item volume | Manual steps break at higher count | Batch and manifest workflow | Larger batch passes |
| SCAM02 | Scale complexity | More branches make workflow confusing | Modularize phases and decision trees | Branch clarity |
| SCAM03 | Scale teams | Multiple people duplicate or conflict | Add roles and handoff contracts | Fewer collisions |
| SCAM04 | Scale domains | Same workflow reused across verticals poorly | Add domain adapter fields | Domain fit |
| SCAM05 | Scale channels | Output must support multiple formats | Add media/deliverable routing | Channel variants |
| SCAM06 | Scale languages/locales | Localization inconsistent | Add locale workflow | Locale QA |
| SCAM07 | Scale tools | Toolchain changes by environment | Add tool abstraction/fallbacks | Tool portability |
| SCAM08 | Scale data size | Manual inspection no longer works | Add sampling/profiling/automation | Data scale handled |
| SCAM09 | Scale approvals | Review bottleneck grows | Add risk-tiered approvals | Approval time |
| SCAM10 | Scale library | Prompt/workflow library becomes hard to search | Improve taxonomy/index | Search success |

## MATRES Resilience

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| MATRES01 | Add fallback path | One missing input stops all work | Define fallback output | Fallback used |
| MATRES02 | Add rollback | Bad change cannot be undone | Define rollback artifact/path | Rollback possible |
| MATRES03 | Add retry policy | Temporary failures require manual recovery | Add retry limits | Retry success |
| MATRES04 | Add degraded mode | No partial value when ideal path fails | Define reduced output | Degraded delivery |
| MATRES05 | Add checkpointing | Interruption loses progress | Save state and artifacts | Resume works |
| MATRES06 | Add conflict resolution | Contradictory sources/instructions stall | Define conflict owner/rule | Conflict resolved |
| MATRES07 | Add exception queue | Failed items disappear | Track exceptions | Exception status |
| MATRES08 | Add incident path | Severe failure lacks communication | Add incident runbook | Incident handled |
| MATRES09 | Add dependency fallback | External systems block workflow | Add alternate dependency path | Dependency resilience |
| MATRES10 | Add recovery review | Same failure repeats | Add lessons/control update | Repeat failures drop |

## REUM Reuse and Knowledge Capture

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| REUM01 | Extract template | Good one-off output likely recurs | Convert to template | Template entry |
| REUM02 | Extract examples | Users need concrete pattern | Store good input/output examples | Example coverage |
| REUM03 | Extract variables | Prompt hardcoded to one case | Parameterize prompt/workflow | Variable list |
| REUM04 | Extract checklist | Review insights not reused | Convert findings to checklist | Checklist update |
| REUM05 | Extract failure lesson | Failure fixed but not prevented | Add failure-mode control | Control update |
| REUM06 | Extract domain adapter | Workflow useful in a vertical | Add domain-specific route | Adapter entry |
| REUM07 | Extract artifact pattern | Useful deliverable structure repeats | Add artifact contract template | Artifact template |
| REUM08 | Extract automation candidate | Repeated manual steps found | Mark automation opportunity | Automation backlog |
| REUM09 | Extract index metadata | Asset exists but hard to discover | Add tags/category/summary | Searchable index |
| REUM10 | Extract maintenance rule | Reusable item may become stale | Add owner/cadence | Maintenance rule |

## LEARNM Continuous Learning

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| LEARNM01 | Capture user corrections | Same preference correction repeats | Add rule/template update | Correction decreases |
| LEARNM02 | Capture reviewer findings | Same QA issue repeats | Update checklist or prompt | Finding trend |
| LEARNM03 | Capture outcome feedback | Workflow success unknown | Add post-delivery feedback loop | Outcome data |
| LEARNM04 | Capture benchmark cases | Quality cannot be compared over time | Keep representative test cases | Benchmark set |
| LEARNM05 | Capture prompt failures | Prompt brittle across inputs | Add failure examples/tests | Prompt robustness |
| LEARNM06 | Capture source gaps | Research misses known source types | Update source rules | Source coverage |
| LEARNM07 | Capture domain nuance | Generic workflow misses expert nuance | Add domain note/adapter | Domain fit |
| LEARNM08 | Capture operational metrics | Process improvement guesses lack data | Use observability metrics | Metric-backed change |
| LEARNM09 | Capture deprecation | Old patterns remain in use | Mark outdated route | Deprecated item |
| LEARNM10 | Capture next experiment | Improvement idea untested | Define experiment and success metric | Experiment result |

## COSTM Cost / Efficiency

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| COSTM01 | Reduce unnecessary clarification | Too many questions slow progress | Use assumption rules | Cycle time drops |
| COSTM02 | Reduce repeated discovery | Same files/sources re-read each run | Cache source inventories | Discovery time drops |
| COSTM03 | Reduce manual QA | Review takes too long | Automate or template checks | QA time drops |
| COSTM04 | Reduce rework | Outputs rejected late | Move acceptance criteria earlier | Rework rate drops |
| COSTM05 | Reduce tool cost | Expensive tools used on low-value steps | Route by value/risk | Cost per run drops |
| COSTM06 | Reduce context bloat | Too many references loaded | Use dimension index routing | Context smaller |
| COSTM07 | Reduce handoff friction | Receivers ask repeated questions | Improve handoff packet | Follow-ups drop |
| COSTM08 | Reduce batch waste | Failed bulk items require full rerun | Retry failed items only | Rerun cost drops |
| COSTM09 | Reduce approval bottleneck | Low-risk work waits unnecessarily | Risk-tier approval | Approval time drops |
| COSTM10 | Reduce maintenance burden | Too many templates become stale | Add ownership and pruning | Stale items drop |

## UXM User Experience

| Code | Upgrade | Current symptom | Improvement action | Evidence |
|---|---|---|---|---|
| UXM01 | Make next action obvious | User unsure what to do | Add next-action handoff | User can act |
| UXM02 | Reduce cognitive load | Workflow explanation overwhelms user | Provide minimal packet first | User comprehension |
| UXM03 | Improve transparency | User cannot tell what was done | Add concise evidence summary | Trust/clarity |
| UXM04 | Improve controllability | User cannot steer process | Add decision points and defaults | Fewer misroutes |
| UXM05 | Improve recoverability | Mistakes feel hard to fix | Add rollback/rework path | Recovery ease |
| UXM06 | Improve discoverability | Library/workflow hard to browse | Add index/tags/examples | Search success |
| UXM07 | Improve confidence | User doubts output quality | Show checks, caveats, and evidence | Confidence signal |
| UXM08 | Improve handoff readability | Final answer too dense | Separate outcome, files, verification | Readability |
| UXM09 | Improve beginner fit | Novice user lacks workflow mental model | Add guided workflow packet | Beginner success |
| UXM10 | Improve professional fit | Expert user needs concise rigor | Provide codes, evidence, and criteria | Expert acceptance |

