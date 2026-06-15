# Professional Workflow Source Evidence Matrix

Use this matrix when a workflow depends on external information, source material, research, user-provided files, datasets, market facts, web pages, standards, product specs, citations, examples, or evidence that must be collected, checked, normalized, cited, refreshed, or preserved.

## Source Scope

| Code | Evidence question | Workflow use |
|---|---|---|
| SRCPLAN01 | What decision or deliverable needs evidence? | Tie source collection to the actual output and avoid collecting irrelevant material. |
| SRCPLAN02 | What claims must be supported? | Identify factual, comparative, technical, legal, financial, design, or operational claims that need proof. |
| SRCPLAN03 | What source types are acceptable? | Define whether web pages, files, APIs, papers, standards, images, CAD files, datasets, interviews, or logs are allowed. |
| SRCPLAN04 | What source types are insufficient? | Exclude blogs, screenshots, stale summaries, social posts, generated text, or secondary sources when they are not enough. |
| SRCPLAN05 | What evidence depth is required? | Choose quick scan, representative sample, exhaustive search, source-backed memo, audit pack, or reproducible dataset. |
| SRCPLAN06 | What recency window applies? | Set whether current, latest, historical, version-specific, or evergreen evidence is needed. |
| SRCPLAN07 | What geography, language, or jurisdiction applies? | Scope sources by region, locale, market, standards body, or regulatory environment. |
| SRCPLAN08 | What source completeness threshold applies? | Define minimum source count, coverage, categories, time range, or corpus boundaries. |
| SRCPLAN09 | What uncertainty is acceptable? | Decide when approximation, inference, partial evidence, or unresolved gaps can be disclosed. |
| SRCPLAN10 | What source plan artifact should be produced? | Leave a short source plan listing needed claims, source classes, depth, recency, and evidence threshold. |

## Source Discovery

| Code | Evidence question | Workflow use |
|---|---|---|
| SRCDISC01 | Where should source search begin? | Prefer local files, provided materials, official sources, connected apps, or project indexes before broad web search. |
| SRCDISC02 | What official source exists? | Locate primary authorities such as documentation, standards bodies, filings, regulators, vendors, repositories, or APIs. |
| SRCDISC03 | What expert or secondary source helps interpret primary evidence? | Add credible analysis, reviews, surveys, or domain explainers when primary evidence is technical or incomplete. |
| SRCDISC04 | What dataset or structured source exists? | Prefer tables, APIs, catalogs, metadata, manifests, or machine-readable exports where available. |
| SRCDISC05 | What source query variants are needed? | Search by synonyms, model names, local language terms, version numbers, standards numbers, and competitor names. |
| SRCDISC06 | What source gaps need targeted search? | Identify missing categories, missing stakeholders, missing dates, or missing artifact types and search them directly. |
| SRCDISC07 | What source should be sampled rather than fully collected? | Use representative sampling when volume is high and exhaustive collection is not required. |
| SRCDISC08 | What source should be excluded as duplicate or low value? | Deduplicate mirrors, scraped copies, reposts, AI summaries, and near-identical pages. |
| SRCDISC09 | What source discovery log should be kept? | Record queries, repositories, connectors, local folders, and inclusion/exclusion decisions. |
| SRCDISC10 | What discovery stop rule applies? | Stop when coverage threshold, diminishing returns, time budget, or authoritative source closure is reached. |

## Authority And Quality Check

| Code | Evidence question | Workflow use |
|---|---|---|
| AUTHCHK01 | Is the source primary, secondary, or tertiary? | Weight evidence by authority and avoid treating summaries as originals. |
| AUTHCHK02 | Who created or owns the source? | Check author, organization, vendor, regulator, researcher, dataset maintainer, or repository owner. |
| AUTHCHK03 | Is the source current enough? | Verify publish date, last updated date, version, release, filing date, or observed timestamp. |
| AUTHCHK04 | Is the source complete enough? | Check missing pages, truncated text, incomplete tables, partial APIs, broken downloads, or inaccessible appendices. |
| AUTHCHK05 | Is the source biased or commercially motivated? | Flag promotional, adversarial, sponsored, partisan, or self-reported evidence. |
| AUTHCHK06 | Is the source technically reliable? | Check schema validity, checksum, documentation, reproducibility, version control, or known issue notes. |
| AUTHCHK07 | Is the source legally or contractually usable? | Check license, terms, attribution, privacy, procurement, or confidentiality limits. |
| AUTHCHK08 | Is the source consistent with other evidence? | Compare core facts, units, dates, definitions, and claims across sources. |
| AUTHCHK09 | What confidence level should be assigned? | Label high, medium, low, unknown, or blocked based on authority and verification. |
| AUTHCHK10 | What source-quality evidence should be kept? | Preserve authority notes, dates, versions, licenses, gaps, and confidence rationale. |

