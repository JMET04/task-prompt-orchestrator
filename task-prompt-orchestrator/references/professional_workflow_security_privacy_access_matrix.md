# Professional Workflow Security Privacy Access Matrix

Use this matrix when a workflow touches private data, regulated information, credentials, connected apps, local files, user accounts, customer records, vendor systems, publishing, sharing, automation, code execution, data movement, or any action where permissions, secrecy, consent, safety, or access boundaries must be explicit before execution.

## Security Boundary

| Code | Security question | Workflow use |
|---|---|---|
| SECBOUND01 | What systems, files, accounts, or environments are in scope? | Define the exact boundary before reading, writing, exporting, or automating anything. |
| SECBOUND02 | What systems or data are explicitly out of scope? | Prevent accidental access to unrelated accounts, drives, repos, folders, tenants, or production systems. |
| SECBOUND03 | What trust zones does the workflow cross? | Identify local device, cloud app, external API, public web, vendor, client, and production boundaries. |
| SECBOUND04 | What action changes the security boundary? | Flag uploads, downloads, connector use, sharing, deployment, publishing, email sends, and database writes. |
| SECBOUND05 | What user authority is assumed? | Record whether the user owns, administers, or merely references the source or system. |
| SECBOUND06 | What environment is safe for this task? | Choose sandbox, local copy, staging, read-only mode, test account, or production with gate. |
| SECBOUND07 | What boundary evidence should be captured? | Record paths, app names, account scope, tenant, project, branch, dataset, and target environment. |
| SECBOUND08 | What boundary mismatch would block the workflow? | Stop when the request crosses into unowned data, unknown accounts, or unsafe production scope. |
| SECBOUND09 | What boundary should be disclosed to the user? | Briefly state when work is limited to visible/local/user-provided materials. |
| SECBOUND10 | What boundary review is needed before completion? | Confirm the final artifact did not include out-of-scope files, data, accounts, or systems. |

## Data Classification

| Code | Security question | Workflow use |
|---|---|---|
| SECDATACLASS01 | What sensitivity class applies to each input? | Label public, internal, confidential, restricted, regulated, personal, secret, or unknown. |
| SECDATACLASS02 | Does the input contain personal data? | Identify names, emails, phone numbers, addresses, IDs, account data, location, or biometrics. |
| SECDATACLASS03 | Does the input contain regulated data? | Flag health, legal, financial, employment, education, minors, payment, or government identifiers. |
| SECDATACLASS04 | Does the input contain secrets? | Detect API keys, passwords, tokens, private keys, connection strings, cookies, or credentials. |
| SECDATACLASS05 | Does the input contain proprietary or client data? | Treat designs, CAD files, datasets, contracts, source code, plans, and research as controlled. |
| SECDATACLASS06 | What classification is unknown? | Mark unknown rather than assuming safe when source origin or content is unclear. |
| SECDATACLASS07 | What classification affects tool choice? | Avoid sending restricted data to external tools unless permission and policy allow it. |
| SECDATACLASS08 | What classification affects storage or export? | Choose redacted, local-only, encrypted, internal, or no-persist handling. |
| SECDATACLASS09 | What classification affects final output? | Prevent accidental exposure of secrets, identifiers, private facts, or controlled materials. |
| SECDATACLASS10 | What classification artifact should be left? | Produce a data-classification note, table, or checklist for sensitive workflows. |

## Identity And Access

| Code | Security question | Workflow use |
|---|---|---|
| IDACCESS01 | Who is acting in this workflow? | Distinguish user, agent, tool, service account, connector, reviewer, and approver identities. |
| IDACCESS02 | What identity owns each credential or connection? | Map API keys, OAuth connections, CLIs, cloud accounts, and app sessions to the right owner. |
| IDACCESS03 | What account context is currently active? | Verify tenant, organization, subscription, repo, cloud project, region, and profile before action. |
| IDACCESS04 | What role or permission is required? | Define read, write, admin, publish, deploy, billing, delete, invite, export, or approve rights. |
| IDACCESS05 | What access is missing? | Mark disconnected apps, expired sessions, unavailable credentials, or insufficient role permissions. |
| IDACCESS06 | What access should not be requested? | Avoid asking for broad admin, persistent credentials, or unrelated account access. |
| IDACCESS07 | What identity should perform the action? | Use the least privileged human, connector, service account, or local tool. |
| IDACCESS08 | What identity evidence should be verified? | Check CLI profile, selected workspace, app connector state, account name, and target IDs. |
| IDACCESS09 | What identity handoff is needed? | Ask the user to complete auth, approval, upload, purchase, or protected action themselves when required. |
| IDACCESS10 | What identity risk should be disclosed? | Warn when action depends on ambiguous account context or elevated rights. |

