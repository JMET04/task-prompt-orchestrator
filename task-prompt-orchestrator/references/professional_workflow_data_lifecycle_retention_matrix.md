# Professional Workflow Data Lifecycle Retention Matrix

Use this matrix when a workflow creates, collects, transforms, stores, shares, migrates, archives, retains, deletes, or audits data. It covers the lifecycle controls between source/evidence and downstream use: what data exists, why it exists, where it moves, how long it should live, how it is protected, and how it is retired.

## Data Scope

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATASCOPE01 | What data objects are in scope? | Identify records, files, datasets, logs, prompts, outputs, media, metadata, embeddings, and derived artifacts. |
| DATASCOPE02 | What business purpose does each data object serve? | Link data to workflow goal, legal basis, user need, operational need, evidence need, or reuse case. |
| DATASCOPE03 | Who owns each data object? | Assign data owner, steward, custodian, processor, reviewer, approver, and downstream consumer. |
| DATASCOPE04 | What system of record applies? | Identify authoritative store, working copy, cache, export, archive, backup, and temporary staging area. |
| DATASCOPE05 | What data grain is required? | Define row, event, document, asset, account, user, session, version, batch, or aggregate level. |
| DATASCOPE06 | What data boundary is excluded? | Mark out-of-scope sources, sensitive fields, prohibited enrichment, unnecessary logs, and nonessential copies. |
| DATASCOPE07 | What jurisdiction or policy scope applies? | Connect data to region, contract, regulation, retention schedule, consent, and internal policy. |
| DATASCOPE08 | What lifecycle stage is each object in? | Classify draft, active, reviewed, approved, published, superseded, archived, frozen, or disposed. |
| DATASCOPE09 | What lifecycle assumption is uncertain? | Record missing owner, unclear purpose, unknown source, ambiguous retention, or weak lineage. |
| DATASCOPE10 | What data-scope artifact is needed? | Produce data inventory, lifecycle map, data charter, or object register. |

## Collection And Generation

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATACOLL01 | How is data collected or generated? | Map manual entry, upload, API, scraping, instrumentation, user action, model output, sensor, or vendor feed. |
| DATACOLL02 | What permission exists for collection? | Verify consent, contract, license, public-source right, internal authority, or operational necessity. |
| DATACOLL03 | What collection minimization applies? | Collect only required fields, period, population, granularity, and sample size. |
| DATACOLL04 | What collection context must be preserved? | Capture source, timestamp, collector, method, query, parameters, version, and user notice. |
| DATACOLL05 | What generated data needs labeling? | Label AI-generated, synthetic, inferred, transformed, anonymized, sampled, or human-reviewed data. |
| DATACOLL06 | What collection quality risk exists? | Check missing fields, duplicates, bot traffic, bad instrumentation, capture bias, stale files, and vendor errors. |
| DATACOLL07 | What collection failure fallback exists? | Define retry, alternate source, manual capture, partial dataset, blocked state, or escalation. |
| DATACOLL08 | What data subject or contributor expectation applies? | Respect notice, opt-out, usage expectation, creator intent, and contextual integrity. |
| DATACOLL09 | What collection evidence is required? | Preserve consent record, source URL, API response, upload manifest, scrape log, or generation trace. |
| DATACOLL10 | What collection artifact is needed? | Produce collection manifest, ingestion note, source log, or generation record. |

## Classification And Sensitivity

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATACLASS01 | What sensitivity class applies? | Classify public, internal, confidential, restricted, regulated, secret, personal, or safety-critical data. |
| DATACLASS02 | What personal or regulated data exists? | Identify PII, PHI, financial, biometric, location, children, employment, education, legal, or account data. |
| DATACLASS03 | What proprietary or business-sensitive data exists? | Mark trade secrets, pricing, strategy, source code, customer lists, contracts, models, and vendor rates. |
| DATACLASS04 | What inferred or derived sensitivity exists? | Detect sensitive conclusions from non-sensitive inputs, joins, embeddings, scores, and predictions. |
| DATACLASS05 | What access tier follows classification? | Map class to roles, approvals, encryption, masking, logging, export limits, and review gates. |
| DATACLASS06 | What classification conflict exists? | Resolve mixed datasets, aggregated data, screenshots, logs, redacted copies, and public/private blends. |
| DATACLASS07 | What downgrade or declassification rule applies? | Define anonymization, aggregation, redaction, review, expiry, and approval before lowering sensitivity. |
| DATACLASS08 | What label must travel with the data? | Attach classification, owner, purpose, retention, source, rights, and handling instructions. |
| DATACLASS09 | What classification validation is needed? | Sample fields, inspect schemas, scan files, review joins, and test redaction. |
| DATACLASS10 | What classification artifact is needed? | Produce data classification table, handling matrix, or sensitive-field register. |

