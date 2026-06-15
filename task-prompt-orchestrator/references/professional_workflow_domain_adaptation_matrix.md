# Professional Workflow Domain Adaptation Matrix

Use this when a generic workflow must be adapted to a specific industry, business function, regulated environment, production context, or professional domain. Domain adaptation rules translate the same workflow skeleton into domain-appropriate inputs, controls, artifacts, reviewers, terminology, and acceptance evidence.

Selection rule:

1. Select the base workflow and subworkflow first.
2. Select the closest domain adaptation code here.
3. Add domain-specific inputs, terminology, compliance checks, artifacts, reviewers, and acceptance evidence to the prompt packet.
4. Do not claim domain fit until the workflow names its domain assumptions and validation boundary.

## RETWF Retail / E-commerce Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| RETWF01 | Product listing workflow | Add SKU, attributes, imagery, price, channel specs | Check marketplace rules | Listing QA |
| RETWF02 | Merchandising workflow | Add assortment, placement, bundles, seasonality | Check inventory and margin | Merch plan |
| RETWF03 | Conversion optimization workflow | Add funnel step, test variant, traffic segment | Avoid unsupported uplift claims | Experiment brief |
| RETWF04 | Customer review workflow | Add review source, sentiment, defect themes | Preserve review authenticity | Review synthesis |
| RETWF05 | Promotion workflow | Add offer terms, eligibility, dates, exclusions | Check pricing/legal rules | Promo checklist |
| RETWF06 | Marketplace operations workflow | Add channel feed, taxonomy, rejection handling | Validate feed schema | Channel log |
| RETWF07 | Returns/refunds workflow | Add policy, reason codes, customer impact | Check consumer protection rules | Returns analysis |
| RETWF08 | Demand planning workflow | Add sales history, lead time, stockouts, forecast | Show assumptions | Demand note |
| RETWF09 | Catalog cleanup workflow | Add duplicate, variant, taxonomy, image issues | Protect live listings | Catalog diff |
| RETWF10 | Customer lifecycle workflow | Add acquisition, retention, loyalty, churn stage | Respect consent rules | Lifecycle map |

## FINWF Finance / Investment Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| FINWF01 | Financial analysis workflow | Add period, metric definition, source statements | Reconcile figures | Model check |
| FINWF02 | Valuation workflow | Add method, drivers, sensitivities, comparables | State assumptions | Valuation pack |
| FINWF03 | Budgeting workflow | Add cost centers, owners, variance thresholds | Separate actuals/forecast | Budget bridge |
| FINWF04 | Investment memo workflow | Add thesis, catalysts, risks, valuation, evidence | Avoid financial advice framing | Memo evidence |
| FINWF05 | Credit analysis workflow | Add leverage, coverage, covenants, liquidity | Check source dates | Credit note |
| FINWF06 | Audit support workflow | Add assertion, sample, control, evidence | Preserve audit trail | Audit packet |
| FINWF07 | KPI reporting workflow | Add metric dictionary, denominator, cadence | Prevent metric drift | KPI dictionary |
| FINWF08 | Scenario planning workflow | Add base/upside/downside, driver ranges | Label uncertainty | Scenario table |
| FINWF09 | Expense control workflow | Add policy, approval, exception, documentation | Check delegation rules | Expense review |
| FINWF10 | Treasury/cash workflow | Add cash position, runway, inflows, obligations | Validate timing | Cash bridge |

## LEGWF Legal / Compliance Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| LEGWF01 | Contract review workflow | Add clause map, obligations, redlines, risk notes | Avoid legal advice overclaim | Clause matrix |
| LEGWF02 | Policy compliance workflow | Add policy source, applicability, control evidence | Confirm jurisdiction/scope | Compliance note |
| LEGWF03 | Regulatory research workflow | Add authority hierarchy, dates, obligations | Verify current law/source | Authority table |
| LEGWF04 | Privacy review workflow | Add data classes, purpose, sharing, retention | Apply minimization | Privacy checklist |
| LEGWF05 | IP rights workflow | Add ownership, license, usage, attribution | Check rights boundary | Rights log |
| LEGWF06 | Legal intake workflow | Add parties, facts, documents, deadlines | Flag counsel review | Intake packet |
| LEGWF07 | Risk register workflow | Add legal exposure, probability, mitigation, owner | Separate facts from assessment | Risk register |
| LEGWF08 | Evidence preservation workflow | Add source, custody, timestamps, integrity | Preserve chain of custody | Evidence log |
| LEGWF09 | Approval workflow | Add required approver, delegation, signoff artifact | Record approval basis | Approval record |
| LEGWF10 | Legal ops workflow | Add matter type, SLA, queue, templates | Protect confidentiality | Matter dashboard |

