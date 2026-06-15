# Professional Workflow Scale and Batch Matrix

Use this when a workflow must handle many items, repeated runs, high-volume production, bulk prompt generation, multi-file processing, large queues, distributed work, or cost-sensitive automation. Scale and batch rules define how to intake volume, split work, process in batches, sample quality, control throughput, track costs, and preserve consistency.

Selection rule:

1. Identify whether the scaling problem is volume, item diversity, concurrency, cost, tool limits, quality risk, or repeated production.
2. Select the closest scale code.
3. Add item schema, batch rule, queue rule, QA sampling, capacity limit, retry handling, and reporting to the prompt packet.
4. Do not scale a workflow until a representative sample passes and failure handling is defined.

## VOLINT Volume Intake

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| VOLINT01 | Item manifest | Many files/tasks/items must be processed | Create canonical manifest with stable IDs | Manifest |
| VOLINT02 | Item schema | Items differ in fields or inputs | Define required and optional item fields | Item schema |
| VOLINT03 | Volume estimate | Total count or size is unknown | Count items, bytes, tokens, pages, or records | Volume count |
| VOLINT04 | Priority class | Items have different urgency/value/risk | Assign priority tier before processing | Priority field |
| VOLINT05 | Risk class | Some items need stricter handling | Label high-risk items for separate lane | Risk field |
| VOLINT06 | Duplicate scan | Repeated items may waste work | Detect and merge duplicates | Dedup report |
| VOLINT07 | Missing-input scan | Some items lack required data | Move incomplete items to exception list | Input gap list |
| VOLINT08 | Source grouping | Items come from multiple sources | Group by source, owner, or authority | Source grouping |
| VOLINT09 | Consent/access check | Bulk work may include restricted items | Verify access and usage rights | Access check |
| VOLINT10 | Intake freeze | Processing needs stable item set | Lock manifest version before run | Frozen manifest |

## BATCH Batch Planning

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| BATCH01 | Batch size | Need choose how many items per run | Set batch size by risk, cost, and tool limit | Batch rule |
| BATCH02 | Batch window | Processing must happen in time windows | Define start/end window and cutoff | Batch window |
| BATCH03 | Pilot batch | Full run is risky | Run small representative batch first | Pilot result |
| BATCH04 | Stratified batch | Items differ by category or risk | Include each important segment | Stratified sample |
| BATCH05 | Rolling batch | Work should proceed continuously | Process next batch after gate passes | Rolling log |
| BATCH06 | Manual batch | Human review limits speed | Bundle items for reviewer capacity | Review batch |
| BATCH07 | Automated batch | Tool can process many items | Use scripted or template-driven batch run | Automation batch |
| BATCH08 | Exception batch | Failed items require separate handling | Move failures to recovery batch | Exception batch |
| BATCH09 | Rework batch | Corrections must be applied across items | Identify affected batch and rerun | Rework log |
| BATCH10 | Batch closeout | Need prove batch completion | Record processed, failed, skipped, accepted counts | Batch summary |

## CHUNK Work Chunking

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| CHUNK01 | File chunking | File is too large for one pass | Split by pages, sections, sheets, or records | Chunk map |
| CHUNK02 | Token chunking | Text exceeds context or model limit | Split by token-safe segments | Token chunks |
| CHUNK03 | Semantic chunking | Meaning must stay intact | Split by topic, heading, object, or scene | Semantic map |
| CHUNK04 | Time chunking | Audio/video/logs are long | Split by timestamp windows | Time segments |
| CHUNK05 | Image region chunking | Visual artifact has many regions/details | Split by view, panel, layer, or callout | Region map |
| CHUNK06 | Data partitioning | Dataset is too large or grouped | Partition by date, entity, shard, or sample | Partition spec |
| CHUNK07 | Dependency chunking | Some chunks depend on others | Preserve prerequisite order | Dependency map |
| CHUNK08 | Merge chunking | Chunks must recombine cleanly | Define merge keys and conflict rule | Merge plan |
| CHUNK09 | Overlap chunking | Boundary context may be lost | Add overlap and deduplicate after merge | Overlap note |
| CHUNK10 | Chunk QA | Need verify each chunk before merge | Apply per-chunk acceptance check | Chunk QA |

## PARLANE Parallel Lanes

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| PARLANE01 | Independent lanes | Workstreams can run in parallel | Split by independent item groups | Lane map |
| PARLANE02 | Role lanes | Different roles handle different steps | Assign lanes by owner/reviewer/operator | Role lane |
| PARLANE03 | Tool lanes | Different tools process different item types | Route items by tool fit | Tool lane |
| PARLANE04 | Domain lanes | Categories need domain-specific prompts | Route by domain adaptation code | Domain lane |
| PARLANE05 | Risk lanes | High-risk items need stricter review | Separate high-risk processing | Risk lane |
| PARLANE06 | Language lanes | Locale/language variants differ | Route by locale and glossary | Locale lane |
| PARLANE07 | Creative lanes | Variants need divergent concept directions | Assign lanes by concept route | Creative lane |
| PARLANE08 | QA lanes | Review can run separately from production | Create QA queue independent of production | QA lane |
| PARLANE09 | Merge lane | Parallel results must be reconciled | Assign merge owner and conflict rule | Merge lane |
| PARLANE10 | Lane shutdown | A lane becomes invalid or blocked | Pause lane without stopping all work | Lane status |

