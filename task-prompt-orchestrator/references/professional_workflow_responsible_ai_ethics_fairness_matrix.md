# Professional Workflow Responsible AI Ethics Fairness Matrix

Use this matrix when a workflow involves AI, automation, ranking, recommendations, content generation, user decisions, sensitive populations, high-stakes outcomes, fairness concerns, or potential social harm. Combine it with governance/policy, security/privacy/access, source/evidence, testing/simulation, quality/audit evidence, and high-risk validation when the workflow may affect real people.

## Ethical Scope

| Code | Ethics question | Workflow use |
|---|---|---|
| ETHSCOPE01 | Who can be affected by this workflow? | Identify users, subjects, bystanders, workers, customers, communities, and downstream recipients. |
| ETHSCOPE02 | What decision or influence does the workflow create? | Separate information support, recommendation, ranking, generation, moderation, triage, approval, or enforcement. |
| ETHSCOPE03 | What stakes are involved? | Classify low, medium, high, or critical stakes across rights, access, money, health, safety, work, reputation, or opportunity. |
| ETHSCOPE04 | What ethical principles apply? | Select fairness, autonomy, non-maleficence, beneficence, transparency, accountability, privacy, dignity, or sustainability. |
| ETHSCOPE05 | What groups need special attention? | Identify protected classes, vulnerable users, minors, disabled people, low-literacy users, non-native speakers, and marginalized groups. |
| ETHSCOPE06 | What power imbalance exists? | Check employer/employee, platform/user, lender/applicant, state/citizen, school/student, buyer/seller, or expert/novice dynamics. |
| ETHSCOPE07 | What ethical boundary is non-negotiable? | Define prohibited uses, escalation thresholds, human decision requirements, and stop conditions. |
| ETHSCOPE08 | What context changes ethical risk? | Note geography, culture, law, language, crisis state, scarcity, sensitive timing, and user expectations. |
| ETHSCOPE09 | What uncertainty must be disclosed? | Record missing evidence, unknown impact, weak measurement, model limits, and disputed values. |
| ETHSCOPE10 | What ethical-scope artifact is needed? | Produce ethics brief, affected-party map, stakes classification, or responsible-use boundary. |

## Harm Mapping

| Code | Ethics question | Workflow use |
|---|---|---|
| HARMMAP01 | What direct harm could occur? | Map denial, exclusion, misinformation, manipulation, unsafe advice, financial loss, privacy harm, or emotional distress. |
| HARMMAP02 | What indirect harm could occur? | Check chilling effects, overreliance, deskilling, stigma, unequal burden, labor displacement, and institutional feedback loops. |
| HARMMAP03 | What misuse or abuse is plausible? | Identify fraud, impersonation, harassment, surveillance, coercion, discrimination, spam, unsafe automation, or rights abuse. |
| HARMMAP04 | What over-automation harm exists? | Detect cases where automation could remove judgment, context, empathy, discretion, or meaningful review. |
| HARMMAP05 | What content harm exists? | Check hateful, sexual, violent, self-harm, medical, legal, financial, political, deceptive, or reputation-damaging outputs. |
| HARMMAP06 | What distribution harm exists? | Assess who sees outputs, how fast they spread, whether they are amplified, and whether corrections can reach recipients. |
| HARMMAP07 | What cumulative harm exists? | Track repeated small harms, fatigue, burden, long-term exclusion, compounding disadvantage, or model drift. |
| HARMMAP08 | What false-positive or false-negative harm matters? | Compare harm from wrongly flagging, approving, rejecting, classifying, recommending, or ignoring a case. |
| HARMMAP09 | What harm evidence is required? | Use complaints, incidents, user research, red-team results, benchmarks, audits, expert review, or domain evidence. |
| HARMMAP10 | What harm-map artifact is needed? | Produce harm register, misuse map, severity matrix, or prevention checklist. |

## Fairness Requirements