## HLTHWF Health / Life Sciences Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| HLTHWF01 | Clinical information workflow | Add population, intervention, comparator, outcome | Avoid medical advice | Clinical caveat |
| HLTHWF02 | Evidence synthesis workflow | Add study design, inclusion criteria, bias notes | Prefer primary literature | Evidence table |
| HLTHWF03 | Patient education workflow | Add literacy level, safety limits, referral cues | Include urgent-care boundary | Patient handout |
| HLTHWF04 | Protocol workflow | Add objective, endpoints, procedures, deviations | Require expert review | Protocol draft |
| HLTHWF05 | Regulatory submission workflow | Add required sections, evidence, version control | Check agency rules | Submission map |
| HLTHWF06 | Lab workflow | Add sample, assay, controls, QC, chain of custody | Prevent unsafe procedures | Lab checklist |
| HLTHWF07 | Pharmacovigilance workflow | Add event, seriousness, causality, reporting clock | Escalate reportable events | Safety case |
| HLTHWF08 | Healthcare operations workflow | Add patient flow, staffing, capacity, handoff | Protect PHI | Ops map |
| HLTHWF09 | Medical claims workflow | Add claim, evidence grade, contraindications | Add claims review | Claim substantiation |
| HLTHWF10 | Bioinformatics workflow | Add dataset, pipeline, reference genome, QC | Track provenance | Analysis log |

## EDUWF Education / Training Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| EDUWF01 | Lesson design workflow | Add objective, learner level, activity, assessment | Align to objective | Lesson plan |
| EDUWF02 | Curriculum workflow | Add sequence, prerequisites, standards, pacing | Check progression | Curriculum map |
| EDUWF03 | Assessment workflow | Add rubric, item type, difficulty, feedback | Avoid bias/leakage | Assessment pack |
| EDUWF04 | Tutoring workflow | Add diagnosis, explanation level, practice, feedback | Encourage learning not shortcuts | Tutoring trace |
| EDUWF05 | Study plan workflow | Add deadline, weak areas, recall schedule | Validate current syllabus | Study calendar |
| EDUWF06 | Training operations workflow | Add cohort, facilitator, materials, completion | Track attendance | Training log |
| EDUWF07 | Learning analytics workflow | Add learner events, outcome, segmentation | Protect student data | Analytics note |
| EDUWF08 | Accessibility learning workflow | Add accommodation, format, readability | Meet accessibility needs | Access check |
| EDUWF09 | Certification prep workflow | Add exam blueprint, domains, practice gates | Avoid stale exam assumptions | Blueprint map |
| EDUWF10 | Feedback workflow | Add learner artifact, rubric, next practice | Make feedback actionable | Feedback record |

## ENGWF Engineering / Product Development Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| ENGWF01 | Software delivery workflow | Add repo, issue, tests, build, deployment path | Respect existing patterns | Diff/test log |
| ENGWF02 | Debugging workflow | Add reproduction, logs, hypothesis, fix, verification | Preserve user changes | Debug trace |
| ENGWF03 | Architecture workflow | Add constraints, interfaces, tradeoffs, migration | Avoid unnecessary abstraction | Architecture note |
| ENGWF04 | Product requirements workflow | Add user, problem, success metric, edge cases | Validate problem fit | PRD slice |
| ENGWF05 | QA workflow | Add test scope, fixtures, expected results, regression | Map tests to risks | Test plan |
| ENGWF06 | DevOps workflow | Add environment, secrets, CI/CD, rollback | Protect credentials | Run log |
| ENGWF07 | API workflow | Add contract, payloads, auth, errors, versioning | Validate compatibility | API contract |
| ENGWF08 | Security engineering workflow | Add threat model, attack surface, controls | Avoid exposing exploit steps | Security review |
| ENGWF09 | Data engineering workflow | Add pipeline, schema, lineage, freshness, quality | Validate transforms | Pipeline check |
| ENGWF10 | Product analytics workflow | Add event taxonomy, metric, cohort, decision | Check denominator | Analytics spec |