## THROT Throughput Control

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| THROT01 | Rate limit | API/tool/user capacity has limit | Set max requests/items per window | Rate log |
| THROT02 | Concurrency limit | Too many simultaneous jobs cause failure | Set worker/job cap | Concurrency log |
| THROT03 | Cost throttle | Spend grows with volume | Set cost cap per run/day/item | Cost cap |
| THROT04 | Review throttle | Human review queue backs up | Limit production to review capacity | Review cap |
| THROT05 | Error throttle | Error rate rises during run | Pause or slow when threshold breached | Error throttle |
| THROT06 | Priority throttle | Critical items must pass before low-value items | Reserve capacity for priority tier | Priority capacity |
| THROT07 | Freshness throttle | New data arrives faster than processing | Define cutoff and refresh window | Freshness window |
| THROT08 | Output throttle | Downstream system cannot consume fast enough | Match output rate to receiver capacity | Output rate |
| THROT09 | Notification throttle | Too many updates overwhelm audience | Batch or summarize updates | Notice cadence |
| THROT10 | Safety throttle | Risky category should scale slowly | Require staged expansion gates | Safety gate |

## SAMPLE QA Sampling

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| SAMPLE01 | Random sample QA | Need broad quality signal | Review random sample from batch | Random QA |
| SAMPLE02 | Stratified QA | Categories differ materially | Sample each segment | Stratified QA |
| SAMPLE03 | High-risk QA | Risky items need full or heavier review | Oversample high-risk items | Risk QA |
| SAMPLE04 | Boundary QA | Edge cases likely fail | Sample smallest/largest/newest/oldest cases | Boundary QA |
| SAMPLE05 | Golden-set QA | Known expected outputs exist | Compare against golden examples | Golden QA |
| SAMPLE06 | Reviewer calibration | Multiple reviewers may disagree | Calibrate on shared sample | Calibration log |
| SAMPLE07 | Drift sample | Quality may change over time | Sample early, middle, late outputs | Drift QA |
| SAMPLE08 | Failure sample | Failed/skipped items need diagnosis | Sample exceptions by failure reason | Failure QA |
| SAMPLE09 | Acceptance sample | Client/user needs proof before full delivery | Share representative acceptance sample | Acceptance sample |
| SAMPLE10 | Sample escalation | Sample fails threshold | Stop batch and move to recovery | Sample failure |

## DEDUPE Deduplication / Idempotency

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| DEDUPE01 | Exact duplicate | Identical items appear repeatedly | Process once and reference duplicates | Exact dedup |
| DEDUPE02 | Near duplicate | Similar items differ slightly | Cluster and decide merge/separate rule | Similarity log |
| DEDUPE03 | Version duplicate | Multiple versions of same artifact exist | Select authoritative version | Version decision |
| DEDUPE04 | Request duplicate | Same request enters multiple channels | Merge tickets and preserve audit | Request merge |
| DEDUPE05 | Output duplicate | Batch creates repeated outputs | Reuse output or vary by rule | Output dedup |
| DEDUPE06 | Retry idempotency | Retry may duplicate side effects | Use stable IDs and no-op repeated writes | Idempotency log |
| DEDUPE07 | Payment/cost duplicate | Paid operation may run twice | Confirm charge/run uniqueness | Cost dedup |
| DEDUPE08 | Notification duplicate | Audience may receive repeated messages | Suppress duplicate notifications | Notice dedup |
| DEDUPE09 | Archive duplicate | Stored artifacts duplicate prior archive | Link to existing archive or version | Archive dedup |
| DEDUPE10 | Dedup exception | Similar items must stay separate | Mark no-merge reason | Dedup exception |

## VARIANT Variant Production

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| VARIANT01 | Audience variants | Output differs by audience/persona | Define audience-specific deltas | Audience variant |
| VARIANT02 | Channel variants | Output differs by platform/channel | Apply channel specs | Channel variant |
| VARIANT03 | Locale variants | Output differs by language/region | Use locale glossary and cultural checks | Locale variant |
| VARIANT04 | Format variants | Same content needs multiple formats | Define source-of-truth and export rules | Format variant |
| VARIANT05 | Creative variants | Need multiple creative directions | Define concept axes and constraints | Creative set |
| VARIANT06 | Test variants | Need A/B or multivariate tests | Define variable, hypothesis, metric | Test matrix |
| VARIANT07 | Risk variants | Conservative and aggressive options needed | Label assumptions and risk tradeoff | Risk variant |
| VARIANT08 | Personalization variants | Output tailored to item/user attributes | Use allowed personalization fields only | Personalization map |
| VARIANT09 | Tier variants | Output differs by service/package level | Define tier entitlement and exclusions | Tier map |
| VARIANT10 | Variant governance | Many variants need approval control | Track owner, status, and approval per variant | Variant register |

