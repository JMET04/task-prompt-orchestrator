# Professional Workflow Data Product BI Semantic Governance Matrix

Use this matrix when a workflow must turn raw data, business questions, metrics, dashboards, reports, semantic layers, governed datasets, data products, or self-service analytics into reliable, permissioned, explainable, and decision-useful outputs.

## Data Product Scope

| Code | Workflow question | Workflow use |
|---|---|---|
| DATPROD01 | What data product or analytics asset is in scope? | Define dataset, dashboard, report, metric layer, semantic model, notebook, data API, export, alert, or decision app. |
| DATPROD02 | What decision or workflow will the data support? | Tie the asset to executive review, product decision, operations queue, finance close, sales pipeline, support triage, or compliance. |
| DATPROD03 | Who is the data consumer? | Identify executive, analyst, operator, product manager, finance user, sales leader, customer, regulator, or embedded app. |
| DATPROD04 | What business outcome matters? | Choose faster decisions, better accuracy, risk reduction, revenue lift, cost control, SLA visibility, trust, or self-service adoption. |
| DATPROD05 | What grain and entity are central? | Define account, user, order, ticket, session, product, contract, invoice, event, asset, location, or time period. |
| DATPROD06 | What freshness requirement applies? | Specify real-time, hourly, daily, weekly, monthly, close-cycle, ad hoc, backfill, or historical snapshot freshness. |
| DATPROD07 | What reliability promise is needed? | Set SLA, data completeness, latency, accuracy, reconciliation, ownership, incident path, and communication expectation. |
| DATPROD08 | What data sensitivity boundary applies? | Classify personal, financial, regulated, customer confidential, internal-only, public, aggregated, or row-level restricted data. |
| DATPROD09 | What data artifact is required? | Produce analytics brief, metric spec, semantic model, dashboard, report, dataset contract, data catalog entry, or runbook. |
| DATPROD10 | What evidence proves the data product is useful? | Use usage, decision impact, trust score, SLA adherence, issue reduction, adoption, stakeholder signoff, and metric consistency. |

## Data Requirements And Stakeholder Questions

| Code | Workflow question | Workflow use |
|---|---|---|
| DATAREQ01 | What business question must be answered? | Convert vague asks into decision question, target audience, time window, segment, and action after answer. |
| DATAREQ02 | What metric or dimension is requested? | Capture measure, dimension, filter, breakdown, comparison, cohort, denominator, and expected interpretation. |
| DATAREQ03 | What decision will change based on the answer? | Validate whether the request affects prioritization, budget, staffing, sales action, product change, or risk response. |
| DATAREQ04 | What existing report or metric may already answer it? | Search catalog, dashboards, notebooks, spreadsheets, semantic layer, and prior analyses before creating new assets. |
| DATAREQ05 | What ambiguity must be resolved? | Clarify definitions, source of truth, timeframe, segment, ownership, permissions, and acceptable approximation. |
| DATAREQ06 | What stakeholder alignment is required? | Align data consumer, metric owner, domain owner, analyst, engineer, governance owner, and executive sponsor. |
| DATAREQ07 | What decision cadence drives delivery? | Match daily ops, weekly review, monthly close, quarterly business review, campaign readout, or real-time alert cadence. |
| DATAREQ08 | What acceptance criteria make the data deliverable usable? | Define required fields, accuracy tolerance, freshness, format, filters, drilldowns, narrative, and signoff. |
| DATAREQ09 | What risk exists if the answer is wrong? | Assess revenue, customer, legal, privacy, operational, reputational, and executive decision risks. |
| DATAREQ10 | What requirements artifact is required? | Produce analytics intake, decision brief, metric request, dashboard brief, stakeholder map, or acceptance checklist. |

## Source Systems And Data Acquisition