## CREWF Creative / Media Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| CREWF01 | Visual concept workflow | Add subject, style, composition, constraints | Respect rights/brand | Concept board |
| CREWF02 | Image2 workflow | Add reference image role, edit intent, technical output | Preserve requested geometry | Prompt packet |
| CREWF03 | Video workflow | Add duration, scene list, camera, audio, captions | Check platform specs | Shot list |
| CREWF04 | Brand workflow | Add brand voice, assets, usage rules, approvals | Enforce brand guardrails | Brand check |
| CREWF05 | Campaign workflow | Add audience, offer, channel, variants, testing | Substantiate claims | Campaign matrix |
| CREWF06 | Design system workflow | Add components, tokens, states, accessibility | Avoid inconsistent patterns | Component spec |
| CREWF07 | Copywriting workflow | Add audience, promise, proof, tone, CTA | Avoid deceptive claims | Copy QA |
| CREWF08 | Editorial workflow | Add angle, outline, sources, edits, publish | Fact/rights check | Editorial package |
| CREWF09 | Localization workflow | Add locale, cultural constraints, glossary | Avoid literal mistranslation | Localization QA |
| CREWF10 | Asset production workflow | Add formats, dimensions, naming, export settings | Validate deliverable specs | Asset manifest |

## OPSWF Operations / Service Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| OPSWF01 | SOP workflow | Add task owner, steps, inputs, exceptions, QA | Keep instructions testable | SOP draft |
| OPSWF02 | Support workflow | Add ticket class, priority, SLA, response template | Protect private data | Support log |
| OPSWF03 | Incident workflow | Add severity, timeline, owner, comms, postmortem | Escalate critical issues | Incident report |
| OPSWF04 | Procurement workflow | Add vendor, requirements, evaluation, approvals | Check conflict/vendor rules | Procurement pack |
| OPSWF05 | Inventory workflow | Add stock levels, reorder point, lead time | Validate counts | Inventory report |
| OPSWF06 | Facilities workflow | Add location, asset, safety, maintenance window | Check safety/access | Work order |
| OPSWF07 | Customer success workflow | Add account health, adoption, risk, action plan | Align with contract | Account plan |
| OPSWF08 | Workforce planning workflow | Add demand, capacity, skills, schedule | Respect labor rules | Staffing plan |
| OPSWF09 | Process improvement workflow | Add baseline, waste, root cause, future state | Measure before/after | Improvement brief |
| OPSWF10 | Knowledge base workflow | Add article type, audience, search terms, ownership | Keep current owner | KB record |

## MFGWF Manufacturing / Physical Product Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| MFGWF01 | CAD drawing workflow | Add dimensions, tolerances, views, materials | Mark non-manufacturing assumptions | Drawing checklist |
| MFGWF02 | Packaging engineering workflow | Add dieline, folds, substrate, print, assembly | Check manufacturability | Packaging spec |
| MFGWF03 | BOM workflow | Add parts, suppliers, quantities, alternates | Validate part numbers | BOM table |
| MFGWF04 | Quality inspection workflow | Add CTQ, sampling, defect classes, acceptance | Use measurable criteria | Inspection plan |
| MFGWF05 | Process planning workflow | Add routing, machines, fixtures, cycle time | Check capacity/safety | Routing sheet |
| MFGWF06 | Supplier workflow | Add supplier profile, capability, risk, lead time | Verify certifications | Supplier note |
| MFGWF07 | Change control workflow | Add ECO, affected parts, inventory, revision | Control revision release | ECO packet |
| MFGWF08 | Compliance marking workflow | Add standards, labels, warnings, region | Require certification check | Compliance map |
| MFGWF09 | Prototype workflow | Add prototype goal, materials, tests, feedback | Separate prototype from production | Prototype report |
| MFGWF10 | Failure analysis workflow | Add defect, conditions, root cause, corrective action | Preserve sample evidence | FA report |

