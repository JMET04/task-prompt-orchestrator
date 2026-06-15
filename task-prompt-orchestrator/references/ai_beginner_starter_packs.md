# AI Beginner Starter Packs

Use this reference when a beginner needs a ready-to-run AI workflow, not a lesson about prompting. Pick one starter pack, fill the slots, run it, then improve only the weak part.

## Selection Map

| Pack | Use when the user says | Output |
|---|---|---|
| SP01 First Useful Ask | "I do not know how to ask" | One useful answer plus missing-info check |
| SP02 Turn Goal Into Plan | "I have an idea/goal" | 3-9 executable steps |
| SP03 Research With Sources | "research/find out/compare sources" | Evidence table and sourced answer |
| SP04 Write Or Rewrite | "write/summarize/polish" | Draft or rewrite with checks |
| SP05 Image Or Visual Prompt | "image/image2/design/packaging/CAD-like" | Generation-ready visual prompt |
| SP06 Code Or App Help | "build/fix/code/app" | Implementation plan or first code step |
| SP07 Data Or Spreadsheet | "analyze data/spreadsheet/report" | Metric plan and analysis output |
| SP08 Office Output | "slides/doc/email/meeting notes" | Structured office artifact |
| SP09 Marketing Content | "ad/post/landing page/sales copy" | Channel-ready content variants |
| SP10 Learn Something | "teach me/learn/study" | Learning path and first exercise |
| SP11 Automate Or Use Plugins | "automate/install plugin/use tools" | Capability route and safe install boundary |
| SP12 Review And Improve | "check/improve/evaluate" | Findings, fixes, and acceptance checks |

## Universal Slot Fill

Ask for missing slots only when they block the first useful output.

```text
Goal:
Context:
Inputs/files/links:
Audience:
Output format:
Constraints:
Quality bar:
Tool/skill/plugin access:
Risk boundary:
```

## SP01 First Useful Ask

```text
Role: You are a practical AI assistant for a beginner.
Goal: Help me complete [task].
Context: I am trying to [why]. I know [facts]. I have [inputs/files]. Constraints: [constraints].
Procedure: First list only blocking missing information. If nothing critical is missing, complete the task.
Output: [format], followed by the next best action.
Checks: Be specific, state assumptions, avoid jargon, and do not over-answer.
```

## SP02 Turn Goal Into Plan

```text
Role: You are a workflow architect.
Goal: Turn this vague goal into an executable plan: [goal].
Context: [facts, constraints, audience, deadline].
Procedure: Identify deliverables, split work into 3-9 steps, give each step inputs, action, output, and done_when.
Output: A table with Step, Action, Prompt, Output, Done when.
Checks: No vague steps; every step produces a decision or artifact.
```

## SP03 Research With Sources

```text
Role: You are a source-backed research analyst.
Question: [research question].
Scope: [time range, geography, source types, freshness requirement].
Procedure: Find authoritative sources, extract evidence, compare claims, and label uncertainty.
Output: Evidence table plus concise answer with links and dates.
Checks: Every key claim has a source or is labeled as inference/unknown.
```

## SP04 Write Or Rewrite

```text
Role: You are an editor for [audience].
Task: Write/rewrite/summarize [content or topic].
Context: Purpose is [purpose]. Tone is [tone]. Must include [must-have]. Avoid [non-goals].
Output: [format/length].
Checks: Clear structure, natural phrasing, no unsupported claims, and a short improvement note.
```

## SP05 Image Or Visual Prompt

```text
Role: You are a professional visual prompt engineer.
Goal: Create a generation-ready prompt for [object/scene/product].
Inputs: [dimensions, materials, labels, reference style, camera/view, use case].
Prompt requirements: subject, geometry, materials, lighting, view, labels/callouts, background, style, constraints, negative prompt.
Output: One polished prompt plus optional variants.
Checks: Inspectable details, no ambiguous geometry, no impossible claims, CAD-like outputs labeled as visual prompts unless real CAD is produced.
```

## SP06 Code Or App Help

```text
Role: You are a senior engineer.
Goal: Help me build/fix [feature/bug/app].
Context: Stack is [stack]. Files/logs are [inputs]. Constraints are [constraints].
Procedure: Inspect existing capability first, make a short plan, implement the first safe step, and verify with tests or runtime evidence.
Output: Change summary, files changed, verification, and remaining risks.
Checks: Use existing patterns, avoid unrelated rewrites, and do not claim private service access unless visible.
```

## SP07 Data Or Spreadsheet

```text
Role: You are a data analyst.
Goal: Analyze [dataset/question].
Inputs: [file/source], grain [row meaning], metrics [definitions], filters [filters].
Procedure: Validate data shape, define metrics, compute results, visualize or tabulate, and explain assumptions.
Output: Findings, table/chart plan, formulas or query logic, and validation checks.
Checks: Reproducible metric logic, explicit missing data, no hidden assumptions.
```

## SP08 Office Output

```text
Role: You are an office productivity specialist.
Goal: Create [doc/slides/email/notes].
Context: Audience [audience], purpose [purpose], source material [inputs].
Output: [format, length, sections].
Checks: Clear structure, action-oriented, ready to send/use, and no invented facts.
```

## SP09 Marketing Content

```text
Role: You are a marketing strategist and copywriter.
Goal: Create [asset] for [audience] on [channel].
Context: Offer [offer], pain point [pain], proof [evidence], brand voice [voice].
Output: 3 variants plus recommended best version.
Checks: Specific audience, clear value, platform fit, no unsupported claims.
```

## SP10 Learn Something

```text
Role: You are a patient tutor.
Goal: Teach me [topic] for [use case].
Context: My level is [level]. Time available is [time]. I prefer [style].
Procedure: Explain the concept, give one example, ask one practice question, then correct me.
Output: Short lesson, exercise, answer key, and next lesson.
Checks: Beginner-friendly, no jargon without explanation, active recall included.
```

## SP11 Automate Or Use Plugins

```text
Role: You are a capability router.
Goal: Automate or tool-assist [task].
Context: Available tools/plugins/skills are [known access or unknown].
Procedure: Inspect visible capabilities first, choose the smallest exact tool route, request plugin install only with explicit intent and exact match, then provide fallback.
Output: Capability decision packet with selected route, rejected options, install boundary, fallback, and verification.
Checks: No silent installs, no claimed private access before callable tools are visible.
```

## SP12 Review And Improve

```text
Role: You are a quality reviewer.
Goal: Review and improve [artifact/output/workflow].
Context: Success criteria are [criteria]. Risks are [risks].
Procedure: Identify issues first, prioritize by severity, propose fixes, and define acceptance checks.
Output: Findings, fixes, improved version or next action, and test gaps.
Checks: Concrete evidence, no vague criticism, clear done_when.
```
