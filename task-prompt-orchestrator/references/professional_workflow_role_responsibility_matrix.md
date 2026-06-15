# Professional Workflow Role Responsibility Matrix

Use this when a workflow needs explicit ownership, RACI-style responsibility, human/AI/tool boundaries, approvals, reviews, handoffs, escalation owners, or operational accountability. Role responsibility prevents a workflow from becoming an ownerless checklist.

Selection rule:

1. Identify the workflow decision, artifact, or action that needs an owner.
2. Select the closest role responsibility code.
3. Add the role, responsibility, handoff boundary, and evidence to the prompt packet.
4. If no owner can be named, route to a blocked, risk, or handoff state instead of silently proceeding.

## OWN Ownership Roles

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| OWN01 | Single accountable owner | Own final outcome and acceptance | Does not replace specialist review | Named owner |
| OWN02 | Task owner | Own one workflow step and its output | Does not own downstream decisions | Step owner map |
| OWN03 | Artifact owner | Maintain a document, prompt, file, dataset, or design asset | Does not approve business decision | Artifact ownership note |
| OWN04 | Decision owner | Choose among options using stated criteria | Must record rationale | Decision log |
| OWN05 | Risk owner | Accept, mitigate, or escalate a named risk | Cannot hide residual risk | Risk register |
| OWN06 | Source owner | Provide or validate authoritative source material | Does not interpret beyond source scope | Source owner note |
| OWN07 | Process owner | Maintain repeatable workflow and update rules | Does not own every execution | Process ownership note |
| OWN08 | Quality owner | Define and enforce quality checks | Does not override requester scope alone | QA ownership note |
| OWN09 | Delivery owner | Ensure final handoff reaches the user/stakeholder | Does not certify specialist correctness | Delivery record |
| OWN10 | Continuation owner | Resume work after interruption or handoff | Must verify current state first | Resume owner note |

## RACI Responsibility Assignment

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| RACI01 | Responsible | Perform the work | May need approval before release | Task assignment |
| RACI02 | Accountable | Own final correctness and acceptance | Only one accountable owner per decision | Accountability map |
| RACI03 | Consulted | Provide input before decision or execution | Input is advisory unless designated | Consultation note |
| RACI04 | Informed | Receive status or outcome | Does not block execution | Notification note |
| RACI05 | Reviewer | Check artifact against criteria | Does not decide unless also approver | Review findings |
| RACI06 | Approver | Accept or reject final output or gate | Must use explicit criteria | Approval record |
| RACI07 | Escalation owner | Resolve blocker, conflict, or risk | Activated only by trigger | Escalation packet |
| RACI08 | Backup owner | Continue if primary owner unavailable | Must receive current handoff | Backup handoff |
| RACI09 | Observer | Monitor without changing workflow | Cannot silently change criteria | Observation log |
| RACI10 | Auditor | Inspect evidence after or during execution | Does not perform controlled task | Audit trail |

## AGNT AI / Agent Roles

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| AGNT01 | Planner agent | Convert goal into workflow, steps, and checks | Must not execute risky actions without gate | Plan packet |
| AGNT02 | Research agent | Gather, compare, and cite sources | Must separate evidence from inference | Evidence table |
| AGNT03 | Drafting agent | Generate content, prompts, or artifact drafts | Drafts need QA before final use | Draft artifact |
| AGNT04 | Coding agent | Inspect repo, edit scoped files, run checks | Must preserve unrelated user changes | Diff and test result |
| AGNT05 | Data agent | Analyze datasets, metrics, and anomalies | Must state grain, filters, and caveats | Analysis log |
| AGNT06 | Visual agent | Build image2/design/CAD prompt packets | Must preserve source invariants | Visual prompt packet |
| AGNT07 | QA agent | Review output against rubric and evidence | Must cite concrete failures | QA report |
| AGNT08 | Orchestrator agent | Coordinate multiple roles, tools, and handoffs | Must maintain state and dependencies | Orchestration log |
| AGNT09 | Recovery agent | Diagnose failures, repair workflow, and resume | Must document failure path | Recovery note |
| AGNT10 | Teacher agent | Explain process and next action for beginners | Must reduce cognitive load | Teaching handoff |

## HUMN Human Roles

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| HUMN01 | Requester | Provide goal, constraints, and feedback | Not responsible for hidden technical gaps | Request brief |
| HUMN02 | User/operator | Use output in real workflow | Needs clear instructions and limits | User instruction note |
| HUMN03 | Subject matter expert | Validate domain-specific correctness | May not own final delivery | SME review |
| HUMN04 | Reviewer | Inspect artifact against criteria | Must separate opinion from criteria | Review note |
| HUMN05 | Approver | Accept or reject gate/output | Must state approval condition | Approval decision |
| HUMN06 | Client/stakeholder | Provide acceptance feedback or priorities | Cannot be assumed if absent | Stakeholder response |
| HUMN07 | Legal/compliance reviewer | Validate regulated claims or process | Does not replace jurisdiction-specific counsel unless authorized | Compliance note |
| HUMN08 | Finance/business owner | Validate financial assumptions and impact | Must disclose assumptions | Business review |
| HUMN09 | Safety/security reviewer | Validate unsafe, sensitive, or abuse-prone areas | Can stop release | Safety/security note |
| HUMN10 | Maintainer | Keep artifact/workflow current over time | Needs update cadence | Maintenance note |