| Code | Workflow question | Workflow use |
|---|---|---|
| DATASRC01 | What source systems contain the needed data? | Identify product analytics, CRM, billing, support, ERP, warehouse, logs, surveys, spreadsheets, APIs, or third-party feeds. |
| DATASRC02 | What source of truth should win conflicts? | Define authoritative system by entity, process, time period, owner, and reconciliation rule. |
| DATASRC03 | What extraction method is appropriate? | Choose batch ETL, ELT, streaming, reverse ETL, API pull, file upload, CDC, manual import, or federated query. |
| DATASRC04 | What source fields and keys are required? | Capture IDs, timestamps, event names, statuses, amounts, dimensions, foreign keys, and source metadata. |
| DATASRC05 | What ingestion risk must be handled? | Watch schema drift, missing files, API limits, late data, duplicates, timezone mismatch, encoding, and partial loads. |
| DATASRC06 | What historical backfill is needed? | Define lookback window, snapshot logic, slowly changing dimensions, id remaps, and validation of historical completeness. |
| DATASRC07 | What source access approval applies? | Manage system owner approval, credentials, least privilege, privacy, vendor terms, and audit logging. |
| DATASRC08 | What source documentation should be captured? | Record table purpose, owner, refresh cadence, known issues, lineage, field definitions, and caveats. |
| DATASRC09 | What monitoring should detect source failure? | Add freshness, row count, schema, null rate, duplicate, volume anomaly, and pipeline failure checks. |
| DATASRC10 | What acquisition artifact is required? | Produce source inventory, ingestion plan, field map, access request, backfill plan, or source validation report. |

## Data Modeling And Transformation

| Code | Workflow question | Workflow use |
|---|---|---|
| DATAMOD01 | What model layer is being built? | Define raw, staging, intermediate, mart, aggregate, feature table, semantic view, export, or serving layer. |
| DATAMOD02 | What entity relationship must be modeled? | Map users, accounts, contracts, orders, events, products, tickets, invoices, campaigns, or assets and keys. |
| DATAMOD03 | What grain should the model use? | Set row grain, time grain, entity grain, event grain, snapshot grain, and aggregation rule. |
| DATAMOD04 | What transformation logic is required? | Define joins, filters, dedupe, normalization, currency, timezone, status mapping, attribution, and business rules. |
| DATAMOD05 | What slowly changing dimension or history handling applies? | Model effective dates, snapshots, current state, historical state, status changes, and retroactive corrections. |
| DATAMOD06 | What performance requirement affects modeling? | Optimize for dashboard latency, query cost, partitioning, clustering, pre-aggregation, caching, and concurrency. |
| DATAMOD07 | What lineage should be traceable? | Track source tables, transformations, owners, versions, dependencies, downstream reports, and change history. |
| DATAMOD08 | What model validation should be run? | Compare counts, sums, uniqueness, referential integrity, nulls, accepted values, reconciliation, and sample records. |
| DATAMOD09 | What model change control is needed? | Use versioning, impact analysis, migration notes, stakeholder notice, test suite, and rollback plan. |
| DATAMOD10 | What modeling artifact is required? | Produce ERD, dbt model spec, transformation SQL, data contract, lineage map, or validation report. |

## Metric Definition And KPI Design