| Code | Ethics question | Workflow use |
|---|---|---|
| FAIRREQ01 | What fairness definition fits the context? | Choose equal treatment, equal opportunity, equalized odds, calibration, procedural fairness, accessibility, or distributive fairness. |
| FAIRREQ02 | What groups should be compared? | Define protected attributes, proxies, intersectional groups, locale, language, device, income, and access conditions. |
| FAIRREQ03 | What outcome disparity is unacceptable? | Set threshold for error, access, ranking, conversion, cost, exposure, delay, quality, or support differences. |
| FAIRREQ04 | What process fairness is required? | Ensure notice, consistent criteria, reviewability, appeal, explanation, and no hidden arbitrary treatment. |
| FAIRREQ05 | What proxy variable risk exists? | Identify features that encode race, gender, age, disability, income, geography, education, or social status. |
| FAIRREQ06 | What fairness tradeoff must be explicit? | Document tradeoffs between accuracy, safety, speed, cost, personalization, privacy, and group parity. |
| FAIRREQ07 | What data imbalance affects fairness? | Check sample size, missing data, label bias, historical discrimination, collection bias, and underrepresented cases. |
| FAIRREQ08 | What fairness mitigation is allowed? | Choose data balancing, thresholding, constraints, review routing, feature removal, calibration, or policy changes. |
| FAIRREQ09 | What fairness validation is required? | Run group-level metrics, qualitative review, user testing, expert review, and drift monitoring. |
| FAIRREQ10 | What fairness artifact is needed? | Produce fairness requirement spec, metric table, disparity review, or mitigation decision log. |

## Data And Label Ethics

| Code | Ethics question | Workflow use |
|---|---|---|
| DATAETH01 | Was the data collected appropriately? | Verify consent, notice, purpose, rights, provenance, licensing, sensitivity, and collection context. |
| DATAETH02 | Does the data represent affected users? | Check coverage across groups, languages, regions, devices, edge cases, and access barriers. |
| DATAETH03 | Are labels ethically reliable? | Inspect labeler instructions, disagreement, harmful taxonomies, cultural bias, expert need, and appeal cases. |
| DATAETH04 | Does historical data encode unfair systems? | Identify policing, lending, hiring, grading, medical, platform, or service history that reflects prior inequity. |
| DATAETH05 | Are sensitive attributes handled correctly? | Decide whether to collect, infer, avoid, protect, aggregate, or use only for fairness auditing. |
| DATAETH06 | What data minimization applies? | Limit data to necessary fields, retention, access, transformation, and sharing for the ethical purpose. |
| DATAETH07 | What data dignity issue exists? | Avoid demeaning categories, exploitative extraction, stigmatizing labels, and disrespectful annotation. |
| DATAETH08 | What synthetic or generated data risk exists? | Check realism, consent, representational harm, leakage, false diversity, and benchmark contamination. |
| DATAETH09 | What dataset limitation must be disclosed? | State coverage gaps, label quality, demographic limits, proxy risks, and known exclusions. |
| DATAETH10 | What data-ethics artifact is needed? | Produce data ethics sheet, label audit, data provenance note, or representativeness checklist. |

## Model And Automation Behavior

| Code | Ethics question | Workflow use |
|---|---|---|
| MODELETH01 | What model or automation role is used? | Distinguish drafting, retrieval, scoring, ranking, classification, generation, prediction, action, or decision support. |
| MODELETH02 | What autonomy level is allowed? | Define advisory, human-confirmed, supervised automation, auto-execute with review, or prohibited autonomy. |
| MODELETH03 | What model limitation matters? | Capture hallucination, bias, brittleness, stale data, uncertainty, calibration, prompt sensitivity, and domain mismatch. |
| MODELETH04 | What high-impact decision boundary applies? | Require human decision, domain expert review, legal review, or manual override for high-stakes outcomes. |
| MODELETH05 | What confidence or uncertainty rule applies? | Set confidence thresholds, abstention rules, uncertainty disclosure, and escalation paths. |
| MODELETH06 | What automation feedback loop exists? | Check whether outputs influence future data, behavior, incentives, rankings, enforcement, or resource allocation. |
| MODELETH07 | What model update risk exists? | Manage regression, drift, changed behavior, benchmark shift, prompt change, policy change, and vendor model updates. |
| MODELETH08 | What fallback is ethical? | Provide safe refusal, human support, alternative access, manual process, or service continuity. |
| MODELETH09 | What model behavior test is needed? | Run scenario tests, adversarial tests, group tests, edge cases, refusal tests, and calibration checks. |
| MODELETH10 | What model-ethics artifact is needed? | Produce automation role card, model-risk note, behavior test report, or override policy. |

