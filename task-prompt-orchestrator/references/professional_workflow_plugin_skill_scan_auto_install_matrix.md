# Professional Workflow Plugin Skill Scan Auto Install Matrix

Use this matrix when a workflow must scan installed skills, enabled plugins, connectors, visible tools, MCP/app capabilities, local scripts, cached plugin packages, or GitHub/Codex/OpenAI common plugin directories before choosing, requesting, installing, invoking, or falling back from a plugin route.

Use this for capability-aware orchestration, sparse-plugin sessions, automatic plugin recommendation, exact install-candidate decisions, and post-install verification. Do not use it to silently install broad plugin profiles, claim unavailable private access, bypass user consent, request adjacent plugins without exact match, or replace platform install/authentication gates.

## SESSCP - Session Capability Scan

| Code | Workflow question | Workflow use |
|---|---|---|
| SESSCP01 | What visible session capabilities exist? | List enabled plugins, connectors, apps, tools, MCP servers, built-in tools, and named skills visible in the current turn. |
| SESSCP02 | What task capability is actually needed? | Translate the user's goal into a narrow capability such as GitHub PR access, OpenAI API guidance, deployment, telemetry, docs, data, or design. |
| SESSCP03 | What capability is already usable? | Prefer a visible callable tool, enabled plugin skill, local script, or bundled reference when it directly fits. |
| SESSCP04 | What capability is only listed but not callable? | Mark plugin presence, skill metadata, cached package, or app description separately from live callable access. |
| SESSCP05 | What authentication or account access may be required? | Identify private repo, SaaS, telemetry, email, drive, payment, or workspace access that requires connector auth. |
| SESSCP06 | What is safe to do read-only? | Prefer read-only discovery, local inventory, docs lookup, or no-side-effect checks before requesting install or mutation. |
| SESSCP07 | What should not be inferred? | Do not infer access to private data, repo state, tickets, logs, docs, files, or account settings from plugin names alone. |
| SESSCP08 | What current limitation should be stated? | Label missing plugin, hidden tool, unauthenticated connector, stale cache, or local-only fallback. |
| SESSCP09 | What evidence proves the capability exists? | Record visible tool names, plugin names, skill paths, dynamic discovery result, or successful harmless lookup. |
| SESSCP10 | What session capability artifact should be produced? | Create capability shortlist, gap note, selected route, or install-decision precheck. |

## SKLSCN - Local Skill Scan

| Code | Workflow question | Workflow use |
|---|---|---|
| SKLSCN01 | Which local skill roots should be scanned? | Use configured skill roots, system skills, personal skills, and plugin skill caches when local inventory matters. |
| SKLSCN02 | Which skill metadata matters? | Capture skill name, description, path, plugin prefix, trigger terms, and relevant reference/script assets. |
| SKLSCN03 | Which skill matches the task directly? | Prefer exact domain skills over generic orchestration when the trigger and scope align. |
| SKLSCN04 | Which skills are partial matches? | Keep adjacent skills as fallback or support routes without treating them as the main capability. |
| SKLSCN05 | Which duplicate skills need care? | Resolve duplicate names by path, plugin prefix, freshness, and scope before selecting one. |
| SKLSCN06 | Which skill instructions must be read? | Read the selected skill's `SKILL.md` completely before using it, then load only relevant references. |
| SKLSCN07 | Which local scripts can accelerate execution? | Prefer bundled scripts for deterministic inventory, validation, conversion, or repeated operations. |
| SKLSCN08 | What skill limits should be recorded? | Note when a skill provides guidance only, lacks live connector access, or requires external auth. |
| SKLSCN09 | How should skill scan output be filtered? | Filter by capability keyword, plugin family, task domain, or needed artifact to avoid context overload. |
| SKLSCN10 | What skill-scan artifact should be produced? | Create installed-skill inventory, selected-skill rationale, or rejected-skill list. |

## PLGCCH - Local Plugin Cache