| Code | Workflow question | Workflow use |
|---|---|---|
| METDEF01 | What metric needs definition? | Name metric, business purpose, owner, numerator, denominator, grain, window, filters, and expected use. |
| METDEF02 | What business process creates the metric? | Link metric to funnel, lifecycle stage, financial process, operational queue, product behavior, or customer journey. |
| METDEF03 | What denominator prevents misleading interpretation? | Define eligible population, active base, opportunity count, total events, revenue base, or time-at-risk. |
| METDEF04 | What dimension breakdowns are allowed? | Specify segment, region, plan, channel, cohort, product, team, owner, time, and privacy-safe cuts. |
| METDEF05 | What exclusions or edge cases apply? | Handle test data, internal users, refunds, canceled orders, bots, duplicates, outliers, trial users, and partial periods. |
| METDEF06 | What target, threshold, or benchmark is needed? | Set goal, alert threshold, SLA, tolerance band, baseline, industry benchmark, or historical comparison. |
| METDEF07 | What interpretation caveat must be visible? | Explain lag, seasonality, sampling, attribution limits, data quality, definitions, and metric tradeoffs. |
| METDEF08 | What metric owner approves changes? | Assign business owner, data owner, finance owner, product owner, governance reviewer, and change approver. |
| METDEF09 | What metric conflict must be reconciled? | Resolve competing definitions, report mismatches, finance reconciliation, legacy metrics, and stakeholder disagreements. |
| METDEF10 | What metric artifact is required? | Produce metric spec, KPI dictionary, calculation SQL, approval log, target sheet, or metric governance record. |

## Semantic Layer And Self-Service Model

| Code | Workflow question | Workflow use |
|---|---|---|
| SEMANTIC01 | What semantic entities should users see? | Expose business-friendly entities, measures, dimensions, filters, hierarchies, relationships, and certified datasets. |
| SEMANTIC02 | What measure belongs in the semantic layer? | Promote reusable, approved metrics with owner, definition, grain, aggregation, filters, and caveats. |
| SEMANTIC03 | What naming should make fields understandable? | Use business names, descriptions, synonyms, examples, units, and deprecate unclear technical field names. |
| SEMANTIC04 | What join path should be governed? | Define safe relationships, join cardinality, bridge tables, many-to-many handling, and fanout prevention. |
| SEMANTIC05 | What self-service guardrail prevents misuse? | Add certified views, allowed dimensions, row-level security, query limits, freshness labels, and warning notes. |
| SEMANTIC06 | What semantic versioning is required? | Version measures, entities, dashboards, API contracts, deprecated fields, and breaking changes. |
| SEMANTIC07 | What tool integration is needed? | Connect BI tools, notebooks, reverse ETL, APIs, embedded analytics, spreadsheets, or data apps to the semantic model. |
| SEMANTIC08 | What validation proves semantic consistency? | Compare metric outputs across BI, SQL, finance reports, product analytics, and dashboards. |
| SEMANTIC09 | What semantic layer adoption support is needed? | Provide examples, training, query templates, office hours, certified dashboards, and support channel. |
| SEMANTIC10 | What semantic artifact is required? | Produce semantic model spec, measure catalog, governed view, certification checklist, or self-service guide. |

## Dashboard And Report Design

| Code | Workflow question | Workflow use |
|---|---|---|
| BIDASH01 | What dashboard or report decision does this support? | Define audience, decision cadence, action owner, primary question, and follow-up workflow. |
| BIDASH02 | What dashboard level is needed? | Choose executive overview, operational cockpit, diagnostic drilldown, cohort analysis, financial report, or alert board. |
| BIDASH03 | What visual encoding fits the question? | Use KPI card, table, line, bar, stacked bar, scatter, funnel, map, cohort, waterfall, or annotation view. |
| BIDASH04 | What filter and drilldown should be available? | Provide date, segment, region, product, owner, cohort, status, channel, and detail-level drill paths. |
| BIDASH05 | What layout supports scanability? | Put key metric first, group related views, use clear labels, define hierarchy, and avoid chart clutter. |
| BIDASH06 | What narrative or annotation is needed? | Add definitions, caveats, target lines, event markers, variance explanation, and next-action guidance. |
| BIDASH07 | What accessibility and export requirement applies? | Support readable colors, keyboard use, alt text where possible, mobile views, CSV export, PDF export, and print use. |
| BIDASH08 | What dashboard QA must pass? | Verify SQL, filters, totals, freshness, permissions, performance, links, exports, and cross-report consistency. |
| BIDASH09 | What adoption or training is needed? | Provide walkthrough, owner, support path, decision ritual, glossary, and feedback channel. |
| BIDASH10 | What dashboard artifact is required? | Produce dashboard spec, wireframe, BI workbook, report pack, QA checklist, or user guide. |

