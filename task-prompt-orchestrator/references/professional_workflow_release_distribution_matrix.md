# Professional Workflow Release Distribution Matrix

Use this matrix when a workflow must move a finished or approved artifact into a real destination: production, client handoff, app deployment, website publishing, prompt-library release, document distribution, CAD/package delivery, dataset export, marketplace listing, email campaign, internal rollout, or any channel where versioning, release gates, packaging, rollout, rollback, and post-release verification matter.

## Release Scope

| Code | Release question | Workflow use |
|---|---|---|
| RELPLAN01 | What exactly is being released? | Define artifact, feature, prompt, file, model, dataset, design, process, app, report, or package. |
| RELPLAN02 | Who is the release audience? | Identify internal users, client, public users, operators, reviewers, regulators, vendors, or downstream systems. |
| RELPLAN03 | What destination receives the release? | Name production system, website, app store, cloud, file share, repository, CMS, email list, print vendor, or client portal. |
| RELPLAN04 | What release type is this? | Classify draft, preview, beta, pilot, staged rollout, full launch, hotfix, patch, migration, or archival release. |
| RELPLAN05 | What release boundary is out of scope? | Prevent accidental release to public, wrong tenant, wrong market, wrong repo, or unapproved recipient. |
| RELPLAN06 | What release dependencies must be ready? | Check approvals, assets, source evidence, translations, legal, analytics, support, training, and operational readiness. |
| RELPLAN07 | What release timing matters? | Define target date, freeze window, embargo, campaign date, maintenance window, timezone, and rollback window. |
| RELPLAN08 | What release success means? | Define available, accessible, discoverable, accepted, installed, delivered, acknowledged, or measurable usage. |
| RELPLAN09 | What release risk level applies? | Classify low, moderate, high, regulated, customer-impacting, revenue-impacting, safety-impacting, or irreversible. |
| RELPLAN10 | What release plan artifact should exist? | Produce release brief with artifact, destination, audience, owner, timing, risk, dependencies, and success criteria. |

## Release Gate

| Code | Release question | Workflow use |
|---|---|---|
| RELGATE01 | What must pass before release? | Require tests, reviews, evidence, approvals, legal checks, accessibility, security, or acceptance criteria. |
| RELGATE02 | Who can approve release? | Identify accountable approver, reviewer, product owner, client, legal, security, QA, or operations lead. |
| RELGATE03 | What approval evidence is required? | Capture signoff, ticket, checklist, comment, timestamp, approved artifact version, and release scope. |
| RELGATE04 | What issue blocks release? | Stop on failed tests, missing evidence, unresolved high risks, stale sources, security findings, or unclear ownership. |
| RELGATE05 | What issue allows conditional release? | Permit known low-risk defects with disclosure, mitigation, owner, deadline, and rollback plan. |
| RELGATE06 | What gate applies to public release? | Add brand, legal, privacy, accessibility, security, source, and public-claim checks. |
| RELGATE07 | What gate applies to client delivery? | Add scope match, deliverable checklist, confidentiality, licensing, acceptance, and handoff instructions. |
| RELGATE08 | What gate applies to production deployment? | Add build, test, config, migration, monitoring, rollback, incident contact, and change approval. |
| RELGATE09 | What gate applies to physical or manufacturing outputs? | Add dimensions, tolerances, materials, safety, vendor specs, print proof, and signoff. |
| RELGATE10 | What release-gate record should be kept? | Preserve gate checklist, pass/fail status, approvers, exceptions, and release decision. |

## Version And Change Set

| Code | Release question | Workflow use |
|---|---|---|
| VERSION01 | What version is being released? | Assign semantic version, date version, revision, document version, build number, or package ID. |
| VERSION02 | What changed since the last version? | Summarize additions, fixes, removals, risk changes, source refreshes, and known limitations. |
| VERSION03 | What compatibility matters? | Check backward compatibility, file format, API, schema, prompt variables, browser, device, vendor, or print compatibility. |
| VERSION04 | What migration is required? | Define data migration, content migration, template update, config change, training change, or user transition. |
| VERSION05 | What dependency versions must be frozen? | Pin model, library, design system, source dataset, prompt template, standards, or vendor spec versions. |
| VERSION06 | What version should remain available? | Decide prior release retention, archive, support window, rollback version, or deprecated copy. |
| VERSION07 | What version label must users see? | Expose release date, revision, build, changelog, status, region, language, or beta label. |
| VERSION08 | What change set needs review? | Review diff, release notes, modified files, prompt changes, data rows, design assets, and generated artifacts. |
| VERSION09 | What change risk should be called out? | Flag breaking change, data change, UX change, policy change, price change, content claim, or manufacturing change. |
| VERSION10 | What version artifact should be produced? | Produce changelog, release notes, manifest, tag, checksum, diff summary, or bill of materials. |

