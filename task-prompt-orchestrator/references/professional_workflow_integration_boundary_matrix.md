# Professional Workflow Integration Boundary Matrix

Use this when a workflow must connect to local files, web sources, APIs, databases, design tools, communication channels, automation platforms, permission systems, import/export formats, synchronization points, monitoring systems, human systems, or publishing environments. Integration boundaries prevent workflow steps from assuming unavailable or unsafe connections.

Selection rule:

1. Identify the system boundary the workflow crosses.
2. Select the closest integration code.
3. Add interface, access, input/output format, failure mode, and verification to the prompt packet.
4. Do not treat integration as complete until the downstream system can consume the output or the fallback path is documented.

## FILEINT File / Filesystem Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| FILEINT01 | Local file read | Exact path, encoding, purpose | Wrong/stale file | File exists and content inspected |
| FILEINT02 | Local file write | Target path, format, overwrite rule | Accidental overwrite | File written and reopened |
| FILEINT03 | Directory scan | Root, filters, recursion limit | Missed or excessive files | File list sampled |
| FILEINT04 | Archive/package | Include list, version, manifest | Missing dependency | Manifest verified |
| FILEINT05 | Large file | Size, chunking, parser | Truncation or memory issue | Row/page/chunk count |
| FILEINT06 | Binary/media file | Viewer/parser and metadata | Misread content | Visual/media inspection |
| FILEINT07 | Spreadsheet file | Sheets, columns, formulas | Hidden sheet/formula loss | Workbook validation |
| FILEINT08 | Document file | Format, styles, comments/tracks | Formatting loss | Render/open check |
| FILEINT09 | CAD/design file | Units, layers, views, export target | Unit/spec mismatch | CAD/design QA |
| FILEINT10 | File retention | Keep/delete, manifest, restore path | Irreversible deletion | Retention record |

## WEBINT Web / Public Source Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| WEBINT01 | Web search | Query, recency, source quality | Irrelevant/stale result | Source date checked |
| WEBINT02 | Web page read | URL, relevant sections, access | Paywall/dynamic content | Page opened/excerpted |
| WEBINT03 | PDF/web document | URL, version/date, citation | Wrong version | Version recorded |
| WEBINT04 | Official source | Authority, page, effective date | Secondary-source drift | Official page cited |
| WEBINT05 | News/current source | Date, event time, multiple sources | Outdated claim | Recent source comparison |
| WEBINT06 | Marketplace/library source | Item, license, metadata | Rights mismatch | License/usage checked |
| WEBINT07 | Social/community source | Post/thread, context, reliability | Anecdote overgeneralized | Caveat and source type |
| WEBINT08 | Web screenshot/reference | URL, visible content, timestamp | Visual drift | Screenshot/time note |
| WEBINT09 | Web form/process | Fields, submission rules, confirmation | Failed submission | Confirmation captured |
| WEBINT10 | Web fallback | Offline/local alternative | No access | Fallback result |

## APIINT API / Connector Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| APIINT01 | REST API | Endpoint, method, params, auth status | Wrong payload | Response schema checked |
| APIINT02 | GraphQL API | Query, variables, schema | Missing field | Response fields checked |
| APIINT03 | MCP/tool connector | Tool name, schema, arguments | Tool mismatch | Tool result inspected |
| APIINT04 | Rate-limited API | Limits, retry, batching | Throttle/failure | Rate plan |
| APIINT05 | Paginated API | Cursor/page, total, stop rule | Missing pages | Page count/reconciliation |
| APIINT06 | Webhook | Event, payload, signature, retry | Missed/duplicate event | Delivery log |
| APIINT07 | Async job API | Job id, polling, timeout | Orphaned job | Job status/result |
| APIINT08 | API version | Version, deprecation, compatibility | Breaking change | Version recorded |
| APIINT09 | API error handling | Error codes, retry/fallback | Silent failure | Error path tested |
| APIINT10 | API audit | Request id, actor, timestamp | Untraceable action | Audit log |

## DBINT Database / Data Warehouse Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| DBINT01 | Table read | Database, table, columns, filters | Wrong table/grain | Sample rows inspected |
| DBINT02 | SQL query | Runnable SQL, joins, filters | Bad join/logic | Query reviewed |
| DBINT03 | Metric layer | Metric definition, grain, denominator | Metric drift | Metric definition cited |
| DBINT04 | Data export | Format, columns, row count | Partial export | Row count reconciled |
| DBINT05 | Data import | Schema, types, constraints | Bad load | Load validation |
| DBINT06 | Sensitive data query | Need-to-know fields, redaction | PII exposure | Data minimization |
| DBINT07 | Incremental refresh | Cursor/watermark, freshness | Duplicate/missed rows | Watermark check |
| DBINT08 | Data lineage | Source, transform, owner | Untraceable output | Lineage note |
| DBINT09 | Query cost | Runtime/cost limits | Expensive query | Cost estimate/limit |
| DBINT10 | Database fallback | Extract/sample/proxy source | Access unavailable | Fallback caveat |

