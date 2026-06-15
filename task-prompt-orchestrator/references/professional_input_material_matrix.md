# Professional Input Material Matrix

Use this when the user's request depends on the kind of input material they provide or reference. Input type determines extraction, source handling, tooling, privacy, and verification before any professional workflow starts.

Selection rule:

1. Identify the primary input: text, PDF, spreadsheet, data, image, video, audio, web/link, codebase, design/CAD, communication records, or regulated document.
2. Select the closest input code below.
3. Add the row's extraction and verification checks to the prompt packet.
4. Combine it with the normal P-code, industry code, deliverable code, lifecycle stage, and risk gate.

## TXT Text / Notes / Drafts

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| TXT01 | Raw idea notes | Notes -> intent -> themes -> gaps -> structured brief | Structured brief | Assumptions separated |
| TXT02 | Long draft | Draft -> outline -> claims -> weak spots -> edit plan | Edit plan | Meaning preserved |
| TXT03 | Meeting notes | Notes -> decisions -> actions -> owners -> risks | Meeting summary | Actions owner/date |
| TXT04 | Transcript text | Transcript -> speakers -> themes -> quotes -> follow-ups | Transcript synthesis | Quotes traceable |
| TXT05 | Requirements notes | Notes -> actors -> requirements -> acceptance -> open questions | Requirements draft | Testable criteria |
| TXT06 | Brainstorm list | Ideas -> clusters -> criteria -> shortlist -> next tests | Prioritized idea list | Criteria explicit |
| TXT07 | User feedback text | Feedback -> pain themes -> evidence -> opportunities | Feedback report | Sample/context stated |
| TXT08 | Policy/procedure text | Text -> obligations -> exceptions -> owners -> controls | Policy/SOP summary | Requirements preserved |
| TXT09 | Prompt text | Prompt -> goal -> variables -> constraints -> tests | Improved prompt | Variables reusable |
| TXT10 | Mixed pasted text | Segment -> classify -> route -> extract -> synthesize | Parsed content map | Content boundaries clear |

## PDF Documents / Reports

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| PDF01 | PDF summary | Extract -> sections -> claims -> citations -> synthesis | PDF summary | Page refs when possible |
| PDF02 | Report audit | Extract -> findings -> evidence -> gaps -> recommendations | Report audit | Findings evidence-linked |
| PDF03 | Contract PDF | Clauses -> obligations -> risks -> questions | Contract issue table | Clause/page refs |
| PDF04 | Academic paper PDF | Abstract/method/results -> claims -> limitations -> relevance | Paper brief | Method/limits included |
| PDF05 | Scanned PDF/OCR | OCR -> quality check -> correction -> extraction | OCR extraction note | OCR uncertainty flagged |
| PDF06 | Multi-PDF comparison | Inventory -> normalize -> compare -> contradiction map | Comparison matrix | Same basis |
| PDF07 | Manual/spec PDF | Tasks/specs -> steps -> warnings -> parameters | Spec/manual extraction | Warnings preserved |
| PDF08 | RFP/tender PDF | Requirements -> deadlines -> compliance matrix -> risks | RFP matrix | Must-haves captured |
| PDF09 | Financial PDF | Tables -> metrics -> assumptions -> variance/issues | Financial extraction | Table math checked |
| PDF10 | Regulatory PDF | Authority -> effective date -> obligations -> evidence | Regulatory brief | Version/date cited |

## SHE Spreadsheet / Workbook Inputs

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INP-SHE01 | Workbook overview | Sheets -> columns -> formulas -> purpose -> issues | Workbook map | Hidden sheets noted |
| INP-SHE02 | Formula audit | Formula cells -> dependencies -> errors -> risks | Formula audit | Broken refs flagged |
| INP-SHE03 | Data cleaning | Columns -> types -> missing/duplicates -> cleaning plan | Clean data plan | No silent deletion |
| INP-SHE04 | KPI workbook | Metrics -> definitions -> source sheets -> caveats | KPI dictionary | Definitions explicit |
| INP-SHE05 | Budget workbook | Assumptions -> categories -> formulas -> scenarios | Budget review | Assumptions visible |
| INP-SHE06 | Survey workbook | Responses -> coding -> pivots -> insights | Survey analysis | Counts/segments shown |
| INP-SHE07 | Inventory workbook | SKU -> stock -> demand -> reorder -> exceptions | Inventory diagnosis | Units consistent |
| INP-SHE08 | CRM/pipeline sheet | Accounts -> stages -> values -> next actions | Pipeline review | Stage definitions |
| INP-SHE09 | Reconciliation workbook | Keys -> matches -> exceptions -> resolution | Reconciliation report | Exceptions traceable |
| INP-SHE10 | Dashboard source sheet | Tables -> chart-ready shape -> refresh -> filters | Dashboard data spec | Grain clear |

