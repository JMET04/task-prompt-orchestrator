# Professional Workflow Library

Use this reference to route user requests to proven professional workflows before generating prompts or executing. The goal is not to teach generic prompting; it is to produce professional products through the right process.

## Source Base

This library is synthesized from official AI prompting guidance, online workflow/prompt libraries, and the local prompt corpus in `D:\image2专业提示词库`.

High-signal source families:

- Fabric patterns: real-world task patterns for summarization, extraction, analysis, writing, threat modeling, and transformation. Source: https://github.com/danielmiessler/Fabric
- Microsoft PromptKit: composable prompt components: persona, protocol, taxonomy, format, and task template. Source: https://github.com/microsoft/PromptKit
- Content Design Prompt Library: production-ready UX/content/conversation-design systems. Source: https://github.com/adedayoagarau/content-design-prompt-library
- KevinRabun prompt-catalog: software, architecture, product, and delivery prompts. Source: https://github.com/KevinRabun/prompt-catalog
- Product management prompt sources: product-manager-prompts, PM-AI-Prompt-Playbook, product-on-purpose/pm-skills.
- QA and testing sources: tayyabakmal1/qa-prompt-library, jaktestowac/awesome-copilot-for-testers, LambdaTest/agent-skills.
- Engineering agent skills: github/awesome-copilot, addyosmani/agent-skills, getsentry/skills, Cloudflare/skills, Vercel and platform skills.
- GTM and sales sources: Prospeda/gtm-skills, Prospeda/claude-gtm-skills, AICMO marketing collection, content design systems.
- Legal/regulatory sources: anthonyloeff/Free-Legal-Prompts, TracyWang95/legal-prompts-for-gpt, rlwadh/regulatory-prompt-library.
- Domain expert prompt sources: aj-geddes/useful-ai-prompts, K-Dense-AI/scientific-agent-skills, MicrosoftDocs/Agent-Skills, NVIDIA/skills, Google/skills.
- Official prompting principles: OpenAI, Anthropic, Google Gemini, Microsoft Azure OpenAI docs.

Local lookup commands:

```powershell
python tools\search_prompt_library.py "requirements engineering" --limit 20
python tools\search_prompt_library.py "test plan" --limit 20
python tools\search_prompt_library.py "content system" --limit 20
python tools\search_prompt_library.py "risk assessment" --limit 20
python tools\search_prompt_library.py "workflow optimization" --limit 20
```

## Routing Protocol

For every user request:

1. Classify the domain and product type.
2. Select one workflow card below. If two domains apply, use a primary workflow plus one support workflow.
3. Build an optimized brief with inputs, constraints, audience, output format, and success criteria.
4. Generate prompt packets for each step in the workflow.
5. Execute the workflow if the user requested action.
6. Verify the product against the workflow's checks.
7. Save reusable prompts or artifacts when useful.

Output a workflow table only when helpful. For direct execution, use the workflow internally and report what was done.

## Workflow Index

For detailed subworkflow routing, read `professional_subworkflow_matrix.md` after selecting the primary P-code.

