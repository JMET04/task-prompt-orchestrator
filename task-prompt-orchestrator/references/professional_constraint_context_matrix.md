# Professional Constraint and Context Matrix

Use this when the user's request is shaped by execution constraints: urgency, budget, quality bar, language, platform, output format, evidence availability, collaboration mode, confidentiality, accessibility, geography, or technical environment.

Selection rule:

1. Select the normal P-code plus any input, industry, deliverable, audience, risk, deep-domain, and lifecycle codes first.
2. Select one or more constraint/context codes here.
3. Add the row's constraint handling to `Constraints`, `Procedure`, and `Quality checks`.
4. If constraints conflict, state the tradeoff and choose the path that preserves safety, evidence, and user value.

## URG Urgency / Timebox

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| URG01 | Immediate answer | State assumptions -> give useful draft -> mark gaps -> next check | Rapid answer | Uncertainty visible |
| URG02 | 15-minute triage | Identify issue -> top risks -> next action -> defer deep work | Triage note | Priorities clear |
| URG03 | Same-day deliverable | Minimum viable scope -> execute -> verify core claims | Same-day draft | Scope boundary |
| URG04 | Deadline rescue | Inventory -> cut scope -> assign owners -> final gate | Rescue plan | Critical path |
| URG05 | Quick research | Best available sources -> confidence -> follow-up list | Quick brief | Freshness caveat |
| URG06 | Fast creative batch | Template -> variants -> shortlist -> repair one winner | Variant batch | Naming/criteria |
| URG07 | Rapid bug response | Repro/logs -> likely cause -> safe patch/rollback | Hotfix brief | Risk noted |
| URG08 | Emergency comms | Known facts -> holding statement -> next update time | Holding statement | No speculation |
| URG09 | Timeboxed learning | Objective -> one concept -> one drill -> feedback | Micro-lesson | Learner can act |
| URG10 | Deferred full analysis | Immediate output -> missing work -> schedule/dependencies | Deferred plan | Follow-up explicit |

## RES Budget / Resources

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| RES01 | No-budget option | Free tools -> manual steps -> limits -> next upgrade | Lean plan | Limits visible |
| RES02 | Low-budget production | Must-haves -> reuse assets -> simple process -> QA | Low-cost production plan | Quality floor |
| RES03 | Small team | Roles -> workload -> automation -> review gates | Small-team workflow | Owner clarity |
| RES04 | Solo operator | Prioritize -> templates -> checklists -> batching | Solo workflow | Sustainable cadence |
| RES05 | Enterprise resources | Teams -> governance -> scale -> dependencies | Enterprise plan | Coordination overhead |
| RES06 | Outsource/vendor path | Scope -> vendor brief -> acceptance -> handoff | Vendor brief | Acceptance criteria |
| RES07 | Tool-limited environment | Available tools -> workaround -> manual verification | Tool-constrained plan | Feasible steps |
| RES08 | Data-limited resources | Sparse data -> proxies -> caveats -> future collection | Sparse-data analysis | Caveats clear |
| RES09 | Compute-limited task | Smaller model/data -> sampling -> validation | Compute-light plan | Accuracy tradeoff |
| RES10 | Budget approval needed | Costs -> value -> risks -> options -> ask | Budget case | Assumptions stated |

## QLT Quality Bar / Rigor

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| QLT01 | Rough draft | Fast structure -> key points -> obvious gaps | Rough draft | Draft labeled |
| QLT02 | Professional draft | Complete structure -> evidence -> polish -> QA | Professional draft | Meets brief |
| QLT03 | Publication-ready | Fact check -> style -> rights -> final proof | Publication-ready artifact | Final gates |
| QLT04 | Audit-grade | Evidence -> traceability -> controls -> exceptions | Audit-grade pack | Source trace |
| QLT05 | Executive-ready | Summary -> decision -> evidence appendix | Executive-ready brief | Skimmable |
| QLT06 | Production-ready | Specs -> tolerances -> QA -> handoff | Production-ready spec | Review gate |
| QLT07 | Research-grade | Method -> sources -> limitations -> reproducibility | Research-grade output | Method transparent |
| QLT08 | Legal/compliance-grade | Clause/rule evidence -> caveats -> review status | Compliance-grade draft | Review boundary |
| QLT09 | Beginner-friendly | Plain language -> examples -> first action | Beginner output | Low jargon |
| QLT10 | Investor/board-grade | Metrics -> risks -> asks -> appendix | Board-grade pack | Concise and defensible |

