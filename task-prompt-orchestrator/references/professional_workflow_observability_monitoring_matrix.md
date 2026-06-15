# Professional Workflow Observability Monitoring Matrix

Use this matrix when a workflow runs repeatedly, operates in production, depends on automation, processes batches, calls tools or APIs, serves users, publishes artifacts, maintains a prompt library, or needs ongoing visibility into health, quality, drift, latency, cost, failures, adoption, and outcomes after launch.

## Observability Scope

| Code | Monitoring question | Workflow use |
|---|---|---|
| OBSCOPE01 | What must be observable for this workflow to be trusted? | Define visibility needs before choosing logs, metrics, traces, dashboards, or reports. |
| OBSCOPE02 | Which workflow stages need monitoring? | Map intake, planning, execution, QA, handoff, publishing, support, refresh, and closeout signals. |
| OBSCOPE03 | Which actors need visibility? | Identify operator, owner, reviewer, approver, user, client, vendor, executive, and auditor views. |
| OBSCOPE04 | What is the normal operating shape? | Define expected volume, cadence, latency, error rate, queue depth, cost, quality, and completion pattern. |
| OBSCOPE05 | What is the smallest useful monitoring set? | Pick vital signs rather than collecting noisy or unactionable data. |
| OBSCOPE06 | What must not be monitored or stored? | Exclude secrets, private content, raw personal data, internal reasoning, or excessive payloads. |
| OBSCOPE07 | What environments need separate visibility? | Separate dev, staging, production, client tenant, local run, batch, and public release signals. |
| OBSCOPE08 | What time horizon matters? | Choose real-time, hourly, daily, weekly, release-level, cohort, or long-term trend monitoring. |
| OBSCOPE09 | What observability artifact should be produced? | Leave a signal map, dashboard spec, alert plan, run log, or monitoring checklist. |
| OBSCOPE10 | What observability stop rule applies? | Stop adding signals when every critical decision has enough visibility and ownership. |

## Signal Inventory

| Code | Monitoring question | Workflow use |
|---|---|---|
| SIGNAL01 | What event signals prove the workflow started? | Capture request created, trigger fired, file received, source changed, schedule ran, or user action. |
| SIGNAL02 | What event signals prove each step completed? | Capture state transitions, artifact creation, tool result, approval, handoff, and final acceptance. |
| SIGNAL03 | What signals show work in progress? | Track queue depth, current state, open items, active batch, assigned owner, and blocked items. |
| SIGNAL04 | What signals show quality? | Track test pass rate, review findings, defect count, sampling results, hallucination flags, or acceptance failures. |
| SIGNAL05 | What signals show user value or adoption? | Track usage, repeat requests, completion, satisfaction, conversion, retention, support contacts, or manual overrides. |
| SIGNAL06 | What signals show risk? | Track policy violations, privacy flags, unsafe actions, high-impact changes, stale evidence, or unresolved conflicts. |
| SIGNAL07 | What signals show performance? | Track latency, throughput, duration, retry count, queue wait, batch runtime, and response time. |
| SIGNAL08 | What signals show cost or resource use? | Track API calls, token use, compute time, storage, licenses, human review time, and vendor spend. |
| SIGNAL09 | What signals show drift or decay? | Track source staleness, template age, model changes, schema changes, user behavior shifts, and quality trend changes. |
| SIGNAL10 | What signal inventory should be maintained? | Store signal name, source, owner, cadence, threshold, retention, and actionability. |

## Logging And Trace

| Code | Monitoring question | Workflow use |
|---|---|---|
| LOGTRACE01 | What should be logged at each workflow step? | Capture timestamp, actor, state, input reference, output reference, decision, and validation result. |
| LOGTRACE02 | What should be excluded from logs? | Redact secrets, personal data, payloads, private messages, and proprietary content unless necessary and allowed. |
| LOGTRACE03 | What trace ID links the workflow together? | Use request ID, run ID, batch ID, item ID, artifact ID, source ID, or user-visible ticket ID. |
| LOGTRACE04 | What log level is appropriate? | Separate debug, info, warning, error, critical, audit, and security events. |
| LOGTRACE05 | What structured fields are required? | Use consistent fields for status, owner, duration, tool, error code, source, artifact, and risk. |
| LOGTRACE06 | What log retention rule applies? | Set retention by privacy, audit, incident, cost, and operational debugging needs. |
| LOGTRACE07 | What trace view helps debugging? | Provide timeline, step graph, dependency map, state transitions, or item-level replay. |
| LOGTRACE08 | What logs need sampling? | Sample high-volume success logs while keeping failures, security events, and audit trails. |
| LOGTRACE09 | What log integrity check is required? | Check missing spans, duplicate events, clock skew, broken trace IDs, and malformed fields. |
| LOGTRACE10 | What logging evidence should be preserved? | Keep log schema, trace examples, retention rule, redaction rule, and known gaps. |