| Code | Professional problem | Product output |
|---|---|---|
| P01 | Source-backed research | Evidence table, synthesis, citations |
| P02 | Literature review / academic paper | Annotated bibliography, related work, citation audit |
| P03 | Competitive / market analysis | Competitor matrix, positioning, opportunity map |
| P04 | Product discovery / PRD | Problem framing, requirements, PRD, roadmap |
| P05 | Requirements engineering | Stakeholder questions, user stories, acceptance criteria |
| P06 | UX / content design | Content model, UX copy, conversation flow, IA |
| P07 | Image2 / visual production | Professional edit/generation prompt and visual output |
| P08 | Packaging / CAD / industrial design | Technical prompt, visual spec, production reference |
| P09 | Marketing campaign | Messaging angles, channel assets, launch plan |
| P10 | Sales / GTM pipeline | ICP, outreach, discovery script, proposal, follow-up |
| P11 | Social content system | Posts, carousels, threads, calendar, repurposing plan |
| P12 | Writing / editing / translation | Outline, draft, critique, final copy |
| P13 | Legal document workflow | Issue list, clause review, risk memo, redline suggestions |
| P14 | Regulatory / compliance | Requirement map, gap analysis, evidence checklist |
| P15 | Finance / budgeting / investment memo | Model assumptions, analysis, memo, risks |
| P16 | Data analysis / dashboard | Metric definitions, analysis, chart/report/dashboard |
| P17 | Software feature build | Spec, implementation plan, code changes, tests |
| P18 | Code review / security audit | Findings, severity, file evidence, fixes |
| P19 | QA / test planning | Test strategy, cases, coverage matrix, automation plan |
| P20 | DevOps / release / incident | Runbook, RCA, deployment checklist, rollback plan |
| P21 | Automation discovery | Process map, automation candidate, SOP, review gates |
| P22 | Business process optimization | Waste map, redesign, KPI plan, rollout steps |
| P23 | Strategy / decision memo | Options, tradeoffs, recommendation, risks |
| P24 | Presentation / deck | Narrative, slide outline, speaker notes, visual brief |
| P25 | Meeting / office productivity | Agenda, notes, decisions, action tracker |
| P26 | Education / training | Curriculum, lessons, exercises, assessment |
| P27 | Hiring / career / job workflow | JD, scorecard, interview kit, outreach, resume |
| P28 | Customer support / knowledge base | FAQ, triage flow, macro set, escalation rules |
| P29 | Scientific / technical protocol | Experiment plan, protocol, data capture, interpretation |
| P30 | Prompt library / skill creation | Taxonomy, prompt cards, skill docs, validation |

## P01 Source-Backed Research

Use for: current facts, industry research, "find sources", "compare claims", "what is true".

Workflow:
1. Define research question, scope, freshness, and source standard.
2. Search primary/authoritative sources first.
3. Extract claims into an evidence table.
4. Separate facts, estimates, opinions, and inferences.
5. Synthesize answer with dates, links, and uncertainty.

Prompt packet:

```text
Role: Source-backed research analyst.
Question: [question].
Scope: [time/geography/source types].
Source standard: prioritize [primary/official/peer-reviewed/industry].
Output: evidence table, concise synthesis, uncertainty notes.
Checks: every material claim has a source; dates are explicit; weak evidence is labeled.
```

## P02 Literature Review / Academic Paper

Use for: related work, paper expansion, citation audit, research proposal.

Workflow:
1. Define research question and boundaries.
2. Build seed paper list from authoritative databases or known works.
3. Cluster literature by method, theory, dataset, and debate.
4. Extract contribution, limitation, and relevance.
5. Write synthesis, not a paper-by-paper list.
6. Audit citations and unsupported claims.

Prompt packet:

```text
Role: Academic literature reviewer.
Topic: [topic].
Boundary: [field/time/method].
Output: themes, annotated bibliography, synthesis, citation gaps.
Checks: primary sources preferred; claims trace to citations; limitations stated.
```

## P03 Competitive / Market Analysis

Use for: competitors, market map, positioning, trend scan.

Workflow:
1. Define market, buyer, use case, geography, and timeframe.
2. Identify competitors and substitutes.
3. Compare features, pricing, positioning, channels, proof, and weaknesses.
4. Map opportunities and threats.
5. Recommend strategy and next research.

Prompt packet:

```text
Role: Competitive intelligence analyst.
Market: [market].
Audience: [buyer/user].
Output: competitor matrix, positioning map, opportunity list, recommendation.
Checks: sources for each competitor claim; separate observed fact from inference.
```

## P04 Product Discovery / PRD

Use for: product ideas, MVP, PRD, roadmap, feature definition.

Workflow:
1. Frame problem, users, jobs-to-be-done, constraints.
2. Capture assumptions and unknowns.
3. Define user journeys and success metrics.
4. Prioritize requirements.
5. Draft PRD with scope, non-goals, risks, and milestones.
6. Convert to backlog or implementation steps.

Prompt packet:

