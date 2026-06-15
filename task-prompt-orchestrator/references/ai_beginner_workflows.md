# AI Beginner Workflows

Use this reference when the user wants to learn AI, build better AI habits, create a workflow library, or turn a vague goal into a repeatable AI-assisted process. When the user needs a ready-to-run prompt rather than an explanation, use `ai_beginner_starter_packs.md` first.

Principles distilled from official and high-quality sources:

- OpenAI Help: prompts should be clear, specific, contextual, and iterated after reviewing output.
- OpenAI prompt management guidance: keep stable role/tone guidance separate from task details; use compact examples; rerun evals when publishing prompts.
- Anthropic prompt engineering docs: define success criteria and some way to test them before optimizing prompts; use clarity, examples, role prompting, structure, prompt chaining, and retrieval/tool use when useful.
- Anthropic context engineering: treat context as finite; curate only the information most likely to produce the desired behavior.
- Google Gemini prompting strategies: prompt design is iterative; give clear, specific instructions and distinguish inputs, tasks, entities, and completion targets.
- Google Workspace guide: organize prompting by role and use case so ordinary workers can adopt it in daily workflows.
- Microsoft Azure OpenAI guidance: validate model outputs; do not assume a prompt that worked once generalizes everywhere.

Official references:

- OpenAI API prompt best practices: https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api
- OpenAI ChatGPT prompt best practices: https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt
- OpenAI Playground prompt management: https://help.openai.com/en/articles/9824968-prompt-management-in-playground
- Anthropic prompt engineering overview: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Anthropic context engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic interactive tutorial: https://github.com/anthropics/prompt-eng-interactive-tutorial
- Google Gemini prompting strategies: https://ai.google.dev/gemini-api/docs/prompting-strategies
- Google Workspace Gemini prompt guide: https://workspace.google.com/learning/content/gemini-prompt-guide
- Microsoft prompt engineering techniques: https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering

## Beginner Operating Loop

Teach this loop first:

```text
1. Goal: Say what you want and why it matters.
2. Context: Give the facts, files, audience, constraints, examples, and non-goals.
3. Task: Ask for one concrete action.
4. Output: Specify the format, length, tone, and acceptance criteria.
5. Review: Check accuracy, completeness, usefulness, and risks.
6. Iterate: Ask for a targeted revision, not a total restart.
7. Save: Store the final prompt, output, and lessons learned.
```

When helping a new user, convert their request into this loop and show only the next 1-3 actions.

## Quick Workflow Selector

| User need | Use workflow |
|---|---|
| "I don't know how to ask AI" | W01 First Useful Prompt |
| "Make this vague idea actionable" | W02 Goal-to-Plan |
| "Research this" | W03 Source-Backed Research |
| "Write / rewrite / summarize" | W04 Writing Pipeline |
| "Generate or edit images" | W05 Visual / Image2 Pipeline |
| "Help me code or build" | W06 Build / Coding Pipeline |
| "Analyze a spreadsheet or data" | W07 Data Analysis Pipeline |
| "Make slides, docs, email, meeting notes" | W08 Office Productivity |
| "Create marketing content" | W09 Marketing Content System |
| "Learn a new skill" | W10 Tutor / 30-Day Learning Plan |
| "Automate my workflow" | W11 Automation Discovery |
| "Check quality or improve output" | W12 Review and Eval Loop |

## W01 First Useful Prompt

Purpose: Help a beginner get a useful answer without knowing prompt engineering.

Use this packet:

```text
Role: You are a practical AI assistant for a beginner.
Goal: Help me complete [task].
Context: I am trying to [why]. My current situation is [facts]. I have [inputs/files]. I need [constraints].
Ask: First, tell me what information is missing. If nothing critical is missing, do the task.
Output: Give me [format], with a short explanation and next step.
Quality checks: Be specific, avoid jargon, and state assumptions.
```

Done when: the user has one concrete output and understands what to do next.

## W02 Goal-to-Plan

Purpose: Turn a vague goal into executable steps.

Procedure:

1. Restate the goal in one sentence.
2. Identify deliverables.
3. Split work into 3-9 steps.
4. Attach a prompt packet and done_when check to each step.
5. Execute step 1 immediately if the user asked for action.

