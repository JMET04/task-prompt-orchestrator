# Professional Workflow Knowledge Asset and Index Governance Matrix

Use this when a workflow should preserve reusable knowledge, prompts, templates, examples, sources, decisions, evaluations, indexes, or learning artifacts. Knowledge asset governance rules define how to capture, name, tag, index, version, deduplicate, validate, archive, retrieve, refresh, and retire reusable workflow knowledge.

Selection rule:

1. Identify the knowledge object: prompt, workflow, template, source, example, decision, metric, runbook, dataset, asset, or lesson.
2. Select the closest governance code.
3. Add asset type, owner, path/index entry, provenance, tags, version, quality gate, retention, and refresh rule to the prompt packet.
4. Do not treat knowledge as reusable until it is findable, versioned, and has an acceptance boundary.

## CAPK Capture Knowledge

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| CAPK01 | Prompt capture | Save prompt that solved a repeatable task | Include variables and constraints | Prompt record |
| CAPK02 | Workflow capture | Save reusable phase/gate pattern | Include trigger and acceptance criteria | Workflow record |
| CAPK03 | Template capture | Save reusable output structure | Separate fixed text from variables | Template record |
| CAPK04 | Example capture | Save representative input/output | Remove sensitive details | Example record |
| CAPK05 | Source capture | Save authoritative source reference | Include date, authority, relevance | Source record |
| CAPK06 | Decision capture | Save decision and rationale | Include owner and evidence | Decision record |
| CAPK07 | Failure capture | Save recurring failure and fix | Include detection and prevention | Failure record |
| CAPK08 | Metric capture | Save metric definition/threshold | Include denominator and cadence | Metric record |
| CAPK09 | Runbook capture | Save repeatable operating steps | Include exception handling | Runbook record |
| CAPK10 | Lesson capture | Save useful lesson from execution | Include when to reuse | Lesson record |

## NAMEK Naming / Identity

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| NAMEK01 | Stable ID | Asset needs durable identifier | Assign unique code or slug | Asset ID |
| NAMEK02 | Human-readable title | Asset needs recognizable title | Use concise task/domain title | Title field |
| NAMEK03 | File naming | File path must be predictable | Use domain-purpose-version naming | File path |
| NAMEK04 | Code prefix | Matrix/code family needs prefix | Use distinct uppercase prefix | Prefix record |
| NAMEK05 | Version suffix | Multiple versions exist | Add version/date/status | Version name |
| NAMEK06 | Locale name | Asset differs by language/region | Include locale code | Locale field |
| NAMEK07 | Domain name | Asset belongs to professional domain | Include domain/category tag | Domain tag |
| NAMEK08 | Lifecycle name | Asset belongs to stage | Include intake/draft/QA/archive state | State tag |
| NAMEK09 | Deprecated name | Asset should not be reused blindly | Mark deprecated/superseded | Deprecation label |
| NAMEK10 | Naming repair | Existing names are inconsistent | Rename or alias with redirect note | Rename log |

## TAGK Tagging / Taxonomy

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| TAGK01 | Domain tag | Need route by industry/function | Apply domain taxonomy | Domain tags |
| TAGK02 | Workflow tag | Need route by process type | Apply workflow dimension/code tags | Workflow tags |
| TAGK03 | Operation tag | Need route by action verb | Apply analyze/generate/edit/etc. | Operation tags |
| TAGK04 | Input tag | Need route by material type | Apply text/file/data/image/code/etc. | Input tags |
| TAGK05 | Output tag | Need route by deliverable type | Apply doc/deck/image/CAD/report/etc. | Output tags |
| TAGK06 | Audience tag | Need route by user/reviewer | Apply audience/context tag | Audience tags |
| TAGK07 | Risk tag | Need route by high-risk domain | Apply legal/medical/security/etc. | Risk tags |
| TAGK08 | Maturity tag | Need route by readiness level | Apply draft/tested/production/deprecated | Maturity tags |
| TAGK09 | Tool tag | Need route by required tool/model/API | Apply tool and environment tags | Tool tags |
| TAGK10 | Tag cleanup | Tags drift or multiply | Merge synonyms and remove dead tags | Tag cleanup |

## INDEXK Indexing

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| INDEXK01 | Prompt index entry | Prompt must be findable | Add category, use case, variables, path | Prompt index row |
| INDEXK02 | Workflow index entry | Workflow matrix/code must be findable | Add layer, code count, route, path | Workflow index row |
| INDEXK03 | Scenario index entry | Scenario needs lookup path | Add scenario, trigger phrase, deliverable | Scenario index row |
| INDEXK04 | Source index entry | Source must be reused safely | Add title, date, authority, status | Source index row |
| INDEXK05 | Template index entry | Template must be discoverable | Add purpose, variables, output format | Template index row |
| INDEXK06 | Example index entry | Example must support selection | Add representative use case and caveats | Example index row |
| INDEXK07 | Decision index entry | Decision must be retrievable | Add topic, owner, date, rationale | Decision index row |
| INDEXK08 | Failure index entry | Known failure must be searchable | Add symptom, cause, fix, prevention | Failure index row |
| INDEXK09 | Asset index entry | File/media/code asset needs lookup | Add path, type, owner, status | Asset index row |
| INDEXK10 | Index audit | Index may be incomplete | Compare files/assets against index rows | Index audit |

