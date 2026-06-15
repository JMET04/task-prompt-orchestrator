# Professional Workflow Failure Mode Matrix

Use this when auditing, debugging, hardening, or stress-testing a workflow. Failure modes identify where a workflow breaks, what evidence reveals the break, and what repair action should be added.

Selection rule:

1. Identify the phase or interface where the workflow is weak.
2. Select the closest failure-mode code.
3. Add detection evidence and repair action to the workflow packet.
4. Re-run relevant QA or state transition checks after repair.

## FMINT Failure: Intake

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FMINT01 | Ambiguous goal | Output cannot be judged as done | Rewrite goal as testable brief | Goal brief required |
| FMINT02 | Missing audience | Tone, depth, or format drifts | Add audience and use case | Audience field |
| FMINT03 | Hidden constraint | Late rejection due to unspoken limit | Add constraint capture step | Constraint brief |
| FMINT04 | Scope creep | Work expands without boundary | Define in/out scope | Scope boundary |
| FMINT05 | Wrong urgency | Slow work on urgent task or rushed deep work | Add urgency and deadline | Time-aware intake |
| FMINT06 | Conflicting instructions | Steps satisfy one instruction and violate another | Resolve priority or ask | Scope conflict check |
| FMINT07 | Over-clarification | Progress stalls on nonblocking questions | Proceed with safe assumptions | Clarification threshold |
| FMINT08 | Under-clarification | Unsafe assumption changes output materially | Ask one blocking question | Blocker test |
| FMINT09 | Wrong workflow family | Process does not fit user intent | Re-route to base P-code | Workflow selection gate |
| FMINT10 | No success criteria | Completion is subjective and unstable | Add acceptance criteria | Success criteria brief |

## FSRC Failure: Sources

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FSRC01 | Missing source | Critical claim/input has no source | Request, search, or caveat | Source inventory |
| FSRC02 | Stale source | Date/version is old or unknown | Refresh or state freshness limit | Freshness check |
| FSRC03 | Low-quality source | OCR/noisy/secondary source reduces confidence | Mark uncertainty and verify critical facts | Source quality note |
| FSRC04 | Source conflict | Sources disagree without resolution | Create conflict map | Conflict rule |
| FSRC05 | Overtrusted source | Single weak source drives conclusion | Add corroboration requirement | Evidence threshold |
| FSRC06 | Untraceable claim | Claim cannot be linked to evidence | Remove, cite, or downgrade claim | Evidence table |
| FSRC07 | Missing citation closure | Bibliography/source exists but claim link is unclear | Link claims to citations | Citation ledger |
| FSRC08 | Source access loss | File/link/API becomes unavailable | Store source status and fallback | Access check |
| FSRC09 | Sensitive source exposure | Private/regulated data is copied unnecessarily | Redact and minimize | Data handling brief |
| FSRC10 | Source set drift | New material changes answer after synthesis | Lock source set or rerun synthesis | Source lock |

## FPLAN Failure: Planning

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FPLAN01 | No plan for complex work | Steps are improvised and inconsistent | Add phased plan | Plan threshold |
| FPLAN02 | Plan too broad | Steps are vague and not executable | Split into atomic actions | WBS contract |
| FPLAN03 | Wrong dependency order | Later step lacks upstream output | Add dependency map | Sequence check |
| FPLAN04 | Missing branch | Workflow fails when condition changes | Add decision tree | Branch coverage |
| FPLAN05 | Missing fallback | Tool/source/path failure stops work | Add fallback path | Fallback control |
| FPLAN06 | Missing QA plan | Defects discovered only after delivery | Define checks before execution | QA-first plan |
| FPLAN07 | No owner | Step waits because responsibility is unclear | Assign role/RACI | Ownership map |
| FPLAN08 | No stop condition | Workflow loops or expands indefinitely | Add exit criteria | Stop rule |
| FPLAN09 | Unbounded batch | Bulk work lacks manifest or limit | Add batch manifest | Batch plan |
| FPLAN10 | Non-resumable plan | Interruption loses state | Add resume packet | Resume-safe plan |

## FEXEC Failure: Execution

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FEXEC01 | Step skipped | Required artifact is absent | Return to missing step | Artifact gate |
| FEXEC02 | Wrong execution mode | Automation/HITL/batch choice mismatches risk | Re-select execution mode | Mode routing |
| FEXEC03 | Uncaptured assumption | Output depends on hidden guess | Add assumption ledger | Assumption note |
| FEXEC04 | Partial output mistaken as final | Missing sections or items delivered as complete | Mark partial and continue | Completeness check |
| FEXEC05 | Unlogged action | No evidence of what was run/changed | Add action/change log | Logging contract |
| FEXEC06 | Unscoped edit | Work touches unrelated files/artifacts | Re-scope and review changes | Scope guard |
| FEXEC07 | Repetition inconsistency | Repeated items handled differently | Add template or batch rule | Batch standard |
| FEXEC08 | Context loss | Execution ignores prior decisions | Rebuild current-state note | Resume check |
| FEXEC09 | Over-generation | Output adds unsupported extras | Trim to brief and evidence | Output spec |
| FEXEC10 | Under-generation | Output lacks expected detail | Expand against acceptance criteria | Coverage check |