| Code | Workflow question | Workflow use |
|---|---|---|
| PLGCCH01 | Which cached plugin packages exist locally? | Scan local plugin cache metadata to understand installed packages and bundled skills. |
| PLGCCH02 | What does plugin cache prove? | Treat it as package presence and bundled metadata, not live session enablement or authentication. |
| PLGCCH03 | What plugin fields should be captured? | Capture display name, version, description, category, apps, MCP servers, skills, and path. |
| PLGCCH04 | Which cache entry maps to the task? | Match by exact plugin name, task signal, app, MCP server, or bundled skill. |
| PLGCCH05 | What cache entry is stale or irrelevant? | Ignore old, disabled, unrelated, backup, or uncallable packages unless they explain available skills. |
| PLGCCH06 | How should cache and session visibility be reconciled? | Prefer session-visible callable tools over local cache; use cache as evidence for recommendations only. |
| PLGCCH07 | What common directory should be attached? | Include GitHub/Codex/OpenAI common plugin directory when the task involves engineering plugin routing. |
| PLGCCH08 | What package risk matters? | Flag unknown source, outdated version, excessive permission surface, or unclear connector auth. |
| PLGCCH09 | How should plugin cache be queried? | Use local inventory script query filters rather than broad manual cache inspection when possible. |
| PLGCCH10 | What plugin-cache artifact should be produced? | Create cache inventory, plugin metadata table, or cache-versus-session comparison. |

## TOOLDY - Dynamic Tool Discovery

| Code | Workflow question | Workflow use |
|---|---|---|
| TOOLDY01 | Is dynamic tool discovery available? | Use tool discovery when a capability may be lazy-loaded or hidden behind plugin/app metadata. |
| TOOLDY02 | What query should be sent? | Query the exact capability, plugin name, domain, or tool action needed by the active task. |
| TOOLDY03 | What result means the capability is callable? | Treat returned callable tool schemas or exposed MCP tools as stronger than directory recommendations. |
| TOOLDY04 | What result means install may be needed? | If no callable route exists and the user has install intent, proceed to install-candidate lookup. |
| TOOLDY05 | How should adjacent tool results be handled? | Use adjacent tools only as fallback or support, not as installation basis. |
| TOOLDY06 | What discovery evidence should be kept? | Record search query, returned tools, chosen tool, no-match result, or capability gap. |
| TOOLDY07 | When should discovery be repeated? | Re-run after installation, auth changes, tool exposure changes, or context transition. |
| TOOLDY08 | What should not be discovered dynamically? | Do not probe private account data, perform side effects, or call mutation tools during discovery. |
| TOOLDY09 | How should discovery shape the plan? | Update route, prompt brief, tool sequence, and fallback before execution. |
| TOOLDY10 | What dynamic-discovery artifact should be produced? | Create callable-tool shortlist, no-match note, or post-install re-scan record. |

## GHCODX - GitHub Codex Directory Match

| Code | Workflow question | Workflow use |
|---|---|---|
| GHCODX01 | Does the task need GitHub? | Use GitHub when repo-hosted issues, PRs, reviews, releases, branches, checks, or actions context is required. |
| GHCODX02 | Does the task need OpenAI Developers? | Use OpenAI Developers for OpenAI APIs, Agents SDK, ChatGPT Apps, connectors, API keys, or current platform behavior. |
| GHCODX03 | Does the task need Codex Security? | Use Codex Security for secrets, auth, data access, threat modeling, scans, dependency risk, or finding validation. |
| GHCODX04 | Does the task need Superpowers? | Use Superpowers for structured planning, TDD, debugging, broad risky implementation, or delivery process discipline. |
| GHCODX05 | Does the task need Build Web Apps? | Use Build Web Apps for frontend implementation, browser verification, responsive UI, or web app polish. |
| GHCODX06 | Does the task need deployment plugins? | Match Vercel, Netlify, Render, or Cloudflare when the target platform or deploy workflow is explicit. |
| GHCODX07 | Does the task need CI or runtime evidence? | Match GitHub/CircleCI for hosted checks, Sentry/Datadog/Jam for incidents, logs, traces, or recordings. |
| GHCODX08 | Does the task need workspace artifact plugins? | Match Documents, Spreadsheets, Presentations, Data Analytics, Google Drive, Slack, or Notion when those artifacts or systems are central. |
| GHCODX09 | Does the task need platform-specific app building? | Match Build iOS Apps, Build macOS Apps, Expo, Test Android Apps, Cloudflare, or OpenAI Developers by target stack. |
| GHCODX10 | What GitHub/Codex directory artifact should be produced? | Create exact plugin candidate, starter profile recommendation, or directory-match explanation. |