## PIPE Pipeline Orchestration

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| PIPE01 | Multi-step pipeline | Each item goes through repeated stages | Define stage order and artifact handoff | Pipeline map |
| PIPE02 | Stage gate | Item must pass before next stage | Add pass/fail rule per stage | Gate log |
| PIPE03 | Pipeline queue | Items wait between stages | Track stage queue and owner | Stage queue |
| PIPE04 | Pipeline retry | Stage failure needs bounded retry | Retry stage without duplicating prior stages | Stage retry |
| PIPE05 | Pipeline rollback | Later stage invalidates earlier output | Define rollback by stage | Stage rollback |
| PIPE06 | Pipeline observability | Need see where items are | Record state, timestamp, owner, result | Pipeline dashboard |
| PIPE07 | Pipeline template | Repeated pipeline should be reusable | Save parameterized pipeline template | Pipeline template |
| PIPE08 | Pipeline branch | Item type changes stage path | Route by branch criteria | Branch log |
| PIPE09 | Pipeline merge | Multiple stages/lane outputs recombine | Merge by stable key and conflict rule | Merge log |
| PIPE10 | Pipeline closeout | Need prove all items reached terminal state | Report done/failed/skipped/blocked counts | Pipeline closeout |

## AUTOS Automation at Scale

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| AUTOS01 | Template automation | Repeated prompt/output can be templated | Parameterize prompt and output schema | Template run |
| AUTOS02 | Script automation | Manual repetition is error-prone | Use script/job where deterministic | Script log |
| AUTOS03 | Connector automation | External system must push/pull items | Define API/connector contract | Connector log |
| AUTOS04 | Scheduler automation | Work recurs on cadence | Define schedule, window, and owner | Schedule record |
| AUTOS05 | Event automation | Work starts from trigger/event | Define event schema and debounce rule | Event log |
| AUTOS06 | Human gate automation | Automation needs review before action | Insert approval or sampling gate | Gate record |
| AUTOS07 | Exception automation | Failed items need automatic routing | Send failures to exception queue | Exception route |
| AUTOS08 | Audit automation | Need trace every automated decision/output | Store inputs, config, version, output | Audit trail |
| AUTOS09 | Stop automation | Unsafe condition should halt run | Define kill switch and threshold | Stop event |
| AUTOS10 | Automation handoff | Automation output needs human continuation | Generate handoff packet per run | Handoff bundle |

## OBSVOL Volume Observability

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| OBSVOL01 | Count tracking | Need know processed/remaining counts | Track counts by state | Count report |
| OBSVOL02 | Throughput tracking | Need rate over time | Track items per hour/day/run | Throughput metric |
| OBSVOL03 | Error tracking | Need failure pattern visibility | Track errors by type, stage, item class | Error report |
| OBSVOL04 | Quality tracking | Need quality trend across volume | Track QA pass rate and defect types | Quality metric |
| OBSVOL05 | Cost tracking | Need spend per item/run | Track unit and total cost | Cost report |
| OBSVOL06 | Latency tracking | Need time per item/stage | Track cycle time and wait time | Latency report |
| OBSVOL07 | Reviewer tracking | Need human bottleneck visibility | Track review queue and turnaround | Review metric |
| OBSVOL08 | Drift tracking | Need detect output/source/prompt drift | Compare samples across time/batches | Drift report |
| OBSVOL09 | Coverage tracking | Need know which segments are covered | Track segment completion | Coverage matrix |
| OBSVOL10 | Executive tracking | Need concise scale status | Summarize volume, risk, cost, blockers | Exec scale report |

## COSTVOL Scale Cost Control

| Code | Scale need | Setup | Control | Evidence |
|---|---|---|---|---|
| COSTVOL01 | Unit cost estimate | Need know cost per item | Estimate token/API/tool/human cost | Unit cost |
| COSTVOL02 | Budget cap | Total spend must stay under ceiling | Stop or ask approval at cap | Budget cap |
| COSTVOL03 | Cost tiering | Not all items deserve same depth | Route by value/risk tier | Cost tier |
| COSTVOL04 | Sample-before-full | Full run is expensive | Run sample and estimate total | Cost sample |
| COSTVOL05 | Cache reuse | Repeated inputs can reuse outputs | Cache stable intermediate results | Cache hit log |
| COSTVOL06 | Cheap-first pass | Low-cost screen can reduce full work | Filter items before expensive step | Screening log |
| COSTVOL07 | Human-cost control | Review time is scarce/expensive | Reserve human review for triggers | Review budget |
| COSTVOL08 | Rework-cost control | Bad batch would be expensive to fix | Add early QA gate | Rework guard |
| COSTVOL09 | Cost anomaly | Spend exceeds expected rate | Pause and diagnose cost driver | Cost alert |
| COSTVOL10 | Cost closeout | Need report actual scale economics | Compare estimated vs actual cost | Cost closeout |