## FTOOL Failure: Tools

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FTOOL01 | Tool unavailable | Command/API/app missing or inaccessible | Use fallback or block with evidence | Tool readiness |
| FTOOL02 | Wrong tool | Output format or capability mismatches task | Re-route to suitable tool | Tool selection |
| FTOOL03 | Tool output unverified | Tool result accepted without check | Validate or sample output | Tool QA |
| FTOOL04 | Parameter error | Tool runs with wrong path/input/options | Re-run with corrected parameters | Parameter contract |
| FTOOL05 | Silent truncation | Output incomplete without visible failure | Inspect boundaries and counts | Completeness check |
| FTOOL06 | Environment mismatch | Command works in one env but not another | Record env/version | Environment note |
| FTOOL07 | Credential/access issue | Permission failure blocks tool | Request access or use safe fallback | Access check |
| FTOOL08 | Destructive tool risk | Command could delete/overwrite risky state | Add preview, backup, or confirmation | Destructive gate |
| FTOOL09 | Tool hallucination/proxy gap | Tool result does not prove claimed fact | Inspect authoritative output | Evidence discipline |
| FTOOL10 | No reproducibility | Tool run cannot be repeated | Record command, inputs, versions | Run log |

## FHUM Failure: Human Collaboration

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FHUM01 | Reviewer unclear | Feedback has no accountable reviewer | Name reviewer and criteria | Review schedule |
| FHUM02 | Approval unclear | Work waits for undefined signoff | Name approver and decision options | Approval packet |
| FHUM03 | Feedback ambiguous | Comment cannot be converted to change | Ask targeted clarification | Comment resolution |
| FHUM04 | Stakeholder conflict | Different people want incompatible outcomes | Add decision owner | Escalation owner |
| FHUM05 | Late stakeholder input | New input invalidates completed work | Assess impact and rebase plan | Change control |
| FHUM06 | Human overload | Too many decisions pushed to user | Bundle choices and recommend default | Decision packet |
| FHUM07 | Missing SME | Domain correctness cannot be validated | Prepare SME review packet | SME gate |
| FHUM08 | Untracked approval | Signoff exists only in conversation memory | Record approval log | Approval record |
| FHUM09 | No handoff receiver | Output has nowhere to go next | Assign downstream owner | Handoff map |
| FHUM10 | Misaligned expectation | User expected action, got only plan or vice versa | Re-read request and execute/plan accordingly | Intent check |

## FQA Failure: Quality Assurance

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FQA01 | No QA evidence | Final answer lacks checks/tests | Run or state skipped checks | QA checklist |
| FQA02 | Narrow test overclaims | Test covers small slice but claim is broad | Limit claim or add tests | Coverage mapping |
| FQA03 | Format failure | Output violates requested schema/file format | Repair format and validate | Schema check |
| FQA04 | Consistency failure | Terms, numbers, or decisions conflict | Reconcile across artifacts | Consistency check |
| FQA05 | Visual defect | Image/UI/CAD prompt misses visible requirement | Add visual QA or reference invariant | Visual QA |
| FQA06 | Unsupported recommendation | Advice lacks criteria or evidence | Add rationale and caveats | Decision evidence |
| FQA07 | Missing edge cases | Workflow only handles happy path | Add branch/fallback cases | Edge-case checklist |
| FQA08 | No acceptance mapping | Output not mapped to user requirements | Create acceptance table | Acceptance criteria |
| FQA09 | No regression check | New route may break existing use | Run route/count validation | Regression note |
| FQA10 | QA not rerun after fix | Repair made but stale QA cited | Re-run current checks | Fresh validation |

## FRISK Failure: Risk / Governance

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FRISK01 | Risk not identified | High-impact area lacks risk note | Add risk gate | Risk intake |
| FRISK02 | Residual risk hidden | Caveats omitted from delivery | Add residual risk closeout | Risk disclosure |
| FRISK03 | Compliance bypass | Regulated output skips approval | Add compliance gate | Governed mode |
| FRISK04 | Privacy leak | Sensitive data appears in output/logs | Redact and minimize | Privacy IO contract |
| FRISK05 | Security exposure | Secrets, exploit paths, or access risks appear | Remove unsafe detail and review | Security gate |
| FRISK06 | Financial assumption hidden | Numbers rely on unstated assumptions | Add assumption note | Finance review |
| FRISK07 | Legal ambiguity | Jurisdiction/rule unknown | Caveat and escalate | Legal caveat |
| FRISK08 | IP/license issue | Asset/source rights unclear | Check rights or replace asset | IP note |
| FRISK09 | Public claim risk | Marketing/public claim lacks proof | Add substantiation or remove | Claim review |
| FRISK10 | Safety stop missed | Physical/user safety risk continues | Stop and reroute | Safety stop card |