## PROVK Provenance / Lineage

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| PROVK01 | Source provenance | Asset depends on sources | Record source IDs and dates | Source lineage |
| PROVK02 | Prompt provenance | Output depends on prompt | Record prompt version and variables | Prompt lineage |
| PROVK03 | Tool provenance | Asset depends on tool/model/script | Record tool version/config | Tool lineage |
| PROVK04 | Human provenance | Asset depends on human review/approval | Record reviewer/approver | Human lineage |
| PROVK05 | Data provenance | Asset depends on data transform | Record dataset, transform, grain | Data lineage |
| PROVK06 | File provenance | Asset derived from files | Record input paths and output path | File lineage |
| PROVK07 | Decision provenance | Asset follows prior decision | Link decision record | Decision lineage |
| PROVK08 | Version provenance | Asset supersedes earlier version | Link predecessor and reason | Version lineage |
| PROVK09 | Rights provenance | Asset has usage/license boundary | Record license, owner, attribution | Rights lineage |
| PROVK10 | Provenance repair | Lineage is missing or unclear | Reconstruct or downgrade trust | Provenance note |

## VERK Versioning

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| VERK01 | Draft version | Asset not ready for production | Mark draft and owner | Draft label |
| VERK02 | Reviewed version | Asset passed review | Mark reviewer and date | Review version |
| VERK03 | Production version | Asset approved for reuse | Mark stable/current | Production label |
| VERK04 | Experimental version | Asset under trial | Mark experiment hypothesis and metric | Experiment version |
| VERK05 | Forked version | Asset adapted for new domain | Record fork reason and parent | Fork record |
| VERK06 | Superseded version | New version replaces old | Mark redirect to current | Superseded note |
| VERK07 | Archived version | Asset no longer active but retained | Mark archive path and retention | Archive version |
| VERK08 | Rollback version | Need known-good fallback | Mark rollback candidate | Rollback label |
| VERK09 | Version comparison | Need know what changed | Save diff/change summary | Version diff |
| VERK10 | Version policy | Versioning is inconsistent | Define status labels and promotion gates | Version policy |

## DEDK Deduplication / Consolidation

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| DEDK01 | Exact duplicate asset | Same content exists twice | Keep canonical and redirect duplicate | Dedup record |
| DEDK02 | Near duplicate asset | Similar assets overlap | Merge or clarify boundaries | Similarity decision |
| DEDK03 | Duplicate prompt | Prompts solve same task | Consolidate variables and examples | Prompt merge |
| DEDK04 | Duplicate workflow | Workflows differ only superficially | Merge or assign separate triggers | Workflow merge |
| DEDK05 | Duplicate tag | Tags are synonyms | Pick canonical tag and alias | Tag merge |
| DEDK06 | Duplicate source | Same source referenced multiple ways | Normalize source ID | Source merge |
| DEDK07 | Duplicate example | Examples teach same case | Keep best representative | Example merge |
| DEDK08 | Conflicting duplicate | Duplicates disagree | Preserve both until conflict resolved | Conflict record |
| DEDK09 | Consolidation batch | Many assets need cleanup | Process by manifest and audit trail | Consolidation log |
| DEDK10 | No-merge exception | Similar assets must remain separate | Record boundary and rationale | No-merge note |

## QUALK Knowledge Quality

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| QUALK01 | Accuracy check | Knowledge may be wrong | Verify against source or test | Accuracy check |
| QUALK02 | Completeness check | Asset may omit required fields | Validate required metadata | Completeness check |
| QUALK03 | Usability check | Asset may be hard to apply | Test on representative task | Usability check |
| QUALK04 | Freshness check | Knowledge may be stale | Check date/version/currency | Freshness check |
| QUALK05 | Safety check | Asset may cause risky output | Add high-risk boundary | Safety check |
| QUALK06 | Rights check | Asset may violate license/IP | Verify usage rights | Rights check |
| QUALK07 | Privacy check | Asset may expose sensitive data | Redact or restrict | Privacy check |
| QUALK08 | Reproducibility check | Asset may not produce same result | Add inputs, steps, expected output | Repro check |
| QUALK09 | Coverage check | Library may miss scenario categories | Compare against taxonomy | Coverage check |
| QUALK10 | Quality signoff | Asset ready for reuse | Record reviewer and acceptance | Quality signoff |