## OPAINV - OpenAI Codex Capability Route

| Code | Workflow question | Workflow use |
|---|---|---|
| OPAINV01 | What OpenAI/Codex task is being attempted? | Classify API build, model selection, tool calling, ChatGPT app, connector, skill, plugin, key setup, or eval work. |
| OPAINV02 | What official/current source is required? | Use OpenAI Developers or official docs for current API behavior, product rules, and key flows. |
| OPAINV03 | What local source should be inspected first? | Inspect repo code, SDK package versions, lockfiles, examples, and existing app configuration before changing implementation. |
| OPAINV04 | What Codex-side capability is needed? | Route to skill-creator, plugin-creator, openai-docs, security, frontend, deployment, or testing workflows as appropriate. |
| OPAINV05 | What API-key flow is safe? | Use approved key picker/confirmation tools when available; never print, invent, or persist secrets outside confirmed destinations. |
| OPAINV06 | What model/tool behavior needs verification? | Verify against official docs, local SDK types, tests, or small safe requests before locking a workflow. |
| OPAINV07 | What app/plugin creation boundary applies? | Distinguish skill creation, ChatGPT app creation, connector install, MCP server creation, and external hosting. |
| OPAINV08 | What OpenAI fallback is acceptable? | Use official web docs, local package inspection, examples, and conservative patterns when plugin access is unavailable. |
| OPAINV09 | What OpenAI route should not be used? | Avoid stale memory, unofficial snippets, unsupported APIs, manual secret handling, or broad install requests. |
| OPAINV10 | What OpenAI/Codex artifact should be produced? | Create OpenAI route plan, plugin need statement, doc-source note, or implementation checklist. |

## SPARSE - Sparse Plugin Policy

| Code | Workflow question | Workflow use |
|---|---|---|
| SPARSE01 | Is the session plugin-sparse for this task? | Treat it as sparse when the needed domain plugin is absent, no callable tool appears, or private SaaS state is unreachable. |
| SPARSE02 | What is the smallest missing capability? | Name one exact plugin or one tight profile; avoid broad capability shopping. |
| SPARSE03 | What can be done before installing? | Use local files, shell, web, visible tools, user-provided materials, and existing skills to make progress. |
| SPARSE04 | What install intent did the user provide? | Distinguish explicit install/use authorization from general interest or recommendation requests. |
| SPARSE05 | What recommendation can be made without install? | Provide a compact profile and why it helps, but do not trigger install flow without explicit intent. |
| SPARSE06 | What profile fits GitHub/Codex work? | Recommend GitHub, OpenAI Developers, Codex Security, Superpowers, and Build Web Apps as a core coding profile when asked broadly. |
| SPARSE07 | What profile fits web shipping? | Recommend GitHub, Build Web Apps, deployment target, backend/data, and telemetry plugins when shipping apps. |
| SPARSE08 | What profile fits data/docs/product work? | Recommend Data Analytics, Spreadsheets, Documents, Presentations, Google Drive, Product Design, or Figma based on deliverable. |
| SPARSE09 | What should not be auto-installed? | Do not request an entire profile, adjacent plugin, or speculative future plugin unless the user asked for that profile. |
| SPARSE10 | What sparse-session artifact should be produced? | Create capability gap, one-plugin install candidate, or profile recommendation. |

## EXACTM - Exact Match Gate