## Transparency And Explainability

| Code | Ethics question | Workflow use |
|---|---|---|
| TRANSPEX01 | Who needs to know AI or automation was used? | Define disclosure for users, subjects, reviewers, clients, regulators, auditors, and internal operators. |
| TRANSPEX02 | What explanation is meaningful? | Provide reason codes, source basis, criteria, uncertainty, limits, and next steps in audience-appropriate language. |
| TRANSPEX03 | What should not be over-disclosed? | Avoid revealing secrets, security controls, private data, model internals, or harmful evasion instructions. |
| TRANSPEX04 | What source or provenance should be visible? | Show citations, inputs, model/tool identity, version, retrieval sources, transformation steps, and reviewer notes. |
| TRANSPEX05 | What user control should be offered? | Provide edit, opt out, manual review, preference setting, data correction, or appeal controls. |
| TRANSPEX06 | What limitation notice is needed? | State that outputs may be wrong, incomplete, biased, approximate, generated, or not professional advice when relevant. |
| TRANSPEX07 | What explanation timing matters? | Decide before action, at decision, after decision, on request, in audit, or during appeal. |
| TRANSPEX08 | What accessibility applies to explanations? | Make notices readable, localized, screen-reader friendly, concise, and available in alternate formats. |
| TRANSPEX09 | What explanation validation is needed? | Test whether users understand, can act on, and do not overtrust the explanation. |
| TRANSPEX10 | What transparency artifact is needed? | Produce disclosure text, explanation template, provenance card, or user notice. |

## Human Oversight And Accountability

| Code | Ethics question | Workflow use |
|---|---|---|
| HUMANOV01 | Who is accountable for the outcome? | Assign accountable owner, operator, reviewer, approver, escalation owner, and incident owner. |
| HUMANOV02 | What human review is meaningful? | Ensure reviewer has time, context, authority, domain expertise, and ability to change the outcome. |
| HUMANOV03 | What cannot be delegated to AI? | Mark decisions requiring human judgment, empathy, legal responsibility, professional license, or ethical discretion. |
| HUMANOV04 | What override mechanism exists? | Provide pause, stop, rollback, manual correction, reviewer escalation, and emergency shutdown. |
| HUMANOV05 | What reviewer bias may occur? | Check automation bias, confirmation bias, fatigue, incentives, inconsistent review, and rubber-stamping. |
| HUMANOV06 | What accountability trace is required? | Log input, output, model/tool, reviewer, decision, rationale, timestamp, and override history. |
| HUMANOV07 | What training does the human need? | Train on limits, review criteria, fairness, privacy, escalation, appeals, and incident response. |
| HUMANOV08 | What segregation of duties is needed? | Separate builder, operator, reviewer, approver, auditor, and appeal resolver when stakes are high. |
| HUMANOV09 | What oversight metric is needed? | Track review rate, override rate, errors caught, appeal outcomes, reviewer load, and unresolved exceptions. |
| HUMANOV10 | What oversight artifact is needed? | Produce RACI, review checklist, accountability log, or human-override runbook. |

## Consent Autonomy And User Agency

| Code | Ethics question | Workflow use |
|---|---|---|
| USERAGCY01 | What user choice is required? | Define opt in, opt out, consent, preference control, manual path, or informed participation. |
| USERAGCY02 | Is consent freely given? | Check coercion, dark patterns, employment pressure, service dependency, bundled consent, and vulnerable users. |
| USERAGCY03 | What user expectation applies? | Compare workflow behavior to reasonable expectations, prior notice, product context, and social norms. |
| USERAGCY04 | What manipulation risk exists? | Detect nudging, emotional exploitation, addiction loops, personalized pressure, scarcity tricks, or deceptive framing. |
| USERAGCY05 | What data or content control should users have? | Provide correction, deletion, export, preference update, feedback, block, mute, or appeal controls. |
| USERAGCY06 | What fallback preserves access? | Offer non-AI path, human support, accessible channel, low-tech option, or delayed manual review. |
| USERAGCY07 | What informed refusal is needed? | Explain when the workflow refuses, defers, routes to human, or limits automation. |
| USERAGCY08 | What agency metric should be tracked? | Monitor opt-out, complaint, appeal, correction, abandonment, confusion, and trust signals. |
| USERAGCY09 | What user-agency test is needed? | Test comprehension, choice architecture, accessibility, pressure, and ability to reverse decisions. |
| USERAGCY10 | What user-agency artifact is needed? | Produce consent flow, choice map, notice text, or agency checklist. |