## LAN Language / Locale / Tone

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| LAN01 | Chinese professional | Domain terms -> concise Chinese -> structure -> checks | Chinese professional output | Terms natural |
| LAN02 | English professional | Audience -> tone -> terminology -> polish | English professional output | Idiomatic |
| LAN03 | Bilingual output | Source -> parallel terms -> two versions -> consistency | Bilingual output | Meaning aligned |
| LAN04 | Plain-language rewrite | Complex text -> core meaning -> examples -> caveats | Plain-language version | Accuracy retained |
| LAN05 | Formal tone | Context -> respectful style -> precise wording | Formal communication | Tone appropriate |
| LAN06 | Conversational tone | Audience -> natural phrasing -> action clarity | Conversational copy | Not sloppy |
| LAN07 | Technical terminology | Glossary -> definitions -> usage consistency | Technical version | Terms defined |
| LAN08 | Local cultural fit | Locale -> norms -> sensitive terms -> alternatives | Localized version | Cultural risks reduced |
| LAN09 | Brand voice | Voice rules -> examples -> variants -> QA | Brand-voice output | Voice consistent |
| LAN10 | Sensitive tone | Situation -> empathy -> facts -> boundaries | Sensitive message | Respectful and clear |

## CHN Platform / Channel

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| CHN01 | Website | Audience -> sections -> SEO/accessibility -> CTA | Website content/spec | First viewport clear |
| CHN02 | Mobile app | User flow -> screens -> states -> constraints | App UX brief | Mobile ergonomics |
| CHN03 | Social platform | Platform norms -> format -> hook -> moderation | Social asset | Platform-native |
| CHN04 | Email | Recipient -> subject -> message -> CTA -> follow-up | Email draft | Clear ask |
| CHN05 | Marketplace | Platform rules -> title/media/copy -> compliance | Listing pack | Claims safe |
| CHN06 | Internal wiki | Taxonomy -> page structure -> links -> ownership | Wiki page | Findable |
| CHN07 | Chat/IM | Context -> concise response -> action -> owner | Chat message | Short and actionable |
| CHN08 | Presentation | Audience -> story -> slides -> notes -> handoff | Slide-ready content | Narrative |
| CHN09 | Print | Size -> bleed -> color -> readability -> production | Print brief | Production specs |
| CHN10 | API/tool interface | Inputs -> schema -> errors -> examples -> docs | API/tool spec | Machine-readable |

## OUT Output Format / Structure

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| OUT01 | Bullet summary | Extract -> prioritize -> bullets -> next actions | Bullet summary | No buried ask |
| OUT02 | Table/matrix | Dimensions -> rows -> columns -> scoring -> notes | Matrix/table | Comparable cells |
| OUT03 | Checklist | Goal -> checks -> pass/fail -> owner -> evidence | Checklist | Testable items |
| OUT04 | Step-by-step guide | Preconditions -> steps -> verification -> troubleshooting | Procedure guide | Reproducible |
| OUT05 | Memo format | Context -> analysis -> recommendation -> risks | Memo | Recommendation clear |
| OUT06 | JSON/schema | Fields -> types -> examples -> validation rules | JSON/schema output | Valid structure |
| OUT07 | Template | Variables -> instructions -> example -> quality checks | Reusable template | Variables clear |
| OUT08 | Script | Audience -> spoken flow -> cues -> timing | Script | Sounds natural |
| OUT09 | Report | Scope -> method -> findings -> recommendations | Report | Evidence-backed |
| OUT10 | Action plan | Goal -> tasks -> owners -> dates -> risks | Action plan | Accountable |

