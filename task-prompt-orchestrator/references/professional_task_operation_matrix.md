# Professional Task Operation Matrix

Use this when the user's intent is best described by an action verb: analyze, generate, edit, summarize, extract, classify, compare, translate, plan, evaluate, diagnose, or decide. This matrix helps turn natural-language requests into precise prompt operations before domain-specific routing.

Selection rule:

1. Identify the main operation the user asks for.
2. Select one operation code below and combine it with P-code, input material, audience, constraint, lifecycle, risk, and domain codes.
3. Put the row's operation pattern into `Procedure`, `Output format`, and `Done when`.
4. If several operations are needed, order them as extract -> analyze -> generate/edit -> evaluate -> finalize.

## ANL Analyze / Interpret

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| ANL01 | Root-cause analysis | Symptom -> evidence -> hypotheses -> tests -> cause | RCA brief | Cause evidence-linked |
| ANL02 | Trend analysis | Data/time -> pattern -> drivers -> implications | Trend memo | Period and baseline |
| ANL03 | Stakeholder analysis | Actors -> interests -> influence -> risks -> actions | Stakeholder map | Role distinctions |
| ANL04 | Risk analysis | Asset/goal -> risks -> likelihood/impact -> mitigations | Risk register | Mitigation owners |
| ANL05 | Gap analysis | Current -> target -> gaps -> priorities -> plan | Gap report | Gaps actionable |
| ANL06 | Impact analysis | Change -> affected groups -> costs/benefits -> risks | Impact memo | Assumptions visible |
| ANL07 | Sentiment/theme analysis | Text -> themes -> sentiment -> evidence -> actions | Theme report | Quotes/samples |
| ANL08 | Financial analysis | Inputs -> metrics -> drivers -> variance -> outlook | Finance analysis | Formula trace |
| ANL09 | Technical analysis | System/artifact -> constraints -> issues -> options | Technical note | Edge cases |
| ANL10 | Policy/claim analysis | Claim/rule -> source -> interpretation -> caveats | Analysis brief | Source basis |

## GEN Generate / Create

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| GEN01 | First draft generation | Brief -> outline -> draft -> self-check | Draft artifact | Matches brief |
| GEN02 | Prompt generation | Goal -> variables -> prompt -> negative/QA checks | Prompt packet | Reusable variables |
| GEN03 | Creative concept generation | Audience -> insight -> routes -> rationale | Concept routes | Distinct options |
| GEN04 | Copy generation | Audience -> promise -> proof -> CTA -> variants | Copy set | Claim-safe |
| GEN05 | Visual brief generation | Subject -> composition -> style -> constraints | Visual prompt/brief | Visual specifics |
| GEN06 | Code generation | Requirement -> pattern -> implementation -> tests | Code change | Existing style |
| GEN07 | Data artifact generation | Source -> transform -> chart/table -> insight | Data artifact | Logic validated |
| GEN08 | Template generation | Use case -> variables -> instructions -> example | Template | Fillable fields |
| GEN09 | Question generation | Objective -> difficulty -> items -> answers | Question set | Answers provided |
| GEN10 | Variant generation | Base -> dimensions -> variants -> selection criteria | Variant pack | Variables isolated |

## EDT Edit / Rewrite / Improve

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| EDT01 | Clarity rewrite | Source -> audience -> structure -> rewrite -> compare | Clear rewrite | Meaning preserved |
| EDT02 | Tone adjustment | Source -> target tone -> examples -> rewrite | Tone-adjusted copy | Tone fits audience |
| EDT03 | Concision edit | Source -> key points -> remove redundancy -> final | Concise version | No lost requirements |
| EDT04 | Expansion edit | Source -> gaps -> evidence -> expanded sections | Expanded draft | New claims supported |
| EDT05 | Style-guide edit | Source -> rules -> corrections -> rationale | Style-compliant draft | Rules cited |
| EDT06 | Localization edit | Source -> locale -> cultural fit -> glossary | Localized rewrite | Meaning retained |
| EDT07 | Technical edit | Source -> terminology -> precision -> caveats | Technical polish | Terms accurate |
| EDT08 | Compliance edit | Source -> risky claims -> safer wording -> review | Compliant draft | Risk reduced |
| EDT09 | Structural edit | Source -> outline -> reorder -> transitions | Reorganized draft | Flow improved |
| EDT10 | Final proofread | Artifact -> spelling -> formatting -> consistency | Proofed final | No obvious defects |