## RETK Retrieval / Search

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| RETK01 | Keyword retrieval | User searches by words | Add common phrases and aliases | Keyword index |
| RETK02 | Code retrieval | User searches by code | Ensure code appears in index/path | Code lookup |
| RETK03 | Scenario retrieval | User searches by situation | Map trigger phrase to asset | Scenario lookup |
| RETK04 | Domain retrieval | User searches by industry | Link domain tag to assets | Domain lookup |
| RETK05 | Deliverable retrieval | User searches by output form | Link deliverable tag to assets | Deliverable lookup |
| RETK06 | Similarity retrieval | Need find related assets | Add related links or embeddings note | Related assets |
| RETK07 | Faceted retrieval | Need filter by multiple axes | Support domain/type/risk/status fields | Facet fields |
| RETK08 | Retrieval test | Need prove findability | Search for expected phrases/codes | Search test |
| RETK09 | Missed retrieval | Asset exists but cannot be found | Add alias/tag/index row | Retrieval fix |
| RETK10 | Retrieval deprecation | Search result points to old asset | Redirect to current asset | Retrieval redirect |

## REFRESHK Refresh / Maintenance

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| REFRESHK01 | Scheduled refresh | Asset needs periodic review | Set daily/weekly/monthly/quarterly cadence | Refresh schedule |
| REFRESHK02 | Event refresh | Source/tool/policy changed | Refresh affected assets | Event refresh |
| REFRESHK03 | Usage refresh | High-use asset needs improvement | Review based on usage threshold | Usage refresh |
| REFRESHK04 | Failure refresh | Asset caused repeated failure | Patch asset and add prevention | Failure refresh |
| REFRESHK05 | Drift refresh | Output behavior changed | Revalidate against examples | Drift refresh |
| REFRESHK06 | Taxonomy refresh | Categories no longer fit | Update tags/index hierarchy | Taxonomy refresh |
| REFRESHK07 | Owner refresh | Owner/reviewer is stale | Reassign stewardship | Owner refresh |
| REFRESHK08 | Example refresh | Examples no longer representative | Add/replace examples | Example refresh |
| REFRESHK09 | Prompt refresh | Prompt quality declines | Benchmark and revise | Prompt refresh |
| REFRESHK10 | Refresh closeout | Maintenance completed | Record changes and next review | Refresh log |

## ACCESSK Access / Permissions

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| ACCESSK01 | Public asset | Asset safe for broad reuse | Mark public and rights status | Public label |
| ACCESSK02 | Internal asset | Asset for internal use only | Restrict and mark boundary | Internal label |
| ACCESSK03 | Confidential asset | Asset contains sensitive info | Restrict access and redact summaries | Confidential label |
| ACCESSK04 | Regulated asset | Asset includes legal/medical/financial risk | Require domain gate | Regulated label |
| ACCESSK05 | Client asset | Asset belongs to external/client context | Record client boundary | Client label |
| ACCESSK06 | Licensed asset | Asset has license terms | Record license and attribution | License record |
| ACCESSK07 | Expiring access | Access should be temporary | Set expiry/review date | Expiry record |
| ACCESSK08 | Access review | Permissions may drift | Audit access vs need-to-know | Access audit |
| ACCESSK09 | Access incident | Improper exposure suspected | Contain, record, and remediate | Access incident |
| ACCESSK10 | Access handoff | Stewardship changes | Transfer permissions and ownership | Access handoff |

## RETIREK Retirement / Pruning

| Code | Governance need | Capture rule | Control | Evidence |
|---|---|---|---|---|
| RETIREK01 | Low-use retirement | Asset unused for long period | Archive or remove after review | Retirement note |
| RETIREK02 | Stale retirement | Asset cannot be refreshed | Deprecate and point to current alternative | Stale note |
| RETIREK03 | Unsafe retirement | Asset creates risk | Remove from active routing | Safety retirement |
| RETIREK04 | Duplicate retirement | Asset replaced by canonical version | Redirect and archive duplicate | Duplicate retirement |
| RETIREK05 | Tool retirement | Asset depends on unsupported tool | Migrate or archive | Tool retirement |
| RETIREK06 | Domain retirement | Domain category no longer used | Merge or archive category | Domain retirement |
| RETIREK07 | Prompt retirement | Prompt underperforms newer version | Deprecate with reason | Prompt retirement |
| RETIREK08 | Index retirement | Index row points to removed asset | Remove or redirect row | Index cleanup |
| RETIREK09 | Archive retention | Retired asset still needed for audit | Store with retention rule | Retention record |
| RETIREK10 | Retirement closeout | Pruning completed | Verify search no longer routes incorrectly | Retirement proof |