## DAT Dataset / Database / Logs

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INP-DAT01 | CSV/table dataset | Schema -> quality -> summary stats -> analysis plan | Data profile | Types and missingness |
| INP-DAT02 | SQL database | Tables -> relationships -> metric logic -> safe queries | Data map | Joins validated |
| INP-DAT03 | Application logs | Time range -> events -> errors -> correlation -> cause | Log analysis | Timestamps/timezone |
| INP-DAT04 | Analytics events | Events -> users/sessions -> funnels -> anomalies | Event analysis | Event definitions |
| INP-DAT05 | Survey dataset | Variables -> coding -> weighting -> insights | Survey report | Sample caveats |
| INP-DAT06 | Experiment data | Design -> arms -> metrics -> guardrails -> readout | Experiment readout | Assignment checked |
| INP-DAT07 | Time series | Frequency -> seasonality -> anomalies -> forecast | Time-series brief | Gaps handled |
| INP-DAT08 | Geospatial data | Coordinates -> projection -> regions -> map logic | Geo analysis brief | CRS/scale noted |
| INP-DAT09 | Sensitive dataset | Fields -> minimization -> redaction -> access controls | Data handling plan | PII protected |
| INP-DAT10 | Model output data | Predictions -> labels -> errors -> calibration -> fixes | Model eval report | Baseline compared |

## IMG Image / Screenshot / Scan

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INP-IMG01 | Product photo | Subject -> defects -> desired output -> edit/generation brief | Product image prompt | Product identity preserved |
| INP-IMG02 | Screenshot | UI/context -> visible text -> issue -> repro/analysis | Screenshot analysis | Visible evidence only |
| INP-IMG03 | Chart image | Extract axes -> values -> trend -> caveats | Chart summary | OCR uncertainty |
| INP-IMG04 | Document scan | OCR -> layout -> key fields -> verification | Extracted fields | Low-confidence fields flagged |
| INP-IMG05 | Packaging image | Structure -> panels -> material -> production prompt | Packaging prompt | Panel relationships |
| INP-IMG06 | CAD/technical image | Views -> lines -> dimensions -> callouts -> prompt | Technical drawing brief | No decorative drift |
| INP-IMG07 | Brand/design asset | Layout -> typography -> palette -> brand issues | Design critique | Specific visual evidence |
| INP-IMG08 | Before/after reference | Baseline -> target -> invariants -> edit prompt | Image2 edit brief | Same angle/scale |
| INP-IMG09 | Medical/safety image | Visible facts -> uncertainty -> professional boundary | Cautious observation | No diagnosis |
| INP-IMG10 | Multi-image set | Inventory -> group -> compare -> select/QA | Image set review | Naming and criteria |

## VID Video / Screen Recording

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INP-VID01 | Screen recording | Steps -> UI state -> error -> repro -> likely cause | Repro report | Timestamped events |
| INP-VID02 | Product video | Scenes -> product behavior -> claims -> edit brief | Product video analysis | Claims visible |
| INP-VID03 | Interview video | Speakers -> themes -> quotes -> moments | Interview highlights | Quotes contextualized |
| INP-VID04 | Tutorial video | Steps -> prerequisites -> missing steps -> summary | Tutorial extraction | Order preserved |
| INP-VID05 | Ad/creative video | Hook -> scenes -> message -> CTA -> issues | Creative audit | First seconds evaluated |
| INP-VID06 | Event recording | Agenda -> speakers -> decisions -> action items | Event summary | Speaker/time refs |
| INP-VID07 | User test recording | Tasks -> friction -> quotes -> severity -> fixes | Usability report | Evidence per issue |
| INP-VID08 | Safety/process video | Process -> hazards -> controls -> deviations | Safety/process review | Professional boundary |
| INP-VID09 | Video for localization | Source scenes -> speech/text -> cultural risks -> plan | Localization brief | Timing/culture noted |
| INP-VID10 | Raw footage batch | Clips -> selects -> sequence -> edit plan | Edit decision list | Clip IDs/timestamps |

