# Professional Workflow Testing and Simulation Matrix

Use this when a workflow must be tested before broad execution, production release, automation, or handoff. Testing and simulation rules expose failure modes, quality gaps, capacity limits, and user misunderstandings before they become expensive.

Selection rule:

1. Identify what must be proven before the workflow is trusted.
2. Select the closest testing/simulation code.
3. Add test setup, sample, expected result, pass/fail rule, and follow-up action to the prompt packet.
4. Do not generalize from a narrow test unless the tested scope matches the claim.

## DRYT Dry Run Tests

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| DRYT01 | Manual dry run | Walk through workflow without external side effects | Every step has input/output | Fix missing steps |
| DRYT02 | Artifact dry run | Produce one representative artifact | Artifact meets format and QA | Update template |
| DRYT03 | Tool dry run | Run tool on safe sample input | Tool output matches expected schema | Adjust tool plan |
| DRYT04 | Handoff dry run | Give packet to receiver or reviewer | Receiver can identify next action | Improve handoff |
| DRYT05 | Approval dry run | Simulate approval packet | Approver can decide with evidence | Add missing evidence |
| DRYT06 | Automation dry run | Run automation in no-op/sandbox mode | Trigger/logs/output path correct | Fix automation |
| DRYT07 | Recovery dry run | Simulate known failure path | Recovery steps are clear | Add recovery control |
| DRYT08 | Communication dry run | Draft status/risk/decision message | Message is accurate and actionable | Refine comms |
| DRYT09 | Closeout dry run | Produce final response/checklist | Evidence and risks are included | Fix closeout |
| DRYT10 | Resume dry run | Resume from saved state | Next actor can continue | Improve memory packet |

## SAMT Sample / Pilot Tests

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| SAMT01 | Single sample test | Run one typical item | Expected output passes QA | Proceed to small batch |
| SAMT02 | Edge sample test | Run unusual/high-risk item | Edge case handled or routed | Add branch/fallback |
| SAMT03 | Stratified sample test | Pick samples by category/risk | All strata pass or issues categorized | Segment workflow |
| SAMT04 | Small batch pilot | Run limited batch with manifest | Failures below threshold | Scale or repair |
| SAMT05 | User pilot | Let target user try workflow/output | User can complete task | Improve UX/handoff |
| SAMT06 | Reviewer pilot | Have reviewer apply criteria | Findings are actionable | Improve rubric |
| SAMT07 | Client pilot | Test with controlled client/stakeholder case | Feedback supports rollout | Adjust client path |
| SAMT08 | Data sample pilot | Analyze subset of dataset | Logic and grain validate | Scale analysis |
| SAMT09 | Prompt sample pilot | Run prompt on representative examples | Outputs meet benchmark | Tune prompt |
| SAMT10 | Automation pilot | Run automation on limited safe scope | No unsafe side effects | Expand trigger/scope |

## REGT Regression Tests

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| REGT01 | Route regression | Existing routing examples still map correctly | No unintended route breaks | Repair routing |
| REGT02 | Template regression | Existing prompt/template examples still work | Output schema/quality preserved | Version template |
| REGT03 | Index regression | Existing index entries remain findable | Search/index fields valid | Fix taxonomy |
| REGT04 | Workflow regression | Existing workflow packet still assembles | Required fields preserved | Update dimension index |
| REGT05 | Artifact regression | Existing deliverable format unchanged | Downstream can consume output | Fix format |
| REGT06 | Tool regression | Tool/script still accepts expected inputs | Tool result unchanged or explained | Fix integration |
| REGT07 | Data regression | Metrics/results remain consistent after change | Variance explained | Fix data logic |
| REGT08 | Visual regression | Design/image output preserves required specs | Visual diffs acceptable | Fix prompt/spec |
| REGT09 | Governance regression | Risk/approval controls still fire | High-risk paths gated | Repair gate |
| REGT10 | Closeout regression | Final response still reports evidence/risks | Closeout fields present | Fix closeout template |

## LOADT Load / Stress Tests

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| LOADT01 | Volume test | Run larger item count | Throughput and failures within threshold | Tune batch size |
| LOADT02 | Concurrency test | Run parallel lanes/items | No collisions or duplicate side effects | Add locks/idempotency |
| LOADT03 | Long-context test | Use large source/context set | Critical info not lost | Add compression/index |
| LOADT04 | Large-file test | Process large file/media/dataset | No truncation and counts reconcile | Add chunking |
| LOADT05 | Rate-limit test | Exercise API/tool near limit | Throttling handled | Add pacing/retry |
| LOADT06 | Queue stress test | Fill queue/backlog | Queue drains or escalates | Add capacity plan |
| LOADT07 | Reviewer load test | Many artifacts require review | Review bottleneck visible | Add tiering/sampling |
| LOADT08 | Cost stress test | Estimate cost at high volume | Cost under threshold or gated | Add budget control |
| LOADT09 | Monitoring stress test | Simulate many alerts/events | Alerts useful and routed | Tune alert rules |
| LOADT10 | Handoff load test | Many handoffs occur | Receiver can track state | Improve handoff index |