## Packaging And Build

| Code | Release question | Workflow use |
|---|---|---|
| PACKAGE01 | What final package format is required? | Choose zip, PDF, DOCX, PPTX, HTML, app build, dataset, prompt pack, image set, CAD export, or print-ready files. |
| PACKAGE02 | What files belong in the package? | Include final artifacts, source references, manifests, licenses, instructions, QA evidence, and required assets. |
| PACKAGE03 | What files must be excluded? | Remove drafts, secrets, private notes, raw personal data, internal comments, temp files, and unrelated outputs. |
| PACKAGE04 | What package structure is expected? | Define folder layout, file names, version labels, language variants, metadata, and index files. |
| PACKAGE05 | What build step is required? | Run compile, render, export, compress, validate, sign, notarize, generate thumbnails, or create checksums. |
| PACKAGE06 | What package quality check is required? | Verify file opens, links work, assets load, images render, docs compile, schemas validate, and dimensions match. |
| PACKAGE07 | What package metadata is required? | Add title, version, author, license, date, source, target audience, tags, and retention notes. |
| PACKAGE08 | What package size or performance limit applies? | Optimize file size, load time, print resolution, media bitrate, dataset rows, or deployment bundle size. |
| PACKAGE09 | What package should be signed or sealed? | Apply signature, checksum, approval stamp, watermark, certification, or immutable archive where needed. |
| PACKAGE10 | What package manifest should be kept? | Record included files, excluded files, versions, hashes, build commands, QA status, and destination. |

## Channel Selection

| Code | Release question | Workflow use |
|---|---|---|
| RELCHAN01 | Which channel reaches the intended audience? | Choose website, app store, email, Slack, Drive, CMS, marketplace, repository, API, print, or client portal. |
| RELCHAN02 | Which channel is authoritative? | Define source of truth when release appears in multiple places. |
| RELCHAN03 | Which channel is draft or preview only? | Keep review links, staging URLs, proof PDFs, beta builds, and internal previews separate from final release. |
| RELCHAN04 | Which channel has format constraints? | Account for size, aspect ratio, metadata, accessibility, file type, embed, schema, or listing requirements. |
| RELCHAN05 | Which channel has policy constraints? | Check platform rules, brand rules, privacy, copyright, marketplace terms, app review, or email compliance. |
| RELCHAN06 | Which channel has audience segmentation? | Target region, language, cohort, plan tier, customer, team, role, or permission group. |
| RELCHAN07 | Which channel needs coordinated timing? | Align release with campaign, training, support, stakeholder notification, embargo, or maintenance window. |
| RELCHAN08 | Which channel needs monitoring after release? | Attach analytics, uptime, delivery, open rate, download count, feedback, or error monitoring. |
| RELCHAN09 | Which channel fallback exists? | Prepare alternate link, offline package, mirror, rollback channel, or manual delivery path. |
| RELCHAN10 | What channel map should be produced? | Record channel, audience, format, owner, timing, access, monitoring, and fallback. |

## Rollout Strategy

| Code | Release question | Workflow use |
|---|---|---|
| ROLLOUT01 | Should release be all-at-once or staged? | Choose full launch, pilot, phased rollout, canary, region rollout, cohort rollout, or feature flag. |
| ROLLOUT02 | What first group should receive the release? | Select internal users, test cohort, low-risk customers, beta testers, or representative users. |
| ROLLOUT03 | What expansion criteria apply? | Expand after quality, adoption, error rate, feedback, SLA, support, and risk thresholds pass. |
| ROLLOUT04 | What hold criteria apply? | Pause on defects, complaints, cost spike, security event, poor adoption, failed QA, or operational overload. |
| ROLLOUT05 | What feature flag or access control is needed? | Use flags, permissions, invite lists, hidden links, staged publishing, or account targeting. |
| ROLLOUT06 | What rollout communication is needed at each phase? | Notify pilot users, support, stakeholders, customers, and leadership with phase-appropriate detail. |
| ROLLOUT07 | What rollout support must be ready? | Prepare help docs, support scripts, troubleshooting, training, escalation, and rollback contacts. |
| ROLLOUT08 | What rollout metric decides success? | Track activation, acceptance, error rate, support volume, quality, conversion, or task completion. |
| ROLLOUT09 | What rollout timeline should be documented? | Define phase dates, gates, owner, expansion criteria, and final availability date. |
| ROLLOUT10 | What rollout record should be archived? | Preserve cohorts, timing, metrics, decisions, incidents, feedback, and final status. |

