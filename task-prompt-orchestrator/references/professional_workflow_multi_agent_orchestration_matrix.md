# Professional Workflow Multi-Agent and Human Orchestration Matrix

Use this when a workflow needs multiple agents, humans, reviewers, tools, roles, teams, or parallel workstreams to coordinate at runtime. This matrix defines how to assign roles, pass context, coordinate work, merge outputs, resolve conflicts, gate decisions, and keep accountability clear.

Selection rule:

1. Identify the participants: human, agent, tool, reviewer, approver, SME, operator, client, vendor, or team.
2. Select the closest orchestration code.
3. Add roster, role contract, message protocol, artifact handoff, merge rule, review gate, and escalation path to the prompt packet.
4. Do not run multi-participant workflows without a named coordinator or merge owner.

## ROSTER Participant Roster

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| ROSTER01 | Human participant roster | Name humans or teams involved | Assign role and availability | Roster table |
| ROSTER02 | Agent participant roster | Name agents or agent functions | Assign mission and limits | Agent roster |
| ROSTER03 | Tool participant roster | Name tools/scripts/APIs used | Define tool owner and fallback | Tool roster |
| ROSTER04 | Reviewer roster | Name reviewers by domain | Match reviewer to risk area | Review roster |
| ROSTER05 | Approver roster | Name approvers and thresholds | Gate release by approval rule | Approval roster |
| ROSTER06 | SME roster | Name expert validators | Use only for material domain risk | SME roster |
| ROSTER07 | Client/vendor roster | Name external participants | Define authority and response path | External roster |
| ROSTER08 | Backup roster | Name backups for critical roles | Use backup on SLA breach | Backup roster |
| ROSTER09 | Observer roster | Name informed-only participants | Limit noise and access | Observer list |
| ROSTER10 | Roster refresh | Participants changed or stale | Reconfirm roster before execution | Roster update |

## AGROLE Agent Role Contracts

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| AGROLE01 | Planner agent | Agent decomposes goal into steps | Human or coordinator approves plan | Plan packet |
| AGROLE02 | Research agent | Agent gathers evidence/sources | Require source ledger | Research ledger |
| AGROLE03 | Builder agent | Agent creates artifact/code/content | Require diff/output contract | Build packet |
| AGROLE04 | Reviewer agent | Agent audits output against rubric | Findings must cite evidence | Review report |
| AGROLE05 | Critic agent | Agent challenges assumptions/options | Separate critique from decision | Critique memo |
| AGROLE06 | Synthesizer agent | Agent merges multiple inputs | Track source-to-output mapping | Synthesis map |
| AGROLE07 | Operator agent | Agent executes runbook/batch | Log actions and exceptions | Ops log |
| AGROLE08 | QA agent | Agent runs tests/checklists | Produce pass/fail evidence | QA report |
| AGROLE09 | Recovery agent | Agent diagnoses and restores failures | Follow containment first | Recovery note |
| AGROLE10 | Archivist agent | Agent saves reusable knowledge | Update index and provenance | Archive entry |

## HUMROLE Human Role Contracts

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| HUMROLE01 | Requester role | Human defines need and success | Confirm scope and acceptance | Request brief |
| HUMROLE02 | Owner role | Human accountable for outcome | Owner decides priority and tradeoffs | Owner record |
| HUMROLE03 | Reviewer role | Human checks quality/domain fit | Reviewer can block only in scope | Review comments |
| HUMROLE04 | Approver role | Human authorizes release/change | Approval criteria explicit | Approval record |
| HUMROLE05 | SME role | Human validates expert-sensitive claims | SME reviews targeted sections | SME note |
| HUMROLE06 | Operator role | Human runs or supervises process | Operator follows runbook | Operator log |
| HUMROLE07 | Editor role | Human polishes/rewrites output | Preserve meaning and constraints | Edit log |
| HUMROLE08 | Designer role | Human validates visual/product fit | Check specs and usability | Design note |
| HUMROLE09 | Developer role | Human owns implementation correctness | Verify tests/builds | Dev note |
| HUMROLE10 | Client role | Human accepts business result | Client decision captured | Client signoff |

## PROTOCOL Communication Protocol

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| PROTOCOL01 | Task message protocol | Participants need consistent instructions | Use goal/input/output/done/handoff format | Task packet |
| PROTOCOL02 | Status protocol | Participants need progress visibility | Use state, blocker, ETA, next action | Status note |
| PROTOCOL03 | Question protocol | Clarifications may interrupt work | Ask only blocking questions with options | Question log |
| PROTOCOL04 | Decision protocol | Decisions need rationale | Record options, criteria, decision, owner | Decision record |
| PROTOCOL05 | Escalation protocol | Blockers need routing | Define threshold and recipient | Escalation note |
| PROTOCOL06 | Review protocol | Feedback needs structure | Use finding, evidence, impact, action | Review packet |
| PROTOCOL07 | Handoff protocol | Work crosses participant boundary | Include context, artifact, state, next step | Handoff note |
| PROTOCOL08 | Incident protocol | Urgent issue needs concise updates | Use severity, impact, action, ETA | Incident update |
| PROTOCOL09 | Merge protocol | Multiple outputs need reconciliation | Use stable IDs and conflict rule | Merge log |
| PROTOCOL10 | Archive protocol | Knowledge must be reusable | Include title, tags, provenance, owner | Archive note |