## Quality And Fitness

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATAQUAL01 | What quality standard must data meet? | Define completeness, accuracy, freshness, uniqueness, consistency, validity, granularity, and representativeness. |
| DATAQUAL02 | What source-of-truth conflict exists? | Compare systems, versions, manual records, vendor feeds, extracts, caches, and published artifacts. |
| DATAQUAL03 | What freshness requirement applies? | Set maximum age, refresh trigger, stale-data label, cache TTL, and evidence date. |
| DATAQUAL04 | What schema or format validity is required? | Validate columns, types, units, encodings, filenames, media specs, document structures, and API contracts. |
| DATAQUAL05 | What deduplication rule applies? | Define identity key, fuzzy match, merge precedence, duplicate retention, and conflict handling. |
| DATAQUAL06 | What missing-data rule applies? | Decide impute, exclude, flag, collect again, ask user, or block workflow. |
| DATAQUAL07 | What anomaly or outlier rule applies? | Detect impossible values, drift, spikes, truncation, corrupted files, and suspicious records. |
| DATAQUAL08 | What sample or test set proves quality? | Use profiling, row counts, checksums, spot checks, reconciliation, and domain expert review. |
| DATAQUAL09 | What quality exception can be accepted? | Record acceptable gaps, caveats, risk owner, downstream warning, and expiration. |
| DATAQUAL10 | What quality artifact is needed? | Produce data quality report, validation log, reconciliation table, or caveat note. |

## Transformation And Lineage

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATALIN01 | What transformations occur? | Map cleaning, parsing, extraction, normalization, joining, summarization, embedding, scoring, and generation. |
| DATALIN02 | What lineage must be tracked? | Record source, transform, script, model, prompt, parameters, version, timestamp, and operator. |
| DATALIN03 | What derived data inherits restrictions? | Propagate rights, sensitivity, consent, purpose, retention, and deletion obligations to outputs. |
| DATALIN04 | What reversible versus irreversible transform applies? | Distinguish redaction, anonymization, aggregation, tokenization, hashing, compression, and lossy conversion. |
| DATALIN05 | What transformation validation is needed? | Compare pre/post counts, checksums, sample rows, schema tests, semantic checks, and review diffs. |
| DATALIN06 | What transformation tool is authoritative? | Identify script, notebook, ETL job, model, spreadsheet formula, manual step, or external service. |
| DATALIN07 | What transformation failure mode exists? | Check silent truncation, encoding errors, bad joins, hallucinated extraction, duplicate creation, and unit mismatch. |
| DATALIN08 | What lineage is needed for audit or reproducibility? | Preserve raw input, intermediate, final output, code, prompt, environment, and run log when required. |
| DATALIN09 | What lineage should be hidden or minimized? | Avoid exposing private raw data, secrets, sensitive prompts, or unnecessary identifiers in public artifacts. |
| DATALIN10 | What lineage artifact is needed? | Produce lineage map, transform log, reproducibility pack, or data derivation note. |

## Storage And Access

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATASTORE01 | Where should each data object live? | Choose local workspace, shared drive, database, object store, document system, archive, vault, or temporary folder. |
| DATASTORE02 | What storage tier is appropriate? | Select hot, warm, cold, archive, immutable, encrypted, air-gapped, or disposable storage. |
| DATASTORE03 | What access model applies? | Define role-based, attribute-based, project-based, owner-approved, least-privilege, or public access. |
| DATASTORE04 | What encryption or protection is required? | Apply encryption at rest, encryption in transit, key management, masking, tokenization, or watermarking. |
| DATASTORE05 | What copy-control rule applies? | Limit downloads, exports, screenshots, temp files, caches, email attachments, and unmanaged duplicates. |
| DATASTORE06 | What backup and recovery rule applies? | Define backup scope, frequency, restore test, retention, immutability, and recovery owner. |
| DATASTORE07 | What access log is required? | Track reads, writes, exports, deletes, privilege changes, sharing, and privileged access. |
| DATASTORE08 | What storage cost or capacity matters? | Estimate storage volume, growth, retrieval cost, egress, compute coupling, and archive fees. |
| DATASTORE09 | What storage exception exists? | Record offline copies, vendor portals, personal devices, temporary shares, and emergency access. |
| DATASTORE10 | What storage artifact is needed? | Produce storage plan, access matrix, backup policy, or data location register. |