## SUM Summarize / Condense

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| SUM01 | Executive summary | Source -> decision points -> risks -> next ask | Executive summary | Skimmable |
| SUM02 | Bullet summary | Source -> main points -> actions -> caveats | Bullet summary | Prioritized |
| SUM03 | Meeting summary | Notes -> decisions -> actions -> owners | Meeting recap | Owner/date |
| SUM04 | Research summary | Sources -> findings -> limits -> implications | Research summary | Citations/scope |
| SUM05 | Technical summary | Artifact -> architecture -> changes -> risks | Technical summary | Accurate details |
| SUM06 | Legal/policy summary | Document -> obligations -> risks -> questions | Plain summary | Not legal advice |
| SUM07 | Customer feedback summary | Feedback -> themes -> examples -> opportunities | Feedback summary | Sample caveat |
| SUM08 | Long document compression | Document -> sections -> key claims -> appendix | Condensed brief | No critical omission |
| SUM09 | Timeline summary | Events -> dates -> actors -> open issues | Timeline | Dates clear |
| SUM10 | Multi-source synthesis | Sources -> themes -> contradictions -> conclusion | Synthesis brief | Source boundaries |

## EXT Extract / Parse

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| EXT01 | Entity extraction | Source -> entity types -> fields -> confidence | Entity table | Confidence flags |
| EXT02 | Requirement extraction | Source -> must/should -> acceptance -> owner | Requirement list | No missed musts |
| EXT03 | Action item extraction | Source -> tasks -> owner -> due date -> dependency | Action list | Owner/date |
| EXT04 | Claim extraction | Source -> claims -> evidence need -> risk | Claim list | Verbatim trace |
| EXT05 | Metric extraction | Source -> metrics -> definition -> period -> source | Metric table | Units/period |
| EXT06 | Clause extraction | Contract -> clauses -> obligations -> deadlines | Clause table | Clause refs |
| EXT07 | Field extraction | Form/doc -> fields -> values -> uncertainty | Extracted fields | Low confidence marked |
| EXT08 | Quote extraction | Source -> quote -> speaker/page/time -> context | Quote bank | Attributed |
| EXT09 | Error/log extraction | Logs -> errors -> timestamps -> context | Error table | Timezone |
| EXT10 | Asset extraction | Folder/page -> assets -> metadata -> rights | Asset inventory | Rights status |

## CLS Classify / Tag / Route

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| CLS01 | Ticket classification | Ticket -> category -> severity -> route -> SLA | Triage table | Rules explicit |
| CLS02 | Content taxonomy | Corpus -> categories -> labels -> examples | Taxonomy | Mutually exclusive where needed |
| CLS03 | Risk classification | Item -> risk type -> severity -> control | Risk labels | Severity rationale |
| CLS04 | Lead/account scoring | Account -> criteria -> score -> next action | Lead score table | Criteria transparent |
| CLS05 | Feedback tagging | Feedback -> themes -> sentiment -> product area | Tagged feedback | Examples retained |
| CLS06 | Document classification | Document -> type -> sensitivity -> retention | Document register | Privacy tags |
| CLS07 | Defect classification | Defect -> type -> severity -> root area | Defect taxonomy | Actionable categories |
| CLS08 | Prompt routing | User ask -> P-code -> subcode -> matrices | Routing decision | Codes justified |
| CLS09 | Data quality classification | Issue -> dimension -> severity -> owner | DQ issue table | Owner assigned |
| CLS10 | Support escalation classification | Case -> severity -> owner -> response path | Escalation route | SLA fit |