```text
Role: Senior product manager.
Problem: [problem].
Users: [segments].
Output: PRD with goals, user stories, requirements, metrics, risks, roadmap.
Checks: user value is clear; scope is bounded; acceptance criteria exist.
```

## P05 Requirements Engineering

Use for: turning vague stakeholder needs into implementable specs.

Workflow:
1. Identify stakeholders and goals.
2. Ask elicitation questions.
3. Convert needs to functional and non-functional requirements.
4. Define acceptance criteria and edge cases.
5. Build traceability matrix.

Prompt packet:

```text
Role: Requirements engineering specialist.
Context: [project].
Output: questions, requirements, user stories, acceptance criteria, traceability.
Checks: every requirement is testable; assumptions and dependencies are explicit.
```

## P06 UX / Content Design

Use for: UX copy, content strategy, conversation design, information architecture.

Workflow:
1. Define user goal, emotion, context, and task stage.
2. Map content hierarchy and user decisions.
3. Draft UX copy or conversation turns.
4. Check accessibility, clarity, tone, and error states.
5. Produce variants and final content spec.

Prompt packet:

```text
Role: Content designer and UX writer.
User context: [context].
Task: [screen/flow/content].
Output: content model, UX copy, error/help states, rationale.
Checks: plain language; accessible; action-oriented; no dark patterns.
```

## P07 Image2 / Visual Production

Use for: image generation, image editing, character refinement, product visuals, posters.

Workflow:
1. Classify intent: generate, edit, style transfer, product mockup, visual audit.
2. Label inputs: edit target, style reference, identity reference, insert object.
3. Define invariants: what must not change.
4. Define edits: what must change.
5. Add domain-specific visual template.
6. Generate/edit.
7. Inspect output and iterate one failure at a time.

Prompt packet:

```text
Role: Professional visual director.
Use case: [image2/edit/generate].
Inputs: [image roles].
Preserve: [identity, composition, style, structure].
Change: [specific edits].
Style: [medium, lighting, finish].
Avoid: [visual failures].
Checks: [pass/fail visual criteria].
```

In `D:\image2专业提示词库`, route to the existing Image2 vertical and specialty packs first.

## P08 Packaging / CAD / Industrial Design

Use for: packaging dieline prompts, CAD-like drawings, industrial concept, CMF, product proposal boards.

Workflow:
1. Identify artifact type: dieline, orthographic drawing, exploded view, product render, CMF board.
2. Capture object dimensions, material, function, and constraints.
3. Choose technical visual style.
4. Generate prompt with line types, views, annotations, and negative constraints.
5. Validate manufacturability/plausibility; mark AI output as reference, not production drawing.

Prompt packet:

```text
Role: Technical visual prompt engineer.
Artifact: [packaging/CAD/industrial].
Object: [object and dimensions].
Requirements: [views, annotations, materials, constraints].
Output: prompt or visual reference.
Checks: geometry plausible; labels/line types clear; no fake production claims.
```

## P09 Marketing Campaign

Use for: launch campaign, ads, email sequence, landing page, positioning.

Workflow:
1. Define ICP, pain, offer, promise, proof, channel, CTA.
2. Generate positioning and message angles.
3. Select best angle.
4. Build channel-specific assets.
5. Create variants and test hypotheses.
6. Review for specificity and compliance.

Prompt packet:

```text
Role: Marketing strategist and copywriter.
Offer: [offer].
Audience: [ICP].
Channel: [channel].
Output: positioning, campaign concept, assets, CTA, test plan.
Checks: concrete proof; no vague hype; channel-native format.
```

## P10 Sales / GTM Pipeline

Use for: ICP, lead research, outreach, discovery, objection handling, proposal.

Workflow:
1. Define ICP and buying triggers.
2. Research account/person context.
3. Draft personalized outreach.
4. Build discovery questions.
5. Map pains to solution and proof.
6. Create follow-up and next-step plan.

Prompt packet:

```text
Role: B2B sales strategist.
Target: [account/person/segment].
Offer: [offer].
Output: ICP notes, outreach, discovery script, objection responses, follow-up.
Checks: personalized; value-led; no unsupported claims.
```

