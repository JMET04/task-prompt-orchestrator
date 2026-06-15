# Professional Workflow Collaboration Topology Matrix

Use this when a workflow depends on how people, agents, teams, clients, vendors, reviewers, or committees collaborate. Collaboration topology defines the coordination shape, merge points, conflict rules, and communication cadence for solo, paired, parallel, cross-functional, async, synchronous, internal, external, and multi-agent work.

Selection rule:

1. Identify the collaboration shape needed for the workflow.
2. Select the closest topology code.
3. Add participants, coordination pattern, merge rule, conflict rule, and communication cadence to the prompt packet.
4. If collaboration ownership is unclear, route to role-responsibility and handoff matrices before execution.

## SOLO Solo Workflows

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| SOLO01 | Solo executor | One person/agent performs all steps | Self-check before delivery | Solo run log |
| SOLO02 | Solo with reviewer | Executor works, reviewer checks | Reviewer findings gate closeout | Review note |
| SOLO03 | Solo with approver | Executor prepares packet, approver decides | Approval gates release | Approval record |
| SOLO04 | Solo with tool support | Executor uses tools/scripts | Tool output verified by executor | Tool log |
| SOLO05 | Solo research | Executor gathers and synthesizes sources | Evidence table resolves conflicts | Research log |
| SOLO06 | Solo creative | Executor generates and selects variants | Criteria-based selection | Variant pack |
| SOLO07 | Solo operations | Operator follows runbook | Deviations logged/escalated | Runbook log |
| SOLO08 | Solo maintenance | Maintainer updates workflow/template | Version and QA required | Maintenance note |
| SOLO09 | Solo emergency | One owner acts quickly under constraints | Post-action review required | Emergency note |
| SOLO10 | Solo learning | User/agent learns and improves workflow | Lesson captured | Learning note |

## PAIR Pair Collaboration

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| PAIR01 | Driver/reviewer pair | One executes, one reviews live or after | Reviewer can block | Pair review |
| PAIR02 | Expert/operator pair | Operator executes, expert validates domain | Expert resolves domain issues | Expert note |
| PAIR03 | Writer/editor pair | Writer drafts, editor revises | Meaning preservation and style criteria | Edit log |
| PAIR04 | Designer/engineer pair | Designer specs, engineer checks feasibility | Feasibility conflict escalates | Design-eng note |
| PAIR05 | Analyst/decision-owner pair | Analyst prepares evidence, owner decides | Decision owner records rationale | Decision memo |
| PAIR06 | Agent/human pair | Agent drafts/executes, human gates | Human approves high-impact steps | HITL record |
| PAIR07 | Tool/operator pair | Tool processes, operator samples QA | Sample failure triggers rework | Sample QA |
| PAIR08 | Mentor/learner pair | Mentor guides, learner executes | Learner must complete task | Training note |
| PAIR09 | Client/consultant pair | Consultant produces, client supplies context | Client resolves business preference | Client note |
| PAIR10 | Legal/business pair | Business proposes, legal gates risk | Legal blocks regulated risk | Legal review |

## PARCOL Parallel Collaboration

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| PARCOL01 | Parallel research lanes | Multiple lanes gather different sources | Merge by evidence quality | Source merge |
| PARCOL02 | Parallel artifact lanes | Teams build separate sections/assets | Merge by shared output schema | Artifact merge |
| PARCOL03 | Parallel review lanes | Reviewers check different criteria | Blocking findings merged first | Review merge |
| PARCOL04 | Parallel batch lanes | Items split across workers/agents | Manifest reconciles item status | Batch merge |
| PARCOL05 | Parallel design variants | Designers/agents create alternatives | Select by criteria/rubric | Variant decision |
| PARCOL06 | Parallel testing lanes | Tests split by risk/coverage | Failures merge to QA report | Test merge |
| PARCOL07 | Parallel localization lanes | Locales handled separately | Locale owner validates fit | Localization merge |
| PARCOL08 | Parallel data lanes | Data sources/segments processed separately | Reconcile definitions and totals | Data merge |
| PARCOL09 | Parallel tool comparison | Different tools run same sample | Choose by metric/risk/cost | Tool comparison |
| PARCOL10 | Parallel recovery lanes | Multiple fixes investigated | Choose safest verified fix | Recovery merge |