## Retention Rules

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATARET01 | How long should data be retained? | Define minimum, maximum, active-use, legal, contractual, audit, operational, and user-request periods. |
| DATARET02 | What retention trigger starts the clock? | Use creation, collection, last use, publication, project close, contract end, consent withdrawal, or account deletion. |
| DATARET03 | What legal hold or freeze may apply? | Pause deletion for litigation, audit, investigation, regulatory request, incident response, or client hold. |
| DATARET04 | What retention schedule conflicts exist? | Resolve privacy deletion, finance retention, contract terms, research reproducibility, and security logs. |
| DATARET05 | What retention differs by data class? | Apply different rules to raw data, derived data, logs, backups, models, prompts, and final artifacts. |
| DATARET06 | What auto-expiry or manual review applies? | Schedule deletion, archive review, owner approval, renewal, or exception handling. |
| DATARET07 | What user or customer deletion right exists? | Handle access, correction, deletion, portability, objection, and consent withdrawal requests. |
| DATARET08 | What retention label should be attached? | Attach owner, date, schedule, trigger, hold status, disposal date, and exception reason. |
| DATARET09 | What retention monitoring is required? | Alert on expired data, missing labels, overdue holds, orphaned records, and unmanaged backups. |
| DATARET10 | What retention artifact is needed? | Produce retention schedule, hold register, expiry report, or retention decision log. |

## Archive And Preservation

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATAARCH01 | What should be archived? | Select final artifacts, evidence packs, raw sources, code, prompts, approvals, logs, and reusable templates. |
| DATAARCH02 | What archive purpose applies? | Preserve legal evidence, audit trail, reproducibility, historical record, customer handoff, or future reuse. |
| DATAARCH03 | What archive format is durable? | Choose open formats, checksums, metadata, manifests, package structure, and dependency snapshots. |
| DATAARCH04 | What archive access should remain? | Define read-only, restricted, public, escrowed, offline, or custodian-controlled access. |
| DATAARCH05 | What archive integrity proof is required? | Use checksums, signatures, immutable storage, version tags, chain of custody, and restore tests. |
| DATAARCH06 | What archive metadata is required? | Include title, owner, source, date, version, rights, retention, sensitivity, summary, and retrieval keywords. |
| DATAARCH07 | What archive should not preserve? | Exclude secrets, unnecessary PII, temporary files, drafts, cache data, and expired restricted content. |
| DATAARCH08 | What archive retrieval path exists? | Define search index, manifest, catalog entry, request process, and restore owner. |
| DATAARCH09 | What preservation risk exists? | Check bit rot, vendor lock-in, broken links, obsolete formats, missing context, and inaccessible encryption keys. |
| DATAARCH10 | What archive artifact is needed? | Produce archive package, manifest, preservation note, or restore test record. |

## Disposal And Deletion

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATADISP01 | What data should be deleted or disposed? | Identify expired, duplicate, unauthorized, unnecessary, superseded, risky, or user-requested deletion targets. |
| DATADISP02 | What disposal method is required? | Use secure delete, cryptographic erasure, account deletion, record purge, redaction, anonymization, or media destruction. |
| DATADISP03 | What dependencies block deletion? | Check legal hold, active workflow, audit need, linked artifacts, backups, model training, or downstream copies. |
| DATADISP04 | What derived data also needs action? | Delete, reprocess, relabel, or retain outputs, aggregates, embeddings, models, reports, and caches. |
| DATADISP05 | What backup deletion rule applies? | Define backup expiry, restore contamination handling, tombstones, and deletion propagation. |
| DATADISP06 | What proof of deletion is required? | Keep deletion log, system confirmation, vendor attestation, checksum list, or destruction certificate. |
| DATADISP07 | What user communication is needed? | Confirm deletion, explain limits, provide timeline, describe retained exceptions, and escalation path. |
| DATADISP08 | What disposal risk exists? | Avoid deleting evidence, breaking reports, violating holds, orphaning references, or leaving recoverable copies. |
| DATADISP09 | What disposal review is required? | Require owner, privacy, legal, security, records, or customer approval for sensitive deletion. |
| DATADISP10 | What disposal artifact is needed? | Produce deletion plan, disposal checklist, deletion certificate, or exception log. |

## Sharing And Egress

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATASHARE01 | Who can receive the data? | Identify internal team, client, vendor, public audience, regulator, partner, model provider, or archive custodian. |
| DATASHARE02 | What sharing purpose is allowed? | Match sharing to contract, consent, legal basis, operational need, publication, or collaboration goal. |
| DATASHARE03 | What minimum shared dataset is enough? | Redact, aggregate, sample, mask, tokenize, summarize, or provide synthetic substitute when possible. |
| DATASHARE04 | What transfer channel is approved? | Use secure link, managed drive, API, encrypted email, SFTP, data room, repository, or approved connector. |
| DATASHARE05 | What cross-border or third-party rule applies? | Check jurisdiction, data processing agreement, subprocessors, SCCs, export controls, and vendor policy. |
| DATASHARE06 | What downstream restriction travels with data? | Attach license, retention, deletion, confidentiality, attribution, no-training, no-reshare, or purpose limits. |
| DATASHARE07 | What egress logging is required? | Track recipient, data scope, date, channel, approval, expiry, download, and revocation. |
| DATASHARE08 | What sharing revocation is possible? | Define link expiry, access removal, takedown, deletion request, key rotation, and recipient notice. |
| DATASHARE09 | What sharing validation is needed? | Inspect redaction, permissions, recipient identity, watermark, package contents, and download access. |
| DATASHARE10 | What sharing artifact is needed? | Produce sharing approval, redaction report, egress log, or recipient handoff note. |

