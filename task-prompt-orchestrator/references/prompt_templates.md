# Prompt Templates

Use these as compact building blocks. Adapt wording to the user's language and domain.

## Universal Execution Step

```text
Role: You are a senior operator for [domain].
Objective: Complete [single step] so that [business/user outcome].
Context: [brief project context, prior decisions, constraints].
Inputs: [files, data, user facts, previous step outputs].
Procedure:
1. Inspect the current state before assuming.
2. Apply the relevant domain method or template.
3. Produce the requested artifact.
4. Verify against the checks below.
Output format: [exact format, file path, table, code diff, prompt block, etc.].
Constraints: [scope limits, style, tools, safety, format].
Quality checks: [observable pass/fail conditions].
Handoff: Return [artifact/decision/summary] for [next step].
```

## Task Decomposition

```text
Role: You are a workflow architect.
Objective: Convert the user's goal into small executable steps.
Context: [optimized brief].
Procedure:
1. Identify the final deliverable and all required intermediate artifacts.
2. Split the work into steps with clear dependencies.
3. Assign each step a domain and prompt template.
4. Define done_when checks that can be verified from files, commands, outputs, or sources.
Output format: A table with id, purpose, inputs, action, template, output, done_when, handoff.
Quality checks: No step is vague; no step has multiple unrelated actions; every step has evidence-based completion criteria.
```

## Prompt Optimization

```text
Role: You are a prompt architect.
Objective: Rewrite the user's rough instruction into a precise execution prompt.
Context: [user request + constraints].
Procedure:
1. Preserve the user's real intent.
2. Add missing structure: role, objective, context, inputs, output format, constraints, quality bar.
3. Remove ambiguity, conflicting wording, and unnecessary decoration.
4. Keep assumptions explicit.
Output format: Provide the optimized prompt, then a short note listing assumptions.
Quality checks: The prompt is directly executable and contains enough context to avoid follow-up discovery.
```

## Image2 / Visual Generation

Before using this template, prefer the project-local Image2 packs in `D:\image2专业提示词库\prompts\`.

```text
Role: You are a professional visual director and production prompt engineer.
Objective: Generate or transform the reference image into [specific visual deliverable].
Reference handling: Preserve [must-keep elements]; change [editable elements].
Subject: [product/object/person/space/interface].
Use case: [packaging, CAD, ecommerce, poster, UI, architecture, industrial design, etc.].
Composition: [view angle, layout, hierarchy, framing].
Style: [brand/style/material/lighting/rendering].
Technical requirements: [aspect ratio, background, resolution intent, annotations, legibility].
Negative prompt: Avoid [distortions, fake text, wrong geometry, extra parts, artifacts].
Output checks: [what must be visible, aligned, readable, dimensionally plausible, brand-consistent].
```

## Research / Source Collection

```text
Role: You are a source-backed research analyst.
Objective: Gather reliable evidence for [question].
Scope: [time range, geography, industry, source types].
Procedure:
1. Search primary or authoritative sources first.
2. Record source title, URL, publisher, date, and claim supported.
3. Separate confirmed facts from inference.
4. Flag stale, conflicting, or weak evidence.
Output format: Evidence table plus concise synthesis.
Quality checks: Every material claim has a source; dates are explicit; no unsourced current facts.
```

## Code / Repo Work

```text
Role: You are a senior engineer working in the existing codebase.
Objective: Implement [change] with minimal unrelated churn.
Context: [repo, files, conventions, user constraints].
Procedure:
1. Inspect relevant files and tests first.
2. Follow local patterns and existing abstractions.
3. Make scoped edits.
4. Run targeted verification.
Output format: Changed files, behavior summary, verification result.
Quality checks: No unrelated rewrites; tests or checks cover the changed behavior; user changes are preserved.
```

## Review / Audit

```text
Role: You are a strict reviewer.
Objective: Find bugs, regressions, missing tests, or risk in [artifact].
Procedure:
1. Inspect the current artifact and relevant context.
2. Prioritize findings by severity.
3. Ground every finding in exact evidence.
4. Include test gaps and assumptions.
Output format: Findings first, then open questions, then brief summary.
Quality checks: No speculative findings; every issue has a concrete impact and location/source.
```

## Document / Report

```text
Role: You are a professional document editor.
Objective: Produce [document/report] for [audience].
Context: [source material, tone, purpose].
Procedure:
1. Extract the required facts and structure.
2. Organize into reader-friendly sections.
3. Preserve citations, numbers, and definitions.
4. Check consistency and completeness.
Output format: [Markdown, DOCX outline, table, memo, etc.].
Quality checks: Clear hierarchy; no unsupported claims; matches audience and format.
```

## Data / Spreadsheet

```text
Role: You are a data analyst.
Objective: Analyze [dataset] to answer [question].
Inputs: [tables, columns, files].
Procedure:
1. Validate schema, row counts, missing values, and units.
2. Compute metrics with explicit formulas.
3. Summarize findings and caveats.
4. Create tables/charts only when they clarify the answer.
Output format: [analysis table, chart, dashboard, workbook].
Quality checks: Reproducible calculations; denominators and filters stated; samples/truncation disclosed.
```
