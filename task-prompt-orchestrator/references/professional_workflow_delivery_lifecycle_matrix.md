# Professional Workflow Delivery Lifecycle Matrix

Use this when a workflow must produce a complete delivery chain rather than isolated steps. Delivery lifecycle rules define how a request becomes a scoped plan, controlled production process, reviewed package, accepted deliverable, and reusable asset.

Selection rule:

1. Select the base workflow and domain adaptation first.
2. Select the closest delivery lifecycle code here.
3. Add required phase artifact, gate, owner, and handoff evidence to the prompt packet.
4. Do not treat delivery as complete until the acceptance and closeout evidence exist.

## BRFDEL Briefing / Intake Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| BRFDEL01 | Raw request intake | Capture goal, context, constraints, deliverable | Request is understandable | Intake note |
| BRFDEL02 | Stakeholder intake | Capture requester, user, reviewer, approver | Roles are named | Stakeholder list |
| BRFDEL03 | Source intake | Inventory files, links, data, images, references | Source access checked | Source inventory |
| BRFDEL04 | Constraint intake | Capture deadline, budget, format, channel, policy | Constraints are explicit | Constraint list |
| BRFDEL05 | Risk intake | Identify high-risk domain, uncertainty, dependencies | Escalation path exists | Risk intake |
| BRFDEL06 | Success intake | Define what success means and how judged | Acceptance basis exists | Success criteria |
| BRFDEL07 | Missing-info intake | Separate blockers from safe assumptions | Blockers resolved or logged | Assumption log |
| BRFDEL08 | Existing-asset intake | Find templates, skills, prior outputs, indexes | Reuse path checked | Asset inventory |
| BRFDEL09 | Scope boundary intake | Define in-scope, out-of-scope, non-goals | Boundary approved | Scope note |
| BRFDEL10 | Brief freeze | Convert intake to execution brief | Brief is stable enough | Frozen brief |

## SCPDEL Scoping / Requirements Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| SCPDEL01 | Deliverable scoping | Define exact output form, sections, files, formats | Output is concrete | Deliverable spec |
| SCPDEL02 | Requirement decomposition | Break goal into functional/nonfunctional needs | Requirements are testable | Requirement list |
| SCPDEL03 | Acceptance scoping | Map each requirement to acceptance evidence | No orphan requirement | Acceptance map |
| SCPDEL04 | Dependency scoping | Identify upstream/downstream dependencies | Dependency owner known | Dependency log |
| SCPDEL05 | Variant scoping | Define variants, audiences, languages, channels | Variant count bounded | Variant plan |
| SCPDEL06 | Quality scoping | Define quality bar, depth, polish, review level | Quality bar explicit | QA rubric |
| SCPDEL07 | Tool scoping | Select tools, APIs, local files, models, fallback | Tool access verified | Tool plan |
| SCPDEL08 | Data scoping | Define data fields, freshness, lineage, sensitivity | Data contract defined | Data spec |
| SCPDEL09 | Compliance scoping | Identify policies, rights, privacy, approvals | Compliance owner known | Control map |
| SCPDEL10 | Effort scoping | Estimate time, capacity, cost, priority | Feasibility confirmed | Effort note |

## PLNDEL Planning / Work Breakdown Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| PLNDEL01 | Phase plan | Sequence phases from intake to closeout | Dependencies make sense | Phase map |
| PLNDEL02 | WBS plan | Break deliverable into atomic tasks | Tasks are assignable | WBS |
| PLNDEL03 | Milestone plan | Define checkpoints, dates, review moments | Milestones tied to evidence | Milestone table |
| PLNDEL04 | Parallel work plan | Split lanes for independent workstreams | Merge rule defined | Lane plan |
| PLNDEL05 | Review plan | Identify reviewers, review scope, timing | Review capacity exists | Review schedule |
| PLNDEL06 | Communication plan | Define status cadence, channels, escalation | Audiences covered | Comms plan |
| PLNDEL07 | Risk plan | Define prevention, detection, mitigation, fallback | Top risks covered | Risk plan |
| PLNDEL08 | Resource plan | Allocate people, tools, budget, data, environment | Resources available | Resource table |
| PLNDEL09 | Verification plan | Define tests, checks, pilots, signoff | Verification maps to risk | Test plan |
| PLNDEL10 | Execution authorization | Confirm plan is ready to execute | Owner accepts plan | Start approval |

## PRDDEL Production / Execution Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| PRDDEL01 | Draft production | Create first complete version | Covers required sections | Draft artifact |
| PRDDEL02 | Asset production | Generate or assemble media/design/document assets | Specs followed | Asset output |
| PRDDEL03 | Data production | Extract, clean, transform, calculate, analyze | Data QA passes | Analysis file |
| PRDDEL04 | Code production | Implement code/config/script changes | Builds or static checks pass | Diff and test |
| PRDDEL05 | Research production | Gather and synthesize evidence | Sources traceable | Evidence table |
| PRDDEL06 | Workflow production | Run the planned steps and record state | State transitions logged | Execution log |
| PRDDEL07 | Batch production | Produce variants or batch outputs | Sample check passes | Batch manifest |
| PRDDEL08 | Automation production | Configure job, trigger, script, integration | Dry run succeeds | Automation log |
| PRDDEL09 | Physical-production prep | Prepare CAD, BOM, packaging, manufacturing notes | Specs measurable | Production packet |
| PRDDEL10 | Interim production checkpoint | Pause for inspection before final polish | Issues triaged | Checkpoint note |

