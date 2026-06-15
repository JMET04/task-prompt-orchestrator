# Professional Workflow Input Output Contract Matrix

Use this when a workflow step needs explicit input requirements, output schemas, interface boundaries, transformation rules, or handoff compatibility. IO contracts prevent broken chains where one step's output cannot be used by the next step.

Selection rule:

1. Identify the workflow step's required inputs and expected outputs.
2. Select one or more IO contract codes.
3. Add source, schema, validation, output shape, and handoff receiver to the prompt packet.
4. If required inputs are missing or outputs cannot be validated, route to clarification, source readiness, or QA state.

## INPC Input Contract Types

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| INPC01 | Goal input | User goal, deliverable, constraints | Structured execution brief | Goal is testable |
| INPC02 | Source input | File/link/text/image/data source and context | Source inventory | Source accessible |
| INPC03 | Parameter input | Variables, thresholds, options, units | Parameter table | Defaults explicit |
| INPC04 | Preference input | Style, tone, format, depth, audience | Preference profile | Preference applied |
| INPC05 | Criteria input | Rubric, acceptance criteria, pass/fail rule | Criteria map | Criteria observable |
| INPC06 | Prior-state input | Existing artifact, log, plan, or status | Current-state note | State verified |
| INPC07 | Tool input | Tool name, path, credentials/permission status, parameters | Tool-ready payload | Tool available or fallback |
| INPC08 | Batch input | Item list, operation, naming, exception rule | Batch manifest | All items listed |
| INPC09 | Sensitive input | Data class, minimization rule, redaction need | Safe input package | Sensitive data handled |
| INPC10 | Unknown input | Missing input and impact | Clarification or assumption note | Missingness disclosed |

## OUTC Output Contract Types

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| OUTC01 | Narrative output | Brief, audience, structure | Written answer/document section | Matches audience |
| OUTC02 | Structured table output | Fields, row grain, sorting | Markdown/CSV/table artifact | Required columns present |
| OUTC03 | Prompt packet output | Goal, variables, constraints, checks | Reusable prompt packet | Variables reusable |
| OUTC04 | Code output | Files, change goal, tests | Patch/code diff and verification | Tests or caveats |
| OUTC05 | Visual prompt output | Source invariants, target changes, specs | Image2/design prompt | Invariants preserved |
| OUTC06 | Report output | Findings, evidence, recommendations | Report or memo | Evidence linked |
| OUTC07 | Plan output | Steps, owners, dependencies, gates | Execution plan | Steps actionable |
| OUTC08 | QA output | Artifact, criteria, results | QA report/checklist | Pass/fail explicit |
| OUTC09 | Decision output | Options, criteria, recommendation | Decision memo/table | Rationale explicit |
| OUTC10 | Handoff output | Current state, artifacts, risks, next action | Handoff packet | Receiver can continue |

## SCHC Schema / Format Contracts

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| SCHC01 | Fixed schema | Required fields and field types | Exact schema output | Schema validates |
| SCHC02 | Flexible schema | Required core fields plus optional fields | Structured but adaptable output | Core fields present |
| SCHC03 | File format | Target file type, encoding, extension | Correct file format | Opens/parses correctly |
| SCHC04 | Markdown contract | Heading levels, tables, code blocks | Markdown artifact | Renders cleanly |
| SCHC05 | JSON/YAML contract | Keys, nesting, arrays, types | Valid JSON/YAML | Parser passes |
| SCHC06 | Spreadsheet contract | Sheets, columns, formulas, grain | Workbook/table-ready output | Columns and formulas valid |
| SCHC07 | Slide/deck contract | Slide list, layout, speaker notes | Deck outline or file | Slide count/spec met |
| SCHC08 | Design spec contract | Dimensions, units, colors, assets | Design/CAD/image spec | Specs complete |
| SCHC09 | API/tool payload contract | Endpoint/tool, params, response fields | Valid payload | Tool accepts payload |
| SCHC10 | Index entry contract | Category, code, title, tags, path | Searchable index row | Index fields complete |

## TRNC Transformation Contracts

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| TRNC01 | Summarize | Source and audience | Condensed summary | Meaning preserved |
| TRNC02 | Expand | Seed content and scope | Expanded artifact | No unsupported claims |
| TRNC03 | Rewrite | Source, target tone, constraints | Rewritten content | Meaning preserved |
| TRNC04 | Translate/localize | Source language, target locale | Localized output | Locale fit checked |
| TRNC05 | Extract | Source and fields | Extracted data/table | Fields traceable |
| TRNC06 | Classify | Items and taxonomy | Labeled items | Labels consistent |
| TRNC07 | Normalize | Raw data/content and target standard | Normalized artifact | Units/terms consistent |
| TRNC08 | Compare | Items and criteria | Comparison matrix | Same basis |
| TRNC09 | Convert format | Source format and target format | Converted artifact | Target usable |
| TRNC10 | Synthesize | Multiple sources and question | Integrated answer/report | Sources reconciled |

