# Professional Workflow State Transition Matrix

Use this when a workflow needs explicit state boundaries, transition rules, pause/resume behavior, blocked states, exception handling, or closure discipline. State transitions prevent a workflow from moving forward before the required evidence exists.

Selection rule:

1. Identify the current workflow state.
2. Select the closest state code below.
3. Add its transition rule and exit evidence to the prompt packet.
4. Do not move to the next state until the exit evidence is present or a blocked/exception state is declared.

## INTS Intake States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| INTS01 | New request received | User gives a new task or goal | Capture goal, deliverable, constraints, and urgency | Intake brief |
| INTS02 | Vague request | Goal is broad but action is possible | Sharpen into an execution brief with assumptions | Sharpened brief |
| INTS03 | Blocking ambiguity | Missing detail changes safety or output materially | Ask only the smallest required question | Answer or explicit assumption |
| INTS04 | Multi-goal request | User asks for several outcomes at once | Split into goal lanes and dependencies | Goal lane map |
| INTS05 | Existing-work continuation | Task resumes prior work | Inspect current state before acting | Current-state note |
| INTS06 | User-corrected direction | User changes or narrows the target | Treat newest direction as authoritative | Updated brief |
| INTS07 | Time-sensitive intake | Deadline or live context matters | Prioritize freshness, timing, and fastest safe path | Time-aware plan |
| INTS08 | High-stakes intake | Work affects money, law, health, safety, privacy, or reputation | Add risk gate before execution | Risk brief |
| INTS09 | Tool-dependent intake | Work requires local files, apps, APIs, or web sources | Check tool availability and fallback | Tool readiness note |
| INTS10 | Template/library intake | User wants reusable prompts or workflows | Define category, variables, and index target | Library entry brief |

## CLRS Clarification States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| CLRS01 | No clarification needed | Reasonable assumptions allow progress | Proceed and disclose assumptions later | Assumption note |
| CLRS02 | Single blocker | One missing answer blocks execution | Ask one concise question | User answer |
| CLRS03 | Multiple blockers | Several missing answers block safe execution | Ask up to three prioritized questions | Clarification answers |
| CLRS04 | Preference unknown | Style, format, or depth is unspecified | Choose the conservative default | Default rationale |
| CLRS05 | Audience unknown | Reader or user is unclear | Infer likely audience from task or ask if material | Audience assumption |
| CLRS06 | Source unknown | Required source material is missing | Search local context or request source if unavailable | Source status |
| CLRS07 | Scope conflict | User asks for incompatible outputs or limits | Resolve by priority, latest instruction, or explicit choice | Scope decision |
| CLRS08 | Safety uncertainty | Request may be unsafe or regulated | Route to high-risk validation before acting | Safety route |
| CLRS09 | Freshness uncertainty | Facts may be outdated | Browse or mark as memory/local-only | Freshness evidence |
| CLRS10 | Execution permission unclear | Task may modify files, publish, or trigger external action | Confirm only if action is irreversible or risky | Permission or safe fallback |

## SRCS Source Readiness States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| SRCS01 | No source required | Task can be completed from instruction alone | Proceed with clear assumptions | Source-free note |
| SRCS02 | Local source available | Files, repo, images, or docs are present locally | Inspect authoritative current files | Source inventory |
| SRCS03 | Web source required | Current facts, public sources, or online prompts are needed | Search and cite reliable sources | Web source log |
| SRCS04 | User-provided source | User pastes or uploads material | Treat supplied material as primary | Source capture note |
| SRCS05 | Source incomplete | Required material is partial | Continue with limits or request the missing part | Gap note |
| SRCS06 | Source conflict | Sources disagree | Record conflict and choose resolution path | Conflict map |
| SRCS07 | Source freshness risk | Source may be stale | Verify date/version or refresh online | Freshness check |
| SRCS08 | Sensitive source | Source contains private, regulated, or proprietary data | Minimize, redact, and restrict exposure | Data handling note |
| SRCS09 | Low-quality source | OCR, screenshots, bad scans, or noisy data reduce confidence | Mark uncertainty and verify critical facts | Quality caveat |
| SRCS10 | Source locked | Source set is final for this run | Freeze source list before synthesis | Locked inventory |

## PLNS Planning States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| PLNS01 | Plan not needed | Work is a trivial single step | Execute directly | Completed action |
| PLNS02 | Lightweight plan | Work has a few obvious steps | Create concise ordered plan | Short plan |
| PLNS03 | Multi-phase plan | Work spans phases or deliverables | Define phases, gates, and dependencies | Phase plan |
| PLNS04 | Branching plan | Outcome depends on conditions | Define decision points and fallback branches | Decision tree |
| PLNS05 | Parallel plan | Independent research or reads can run together | Split lanes and merge criteria | Parallel lane map |
| PLNS06 | Tool plan | Execution depends on tools or scripts | Pick tool, input, output, fallback | Tool plan |
| PLNS07 | QA-first plan | Failure cost is high | Define tests or acceptance before execution | QA plan |
| PLNS08 | Human-in-loop plan | Review or approval is required | Place review gates before finalization | Review schedule |
| PLNS09 | Batch plan | Many items need repeated processing | Create manifest, naming, and exception rules | Batch manifest |
| PLNS10 | Resume-safe plan | Work may span turns or sessions | Record state, pending steps, and next action | Resume plan |

