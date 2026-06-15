# Professional Workflow Platform Engineering DevOps Environment Matrix

Use this matrix when a workflow must build, test, package, deploy, operate, monitor, roll back, provision, secure, scale, or govern software platforms, CI/CD pipelines, environments, infrastructure, configuration, secrets, runtime services, incident response, or developer experience.

## Platform Engineering Scope

| Code | Workflow question | Workflow use |
|---|---|---|
| PLATSCOPE01 | What platform, service, app, or environment is in scope? | Define app, API, job, worker, data pipeline, mobile app, web app, internal tool, cloud service, or shared platform. |
| PLATSCOPE02 | What engineering outcome matters most? | Choose delivery speed, reliability, security, scalability, cost, developer productivity, compliance, recovery, or operability. |
| PLATSCOPE03 | What deployment target applies? | Identify local, dev, test, staging, preview, production, edge, mobile store, Kubernetes, serverless, VM, or managed platform. |
| PLATSCOPE04 | What lifecycle stage is current? | Classify prototype, active development, release candidate, production, migration, incident, maintenance, deprecation, or sunset. |
| PLATSCOPE05 | What service criticality applies? | Classify internal, customer-facing, revenue-critical, regulated, batch-critical, experimental, or tier-0/1/2 service. |
| PLATSCOPE06 | What ownership model applies? | Assign app team, platform team, SRE, DevOps, security, data, vendor, on-call owner, or service owner. |
| PLATSCOPE07 | What architecture context matters? | Capture monolith, microservice, frontend, backend, event-driven, data, mobile, batch, AI, or third-party integration context. |
| PLATSCOPE08 | What operational promise must be kept? | Define SLA, SLO, RTO, RPO, support hours, compliance evidence, customer commitment, and escalation path. |
| PLATSCOPE09 | What platform artifact is required? | Produce platform brief, service catalog entry, deployment plan, runbook, architecture note, or readiness checklist. |
| PLATSCOPE10 | What evidence proves platform work succeeded? | Use passing pipeline, healthy deployment, SLO compliance, rollback test, cost baseline, security scan, and user acceptance. |

## Repository Branching And Code Integration

| Code | Workflow question | Workflow use |
|---|---|---|
| REPOFLOW01 | What repository and branch strategy applies? | Choose trunk-based, GitFlow, release branch, monorepo, polyrepo, feature branch, or protected-branch model. |
| REPOFLOW02 | What code review gate is required? | Define reviewers, CODEOWNERS, required approvals, security review, design review, data review, and merge criteria. |
| REPOFLOW03 | What merge readiness must be checked? | Verify tests, lint, typecheck, build, migrations, docs, feature flags, config, and backward compatibility. |
| REPOFLOW04 | What dependency or package change is involved? | Track lockfiles, version bumps, transitive risk, license, security advisories, and rollback plan. |
| REPOFLOW05 | What migration or schema change accompanies code? | Coordinate database migrations, backfills, compatibility windows, feature flags, and deploy order. |
| REPOFLOW06 | What release note or changelog entry is needed? | Capture user impact, breaking change, migration step, operational note, and support implication. |
| REPOFLOW07 | What generated files or artifacts should be controlled? | Decide whether to commit generated code, schemas, snapshots, assets, docs, or build artifacts. |
| REPOFLOW08 | What conflict or drift must be resolved? | Handle stale branches, merge conflicts, divergent generated files, environment drift, and dependency drift. |
| REPOFLOW09 | What repository automation should run? | Use formatting, lint, tests, dependency scan, secret scan, license check, changelog, or release tagging. |
| REPOFLOW10 | What repo workflow artifact is required? | Produce PR checklist, merge plan, review record, changelog note, migration note, or branch policy. |

## Continuous Integration Pipeline