## FAULTT Fault / Exception Tests

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| FAULTT01 | Missing input test | Remove required input | Workflow asks, assumes, or blocks correctly | Fix intake rule |
| FAULTT02 | Bad input test | Provide malformed/noisy input | Validation catches issue | Add normalization |
| FAULTT03 | Missing source test | Remove source/access | Fallback or blocker is clear | Add source fallback |
| FAULTT04 | Tool failure test | Simulate tool/command/API failure | Recovery path captured | Add fallback/retry |
| FAULTT05 | Approval rejection test | Simulate rejected artifact | Rework path is clear | Improve review loop |
| FAULTT06 | Conflicting instruction test | Provide conflicting constraints | Workflow resolves or asks | Add conflict rule |
| FAULTT07 | Privacy failure test | Include sensitive data | Minimization/redaction applies | Fix privacy boundary |
| FAULTT08 | Security failure test | Include secret/unsafe action | Unsafe path blocked | Add security gate |
| FAULTT09 | Batch item failure test | Make one item fail | Failure isolated and logged | Add exception queue |
| FAULTT10 | Stale context test | Use outdated state/source | Invalidation rule fires | Improve memory refresh |

## UATT User Acceptance Tests

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| UATT01 | User task test | User tries intended task | User completes task without hidden help | Improve instructions |
| UATT02 | Reviewer acceptance test | Reviewer checks criteria | Blocking findings resolved | Revise artifact |
| UATT03 | Approver acceptance test | Approver makes decision | Approval/rejection criteria clear | Fix approval packet |
| UATT04 | Operator acceptance test | Operator runs runbook | Runbook executable | Improve runbook |
| UATT05 | Beginner acceptance test | Beginner uses output/workflow | Cognitive load acceptable | Simplify guide |
| UATT06 | Expert acceptance test | Expert reviews rigor | Evidence/criteria sufficient | Add depth |
| UATT07 | Client acceptance test | Client reviews deliverable | Client can approve or request changes | Adjust client packet |
| UATT08 | Production acceptance test | Producer/engineer can use handoff | Specs complete | Fix production handoff |
| UATT09 | Accessibility acceptance test | Target users can access/use output | Accessibility needs met | Improve accessibility |
| UATT10 | Reuse acceptance test | Another case reuses template | Template adapts without major rewrite | Improve variables |

## PROMPTT Prompt / Agent Evaluation Tests

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| PROMPTT01 | Prompt schema test | Run prompt and inspect output fields | Required schema present | Tighten prompt |
| PROMPTT02 | Prompt robustness test | Run varied inputs | Output remains usable | Add examples/constraints |
| PROMPTT03 | Prompt negative test | Provide out-of-scope input | Prompt refuses/routes correctly | Add boundaries |
| PROMPTT04 | Prompt evidence test | Ask sourced answer | Claims link to sources | Improve citation instructions |
| PROMPTT05 | Prompt style test | Test audience/style variants | Style matches target | Adjust style block |
| PROMPTT06 | Prompt invariants test | Image2/design invariants included | Invariants preserved | Strengthen invariant block |
| PROMPTT07 | Multi-step prompt test | Run chained prompts | Step outputs feed next step | Fix IO contract |
| PROMPTT08 | Tool-use prompt test | Prompt calls/uses tools correctly | Tool inputs valid | Improve tool plan |
| PROMPTT09 | Safety prompt test | High-risk input appears | Risk gates trigger | Add safety rules |
| PROMPTT10 | Benchmark prompt test | Run representative benchmark cases | Score meets threshold | Version/tune prompt |

## DATATST Data / Source Validation Tests

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| DATATST01 | Schema test | Validate columns/types/fields | Schema matches contract | Fix parser/schema |
| DATATST02 | Row count test | Compare expected/actual counts | Counts reconcile | Investigate gaps |
| DATATST03 | Null/duplicate test | Profile missing/duplicate data | Issues below threshold or handled | Clean data |
| DATATST04 | Join test | Validate keys and join cardinality | No unexplained duplication/drop | Fix join logic |
| DATATST05 | Metric test | Recompute sample metric | Metric matches definition | Fix calculation |
| DATATST06 | Freshness test | Check source date/watermark | Freshness threshold met | Refresh source |
| DATATST07 | Source reliability test | Rank/compare sources | Critical claims use reliable sources | Replace weak source |
| DATATST08 | Citation test | Verify citations resolve | Links/pages valid | Repair citation |
| DATATST09 | Lineage test | Trace output to source/transform | Lineage complete | Add provenance |
| DATATST10 | Privacy data test | Inspect sensitive fields | Sensitive data minimized/redacted | Fix handling |