## Release Communication

| Code | Release question | Workflow use |
|---|---|---|
| RELCOMM01 | Who needs to know about the release? | Identify users, clients, support, sales, operations, leadership, vendors, regulators, or public audience. |
| RELCOMM02 | What does each audience need to know? | Tailor value, change summary, action needed, risk, timeline, support path, and limitations. |
| RELCOMM03 | What communication channel should be used? | Choose email, changelog, release notes, Slack, in-app message, documentation, meeting, or public post. |
| RELCOMM04 | What user action is required? | Ask recipients to update, review, approve, migrate, download, acknowledge, train, or provide feedback. |
| RELCOMM05 | What should be disclosed as known limitations? | Mention scoped exclusions, unresolved low-risk issues, compatibility limits, or staged availability. |
| RELCOMM06 | What support or escalation path should be included? | Provide contact, ticket link, help doc, runbook, FAQ, or rollback request path. |
| RELCOMM07 | What launch narrative is needed? | Explain why the release matters, what changed, and how success will be measured. |
| RELCOMM08 | What legal or compliance wording is needed? | Include disclaimers, terms, privacy notices, license, attribution, or regulatory statements. |
| RELCOMM09 | What release communication must be approved? | Gate external, legal, public, executive, customer, investor, or regulated communications. |
| RELCOMM10 | What communication evidence should be kept? | Archive sent messages, recipients, approvals, publication URL, and acknowledgement status. |

## Migration And Transition

| Code | Release question | Workflow use |
|---|---|---|
| MIGRATE01 | What existing users, files, data, or habits must transition? | Identify old version, legacy workflow, prior template, stale link, retired system, or manual process. |
| MIGRATE02 | What migration path is required? | Define automatic migration, manual steps, import/export, mapping table, training, or coexistence period. |
| MIGRATE03 | What compatibility bridge is needed? | Support old and new formats, redirects, aliases, dual-run, adapters, or conversion scripts. |
| MIGRATE04 | What data or content must be transformed? | Map fields, file names, taxonomy, permissions, prompts, layouts, metadata, or configuration. |
| MIGRATE05 | What migration validation is required? | Check row counts, checksums, sample outputs, user access, visual parity, links, and acceptance criteria. |
| MIGRATE06 | What migration fallback is needed? | Prepare restore, previous version, manual correction, alternate workflow, or rollback package. |
| MIGRATE07 | What migration communication is needed? | Tell users what changes, deadlines, actions, support, and consequences apply. |
| MIGRATE08 | What migration timing minimizes disruption? | Choose maintenance window, phased migration, low-volume period, or user-selected transition. |
| MIGRATE09 | What migration issue should block release? | Block on data loss, permission mismatch, broken compatibility, failed validation, or missing owner. |
| MIGRATE10 | What migration record should be preserved? | Keep mappings, validation evidence, exceptions, user notices, and rollback status. |

## Rollback And Withdrawal

| Code | Release question | Workflow use |
|---|---|---|
| RELBACK01 | What rollback path exists before release? | Define previous version, restore point, feature flag, package archive, backup, or manual withdrawal. |
| RELBACK02 | What condition triggers rollback? | Trigger on critical defect, security issue, legal block, broken channel, failed migration, or severe user impact. |
| RELBACK03 | Who can authorize rollback? | Identify release owner, incident lead, client approver, security, operations, or executive authority. |
| RELBACK04 | What can be rolled back safely? | Separate reversible content, config, feature flags, builds, docs, data migrations, and public communications. |
| RELBACK05 | What cannot be fully rolled back? | Flag emails sent, public downloads, printed materials, external posts, client exports, and data changes. |
| RELBACK06 | What rollback communication is needed? | Notify affected users, support, clients, stakeholders, and channels with status and next steps. |
| RELBACK07 | What rollback validation is required? | Confirm prior version active, links updated, access restored, errors stopped, and users unblocked. |
| RELBACK08 | What withdrawal or takedown process is needed? | Remove public posts, delist package, revoke link, unpublish page, replace file, or recall artifact. |
| RELBACK09 | What follow-up release is needed? | Plan hotfix, corrected package, reissue notice, migration repair, or postmortem. |
| RELBACK10 | What rollback evidence should be archived? | Record trigger, decision, steps, affected scope, validation, communication, and residual risk. |

