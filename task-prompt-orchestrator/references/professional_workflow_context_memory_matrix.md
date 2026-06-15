# Professional Workflow Context and Memory Matrix

Use this when a workflow must preserve state across steps, files, sessions, agents, versions, or long-running goals. Context and memory rules prevent stale assumptions, lost decisions, repeated discovery, and broken continuation.

Selection rule:

1. Identify what context must survive beyond the immediate step.
2. Select the closest context/memory code.
3. Add capture, refresh, storage, and invalidation rules to the prompt packet.
4. Verify current authoritative state before using older memory.

## CUR Current-State Memory

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| CUR01 | Current goal | Store objective, scope, and success criteria | Refresh when user changes direction | Goal state note |
| CUR02 | Current plan | Store steps, status, blockers, next action | Refresh after each completed step | Updated plan |
| CUR03 | Current artifact state | Store files/artifacts created or modified | Inspect file before continuing | Artifact state note |
| CUR04 | Current source set | Store sources used and lock status | Refresh when source changes or freshness matters | Source inventory |
| CUR05 | Current validation state | Store checks run, results, skipped checks | Rerun after edits or stale checks | Validation summary |
| CUR06 | Current risk state | Store open risks and mitigations | Refresh when impact/source changes | Risk register |
| CUR07 | Current owner state | Store owners, reviewers, approvers | Refresh when handoff changes | RACI note |
| CUR08 | Current dependency state | Store upstream/downstream blockers | Refresh when dependency changes | Dependency map |
| CUR09 | Current decision state | Store decisions and rationale | Refresh when new evidence appears | Decision log |
| CUR10 | Current closeout state | Store done/not done/evidence/follow-up | Refresh before final response | Closeout note |

## CTXSUM Context Compression

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| CTXSUM01 | Goal summary | Compress objective without narrowing scope | Recheck against original request | Goal summary |
| CTXSUM02 | Source summary | Summarize sources with citations/status | Reopen source for critical facts | Source digest |
| CTXSUM03 | File summary | Summarize file purpose and key content | Re-read file before editing | File digest |
| CTXSUM04 | Decision summary | Summarize decisions and unresolved tradeoffs | Recheck if assumptions change | Decision digest |
| CTXSUM05 | Progress summary | Summarize completed/pending/blockers | Update after each work segment | Progress digest |
| CTXSUM06 | Risk summary | Summarize risks, gates, caveats | Refresh before public/high-stakes output | Risk digest |
| CTXSUM07 | QA summary | Summarize checks and failure history | Rerun checks after changes | QA digest |
| CTXSUM08 | Handoff summary | Summarize state for next human/agent | Verify before resuming | Handoff digest |
| CTXSUM09 | Prompt summary | Summarize reusable prompt variables/tests | Update after prompt changes | Prompt digest |
| CTXSUM10 | Library summary | Summarize categories and coverage gaps | Refresh after index changes | Library digest |

## IDX Index Memory

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| IDX01 | Artifact index | Store path, title, type, status | Refresh after file moves/edits | Artifact index row |
| IDX02 | Prompt index | Store category, use case, variables, path | Refresh after prompt update | Prompt index row |
| IDX03 | Workflow index | Store workflow dimension, codes, use case | Refresh after matrix changes | Workflow index row |
| IDX04 | Source index | Store source, date, relevance, reliability | Refresh when source set changes | Source index row |
| IDX05 | Decision index | Store decisions by topic and date | Refresh when reversed/updated | Decision index row |
| IDX06 | Risk index | Store risks by domain and owner | Refresh when mitigated/closed | Risk index row |
| IDX07 | Template index | Store reusable templates and examples | Refresh when template changes | Template index row |
| IDX08 | Failure index | Store recurring failures and fixes | Refresh after recovery | Failure index row |
| IDX09 | Metrics index | Store observed metrics and thresholds | Refresh after monitoring run | Metrics index row |
| IDX10 | Archive index | Store final package, version, retrieval path | Refresh after archive changes | Archive index row |

## PREF Preference Memory

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| PREF01 | Output style preference | Store preferred depth, tone, structure | Refresh when user corrects style | Style preference |
| PREF02 | Workflow preference | Store preferred planning/execution balance | Refresh when user redirects process | Workflow preference |
| PREF03 | Clarification preference | Store when user wants questions vs assumptions | Refresh after correction | Clarification rule |
| PREF04 | Language preference | Store language, terminology, locale | Refresh on locale/task shift | Language note |
| PREF05 | Evidence preference | Store citation/source rigor expected | Refresh by risk/domain | Evidence rule |
| PREF06 | File organization preference | Store indexing/path/naming habits | Refresh when project structure changes | Organization note |
| PREF07 | Risk tolerance preference | Store conservative/aggressive defaults | Refresh for high-stakes tasks | Risk preference |
| PREF08 | UI/format preference | Store tables, markdown, diagrams, code blocks | Refresh when output type changes | Format note |
| PREF09 | Domain preference | Store recurring domain focus | Refresh when new domain appears | Domain note |
| PREF10 | Follow-up preference | Store desired next-step style | Refresh when user asks different cadence | Follow-up note |