## Data Quality Testing And Reconciliation

| Code | Workflow question | Workflow use |
|---|---|---|
| BIDATAQUAL01 | What quality dimensions matter? | Check completeness, accuracy, timeliness, uniqueness, validity, consistency, integrity, and reconciliation. |
| BIDATAQUAL02 | What quality rule should be automated? | Define null, range, accepted values, uniqueness, referential integrity, freshness, volume, schema, and anomaly tests. |
| BIDATAQUAL03 | What reconciliation target is authoritative? | Compare warehouse to billing, finance, CRM, operational system, source export, or audited report. |
| BIDATAQUAL04 | What tolerance is acceptable? | Set exact match, percentage variance, absolute variance, sampling tolerance, or business-approved caveat. |
| BIDATAQUAL05 | What data incident severity applies? | Classify by affected reports, business decisions, revenue, compliance, customer exposure, and duration. |
| BIDATAQUAL06 | What root cause should be diagnosed? | Investigate source change, pipeline failure, transformation bug, late data, duplicate, permission issue, or human error. |
| BIDATAQUAL07 | What remediation should be applied? | Backfill, patch logic, quarantine data, update source mapping, correct dimensions, rerun pipeline, or add test. |
| BIDATAQUAL08 | What communication is required for quality issues? | Notify affected users, owner, severity, impact, workaround, ETA, resolution, and prevention action. |
| BIDATAQUAL09 | What quality trend should be monitored? | Track incidents, test failures, SLA misses, recurring sources, downstream impact, and remediation time. |
| BIDATAQUAL10 | What quality artifact is required? | Produce test suite, reconciliation report, incident note, quality dashboard, remediation log, or data health scorecard. |

## Access Privacy And Data Governance

| Code | Workflow question | Workflow use |
|---|---|---|
| BIDATAGOV01 | What data classification applies? | Label public, internal, confidential, restricted, regulated, personal, financial, health, minor, or customer-owned data. |
| BIDATAGOV02 | What access model is required? | Apply role-based, attribute-based, row-level, column-level, purpose-based, temporary, or break-glass access. |
| BIDATAGOV03 | What approval workflow grants access? | Route request, manager approval, data owner approval, privacy review, security review, expiration, and audit logging. |
| BIDATAGOV04 | What privacy minimization is needed? | Mask, aggregate, hash, pseudonymize, tokenize, suppress small cells, or remove unnecessary fields. |
| BIDATAGOV05 | What policy or regulation affects usage? | Check GDPR, CCPA, HIPAA, PCI, SOC2, finance controls, employment data, contracts, and internal data policy. |
| BIDATAGOV06 | What data sharing or export risk exists? | Govern CSV exports, screenshots, emails, third-party tools, public embeds, customer shares, and cross-border transfers. |
| BIDATAGOV07 | What audit evidence must be retained? | Record access grants, query logs, approvals, data owner, purpose, retention, and revocation events. |
| BIDATAGOV08 | What sensitive metric display rule applies? | Suppress small groups, hide PII, delay data, aggregate, watermark, or restrict drilldown where needed. |
| BIDATAGOV09 | What access review cadence is needed? | Review quarterly, annually, after role change, after incident, after contract change, or before audit. |
| BIDATAGOV10 | What governance artifact is required? | Produce access matrix, data policy note, privacy review, audit log, classification table, or governance checklist. |

## Catalog Metadata And Lineage

