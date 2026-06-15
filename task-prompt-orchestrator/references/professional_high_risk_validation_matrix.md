# Professional High-Risk Validation Matrix

Use this when a task could affect health, law, money, safety, security, privacy, rights, reputation, employment, public claims, regulated operations, or vulnerable people. This matrix does not replace the normal workflow; it adds gates before final delivery.

Selection rule:

1. Select the normal P-code, industry code, and deliverable code first.
2. If the task touches any risk area below, add the matching validation code.
3. Put the gate in the prompt packet under `Quality checks` and `Boundaries`.
4. If a gate fails, label the output as draft, ask for professional review, or narrow the deliverable.

## SRC Source / Evidence / Freshness

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| SRC01 | Latest status, news, live facts | Browse or use current source; separate event date from publish date | Date boundary explicit |
| SRC02 | Scientific or technical claim | Prefer primary papers, standards, or official docs | Claim tied to source |
| SRC03 | Statistical claim | Capture denominator, time period, geography, and method | No naked percentages |
| SRC04 | Quoted material | Keep quotes short and attributed | Quote is accurate and minimal |
| SRC05 | Comparative claim | Use comparable entities and same measurement basis | Apples-to-apples comparison |
| SRC06 | Uncertain source quality | Grade source authority and conflict of interest | Confidence stated |
| SRC07 | User-supplied source only | Do not imply outside verification | Scope says source-limited |
| SRC08 | Historical timeline | Distinguish event, filing, publication, and revision dates | Chronology stable |
| SRC09 | Standards/regulations | Verify version, jurisdiction, effective date | Version/date shown |
| SRC10 | Missing evidence | Mark as unsupported or ask for source | No invented citation |

## LRG Legal / Regulatory

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| LRG01 | Legal advice request | Provide information, issues, and questions for counsel, not definitive advice | Legal boundary present |
| LRG02 | Contract review | Reference clauses and flag business/legal uncertainty | Clause evidence included |
| LRG03 | Jurisdiction-specific law | Verify jurisdiction and current law | Jurisdiction named |
| LRG04 | Compliance obligation | Map obligation to source, owner, evidence, and gap | Obligation register style |
| LRG05 | Litigation or dispute | Preserve facts, claims, and disputed points separately | No adjudication invented |
| LRG06 | Privacy policy/terms | Summarize rights, duties, risks, and open questions | Plain-language caveats |
| LRG07 | Employment/legal HR | Avoid illegal discrimination or retaliation guidance | Fair-process framing |
| LRG08 | Tax/accounting law | Require professional review for filing/payment decisions | No filing instruction as final |
| LRG09 | IP ownership/license | Identify rights holder, license, use scope, restrictions | Uncertain rights flagged |
| LRG10 | Regulated industry content | Add review gate before external publication | Draft status clear |

## HTH Health / Medical / Wellness

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| HTH01 | Symptoms or diagnosis | Encourage clinician evaluation; do not diagnose | Visit-prep framing |
| HTH02 | Medication or dosage | Do not invent dosing; advise pharmacist/clinician review | No dosage directive |
| HTH03 | Emergency symptoms | Recommend urgent local emergency care | Urgency not softened |
| HTH04 | Mental health crisis | Provide crisis/escalation boundary and supportive steps | Safety-first language |
| HTH05 | Diet/fitness plan | Keep gradual, non-clinical, and constraint-aware | Injury/medical caveat |
| HTH06 | Medical literature summary | State population, limits, and non-generalizability | No overclaim |
| HTH07 | Caregiver guidance | Include warning signs and recordkeeping | Escalation signs clear |
| HTH08 | Medical device/product claim | Avoid treatment claims unless sourced and approved | Claim evidence required |
| HTH09 | Vulnerable patient | Use extra caution for children, pregnancy, elder care | Professional review gate |
| HTH10 | Health misinformation risk | Use authoritative current sources | Source quality visible |

## MNY Finance / Investment / Tax

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| MNY01 | Investment advice | Provide research framework, not personal recommendation | Risk disclaimer and assumptions |
| MNY02 | Trading/market timing | Require current data and risk limits; no guaranteed return | No certainty language |
| MNY03 | Valuation/model | Show assumptions, scenarios, and sensitivities | Assumptions auditable |
| MNY04 | Personal finance | Ask/assume constraints carefully; avoid one-size-fits-all | Context limits stated |
| MNY05 | Tax decision | Require jurisdiction and professional review | Draft guidance only |
| MNY06 | Loan/debt guidance | Show tradeoffs, fees, rates, and consequences | Terms explicit |
| MNY07 | Insurance coverage | Reference policy terms and exclusions | No coverage guarantee |
| MNY08 | Fundraising claims | Separate actual metrics from projections | Forecast caveat |
| MNY09 | Accounting treatment | Cite policy/standard when possible; flag uncertainty | Review gate |
| MNY10 | Crypto/volatile asset | Highlight volatility, custody, fraud, and regulation risks | No hype framing |