## Permission Control

| Code | Security question | Workflow use |
|---|---|---|
| PERMCTRL01 | What is the minimum permission needed? | Use read-only, scoped, temporary, or single-resource access whenever possible. |
| PERMCTRL02 | What action requires explicit confirmation? | Gate destructive, irreversible, public, paid, account-changing, or high-impact operations. |
| PERMCTRL03 | What action is safe to perform without interruption? | Proceed with read-only inspection, local validation, draft creation, or reversible edits within scope. |
| PERMCTRL04 | What permission boundary applies to automation? | Limit automation to named resources, dry-run first, and avoid broad recursive side effects. |
| PERMCTRL05 | What permission boundary applies to sharing? | Restrict recipients, visibility, link access, download rights, comment rights, and expiration. |
| PERMCTRL06 | What permission boundary applies to generated artifacts? | Control where files, reports, images, logs, and exports are written or published. |
| PERMCTRL07 | What permission boundary applies to agents or subagents? | Share only task-local context, avoid secrets, and restrict production-side effects. |
| PERMCTRL08 | What permission should be revoked or reduced after work? | Remove temporary access, expire links, delete tokens, or close sessions where appropriate. |
| PERMCTRL09 | What permission decision must be logged? | Record requested scope, granted scope, confirmation, actor, timestamp, and action. |
| PERMCTRL10 | What permission review proves safe completion? | Verify no unexpected writes, shares, deletes, permissions, or public exposure occurred. |

## Secret Handling

| Code | Security question | Workflow use |
|---|---|---|
| SECRETS01 | Did the workflow encounter credentials or tokens? | Stop display, redact, and avoid copying secrets into prompts, logs, files, or final answers. |
| SECRETS02 | What secret type is present? | Classify API key, OAuth token, password, private key, certificate, cookie, session, or connection string. |
| SECRETS03 | Is the secret still valid or exposed? | Treat visible secrets as compromised unless verified otherwise. |
| SECRETS04 | What secret should be stored only in environment or secret manager? | Route credentials to env files, vaults, platform secrets, or user-side entry flows. |
| SECRETS05 | What secret must not be persisted? | Avoid writing secrets to markdown, screenshots, chat, git, logs, caches, or generated artifacts. |
| SECRETS06 | What redaction pattern is needed? | Preserve enough prefix/suffix or label for identification without revealing usable value. |
| SECRETS07 | What rotation guidance is needed? | Recommend rotation when a secret was pasted, logged, committed, or sent to an unsafe context. |
| SECRETS08 | What secret scanning is needed? | Search diffs, outputs, logs, and generated files for credential patterns when risk exists. |
| SECRETS09 | What secret handoff is safe? | Use local confirmation tools, platform pickers, or user-entered env vars rather than exposing values. |
| SECRETS10 | What secret-handling evidence should be kept? | Record redaction, storage location type, rotation need, and scan result without revealing secret values. |

## Privacy Minimization

| Code | Security question | Workflow use |
|---|---|---|
| PRIVMIN01 | What personal data is necessary for the task? | Use only fields that directly affect the requested decision or artifact. |
| PRIVMIN02 | What personal data can be removed? | Drop direct identifiers, contact details, location, demographics, free-text notes, or account data when not needed. |
| PRIVMIN03 | What personal data can be aggregated? | Use counts, cohorts, ranges, or anonymized summaries instead of row-level details. |
| PRIVMIN04 | What personal data can be pseudonymized? | Replace names, emails, IDs, and customer records with stable non-identifying labels. |
| PRIVMIN05 | What personal data should remain local only? | Avoid external tools for sensitive records unless the user explicitly authorizes and policy allows it. |
| PRIVMIN06 | What sensitive attribute needs extra care? | Flag health, age, disability, race, religion, politics, sexuality, union, biometrics, or protected status. |
| PRIVMIN07 | What inference about a person should be avoided? | Avoid unsupported profiling, sensitive classification, or unnecessary personal judgments. |
| PRIVMIN08 | What privacy caveat should be included? | State when analysis used redacted, sampled, aggregated, or partial data. |
| PRIVMIN09 | What privacy review is needed before sharing? | Check recipients, identifiers, small cohorts, re-identification risk, and hidden metadata. |
| PRIVMIN10 | What minimization evidence should be preserved? | Record removed fields, aggregation level, pseudonymization method, and residual risk. |