| Code | Workflow question | Workflow use |
|---|---|---|
| CIPIPE01 | What CI pipeline should validate the change? | Run build, unit tests, integration tests, E2E, lint, typecheck, security scan, container build, or artifact packaging. |
| CIPIPE02 | What CI trigger should run? | Use push, pull request, tag, schedule, manual dispatch, dependency update, release branch, or path-based trigger. |
| CIPIPE03 | What test matrix is needed? | Cover OS, runtime version, browser, database, service dependency, locale, feature flag, and package variant. |
| CIPIPE04 | What pipeline dependency should be cached? | Cache packages, build outputs, test data, browsers, containers, and compiled assets with invalidation rules. |
| CIPIPE05 | What CI secret or credential is needed? | Scope tokens, service credentials, signing keys, registry auth, cloud creds, and avoid exposing them in logs. |
| CIPIPE06 | What flaky test handling applies? | Detect flake, retry safely, quarantine, record owner, collect logs, and avoid hiding real regressions. |
| CIPIPE07 | What CI artifact should be retained? | Store test reports, coverage, screenshots, logs, build artifacts, SBOM, container image, and provenance. |
| CIPIPE08 | What pipeline failure triage should happen? | Classify code failure, test failure, environment issue, dependency outage, quota, timeout, or config error. |
| CIPIPE09 | What CI performance bottleneck exists? | Optimize parallelism, cache, sharding, dependency install, build step, test selection, and runner capacity. |
| CIPIPE10 | What CI artifact is required? | Produce pipeline config, CI report, failure triage note, artifact manifest, or optimization plan. |

## Continuous Delivery And Deployment

| Code | Workflow question | Workflow use |
|---|---|---|
| CDDEPLOY01 | What deployment unit is being released? | Define app, service, container, function, static site, mobile build, database migration, package, or infrastructure change. |
| CDDEPLOY02 | What deployment strategy should be used? | Choose rolling, blue-green, canary, feature flag, shadow, staged rollout, manual promotion, or big-bang release. |
| CDDEPLOY03 | What promotion path applies? | Move through dev, test, staging, preview, production, regional, customer cohort, or store review environments. |
| CDDEPLOY04 | What release gate must pass? | Require tests, approvals, security scan, migration readiness, monitoring, rollback, capacity, and support readiness. |
| CDDEPLOY05 | What deployment approval is required? | Route production, regulated, high-risk, after-hours, customer-impacting, or infrastructure deployments to approvers. |
| CDDEPLOY06 | What deployment dependency exists? | Coordinate database, queue, cache, feature flag, config, DNS, CDN, mobile app, API clients, and third-party systems. |
| CDDEPLOY07 | What post-deploy verification should run? | Check health, logs, metrics, synthetic tests, smoke tests, customer journeys, migrations, and error budgets. |
| CDDEPLOY08 | What release communication is needed? | Notify stakeholders, support, customers, incident channel, status page, and internal release notes as appropriate. |
| CDDEPLOY09 | What deployment freeze or window applies? | Respect blackout dates, business hours, low-traffic windows, maintenance windows, and regional timing. |
| CDDEPLOY10 | What deployment artifact is required? | Produce deploy plan, release checklist, approval log, rollout dashboard, or post-deploy verification report. |

## Environment Management

| Code | Workflow question | Workflow use |
|---|---|---|
| ENVIRON01 | What environment is being managed? | Define local, dev, test, staging, QA, preview, production, DR, sandbox, customer tenant, or ephemeral environment. |
| ENVIRON02 | What parity is required between environments? | Compare runtime, config, data shape, dependencies, network, permissions, feature flags, and infrastructure. |
| ENVIRON03 | What environment provisioning method applies? | Use scripts, containers, IaC, platform templates, preview apps, seed data, or manual setup with runbook. |
| ENVIRON04 | What test data or seed data is needed? | Provide anonymized data, fixtures, synthetic data, golden dataset, migrations, and reset process. |
| ENVIRON05 | What environment access control applies? | Restrict by role, team, tenant, network, VPN, approval, expiration, and audit logging. |
| ENVIRON06 | What environment drift should be detected? | Monitor config, schema, dependencies, cloud resources, permissions, versions, and manual changes. |
| ENVIRON07 | What cleanup or lifecycle rule applies? | Expire preview environments, test resources, old branches, unused databases, and temporary credentials. |
| ENVIRON08 | What environment troubleshooting path is needed? | Check logs, config, network, dependencies, secrets, migrations, data, and resource limits. |
| ENVIRON09 | What environment cost risk exists? | Track orphan resources, oversized instances, preview sprawl, storage, data transfer, and idle services. |
| ENVIRON10 | What environment artifact is required? | Produce environment map, setup guide, parity checklist, access matrix, or cleanup report. |