## VERS Version Memory

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| VERS01 | Artifact version | Store version/date/change summary | Refresh after every material edit | Version note |
| VERS02 | Prompt version | Store prompt revision and tests | Refresh after prompt tuning | Prompt changelog |
| VERS03 | Workflow version | Store workflow matrix/version changes | Refresh after matrix expansion | Workflow changelog |
| VERS04 | Source version | Store source date/version/access status | Refresh when currentness matters | Source version note |
| VERS05 | Decision version | Store superseded decisions and reason | Refresh after reversal | Decision history |
| VERS06 | Index version | Store index update time and coverage count | Refresh after new entries | Index version note |
| VERS07 | Template version | Store template variables and examples | Refresh after reuse feedback | Template version |
| VERS08 | Validation version | Store validator version and scope | Refresh when checks change | Validation version |
| VERS09 | Environment version | Store tool/runtime/platform versions | Refresh when environment changes | Environment note |
| VERS10 | Archive version | Store final package version and retention rule | Refresh on archive update | Archive version |

## CTXDEC Decision Memory

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| CTXDEC01 | Chosen route | Store selected workflow/domain route | Re-evaluate when user changes scope | Route decision |
| CTXDEC02 | Rejected option | Store rejected alternative and reason | Revisit if assumptions change | Rejection rationale |
| CTXDEC03 | Tradeoff decision | Store criteria, option, rationale | Refresh when criteria change | Tradeoff log |
| CTXDEC04 | Approval decision | Store approver, condition, date, artifact | Refresh if artifact changes | Approval log |
| CTXDEC05 | Risk decision | Store accept/mitigate/escalate/avoid choice | Refresh when risk changes | Risk decision |
| CTXDEC06 | Exception decision | Store deviation, reason, owner | Refresh at closeout | Exception log |
| CTXDEC07 | Clarification decision | Store asked/skipped question and why | Refresh if output fails expectation | Clarification log |
| CTXDEC08 | Tool decision | Store chosen tool and fallback | Refresh if tool fails | Tool decision |
| CTXDEC09 | Automation decision | Store manual/template/automation choice | Refresh after frequency/risk changes | Automation decision |
| CTXDEC10 | Closure decision | Store complete/partial/blocked rationale | Refresh before goal status change | Closure decision |

## EVID Evidence Memory

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| EVID01 | Claim evidence | Store claim-to-source mapping | Refresh when claim changes | Evidence table |
| EVID02 | File evidence | Store paths and inspected lines/sections | Re-read before edit/citation | File evidence note |
| EVID03 | Command evidence | Store command, cwd, output summary, exit result | Rerun after relevant change | Command log |
| EVID04 | Test evidence | Store test name, result, coverage limit | Rerun after code/content change | Test summary |
| EVID05 | Visual evidence | Store screenshot/image facts and QA result | Reinspect after visual change | Visual evidence note |
| EVID06 | Data evidence | Store metric calculation and source grain | Refresh when dataset changes | Data evidence note |
| EVID07 | Approval evidence | Store signoff artifact and condition | Refresh if artifact changes | Approval evidence |
| EVID08 | Risk evidence | Store risk basis and mitigation proof | Refresh when context changes | Risk evidence |
| EVID09 | Freshness evidence | Store source date/currentness check | Refresh for volatile facts | Freshness note |
| EVID10 | Completion evidence | Store requirement-to-proof map | Refresh before final close | Completion audit |

## RESM Resume Memory

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| RESM01 | Next action | Store exact next step | Refresh after any user message | Next-action note |
| RESM02 | Pending blockers | Store blocker, owner, needed input | Refresh after each attempt | Blocker list |
| RESM03 | Partial edits | Store files possibly incomplete | Inspect before patching | Edit state note |
| RESM04 | Batch progress | Store processed/pending/failed items | Refresh from manifest | Batch status |
| RESM05 | Research progress | Store searched sources and gaps | Refresh with current search if needed | Research status |
| RESM06 | Validation progress | Store passed/failed/skipped checks | Refresh before claiming readiness | Validation status |
| RESM07 | Review progress | Store findings and resolution state | Refresh after fixes | Review status |
| RESM08 | Automation progress | Store runs, failures, retry state | Refresh from logs | Automation status |
| RESM09 | Handoff progress | Store receiver and transferred artifacts | Refresh after response | Handoff status |
| RESM10 | Goal progress | Store progress against full objective | Refresh before goal update | Goal progress |