## AVA Evidence / Data Availability

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| AVA01 | Complete evidence | Verify -> synthesize -> cite -> conclude | Evidence-backed output | Citations complete |
| AVA02 | Partial evidence | Use available data -> label gaps -> propose next collection | Partial brief | Gaps explicit |
| AVA03 | No source material | State assumptions -> give framework -> ask for inputs | Framework draft | Assumptions visible |
| AVA04 | Conflicting evidence | Map claims -> compare authority -> confidence | Conflict matrix | Confidence levels |
| AVA05 | Stale evidence | Date boundary -> refresh path -> caveat output | Stale-source brief | Freshness warning |
| AVA06 | Proprietary evidence | Use provided docs only -> cite internal source labels | Source-limited answer | Scope limited |
| AVA07 | Anecdotal evidence | Separate anecdotes from patterns -> avoid overclaim | Anecdote synthesis | No broad claim |
| AVA08 | Quantitative evidence | Validate definitions -> compute -> caveat | Quant analysis | Denominators |
| AVA09 | Qualitative evidence | Code themes -> quotes -> saturation caveat | Qual report | Quotes traceable |
| AVA10 | Evidence handoff needed | Evidence table -> open questions -> review needs | Evidence pack | Reviewer-ready |

## COL Collaboration / Approval Mode

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| COL01 | Solo execution | Plan -> execute -> self-QA -> report | Solo work plan | Verification included |
| COL02 | Team collaboration | Roles -> handoffs -> review gates -> cadence | Team workflow | Owners clear |
| COL03 | Client collaboration | Scope -> drafts -> feedback cycles -> approvals | Client workflow | Expectations clear |
| COL04 | Expert review required | Draft -> questions -> evidence -> review packet | Review packet | Expert asks explicit |
| COL05 | Multi-stakeholder approval | Stakeholders -> criteria -> conflicts -> decision log | Approval plan | Decision rights |
| COL06 | Async collaboration | Artifact -> comments -> decisions -> next actions | Async workflow | Status visible |
| COL07 | Workshop mode | Objectives -> agenda -> exercises -> outputs | Workshop plan | Facilitator-ready |
| COL08 | Handoff to implementer | Context -> requirements -> assets -> tests -> risks | Handoff brief | Implementable |
| COL09 | Feedback incorporation | Feedback -> categorize -> accept/reject -> update | Revision log | Rationale |
| COL10 | Governance-heavy process | Controls -> signoffs -> records -> audit trail | Governance workflow | Records kept |

## CFT Confidentiality / Sensitivity

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| CFT01 | Public-safe output | Remove sensitive details -> generalize -> cite public facts | Public-safe version | No confidential info |
| CFT02 | Internal confidential | Label audience -> minimize sharing -> avoid external claims | Internal brief | Audience marked |
| CFT03 | Personal data present | Redact/minimize -> purpose limit -> handling note | Privacy-safe output | PII protected |
| CFT04 | Trade secret material | Abstract details -> protect know-how -> review gate | Trade-secret-safe brief | No unnecessary disclosure |
| CFT05 | Legal privileged context | Preserve facts -> avoid broad sharing -> counsel gate | Privilege-aware note | Privilege caveat |
| CFT06 | Security-sensitive details | Remove exploit/secrets -> defensive summary | Security-safe output | No secret leakage |
| CFT07 | HR-sensitive content | Minimize identities -> fairness -> documentation | HR-sensitive brief | Need-to-know |
| CFT08 | Health-sensitive content | De-identify -> supportive framing -> clinician gate | Health privacy brief | No diagnosis |
| CFT09 | Vendor/confidential NDA | Obligations -> allowed use -> redactions -> review | NDA-safe summary | Use limits |
| CFT10 | Anonymized case study | Remove identifiers -> combine details -> consent status | Anonymous case study | Re-identification risk |