## Access And Rights

| Code | Evidence question | Workflow use |
|---|---|---|
| ACCESS01 | Can the workflow legally access this source? | Confirm public access, user-provided permission, connector authorization, or licensed use. |
| ACCESS02 | Does the source contain private or sensitive data? | Identify PII, PHI, trade secrets, credentials, payment data, minors, or confidential material. |
| ACCESS03 | What access method is safest? | Choose API, export, download, browsing, local read, connector, or user-provided excerpt. |
| ACCESS04 | What access credentials or connections are missing? | Mark auth, plugin connection, API key, VPN, account, purchase, or user upload gaps. |
| ACCESS05 | What terms restrict reuse or quoting? | Apply copyright, license, attribution, quote length, redistribution, and commercial-use constraints. |
| ACCESS06 | What source should not be ingested? | Exclude disallowed personal data, pirated material, private systems, or sources outside user permission. |
| ACCESS07 | What redaction is required before use? | Remove secrets, direct identifiers, payment details, private contact details, or regulated attributes. |
| ACCESS08 | What audit trail is needed for access? | Record source path, URL, connector, timestamp, user-provided status, and permission basis. |
| ACCESS09 | What fallback exists when access is unavailable? | Use public metadata, official summaries, alternate sources, or ask for user-provided exports. |
| ACCESS10 | What access caveat should appear in the output? | Disclose unavailable, restricted, partial, or user-provided-only evidence where material. |

## Collection And Capture

| Code | Evidence question | Workflow use |
|---|---|---|
| COLLECT01 | What exact source items should be captured? | List URLs, files, records, examples, rows, images, transcripts, commits, or artifacts. |
| COLLECT02 | What metadata must be captured with each item? | Store title, author, source, date, version, URL/path, access time, license, and owner. |
| COLLECT03 | What format should capture use? | Choose markdown, CSV, JSON, PDF, screenshot, raw text, image, transcript, or database export. |
| COLLECT04 | What capture granularity is needed? | Capture page, section, paragraph, table row, figure, field, prompt, code block, or full artifact. |
| COLLECT05 | What collection order is most efficient? | Gather authoritative sources first, then fill interpretation, examples, edge cases, and counterevidence. |
| COLLECT06 | How should large sources be chunked? | Chunk by document section, record batch, page range, time window, or semantic unit. |
| COLLECT07 | How should duplicates be detected? | Compare URL canonicalization, title, hash, text similarity, source ID, or row key. |
| COLLECT08 | How should collection failures be handled? | Retry, switch method, log missing item, use cached copy, or mark blocked. |
| COLLECT09 | What collection manifest should be produced? | Keep an itemized manifest of collected sources, metadata, status, and storage location. |
| COLLECT10 | What collection QA check is required? | Confirm source count, category coverage, readable content, metadata completeness, and missing items. |

## Extraction And Parsing

| Code | Evidence question | Workflow use |
|---|---|---|
| EXTRACT01 | What facts or fields must be extracted? | Define claim, metric, date, dimension, requirement, specification, quote, example, or decision fields. |
| EXTRACT02 | What structure should extracted evidence use? | Use tables, JSON, schema rows, evidence cards, requirement IDs, or source-note blocks. |
| EXTRACT03 | What extraction method is safest? | Prefer parsers, APIs, structured exports, OCR, or manual review based on source format. |
| EXTRACT04 | What extraction should preserve exact wording? | Preserve short quotes, requirements, legal text, technical specs, error messages, and identifiers. |
| EXTRACT05 | What extraction should be paraphrased? | Summarize copyrighted, lengthy, repetitive, or non-critical prose while keeping source references. |
| EXTRACT06 | What unit or definition must be captured? | Preserve units, denominators, assumptions, version, geography, time period, and calculation method. |
| EXTRACT07 | What visual evidence must be interpreted? | Extract labels, dimensions, callouts, layout, figure meaning, diagram flow, or CAD annotations. |
| EXTRACT08 | What extraction needs human or expert review? | Escalate ambiguous legal, medical, engineering, safety, financial, or visual interpretation. |
| EXTRACT09 | What extraction error checks are needed? | Compare source snippets, row counts, OCR quality, schema validity, and spot-check samples. |
| EXTRACT10 | What extracted-evidence artifact should be left? | Produce evidence table, source card set, parsed dataset, claim map, or extraction log. |