## INVALID Invalidation Rules

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| INVALID01 | User correction invalidates prior plan | Mark prior plan stale | Rebuild from newest user direction | Updated plan |
| INVALID02 | File edit invalidates prior validation | Mark tests/checks stale | Rerun relevant checks | Fresh validation |
| INVALID03 | Source update invalidates synthesis | Mark source conclusions stale | Refresh source and re-synthesize | Updated synthesis |
| INVALID04 | Scope change invalidates coverage count | Mark coverage report stale | Recount current artifacts | Fresh count |
| INVALID05 | Risk change invalidates approval | Mark approval conditional/stale | Re-approve if needed | Approval refresh |
| INVALID06 | Tool failure invalidates automation path | Mark automation route stale | Choose fallback/retry | Tool status |
| INVALID07 | Time passage invalidates freshness | Mark volatile facts stale | Browse/refresh source | Freshness check |
| INVALID08 | Handoff change invalidates owner map | Mark RACI stale | Update owner/reviewer/approver | RACI refresh |
| INVALID09 | Template change invalidates examples | Mark examples stale | Re-test representative examples | Example QA |
| INVALID10 | Goal completion claim invalidates active progress | Re-audit requirements | Keep goal active unless proven complete | Completion audit |

## PRIV Privacy / Access Memory

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| PRIV01 | Sensitive data memory | Store only necessary minimized facts | Refresh redaction before sharing | Data minimization note |
| PRIV02 | Redacted memory | Store redacted version and redaction rule | Refresh when fields change | Redaction note |
| PRIV03 | Access-scoped memory | Store who can use artifact/context | Refresh on handoff/sharing | Access note |
| PRIV04 | Secret-safe memory | Do not store secrets; store existence/status only | Refresh if secret handling changes | Secret handling note |
| PRIV05 | Regulated memory | Store rule, jurisdiction, caveat, approval | Refresh with legal/policy changes | Compliance note |
| PRIV06 | Retention memory | Store keep/delete date and owner | Refresh at retention trigger | Retention note |
| PRIV07 | Consent memory | Store permission scope and source | Refresh if use changes | Consent note |
| PRIV08 | External-sharing memory | Store recipient and allowed content | Refresh before sharing externally | Sharing note |
| PRIV09 | Audit-minimal memory | Store enough evidence without overexposure | Refresh during audit | Minimal audit packet |
| PRIV10 | Deletion memory | Store deletion target and recovery/manifest | Refresh after cleanup | Deletion manifest |

## CROSS Cross-Context Transfer

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| CROSS01 | Agent-to-agent transfer | Store objective, state, evidence, next action | Receiving agent verifies files/state | Agent handoff |
| CROSS02 | Thread-to-thread transfer | Store links, artifacts, decisions, open issues | New thread inspects current files | Thread handoff |
| CROSS03 | Human-to-agent transfer | Store user intent and source materials | Agent confirms current state | User handoff |
| CROSS04 | Agent-to-human transfer | Store outcome, files, checks, caveats | Human can act without hidden context | Human handoff |
| CROSS05 | Project-to-library transfer | Store reusable workflow/prompt/index metadata | Verify category and examples | Library entry |
| CROSS06 | Draft-to-production transfer | Store specs, approvals, QA, export path | Production owner verifies readiness | Production handoff |
| CROSS07 | Local-to-web transfer | Store local artifact and public/channel requirements | Verify before publishing | Publish packet |
| CROSS08 | Research-to-writing transfer | Store claims, evidence, gaps, citations | Writer verifies claim support | Research handoff |
| CROSS09 | Design-to-engineering transfer | Store specs, assets, constraints, QA | Engineering verifies feasibility | Design handoff |
| CROSS10 | Ops-to-archive transfer | Store run history, final status, retention | Archive owner verifies retrieval | Archive handoff |

## LEARN Memory Learning Loop

| Code | Memory type | Capture rule | Refresh rule | Evidence |
|---|---|---|---|---|
| LEARN01 | Correction learning | Capture user corrections as candidate rules | Apply only when pattern repeats or user asks memory update | Correction note |
| LEARN02 | Failure learning | Capture recurring failure and fix | Add prevention to workflow | Failure lesson |
| LEARN03 | Preference learning | Capture stable user preference | Refresh with newer correction | Preference update |
| LEARN04 | Quality learning | Capture QA findings and improved checklist | Refresh after benchmark | QA lesson |
| LEARN05 | Source learning | Capture useful source types and gaps | Refresh by domain | Source lesson |
| LEARN06 | Prompt learning | Capture prompt variants and test outcomes | Refresh after new examples | Prompt lesson |
| LEARN07 | Automation learning | Capture manual repetition candidates | Refresh after usage data | Automation candidate |
| LEARN08 | Domain learning | Capture domain-specific nuance | Refresh with SME/user correction | Domain note |
| LEARN09 | Index learning | Capture search misses and taxonomy gaps | Refresh index/tag rules | Index improvement |
| LEARN10 | Retirement learning | Capture outdated memories/templates | Mark deprecated or archive | Retirement note |