## GOVWF Government / Public Sector Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| GOVWF01 | Policy memo workflow | Add mandate, stakeholders, options, impacts | Distinguish evidence from policy | Policy memo |
| GOVWF02 | Grant workflow | Add eligibility, objectives, budget, compliance | Check solicitation rules | Grant checklist |
| GOVWF03 | Public communication workflow | Add audience, accessibility, translations, approval | Avoid unsupported claims | Public notice |
| GOVWF04 | Procurement/RFP workflow | Add requirements, scoring, vendor questions | Preserve fairness | RFP matrix |
| GOVWF05 | Records workflow | Add retention, disclosure, classification, custody | Follow records policy | Records log |
| GOVWF06 | Program evaluation workflow | Add logic model, indicators, data, findings | Show limitations | Evaluation report |
| GOVWF07 | Stakeholder consultation workflow | Add groups, questions, feedback synthesis | Avoid selective reporting | Consultation log |
| GOVWF08 | Permitting workflow | Add applicant, criteria, documents, decision path | Follow statutory process | Permit checklist |
| GOVWF09 | Risk/emergency workflow | Add scenario, command roles, resources, alerts | Escalate safety risks | Response plan |
| GOVWF10 | Legislative tracking workflow | Add bill, status, amendments, implications | Verify latest status | Tracking note |

## HRWF HR / People Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| HRWF01 | Recruiting workflow | Add role, competencies, sourcing, interview plan | Reduce bias | Hiring packet |
| HRWF02 | Interview workflow | Add structured questions, rubric, notes | Use consistent criteria | Interview kit |
| HRWF03 | Onboarding workflow | Add role tasks, systems, training, milestones | Protect access scope | Onboarding plan |
| HRWF04 | Performance workflow | Add goals, evidence, feedback, development plan | Avoid unsupported judgments | Review packet |
| HRWF05 | Learning workflow | Add skill gap, curriculum, practice, assessment | Track completion | L&D plan |
| HRWF06 | Employee relations workflow | Add facts, policy, parties, escalation | Protect confidentiality | Case note |
| HRWF07 | Compensation workflow | Add role level, market data, bands, approvals | Check equity/policy | Comp analysis |
| HRWF08 | Workforce analytics workflow | Add population, metric, privacy threshold | Avoid re-identification | People analytics |
| HRWF09 | Policy rollout workflow | Add policy change, audience, training, acknowledgement | Verify understanding | Rollout log |
| HRWF10 | Offboarding workflow | Add access removal, knowledge transfer, final docs | Confirm revocation | Offboarding checklist |

## AECWF Architecture / Construction / Real Estate Workflow Adaptation

| Code | Domain adaptation | Workflow adjustment | Required guardrail | Evidence |
|---|---|---|---|---|
| AECWF01 | Design brief workflow | Add site, users, constraints, program, style | Capture assumptions | Design brief |
| AECWF02 | Drawing review workflow | Add sheet set, scale, codes, annotations | Flag code-professional review | Drawing review |
| AECWF03 | Specification workflow | Add materials, standards, installation, alternates | Check product/code fit | Spec section |
| AECWF04 | Cost estimate workflow | Add quantities, unit costs, assumptions, exclusions | Date cost basis | Estimate note |
| AECWF05 | Schedule workflow | Add milestones, dependencies, permits, inspections | Track critical path | Schedule map |
| AECWF06 | Site issue workflow | Add location, condition, photos, responsible party | Preserve field evidence | Field report |
| AECWF07 | Permit workflow | Add jurisdiction, forms, drawings, approvals | Verify local requirements | Permit matrix |
| AECWF08 | Facility operations workflow | Add asset, maintenance, inspection, lifecycle | Track service history | Facility log |
| AECWF09 | Real estate diligence workflow | Add property, comps, title, zoning, risk | Verify source authority | Diligence pack |
| AECWF10 | Handover workflow | Add as-builts, O&M manuals, warranties, training | Confirm owner acceptance | Handover record |
