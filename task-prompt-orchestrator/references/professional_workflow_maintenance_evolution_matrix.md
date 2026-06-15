# Professional Workflow Maintenance and Evolution Matrix

Use this when a workflow, prompt template, index, automation, or operating process must remain useful over time. Maintenance and evolution rules prevent workflows from becoming stale, duplicated, unowned, unsafe, or impossible to migrate.

Selection rule:

1. Identify what may become stale, duplicated, unsupported, or misaligned over time.
2. Select the closest maintenance/evolution code.
3. Add owner, cadence, trigger, update action, and retirement rule to the prompt packet.
4. Prefer pruning and versioning over unbounded expansion.

## OWNM Ownership Maintenance

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| OWNM01 | Owner assignment | New workflow/template created | Assign accountable owner | Owner field |
| OWNM02 | Owner review | Owner missing or stale | Confirm or reassign owner | Owner update |
| OWNM03 | Backup owner | Primary owner unavailable | Name backup and handoff | Backup note |
| OWNM04 | Reviewer roster | Reviews bottleneck or expertise changes | Update reviewer list | Reviewer roster |
| OWNM05 | Approver roster | Approval path changes | Update approvers and criteria | Approval roster |
| OWNM06 | Maintainer capacity | Maintenance backlog grows | Allocate maintenance effort | Capacity note |
| OWNM07 | Stewardship boundary | Multiple owners conflict | Define stewardship scope | Stewardship map |
| OWNM08 | Escalation owner | Repeated unresolved issue | Assign escalation owner | Escalation map |
| OWNM09 | Archive owner | Artifact/workflow enters archive | Assign retrieval/retention owner | Archive owner |
| OWNM10 | Retirement owner | Workflow should be deprecated | Assign owner for migration/removal | Retirement owner |

## CADM Cadence Maintenance

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| CADM01 | Daily maintenance | High-change operational workflow | Run daily checks | Daily log |
| CADM02 | Weekly maintenance | Active library/process | Review additions, gaps, failures | Weekly review |
| CADM03 | Monthly maintenance | Stable but used workflow | Check freshness, owners, metrics | Monthly report |
| CADM04 | Quarterly maintenance | Governance/strategy workflow | Reassess risk, taxonomy, maturity | Quarterly review |
| CADM05 | Annual maintenance | Long-lived policy/template | Revalidate against current needs | Annual review |
| CADM06 | Event-driven maintenance | Source/tool/policy changes | Refresh affected workflows | Event update |
| CADM07 | Usage-driven maintenance | Usage crosses threshold | Improve high-use workflows | Usage review |
| CADM08 | Failure-driven maintenance | Same failure repeats | Add prevention/control | Failure update |
| CADM09 | Staleness-driven maintenance | Source/template age exceeds threshold | Refresh or deprecate | Staleness note |
| CADM10 | No-maintenance mode | Workflow is one-off/low-risk | Mark no recurring maintenance | No-maintenance note |

## DRIFTM Drift Detection

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| DRIFTM01 | Source drift | Source date/version changes | Refresh evidence and outputs | Source drift note |
| DRIFTM02 | Prompt drift | Prompt output quality changes | Re-benchmark and tune | Prompt benchmark |
| DRIFTM03 | Tool drift | Tool/API/model behavior changes | Revalidate integration | Tool drift note |
| DRIFTM04 | Schema drift | Input/output schema changes | Update IO contracts | Schema update |
| DRIFTM05 | Metric drift | Metric definition or denominator changes | Update metric dictionary | Metric update |
| DRIFTM06 | Audience drift | Target user/context changes | Update audience route | Audience update |
| DRIFTM07 | Policy drift | Legal/compliance/policy changes | Update governance gate | Policy update |
| DRIFTM08 | Taxonomy drift | Categories no longer fit library | Refactor tags/index | Taxonomy update |
| DRIFTM09 | Process drift | Operators stop following workflow | Retrain or simplify | Process audit |
| DRIFTM10 | Quality drift | QA scores decline over time | Investigate and repair | Quality trend |

## VERM Version Maintenance

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| VERM01 | Major version | Breaking workflow/template change | Increment major version and migration note | Major changelog |
| VERM02 | Minor version | Backward-compatible improvement | Increment minor version | Minor changelog |
| VERM03 | Patch version | Typo/clarity/fix only | Record patch | Patch note |
| VERM04 | Version snapshot | Significant release/archive | Save snapshot and retrieval path | Snapshot record |
| VERM05 | Version comparison | Need to choose old/new route | Compare metrics and compatibility | Version comparison |
| VERM06 | Version rollback | New version fails | Restore prior version | Rollback record |
| VERM07 | Version compatibility | Downstream depends on old format | Keep compatibility adapter | Compatibility note |
| VERM08 | Version annotation | Multiple variants coexist | Label intended use and limits | Variant note |
| VERM09 | Version approval | High-impact version change | Require reviewer/approver | Version approval |
| VERM10 | Version retirement | Old version should stop use | Mark deprecated and point replacement | Deprecation note |