## TOOL Tool / System Roles

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| TOOLR01 | Search tool | Find current or external evidence | Results require source evaluation | Search log |
| TOOLR02 | Local shell/tool | Inspect or modify local state | Commands need scoped paths and result capture | Command log |
| TOOLR03 | Validator | Check schema, syntax, tests, or required fields | Passing check only proves covered criteria | Validation result |
| TOOLR04 | Generator | Produce image, media, code, text, or document output | Output requires human/QA review when high impact | Generation record |
| TOOLR05 | Parser/extractor | Extract data from files or media | Low-confidence extraction must be flagged | Extraction note |
| TOOLR06 | Renderer/viewer | Show visual, document, or dashboard output | Visual check still needed | Render proof |
| TOOLR07 | Storage/index | Preserve artifacts and search metadata | Must avoid stale or duplicate entries | Index record |
| TOOLR08 | Automation runner | Repeat workflow steps on triggers or batches | Needs failure handling and logs | Automation run log |
| TOOLR09 | Connector/API | Access third-party system or data | Permissions and freshness matter | Connector result |
| TOOLR10 | Monitoring tool | Track ongoing metric, threshold, or status | Alerts need owner and response path | Monitoring note |

## APRV Approval Roles

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| APRV01 | Content approver | Approve text, claims, tone, and publication readiness | Cannot approve unsupported factual claims alone | Content approval |
| APRV02 | Design approver | Approve visual direction, brand, and production specs | Does not certify manufacturing feasibility alone | Design approval |
| APRV03 | Technical approver | Approve architecture, code, deployment, or integration | Needs tests or rationale | Technical approval |
| APRV04 | Data approver | Approve metric logic, dataset use, and caveats | Needs provenance and validation | Data approval |
| APRV05 | Compliance approver | Approve regulated or policy-sensitive output | Needs evidence and caveats | Compliance approval |
| APRV06 | Security approver | Approve secret handling, access, and threat controls | Can block release | Security approval |
| APRV07 | Budget approver | Approve cost, spend, vendor, or resource use | Needs financial assumptions | Budget approval |
| APRV08 | Client approver | Approve client-facing deliverable | Needs clear acceptance criteria | Client signoff |
| APRV09 | Launch approver | Approve go-live or publish step | Needs rollback and monitor plan | Launch approval |
| APRV10 | Exception approver | Approve deviation from normal workflow | Must record reason and risk | Exception approval |

## ROLEREV Review Roles

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| ROLEREV01 | Accuracy reviewer | Check factual correctness | Must cite evidence or uncertainty | Accuracy findings |
| ROLEREV02 | Completeness reviewer | Check coverage against scope | Must name missing areas | Completeness findings |
| ROLEREV03 | Style reviewer | Check tone, voice, and readability | Cannot override factual accuracy | Style findings |
| ROLEREV04 | Format reviewer | Check schema, layout, naming, and file specs | Must use explicit spec | Format findings |
| ROLEREV05 | Risk reviewer | Check legal, financial, safety, privacy, or reputation risk | Can trigger escalation | Risk findings |
| ROLEREV06 | Usability reviewer | Check whether target user can act on output | Must test against a user task | Usability findings |
| ROLEREV07 | Technical reviewer | Check code, architecture, or tool logic | Must inspect relevant files/results | Technical findings |
| ROLEREV08 | Data reviewer | Check metrics, data quality, sample, and assumptions | Must verify calculations where possible | Data findings |
| ROLEREV09 | Visual reviewer | Check image/design/CAD visual fidelity and specs | Must inspect visible output or prompt constraints | Visual findings |
| ROLEREV10 | Prompt reviewer | Check prompt clarity, variables, constraints, and testability | Must include failure cases | Prompt findings |

## EXEC Execution Roles

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| EXEC01 | Single executor | Perform all low-risk steps end to end | Needs QA before final delivery | Execution log |
| EXEC02 | Step executor | Perform one assigned workflow step | Must hand off output clearly | Step output |
| EXEC03 | Batch executor | Process many items consistently | Must track item status and exceptions | Batch manifest |
| EXEC04 | Tool executor | Run scripts, commands, or apps | Must capture parameters and results | Tool run log |
| EXEC05 | Research executor | Conduct source gathering and synthesis | Must preserve search and citation trail | Research log |
| EXEC06 | Creative executor | Generate creative variants or drafts | Must use selection criteria | Variant pack |
| EXEC07 | Data executor | Transform, analyze, or validate data | Must preserve source and transform logic | Data run note |
| EXEC08 | Production executor | Export, publish, deploy, or package final output | Needs approval if public or irreversible | Production record |
| EXEC09 | Recovery executor | Fix failed, blocked, or rejected work | Must document what changed | Recovery log |
| EXEC10 | Maintenance executor | Perform recurring checks and updates | Must follow cadence and thresholds | Maintenance log |