Prompt packet:

```text
Role: You are a workflow architect.
Objective: Turn this goal into an executable plan: [goal].
Context: [facts, constraints, audience, deadline].
Output: A table with Step, Action, Prompt, Output, Done when.
Quality checks: No vague steps; every step produces an artifact or decision.
```

## W03 Source-Backed Research

Purpose: Prevent unsupported answers and teach citation habits.

Procedure:

1. Define the research question and freshness requirement.
2. Search primary or authoritative sources first.
3. Extract claims into an evidence table.
4. Separate confirmed facts from inference.
5. Synthesize with links and dates.

Prompt packet:

```text
Role: You are a source-backed research analyst.
Question: [research question].
Scope: [time range, geography, source types].
Procedure: Find authoritative sources, extract evidence, compare claims, and flag uncertainty.
Output: Evidence table plus concise answer.
Quality checks: Every key claim has a source; dates are explicit; weak evidence is labeled.
```

## W04 Writing Pipeline

Purpose: Turn AI from a one-shot writer into a drafting partner.

Procedure:

1. Brief: audience, purpose, tone, length, must-include facts.
2. Outline: get structure before prose.
3. Draft: write from approved outline.
4. Critique: check clarity, accuracy, missing context, and tone.
5. Revise: targeted rewrite.
6. Package: final version plus optional title, summary, or variants.

Prompt packet:

```text
Role: You are a professional editor.
Task: Create [document type] for [audience].
Context: [facts and source material].
Tone: [tone].
Output: First outline, then draft after approval unless user asked to proceed directly.
Quality checks: Clear structure, no invented facts, matches audience, concise.
```

## W05 Visual / Image2 Pipeline

Purpose: Help beginners generate or edit images without vague art prompts.

Procedure:

1. Identify mode: generate new image or edit existing image.
2. Label inputs: edit target, reference, style, insert object.
3. Define invariants: what must stay unchanged.
4. Define changes: what must be modified.
5. Add style, composition, technical requirements, and negative prompt.
6. Validate output against the visual checklist.
7. Iterate one failure at a time.

Prompt packet:

```text
Use case: [generate/edit/image2].
Asset type: [poster, product image, CAD, packaging, UI, character, etc.].
Input images: [Image 1 role; Image 2 role].
Preserve: [identity, composition, pose, style, colors, structure].
Change: [specific edits].
Style: [medium, lighting, finish].
Avoid: [drift, wrong hands, text artifacts, extra objects, bad anatomy, etc.].
Output checks: [visible pass/fail criteria].
```

When working in `D:\image2专业提示词库`, prefer its Image2 templates and indexes before writing a fresh visual prompt.

## W06 Build / Coding Pipeline

Purpose: Help beginners use AI to build safely instead of asking for random code.

Procedure:

1. Describe desired behavior, platform, users, and constraints.
2. Inspect existing project state.
3. Ask AI for a small implementation plan.
4. Implement one slice.
5. Run tests or manual checks.
6. Ask for a review.
7. Document how to run and what changed.

Prompt packet:

```text
Role: You are a senior engineer in this codebase.
Objective: Implement [small feature/fix].
Context: [repo, files, desired behavior].
Procedure: Inspect first, follow local patterns, make scoped edits, verify.
Output: Changed files, behavior summary, verification.
Quality checks: No unrelated rewrites; tests or checks cover the behavior.
```

## W07 Data Analysis Pipeline

Purpose: Keep analysis reproducible and avoid chart-first work.

Procedure:

1. Define the question.
2. Inspect schema, row counts, missing values, units.
3. Define metrics and filters.
4. Compute results.
5. Validate calculations.
6. Summarize insight, caveats, and next action.
7. Visualize only when it clarifies.

Prompt packet:

```text
Role: You are a data analyst.
Question: [question].
Inputs: [tables/files].
Metrics: [definitions, formulas, filters].
Output: Findings table, calculation notes, and chart if useful.
Quality checks: Reproducible formulas, units stated, caveats included.
```

## W08 Office Productivity

Purpose: Make AI useful for everyday documents, meetings, and email.

Procedure:

1. Classify task: email, meeting notes, document, slide, spreadsheet, schedule.
2. Provide audience, desired outcome, tone, constraints.
3. Ask for draft or structured extraction.
4. Review for facts, tone, and missing action items.
5. Produce final copy plus next actions.

Prompt packet:

```text
Role: You are an executive assistant.
Task: [email/meeting/doc/slides].
Context: [audience, facts, goal].
Output: [format].
Quality checks: Clear, actionable, correct tone, no invented commitments.
```

## W09 Marketing Content System

Purpose: Build repeatable marketing outputs instead of isolated posts.

Procedure:

1. Define audience, offer, promise, proof, channel, and CTA.
2. Generate messaging angles.
3. Select one angle.
4. Draft channel-native content.
5. Create variants.
6. Review for specificity, credibility, and compliance.
7. Save reusable positioning language.

Prompt packet:

```text
Role: You are a marketing strategist and copywriter.
Offer: [product/service].
Audience: [segment].
Channel: [LinkedIn, email, landing page, ad, short video].
Objective: [awareness, conversion, retention].
Output: [draft + variants + CTA].
Quality checks: Specific audience, concrete proof, no vague hype.
```

## W10 Tutor / 30-Day Learning Plan

Purpose: Help beginners learn AI or any topic through practice.

Procedure:

1. Diagnose current level and goal.
2. Build a 7-day quick-start or 30-day plan.
3. Each lesson has concept, example, practice task, feedback criteria.
4. Use Socratic questions when the learner is stuck.
5. Track outputs in a portfolio.

Prompt packet:

```text
Role: You are a patient tutor.
Topic: [topic].
Learner level: [beginner/intermediate].
Goal: [outcome].
Plan: Create a progressive learning path with daily practice.
Output: Day, concept, example, exercise, success criteria.
Quality checks: Practical, not too much theory, produces portfolio artifacts.
```

## W11 Automation Discovery

Purpose: Help users find where AI saves time without breaking processes.

Procedure:

1. List repeated tasks.
2. Score by frequency, pain, risk, data availability, and reversibility.
3. Pick a low-risk first automation.
4. Design human-in-the-loop workflow.
5. Create prompt, input template, output template, and review step.
6. Test on 3 examples.
7. Save SOP.

Prompt packet:

```text
Role: You are an AI workflow automation specialist.
Objective: Identify and design one low-risk automation.
Inputs: [current process, tools, data, constraints].
Output: Candidate table, selected workflow, SOP, prompt, review checklist.
Quality checks: Human review included; no secrets exposed; failure mode described.
```

## W12 Review and Eval Loop

Purpose: Teach users that good AI work needs checking.

Procedure:

1. Define success criteria.
2. Create a checklist or grader.
3. Test the output against real examples.
4. Categorize failures.
5. Improve prompt or workflow.
6. Retest.
7. Save final prompt with version and known limits.

Prompt packet:

```text
Role: You are a strict evaluator.
Artifact: [output to review].
Success criteria: [criteria].
Procedure: Check correctness, completeness, format, source support, risks, and usefulness.
Output: Pass/fail table, issues by severity, exact fixes.
Quality checks: Findings are specific and actionable; no vague criticism.
```

## 7-Day AI Starter Path

Use this when a user asks how to get started quickly.

| Day | Practice | Output |
|---|---|---|
| 1 | First Useful Prompt | One clear prompt for a real task |
| 2 | Goal-to-Plan | A 3-9 step plan with done_when checks |
| 3 | Writing Pipeline | One polished email/doc/post |
| 4 | Research Pipeline | Evidence table plus short answer |
| 5 | Visual or Data Pipeline | One image prompt/edit prompt or one analysis |
| 6 | Automation Discovery | One low-risk AI workflow SOP |
| 7 | Review and Eval | A saved prompt v1.0 with checklist and revision notes |

## Beginner Guardrails

- Never ask a beginner to learn all prompting theory before doing useful work.
- Prefer concrete artifacts over explanations.
- Use the user's language.
- Ask for missing context only when it blocks quality or safety.
- Warn users not to paste secrets, private keys, credentials, or sensitive personal data.
- For factual/current/high-stakes work, browse or require sources.
- Save reusable prompts and workflows so the user improves over time.