## CMP Compare / Benchmark

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| CMP01 | Option comparison | Options -> criteria -> scoring -> recommendation | Option matrix | Criteria weighted |
| CMP02 | Competitor comparison | Competitors -> dimensions -> evidence -> gaps | Competitor matrix | Comparable basis |
| CMP03 | Version comparison | Versions -> changes -> impacts -> decisions | Change summary | Material changes |
| CMP04 | Vendor comparison | Vendors -> requirements -> price/risk -> recommendation | Vendor matrix | Evidence requested |
| CMP05 | Product comparison | Products -> features -> fit -> tradeoffs | Product comparison | User needs tied |
| CMP06 | Method comparison | Methods -> assumptions -> limits -> fit | Method matrix | Use-case fit |
| CMP07 | Policy comparison | Rules -> scope -> obligations -> conflicts | Policy comparison | Jurisdiction/version |
| CMP08 | Benchmark comparison | Baseline -> benchmark -> gaps -> actions | Benchmark report | Same metrics |
| CMP09 | Before/after comparison | Before -> after -> dimensions -> result | Before/after report | Same measurement |
| CMP10 | Scenario comparison | Scenarios -> assumptions -> outcomes -> triggers | Scenario matrix | Assumptions clear |

## TRN Translate / Localize

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| TRN01 | Direct translation | Source -> target language -> terminology -> QA | Translation | Meaning preserved |
| TRN02 | Professional localization | Source -> locale -> cultural fit -> glossary | Localized version | Locale natural |
| TRN03 | Technical translation | Source -> domain terms -> units -> diagrams refs | Technical translation | Terms consistent |
| TRN04 | Legal/policy translation | Source -> legal terms -> caveats -> review | Legal translation draft | Review gate |
| TRN05 | Marketing transcreation | Intent -> local idiom -> variants -> rationale | Transcreation options | Persuasion preserved |
| TRN06 | Subtitle translation | Source -> timing -> line length -> tone | Subtitle file/script | Timing readable |
| TRN07 | UI string localization | Strings -> length -> placeholders -> plurals | UI localization | Placeholders intact |
| TRN08 | Glossary building | Corpus -> terms -> definitions -> approved translations | Glossary | Consistent |
| TRN09 | Translation QA | Source/target -> errors -> severity -> fixes | QA report | Issues categorized |
| TRN10 | Bilingual rewrite | Source -> two versions -> alignment -> notes | Bilingual output | Versions aligned |

## PLN Plan / Organize

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| OPL01 | Project plan | Goal -> tasks -> owners -> dates -> risks | Project plan | Accountable |
| OPL02 | Research plan | Question -> sources -> method -> timeline | Research plan | Reproducible |
| OPL03 | Content plan | Audience -> pillars -> formats -> calendar | Content plan | Cadence realistic |
| OPL04 | Learning plan | Goal -> topics -> drills -> review cadence | Study plan | Spaced review |
| OPL05 | Launch plan | Audience -> channels -> assets -> dates -> metrics | Launch plan | Owners/dates |
| OPL06 | Experiment plan | Hypothesis -> design -> metrics -> guardrails | Experiment plan | Measurable |
| OPL07 | Migration plan | Current -> target -> phases -> rollback | Migration plan | Compatibility |
| OPL08 | Meeting/workshop plan | Outcome -> agenda -> activities -> outputs | Facilitation plan | Timeboxed |
| OPL09 | Risk response plan | Risks -> triggers -> mitigations -> owners | Risk plan | Triggers |
| OPL10 | Automation plan | Trigger -> steps -> exceptions -> monitoring | Automation plan | Failure path |