| Code | Workflow question | Workflow use |
|---|---|---|
| EXACTM01 | What exact candidate name is required? | Use exact plugin names such as GitHub, OpenAI Developers, Codex Security, Build Web Apps, Superpowers, or named platform plugin. |
| EXACTM02 | What is the user's requested name? | Normalize spelling, aliases, and task wording while preserving the specific requested capability. |
| EXACTM03 | What install candidates were returned? | Compare returned candidate ids, labels, and tool types against the exact needed capability. |
| EXACTM04 | Is an adjacent candidate sufficient? | Treat adjacent candidates as fallback recommendations, not install targets, unless the user approves that exact plugin. |
| EXACTM05 | What if multiple exact-looking candidates exist? | Prefer plugin over connector when both match; otherwise pick the candidate that matches the explicit user request. |
| EXACTM06 | What if no exact candidate exists? | Do not request install; continue with fallback and label missing plugin. |
| EXACTM07 | What if the plugin is already installed? | Do not request install; re-scan tools and use the enabled route if callable. |
| EXACTM08 | What if the candidate needs account auth? | Request or note authentication only through the platform flow; do not claim private data access yet. |
| EXACTM09 | What exact-match evidence should be recorded? | Record requested capability, returned exact candidate, rejected adjacent options, and decision. |
| EXACTM10 | What exact-match artifact should be produced? | Create install gate decision, exact candidate rationale, or no-match fallback note. |

## REQINS - Request Install Flow

| Code | Workflow question | Workflow use |
|---|---|---|
| REQINS01 | Is plugin install tooling available? | Use the platform install-list and install-request tools only when present in the current session. |
| REQINS02 | Has the user explicitly authorized install? | Proceed only when user named the missing plugin or asked to use/install missing capabilities. |
| REQINS03 | What installation reason should be shown? | Provide one concise reason tied to the active task and exact missing capability. |
| REQINS04 | What candidate fields are required? | Pass the returned plugin or connector id and tool type exactly as provided. |
| REQINS05 | What should not happen in parallel? | Do not call install request in parallel with other tools; submit it as a distinct action. |
| REQINS06 | What if the user declines? | Respect decline, continue fallback, and avoid repeated prompts unless scope changes. |
| REQINS07 | What if install is queued or pending? | Pause plugin-dependent actions, continue local work if safe, and re-scan later. |
| REQINS08 | What if install succeeds but tools are missing? | Re-run dynamic discovery, check app auth, and fall back if no callable route appears. |
| REQINS09 | What install decision must be documented? | Record intent, candidate, exact match, request result, and fallback path. |
| REQINS10 | What install artifact should be produced? | Create installation request packet, post-request status, or user-facing capability note. |

## POSTIN - Post Install Rescan

| Code | Workflow question | Workflow use |
|---|---|---|
| POSTIN01 | What must be re-scanned after install? | Re-check visible plugins, tools, MCP/app capabilities, skills, and dynamic discovery results. |
| POSTIN02 | What harmless proof should be run? | Run a read-only lookup, metadata call, schema inspection, or tool discovery confirmation when available. |
| POSTIN03 | What authentication state changed? | Identify whether account connection, permission grant, workspace selection, or repo access is still needed. |
| POSTIN04 | What route should be selected now? | Switch to the new callable plugin route only after it is visible and appropriate. |
| POSTIN05 | What stale assumptions should be cleared? | Replace pre-install guesses with current tool schemas, capabilities, and access limits. |
| POSTIN06 | What fallback remains needed? | Keep local or web fallback for unavailable scopes, missing auth, or partial plugin coverage. |
| POSTIN07 | What user-facing update is needed? | Briefly report installed/available route, unresolved access needs, and next action. |
| POSTIN08 | What should not be done immediately? | Do not perform destructive or private-data actions without task-specific confirmation and normal safety gates. |
| POSTIN09 | What post-install evidence should be saved? | Record callable tool name, skill path, harmless lookup result, or no-access status. |
| POSTIN10 | What post-install artifact should be produced? | Create re-scan report, route update, or plugin readiness note. |

## PLGFBK - Plugin Fallback