## REVDEL Review / QA Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| REVDEL01 | Self-review | Check output against brief and acceptance criteria | Major gaps fixed | Self-review |
| REVDEL02 | Peer review | Route to reviewer with focused questions | Review response captured | Peer comments |
| REVDEL03 | SME review | Route domain-sensitive parts to expert | SME concerns resolved | SME signoff |
| REVDEL04 | Fact/source review | Verify claims, citations, numbers, dates | Claims trace to sources | Source audit |
| REVDEL05 | Format review | Check file format, naming, layout, dimensions | Output opens/renders | Format check |
| REVDEL06 | Technical QA | Run tests, validators, scripts, lint, schema checks | Required checks pass | Test output |
| REVDEL07 | Policy QA | Check privacy, rights, security, legal, brand | Policy risks handled | Policy checklist |
| REVDEL08 | Usability QA | Check user flow, clarity, accessibility, comprehension | User can act | UX check |
| REVDEL09 | Regression QA | Confirm changes did not break existing behavior | Regression covered | Regression log |
| REVDEL10 | Review disposition | Convert feedback to fix/accept/defer decisions | No unresolved blocker | Disposition log |

## APRDEL Approval / Governance Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| APRDEL01 | Owner approval | Request owner acceptance against scope | Owner decision recorded | Owner signoff |
| APRDEL02 | Client approval | Present deliverable and decision points | Client approves or comments | Client response |
| APRDEL03 | Legal approval | Route legal-sensitive content | Legal risk resolved | Legal signoff |
| APRDEL04 | Finance approval | Route cost, pricing, budget, investment decisions | Finance criteria met | Finance signoff |
| APRDEL05 | Security approval | Route access, data, infra, vulnerability risk | Security criteria met | Security signoff |
| APRDEL06 | Brand approval | Route public-facing brand/claims/assets | Brand fit confirmed | Brand signoff |
| APRDEL07 | Data approval | Route metric/data-source/PII decisions | Data governance passes | Data signoff |
| APRDEL08 | Change approval | Route process/system changes through control board | Change risk accepted | Change record |
| APRDEL09 | Exception approval | Document approved deviation from standard | Exception owner named | Exception note |
| APRDEL10 | Release approval | Confirm all gates before publish/deploy/handoff | Release authorized | Release approval |

## PKGDEL Packaging / Export Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| PKGDEL01 | Final file packaging | Assemble final files with names and versions | Files complete | File manifest |
| PKGDEL02 | Source package | Include sources, citations, data, references | Traceability preserved | Source bundle |
| PKGDEL03 | Editable package | Include editable originals and locked exports | Edit path clear | Editable bundle |
| PKGDEL04 | Deployment package | Include build, env, config, release notes | Deploy path reproducible | Deploy package |
| PKGDEL05 | Design package | Include assets, specs, tokens, exports, previews | Design specs usable | Design handoff |
| PKGDEL06 | Manufacturing package | Include drawings, BOM, tolerances, QA notes | Production inputs complete | MFG pack |
| PKGDEL07 | Training package | Include slides, scripts, exercises, facilitator notes | Instructor can run | Training bundle |
| PKGDEL08 | Executive package | Include summary, decision, risks, appendix | Decision-ready | Exec pack |
| PKGDEL09 | Archive package | Include metadata, owner, retention, version | Future retrieval possible | Archive record |
| PKGDEL10 | Transfer package | Include handoff note, next actions, contacts, risks | Receiver can continue | Transfer note |

## LCHDEL Launch / Release Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| LCHDEL01 | Publish launch | Publish approved content/artifact to channel | Channel spec passes | Publish log |
| LCHDEL02 | Software release | Deploy code/config with monitoring and rollback | Health check passes | Release log |
| LCHDEL03 | Campaign launch | Activate campaign assets, audiences, tracking | Tracking verified | Launch sheet |
| LCHDEL04 | Training launch | Run session or release learning path | Attendance/access confirmed | Training record |
| LCHDEL05 | Process launch | Start new SOP/workflow in operations | Operators trained | SOP launch |
| LCHDEL06 | Automation launch | Enable scheduled/event trigger | First run monitored | Automation run |
| LCHDEL07 | Product launch support | Prepare support, FAQ, escalation, known issues | Support ready | Support pack |
| LCHDEL08 | Data/report launch | Deliver dashboard/report and refresh cadence | Data refresh verified | Report launch |
| LCHDEL09 | Controlled rollout | Release to pilot cohort or percentage | Rollback criteria set | Rollout log |
| LCHDEL10 | Launch communication | Notify audiences with impact and action needed | Message delivered | Notice record |