## Sensitive Populations And Contexts

| Code | Ethics question | Workflow use |
|---|---|---|
| SENSCTX01 | Are minors involved? | Add age-appropriate design, guardian rules, school context, safety escalation, and content restrictions. |
| SENSCTX02 | Are vulnerable or dependent users involved? | Check health, disability, financial distress, migration status, incarceration, crisis, elder care, or dependence. |
| SENSCTX03 | Are workers or applicants affected? | Manage hiring, evaluation, surveillance, scheduling, productivity scoring, discipline, or termination risks. |
| SENSCTX04 | Are public-sector or civic rights affected? | Check benefits, policing, immigration, voting, education, housing, public services, or due process. |
| SENSCTX05 | Are healthcare or wellbeing outcomes affected? | Add clinical boundaries, emergency handling, professional review, safety disclaimers, and support referral. |
| SENSCTX06 | Are financial or livelihood outcomes affected? | Add credit, pricing, insurance, employment, income, housing, and fraud-control fairness checks. |
| SENSCTX07 | Are cultural or religious sensitivities involved? | Review symbols, language, norms, sacred content, stereotypes, and local expert input. |
| SENSCTX08 | Is crisis, conflict, or disaster context involved? | Raise thresholds for accuracy, harm prevention, escalation, uncertainty disclosure, and source reliability. |
| SENSCTX09 | What sensitive-context evidence is required? | Use domain expert review, community feedback, policy review, legal review, or specialized testing. |
| SENSCTX10 | What sensitive-context artifact is needed? | Produce sensitive-context checklist, expert review note, or protected-group impact assessment. |

## Content And Communication Ethics

| Code | Ethics question | Workflow use |
|---|---|---|
| CONTENTE01 | Could the output mislead users? | Check false claims, missing caveats, fake certainty, deepfake risk, hidden sponsorship, or deceptive framing. |
| CONTENTE02 | Could the output impersonate someone? | Require consent, labeling, voice/likeness rights, parody boundaries, and anti-deception controls. |
| CONTENTE03 | Could the output stigmatize or stereotype? | Review language, imagery, examples, categories, persona assumptions, and cultural framing. |
| CONTENTE04 | Could the output enable harmful action? | Prevent instructions for abuse, evasion, fraud, violence, self-harm, privacy invasion, or unsafe practices. |
| CONTENTE05 | Could the output create reputational harm? | Verify claims about people, companies, communities, and products before publication. |
| CONTENTE06 | What editorial standard applies? | Define evidence level, fact-checking, review, corrections, authorship, disclosure, and signoff. |
| CONTENTE07 | What generated-media label is needed? | Label synthetic images, audio, video, avatars, edited media, simulations, and AI-assisted text when relevant. |
| CONTENTE08 | What public-interest exception exists? | Balance transparency, harm, privacy, newsworthiness, safety, and rights when publishing sensitive content. |
| CONTENTE09 | What content ethics test is needed? | Run safety review, bias review, source check, cultural review, adversarial prompt test, and audience review. |
| CONTENTE10 | What content-ethics artifact is needed? | Produce content risk checklist, disclosure label, editorial signoff, or correction plan. |

## Appeals Redress And Contestability