## REFM Refresh Maintenance

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| REFM01 | Source refresh | Freshness threshold reached | Re-check sources | Source refresh log |
| REFM02 | Web/current refresh | Volatile public facts involved | Browse current sources | Currentness evidence |
| REFM03 | Data refresh | Dataset/source updated | Re-run data validation | Data refresh log |
| REFM04 | Index refresh | New/changed artifacts | Update index rows | Index update |
| REFM05 | Prompt refresh | Prompt underperforms or context changes | Tune and test prompt | Prompt refresh |
| REFM06 | Workflow refresh | User needs/process changes | Update steps/artifacts/roles | Workflow update |
| REFM07 | Risk refresh | Impact or regulation changes | Re-run risk gate | Risk refresh |
| REFM08 | Metric refresh | Measurement no longer useful | Replace metric | Metric refresh |
| REFM09 | Training refresh | Operators/users misunderstand process | Update training materials | Training update |
| REFM10 | Archive refresh | Archive metadata stale | Update retrieval/version/retention | Archive update |

## PRUNEM Pruning / Deduplication

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| PRUNEM01 | Duplicate prompt | Similar prompts overlap | Merge or mark distinction | Dedup note |
| PRUNEM02 | Duplicate workflow | Two workflows solve same case | Consolidate route | Workflow merge |
| PRUNEM03 | Low-use item | Template unused beyond threshold | Archive or simplify | Usage note |
| PRUNEM04 | Stale item | Source/tool/process obsolete | Deprecate or refresh | Staleness decision |
| PRUNEM05 | Overcomplex workflow | Ceremony exceeds value | Remove low-value steps | Simplification note |
| PRUNEM06 | Broken index entry | Link/path/category invalid | Repair or remove | Index repair |
| PRUNEM07 | Outdated examples | Examples no longer representative | Replace examples | Example update |
| PRUNEM08 | Redundant metric | Metric does not affect decisions | Remove or replace | Metric prune |
| PRUNEM09 | Redundant approval | Low-risk gate bottlenecks work | Risk-tier or remove gate | Approval prune |
| PRUNEM10 | Archive cleanup | Old artifacts clutter active library | Move to archive with manifest | Cleanup record |

## MIGM Migration

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| MIGM01 | Template migration | Old template schema changes | Map old fields to new fields | Migration map |
| MIGM02 | Workflow migration | Process model changes | Move active cases to new workflow | Workflow migration |
| MIGM03 | Index migration | Taxonomy/category system changes | Rewrite index rows | Index migration |
| MIGM04 | Tool migration | Tool/API replaced | Update integration and fallback | Tool migration |
| MIGM05 | Data migration | Source/storage/schema changes | Validate migrated data | Data migration |
| MIGM06 | Prompt migration | Prompt model/platform changes | Re-benchmark prompts | Prompt migration |
| MIGM07 | Automation migration | Scheduler/orchestrator changes | Test trigger/run/logs | Automation migration |
| MIGM08 | Governance migration | Policy/risk framework changes | Update gates and evidence | Governance migration |
| MIGM09 | Communication migration | Channel/audience changes | Update templates and owners | Comms migration |
| MIGM10 | Archive migration | Storage/retrieval changes | Verify package retrieval | Archive migration |

## DEPM Deprecation

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| DEPM01 | Deprecate prompt | Prompt outdated, unsafe, or superseded | Mark deprecated and link replacement | Prompt deprecation |
| DEPM02 | Deprecate workflow | Workflow no longer fits process | Mark deprecated and migrate cases | Workflow deprecation |
| DEPM03 | Deprecate source | Source unreliable/outdated | Remove from preferred source set | Source deprecation |
| DEPM04 | Deprecate metric | Metric misleading or unused | Replace or remove metric | Metric deprecation |
| DEPM05 | Deprecate tool | Tool unavailable/unsafe/obsolete | Update tool route | Tool deprecation |
| DEPM06 | Deprecate category | Taxonomy no longer useful | Merge/relabel category | Category deprecation |
| DEPM07 | Deprecate approval path | Approval owner/process invalid | Update gate | Approval deprecation |
| DEPM08 | Deprecate automation | Automation unsafe or low-value | Disable and preserve logs | Automation deprecation |
| DEPM09 | Deprecate artifact | Artifact should not be reused | Mark archived/retired | Artifact deprecation |
| DEPM10 | Deprecation notice | Users may still use old item | Communicate replacement/timeline | Deprecation notice |