## DESIGNINT Design / CAD / Media Tool Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| DESIGNINT01 | Figma/design file | File/frame, components, tokens | Wrong frame/style drift | Frame inspected |
| DESIGNINT02 | CAD system | Units, views, dimensions, tolerances | Unit/tolerance error | CAD spec check |
| DESIGNINT03 | Image generation | Source image, invariants, prompt, negatives | Identity/spec drift | Visual QA |
| DESIGNINT04 | Image editing | Input image, edit region, preserve rules | Unwanted mutation | Before/after check |
| DESIGNINT05 | Video workflow | Duration, aspect, scenes, audio | Timing/aspect mismatch | Render preview |
| DESIGNINT06 | Audio workflow | Script, voice, timing, format | Timing/noise issue | Playback check |
| DESIGNINT07 | Slide/design export | Size, format, resolution | Export mismatch | Export opened |
| DESIGNINT08 | Asset library | License, brand, version | Wrong/unlicensed asset | Asset metadata |
| DESIGNINT09 | Production handoff | Specs, materials, dielines, callouts | Manufacturing ambiguity | Production QA |
| DESIGNINT10 | Design fallback | Text/spec prompt when tool unavailable | Tool gap | Fallback deliverable |

## COMMINT Communication Channel Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| COMMINT01 | Email | Recipient, subject, body, attachments | Wrong recipient/context | Draft/review |
| COMMINT02 | Chat/Slack/Teams | Channel, audience, thread context | Misrouted update | Channel/thread noted |
| COMMINT03 | Ticketing/Jira/Linear | Project, issue type, fields, status | Bad triage | Ticket fields verified |
| COMMINT04 | Calendar | Timezone, attendees, agenda | Wrong time/attendees | Calendar details checked |
| COMMINT05 | Document comment | Target doc, section, comment type | Lost context | Comment target clear |
| COMMINT06 | Client message | Audience, approval status, caveats | Overpromise | Message reviewed |
| COMMINT07 | Status dashboard | Metric, status, owner, cadence | Stale status | Updated timestamp |
| COMMINT08 | Notification trigger | Event, recipient, threshold | Alert fatigue/missed alert | Notification test |
| COMMINT09 | Public post | Channel, audience, approval, claims | Public claim risk | Approval/evidence |
| COMMINT10 | Communication fallback | Alternate channel/owner | Channel unavailable | Fallback sent/logged |

## AUTOINT Automation / Orchestration Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| AUTOINT01 | Scheduled automation | Schedule, owner, input source | Runs at wrong time | Schedule verified |
| AUTOINT02 | Event automation | Event source, filter, payload | False trigger | Event test |
| AUTOINT03 | Batch automation | Manifest, chunking, retry | Item loss/duplicate | Batch reconciliation |
| AUTOINT04 | Agentic workflow | Goal, tools, state, stop rules | Runaway/unsafe action | Guardrails logged |
| AUTOINT05 | CI/CD automation | Build/test/deploy steps | Failed release | Pipeline result |
| AUTOINT06 | RPA/browser automation | Steps, selectors, fallback | UI drift | Run proof |
| AUTOINT07 | Queue worker | Queue, concurrency, dead letter | Stuck messages | Queue metrics |
| AUTOINT08 | Idempotency | Key, duplicate behavior | Duplicate side effects | Idempotency check |
| AUTOINT09 | Automation monitoring | Logs, alerts, owner | Silent failure | Monitor configured |
| AUTOINT10 | Automation shutdown | Pause/cancel/rollback | Cannot stop process | Manual control tested |

## AUTHINT Auth / Permission Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| AUTHINT01 | User permission | User approval and scope | Unauthorized action | Permission note |
| AUTHINT02 | File access | Read/write permission | Access denied | Access check |
| AUTHINT03 | API credential | Credential presence/status only | Secret exposure | Secret-safe handling |
| AUTHINT04 | Role-based access | Role, resource, allowed action | Over-permission | Least-privilege note |
| AUTHINT05 | External sharing | Recipient, asset class, rights | Data leak | Sharing approval |
| AUTHINT06 | Compliance approval | Rule, approver, artifact | Policy violation | Compliance signoff |
| AUTHINT07 | Audit identity | Actor/tool/action timestamp | Unattributed action | Audit record |
| AUTHINT08 | Temporary access | Expiry, purpose, revocation | Access persists too long | Expiry tracked |
| AUTHINT09 | Consent boundary | Consent scope and use | Use beyond consent | Consent note |
| AUTHINT10 | Permission fallback | Safe subset or simulated output | Blocked by access | Fallback documented |