## REHEARST Release / Handoff Rehearsal

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| REHEARST01 | Release rehearsal | Simulate release/publish/deploy | Checklist, rollback, monitor ready | Fix launch plan |
| REHEARST02 | Rollback rehearsal | Simulate bad release | Rollback path works | Fix rollback |
| REHEARST03 | Handoff rehearsal | Receiver tries handoff packet | Receiver can continue | Fix handoff |
| REHEARST04 | Support rehearsal | Simulate user/client question | Support answer/routing ready | Add support notes |
| REHEARST05 | Incident rehearsal | Simulate incident update/recovery | Incident comms/runbook usable | Fix incident path |
| REHEARST06 | Approval rehearsal | Approver reviews packet | Decision can be made | Add evidence |
| REHEARST07 | Client presentation rehearsal | Present deliverable to external audience | Message clear and caveated | Refine narrative |
| REHEARST08 | Training rehearsal | Teach workflow to operator/user | Learner can perform task | Improve training |
| REHEARST09 | Archive rehearsal | Retrieve archived package | Artifact findable and complete | Fix archive/index |
| REHEARST10 | Maintenance rehearsal | Simulate future update | Owner can update safely | Fix maintenance path |

## AUDT Audit / Compliance Simulation

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| AUDT01 | Evidence audit | Auditor checks claims/actions | Evidence supports claims | Fill evidence gaps |
| AUDT02 | Decision audit | Auditor reconstructs decision | Criteria/rationale visible | Improve decision log |
| AUDT03 | Approval audit | Auditor checks signoffs | Approval matches artifact version | Fix approval record |
| AUDT04 | Privacy audit | Auditor checks data handling | Minimization/retention clear | Fix privacy controls |
| AUDT05 | Security audit | Auditor checks access/secrets/actions | Controls and logs present | Fix security evidence |
| AUDT06 | Compliance audit | Auditor checks regulated requirement | Requirement evidence present | Fix compliance pack |
| AUDT07 | Change audit | Auditor checks what changed and why | Change log complete | Improve changelog |
| AUDT08 | Source audit | Auditor checks source quality/freshness | Sources traceable and current enough | Refresh/replace source |
| AUDT09 | Automation audit | Auditor checks automated run decisions | Logs, triggers, owners visible | Improve observability |
| AUDT10 | Closeout audit | Auditor checks completion claim | Requirement-to-proof map complete | Continue missing work |

## COMPARET Comparative Tests

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| COMPARET01 | Old vs new workflow | Run same case on both versions | New version improves target metric | Keep or roll back |
| COMPARET02 | Manual vs automated | Compare manual and automated output | Automation matches/extends quality | Tune automation |
| COMPARET03 | Tool A vs Tool B | Run same sample through tools | Best tool chosen by criteria | Update tool route |
| COMPARET04 | Prompt A vs Prompt B | Compare prompt variants | Winner meets benchmark | Version prompt |
| COMPARET05 | Full vs lightweight workflow | Compare effort and quality | Choose appropriate tier | Add routing rule |
| COMPARET06 | Source strategy comparison | Compare source sets | Higher reliability/coverage chosen | Update source rule |
| COMPARET07 | Review strategy comparison | Compare full/sampled/tiered review | Review catches enough risk | Tune QA route |
| COMPARET08 | Communication variant test | Compare messages | Audience understands and acts | Update comms template |
| COMPARET09 | Handoff variant test | Compare handoff formats | Receiver needs fewer clarifications | Update handoff |
| COMPARET10 | Metric comparison | Compare evaluation metrics | Metric changes decisions | Keep useful metric |

## SIGNOFFT Test Signoff

| Code | Test type | Setup | Pass rule | Follow-up |
|---|---|---|---|---|
| SIGNOFFT01 | Test plan signoff | Define test scope and owner | Owner accepts test plan | Run tests |
| SIGNOFFT02 | Test result signoff | Summarize pass/fail/caveats | Decision owner accepts result | Proceed/rework |
| SIGNOFFT03 | QA signoff | QA confirms criteria | Blocking issues closed | Release/hand off |
| SIGNOFFT04 | Risk signoff | Risk owner reviews residual risk | Risk accepted/mitigated | Continue or stop |
| SIGNOFFT05 | Compliance signoff | Compliance reviewer checks pack | Approval or required changes | Gate decision |
| SIGNOFFT06 | User signoff | User accepts tested output | Acceptance recorded | Close or expand |
| SIGNOFFT07 | Automation signoff | Owner accepts automation readiness | Trigger/monitor/fallback ready | Enable automation |
| SIGNOFFT08 | Production signoff | Release owner accepts readiness | Release checklist passes | Launch |
| SIGNOFFT09 | Archive signoff | Owner accepts final package | Archive complete and findable | Retain |
| SIGNOFFT10 | Learning signoff | Owner accepts lessons and updates | Improvements recorded | Update workflow |