## Infrastructure As Code And Provisioning

| Code | Workflow question | Workflow use |
|---|---|---|
| IACPROV01 | What infrastructure resource is needed? | Define compute, network, database, storage, queue, secret store, CDN, DNS, IAM, observability, or managed service. |
| IACPROV02 | What IaC tool or provisioning route applies? | Use Terraform, Pulumi, CloudFormation, Bicep, Helm, Kubernetes manifests, platform config, or CLI scripts. |
| IACPROV03 | What state and workspace strategy applies? | Manage remote state, locking, workspaces, environments, drift detection, and state access. |
| IACPROV04 | What plan review is required before apply? | Review diff, destructive changes, cost, security, dependency, region, and rollback implications. |
| IACPROV05 | What dependency ordering is needed? | Sequence network, IAM, secrets, databases, compute, DNS, certificates, monitoring, and app deploys. |
| IACPROV06 | What tagging and ownership standard applies? | Apply service, owner, environment, cost center, data classification, lifecycle, and compliance tags. |
| IACPROV07 | What security baseline should be enforced? | Configure least privilege, encryption, private networking, logging, backup, patching, and policy-as-code. |
| IACPROV08 | What drift or manual change should be reconciled? | Detect drift, decide import, revert, update code, or document exception. |
| IACPROV09 | What teardown or migration plan applies? | Plan destroy, decommission, data migration, DNS cutover, backup, archive, and dependency removal. |
| IACPROV10 | What provisioning artifact is required? | Produce IaC plan, resource manifest, architecture diagram, drift report, or provisioning runbook. |

## Configuration Secrets And Runtime Settings

| Code | Workflow question | Workflow use |
|---|---|---|
| CONFIG01 | What configuration is required? | Define environment variables, feature flags, service endpoints, limits, defaults, toggles, and runtime parameters. |
| CONFIG02 | What secret or credential is involved? | Identify API keys, database passwords, signing keys, certificates, tokens, webhooks, and third-party credentials. |
| CONFIG03 | What storage mechanism should hold secrets? | Use secret manager, vault, platform secrets, KMS, encrypted files, or scoped CI secrets. |
| CONFIG04 | What rotation or expiration rule applies? | Set rotation cadence, revocation path, emergency rotation, owner, and affected services. |
| CONFIG05 | What config validation prevents bad deploys? | Validate required keys, allowed values, schema, environment-specific values, and safe defaults. |
| CONFIG06 | What feature flag strategy applies? | Define flag owner, rollout rule, targeting, kill switch, cleanup date, and monitoring. |
| CONFIG07 | What config drift should be monitored? | Compare desired config, runtime config, platform settings, secrets, flags, and environment overrides. |
| CONFIG08 | What sensitive value must not leak? | Prevent logs, screenshots, commits, build artifacts, analytics, and error reports from exposing secrets. |
| CONFIG09 | What config change communication is needed? | Notify deployers, on-call, support, security, customers, and dependent teams when settings change. |
| CONFIG10 | What configuration artifact is required? | Produce config manifest, secret inventory, rotation log, flag register, or runtime settings checklist. |

## Runtime Operations And Service Reliability

| Code | Workflow question | Workflow use |
|---|---|---|
| RUNTIME01 | What runtime service must stay healthy? | Define web service, API, worker, queue consumer, scheduler, database, cache, CDN, mobile backend, or data pipeline. |
| RUNTIME02 | What SLO or reliability target applies? | Set availability, latency, error rate, throughput, freshness, durability, RTO, RPO, and error budget. |
| RUNTIME03 | What dependency can degrade service? | Track database, cache, queue, third-party API, auth, DNS, CDN, cloud region, and downstream service dependencies. |
| RUNTIME04 | What scaling rule should apply? | Configure autoscaling, concurrency, queue depth, worker count, memory, CPU, replicas, and rate limits. |
| RUNTIME05 | What backup or recovery plan is required? | Define backups, restore tests, replication, snapshots, failover, DR region, and recovery runbook. |
| RUNTIME06 | What maintenance activity is scheduled? | Plan patching, certificate renewal, database vacuum, index rebuild, dependency update, and platform upgrade. |
| RUNTIME07 | What operational runbook is needed? | Document common alarms, diagnosis commands, dashboards, mitigation steps, escalation, and rollback. |
| RUNTIME08 | What customer-impact risk exists? | Assess downtime, degraded mode, data loss, slow response, incorrect output, and communication needs. |
| RUNTIME09 | What reliability review should happen? | Review incidents, SLOs, error budget, toil, capacity, dependencies, and resilience investments. |
| RUNTIME10 | What runtime artifact is required? | Produce service runbook, SLO spec, dependency map, backup plan, or reliability review. |