## SME Subject Matter Roles

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| SME01 | Domain expert | Validate specialized domain assumptions | Does not own workflow mechanics by default | Domain review |
| SME02 | Legal SME | Interpret legal/regulatory issues | Needs jurisdiction and caveats | Legal review |
| SME03 | Finance SME | Validate financial logic and assumptions | Needs source and sensitivity | Finance review |
| SME04 | Medical/science SME | Validate scientific or health-related content | Needs evidence level and limits | Science review |
| SME05 | Engineering SME | Validate feasibility, specs, and constraints | Needs technical context | Engineering review |
| SME06 | Security SME | Validate threat model, controls, and abuse paths | Can stop unsafe release | Security review |
| SME07 | Data science SME | Validate methods, metrics, and interpretation | Needs sample and methodology | Method review |
| SME08 | Design/brand SME | Validate visual fit, brand, and usability | Needs target audience and channel | Design review |
| SME09 | Manufacturing/CAD SME | Validate dimensions, materials, tolerances, and production handoff | Needs units and standards | Manufacturing review |
| SME10 | Localization SME | Validate language, market, culture, and locale constraints | Needs target locale | Localization review |

## COMM Communication Roles

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| COMM01 | Status sender | Communicate progress, blockers, and next step | Must not overclaim completion | Status update |
| COMM02 | Decision communicator | Explain selected option and rationale | Must include tradeoffs | Decision message |
| COMM03 | Risk communicator | Notify stakeholders of risk and mitigation | Must avoid hiding residual risk | Risk message |
| COMM04 | Handoff communicator | Transfer current state to next actor | Must include action and artifact links | Handoff message |
| COMM05 | Client communicator | Present output to external/client audience | Must match audience and approval status | Client message |
| COMM06 | Incident communicator | Share incident facts, status, and next update | Must avoid speculation | Incident update |
| COMM07 | Approval requester | Ask for signoff with criteria and options | Must make decision easy | Approval request |
| COMM08 | Rework communicator | Explain rejection, revision path, and owner | Must name concrete changes | Rework note |
| COMM09 | Training communicator | Teach user how to use workflow/output | Must include practice or next action | Training note |
| COMM10 | Archive communicator | Announce where final artifacts and logs live | Must include retrieval path | Archive notice |

## ROLEESC Escalation Roles

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| ROLEESC01 | Blocker escalator | Raise missing input, permission, or source blocker | Must show attempts and needed action | Blocker packet |
| ROLEESC02 | Risk escalator | Escalate high-impact unresolved risk | Must include severity and mitigation | Risk escalation |
| ROLEESC03 | Technical escalator | Escalate build, runtime, integration, or data failure | Must include logs and repro | Technical escalation |
| ROLEESC04 | Compliance escalator | Escalate regulated or policy-sensitive uncertainty | Must include evidence and question | Compliance escalation |
| ROLEESC05 | Scope escalator | Escalate scope conflict or overload | Must propose bounded options | Scope escalation |
| ROLEESC06 | Quality escalator | Escalate failed QA or unacceptable output | Must include criteria and failures | Quality escalation |
| ROLEESC07 | Ownership escalator | Escalate missing accountable owner | Must name impacted decision | Ownership escalation |
| ROLEESC08 | Timeline escalator | Escalate deadline risk or sequencing issue | Must include critical path | Timeline escalation |
| ROLEESC09 | Vendor/tool escalator | Escalate third-party dependency failure | Must include vendor/tool status | Dependency escalation |
| ROLEESC10 | Final escalation owner | Decide when repeated blockers require blocked status | Must follow blocked-audit rules | Escalation closeout |

## HANDR Handoff Roles

| Code | Role pattern | Responsibility | Boundary | Evidence |
|---|---|---|---|---|
| HANDR01 | Upstream handoff owner | Provide complete inputs to execution | Must include assumptions and source status | Upstream handoff |
| HANDR02 | Downstream handoff owner | Receive output and continue workflow | Must confirm acceptance or gaps | Downstream receipt |
| HANDR03 | Cross-functional handoff | Transfer between product, design, engineering, data, or ops | Must include role-specific specs | Cross-functional packet |
| HANDR04 | Human-to-agent handoff | Give agent enough context to act safely | Must include goal, files, constraints | Agent handoff |
| HANDR05 | Agent-to-human handoff | Give human clear outcome, risks, and next action | Must avoid hidden state | Human handoff |
| HANDR06 | Agent-to-agent handoff | Transfer exact state between agents or turns | Must include evidence and next action | Agent handoff packet |
| HANDR07 | Review handoff owner | Send artifact to reviewer with criteria | Must name decision requested | Review handoff |
| HANDR08 | Approval handoff owner | Send artifact to approver with acceptance options | Must include risk and evidence | Approval handoff |
| HANDR09 | Operations handoff owner | Move workflow into ongoing operation | Must include runbook and thresholds | Ops handoff |
| HANDR10 | Archive handoff owner | Preserve final output and make it findable | Must include index/category | Archive handoff |