## FDATA Failure: Data / Metrics

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FDATA01 | Unknown grain | Rows/metrics cannot be interpreted | Define grain | Data context |
| FDATA02 | Bad join/key | Counts duplicate or drop records | Validate joins and keys | Join check |
| FDATA03 | Missing data quality check | Nulls/duplicates/outliers unnoticed | Profile data | Data QA |
| FDATA04 | Metric definition drift | Same metric means different things | Create metric definition | Metric dictionary |
| FDATA05 | Denominator missing | Rate/percentage lacks base | Add denominator | Metric contract |
| FDATA06 | Timezone/window error | Time analysis misaligned | Define timezone/window | Time contract |
| FDATA07 | Sample bias | Dataset not representative | State sample caveat | Sample note |
| FDATA08 | Transformation untracked | Cleaned data cannot be traced | Record transform steps | Provenance note |
| FDATA09 | Visualization mismatch | Chart implies wrong relationship | Fix encoding/labels | Chart QA |
| FDATA10 | Data output not reusable | Table lacks columns needed downstream | Add downstream fields | IO contract |

## FHAND Failure: Handoff

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FHAND01 | Missing next action | Receiver does not know what to do | Add exact next step | Handoff contract |
| FHAND02 | Missing artifact location | Output exists but cannot be found | Add path/link/index | Delivery summary |
| FHAND03 | Missing limitations | Receiver assumes output is stronger than it is | Add limitations/caveats | Handoff note |
| FHAND04 | Missing owner | Follow-up action has no assignee | Assign owner | RACI map |
| FHAND05 | Missing context | Receiver cannot resume without prior decisions | Add context brief | Resume packet |
| FHAND06 | Wrong audience handoff | Technical detail given to nontechnical user or reverse | Reframe handoff | Audience route |
| FHAND07 | No review trail | Receiver cannot verify quality | Attach QA/evidence | QA handoff |
| FHAND08 | No archive/index | Reusable work is lost | Add archive/index entry | Archive contract |
| FHAND09 | Handoff too verbose | Receiver cannot identify action | Summarize decision and next action | Handoff template |
| FHAND10 | Handoff before ready | Output transferred without required gates | Return to QA/approval | Readiness check |

## FAUTO Failure: Automation

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FAUTO01 | Wrong trigger | Automation runs too early/late/often | Adjust trigger rule | Trigger matrix |
| FAUTO02 | No idempotency | Re-run duplicates or corrupts output | Add idempotency key/check | Idempotency rule |
| FAUTO03 | No retry policy | Temporary failure stops process | Add bounded retry | Retry rule |
| FAUTO04 | No dead-letter path | Failed items disappear or block queue | Add failure queue/log | Exception handling |
| FAUTO05 | No monitoring | Automation fails silently | Add metrics/alerts | Observability |
| FAUTO06 | No manual override | Human cannot stop or adjust run | Add pause/resume/cancel controls | Manual control |
| FAUTO07 | No audit log | Automated decision cannot be inspected | Add audit trail | Logging contract |
| FAUTO08 | No access boundary | Automation sees or changes too much | Limit scope/permissions | Least privilege |
| FAUTO09 | No version control | Automation changes without trace | Version workflow/template | Version contract |
| FAUTO10 | Brittle prompt/template | Small input variation breaks output | Add schema, examples, tests | Template tests |

## FCLOSE Failure: Closure

| Code | Failure mode | Detection evidence | Repair action | Prevention |
|---|---|---|---|---|
| FCLOSE01 | Premature completion claim | Goal not fully verified | Reopen missing requirements | Completion audit |
| FCLOSE02 | No final summary | User cannot tell what changed | Add concise delivery summary | Closeout template |
| FCLOSE03 | Tests not reported | Verification happened but not disclosed | Report checks and skips | Verification summary |
| FCLOSE04 | Risks not reported | Residual risks missing from final | Add risk closeout | Risk disclosure |
| FCLOSE05 | Follow-up vague | Next step is optional or unclear | Name specific next action | Next-iteration note |
| FCLOSE06 | Goal status wrong | Active goal marked complete/blocked incorrectly | Re-audit objective | Goal audit |
| FCLOSE07 | Artifacts not indexed | Work exists but not discoverable | Update index/archive | Archive route |
| FCLOSE08 | Reuse not extracted | Useful workflow remains one-off | Extract template | Reuse contract |
| FCLOSE09 | Learning not captured | Repeated issue likely recurs | Add lesson/control | Lessons note |
| FCLOSE10 | Closure not honest | Final answer overstates certainty | Revise with evidence and limits | Evidence-based close |