## CROSSFUNC Cross-Functional Collaboration

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| CROSSFUNC01 | Product/design/engineering | Product defines goal, design specifies, engineering validates | Product owner resolves scope | PDE packet |
| CROSSFUNC02 | Data/product/business | Data produces evidence, product/business decides | Metric definition governs | Data decision |
| CROSSFUNC03 | Marketing/legal/brand | Marketing drafts, brand/legal approve | Legal/brand blocks release | Campaign approval |
| CROSSFUNC04 | Sales/product/support | Sales/support surface needs, product prioritizes | Product owner decides | Feedback triage |
| CROSSFUNC05 | Ops/security/engineering | Ops reports issue, security/engineering fix | Severity determines owner | Incident packet |
| CROSSFUNC06 | Finance/operations/product | Finance validates assumptions, ops/product execute | Finance gates spend/metrics | Finance review |
| CROSSFUNC07 | HR/legal/manager | Manager proposes, HR/legal validates fairness | Legal/HR blocks risk | HR review |
| CROSSFUNC08 | Research/writing/editorial | Research supplies evidence, writing drafts, editorial QA | Evidence governs claims | Editorial packet |
| CROSSFUNC09 | Manufacturing/design/procurement | Design specs, manufacturing validates, procurement sources | Manufacturing feasibility gates | Production packet |
| CROSSFUNC10 | Compliance/business/technology | Business goal mapped to controls and implementation | Compliance gate controls release | Compliance packet |

## ASYNC Async Collaboration

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| ASYNC01 | Async status thread | Updates posted at defined cadence | Latest status wins with timestamp | Status thread |
| ASYNC02 | Async review queue | Reviewers respond when available | Criteria and deadline control merge | Review queue |
| ASYNC03 | Async approval queue | Approver decides from packet | Approval tied to version | Approval queue |
| ASYNC04 | Async handoff | Sender leaves complete packet | Receiver verifies current state | Handoff packet |
| ASYNC05 | Async batch queue | Workers process queued items | Manifest is source of truth | Queue manifest |
| ASYNC06 | Async client feedback | Client comments collected over time | Decision owner clusters and resolves | Feedback log |
| ASYNC07 | Async multi-timezone | Work passes by timezone | Handoff includes timezone/deadline | Timezone handoff |
| ASYNC08 | Async research review | Sources/findings reviewed over time | Evidence ledger governs claims | Source review |
| ASYNC09 | Async incident updates | Updates sent on cadence until stable | Facts only, no speculation | Incident thread |
| ASYNC10 | Async archive review | Archive/index checked later | Retrieval proof closes review | Archive review |

## SYNC Synchronous Collaboration

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| SYNC01 | Live working session | Participants co-create or decide live | Capture decisions/actions | Session notes |
| SYNC02 | Live review | Reviewer inspects artifact in meeting | Findings recorded immediately | Review notes |
| SYNC03 | Live approval | Approver decides in meeting | Approval conditions recorded | Approval note |
| SYNC04 | Live incident room | Owners coordinate recovery live | Incident commander resolves priority | Incident log |
| SYNC05 | Live design critique | Designers/stakeholders critique artifact | Criteria separate taste from defects | Critique notes |
| SYNC06 | Live planning | Team sequences work together | Owner and dates assigned | Plan notes |
| SYNC07 | Live training | Instructor teaches operator/user | Practice confirms understanding | Training record |
| SYNC08 | Live client workshop | Client and team align scope/options | Client decision captured | Workshop summary |
| SYNC09 | Live debugging | Developer/agent/user inspect issue together | Repro and fix path recorded | Debug log |
| SYNC10 | Live closeout | Stakeholders verify final outcome | Signoff or open issues recorded | Closeout notes |