## P11 Social Content System

Use for: LinkedIn posts, carousels, Twitter/X threads, short-video scripts, content calendar.

Workflow:
1. Define audience, authority thesis, pillar, and CTA.
2. Extract ideas from source material.
3. Select format and hook.
4. Draft content.
5. Repurpose into variants.
6. Build calendar and measurement plan.

Prompt packet:

```text
Role: Social content strategist.
Source: [material].
Audience: [audience].
Channel: [channel].
Output: hook, draft, variants, calendar, metric.
Checks: platform-native; one clear idea; credible proof.
```

## P12 Writing / Editing / Translation

Use for: articles, reports, emails, summaries, translation, polishing.

Workflow:
1. Define audience, purpose, tone, length, and source facts.
2. Outline.
3. Draft.
4. Critique for clarity, accuracy, completeness, and style.
5. Revise.
6. Produce final plus optional variants.

Prompt packet:

```text
Role: Professional editor.
Document: [type].
Audience: [audience].
Source facts: [facts].
Output: outline, draft, final, optional variants.
Checks: no invented facts; audience fit; clean structure.
```

## P13 Legal Document Workflow

Use for: contract summary, clause review, legal memo drafting, issue spotting. Not legal advice.

Workflow:
1. Identify document type, jurisdiction if known, and review purpose.
2. Extract parties, obligations, dates, rights, remedies, and unusual clauses.
3. Spot issues and missing terms.
4. Rank risk and business impact.
5. Draft questions or redline suggestions for counsel.

Prompt packet:

```text
Role: Legal document analyst, not a lawyer.
Document: [document].
Purpose: [review goal].
Output: summary, issue list, risk table, questions for counsel.
Checks: cite exact clauses; avoid definitive legal advice; flag jurisdiction limits.
```

## P14 Regulatory / Compliance

Use for: policy mapping, MedTech/IVD/pharma/SaMD prompts, audit readiness, compliance gap analysis.

Workflow:
1. Identify regulation, product/process, jurisdiction, and lifecycle stage.
2. Extract applicable requirements.
3. Map evidence and owners.
4. Identify gaps and risks.
5. Create remediation plan and audit checklist.

Prompt packet:

```text
Role: Regulatory compliance analyst.
Regime: [regulation/jurisdiction].
Product/process: [scope].
Output: requirement map, evidence checklist, gap analysis, remediation plan.
Checks: requirement citations; unknowns flagged; no unsupported compliance claims.
```

## P15 Finance / Budgeting / Investment Memo

Use for: budget planning, expense analysis, financial memo, valuation, investment thesis.

Workflow:
1. Define financial question and time horizon.
2. Collect inputs, assumptions, and constraints.
3. Build calculations or logic.
4. Analyze scenarios and sensitivities.
5. Write memo with risks and recommendation.

Prompt packet:

```text
Role: Finance analyst.
Question: [question].
Inputs: [numbers/assumptions].
Output: analysis, scenario table, recommendation, risks.
Checks: formulas clear; assumptions stated; not financial advice.
```

## P16 Data Analysis / Dashboard

Use for: CSV/spreadsheet analysis, BI dashboard, KPI report, metric diagnostics.

Workflow:
1. Define question and metric.
2. Inspect schema, row counts, missing values, units, grain.
3. Clean/transform.
4. Compute metrics.
5. Validate calculations.
6. Visualize and explain.
7. Save reproducible artifact.

Prompt packet:

```text
Role: Data analyst.
Question: [question].
Inputs: [files/tables].
Metrics: [definitions].
Output: findings, table/chart, methodology, caveats.
Checks: reproducible; units and filters stated; sample limits disclosed.
```

## P17 Software Feature Build

Use for: implement feature, fix bug, build app, refactor, integrate API.

Workflow:
1. Inspect current repo and user request.
2. Define behavior and acceptance criteria.
3. Make a small implementation plan.
4. Edit scoped files.
5. Run targeted tests.
6. Summarize changes and verification.

Prompt packet:

```text
Role: Senior engineer.
Objective: [feature/fix].
Repo context: [files/framework].
Output: code changes, tests, run instructions.
Checks: follows local patterns; no unrelated churn; verification run.
```

## P18 Code Review / Security Audit

Use for: code review, PR review, vulnerability scan, risk audit.

Workflow:
1. Identify changed files and threat/quality scope.
2. Inspect relevant code and tests.
3. Find concrete bugs, risks, regressions, missing tests.
4. Prioritize by severity.
5. Suggest minimal fixes.

Prompt packet:

```text
Role: Strict code/security reviewer.
Scope: [files/PR/repo].
Output: findings first, severity, evidence, impact, fix, test gaps.
Checks: every finding has file/source evidence; no speculation.
```

## P19 QA / Test Planning

Use for: test cases, test automation, QA strategy, mobile/web/API testing.

Workflow:
1. Define feature and risk areas.
2. Map requirements to test scenarios.
3. Create positive, negative, boundary, accessibility, regression cases.
4. Prioritize automation candidates.
5. Produce coverage matrix.

Prompt packet:

```text
Role: QA lead.
Feature: [feature].
Output: test strategy, test cases, coverage matrix, automation plan.
Checks: requirements traced; edge cases included; priorities clear.
```

## P20 DevOps / Release / Incident

Use for: deployment, rollback, incident response, RCA, observability, cloud ops.

Workflow:
1. Define system, change/incident, severity, and constraints.
2. Gather logs, metrics, timeline, config, dependencies.
3. Diagnose likely causes.
4. Create mitigation and rollback plan.
5. Write RCA or release checklist.

Prompt packet:

```text
Role: Site reliability / DevOps engineer.
Scope: [system/change/incident].
Output: triage, action plan, runbook, RCA or release checklist.
Checks: commands safe; rollback path exists; evidence separated from hypothesis.
```

## P21 Automation Discovery

Use for: "what can I automate", SOPs, AI workflow integration, business process automation.

Workflow:
1. List repeated processes.
2. Score frequency, pain, risk, data access, reversibility.
3. Select low-risk automation.
4. Design human-in-the-loop flow.
5. Create prompt, input template, output template, review gate.
6. Test on examples.

Prompt packet:

```text
Role: AI workflow automation specialist.
Process: [process].
Output: automation candidate table, selected workflow, SOP, prompt, review checklist.
Checks: human review; no secrets; failure modes documented.
```

## P22 Business Process Optimization

Use for: operations improvement, Lean/Six Sigma-style workflow redesign, productivity systems.

Workflow:
1. Map current process and handoffs.
2. Identify bottlenecks, waste, rework, and failure points.
3. Redesign future-state process.
4. Define KPIs and owners.
5. Create rollout plan and change risks.

Prompt packet:

```text
Role: Process optimization consultant.
Process: [process].
Output: current map, issues, future state, KPIs, rollout plan.
Checks: bottlenecks tied to evidence; changes are practical.
```

## P23 Strategy / Decision Memo

Use for: executive decision, options analysis, business strategy, policy choice.

Workflow:
1. Define decision and criteria.
2. Gather facts, constraints, and stakeholders.
3. Generate options.
4. Evaluate tradeoffs, risks, costs, reversibility.
5. Recommend action and next experiments.

Prompt packet:

```text
Role: Strategy advisor.
Decision: [decision].
Criteria: [criteria].
Output: options, tradeoff table, recommendation, risks, next steps.
Checks: assumptions explicit; recommendation follows criteria.
```

## P24 Presentation / Deck

Use for: pitch deck, training deck, board update, proposal deck.

Workflow:
1. Define audience, decision, and narrative.
2. Build storyline.
3. Outline slides.
4. Add evidence, visuals, and speaker notes.
5. Check pacing and message hierarchy.

Prompt packet:

```text
Role: Presentation strategist.
Audience: [audience].
Goal: [decision/change].
Output: storyline, slide outline, visual brief, speaker notes.
Checks: one message per slide; evidence supports claims.
```

## P25 Meeting / Office Productivity

Use for: meeting agenda, notes, action items, email, calendar, executive assistant tasks.