## EXST Execution States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| EXST01 | Ready to execute | Plan and inputs are sufficient | Act on the smallest useful step | Step output |
| EXST02 | Local edit execution | Files must be created or changed | Edit scoped files and preserve unrelated changes | File diff or changed file |
| EXST03 | Research execution | Claims need evidence | Gather, compare, and cite sources | Evidence table |
| EXST04 | Generation execution | New content, prompt, image brief, or artifact is created | Generate against output spec | Draft artifact |
| EXST05 | Transformation execution | Existing material must be rewritten, converted, or cleaned | Preserve meaning and record transforms | Transformed artifact |
| EXST06 | Analysis execution | Inputs need interpretation | Analyze with explicit method and caveats | Analysis result |
| EXST07 | Automation execution | Script/tool performs the work | Run with bounded inputs and capture result | Run log |
| EXST08 | Batch execution | Multiple items are processed | Track each item status and failure | Batch result table |
| EXST09 | Collaborative execution | User or reviewer participates during work | Pause only at defined gates | Review interaction |
| EXST10 | Degraded execution | Ideal path is unavailable but useful progress is possible | Deliver limited output with limits and follow-up | Degraded output note |

## QAST Quality Check States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| QAST01 | Self-check required | Any nontrivial deliverable exists | Compare output against brief and criteria | QA checklist |
| QAST02 | Test execution | Code, data, automation, or structured output changed | Run relevant tests or validators | Test result |
| QAST03 | Source verification | Claims or sourced content exist | Check each critical claim against evidence | Verification table |
| QAST04 | Format validation | Output must match a schema, file type, or template | Validate structure and required fields | Format check |
| QAST05 | Visual validation | Image, UI, design, CAD, or layout output exists | Inspect visible details and constraints | Visual QA note |
| QAST06 | Consistency check | Multiple artifacts or sections must align | Compare terminology, numbers, specs, and decisions | Consistency note |
| QAST07 | Risk check | Work has high-impact consequences | Apply the relevant risk gate | Risk QA result |
| QAST08 | Completeness check | User requested broad coverage | Check category coverage and known gaps | Coverage report |
| QAST09 | Regression check | Existing behavior or library integrity could be affected | Confirm old routes still work | Regression note |
| QAST10 | Final readiness check | Work appears complete | Confirm deliverable, evidence, risks, and next step | Readiness note |

## APST Approval States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| APST01 | No approval needed | Output is low-risk and within requested scope | Deliver after QA | QA pass |
| APST02 | User approval needed | Irreversible, costly, public, or preference-heavy action remains | Ask for explicit approval | Approval response |
| APST03 | Expert review needed | Domain judgment exceeds available evidence | Prepare expert packet | Expert review packet |
| APST04 | Compliance approval needed | Legal, privacy, finance, safety, or regulated content appears | Require compliance review before final use | Compliance packet |
| APST05 | Brand approval needed | Public creative, marketing, or brand asset is produced | Check brand rules and approval owner | Brand approval note |
| APST06 | Technical approval needed | Architecture, security, deployment, or shared code changes matter | Route to technical review | Technical review note |
| APST07 | Data approval needed | Dataset handling or metric definition affects decisions | Confirm data owner or methodology | Data approval note |
| APST08 | Client/stakeholder approval needed | External stakeholder acceptance is required | Package deliverable and decision ask | Stakeholder packet |
| APST09 | Conditional approval | Output is acceptable with caveats | Record caveats and conditions | Conditional signoff |
| APST10 | Approval rejected | Reviewer/user rejects output | Capture reason and transition to rework | Rejection note |

## HDST Handoff States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| HDST01 | User handoff | Final or interim output is ready | Explain what exists, where, and how to use it | User handoff note |
| HDST02 | Developer handoff | Code or technical work needs continuation | Include files, tests, risks, and next steps | Developer handoff |
| HDST03 | Designer handoff | Design/image/CAD asset moves to production | Include specs, assets, variants, constraints | Designer handoff |
| HDST04 | Research handoff | Research supports another writing or decision step | Include sources, findings, gaps, citations | Research handoff |
| HDST05 | Operations handoff | Runbook or process enters operation | Include owner, cadence, thresholds, escalation | Ops handoff |
| HDST06 | Review handoff | Artifact needs external review | Include review criteria and decision options | Review packet |
| HDST07 | Prompt-library handoff | Prompt/workflow should be reused | Include category, variables, examples, tests | Library entry |
| HDST08 | Automation handoff | Automated process is ready for repeat use | Include trigger, inputs, logs, failure handling | Automation handoff |
| HDST09 | Resume handoff | Work will continue later | Include exact state and next action | Resume handoff |
| HDST10 | Archive handoff | Work must be preserved | Include final files, sources, logs, and version | Archive package |