## ARCHM Archive Maintenance

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| ARCHM01 | Archive final artifact | Work completed | Store final, sources, QA, version | Archive package |
| ARCHM02 | Archive source bundle | Sources support future audit | Store source list/status | Source archive |
| ARCHM03 | Archive decision log | Decisions matter later | Store rationale and date | Decision archive |
| ARCHM04 | Archive prompt/template | Reusable prompt released | Store variables/examples/tests | Template archive |
| ARCHM05 | Archive workflow version | Workflow version released | Store version and changelog | Workflow archive |
| ARCHM06 | Archive test results | Tests prove readiness | Store test plan/results | Test archive |
| ARCHM07 | Archive run logs | Automation/operations need audit | Store logs with retention | Run log archive |
| ARCHM08 | Archive deprecated item | Item retired but may be referenced | Store replacement and reason | Deprecated archive |
| ARCHM09 | Archive retrieval test | Archive findability matters | Retrieve package periodically | Retrieval proof |
| ARCHM10 | Archive retention review | Retention date reached | Keep/delete/migrate decision | Retention review |

## MONMAINT Monitoring Maintenance

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| MONMAINT01 | Monitor health | Workflow runs repeatedly | Track success/failure | Health report |
| MONMAINT02 | Monitor quality | Output quality may drift | Track QA metrics | Quality report |
| MONMAINT03 | Monitor usage | Library/template may be unused | Track adoption | Usage report |
| MONMAINT04 | Monitor cost | Tool/human cost may grow | Track cost metrics | Cost report |
| MONMAINT05 | Monitor risk | Risk state may change | Track open risks | Risk report |
| MONMAINT06 | Monitor freshness | Sources/templates may stale | Track age/freshness | Freshness report |
| MONMAINT07 | Monitor capacity | Workload may exceed resources | Track bottlenecks | Capacity report |
| MONMAINT08 | Monitor incidents | Failures may recur | Track incident/failure modes | Incident trend |
| MONMAINT09 | Monitor feedback | Users report friction | Track feedback themes | Feedback report |
| MONMAINT10 | Monitor outcomes | Activity may not produce value | Track outcome metrics | Outcome report |

## EVOM Evolution Roadmap

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| EVOM01 | Next improvement | Metrics/failures reveal opportunity | Add prioritized improvement | Roadmap item |
| EVOM02 | Automation candidate | Repeated stable manual step | Add automation backlog item | Automation candidate |
| EVOM03 | Governance upgrade | Risk/scale increases | Add stronger controls | Governance roadmap |
| EVOM04 | Scale upgrade | Volume/team/domain grows | Add scale plan | Scale roadmap |
| EVOM05 | UX upgrade | User friction persists | Improve handoff/training/interface | UX roadmap |
| EVOM06 | Quality upgrade | QA trend below target | Improve templates/checks/examples | Quality roadmap |
| EVOM07 | Integration upgrade | Manual transfer causes errors | Add integration/API/export | Integration roadmap |
| EVOM08 | Metrics upgrade | Current metrics weak | Add better decision-useful metric | Metrics roadmap |
| EVOM09 | Taxonomy upgrade | Library findability declines | Refactor category/tag system | Taxonomy roadmap |
| EVOM10 | Strategic upgrade | Workflow becomes core capability | Promote to maintained system | Strategy roadmap |

## RETM Retirement

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| RETM01 | Retire one-off workflow | No recurring value | Archive and mark closed | Retirement note |
| RETM02 | Retire outdated workflow | Replaced by better version | Deprecate and migrate users | Migration note |
| RETM03 | Retire risky workflow | Risk exceeds value | Disable and preserve evidence | Risk retirement |
| RETM04 | Retire unused template | Usage below threshold | Archive or delete by policy | Usage decision |
| RETM05 | Retire broken automation | Automation repeatedly fails | Disable trigger and document fallback | Automation retirement |
| RETM06 | Retire stale source route | Source no longer reliable | Remove from route/index | Source retirement |
| RETM07 | Retire old metric | Metric no longer useful | Remove from report and note replacement | Metric retirement |
| RETM08 | Retire duplicate category | Taxonomy overlap found | Merge category and update index | Category retirement |
| RETM09 | Retire project archive | Retention period ends | Keep/delete by rule | Retention action |
| RETM10 | Retire with lessons | Workflow ends but learning remains useful | Capture lessons and reusable parts | Lessons archive |

## KNOWM Knowledge Maintenance

| Code | Maintenance area | Trigger | Action | Evidence |
|---|---|---|---|---|
| KNOWM01 | Capture new rule | Repeated correction or insight | Add candidate rule/template | Rule note |
| KNOWM02 | Update domain note | Domain nuance changes | Refresh domain adapter | Domain update |
| KNOWM03 | Update examples | Better examples available | Replace/add examples | Example update |
| KNOWM04 | Update glossary | Terminology evolves | Refresh terms | Glossary update |
| KNOWM05 | Update source guide | Better source route found | Add source rule | Source guide |
| KNOWM06 | Update failure guide | New failure mode appears | Add failure/control | Failure guide |
| KNOWM07 | Update training | Users misunderstand workflow | Revise training note | Training update |
| KNOWM08 | Update FAQ | Repeated questions appear | Add answer/pattern | FAQ update |
| KNOWM09 | Update index aliases | Search misses occur | Add aliases/tags | Alias update |
| KNOWM10 | Update memory boundary | Persistent fact may be stale/sensitive | Refresh, caveat, or remove | Memory boundary note |