## Monitoring Alerting And Observability

| Code | Workflow question | Workflow use |
|---|---|---|
| PLATOBS01 | What signals should be collected? | Capture metrics, logs, traces, events, deploy markers, synthetic checks, heartbeats, and business KPIs. |
| PLATOBS02 | What dashboard view is needed? | Create service health, release, incident, capacity, cost, SLO, dependency, queue, or executive reliability dashboard. |
| PLATOBS03 | What alert should page someone? | Page on user impact, SLO burn, outage, data loss, security event, failed deploy, exhausted capacity, or critical job failure. |
| PLATOBS04 | What alert should not page? | Route noisy, low-severity, self-healing, non-actionable, duplicate, or informational alerts to lower-priority channels. |
| PLATOBS05 | What alert metadata is required? | Include service, severity, owner, runbook, dashboard, recent deploys, suspected cause, and escalation path. |
| PLATOBS06 | What log or trace context is needed? | Use request ID, user/account ID where safe, version, region, dependency, job ID, and error classification. |
| PLATOBS07 | What anomaly or drift should be detected? | Detect traffic changes, latency shifts, error spikes, data freshness drift, cost spikes, and usage anomalies. |
| PLATOBS08 | What observability coverage gap exists? | Identify blind spots in logs, metrics, traces, frontend errors, background jobs, and third-party dependencies. |
| PLATOBS09 | What alert review cadence should run? | Review noise, missed incidents, stale dashboards, thresholds, owners, and runbooks at a set cadence. |
| PLATOBS10 | What observability artifact is required? | Produce monitoring plan, alert map, dashboard, SLO report, or observability gap list. |

## Incident Problem And On-Call

| Code | Workflow question | Workflow use |
|---|---|---|
| INCIDENT01 | What incident severity applies? | Classify by user impact, revenue, data loss, security, compliance, duration, affected region, and workaround. |
| INCIDENT02 | Who is incident commander or owner? | Assign commander, technical lead, communications lead, scribe, customer owner, and executive escalation. |
| INCIDENT03 | What immediate containment is needed? | Use rollback, disable feature, scale service, block traffic, rotate secret, failover, or freeze deploys. |
| INCIDENT04 | What communication cadence applies? | Send internal updates, customer updates, status page, stakeholder brief, and resolution notices by severity. |
| INCIDENT05 | What diagnosis path should be followed? | Check recent deploys, alerts, logs, traces, metrics, dependencies, config changes, and external provider status. |
| INCIDENT06 | What problem-management follow-up is required? | Run RCA, identify contributing factors, corrective actions, owners, due dates, and prevention tests. |
| INCIDENT07 | What on-call readiness is needed? | Maintain rotation, escalation, runbooks, access, training, handoff, and fatigue controls. |
| INCIDENT08 | What postmortem standard applies? | Use blameless timeline, impact, detection, response, root cause, action items, and lessons learned. |
| INCIDENT09 | What incident trend should be reviewed? | Track frequency, severity, MTTA, MTTR, recurring causes, alert quality, and team load. |
| INCIDENT10 | What incident artifact is required? | Produce incident log, status update, timeline, RCA, postmortem, or action-item tracker. |

## Rollback Migration And Change Safety