## Normalization And Structuring

| Code | Evidence question | Workflow use |
|---|---|---|
| NORM01 | What fields need normalized names? | Standardize source, title, author, date, version, category, code, status, and claim IDs. |
| NORM02 | What units need normalization? | Convert length, mass, currency, time, percentages, dates, coordinate systems, and scale. |
| NORM03 | What categories need controlled vocabulary? | Map industries, workflows, artifact types, risks, materials, roles, channels, or product classes. |
| NORM04 | What dates need a consistent format? | Use absolute dates and record timezone, version, release, or observed-at time when needed. |
| NORM05 | What identifiers need canonical form? | Normalize URLs, DOIs, SKUs, model names, file paths, issue IDs, standards, and part numbers. |
| NORM06 | What source hierarchy should be represented? | Connect corpus, document, section, table, row, figure, claim, and extracted field. |
| NORM07 | What conflicting definitions need separation? | Keep alternative definitions, scopes, or metric formulas separate instead of merging them. |
| NORM08 | What missing values need explicit labels? | Use unknown, unavailable, not applicable, not found, or blocked rather than blank ambiguity. |
| NORM09 | What normalized index should be produced? | Create lookup tables, source catalogs, claim maps, or scenario indexes for retrieval. |
| NORM10 | What normalization QA check is required? | Check schema completeness, duplicate IDs, unit consistency, category drift, and sort order. |

## Triangulation

| Code | Evidence question | Workflow use |
|---|---|---|
| TRIANG01 | Which claims need more than one source? | Require multiple sources for high-impact, disputed, recent, or uncertain claims. |
| TRIANG02 | Which sources independently confirm each other? | Avoid counting copies, reposts, or citations of the same original as independent evidence. |
| TRIANG03 | Which evidence confirms the same fact from different angles? | Combine official docs, observed data, expert analysis, examples, and user-provided artifacts. |
| TRIANG04 | Which evidence only supports part of a claim? | Split broad claims into supported and unsupported subclaims. |
| TRIANG05 | Which evidence contradicts the expected answer? | Include counterevidence rather than suppressing inconvenient sources. |
| TRIANG06 | Which evidence is correlated but not causal? | Avoid overclaiming causation from trends, anecdotes, or single observations. |
| TRIANG07 | Which evidence depends on assumptions? | Record assumptions, scenario boundaries, estimation methods, and sensitivity factors. |
| TRIANG08 | Which evidence should be weighted higher? | Weight primary, recent, official, complete, reproducible, and domain-authoritative sources. |
| TRIANG09 | What triangulation summary should be produced? | State confirmed, partially confirmed, contradicted, unknown, and not checked claims. |
| TRIANG10 | What triangulation QA check is required? | Verify independence, source diversity, claim coverage, and confidence labels. |

## Conflict Resolution

| Code | Evidence question | Workflow use |
|---|---|---|
| CONFLICT01 | What facts conflict across sources? | Identify mismatched dates, numbers, definitions, prices, specs, requirements, or statuses. |
| CONFLICT02 | Is the conflict caused by version differences? | Separate old versus new releases, draft versus final, region variants, or historical changes. |
| CONFLICT03 | Is the conflict caused by scope differences? | Compare geography, audience, unit, product variant, sample, legal context, or methodology. |
| CONFLICT04 | Is the conflict caused by source quality differences? | Prefer primary, complete, official, and current evidence when appropriate. |
| CONFLICT05 | Is the conflict unresolved? | Mark unresolved rather than forcing a false reconciliation. |
| CONFLICT06 | What decision rule resolves the conflict? | Apply recency, authority, exact scope, user-provided source priority, or documented hierarchy. |
| CONFLICT07 | What claim should be narrowed? | Rewrite broad claims into precise, source-supported statements. |
| CONFLICT08 | What additional source would resolve the conflict? | Identify missing primary document, dataset, SME review, vendor confirmation, or test result. |
| CONFLICT09 | What conflict note should be shown? | Explain material conflicts, chosen interpretation, and residual uncertainty. |
| CONFLICT10 | What conflict log should be preserved? | Record conflicting sources, values, decision rule, chosen value, and unresolved items. |