## HANDC Handoff Interface Contracts

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| HANDC01 | Step-to-step handoff | Previous output and next input needs | Compatible step packet | Next step can start |
| HANDC02 | Agent-to-user handoff | Result, files, limits, next action | User-facing summary | User can act |
| HANDC03 | User-to-agent handoff | Goal, sources, constraints | Agent-ready brief | Agent can execute |
| HANDC04 | Agent-to-agent handoff | State, evidence, pending work | Resume packet | New agent can continue |
| HANDC05 | Human review handoff | Artifact and criteria | Review request packet | Reviewer can decide |
| HANDC06 | Approval handoff | Artifact, evidence, risks, options | Approval packet | Approver can sign/reject |
| HANDC07 | Developer handoff | Files, changes, tests, risks | Engineering handoff | Developer can resume |
| HANDC08 | Designer handoff | Assets, specs, variants, constraints | Design handoff | Production specs clear |
| HANDC09 | Ops handoff | Runbook, thresholds, owners | Operations packet | Ops can run process |
| HANDC10 | Archive handoff | Final artifacts, source, version, tags | Archive/index packet | Artifact findable |

## DEPC Dependency Contracts

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| DEPC01 | Upstream dependency | Required upstream artifact and owner | Dependency note | Upstream exists |
| DEPC02 | Downstream dependency | Receiver, expected input, timing | Downstream handoff | Receiver needs met |
| DEPC03 | Tool dependency | Tool, version, access, fallback | Tool dependency note | Tool works or fallback |
| DEPC04 | Data dependency | Dataset/source, freshness, owner | Data dependency note | Data current enough |
| DEPC05 | Approval dependency | Approver, criteria, deadline | Approval dependency note | Approval status known |
| DEPC06 | Human dependency | Person/role, expected contribution | Human dependency note | Owner named |
| DEPC07 | External dependency | Vendor, partner, API, legal, or market event | External dependency note | Status tracked |
| DEPC08 | Sequence dependency | Must-do-before relation | Sequence map | Order enforced |
| DEPC09 | Parallel dependency | Independent lanes and merge rule | Merge contract | Merge rule clear |
| DEPC10 | Missing dependency | Unknown or absent dependency | Blocker/fallback note | Gap disclosed |

## QUALC Quality Interface Contracts

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| QUALC01 | Completeness interface | Scope and required sections | Complete artifact | No required section missing |
| QUALC02 | Accuracy interface | Claims and evidence | Evidence-backed artifact | Claims traceable |
| QUALC03 | Consistency interface | Terms, numbers, decisions | Consistent artifact set | Conflicts resolved |
| QUALC04 | Usability interface | Target task and user | Actionable output | User task supported |
| QUALC05 | Readability interface | Audience and reading level | Clear output | Tone/level fit |
| QUALC06 | Visual fidelity interface | Source image/spec and constraints | Visual prompt/spec/output | Visual facts preserved |
| QUALC07 | Technical correctness interface | Code/spec/architecture and tests | Technically valid output | Tests or review pass |
| QUALC08 | Data correctness interface | Grain, metric, formula, sample | Valid analysis/table | Math/grain checked |
| QUALC09 | Compliance interface | Rule, jurisdiction, evidence | Compliant or caveated output | Risk gate passed |
| QUALC10 | Production readiness interface | Specs, owner, QA, handoff | Release-ready package | Final readiness checked |

## ERRC Error / Fallback Contracts

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| ERRC01 | Missing input fallback | Missing field and impact | Assumption or blocker note | Missingness visible |
| ERRC02 | Invalid input fallback | Bad format/schema/source | Repair request or normalized input | Input repaired |
| ERRC03 | Tool failure fallback | Failed command/tool and error | Alternate path or failure report | Failure captured |
| ERRC04 | Source conflict fallback | Conflicting facts/sources | Conflict map and resolution | Conflict handled |
| ERRC05 | Low confidence fallback | Uncertain extraction/analysis | Caveated output | Confidence marked |
| ERRC06 | Partial output fallback | Incomplete run or limited access | Partial artifact and next step | Limits disclosed |
| ERRC07 | QA failure fallback | Failed criteria | Rework plan | Failure actionable |
| ERRC08 | Approval rejection fallback | Rejection reason | Revision path | Reason addressed |
| ERRC09 | Dependency unavailable fallback | Missing external dependency | Alternative or blocked note | Dependency status known |
| ERRC10 | Recovery output | Exception and fix path | Recovery report | Workflow can resume |