## AUD Audio / Voice / Call

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INP-AUD01 | Sales call recording | Participants -> needs -> objections -> next steps | Call summary | No commitments invented |
| INP-AUD02 | Customer support call | Issue -> sentiment -> resolution -> follow-up | Support call report | Policy alignment |
| INP-AUD03 | Interview audio | Topics -> quotes -> themes -> insights | Interview synthesis | Quote timestamps |
| INP-AUD04 | Podcast/audio content | Segments -> main points -> clips -> show notes | Show notes | Names/claims checked |
| INP-AUD05 | Voiceover audio | Script match -> pacing -> clarity -> fixes | Voiceover QA | Timestamped notes |
| INP-AUD06 | Meeting audio | Agenda -> decisions -> actions -> risks | Meeting recap | Owners/dates |
| INP-AUD07 | Noisy audio | Quality -> intelligibility -> uncertain segments -> next step | Audio quality note | Unclear parts labeled |
| INP-AUD08 | Multilingual audio | Language -> translation -> cultural notes -> QA | Translation summary | Uncertain terms flagged |
| INP-AUD09 | Medical/legal call | Facts -> questions -> professional boundary -> next steps | Cautious call brief | No advice beyond scope |
| INP-AUD10 | Audio ad/music | Message/mood -> structure -> brand fit -> edits | Audio creative audit | Rights/claims checked |

## WEB Links / Pages / Online Sources

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INP-WEB01 | Single web page | Open -> extract claims -> summarize -> cite | Page summary | URL/date captured |
| INP-WEB02 | Multiple links | Inventory -> cluster -> compare -> synthesize | Link synthesis | Source boundaries |
| INP-WEB03 | Current facts | Browse -> source hierarchy -> date compare -> answer | Current brief | Freshness boundary |
| INP-WEB04 | Competitor pages | Pages -> features/pricing/copy -> matrix | Competitor web audit | Comparable dimensions |
| INP-WEB05 | Documentation site | Nav -> relevant docs -> examples -> task answer | Docs-based answer | Official docs preferred |
| INP-WEB06 | News sources | Articles -> event timeline -> source comparison | News timeline | Event vs publish date |
| INP-WEB07 | Product reviews | Reviews -> themes -> quotes -> opportunities | Review mining report | Sample size |
| INP-WEB08 | Web app/site audit | Pages -> UX/performance/accessibility -> fixes | Site audit | Repro steps |
| INP-WEB09 | Search result research | Query -> source selection -> evidence table -> synthesis | Research pack | Search terms noted |
| INP-WEB10 | Paywalled/limited access | Available text -> limitations -> alternative sources | Limited-source brief | Access limits explicit |

## COD Codebase / Repository / Diff

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INP-COD01 | Repo orientation | Files -> architecture -> entry points -> build/test | Repo map | Commands verified |
| INP-COD02 | Bug fix request | Repro -> code path -> patch -> tests | Bug fix | Tests or reason |
| INP-COD03 | Feature implementation | Requirements -> patterns -> changes -> verification | Implemented feature | Existing style followed |
| INP-COD04 | Code review diff | Diff -> behavior risks -> tests -> findings | Review findings | File/line evidence |
| INP-COD05 | Test failure | Failure -> logs -> suspected cause -> fix -> rerun | Test fix note | Failure reproduced |
| INP-COD06 | Security scan | Entry points -> findings -> exploitability -> fix | Security triage | Authorization boundary |
| INP-COD07 | Performance issue | Baseline -> bottleneck -> change -> benchmark | Perf plan/patch | Before/after metric |
| INP-COD08 | Migration/refactor | Current -> target -> steps -> compatibility -> tests | Migration plan | Rollback path |
| INP-COD09 | Docs generation | Code -> public API -> examples -> caveats | Developer docs | Runnable examples |
| INP-COD10 | Config/CI issue | Pipeline/config -> failure -> environment -> fix | CI/config fix | Secrets protected |