| Code | Workflow question | Workflow use |
|---|---|---|
| PLGFBK01 | What fallback can solve the active task? | Use local repo files, shell tools, web search, official docs, local scripts, or user-provided exports. |
| PLGFBK02 | What fallback is only partial? | Label missing private repo, issue, PR, logs, docs, email, drive, design, or analytics state. |
| PLGFBK03 | What fallback is safer than installing? | Use local read-only inspection for small tasks where plugin install would add unnecessary permission surface. |
| PLGFBK04 | What fallback needs user-provided data? | Ask for exported logs, links, screenshots, pasted issue text, or files when connector access is unavailable. |
| PLGFBK05 | What official source should replace a plugin? | Use primary docs, public APIs, standards, filings, or authoritative pages for current public facts. |
| PLGFBK06 | What fallback should not be used? | Avoid scraping private systems, guessing account state, fabricating tool output, or bypassing auth. |
| PLGFBK07 | What fallback output label is needed? | Mark fallback as local-only, public-only, unauthenticated, approximate, or pending connector access. |
| PLGFBK08 | When should fallback become an install recommendation? | Recommend install after repeated blockage, private-state need, or clear productivity gain. |
| PLGFBK09 | How should fallback be validated? | Run local tests, compare against provided evidence, cite official sources, or ask for confirmation. |
| PLGFBK10 | What fallback artifact should be produced? | Create limitation note, workaround plan, or install recommendation for later. |

## AUTOPL - Auto Plugin Use Policy

| Code | Workflow question | Workflow use |
|---|---|---|
| AUTOPL01 | When may the agent choose a plugin automatically? | Use an already enabled, callable, least-privilege plugin when it directly fits the current task. |
| AUTOPL02 | When may the agent request installation? | Request install only after explicit install intent, exact candidate match, and no already callable route. |
| AUTOPL03 | What should the agent optimize before acting? | Refine the brief, select capability route, define safety gates, and choose minimal tool sequence. |
| AUTOPL04 | What consent is required for side effects? | Follow normal approval and safety rules for writes, deploys, payments, emails, account changes, or publishing. |
| AUTOPL05 | What capability should be preferred? | Prefer the narrowest exact plugin/tool over broad profiles, generic web search, or manual reimplementation. |
| AUTOPL06 | What should be avoided with many plugins installed? | Avoid unnecessary tool calls, over-routing, and slow plugin hops when local context is enough. |
| AUTOPL07 | What should be avoided with few plugins installed? | Avoid claiming incapability too early; scan skills, tool discovery, local scripts, and common directory first. |
| AUTOPL08 | How should plugin choice be explained? | State selected route and key limitation briefly when it affects output quality or access. |
| AUTOPL09 | How should plugin routing improve over time? | Add recurring gaps to common directory, skill routes, scripts, or index entries after validation. |
| AUTOPL10 | What auto-use artifact should be produced? | Create route decision, tool plan, or reusable plugin selection rule. |

## PLGAUD - Plugin Capability Audit

| Code | Workflow question | Workflow use |
|---|---|---|
| PLGAUD01 | What decisions must be auditable? | Capture capability scan, selected plugin/tool, rejected options, install gate, fallback, and validation evidence. |
| PLGAUD02 | What evidence is enough for installed skills? | Record skill name, path, trigger match, and instruction file read. |
| PLGAUD03 | What evidence is enough for enabled plugins? | Record visible plugin name, callable tool/schema, MCP/app capability, or successful read-only call. |
| PLGAUD04 | What evidence is enough for install decisions? | Record user intent, exact candidate, candidate source, request result, and post-install re-scan. |
| PLGAUD05 | What risks should be logged? | Note auth gap, permission surface, private data limits, side-effect risk, cost, rate limits, and stale sources. |
| PLGAUD06 | What validation should close the loop? | Run validator, harmless lookup, test, source check, or user acceptance depending on task type. |
| PLGAUD07 | What should be added to indexes? | Add recurring plugin route, exact candidate rule, fallback, or capability scan pattern to the relevant directory. |
| PLGAUD08 | What should be removed from claims? | Remove unsupported access claims, broad automation promises, or outdated plugin names. |
| PLGAUD09 | What review cadence is useful? | Review common plugin directory after plugin list changes, major platform changes, or repeated task failures. |
| PLGAUD10 | What audit artifact should be produced? | Create capability audit packet, install log, or plugin directory maintenance note. |