## Migration And Portability

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATAMIGR01 | What data must move between systems? | Define source, destination, object types, volume, schema, ownership, and cutover scope. |
| DATAMIGR02 | What mapping or transformation is required? | Map fields, IDs, units, encodings, permissions, metadata, relationships, and validation rules. |
| DATAMIGR03 | What data portability obligation exists? | Support user export, client handoff, vendor exit, regulatory portability, or archive transfer. |
| DATAMIGR04 | What migration freeze or cutover applies? | Plan read-only window, delta sync, backfill, rollback, and parallel run. |
| DATAMIGR05 | What migration validation is required? | Compare row counts, checksums, referential integrity, samples, business metrics, and user acceptance. |
| DATAMIGR06 | What permission migration risk exists? | Preserve or intentionally reset roles, groups, shares, ownership, and audit logs. |
| DATAMIGR07 | What data loss or corruption risk exists? | Plan backups, restore points, test migration, dry run, and reconciliation. |
| DATAMIGR08 | What legacy system disposition follows? | Decide decommission, archive, read-only retention, contract termination, or secure wipe. |
| DATAMIGR09 | What migration communication is required? | Notify users, owners, vendors, clients, support, and auditors about timing, impacts, and fallback. |
| DATAMIGR10 | What migration artifact is needed? | Produce migration plan, mapping table, reconciliation report, or cutover checklist. |

## Governance And Stewardship

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATAGOV01 | What governance policy applies? | Map data to privacy, security, records, AI, legal, finance, research, brand, and customer policies. |
| DATAGOV02 | Who stewards the lifecycle? | Assign owner for inventory, quality, access, retention, archive, deletion, sharing, and audit. |
| DATAGOV03 | What data contract is required? | Define schema, SLA, freshness, quality, access, retention, lineage, and change notice expectations. |
| DATAGOV04 | What change-control applies? | Review schema changes, source changes, model changes, retention changes, and vendor changes. |
| DATAGOV05 | What exception process exists? | Record exception request, risk, approval, compensating control, expiry, and re-review. |
| DATAGOV06 | What training or handling guidance is needed? | Provide labels, examples, do/don't rules, secure handling, and escalation paths. |
| DATAGOV07 | What catalog or index entry is needed? | Register dataset, owner, purpose, schema, sensitivity, lineage, retention, and access route. |
| DATAGOV08 | What lifecycle KPI should be monitored? | Track stale data, orphaned data, expired data, access violations, quality failures, and deletion backlog. |
| DATAGOV09 | What governance review cadence applies? | Schedule monthly, quarterly, annual, event-triggered, incident-triggered, or project-close review. |
| DATAGOV10 | What governance artifact is needed? | Produce data governance card, stewardship RACI, data contract, or exception register. |

## Lifecycle Audit And Learning

| Code | Data lifecycle question | Workflow use |
|---|---|---|
| DATAAUD01 | What lifecycle evidence must be auditable? | Preserve inventory, collection proof, classification, access, lineage, retention, sharing, deletion, and approvals. |
| DATAAUD02 | What audit question must be answerable? | Prove who had what data, why, when, from where, where it went, and what happened to it. |
| DATAAUD03 | What sampling or control test applies? | Test access logs, retention labels, deletion records, archive restore, sharing approvals, and lineage traces. |
| DATAAUD04 | What lifecycle incident occurred? | Record unauthorized collection, over-retention, bad deletion, broken archive, bad migration, or improper sharing. |
| DATAAUD05 | What remediation is required? | Reclassify, revoke access, delete, restore, notify, retrain, change contract, or update policy. |
| DATAAUD06 | What downstream artifact must be corrected? | Update reports, models, dashboards, prompts, summaries, citations, and customer deliverables. |
| DATAAUD07 | What audit owner signs off? | Assign privacy, security, records, legal, data owner, client, or regulator-facing owner. |
| DATAAUD08 | What lesson should become reusable? | Add checklist items, templates, validation scripts, retention rules, index tags, and test cases. |
| DATAAUD09 | What unresolved lifecycle risk remains? | Document residual risk, accepted exception, monitoring plan, and next review. |
| DATAAUD10 | What audit artifact is needed? | Produce lifecycle audit pack, control test report, incident log, or lessons update. |