## DSG Design / CAD / Creative Files

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INP-DSG01 | Figma/design file | Screens -> components -> states -> implementation notes | Design analysis | Components/states |
| INP-DSG02 | CAD drawing | Views -> dimensions -> materials -> missing specs | CAD review | Engineering boundary |
| INP-DSG03 | Packaging dieline | Panels -> folds/cuts -> print zones -> risks | Dieline review | Fold/cut distinction |
| INP-DSG04 | Brand guideline | Rules -> tokens -> examples -> deviations | Brand rule summary | Rule references |
| INP-DSG05 | Logo/identity asset | Usage -> clearspace -> colors -> scalability | Identity QA | Misuse flagged |
| INP-DSG06 | Presentation design file | Slides -> narrative -> layout -> fixes | Deck design audit | Slide refs |
| INP-DSG07 | Architecture/interior plan | Zones -> circulation -> constraints -> issues | Space plan critique | Scale caveat |
| INP-DSG08 | 3D/model reference | Views -> geometry -> material -> render brief | 3D/render brief | Geometry preserved |
| INP-DSG09 | Print production file | Bleed -> color -> resolution -> fonts -> marks | Print preflight brief | Production risks |
| INP-DSG10 | Creative moodboard | References -> common traits -> direction -> gaps | Moodboard synthesis | Direction explicit |

## COM Communication Records

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INP-COM01 | Email thread | Parties -> timeline -> commitments -> open items | Thread summary | Commitments quoted |
| INP-COM02 | Chat log | Messages -> decisions -> blockers -> action items | Chat recap | Speaker context |
| INP-COM03 | Support ticket history | Issue -> attempts -> customer impact -> next step | Ticket summary | No missed context |
| INP-COM04 | Sales CRM notes | Account -> stakeholders -> pain -> stage -> next ask | Account brief | Evidence-backed |
| INP-COM05 | Interview notes | Questions -> answers -> themes -> quotes | Interview synthesis | Quotes traceable |
| INP-COM06 | Community comments | Themes -> sentiment -> moderation risks -> actions | Community report | Sample caveat |
| INP-COM07 | Complaint thread | Facts -> emotion -> resolution options -> response | Complaint response brief | Empathy and accuracy |
| INP-COM08 | Negotiation thread | Positions -> concessions -> risks -> next message | Negotiation brief | No invented authority |
| INP-COM09 | Incident comms | Timeline -> updates -> facts/unknowns -> comms gaps | Incident comms review | No speculation |
| INP-COM10 | Approval conversation | Decisions -> conditions -> owners -> evidence | Approval log | Audit trail |

## REG Regulated / Formal Documents

| Code | Scenario | Best workflow | Product | Checks |
|---|---|---|---|---|
| INP-REG01 | Contract/agreement | Clauses -> obligations -> risks -> questions | Contract review draft | Not legal advice |
| INP-REG02 | Policy/regulation | Authority -> scope -> obligations -> implementation | Obligation brief | Version/date |
| INP-REG03 | Standard/certification doc | Clauses -> evidence -> gaps -> action plan | Compliance map | Clause traceability |
| INP-REG04 | Medical/scientific record | Facts -> timeline -> questions -> clinician/review gate | Cautious summary | No diagnosis |
| INP-REG05 | Financial statement | Statements -> metrics -> trends -> questions | Financial review | Assumptions/caveats |
| INP-REG06 | Insurance policy | Coverage -> exclusions -> conditions -> questions | Policy summary | No coverage guarantee |
| INP-REG07 | HR/personnel document | Facts -> policy -> fairness/privacy -> next steps | HR document brief | Sensitive data protected |
| INP-REG08 | Government filing | Form -> requirements -> evidence -> gaps -> deadline | Filing checklist | Professional review |
| INP-REG09 | Safety data sheet | Hazards -> PPE -> handling -> disposal -> emergency | SDS summary | Safety boundary |
| INP-REG10 | IP/license document | Rights -> restrictions -> obligations -> uncertainties | Rights summary | License terms cited |