## Citation And Provenance

| Code | Evidence question | Workflow use |
|---|---|---|
| CITEPROV01 | Which output claims need citations? | Cite facts, numbers, quotes, legal claims, technical specs, comparisons, and source-derived judgments. |
| CITEPROV02 | What citation format is required? | Use links, footnotes, source IDs, bibliography, evidence table, or inline file references. |
| CITEPROV03 | What source snippet is needed for verification? | Keep short compliant excerpts, line references, table row IDs, or page numbers. |
| CITEPROV04 | What provenance must follow transformed data? | Preserve source ID, extraction method, transform rule, timestamp, and reviewer status. |
| CITEPROV05 | What citations must avoid overquoting? | Respect copyright, quote limits, lyrics limits, and source-specific reuse rules. |
| CITEPROV06 | What citation granularity is needed? | Cite document, page, section, paragraph, table row, dataset field, or commit. |
| CITEPROV07 | What local file links should be used? | Reference absolute local paths and line numbers for workspace files. |
| CITEPROV08 | What web source links should be included? | Provide direct source URLs and distinguish source facts from inference. |
| CITEPROV09 | What uncited claims should be removed or labeled? | Delete unsupported claims or label them as inference, assumption, or recommendation. |
| CITEPROV10 | What provenance QA check is required? | Verify every material claim has a valid source or explicit uncertainty label. |

## Evidence Pack

| Code | Evidence question | Workflow use |
|---|---|---|
| EVIDPACK01 | What final evidence packet is required? | Choose source list, claim table, appendix, manifest, audit pack, dataset, or annotated bibliography. |
| EVIDPACK02 | What evidence packet must be human-readable? | Provide concise summaries, claim support, confidence, gaps, and source links. |
| EVIDPACK03 | What evidence packet must be machine-readable? | Provide structured JSON, CSV, index rows, manifests, schemas, or reproducible queries. |
| EVIDPACK04 | What evidence should be attached to each workflow step? | Link intake facts, decisions, outputs, QA checks, and approvals to source evidence. |
| EVIDPACK05 | What evidence proves source coverage? | Include categories searched, sources collected, gaps, exclusions, and stop rule. |
| EVIDPACK06 | What evidence proves source quality? | Include authority, recency, license, confidence, conflicts, and verification notes. |
| EVIDPACK07 | What evidence proves extraction accuracy? | Include samples, row counts, parser logs, OCR checks, and review notes. |
| EVIDPACK08 | What evidence proves final-answer traceability? | Map final claims to source IDs and extracted fields. |
| EVIDPACK09 | What evidence pack should be archived for reuse? | Store reusable source catalog, prompt examples, standards references, and refresh instructions. |
| EVIDPACK10 | What evidence pack QA check is required? | Confirm completeness, readability, machine validity, citations, and unresolved gaps. |

## Refresh And Drift

| Code | Evidence question | Workflow use |
|---|---|---|
| REFRESH01 | Which evidence is likely to become stale? | Flag prices, specs, schedules, APIs, laws, rankings, availability, and people/company facts. |
| REFRESH02 | What refresh trigger applies? | Refresh on time interval, release, policy change, market event, user request, source update, or failed validation. |
| REFRESH03 | What source should be checked first on refresh? | Revisit primary source, official feed, connected app, local index, or authoritative dataset. |
| REFRESH04 | What cached evidence can still be reused? | Preserve evergreen definitions, historical facts, stable examples, and prior extraction schemas. |
| REFRESH05 | What evidence should be invalidated? | Mark outdated, contradicted, superseded, inaccessible, or low-confidence evidence. |
| REFRESH06 | What change detection method is needed? | Compare version numbers, timestamps, hashes, release notes, row counts, or monitored fields. |
| REFRESH07 | What refresh delta should be reported? | Summarize new, changed, removed, unchanged, and unresolved evidence. |
| REFRESH08 | What downstream artifacts need refresh? | Update indexes, prompts, templates, reports, workflows, dashboards, and validation packets. |
| REFRESH09 | What refresh record should be kept? | Store refresh date, sources checked, changes found, actions taken, and remaining risks. |
| REFRESH10 | What refresh QA check is required? | Verify updated citations, source coverage, stale-claim removal, and version consistency. |