## CYB Cybersecurity / Abuse

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| CYB01 | Vulnerability analysis | Keep within owned/authorized systems | Authorization boundary |
| CYB02 | Exploit detail | Avoid operational abuse steps unless defensive and authorized | Defensive framing |
| CYB03 | Credential/secret handling | Do not reveal, log, or store secrets | Secret-safe output |
| CYB04 | Malware/phishing topic | Focus on detection, prevention, or safe analysis | No deployment guidance |
| CYB05 | API security review | Check auth, authorization, validation, rate limits, data exposure | Endpoint evidence |
| CYB06 | Incident response | Prioritize containment, preservation, escalation | Action order clear |
| CYB07 | Access control | Apply least privilege and auditability | Privilege gaps flagged |
| CYB08 | Security tool output | Triage false positives and exploitability | Severity justified |
| CYB09 | Social engineering risk | Avoid scripts that facilitate deception | Safety redirect |
| CYB10 | Security documentation | Include owner, control, evidence, and monitoring | Audit-ready |

## PRV Privacy / Personal Data

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| PRV01 | Personal data processing | Map data categories, purpose, retention, access | Data flow explicit |
| PRV02 | Sensitive data | Minimize, redact, or avoid collection | Least data principle |
| PRV03 | Public sharing | Remove direct identifiers and risky quasi-identifiers | De-identification check |
| PRV04 | User tracking/analytics | State consent, purpose, retention, opt-out | Consent boundary |
| PRV05 | Children/minors data | Apply heightened consent and minimization | Minor-safety gate |
| PRV06 | Vendor data sharing | Identify vendor access, location, controls, DPA needs | Vendor risk noted |
| PRV07 | AI training/use of data | State whether data is retained, reused, or excluded | Use boundary clear |
| PRV08 | Data breach context | Preserve facts; advise incident process and counsel | No premature notification claim |
| PRV09 | Employee data | Need-to-know, fairness, retention, access rights | HR privacy gate |
| PRV10 | Form/intake design | Collect only fields needed for routing or service | Required fields justified |

## CLM Claims / Advertising / Public Promises

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| CLM01 | Product performance claim | Require substantiation and conditions | Evidence tied to claim |
| CLM02 | Health/medical marketing claim | Avoid treatment/cure claim unless approved and sourced | Regulated claim gate |
| CLM03 | Financial return claim | No guaranteed returns; include risk and assumptions | No misleading promise |
| CLM04 | Environmental/sustainability claim | Require lifecycle/source basis | No greenwashing |
| CLM05 | Comparative advertising | Use fair, current, verifiable comparison | Basis disclosed |
| CLM06 | Testimonial/review use | Check consent, typicality, disclosure | Endorsement compliant |
| CLM07 | Scarcity/urgency claim | Ensure offer is true and time-bound | No fake scarcity |
| CLM08 | Safety claim | Require test standard or certification | Certification named |
| CLM09 | AI capability claim | Separate supported capability from aspiration | No overclaim |
| CLM10 | Public launch copy | Add legal/compliance review for regulated areas | Review gate visible |

## MIN Minors / Vulnerable Users / Education

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| MIN01 | Child-facing content | Age-appropriate, safe, non-exploitative framing | Audience age stated |
| MIN02 | Student assessment | Fair rubric, no sensitive inference beyond evidence | Evidence-based feedback |
| MIN03 | Learning plan for minor | Encourage guardian/teacher context for high stakes | Support boundary |
| MIN04 | Bullying/self-harm concern | Safety escalation and supportive resources | Immediate safety first |
| MIN05 | Vulnerable customer | Avoid pressure tactics and unclear commitments | Ethical communication |
| MIN06 | Accessibility need | Provide accessible alternatives and plain language | Accessibility check |
| MIN07 | Elder care | Include professional/guardian review for care decisions | Escalation signs |
| MIN08 | Disability-related advice | Avoid diagnosis; focus on accommodations and questions | Non-diagnostic |
| MIN09 | Financial/legal action by vulnerable user | Require trusted professional review | No pressure |
| MIN10 | Data from minors | Apply strict privacy and consent gate | Minimal data |