## HNDDEL Handoff / Adoption Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| HNDDEL01 | User handoff | Explain output, usage, limits, next steps | User can use deliverable | User handoff |
| HNDDEL02 | Operator handoff | Transfer SOP/runbook, credentials path, escalation | Operator can run | Ops handoff |
| HNDDEL03 | Developer handoff | Transfer code context, tests, open issues, decisions | Developer can continue | Dev handoff |
| HNDDEL04 | Designer handoff | Transfer assets, specs, states, constraints | Designer can edit | Design handoff |
| HNDDEL05 | Analyst handoff | Transfer metric definitions, data lineage, caveats | Analyst can reproduce | Analyst handoff |
| HNDDEL06 | Reviewer handoff | Transfer review checklist, evidence, decision needs | Reviewer can decide | Review packet |
| HNDDEL07 | Support handoff | Transfer FAQs, known issues, response scripts | Support can respond | Support note |
| HNDDEL08 | Training handoff | Transfer learning materials and facilitator notes | Trainer can deliver | Training handoff |
| HNDDEL09 | Client handoff | Transfer final package, scope notes, acceptance ask | Client can accept | Client package |
| HNDDEL10 | Archive handoff | Transfer ownership, version, retention, retrieval path | Archive complete | Archive handoff |

## ACCDEL Acceptance / Signoff Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| ACCDEL01 | Requirement acceptance | Check each requirement against output | All must-pass items met | Acceptance matrix |
| ACCDEL02 | Quality acceptance | Check quality rubric, polish, usability | Quality threshold met | QA signoff |
| ACCDEL03 | Technical acceptance | Check tests, validators, performance, compatibility | Technical gates pass | Technical signoff |
| ACCDEL04 | Data acceptance | Check accuracy, lineage, freshness, privacy | Data gates pass | Data signoff |
| ACCDEL05 | Business acceptance | Check outcome, value, decision readiness | Business owner accepts | Business signoff |
| ACCDEL06 | Compliance acceptance | Check policy/legal/security/rights | Compliance gates pass | Compliance signoff |
| ACCDEL07 | User acceptance | Check user can perform intended action | UAT passes | UAT record |
| ACCDEL08 | Exception acceptance | Record accepted residual risks/deviations | Exceptions approved | Exception register |
| ACCDEL09 | Partial acceptance | Define accepted scope and remaining gap | Residual work tracked | Partial signoff |
| ACCDEL10 | Final acceptance | Record final approval and completion state | No open blockers | Final signoff |

## CLSDEL Closeout / Retrospective Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| CLSDEL01 | Completion summary | Summarize what changed, outputs, tests, risks | Summary matches evidence | Closeout note |
| CLSDEL02 | Decision log closeout | Record key decisions and rationale | Decisions traceable | Decision log |
| CLSDEL03 | Issue closeout | Confirm blockers, defects, follow-ups resolved/deferred | No hidden blocker | Issue log |
| CLSDEL04 | Metric closeout | Capture outcome metric or baseline for later | Metric owner known | Metric note |
| CLSDEL05 | Cost/time closeout | Compare estimate to actual effort/cost | Variance explained | Variance note |
| CLSDEL06 | Lessons learned | Capture what worked, failed, should change | Lessons actionable | Retrospective |
| CLSDEL07 | Documentation closeout | Update docs, index, README-equivalent, runbook | Docs current | Doc update |
| CLSDEL08 | Access closeout | Remove temporary access/secrets/files where needed | Access cleaned | Access log |
| CLSDEL09 | Archive closeout | Store final package and evidence in stable path | Retrieval tested | Archive proof |
| CLSDEL10 | Follow-up closeout | Define next owner, next date, next action | Continuation clear | Follow-up task |

## RUSEDEL Reuse / Template Delivery

| Code | Lifecycle unit | Workflow action | Gate | Evidence |
|---|---|---|---|---|
| RUSEDEL01 | Template extraction | Convert repeated structure into reusable template | Variables separated | Template draft |
| RUSEDEL02 | Prompt packet reuse | Save optimized prompt packet and routing notes | Prompt reusable | Prompt record |
| RUSEDEL03 | Checklist reuse | Extract QA/acceptance checklist | Checklist testable | Checklist |
| RUSEDEL04 | Workflow reuse | Save phase map, gates, roles, artifacts | Workflow portable | Workflow template |
| RUSEDEL05 | Example reuse | Save representative example input/output | Example anonymized | Example artifact |
| RUSEDEL06 | Automation reuse | Save script/job/integration pattern | Re-run path documented | Automation template |
| RUSEDEL07 | Index reuse | Add entry to scenario/prompt/workflow index | Findability improved | Index entry |
| RUSEDEL08 | Training reuse | Convert lessons into onboarding/training material | New user can follow | Training note |
| RUSEDEL09 | Governance reuse | Save policy/control mapping for repeat cases | Control owner known | Governance template |
| RUSEDEL10 | Maintenance reuse | Define owner, review cadence, retirement trigger | Template will stay current | Maintenance note |