## CTXSHIP Context Shipping

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| CTXSHIP01 | Minimal context packet | Participant needs only task-local context | Send necessary inputs and constraints only | Context packet |
| CTXSHIP02 | Full context packet | High-risk participant needs full history | Include decisions, risks, sources, versions | Full packet |
| CTXSHIP03 | Evidence packet | Reviewer needs proof | Include source links, tests, logs, samples | Evidence packet |
| CTXSHIP04 | State packet | Resumer needs current state | Include done/pending/blockers/next action | State packet |
| CTXSHIP05 | Tool context packet | Tool/operator needs environment details | Include paths, versions, commands, limits | Tool packet |
| CTXSHIP06 | Design context packet | Designer needs visual/product constraints | Include assets, specs, references, states | Design packet |
| CTXSHIP07 | Domain context packet | SME needs domain assumptions | Include scope, claims, uncertainty, standards | Domain packet |
| CTXSHIP08 | Privacy-minimized packet | Participant should not see all data | Redact and minimize before handoff | Redaction note |
| CTXSHIP09 | Refresh context packet | Prior context may be stale | Reopen authoritative sources before shipping | Refresh note |
| CTXSHIP10 | Context receipt | Receiver must confirm understanding | Ask receiver to restate next action | Receipt note |

## DECOMP Work Decomposition

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| DECOMP01 | Role-based decomposition | Split by participant expertise | Assign each role one clear output | Role WBS |
| DECOMP02 | Artifact-based decomposition | Split by deliverable sections/assets | Define shared output schema | Artifact WBS |
| DECOMP03 | Phase-based decomposition | Split by lifecycle stage | Gate phase before next stage | Phase WBS |
| DECOMP04 | Risk-based decomposition | Split risky parts for extra review | Route high-risk work separately | Risk WBS |
| DECOMP05 | Domain-based decomposition | Split by professional domain | Use domain-specific reviewer | Domain WBS |
| DECOMP06 | Batch-based decomposition | Split by item manifest | Track each item owner/status | Batch WBS |
| DECOMP07 | Parallel decomposition | Work can run concurrently | Define merge order and conflicts | Parallel WBS |
| DECOMP08 | Sequential decomposition | Work must happen in strict order | Define dependency chain | Sequence WBS |
| DECOMP09 | Exploratory decomposition | Unknown path needs exploration lanes | Timebox lanes and compare | Exploration WBS |
| DECOMP10 | Decomposition revision | Work split proves wrong | Replan and notify affected owners | Replan note |

## DISPATCH Work Dispatch

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| DISPATCH01 | Single-owner dispatch | One participant receives next task | Include done_when and handoff | Dispatch note |
| DISPATCH02 | Parallel dispatch | Multiple participants start together | Use shared manifest and deadline | Parallel dispatch |
| DISPATCH03 | Review dispatch | Output is routed for review | Include rubric and evidence | Review dispatch |
| DISPATCH04 | Approval dispatch | Decision packet goes to approver | Include options and recommendation | Approval dispatch |
| DISPATCH05 | Specialist dispatch | Expert handles narrow question | Define exact domain question | Specialist request |
| DISPATCH06 | Tool dispatch | Script/tool receives structured inputs | Validate schema before run | Tool dispatch |
| DISPATCH07 | Recovery dispatch | Failure routed to recovery owner | Include severity and containment | Recovery dispatch |
| DISPATCH08 | Batch dispatch | Items assigned to workers/agents | Assign stable item IDs | Batch dispatch |
| DISPATCH09 | Learning dispatch | Learner receives guided task | Include hint, success check, feedback path | Learning dispatch |
| DISPATCH10 | Dispatch recall | Dispatched work should stop/change | Send cancellation or updated brief | Recall note |

## MERGE Output Merge

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| MERGE01 | Section merge | Separate sections become one artifact | Normalize structure and transitions | Section merge |
| MERGE02 | Evidence merge | Multiple evidence sets combine | Deduplicate and rank source authority | Evidence merge |
| MERGE03 | Variant merge | Multiple creative/options outputs combine | Select or blend by criteria | Variant merge |
| MERGE04 | Data merge | Tables/results combine | Use keys, grain, and reconciliation checks | Data merge |
| MERGE05 | Code merge | Changes combine in repo/files | Inspect conflicts and run tests | Code merge |
| MERGE06 | Review merge | Multiple review findings combine | Deduplicate and severity-rank | Review merge |
| MERGE07 | Decision merge | Multiple recommendations combine | Record tradeoffs and final owner | Decision merge |
| MERGE08 | Batch merge | Item outputs combine | Reconcile manifest terminal states | Batch merge |
| MERGE09 | Knowledge merge | Lessons/templates/index entries combine | Preserve provenance and tags | Knowledge merge |
| MERGE10 | Merge rejection | Outputs cannot safely combine | Escalate conflict or rerun lane | Rejection note |