| Code | Ethics question | Workflow use |
|---|---|---|
| REDRESS01 | Can affected people contest the outcome? | Provide appeal, correction, human review, complaint, or dispute path when outcomes matter. |
| REDRESS02 | What decision record supports appeal? | Preserve criteria, inputs, output, reviewer notes, explanation, policy, and timestamp. |
| REDRESS03 | Who resolves appeals independently? | Assign appeal owner separate from original operator when stakes or conflict require it. |
| REDRESS04 | What remedy is possible? | Define correction, reversal, compensation, apology, deletion, re-review, service access, or policy change. |
| REDRESS05 | What appeal timeline is fair? | Set response time, urgency path, emergency escalation, and status communication. |
| REDRESS06 | What user support is required? | Provide plain-language guidance, accessible channel, translation, documentation, and escalation help. |
| REDRESS07 | What systemic issue should appeals reveal? | Analyze repeated appeals for bias, data errors, policy gaps, model failures, or reviewer inconsistency. |
| REDRESS08 | What retaliation or burden risk exists? | Avoid punitive appeals, excessive proof burden, hidden fees, intimidation, or service loss. |
| REDRESS09 | What redress metric should be tracked? | Track appeal rate, reversal rate, time to resolution, group disparity, repeated issue, and satisfaction. |
| REDRESS10 | What redress artifact is needed? | Produce appeal process, remedy matrix, complaint log, or contestability checklist. |

## Responsible AI Testing

| Code | Ethics question | Workflow use |
|---|---|---|
| RAITEST01 | What ethical test set is required? | Build representative, edge-case, adversarial, protected-group, multilingual, and sensitive-context cases. |
| RAITEST02 | What fairness metric is tested? | Measure group disparities, error rates, calibration, ranking exposure, access, latency, and quality. |
| RAITEST03 | What harm scenario is tested? | Test misinformation, misuse, overreliance, emotional harm, unsafe advice, and rights-impact cases. |
| RAITEST04 | What transparency test is required? | Validate disclosure clarity, explanation usefulness, source visibility, uncertainty notice, and user comprehension. |
| RAITEST05 | What human-oversight test is required? | Test escalation, override, reviewer capacity, reviewer independence, and accountability logs. |
| RAITEST06 | What red-team method applies? | Use adversarial prompts, abuse cases, jailbreak attempts, proxy detection, and social-context challenges. |
| RAITEST07 | What benchmark limitation exists? | Avoid overtrusting benchmark scores that miss local context, edge cases, culture, or affected groups. |
| RAITEST08 | What pass/fail threshold applies? | Define severity-based gates, remediation rules, release blockers, warning thresholds, and exception approval. |
| RAITEST09 | What retest cadence applies? | Retest after model updates, prompt changes, data drift, policy changes, incidents, and scheduled reviews. |
| RAITEST10 | What Responsible AI test artifact is needed? | Produce RAI test plan, result table, red-team report, or release gate summary. |

## Monitoring Incidents And Audit

| Code | Ethics question | Workflow use |
|---|---|---|
| RAIAUDIT01 | What ethical signal should be monitored? | Track complaints, appeals, disparity, drift, refusals, overrides, incidents, user trust, and harm reports. |
| RAIAUDIT02 | What incident severity applies? | Classify harm by people affected, reversibility, rights impact, safety, spread, and legal exposure. |
| RAIAUDIT03 | What incident response is required? | Define triage, containment, correction, user notice, escalation, rollback, and postmortem. |
| RAIAUDIT04 | What audit evidence must persist? | Store scope, risk assessment, tests, approvals, model/tool versions, logs, incidents, and remediation. |
| RAIAUDIT05 | What external review may be needed? | Engage legal, compliance, ethics board, domain experts, community reviewers, or independent auditors. |
| RAIAUDIT06 | What policy or model change follows? | Update prompt, model, data, threshold, workflow, review rule, user notice, or prohibited-use boundary. |
| RAIAUDIT07 | What accountability report is needed? | Summarize risks, mitigations, incidents, metrics, exceptions, owners, and next review date. |
| RAIAUDIT08 | What retirement condition applies? | Retire or suspend workflow when harm is unmanageable, evidence is weak, or controls fail. |
| RAIAUDIT09 | What learning should feed the library? | Convert incidents and audits into templates, test cases, routing rules, and training updates. |
| RAIAUDIT10 | What audit artifact is needed? | Produce RAI audit pack, incident log, model/workflow card, or responsible-use review. |