## Metrics Design

| Code | Monitoring question | Workflow use |
|---|---|---|
| METRICD01 | What health metric proves the workflow is alive? | Define trigger success, run heartbeat, queue progress, tool availability, or completion rate. |
| METRICD02 | What quality metric proves output is acceptable? | Define acceptance rate, defect rate, rework rate, review score, evidence coverage, or test pass rate. |
| METRICD03 | What timeliness metric matters? | Define lead time, cycle time, SLA, queue age, freshness, latency, or time-to-resolution. |
| METRICD04 | What reliability metric matters? | Define success rate, failure rate, retry rate, rollback rate, incident count, or availability. |
| METRICD05 | What cost metric matters? | Define cost per run, cost per item, token spend, compute cost, tool cost, or human time. |
| METRICD06 | What scale metric matters? | Define item volume, batch size, concurrency, throughput, backlog, and capacity utilization. |
| METRICD07 | What adoption metric matters? | Define active users, repeat use, handoff acceptance, manual override rate, or abandonment. |
| METRICD08 | What risk metric matters? | Define policy flags, security events, stale sources, unresolved exceptions, or high-risk approvals. |
| METRICD09 | What denominator prevents misleading metrics? | Specify per run, per item, per user, per batch, per artifact, per time window, or per source. |
| METRICD10 | What metric dictionary should be produced? | Store metric name, definition, denominator, owner, source, threshold, cadence, and caveats. |

## Thresholds And SLOs

| Code | Monitoring question | Workflow use |
|---|---|---|
| SLOMON01 | What service level objective matters? | Define target for availability, latency, freshness, completion, quality, or response time. |
| SLOMON02 | What threshold marks warning versus failure? | Separate informational, warning, error, critical, and blocked thresholds. |
| SLOMON03 | What threshold is static versus adaptive? | Use fixed limits for hard constraints and baselines for seasonality or variable volume. |
| SLOMON04 | What error budget is acceptable? | Decide allowable failures, delays, defects, stale items, or manual overrides over a period. |
| SLOMON05 | What threshold requires human review? | Gate high-risk anomalies, quality drops, source conflicts, security events, or user-impacting failures. |
| SLOMON06 | What threshold should trigger auto-retry? | Use automated retry only for transient, bounded, idempotent, and low-risk failures. |
| SLOMON07 | What threshold should pause the workflow? | Stop when error budget, privacy risk, cost spike, data corruption, or quality failure exceeds limit. |
| SLOMON08 | What threshold needs escalation? | Escalate breaches by severity, affected users, duration, cost, risk, or repeated failure. |
| SLOMON09 | What threshold needs periodic review? | Revisit thresholds after volume growth, workflow redesign, model change, or user expectation shift. |
| SLOMON10 | What SLO artifact should be left? | Produce SLO table with metric, target, threshold, action, owner, and review cadence. |

## Alerts And Escalation

| Code | Monitoring question | Workflow use |
|---|---|---|
| ALERT01 | What condition should generate an alert? | Alert only on actionable symptoms, threshold breaches, risk events, or user-impacting failures. |
| ALERT02 | Who receives each alert? | Route to owner, on-call, reviewer, approver, security, legal, vendor, client, or executive. |
| ALERT03 | What severity should the alert have? | Classify by impact, urgency, affected scope, data risk, customer impact, and reversibility. |
| ALERT04 | What message should the alert include? | Include what happened, affected scope, evidence, run ID, likely cause, action, and owner. |
| ALERT05 | What alert should be suppressed or grouped? | Reduce noise through deduplication, grouping, rate limits, maintenance windows, and known issue labels. |
| ALERT06 | What alert requires acknowledgment? | Require ack for production failures, privacy/security events, stalled queues, high-cost spikes, and SLA breaches. |
| ALERT07 | What alert requires escalation? | Escalate on missed ack, repeated breach, high severity, unresolved risk, or customer-facing impact. |
| ALERT08 | What alert requires a runbook link? | Attach diagnostic steps, rollback, retry, contact, and validation instructions. |
| ALERT09 | What alert review is needed? | Review false positives, missed alerts, noise, routing, severity, and response time. |
| ALERT10 | What alert evidence should be archived? | Keep alert ID, trigger, severity, recipients, ack, actions, resolution, and follow-up. |