| Code | Workflow question | Workflow use |
|---|---|---|
| DATACAT01 | What data asset should be cataloged? | Catalog table, view, dashboard, report, metric, model, pipeline, notebook, API, export, or semantic entity. |
| DATACAT02 | What metadata must be recorded? | Capture owner, description, source, refresh, grain, fields, sensitivity, quality status, usage, and downstream assets. |
| DATACAT03 | What lineage should be visible? | Show upstream systems, transformations, models, dashboards, exports, reverse ETL, and business processes. |
| DATACAT04 | What certification status applies? | Mark draft, certified, deprecated, experimental, restricted, stale, broken, or superseded with owner rationale. |
| DATACAT05 | What glossary term should be linked? | Connect business terms, KPIs, entity definitions, synonyms, examples, and approved metric definitions. |
| DATACAT06 | What discoverability tag is needed? | Add domain, team, function, product, lifecycle, sensitivity, frequency, and decision-use tags. |
| DATACAT07 | What duplicate or stale asset should be resolved? | Merge, redirect, deprecate, archive, or clarify competing dashboards, tables, metrics, and notebooks. |
| DATACAT08 | What documentation freshness rule applies? | Set review date, owner reminder, stale warning, automated metadata sync, and deprecation trigger. |
| DATACAT09 | What user feedback should update metadata? | Capture confusing definitions, missing owners, broken links, stale fields, and requested examples. |
| DATACAT10 | What catalog artifact is required? | Produce catalog entry, lineage map, glossary page, certification record, deprecation note, or asset inventory. |

## Reporting Operations And Distribution

| Code | Workflow question | Workflow use |
|---|---|---|
| REPORTOPS01 | What recurring report is being operated? | Define weekly business review, board pack, finance close, sales report, product review, ops digest, or customer report. |
| REPORTOPS02 | What schedule and dependency chain applies? | Set data refresh, QA, analyst review, stakeholder comments, executive delivery, and archive timing. |
| REPORTOPS03 | What report package format is required? | Choose dashboard, PDF, slide deck, spreadsheet, email digest, notebook, CSV export, API, or embedded view. |
| REPORTOPS04 | What manual step should be automated or controlled? | Reduce copy-paste, spreadsheet edits, screenshot exports, manual filters, and repeated commentary where possible. |
| REPORTOPS05 | What variance explanation is needed? | Add drivers, anomalies, segment changes, seasonality, pipeline issues, external factors, and action recommendations. |
| REPORTOPS06 | What pre-distribution QA must pass? | Check data freshness, totals, formatting, access, commentary, links, exports, and sensitive information. |
| REPORTOPS07 | What stakeholder distribution rule applies? | Send to approved list, role group, customer, board, regulator, internal channel, or secure portal. |
| REPORTOPS08 | What correction process applies after delivery? | Issue correction note, replace report, annotate dashboard, notify audience, archive superseded version, and log cause. |
| REPORTOPS09 | What report retirement or consolidation should happen? | Remove low-use, duplicate, stale, inaccurate, or unsupported reports and redirect users. |
| REPORTOPS10 | What reporting artifact is required? | Produce report runbook, distribution manifest, QA log, commentary pack, archive record, or correction log. |

## Self-Service Analytics Enablement

| Code | Workflow question | Workflow use |
|---|---|---|
| SELFSVC01 | What self-service audience needs enablement? | Identify analysts, operators, managers, product teams, sales, finance, support, executives, or customers. |
| SELFSVC02 | What question patterns should self-service support? | Support exploration by time, segment, funnel, cohort, account, product, geography, owner, or status. |
| SELFSVC03 | What certified starting point should users use? | Provide governed dataset, dashboard, template query, notebook, metric explorer, or semantic model. |
| SELFSVC04 | What training or documentation is needed? | Create glossary, query examples, dashboard walkthrough, office hours, FAQ, data caveats, and escalation path. |
| SELFSVC05 | What guardrail prevents bad analysis? | Add safe defaults, metric definitions, sample-size warnings, privacy constraints, join guidance, and review triggers. |
| SELFSVC06 | What support workflow handles data questions? | Route questions, bugs, access issues, definition disputes, dashboard requests, and training needs to owners. |
| SELFSVC07 | What self-service adoption metric matters? | Track active users, repeat usage, certified asset use, support tickets, duplicated reports, and decision impact. |
| SELFSVC08 | What advanced user path is needed? | Provide sandbox, notebook, SQL access, feature store, API, governed export, or analyst certification path. |
| SELFSVC09 | What misuse or overload should be monitored? | Watch expensive queries, data exports, privacy violations, dashboard sprawl, stale copies, and wrong metric usage. |
| SELFSVC10 | What self-service artifact is required? | Produce enablement plan, starter dashboard, query template, data guide, support playbook, or adoption report. |