## Consent And Purpose

| Code | Security question | Workflow use |
|---|---|---|
| CONSENT01 | What is the stated purpose for using the data? | Tie data use to the user's request and avoid unrelated secondary use. |
| CONSENT02 | Did the user provide the material or authorize access? | Distinguish user-provided data from third-party, scraped, connected, or inferred data. |
| CONSENT03 | What consent is missing or unclear? | Ask or defer when using private, regulated, customer, employee, or third-party data is not justified. |
| CONSENT04 | What purpose limitation applies? | Do not reuse data for training, profiling, outreach, publishing, or unrelated analysis without permission. |
| CONSENT05 | What audience is authorized to see the output? | Restrict internal, client, public, reviewer, regulator, or vendor visibility. |
| CONSENT06 | What retention expectation applies? | Decide whether data should be transient, archived, versioned, or deleted after use. |
| CONSENT07 | What consent boundary applies to generated media? | Check likeness, brand, copyright, minors, private location, or sensitive context before generation or editing. |
| CONSENT08 | What consent boundary applies to communications? | Avoid sending messages, invites, emails, posts, or notifications without explicit authorization. |
| CONSENT09 | What consent record should be kept? | Record authorization source, purpose, audience, retention, and any user confirmation. |
| CONSENT10 | What consent disclosure belongs in the final answer? | Mention only material limits, unavailable authorization, or user action still required. |

## Secure Sharing

| Code | Security question | Workflow use |
|---|---|---|
| SAFESHARE01 | Who should receive the output? | Define recipient roles, groups, domains, or public audience before sharing. |
| SAFESHARE02 | What output visibility is appropriate? | Choose private draft, local file, internal link, restricted share, client share, or public release. |
| SAFESHARE03 | What content must be removed before sharing? | Redact secrets, identifiers, private notes, hidden columns, comments, metadata, or internal reasoning. |
| SAFESHARE04 | What file metadata should be checked? | Inspect author names, tracked changes, comments, EXIF, hidden sheets, speaker notes, and embedded files. |
| SAFESHARE05 | What link settings are safe? | Set specific recipients, expiration, view-only, disable download, or no public indexing where needed. |
| SAFESHARE06 | What watermark or classification label is needed? | Mark confidential, draft, internal, restricted, public, or client-visible. |
| SAFESHARE07 | What export format reduces risk? | Use flattened PDF, redacted image, sanitized CSV, compiled artifact, or summary instead of raw source. |
| SAFESHARE08 | What sharing approval is required? | Gate external, public, regulated, client, legal, or executive releases. |
| SAFESHARE09 | What sharing log should be preserved? | Record artifact, audience, channel, permission, approval, and date. |
| SAFESHARE10 | What post-share review is needed? | Confirm access settings, recipients, public exposure, and revocation options. |

## Threat And Abuse Check

| Code | Security question | Workflow use |
|---|---|---|
| THREAT01 | Could this workflow enable unauthorized access? | Review credential use, bypass requests, account takeover, scraping, or privilege escalation risk. |
| THREAT02 | Could this workflow enable harmful automation? | Check spam, phishing, fraud, harassment, scraping, botting, or mass-account actions. |
| THREAT03 | Could this workflow expose private or regulated data? | Identify leakage paths through prompts, logs, links, generated files, or third-party tools. |
| THREAT04 | Could this workflow damage systems or data? | Review deletes, overwrites, migrations, deployments, scripts, and recursive file actions. |
| THREAT05 | Could this workflow create unsafe physical-world output? | Check CAD, manufacturing, medical, electrical, chemical, construction, aviation, or safety-critical advice. |
| THREAT06 | Could this workflow create misleading public claims? | Check citations, evidence, disclosure, impersonation, synthetic media, and reputation risk. |
| THREAT07 | Could this workflow violate platform or legal rules? | Check scraping terms, copyright, export controls, sanctions, privacy, and procurement constraints. |
| THREAT08 | What misuse-resistant alternative exists? | Provide benign summary, defensive analysis, redacted workflow, or high-level guidance. |
| THREAT09 | What threat gate must stop execution? | Stop if the request depends on unauthorized access, secret exposure, evasion, or harmful action. |
| THREAT10 | What threat assessment evidence should be kept? | Record risks considered, mitigations, stop gates, and safe alternative route. |