## Anomaly And Drift Detection

| Code | Monitoring question | Workflow use |
|---|---|---|
| ANOMALY01 | What abnormal pattern should be detected? | Monitor spikes, drops, stalls, missing events, duplicate runs, quality regression, or cost surge. |
| ANOMALY02 | What baseline defines normal? | Use historical median, rolling window, seasonality, expected schedule, sample set, or business calendar. |
| ANOMALY03 | What drift can affect output quality? | Watch model updates, prompt changes, source changes, schema drift, user behavior, or policy updates. |
| ANOMALY04 | What data drift can affect decisions? | Monitor distribution shifts, missing fields, new categories, unit changes, and stale datasets. |
| ANOMALY05 | What source drift can affect evidence? | Track changed URLs, outdated docs, superseded specs, broken links, and refreshed standards. |
| ANOMALY06 | What user journey drift matters? | Detect onboarding drop-off, support increase, abandonment, lower repeat use, or adoption plateau. |
| ANOMALY07 | What anomaly requires immediate action? | Act on data loss, security risk, failing outputs, high-cost runaway, or user-visible outage. |
| ANOMALY08 | What anomaly can be watched? | Track mild variance, early warning trends, and known seasonal movement without interrupting work. |
| ANOMALY09 | What anomaly investigation artifact is needed? | Produce anomaly note with timeline, scope, baseline, suspected causes, and next checks. |
| ANOMALY10 | What drift review should be scheduled? | Set cadence for prompts, sources, schemas, models, dashboards, and thresholds. |

## Dashboard And Reporting

| Code | Monitoring question | Workflow use |
|---|---|---|
| DASHMON01 | What dashboard question must be answered first? | Anchor dashboard design to operational decisions, not vanity metrics. |
| DASHMON02 | What view does the operator need? | Show queue, failures, current state, blocked items, latency, retries, and next action. |
| DASHMON03 | What view does the owner need? | Show trend, SLA, cost, quality, adoption, risk, and improvement backlog. |
| DASHMON04 | What view does the reviewer or auditor need? | Show evidence, approvals, exceptions, controls, samples, and traceability. |
| DASHMON05 | What view does the user or client need? | Show status, deliverables, ETA, decisions needed, limitations, and support path. |
| DASHMON06 | What dashboard grain is useful? | Choose run, item, batch, user, team, source, artifact, workflow, or time-window grain. |
| DASHMON07 | What dashboard filters are needed? | Add status, owner, severity, source, domain, customer, date, workflow, environment, and risk filters. |
| DASHMON08 | What dashboard should avoid exposing? | Hide secrets, private content, row-level PII, sensitive cohorts, and internal reasoning. |
| DASHMON09 | What report cadence is needed? | Choose real-time dashboard, daily digest, weekly review, monthly KPI, release report, or incident report. |
| DASHMON10 | What dashboard QA check is required? | Verify metric definitions, freshness, filters, permissions, row counts, and chart interpretation. |

## Feedback Loops

| Code | Monitoring question | Workflow use |
|---|---|---|
| FEEDLOOP01 | What user feedback should be collected? | Capture satisfaction, rejection reasons, confusion, missing needs, bugs, and usefulness. |
| FEEDLOOP02 | What operator feedback should be collected? | Capture friction, manual workarounds, alert noise, unclear ownership, and missing runbook steps. |
| FEEDLOOP03 | What reviewer feedback should be collected? | Capture quality defects, policy concerns, evidence gaps, and acceptance blockers. |
| FEEDLOOP04 | What system feedback should be collected? | Use retries, failures, latency, cost, drift, queue stalls, and validation outcomes. |
| FEEDLOOP05 | What feedback should create backlog items? | Convert repeated pain, high-impact failures, and quality issues into tracked improvements. |
| FEEDLOOP06 | What feedback should update prompts or templates? | Use recurring edits, ambiguity, missing fields, and failed outputs to improve reusable assets. |
| FEEDLOOP07 | What feedback should update training or adoption? | Use support patterns, user mistakes, and low adoption to improve enablement. |
| FEEDLOOP08 | What feedback should update thresholds or alerts? | Tune noise, missed detections, severity, routing, and escalation rules. |
| FEEDLOOP09 | What feedback loop should be closed publicly? | Tell relevant users when defects, gaps, or requested improvements are resolved. |
| FEEDLOOP10 | What feedback evidence should be preserved? | Keep feedback source, theme, frequency, severity, decision, owner, and resolution status. |