## PHY Physical Safety / Engineering / Manufacturing

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| PHY01 | Structural/mechanical design | Treat as concept unless verified by qualified engineer | Engineering review gate |
| PHY02 | Electrical/electronics work | Include safety, codes, isolation, and qualified review | No unsafe wiring steps |
| PHY03 | Chemical/material handling | Require SDS, PPE, ventilation, disposal guidance | Safety data boundary |
| PHY04 | Manufacturing instruction | Separate visual prompt from production-ready CAD/spec | Draft status clear |
| PHY05 | Packaging structural design | Verify dimensions, load, material, and die-line feasibility | Prototype/test needed |
| PHY06 | Medical/assistive device | Require regulatory and clinical engineering review | No treatment guarantee |
| PHY07 | Food/consumer product | Add food safety/material compliance review | Compliance gate |
| PHY08 | Installation/repair | Include power-off, tools, hazards, and professional boundary | Hazard warnings |
| PHY09 | Transportation/outdoor gear | Flag load, weather, failure mode, and testing needs | Safety factor mentioned |
| PHY10 | Child product/toy | Require age, choking, material, and certification review | Child-safety gate |

## EMP Employment / HR / Fairness

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| EMP01 | Hiring screen | Use job-related criteria only | No protected-class inference |
| EMP02 | Candidate evaluation | Tie assessment to evidence and scorecard | No vibe-based decision |
| EMP03 | Interview questions | Avoid protected or illegal topics | Structured questions |
| EMP04 | Performance feedback | Specific behavior, impact, expectation, support | Fair and documented |
| EMP05 | Termination/discipline | Require policy, evidence, HR/legal review | Review gate |
| EMP06 | Compensation decision | Use role, market, performance, equity checks | Bias check |
| EMP07 | Employee survey | Preserve confidentiality and aggregation thresholds | Privacy respected |
| EMP08 | Workplace investigation | Separate allegations, evidence, findings, actions | Due process |
| EMP09 | Policy rollout | Plain language, consistent application, FAQ | No hidden obligations |
| EMP10 | Workforce planning | Avoid discriminatory assumptions | Scenario-based |

## PUB Public Communications / Reputation

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| PUB01 | Crisis statement | Verify facts, acknowledge impact, avoid speculation | Holding statement safe |
| PUB02 | Apology | Own impact, avoid defensiveness, state remedy | Specific and sincere |
| PUB03 | Press release | Check newsworthiness, facts, approvals | Claims sourced |
| PUB04 | Social post on sensitive topic | Check audience, timing, tone, and harm risk | Tone review |
| PUB05 | Executive message | Align message, action, accountability, next steps | Leadership voice credible |
| PUB06 | Layoff/reorg comms | Clear facts, empathy, legal/HR review | No ambiguity |
| PUB07 | Customer incident update | Separate known, unknown, next update time | Trust-preserving |
| PUB08 | Political/social issue | Clarify stance, stakeholders, risk, consistency | No accidental commitment |
| PUB09 | Community moderation | Rules, enforcement, appeal path | Fairness clear |
| PUB10 | Reputation audit | Evidence, stakeholder impact, response options | No rumor amplification |

## IPP Intellectual Property / Content Rights

| Code | Trigger | Required gate | Output check |
|---|---|---|---|
| IPP01 | Use of third-party image | Check license, permission, attribution, restrictions | Rights status stated |
| IPP02 | Style imitation | Avoid living-artist/style-owner targeting when inappropriate | Safer style description |
| IPP03 | Brand/logo use | Confirm ownership or permitted use | Trademark caution |
| IPP04 | Song/lyrics | Avoid long lyrics; summarize or use brief compliant excerpt | Copyright-safe |
| IPP05 | Book/article excerpt | Keep quotes short; summarize instead | Quotation limit respected |
| IPP06 | Dataset reuse | Check license, terms, privacy, redistribution | Dataset license noted |
| IPP07 | Software/license | Identify license obligations and compatibility risks | License obligations |
| IPP08 | Patent-like concept | Flag novelty/non-infringement uncertainty | Counsel review gate |
| IPP09 | UGC/testimonial asset | Consent, usage scope, platform terms | Consent gate |
| IPP10 | Generated asset handoff | Document prompt, sources, model, usage limits | Provenance recorded |