## XPORT Import / Export Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| XPORT01 | Markdown export | Headings, tables, links | Broken render | Render/preview |
| XPORT02 | CSV export | Columns, delimiter, encoding | Bad parse | CSV parsed |
| XPORT03 | JSON export | Schema, types, nesting | Invalid JSON | Parser passes |
| XPORT04 | DOCX/PDF export | Layout, fonts, pagination | Formatting loss | File opened/rendered |
| XPORT05 | PPTX export | Slide size, media, notes | Broken deck | Deck opened/rendered |
| XPORT06 | Image export | Resolution, aspect, format | Wrong size/quality | Image metadata |
| XPORT07 | CAD export | Units, layers, dimensions | Manufacturing mismatch | CAD QA |
| XPORT08 | Web/app export | Build files, route, assets | Broken app/page | Smoke test |
| XPORT09 | Package export | Manifest, dependencies, checksum/status | Missing file | Package verified |
| XPORT10 | Import validation | Source import format and schema | Bad ingest | Import check |

## SYNCINT Sync / State Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| SYNCINT01 | State sync | Current state, owner, timestamp | Stale state | State timestamp |
| SYNCINT02 | File sync | Local/cloud/repo paths | Version conflict | Version checked |
| SYNCINT03 | Index sync | Matrix/index/library entries | Search gap | Index row exists |
| SYNCINT04 | Source sync | Source set and freshness | Outdated source | Freshness note |
| SYNCINT05 | Decision sync | Decision log and affected artifacts | Old decision used | Decision update |
| SYNCINT06 | Review sync | Findings and resolution status | Reopened issue lost | Finding status |
| SYNCINT07 | Approval sync | Approval status and artifact version | Approval on old artifact | Approval version |
| SYNCINT08 | Automation sync | Job/run state and logs | Duplicate/missing run | Run id/log |
| SYNCINT09 | Cross-thread sync | Handoff between agents/threads | Context drift | Handoff verification |
| SYNCINT10 | Archive sync | Final artifact and archive/index | Lost deliverable | Archive retrieval |

## MONINT Monitoring / Observability Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| MONINT01 | Log integration | Log source, fields, retention | Missing logs | Log sample |
| MONINT02 | Metric integration | Metric, source, threshold | Wrong metric | Metric definition |
| MONINT03 | Alert integration | Trigger, recipient, severity | Alert fatigue/missed alert | Alert test |
| MONINT04 | Dashboard integration | Dataset, chart, refresh | Stale dashboard | Timestamp/refresh |
| MONINT05 | QA monitor | Quality score, sample rule | Quality drift | QA trend |
| MONINT06 | Cost monitor | Usage/cost source, threshold | Budget surprise | Cost alert |
| MONINT07 | Freshness monitor | Source age, threshold | Stale output | Freshness alert |
| MONINT08 | Error monitor | Error type/rate, owner | Silent failure | Error trend |
| MONINT09 | Adoption monitor | Usage/search/action event | Unknown adoption | Adoption metric |
| MONINT10 | Outcome monitor | Business/user outcome metric | Activity without value | Outcome report |

## HUMANINT Human System Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| HUMANINT01 | Human intake | Form/question/process for request | Missing context | Intake complete |
| HUMANINT02 | Human review | Reviewer, criteria, artifact | Opinion-only review | Review checklist |
| HUMANINT03 | Human approval | Approver, decision options, deadline | Unclear approval | Approval record |
| HUMANINT04 | Human operation | Operator, runbook, tools | Execution inconsistency | Runbook followed |
| HUMANINT05 | Human escalation | Escalation owner, trigger, packet | Blocker lingers | Escalation sent |
| HUMANINT06 | Human training | Audience, guide, practice | Misuse of workflow | Training evidence |
| HUMANINT07 | Human feedback | Feedback channel, taxonomy | Feedback lost | Feedback logged |
| HUMANINT08 | Human exception handling | Owner, exception class, response | Exception unmanaged | Exception status |
| HUMANINT09 | Human handoff | Receiver, next action, context | Handoff confusion | Receiver can act |
| HUMANINT10 | Human fallback | Manual path when automation fails | No fallback | Manual path documented |

## RELEASEINT Release / Publishing Integration

| Code | Boundary | Interface requirement | Failure mode | Verification |
|---|---|---|---|---|
| RELEASEINT01 | Internal release | Audience, access, changelog | Wrong audience | Release note |
| RELEASEINT02 | Public publishing | Channel, approval, claims, assets | Public error/risk | Pre-publish check |
| RELEASEINT03 | Software deploy | Build, environment, rollback | Broken deployment | Smoke test |
| RELEASEINT04 | Document publication | Format, version, owner | Wrong/outdated doc | Version check |
| RELEASEINT05 | Design handoff release | Specs, assets, export | Production ambiguity | Handoff QA |
| RELEASEINT06 | Data/report release | Source, metric, caveats | Misinterpreted report | Report QA |
| RELEASEINT07 | Prompt/library release | Category, variables, tests | Unusable entry | Template test |
| RELEASEINT08 | Automation release | Trigger, monitoring, owner | Silent automation bug | Run/monitor proof |
| RELEASEINT09 | Rollback release | Rollback artifact and trigger | Cannot recover | Rollback path |
| RELEASEINT10 | Post-release monitor | Metrics, owner, review date | No feedback loop | Monitor schedule |