## BLST Blocked States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| BLST01 | Waiting for user input | User answer is required to continue safely | State blocker and smallest needed input | User response |
| BLST02 | Missing source blocker | Required file/source is absent | Identify missing source and fallback | Source supplied or fallback chosen |
| BLST03 | Tool unavailable blocker | Required tool, app, API, or runtime is unavailable | Try viable fallback before blocking | Tool restored or fallback result |
| BLST04 | Permission blocker | Action requires approval or access | Ask for permission or provide safe alternative | Permission response |
| BLST05 | Contradictory instruction blocker | Instructions conflict materially | Ask to resolve or apply higher-priority rule | Resolution note |
| BLST06 | Safety blocker | Request cannot be fulfilled safely as asked | Refuse unsafe part and offer safe alternative | Safe alternative |
| BLST07 | Evidence blocker | Claim or recommendation lacks enough evidence | Gather more evidence or limit conclusion | Evidence update |
| BLST08 | External dependency blocker | Third-party state or human owner is needed | Record dependency and next owner | Dependency note |
| BLST09 | Scope overload blocker | Requested scope cannot be completed in one pass | Make bounded progress and leave active goal | Progress note |
| BLST10 | Repeated blocker | Same blocker repeats across goal turns | Follow blocked-audit rules before marking blocked | Blocked audit evidence |

## ERST Error / Exception States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| ERST01 | Command failure | Shell/tool command fails | Read error, adjust command, retry if safe | Failure or fix log |
| ERST02 | Validation failure | Test, lint, schema, or validator fails | Fix root cause or report residual risk | Validation result |
| ERST03 | File conflict | Current files differ from expected state | Inspect current file and preserve user changes | Conflict resolution |
| ERST04 | Partial write | Artifact may be incomplete | Inspect file boundaries and repair missing content | Complete artifact |
| ERST05 | Data mismatch | Totals, schema, or source facts disagree | Reconcile or flag discrepancy | Reconciliation note |
| ERST06 | Output quality failure | Draft does not meet quality bar | Diagnose failure class and revise | Revised output |
| ERST07 | Citation failure | Source, quote, or claim link is broken | Replace, remove, or caveat claim | Citation fix |
| ERST08 | Runtime failure | App/server/build/test environment fails | Inspect logs and fix or isolate cause | Runtime status |
| ERST09 | Policy exception | Requested output crosses safety or policy boundary | Provide compliant alternative | Policy-safe output |
| ERST10 | Recovery complete | Exception has been handled | Return to prior state or close with risk | Recovery note |

## RSTT Resume / Continuation States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| RSTT01 | Context resume | A previous session or compacted context resumes | Inspect authoritative files before relying on summary | Current-state proof |
| RSTT02 | Plan resume | Existing plan continues | Update statuses before acting | Updated plan |
| RSTT03 | Artifact resume | Existing artifact is extended | Read tail/head and preserve structure | Artifact state note |
| RSTT04 | Goal resume | Active goal continues across turns | Make concrete progress without redefining success | Goal progress note |
| RSTT05 | Interrupted edit resume | Prior edit may have been truncated | Inspect file completeness before patching | Completeness check |
| RSTT06 | Validation resume | Prior validation was partial or stale | Rerun relevant current-state checks | Fresh validation |
| RSTT07 | Research resume | Prior research may be stale | Refresh current facts when needed | Updated source log |
| RSTT08 | Batch resume | Bulk processing continues after interruption | Skip completed items and continue manifest | Updated manifest |
| RSTT09 | Review resume | Prior review findings remain open | Recheck each finding against current artifact | Finding status |
| RSTT10 | Handoff resume | Another agent/user continues work | Use handoff packet and verify assumptions | Resumed action |

## CLST Closure States

| Code | State | Enter when | Transition rule | Exit evidence |
|---|---|---|---|---|
| CLST01 | Ready to close | Deliverable exists and checks passed | Summarize outcome, files, tests, and risks | Final response |
| CLST02 | Partial close | Useful output exists but scope remains open | Report progress and next best area | Partial close note |
| CLST03 | Close with caveat | Output is valid under assumptions or limits | State caveats plainly | Caveat note |
| CLST04 | Close with risk | Residual risk remains | Name risk, owner, and mitigation | Risk closeout |
| CLST05 | Close after rejection | Work was rejected and revised or stopped | Record rejection reason and status | Rejection closeout |
| CLST06 | Close after blocked audit | Strict blocked criteria are met | Mark blocked only under goal rules | Blocked status |
| CLST07 | Close after verification | Tests/validators/evidence prove completion | Include verification summary | Verification summary |
| CLST08 | Close to archive | Work should be preserved for reuse | Store index, template, or archive entry | Archive note |
| CLST09 | Close to next iteration | New improvement area is known | Leave specific next step without claiming completion | Next-iteration note |
| CLST10 | Complete goal close | Full objective is proven complete | Mark goal complete only with current evidence | Completion audit |