## EVA Evaluate / Review / Score

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| EVA01 | Quality evaluation | Artifact -> criteria -> score -> fixes | Evaluation report | Criteria explicit |
| EVA02 | Rubric scoring | Submission -> rubric -> evidence -> score | Scored rubric | Evidence tied |
| EVA03 | Proposal evaluation | Requirements -> response -> score -> risks | Proposal scorecard | Requirement coverage |
| EVA04 | Candidate evaluation | Evidence -> scorecard -> risks -> decision | Candidate memo | Job-related |
| EVA05 | Model evaluation | Predictions -> labels -> metrics -> errors | Model eval | Baseline |
| EVA06 | Prompt evaluation | Outputs -> criteria -> failure modes -> revisions | Prompt eval | Test cases |
| EVA07 | Usability evaluation | Flow -> tasks -> friction -> severity -> fixes | UX evaluation | User evidence |
| EVA08 | Compliance evaluation | Artifact -> rules -> gaps -> remediation | Compliance eval | Rule refs |
| EVA09 | Vendor evaluation | Vendor -> criteria -> evidence -> recommendation | Vendor scorecard | Comparable |
| EVA10 | Investment evaluation | Thesis -> evidence -> risks -> scenarios | Investment evaluation | Balanced |

## DIA Diagnose / Troubleshoot

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| DIA01 | Bug diagnosis | Symptom -> reproduce -> logs -> cause -> fix | Bug diagnosis | Repro |
| DIA02 | Metric drop diagnosis | Metric -> segments -> timeline -> hypotheses | Metric diagnosis | Driver evidence |
| DIA03 | Campaign diagnosis | Goal -> actual -> funnel -> creative/channel fixes | Campaign diagnosis | One variable isolated |
| DIA04 | Process failure diagnosis | Intended -> actual -> failure point -> countermeasure | Process diagnosis | Root cause |
| DIA05 | Data issue diagnosis | Source -> pipeline -> discrepancy -> resolution | Data issue report | Reconciliation |
| DIA06 | Customer issue diagnosis | Customer context -> symptoms -> cause -> save path | Customer diagnosis | Impact noted |
| DIA07 | Performance diagnosis | Baseline -> bottleneck -> test -> fix options | Performance diagnosis | Benchmark |
| DIA08 | Security incident diagnosis | Alert -> scope -> indicators -> containment | Security diagnosis | Authorization |
| DIA09 | Learning gap diagnosis | Output -> misconception -> remediation | Learning diagnosis | Next drill |
| DIA10 | Prompt failure diagnosis | Expected -> actual -> failure mode -> revised test | Prompt diagnosis | Failure isolated |

## DEC Decide / Recommend

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| DEC01 | Recommendation memo | Context -> options -> criteria -> recommendation | Decision memo | Clear rationale |
| DEC02 | Prioritization | Items -> criteria -> scoring -> shortlist | Priority list | Criteria visible |
| DEC03 | Go/no-go decision | Evidence -> risks -> gates -> decision -> conditions | Go/no-go brief | Conditions clear |
| DEC04 | Build/buy/partner | Capability -> options -> costs/risks -> recommendation | Build/buy memo | Tradeoffs |
| DEC05 | Roadmap decision | Goals -> options -> impact -> sequencing | Roadmap decision | Dependencies |
| DEC06 | Hiring decision | Evidence -> scorecard -> risks -> decision | Hiring decision memo | Fairness |
| DEC07 | Vendor decision | Requirements -> vendor matrix -> risks -> recommendation | Vendor decision | Comparable |
| DEC08 | Investment decision | Thesis -> scenarios -> risks -> recommendation | Investment decision brief | No personal advice |
| DEC09 | Policy decision | Options -> stakeholders -> impacts -> recommendation | Policy decision memo | Tradeoffs |
| DEC10 | Stop/continue decision | Progress -> cost -> signals -> recommendation | Stop/continue brief | Stop criteria |