| Code | Workflow question | Workflow use |
|---|---|---|
| ROLLBACK01 | What rollback trigger should be defined? | Set error rate, latency, failed smoke test, support spike, data issue, business metric drop, or manual decision threshold. |
| ROLLBACK02 | What rollback mechanism is available? | Use previous build, feature flag off, config revert, database rollback, traffic shift, DNS rollback, or package downgrade. |
| ROLLBACK03 | What migration makes rollback hard? | Identify destructive schema change, data migration, irreversible external side effect, cache format, or API contract break. |
| ROLLBACK04 | What forward-fix option exists? | Choose hotfix, config patch, data correction, feature flag rule, scaling change, or dependency workaround. |
| ROLLBACK05 | What data migration safety pattern applies? | Use expand-contract, dual writes, backfill, shadow reads, validation, and cutover checkpoints. |
| ROLLBACK06 | What change freeze should be applied? | Pause deploys, infrastructure changes, migrations, or config edits during incidents, audits, or high-risk windows. |
| ROLLBACK07 | What rollback communication is needed? | Notify engineering, support, customer success, customers, status page, and leadership as appropriate. |
| ROLLBACK08 | What rollback verification should run? | Check service health, data integrity, customer journeys, logs, metrics, and lingering side effects. |
| ROLLBACK09 | What lesson should update future changes? | Add migration guardrail, deploy gate, test, alert, runbook, or feature flag cleanup. |
| ROLLBACK10 | What rollback artifact is required? | Produce rollback plan, migration checklist, cutover log, change record, or safety review. |

## Cost Capacity And Performance Engineering

| Code | Workflow question | Workflow use |
|---|---|---|
| PLATCOST01 | What cost driver should be monitored? | Track compute, storage, bandwidth, database, logs, traces, CI runners, third-party APIs, and idle environments. |
| PLATCOST02 | What capacity limit may be hit? | Check CPU, memory, disk, connections, queue depth, rate limits, quotas, database locks, and regional limits. |
| PLATCOST03 | What performance target applies? | Define latency, throughput, concurrency, startup time, build time, job duration, page load, and resource utilization. |
| PLATCOST04 | What load or stress test is needed? | Run baseline, peak, soak, spike, failover, queue backlog, and dependency degradation tests. |
| PLATCOST05 | What optimization should be prioritized? | Choose caching, query tuning, autoscaling, rightsizing, compression, batching, CDN, or architecture change. |
| PLATCOST06 | What cost allocation is required? | Tag cost by service, environment, team, customer, feature, product, and lifecycle stage. |
| PLATCOST07 | What budget guardrail should alert? | Set spend anomaly, forecast overrun, quota threshold, idle resource alert, and approval gate for scale changes. |
| PLATCOST08 | What performance regression should block release? | Gate on latency, memory, bundle size, query cost, test duration, error rate, or capacity headroom. |
| PLATCOST09 | What capacity planning cadence applies? | Review growth forecasts, traffic patterns, seasonal peaks, upcoming launches, and infrastructure roadmap. |
| PLATCOST10 | What cost/performance artifact is required? | Produce cost report, capacity plan, performance test report, optimization backlog, or budget alert map. |

## Platform Developer Experience

| Code | Workflow question | Workflow use |
|---|---|---|
| DEVEXP01 | What developer workflow is being improved? | Improve onboarding, local setup, CI feedback, deployment, debugging, test data, docs, or platform self-service. |
| DEVEXP02 | What friction slows engineering? | Identify slow builds, flaky tests, unclear docs, environment setup, permissions, tool sprawl, and manual approvals. |
| DEVEXP03 | What paved road should be provided? | Offer templates, scaffolds, golden paths, reusable workflows, service catalog, IaC modules, and CI templates. |
| DEVEXP04 | What self-service capability is needed? | Enable environment creation, secret request, deploy preview, logs, dashboards, feature flags, and rollback. |
| DEVEXP05 | What documentation should exist? | Provide getting-started, runbook, architecture, deployment, troubleshooting, API, and ownership docs. |
| DEVEXP06 | What platform support model applies? | Define office hours, ticket queue, Slack channel, escalation, service-level expectations, and ownership. |
| DEVEXP07 | What developer experience metric matters? | Track lead time, build time, deploy frequency, failure rate, setup time, support tickets, and satisfaction. |
| DEVEXP08 | What migration or adoption plan is needed? | Move teams to new platform, CI template, runtime, deployment path, or observability standard with support. |
| DEVEXP09 | What platform contribution model applies? | Define contribution guidelines, module ownership, review process, versioning, and backward compatibility. |
| DEVEXP10 | What developer-experience artifact is required? | Produce platform guide, golden path, service template, migration plan, support playbook, or DX metrics report. |