## SECC Security / Privacy IO Contracts

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| SECC01 | Data minimization | Needed fields and purpose | Minimal input package | Extra data excluded |
| SECC02 | Redaction | Sensitive fields and redaction rule | Redacted artifact | Sensitive fields removed |
| SECC03 | Access boundary | Who can see/use artifact | Access note | Audience appropriate |
| SECC04 | Secret handling | Secret/token indicators | Safe handling note | Secrets not exposed |
| SECC05 | Privacy purpose | Personal data and purpose | Privacy handling note | Purpose stated |
| SECC06 | Retention rule | Keep/delete duration | Retention note | Retention clear |
| SECC07 | Regulated output boundary | Rule and audience | Caveated/approved output | Gate applied |
| SECC08 | Abuse-risk boundary | Potential misuse mode | Safe output variant | Unsafe detail avoided |
| SECC09 | External sharing boundary | External recipient and asset class | Sharing approval note | Rights/access checked |
| SECC10 | Audit evidence boundary | Evidence needed without overexposure | Minimal audit packet | Evidence sufficient |

## VERC Version / Change Contracts

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| VERC01 | Versioned input | Version/date/source status | Version note | Version identified |
| VERC02 | Versioned output | Output version and change summary | Versioned artifact | Version visible |
| VERC03 | Diff contract | Old and new artifact | Change summary/diff | Changes traceable |
| VERC04 | Migration contract | Source version, target version | Migration output | Migration verified |
| VERC05 | Update contract | Existing artifact and update request | Updated artifact | Old intent preserved |
| VERC06 | Rollback contract | Current state and prior state | Rollback plan/output | Rollback possible |
| VERC07 | Changelog contract | Changes, reason, impact | Changelog entry | Impact stated |
| VERC08 | Compatibility contract | Upstream/downstream consumers | Compatible output | Consumers unaffected |
| VERC09 | Deprecation contract | Retired artifact/rule and replacement | Deprecation note | Replacement clear |
| VERC10 | Snapshot contract | Artifacts, date, source, status | Snapshot record | Snapshot reproducible |

## METC Metrics / Observability Contracts

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| METC01 | Progress metric | Step list and completion rule | Progress status | Percent/status meaningful |
| METC02 | Quality metric | Score/rubric and threshold | Quality score | Threshold applied |
| METC03 | Time metric | Start/end/deadline/SLA | Timing status | Time basis clear |
| METC04 | Cost metric | Budget/resource unit | Cost status | Cost basis clear |
| METC05 | Coverage metric | Category list and scope | Coverage report | Gaps visible |
| METC06 | Error metric | Error class and count | Error summary | Errors categorized |
| METC07 | Throughput metric | Item count and time window | Throughput note | Window stated |
| METC08 | Freshness metric | Source date and freshness rule | Freshness status | Staleness known |
| METC09 | Adoption metric | Usage/users/actions | Adoption report | Denominator stated |
| METC10 | Outcome metric | Desired result and measurement | Outcome report | Outcome measurable |

## REUSC Reuse / Template Contracts

| Code | Contract | Input requirements | Output requirement | Validation |
|---|---|---|---|---|
| REUSC01 | Prompt template IO | Variables, defaults, examples | Reusable prompt template | Variables complete |
| REUSC02 | Workflow template IO | Trigger, steps, artifacts, checks | Workflow template | Reusable across cases |
| REUSC03 | Checklist template IO | Criteria and pass/fail rules | Checklist template | Criteria observable |
| REUSC04 | Report template IO | Sections, data slots, evidence slots | Report template | Slots clear |
| REUSC05 | Design prompt template IO | Subject, style, specs, negatives | Visual prompt template | Invariants encoded |
| REUSC06 | CAD/production template IO | Dimensions, materials, views, callouts | Production prompt/spec template | Specs reusable |
| REUSC07 | Research template IO | Question, source rules, citation format | Research workflow template | Search reproducible |
| REUSC08 | Review template IO | Artifact, criteria, severity, evidence | Review template | Findings structured |
| REUSC09 | Automation template IO | Trigger, inputs, runbook, logs | Automation template | Failure path included |
| REUSC10 | Index template IO | Category, tags, code, path, summary | Index entry template | Searchable entry |