## Analysis Experiment And Insight Delivery

| Code | Workflow question | Workflow use |
|---|---|---|
| ANALYTIC01 | What analytical method fits the question? | Choose descriptive, diagnostic, cohort, funnel, segmentation, regression, experiment, forecast, attribution, or causal analysis. |
| ANALYTIC02 | What analysis plan should be written first? | Define question, hypothesis, data, population, method, exclusions, limitations, review owner, and decision rule. |
| ANALYTIC03 | What comparison or baseline is required? | Select prior period, control group, matched cohort, forecast, target, benchmark, or untreated population. |
| ANALYTIC04 | What statistical or methodological caveat applies? | Address sample size, bias, confounding, seasonality, multiple testing, survivorship, missing data, and causality limits. |
| ANALYTIC05 | What insight is actionable? | Translate finding into recommendation, owner, expected impact, confidence, next experiment, and risk. |
| ANALYTIC06 | What analysis reproducibility is required? | Preserve SQL, notebook, version, parameters, data snapshot, package versions, and output artifacts. |
| ANALYTIC07 | What peer review should happen? | Review method, code, assumptions, source data, metric definitions, sensitivity checks, and conclusion wording. |
| ANALYTIC08 | What narrative should accompany results? | Explain context, key finding, evidence, implication, caveat, recommendation, and decision requested. |
| ANALYTIC09 | What follow-up should update data products? | Create metric, dashboard, alert, segment, experiment, playbook update, or product change from the insight. |
| ANALYTIC10 | What analysis artifact is required? | Produce analysis plan, notebook, SQL pack, insight memo, experiment readout, or decision brief. |

## Data Product Lifecycle And Operations

| Code | Workflow question | Workflow use |
|---|---|---|
| DPLIFE01 | What lifecycle stage is the data product in? | Classify concept, prototype, beta, certified, production, monitored, deprecated, retired, or replaced. |
| DPLIFE02 | What production readiness gate must pass? | Verify owner, SLA, tests, docs, lineage, access, privacy, dashboard QA, support path, and monitoring. |
| DPLIFE03 | What operational owner maintains it? | Assign business owner, data owner, analytics owner, engineering owner, governance owner, and support owner. |
| DPLIFE04 | What incident process applies? | Define detection, severity, triage, customer notice, rollback, patch, backfill, RCA, and prevention. |
| DPLIFE05 | What change request process applies? | Manage new fields, metric changes, schema changes, dashboard edits, permission changes, and breaking changes. |
| DPLIFE06 | What cost and performance should be controlled? | Monitor query cost, storage, refresh time, dashboard load, compute, concurrency, and unused assets. |
| DPLIFE07 | What adoption or satisfaction feedback is needed? | Collect usage, survey, stakeholder feedback, support tickets, decision impact, and unmet needs. |
| DPLIFE08 | What deprecation or migration path applies? | Announce replacement, redirect users, freeze changes, migrate dashboards, archive old assets, and remove access. |
| DPLIFE09 | What quarterly review should happen? | Review usage, trust, incidents, quality, cost, relevance, duplicates, permissions, and roadmap. |
| DPLIFE10 | What lifecycle artifact is required? | Produce product runbook, readiness checklist, roadmap, incident log, cost report, deprecation plan, or lifecycle review. |