## ARBIT Conflict Arbitration

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| ARBIT01 | Instruction conflict | Participants received conflicting instructions | Resolve by priority and latest authority | Conflict note |
| ARBIT02 | Evidence conflict | Sources or analyses disagree | Create conflict table and confidence | Evidence arbitration |
| ARBIT03 | Design conflict | Visual/design directions differ | Decide by brief, audience, constraints | Design arbitration |
| ARBIT04 | Technical conflict | Implementation approaches differ | Decide by tests, maintainability, risk | Tech arbitration |
| ARBIT05 | Business conflict | Value, cost, or priority differs | Owner decides with tradeoff memo | Business arbitration |
| ARBIT06 | Compliance conflict | Desired output conflicts with policy | Policy/legal/security gate decides | Compliance arbitration |
| ARBIT07 | Reviewer conflict | Reviewers disagree | Merge findings and escalate unresolved blockers | Review arbitration |
| ARBIT08 | Agent conflict | Agents produce incompatible outputs | Re-run with shared criteria or coordinator decision | Agent arbitration |
| ARBIT09 | Client/internal conflict | Client preference conflicts with internal constraints | Present options and implications | Client arbitration |
| ARBIT10 | Arbitration closeout | Conflict resolved | Record final decision and changed instructions | Arbitration record |

## GATEORCH Orchestration Gates

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| GATEORCH01 | Start gate | Participants should not begin too early | Confirm brief, inputs, owners, deadline | Start gate |
| GATEORCH02 | Source gate | Research/source work must be trustworthy | Check source inventory and authority | Source gate |
| GATEORCH03 | Draft gate | Draft ready before review | Check completeness against outline | Draft gate |
| GATEORCH04 | Review gate | Review must finish before merge/release | Require disposition of findings | Review gate |
| GATEORCH05 | Approval gate | Output needs owner/client/legal approval | Hold until approval evidence exists | Approval gate |
| GATEORCH06 | Merge gate | Parallel outputs must be compatible | Check schema, conflicts, missing parts | Merge gate |
| GATEORCH07 | QA gate | Artifact must pass tests/rubric | Require pass/fail evidence | QA gate |
| GATEORCH08 | Risk gate | High-impact work needs risk decision | Require accepted residual risk | Risk gate |
| GATEORCH09 | Handoff gate | Receiver must be able to continue | Confirm receipt and next action | Handoff gate |
| GATEORCH10 | Closeout gate | Workflow should close | Confirm outputs, evidence, archive, follow-up | Closeout gate |

## TRACEORCH Accountability Trace

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| TRACEORCH01 | Action trace | Need know who did what | Log participant, action, artifact, time | Action trace |
| TRACEORCH02 | Decision trace | Need know why decision was made | Log owner, criteria, options, rationale | Decision trace |
| TRACEORCH03 | Source trace | Need trace claim to evidence | Map output claims to source IDs | Source trace |
| TRACEORCH04 | Review trace | Need trace comments to fixes | Link finding to disposition | Review trace |
| TRACEORCH05 | Prompt trace | Need know prompt used | Save prompt version and variables | Prompt trace |
| TRACEORCH06 | Tool trace | Need know tool output origin | Save command/API/tool version/output | Tool trace |
| TRACEORCH07 | Merge trace | Need know how outputs combined | Save merge rule and conflicts | Merge trace |
| TRACEORCH08 | Approval trace | Need prove authorization | Save approver and approval basis | Approval trace |
| TRACEORCH09 | Exception trace | Need know deviations | Log exception, owner, reason, mitigation | Exception trace |
| TRACEORCH10 | Audit trace | Need complete orchestration evidence | Bundle traces into audit packet | Audit trace |

## RETROORCH Team Learning

| Code | Orchestration need | Setup | Control | Evidence |
|---|---|---|---|---|
| RETROORCH01 | Coordination retro | Collaboration was inefficient | Capture bottlenecks and improvements | Retro note |
| RETROORCH02 | Role retro | Ownership was unclear | Update role contracts | Role update |
| RETROORCH03 | Prompt retro | Agent instructions underperformed | Patch prompt packet/template | Prompt update |
| RETROORCH04 | Review retro | Review missed or overblocked issues | Update rubric and reviewer guidance | Review update |
| RETROORCH05 | Merge retro | Merge caused rework | Improve schema/conflict rule | Merge update |
| RETROORCH06 | Tool retro | Tool choice slowed or degraded output | Update tool routing/fallback | Tool update |
| RETROORCH07 | Communication retro | Updates were noisy or missing | Adjust cadence and format | Comms update |
| RETROORCH08 | Training retro | Participant needed more guidance | Add onboarding/example material | Training update |
| RETROORCH09 | Reuse retro | Workflow produced reusable pattern | Save template and index entry | Reuse entry |
| RETROORCH10 | Retro closeout | Improvements need follow-through | Assign owners and verification | Retro actions |