Workflow:
1. Define meeting/task purpose.
2. Capture participants, context, decisions needed.
3. Create agenda or extract notes.
4. Identify decisions, owners, deadlines.
5. Draft follow-up.

Prompt packet:

```text
Role: Executive operations assistant.
Task: [agenda/notes/follow-up].
Context: [meeting/doc/email].
Output: concise artifact plus action tracker.
Checks: owners and deadlines clear; no invented commitments.
```

## P26 Education / Training

Use for: curriculum, lesson plan, study guide, tutoring, course design.

Workflow:
1. Define learner level and target outcome.
2. Break topic into modules.
3. Create explanation, examples, practice, assessment.
4. Add feedback rubric.
5. Build schedule and review loop.

Prompt packet:

```text
Role: Instructional designer.
Topic: [topic].
Learner: [level].
Output: curriculum, lesson plan, exercises, assessment rubric.
Checks: progressive difficulty; measurable learning outcomes.
```

## P27 Hiring / Career / Job Workflow

Use for: job descriptions, interview kits, scorecards, resume tailoring, career planning.

Workflow:
1. Define role, level, company context, and must-have skills.
2. Build scorecard.
3. Create JD or resume positioning.
4. Draft interview questions or outreach.
5. Evaluate against criteria.

Prompt packet:

```text
Role: Talent strategist.
Role/candidate: [role or candidate].
Output: JD/scorecard/interview kit/resume/outreach.
Checks: criteria measurable; avoids discriminatory language.
```

## P28 Customer Support / Knowledge Base

Use for: FAQ, help center, support macros, triage, escalation.

Workflow:
1. Identify user issue categories.
2. Map symptoms to resolutions.
3. Draft support macros and knowledge base articles.
4. Add escalation triggers.
5. Review tone, accuracy, and self-service clarity.

Prompt packet:

```text
Role: Customer support knowledge manager.
Product/context: [product].
Output: FAQ, triage flow, macros, escalation rules.
Checks: accurate, empathetic, actionable; clear escalation.
```

## P29 Scientific / Technical Protocol

Use for: experiment design, lab protocol, technical procedure, scientific analysis plan.

Workflow:
1. Define hypothesis/objective and constraints.
2. Identify variables, controls, materials, safety, and data capture.
3. Draft protocol.
4. Define analysis plan and failure criteria.
5. Review limitations and ethics/safety.

Prompt packet:

```text
Role: Scientific protocol designer.
Objective: [objective].
Inputs: [materials/data].
Output: protocol, controls, data plan, interpretation guide.
Checks: controls included; safety/ethics flagged; claims bounded.
```

## P30 Prompt Library / Skill Creation

Use for: organizing prompts, creating a skill, building a workflow library, indexing prompt assets.

Workflow:
1. Define target users and trigger tasks.
2. Collect source prompts/workflows with license/source notes.
3. Normalize into taxonomy.
4. Convert to workflow cards and prompt packets.
5. Add indexes, routing rules, examples, and validation.
6. Test on representative tasks.

Prompt packet:

```text
Role: Prompt library architect.
Goal: [library/skill].
Sources: [sources].
Output: taxonomy, workflow cards, prompt packets, index, validation report.
Checks: every category has trigger, workflow, output, and acceptance criteria.
```

## Composition Rules

Use one primary workflow plus support workflows:

- Product launch: P04 primary + P09 + P10 + P24.
- New app: P04 primary + P17 + P19 + P09.
- Research report: P01 primary + P12 + P24.
- Image campaign: P07 primary + P09 + P11.
- Compliance deliverable: P14 primary + P13 + P25.
- Data dashboard: P16 primary + P24 + P12.
- Automation project: P21 primary + P22 + P17.

## Product Generation Output Schema

When a user asks to "generate a product" from a professional task, produce:

```text
Selected workflow:
Why this workflow:
Optimized brief:
Execution steps:
Prompt packets:
Artifacts to create:
Verification checklist:
Next action:
```

If executing, create the artifacts and report paths/results instead of only listing the schema.