## ACC Accessibility / Inclusion

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| ACC01 | Plain language need | Audience -> simplify -> examples -> glossary | Plain-language output | Readability |
| ACC02 | Screen reader accessibility | Structure -> headings -> alt text -> link text | Accessible content | Navigable |
| ACC03 | Visual accessibility | Contrast -> font size -> layout -> labels | Visual accessibility brief | Contrast/readability |
| ACC04 | Cognitive accessibility | Chunk -> step order -> reduce memory load | Cognitive-friendly guide | One action at a time |
| ACC05 | Multilingual inclusion | Locale -> glossary -> cultural fit -> alternatives | Inclusive localized copy | Terms respectful |
| ACC06 | Disability accommodation | Task -> barriers -> accommodations -> options | Accommodation-aware plan | Non-diagnostic |
| ACC07 | Inclusive examples | Audience -> representation -> bias check -> revise | Inclusive content | Avoid stereotypes |
| ACC08 | Mobile accessibility | Touch targets -> layout -> states -> text scaling | Mobile a11y brief | Responsive |
| ACC09 | Caption/transcript need | Media -> captions -> transcript -> speaker labels | Caption/transcript plan | Sync/labels |
| ACC10 | Accessible data visualization | Chart -> labels -> alt summary -> table backup | Accessible chart spec | Insight available |

## GEO Geography / Jurisdiction / Market

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| GEO01 | US context | Jurisdiction -> state/federal caveat -> local sources | US-context brief | Jurisdiction clear |
| GEO02 | China context | National/local context -> source hierarchy -> language fit | China-context brief | Local terms |
| GEO03 | EU context | EU/regional rules -> member-state caveat -> privacy focus | EU-context brief | GDPR awareness |
| GEO04 | Cross-border context | Countries -> conflicts -> localization -> review gates | Cross-border brief | Market differences |
| GEO05 | Local market analysis | Geography -> demand -> competitors -> channels | Local market scan | Local evidence |
| GEO06 | Import/export context | Origin/destination -> docs -> restrictions -> broker questions | Trade brief | Specialist review |
| GEO07 | Tax/legal location | Location -> rules -> professional review -> caveat | Location-specific note | No overclaim |
| GEO08 | Cultural adaptation | Locale -> norms -> risks -> alternatives | Cultural adaptation brief | Sensitive terms |
| GEO09 | Multi-region rollout | Regions -> sequencing -> localization -> constraints | Multi-region plan | Dependencies |
| GEO10 | Unknown location | State missing location -> generic framework -> ask/assume | Location-limited output | Boundary explicit |

## ENV Tooling / Technical Environment

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| ENV01 | Local Windows workspace | Inspect files -> use PowerShell -> verify outputs | Windows execution plan | Paths exact |
| ENV02 | Web/browser task | URL/page -> inspect -> test -> screenshot/evidence | Browser task plan | Repro evidence |
| ENV03 | API/tool integration | Tool capability -> schema -> call -> validate | Tool workflow | Schema respected |
| ENV04 | No network | Use local sources -> mark stale risk -> offline path | Offline plan | Source limits |
| ENV05 | Network required | Browse/source -> cite -> cache important facts | Online research plan | Sources linked |
| ENV06 | Restricted permissions | Read-only path -> safe actions -> ask/alternative | Permission-safe plan | No unsafe write |
| ENV07 | Large files | Sample/index -> targeted reads -> avoid full dumps | Large-file plan | Coverage rationale |
| ENV08 | Existing repo conventions | Inspect patterns -> minimal patch -> tests | Repo-aware plan | No unrelated churn |
| ENV09 | Plugin/skill available | Prefer specialized skill/tool -> fallback | Tool-assisted plan | Existing capability used |
| ENV10 | Output artifact hosting | Choose file/render/link -> validate accessibility | Delivery plan | User can open |