## Post-Release Verification

| Code | Release question | Workflow use |
|---|---|---|
| POSTREL01 | How do we prove the release reached the destination? | Verify URL, deployment, file share, recipient delivery, download, app store status, or client acknowledgement. |
| POSTREL02 | How do we prove the right version is live? | Check version label, checksum, build number, metadata, changelog, release tag, or visible content. |
| POSTREL03 | How do we prove access is correct? | Test permissions, audience segment, login state, sharing settings, geo/language variant, and public visibility. |
| POSTREL04 | How do we prove functionality or artifact quality after release? | Run smoke tests, link checks, render checks, sample downloads, visual review, or API checks. |
| POSTREL05 | How do we prove monitoring is active? | Confirm analytics, logs, alerts, dashboards, feedback paths, and ownership are live. |
| POSTREL06 | How do we prove users can take the intended action? | Test onboarding, CTA, form, purchase, download, install, import, print, or support flow. |
| POSTREL07 | How do we detect early release issues? | Watch support tickets, errors, complaints, bounce rates, conversion drops, or quality regressions. |
| POSTREL08 | What post-release review timing applies? | Review immediately, after first hour, first day, first week, first batch, or first client response. |
| POSTREL09 | What post-release signoff is required? | Get owner, QA, client, support, or operations confirmation that release is accepted. |
| POSTREL10 | What post-release evidence should be kept? | Preserve live URL, version proof, access proof, test results, monitoring proof, and acceptance record. |

## Release Support Readiness

| Code | Release question | Workflow use |
|---|---|---|
| RELSUPPORT01 | What support team needs to be ready for the release? | Identify support, operations, sales, customer success, implementation, vendor, or account teams. |
| RELSUPPORT02 | What support materials must be ready? | Prepare FAQ, help article, troubleshooting guide, known issues, escalation path, and contact script. |
| RELSUPPORT03 | What operational runbook must be ready? | Include deploy steps, validation checks, rollback, incident handling, monitoring, and owner contacts. |
| RELSUPPORT04 | What training must happen before release? | Train operators, support, reviewers, admins, clients, or internal users on changed workflows. |
| RELSUPPORT05 | What support load is expected? | Forecast tickets, questions, onboarding load, review volume, call volume, or manual intervention. |
| RELSUPPORT06 | What support escalation threshold applies? | Escalate when issue volume, severity, blocked users, client impact, or SLA risk exceeds threshold. |
| RELSUPPORT07 | What known issue handling is required? | Publish workaround, owner, severity, affected scope, fix plan, and user-facing wording. |
| RELSUPPORT08 | What release support channel should be monitored? | Watch help desk, chat, email, forums, social, client portal, telemetry, or account notes. |
| RELSUPPORT09 | What support readiness should block release? | Block on missing runbook, untrained support, no rollback contact, unresolved known issue, or missing escalation. |
| RELSUPPORT10 | What support readiness evidence should be kept? | Archive runbook, training status, FAQ, support ownership, known issues, and escalation plan. |

## Distribution Audit

| Code | Release question | Workflow use |
|---|---|---|
| DISTAUDIT01 | Was the release delivered only to intended destinations? | Audit channels, recipients, tenants, public links, repos, environments, and printed/exported packages. |
| DISTAUDIT02 | Was the correct artifact released? | Compare manifest, checksum, version, package contents, file names, and visible metadata. |
| DISTAUDIT03 | Were release gates completed? | Verify tests, approvals, signoffs, legal, security, QA, accessibility, and acceptance evidence. |
| DISTAUDIT04 | Were channel constraints respected? | Check format, policy, size, metadata, locale, audience, and platform-specific requirements. |
| DISTAUDIT05 | Were communications sent and archived? | Confirm release notes, notices, recipient list, support instructions, and approval records. |
| DISTAUDIT06 | Was rollback readiness real? | Verify previous version, restore point, withdrawal path, contacts, and rollback validation steps. |
| DISTAUDIT07 | Were early release metrics reviewed? | Check adoption, errors, support, quality, performance, cost, and user feedback. |
| DISTAUDIT08 | Were release exceptions closed or tracked? | Track known issues, conditional approvals, post-release fixes, and unresolved risks. |
| DISTAUDIT09 | Was the release knowledge captured for reuse? | Save release checklist, manifest, lessons, templates, channel notes, and decision records. |
| DISTAUDIT10 | What release improvement should be made next? | Identify missing gate, packaging issue, channel weakness, rollback gap, or communication improvement. |