## MULTIAG Multi-Agent Collaboration

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| MULTIAG01 | Planner/executor agents | Planner defines workflow, executor acts | Executor reports evidence to planner | Agent plan/run |
| MULTIAG02 | Research agents | Agents research independent lanes | Merge by source quality and citations | Research merge |
| MULTIAG03 | Critic agent | Critic reviews output from maker agent | Findings require evidence | Critic report |
| MULTIAG04 | QA agent | QA agent checks artifact against rubric | Blocking QA gates delivery | QA agent report |
| MULTIAG05 | Tool agent | Tool-focused agent runs integrations | Tool outputs verified by orchestrator | Tool agent log |
| MULTIAG06 | Domain agents | Agents cover specialized domains | Orchestrator resolves conflicts | Domain merge |
| MULTIAG07 | Red-team agent | Agent probes failure/safety gaps | Findings routed to fixes | Red-team report |
| MULTIAG08 | Summarizer agent | Agent compresses state for continuation | Main agent verifies current state | Summary packet |
| MULTIAG09 | Orchestrator agent | One agent coordinates lanes and merge | Orchestrator owns final synthesis | Orchestration log |
| MULTIAG10 | Agent handoff chain | Agents pass state across turns/tasks | Handoff packet verified before use | Agent handoff |

## CLIENTCOL Client / Stakeholder Collaboration

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| CLIENTCOL01 | Client intake | Client supplies goal/context/constraints | Missing context becomes ask | Intake packet |
| CLIENTCOL02 | Client review | Client reviews draft/output | Feedback classified by impact | Client review log |
| CLIENTCOL03 | Client approval | Client approves deliverable/gate | Approval tied to version | Client signoff |
| CLIENTCOL04 | Client workshop | Joint exploration/decision session | Decisions/actions captured | Workshop notes |
| CLIENTCOL05 | Client change request | Client changes scope/requirements | Impact assessment required | Change decision |
| CLIENTCOL06 | Client issue resolution | Client reports defect/concern | Issue triaged and owner assigned | Issue log |
| CLIENTCOL07 | Client training | Client learns to use output/workflow | Client can perform target task | Training evidence |
| CLIENTCOL08 | Client handoff | Deliverable moves to client ownership | Limits and next actions clear | Client handoff |
| CLIENTCOL09 | Client escalation | Client priority/risk needs escalation | Escalation owner responds | Escalation note |
| CLIENTCOL10 | Client closeout | Client accepts or documents open issues | Acceptance/open list recorded | Closeout record |

## VENDORCOL Vendor / Partner Collaboration

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| VENDORCOL01 | Vendor intake | Vendor receives requirements/spec | Requirements acceptance recorded | Vendor brief |
| VENDORCOL02 | Vendor delivery | Vendor returns artifact/service | QA and SLA check gate acceptance | Vendor QA |
| VENDORCOL03 | Vendor review | Team reviews vendor output | Findings sent as structured issues | Vendor review |
| VENDORCOL04 | Vendor approval | Vendor work needs internal signoff | Signoff tied to deliverable | Vendor approval |
| VENDORCOL05 | Vendor incident | Vendor failure affects workflow | Vendor owner coordinates response | Vendor incident |
| VENDORCOL06 | Vendor data exchange | Data shared with vendor | Privacy/security controls apply | Data sharing note |
| VENDORCOL07 | Vendor change request | Vendor/client changes scope | Contract/SLA impact reviewed | Change note |
| VENDORCOL08 | Vendor performance review | Vendor quality/timeliness assessed | Scorecard drives decision | Scorecard |
| VENDORCOL09 | Vendor offboarding | Vendor no longer used | Access revoked and artifacts transferred | Offboarding note |
| VENDORCOL10 | Partner co-creation | Partner and team jointly produce output | Shared approval and rights recorded | Partner packet |