## Safe Execution

| Code | Security question | Workflow use |
|---|---|---|
| SAFEEXEC01 | Is there a read-only inspection path first? | Inspect state before writes, deletes, deployments, sends, or permission changes. |
| SAFEEXEC02 | Is there a dry-run or preview mode? | Use dry-run, plan, validation, staging, diff, preview, or sample execution before full action. |
| SAFEEXEC03 | Is there a backup or restore point? | Preserve manifests, copies, versions, rollback scripts, or recovery anchors before risky changes. |
| SAFEEXEC04 | Is the command scoped tightly enough? | Use explicit paths, literal parameters, filters, target IDs, and bounded batches. |
| SAFEEXEC05 | Is the output path safe? | Avoid overwriting originals, protected folders, system locations, secrets, or unrelated project files. |
| SAFEEXEC06 | Is parallelism safe? | Parallelize reads, but serialize edits, deployments, sends, permission changes, and destructive actions. |
| SAFEEXEC07 | Is there a stop condition? | Abort on unexpected target count, missing backup, permission mismatch, failed validation, or ambiguous state. |
| SAFEEXEC08 | Is there a human review gate? | Add approval before irreversible, external, public, legal, financial, or production-impacting actions. |
| SAFEEXEC09 | What execution trace should be kept? | Record commands, tool calls, target scope, key outputs, validation, and rollback notes. |
| SAFEEXEC10 | What final execution review is required? | Confirm target state, no extra side effects, tests passed, and sensitive output is clean. |

## Breach And Incident Response

| Code | Security question | Workflow use |
|---|---|---|
| BREACH01 | What event would count as a security or privacy incident? | Define exposure, unauthorized access, wrong recipient, secret leak, data loss, or unsafe publish. |
| BREACH02 | How is an incident detected? | Monitor errors, access logs, public links, secret scans, user reports, validation failures, or unexpected diffs. |
| BREACH03 | What immediate containment is needed? | Revoke links, rotate secrets, stop jobs, disable access, quarantine files, or pause deployment. |
| BREACH04 | What evidence should be preserved? | Keep timestamps, logs, affected resources, recipients, commands, diffs, and screenshots without spreading secrets. |
| BREACH05 | Who must be notified? | Identify user, owner, security, legal, compliance, client, regulator, or platform support. |
| BREACH06 | What remediation is required? | Remove exposure, restore data, patch workflow, tighten permissions, reissue artifacts, or correct recipients. |
| BREACH07 | What communication should be sent? | Provide factual, minimal, timestamped, non-speculative incident status and next actions. |
| BREACH08 | What root cause should be analyzed? | Review permission gaps, workflow defects, tool misuse, missing validation, or unclear ownership. |
| BREACH09 | What prevention update is needed? | Add checks, gates, redaction, scanning, access reviews, or training to the workflow. |
| BREACH10 | What incident closeout evidence is required? | Record containment, remediation, notification, validation, lessons, and residual risk. |

## Security Audit

| Code | Security question | Workflow use |
|---|---|---|
| SECAUDIT01 | Did the workflow respect declared boundaries? | Verify only in-scope systems, files, accounts, and data were accessed or changed. |
| SECAUDIT02 | Did the workflow classify sensitive data correctly? | Check public/internal/confidential/regulated/secret labels and unknowns. |
| SECAUDIT03 | Did the workflow use least privilege? | Review account, connector, token, file, share, and automation permissions. |
| SECAUDIT04 | Did the workflow avoid secret leakage? | Scan outputs, logs, diffs, prompts, generated files, and final response for secrets. |
| SECAUDIT05 | Did the workflow minimize personal data? | Verify redaction, aggregation, pseudonymization, and removal of unnecessary identifiers. |
| SECAUDIT06 | Did the workflow have proper consent and purpose? | Confirm user authorization, purpose limitation, audience, and retention. |
| SECAUDIT07 | Did the workflow share safely? | Check recipients, link settings, metadata, export format, and approval. |
| SECAUDIT08 | Did the workflow handle risky execution safely? | Confirm dry-run, backup, scoped command, stop conditions, and rollback readiness. |
| SECAUDIT09 | Did the workflow preserve audit evidence? | Verify logs, decisions, approvals, validation, incidents, and residual risks are traceable. |
| SECAUDIT10 | What security improvement should be added next? | Identify missing guardrail, validator, checklist, permission rule, or redaction pattern. |