## Run Review And Audit

| Code | Monitoring question | Workflow use |
|---|---|---|
| RUNAUDIT01 | What run review happens after each execution? | Check completion, quality, failures, exceptions, cost, latency, and handoff status. |
| RUNAUDIT02 | What batch review happens after volume runs? | Review throughput, sample QA, duplicate rate, skipped items, failures, and cost. |
| RUNAUDIT03 | What production review happens periodically? | Review SLOs, alerts, incidents, drift, adoption, backlog, and capacity. |
| RUNAUDIT04 | What audit evidence proves monitoring worked? | Keep dashboards, alerts, logs, metric snapshots, incident records, and review notes. |
| RUNAUDIT05 | What monitoring gap was discovered? | Record missing signal, hidden failure mode, stale metric, missing owner, or weak threshold. |
| RUNAUDIT06 | What alert or metric should be retired? | Remove noisy, unused, redundant, misleading, or privacy-risk signals. |
| RUNAUDIT07 | What monitoring artifact should be versioned? | Version dashboards, metric dictionaries, alert rules, SLOs, and runbooks. |
| RUNAUDIT08 | What monitoring change needs approval? | Gate changes that alter SLA, privacy, security, executive reporting, or customer-visible status. |
| RUNAUDIT09 | What monitoring closeout should be reported? | Summarize status, key changes, unresolved risks, and next review date. |
| RUNAUDIT10 | What monitoring maturity upgrade is next? | Move from manual checks to dashboards, alerts, automation, SLOs, anomaly detection, or self-healing. |

## Cost And Capacity Watch

| Code | Monitoring question | Workflow use |
|---|---|---|
| COSTWATCH01 | What cost source should be monitored? | Track API usage, model tokens, compute, storage, licensing, vendor calls, and human review time. |
| COSTWATCH02 | What capacity source should be monitored? | Track queue depth, concurrency, rate limits, reviewer bandwidth, tool quotas, and infrastructure limits. |
| COSTWATCH03 | What cost threshold needs warning? | Set budget warning, per-run cap, per-item cap, daily cap, or runaway spend trigger. |
| COSTWATCH04 | What capacity threshold needs action? | Alert on backlog age, saturation, throttling, queue growth, missed SLA, or reviewer overload. |
| COSTWATCH05 | What cost anomaly should pause execution? | Stop runaway loops, duplicate batches, unexpected API spikes, or unbounded generation. |
| COSTWATCH06 | What capacity anomaly should trigger scaling? | Add workers, reviewers, batching, queue rules, caching, or throttling based on demand. |
| COSTWATCH07 | What optimization opportunity should be watched? | Track caching, dedupe, sampling, prompt compression, batching, and automation savings. |
| COSTWATCH08 | What cost allocation is needed? | Attribute cost by user, project, workflow, client, source, batch, or artifact. |
| COSTWATCH09 | What cost/capacity report is needed? | Provide spend, trend, forecast, bottleneck, utilization, and action recommendations. |
| COSTWATCH10 | What cost/capacity audit evidence should be kept? | Record thresholds, usage snapshots, budget decisions, scaling actions, and exceptions. |

## Monitoring Governance

| Code | Monitoring question | Workflow use |
|---|---|---|
| MONGOV01 | Who owns each signal, dashboard, and alert? | Assign accountable owners for monitoring assets and responses. |
| MONGOV02 | Who can view monitoring data? | Apply role-based access to logs, dashboards, traces, cost, security, and customer data. |
| MONGOV03 | What monitoring data has retention limits? | Set retention for logs, metrics, traces, screenshots, reports, incidents, and raw payloads. |
| MONGOV04 | What monitoring data needs redaction? | Remove secrets, PII, client content, private messages, and sensitive metadata. |
| MONGOV05 | What monitoring change process applies? | Review changes to alerts, thresholds, dashboards, SLOs, and metric definitions. |
| MONGOV06 | What monitoring source is authoritative? | Define source of truth for health, status, cost, incidents, and executive reporting. |
| MONGOV07 | What monitoring access should be audited? | Review who viewed, exported, changed, or shared monitoring data. |
| MONGOV08 | What compliance requirement affects monitoring? | Apply privacy, security, legal hold, audit, financial control, accessibility, or industry rules. |
| MONGOV09 | What monitoring documentation must exist? | Maintain metric dictionary, alert catalog, dashboard guide, runbook, and ownership map. |
| MONGOV10 | What governance review proves readiness? | Verify ownership, access, retention, redaction, change control, and documentation before launch. |