## COMMITTEE Committee / Board Collaboration

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| COMMITTEE01 | Review board | Board reviews artifact/risk | Chair records decision | Board minutes |
| COMMITTEE02 | Approval committee | Committee approves gate/release/spend | Voting/quorum rule applies | Approval minutes |
| COMMITTEE03 | Governance council | Council sets policy/control route | Policy owner updates route | Governance record |
| COMMITTEE04 | Architecture board | Board reviews technical design | Architecture decision record | ADR/board note |
| COMMITTEE05 | Risk committee | Committee reviews high-impact risk | Risk disposition recorded | Risk minutes |
| COMMITTEE06 | Editorial board | Board reviews claims/narrative | Evidence and style criteria apply | Editorial decision |
| COMMITTEE07 | Investment committee | Committee reviews financial/investment recommendation | Assumptions and risks required | IC memo |
| COMMITTEE08 | Change advisory board | CAB reviews operational change | Change/rollback plan required | CAB record |
| COMMITTEE09 | Accessibility review panel | Panel reviews accessibility/inclusion | Accessibility findings gate release | Accessibility minutes |
| COMMITTEE10 | Exception committee | Committee approves policy exceptions | Exception rationale recorded | Exception record |

## CROWD Community / Open Collaboration

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| CROWD01 | Community feedback | Many users submit feedback | Cluster themes and evidence | Feedback synthesis |
| CROWD02 | Open review | Many reviewers inspect artifact | Weight by criteria/source quality | Review synthesis |
| CROWD03 | Crowdsourced ideas | Many contributors submit ideas | Rank by criteria and feasibility | Idea shortlist |
| CROWD04 | Beta group | Limited community tests workflow/output | Issues triaged by severity | Beta report |
| CROWD05 | User research panel | Panel provides structured feedback | Research protocol governs | Research report |
| CROWD06 | Open-source contribution | External contributors submit changes | Maintainer review gates merge | Contribution record |
| CROWD07 | Community moderation | User-generated content/workflow input | Moderation policy applies | Moderation log |
| CROWD08 | Public challenge | Participants produce variants/solutions | Scoring rubric governs | Challenge result |
| CROWD09 | Community knowledge base | Users contribute reusable knowledge | Curator validates and indexes | KB entry |
| CROWD10 | Community escalation | Public issue gains urgency | Owner responds with status cadence | Escalation update |

## MERGECOL Merge / Conflict Collaboration

| Code | Topology | Coordination pattern | Merge/conflict rule | Evidence |
|---|---|---|---|---|
| MERGECOL01 | Evidence merge | Sources/lane findings conflict | Higher authority/freshness wins or caveat | Evidence merge |
| MERGECOL02 | Artifact merge | Sections/assets from multiple owners | Shared schema and editor merge | Artifact merge log |
| MERGECOL03 | Decision merge | Multiple owners propose decisions | Accountable owner decides | Decision record |
| MERGECOL04 | Review merge | Multiple reviewers find issues | Sort by severity and owner | Review synthesis |
| MERGECOL05 | Data merge | Multiple datasets/sheets combine | Reconcile keys/grain/totals | Data merge QA |
| MERGECOL06 | Prompt merge | Prompt variants combine | Benchmark and choose/compose | Prompt merge |
| MERGECOL07 | Design merge | Visual variants combine | Design owner preserves system consistency | Design merge |
| MERGECOL08 | Code merge | Branches/patches combine | Tests and conflict resolution required | Code merge note |
| MERGECOL09 | Client/internal conflict | Client wants conflict with policy/feasibility | Escalate with options | Conflict memo |
| MERGECOL10 | Final synthesis | Multiple lanes become final answer | Orchestrator records caveats and sources | Synthesis note |
