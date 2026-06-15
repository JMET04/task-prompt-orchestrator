# Common Plugin Directory

Use this directory during capability discovery when the current session has few installed plugins, the task mentions GitHub/Codex/OpenAI/app building/deployment/security, or a stronger plugin route would avoid manual work.

## Installation Rule

- Do not silently claim a plugin is installed or usable.
- If a required plugin is already enabled, use its skills or callable tools.
- If a required plugin is not visible, first try dynamic tool discovery for the named capability.
- If the user explicitly asks to use or install a missing plugin, list available install candidates and request installation only when there is an exact match.
- If no exact install candidate exists, continue with the best fallback and label the limitation.
- Treat connectors as session/account scoped; installed does not always mean authenticated or able to access the user's private data.

## Auto-Install Boundary

Use this boundary whenever a user wants the agent to install plugins for them:

| Gate | Required behavior |
|---|---|
| User intent | Treat "install/use the right plugin", "set up missing plugins", or a named missing plugin as explicit install intent. Treat vague usefulness as recommendation only. |
| Discovery | Run dynamic tool discovery first when available, because the plugin may already expose callable tools even if it is not obvious from the visible list. |
| Candidate lookup | Use the plugin install candidate list only after explicit install intent or an exact named missing plugin. |
| Exact match | Request installation only when the returned candidate exactly matches the requested plugin or capability. Do not request adjacent plugins just because they seem useful. |
| Consent surface | Use the platform's plugin install request flow. Do not present manual install steps as if installation already happened. |
| Re-scan | After installation, re-check visible tools, skills, and plugin metadata before using the plugin. |
| Fallback | If install is unavailable or not authenticated, continue with local tools, web sources, user-provided files, or built-in skills and label the limitation. |

## Sparse Plugin Environment Heuristic

Treat the session as plugin-sparse when one or more of these signals is true:

| Signal | Meaning | Recommended response |
|---|---|---|
| No domain plugin is visible for the task | The agent may have only local files, shell, web, and generic skills. | Use the local workflow first, then recommend the smallest matching install profile. |
| The task needs private SaaS state | Repository, issue tracker, logs, docs, email, drive, design, or analytics context may be unreachable. | Ask for or request the exact plugin only when the user wants that live context. |
| Tool discovery returns no callable tool | A plugin may be absent, disabled, or not exposed in this session. | Check install candidates only under explicit install intent; otherwise fall back. |
| User says "install what is missing" or "use the right plugin" | This is explicit install intent. | Run candidate lookup, request exact matches, then re-scan before execution. |
| User asks for a broad capability upgrade | This is usually recommendation intent, not task-specific install consent. | Present a compact profile such as Codex core coding or web app shipping. |

Do not install a broad profile just because it would be useful. Install/request only the exact plugin needed for the current user goal, unless the user explicitly asks to set up a whole profile.

## Plugin Install Tool Sequence

When install tools are available, use this sequence:

| Step | Tool/capability | Use when | Stop condition |
|---|---|---|---|
| 1 | Current session context | Always inspect visible plugins, skills, apps, and tools first. | A suitable enabled plugin/tool is already usable. |
| 2 | Dynamic tool discovery, such as `tool_search` | The capability may be lazy-loaded or hidden behind app/plugin metadata. | A callable tool is exposed for the task. |
| 3 | `list_available_plugins_to_install` | The user explicitly asked to use/install a missing plugin or named a missing plugin. | No exact candidate exists. |
| 4 | `request_plugin_install` | The candidate exactly matches the requested plugin/capability. | Installation request is submitted or declined. |
| 5 | Re-scan context and tool discovery | After a successful install request. | The expected plugin/tool/skill is visible or access is still blocked. |

Never call the install request for adjacent recommendations, broad "nice to have" plugins, or plugins that merely seem helpful. If the user asks for GitHub or Codex/OpenAI capability and the exact candidate is available, prefer the exact names `GitHub`, `OpenAI Developers`, `Codex Security`, `Build Web Apps`, or `Superpowers` from the starter pack below.

## Quick Capability Scan Workflow

Use this scan before recommending a new implementation from scratch:

| Step | Action | Output |
|---|---|---|
| 1 | Read visible session plugins, tools, skills, and task-specific app instructions. | Current capability shortlist |
| 2 | Run dynamic tool discovery for the task capability when the visible list is sparse or ambiguous. | Callable tool or confirmed gap |
| 3 | Run the local capability inventory script when installed skill or cached plugin-package coverage matters. | Installed skill inventory plus local plugin cache inventory |
| 4 | If the user explicitly asked to use/install a missing plugin, check install candidates. | Exact candidate match or no-match note |
| 5 | Request installation only for an exact match, then re-scan visible tools before execution. | Installed/available plugin route |
| 6 | If installation is unavailable, choose the strongest fallback and state the limitation. | Fallback execution route |

Local plugin cache inventory shows package presence and bundled skills, not live account authentication or callable connector availability. Always verify session-visible tools after install or before claiming a plugin can act.

## GitHub And Codex Common Install Directory

Use this directory when the user has few plugins installed and asks Codex to improve its own working ability, automatically use missing capabilities, install the right plugin, or handle GitHub/Codex/OpenAI engineering work with less manual setup.

For a tighter execution map, especially when deciding whether Codex may request installation, read `github_codex_common_plugin_directory.md`. That file is the canonical GitHub/Codex sparse-plugin install workflow; this section remains the broad directory and quick starter pack.

| Task signal | Exact install candidate to look for | Request only when | Primary capability gained | Fallback before or if unavailable |
|---|---|---|---|---|
| GitHub repo, issue, PR, review, branch, release, hosted checks, or CI status | GitHub | The task needs GitHub-hosted state or the user explicitly asks to use/install GitHub. | Repository/issue/PR/release/check context and repo-side actions. | Local `git`, GitHub CLI if authenticated, pasted issue/PR text, repository files. |
| OpenAI API, Agents SDK, Responses API, ChatGPT app, plugin/connector, model behavior, tool calling, API key setup | OpenAI Developers | The task needs current OpenAI platform behavior or the user asks to install/use OpenAI/Codex developer capability. | Official OpenAI development workflows, docs routing, API/app/key guidance. | Official OpenAI web docs, local SDK/package inspection, project examples. |
| Codex security, agent safety, threat model, secrets, auth, data access, dependency risk, webhook, sandbox, finding validation | Codex Security | The task is security-sensitive or the user asks for Codex security capability. | Security scans, threat modeling, finding discovery, validation, and fix guidance. | Local static analysis, dependency audit, manual security review. |
| Codex delivery discipline, planning, TDD, debugging, reusable engineering workflow | Superpowers | The work is broad/risky or the user asks Codex to work with stronger process automation. | Structured planning, TDD, debugging, and delivery loops. | Local checklist, tests, repo conventions, this orchestrator. |
| Web app coding, frontend implementation, browser debugging, responsive UI, app polish | Build Web Apps | The task is UI/app-building heavy or the user asks for Codex web-app capability. | Frontend build/debug/test workflows and browser verification guidance. | Local package scripts, Playwright, browser screenshots, framework docs. |
| GitHub CI plus external pipeline logs/config | CircleCI | The failure source is CircleCI or the user names CircleCI. | Build/config inspection and CI debugging. | Local config validation, GitHub checks, pasted logs. |
| Deploy preview or production web app/agent | Vercel, Netlify, Render, or Cloudflare | The repo targets that platform or the user names a target. | Platform deploy, preview, debug, monitor, or edge/worker capability. | Local build, platform CLI if installed, official docs. |
| Runtime error, production incident, log, trace, replay, or customer bug recording | Sentry, Datadog, or Jam | The task needs connected telemetry/recording context or the user names the tool. | Real issue/log/trace/session context. | Local logs, stack traces, screenshots, reproduction scripts. |

### Sparse-Session Auto-Install Policy

When plugins are sparse, apply this exact sequence:

| Step | Action | Allowed outcome |
|---|---|---|
| 1 | Name the smallest task-specific capability gap. | One missing plugin or one tightly scoped profile. |
| 2 | Check visible plugins/tools and dynamic tool discovery. | Use already-enabled capability if present. |
| 3 | If the user explicitly authorized install/use of missing plugins, call the install-candidate listing. | Candidate list or no-match result. |
| 4 | Match by exact plugin name from this directory, not by vague similarity. | `GitHub`, `OpenAI Developers`, `Codex Security`, `Superpowers`, `Build Web Apps`, or a task-named platform plugin. |
| 5 | Request installation through the platform install flow. | Install request submitted or user declines. |
| 6 | Re-scan visible tools/skills/plugins before execution. | Confirmed capability route or labeled fallback. |

Do not request a whole profile automatically. For broad upgrades, present the profile and ask/act only on the plugin that is necessary for the current task or explicitly requested by the user.

## GitHub And Codex Starter Pack

Use this as the default plugin shortlist when a user has few plugins installed and wants coding, repository, automation, app-building, or Codex/OpenAI work to become stronger.

| Need | Primary plugin to use/request | Add when | Fallback if unavailable | Verify after install |
|---|---|---|---|---|
| Repository inspection, PRs, issues, reviews, releases, CI status | GitHub | The workflow depends on GitHub-hosted state beyond local files. | Local `git`, GitHub CLI if authenticated, web repository pages, pasted issue/PR text. | Re-run tool discovery for GitHub issue/PR/repo tools and inspect a harmless repo query. |
| OpenAI APIs, Agents SDK, ChatGPT Apps, model/tool behavior, API keys | OpenAI Developers | The task asks for current OpenAI platform implementation or key setup. | Official OpenAI docs, local SDK inspection, examples in repo. | Re-run discovery for OpenAI docs/API/key tools and confirm the relevant skill is visible. |
| Codex-side security review, threat models, finding validation | Codex Security | The task changes auth, secrets, payments, data access, webhooks, dependencies, or execution sandboxing. | Local static analysis, dependency audit, manual threat model. | Re-run discovery for security scan/threat-model/fix-finding tools. |
| Frontend/web app build with browser verification | Build Web Apps | The task includes UI, React/Vite/Next, browser screenshots, responsive states, or app polish. | Local package scripts, Playwright, browser dev server, official docs. | Confirm frontend testing/debugging skills/tools are visible. |
| Structured delivery workflow, TDD, debugging discipline | Superpowers | The task is broad, risky, or benefits from explicit planning and verification loops. | Local plan and test checklist. | Confirm planning/TDD/debugging skills are visible. |
| Deploy/debug web apps and agents | Vercel, Netlify, Render, Cloudflare | The repo targets one of these hosting platforms or user asks for deploy/preview. | Local build, CLI if installed, platform docs. | Discover platform-specific deploy/debug tools before running deploy actions. |
| CI/CD inspection and fixes | CircleCI, GitHub | The failure is in hosted CI or pipeline configuration. | Local config validation and test reproduction. | Discover CI build/config tools and confirm project access. |
| Production error context | Sentry, Datadog, Jam | The task needs real errors, logs, traces, replay, or recording context. | Local logs, pasted stack traces, screenshots. | Discover issue/log/recording tools and run a read-only lookup. |
| Documents, spreadsheets, slides, reports | Documents, Spreadsheets, Presentations, Data Analytics | The deliverable must be a formatted artifact, dashboard, workbook, or report. | Local document libraries, markdown/CSV/HTML export. | Confirm artifact/render/export tools or bundled runtimes are visible. |

## Minimal Install Profiles

Use these profiles to recommend a compact set instead of a long plugin list when the user's plugin environment is sparse.

| Profile | Install/request first | Add only when the task needs it | Covers |
|---|---|---|---|
| Codex core coding | GitHub, OpenAI Developers, Codex Security, Superpowers | Build Web Apps, CircleCI, Sentry, Datadog | Repo context, OpenAI/Codex work, security review, structured delivery, CI and incident context |
| Web app shipping | GitHub, Build Web Apps, Vercel or Netlify or Render, Cloudflare | Supabase, Neon Postgres, Convex, Sentry | Frontend implementation, browser verification, deploy previews, backend/data, runtime errors |
| Agent/app platform | OpenAI Developers, GitHub, Cloudflare, Vercel | Supabase, Neon Postgres, Build Web Apps, Codex Security | OpenAI APIs, Agents SDK, ChatGPT apps, tool calling, app hosting, secrets/security |
| Data/report work | Data Analytics, Spreadsheets, Documents, Presentations | Deepnote, Google Drive, Build Web Data Visualization | Analysis, dashboards, workbooks, docs, decks, shareable reports |
| Product/design/creative | Product Design, Figma, Creative Production | Canva, Picsart, Fal, Shutterstock, Wix | Prototypes, design audits, campaign assets, image/video generation, licensed media |
| Team workspace | Google Drive, Slack, Gmail, Atlassian Rovo, Linear, Notion | Jam | Company knowledge, docs, tickets, messages, email, meeting/debug recordings |
| Research/finance/domain | Fiscal AI, Aiera, Public Equity Investing, Zotero, Hugging Face | Life Science Research, Midpage, Investment Banking | Filings, transcripts, citations, models/datasets, domain research |

## GitHub Task Map

| User intent | Capability route | Install candidate phrase |
|---|---|---|
| "Look at my repo/issue/PR" | GitHub plugin first, then local `git` and repo files. | GitHub |
| "Review this PR" | GitHub plugin for PR metadata plus local diff review when files are present. | GitHub |
| "Fix CI" | GitHub for checks/logs, CircleCI if the pipeline is CircleCI, local reproduction for code changes. | GitHub, CircleCI |
| "Create/publish release" | GitHub plugin when account/repo access is needed; local changelog/build checks first. | GitHub |
| "Sync issue to implementation plan" | GitHub issue context plus task workflow matrices and local code inspection. | GitHub |

## Codex/OpenAI Task Map

| User intent | Capability route | Install candidate phrase |
|---|---|---|
| "Build with OpenAI API" | OpenAI Developers plugin/skill, official docs fallback, local SDK inspection. | OpenAI Developers |
| "Make a ChatGPT app/plugin/connector" | OpenAI Developers plus plugin-creator/skill-creator when local capability packaging is required. | OpenAI Developers |
| "Scan installed plugins and skills" | Capability discovery matrix plus `scripts/capability_inventory.py`; use session context for plugins. | No install required unless a named plugin is missing |
| "Codex should choose tools automatically" | Capability discovery matrix, common plugin directory, integration boundary, and governance policy. | Superpowers, OpenAI Developers |
| "Security-scan this agent/app/workflow" | Codex Security first when available, otherwise local static/security review. | Codex Security |

## Engineering And Codex Core Plugins

| Plugin | Use when | Prefer over | Common fallback |
|---|---|---|---|
| GitHub | Inspect repositories, issues, pull requests, branches, diffs, reviews, CI, releases, or publish repository changes. | Manual web browsing or ad hoc `git` commands when API context is needed. | Local `git`, GitHub CLI if authenticated, web search, repository files. |
| OpenAI Developers | Build with OpenAI APIs, Agents SDK, ChatGPT Apps, API keys, model behavior, tool calling, or Responses/Assistants migration. | Unverified memory about current OpenAI APIs. | Official OpenAI docs via web, local examples, SDK inspection. |
| Codex Security | Run security scans, threat models, attack-path analysis, finding discovery, or fix security findings. | Generic code review for security-sensitive work. | Local static analysis, dependency scanners, manual review, official advisories. |
| Superpowers | Use structured planning, TDD, debugging, and software delivery workflows. | Loose task planning for complex implementation. | Local plan, tests, repo conventions. |
| Build Web Apps | Build, test, debug, or refine frontend web apps with browser verification. | Generic coding workflow for UI-heavy work. | Local package scripts, Playwright, browser screenshots, React/Vite docs. |
| Build iOS Apps | Build, run, test, or debug iOS apps with simulator workflows. | Raw `xcodebuild` shell commands for simulator tasks. | XcodeBuildMCP if available, Xcode CLI, project docs. |
| Build macOS Apps | Build, package, sign, debug, or instrument macOS apps. | Generic Swift/macOS advice. | Xcode CLI, SwiftPM, local logs. |
| Expo | Build, upgrade, debug, or deploy Expo/React Native apps. | Generic React Native guidance. | Expo CLI, local package scripts, official Expo docs. |
| Test Android Apps | Reproduce, inspect, screenshot, or profile Android app issues. | Generic Android advice without emulator evidence. | Android Studio/ADB, local Gradle tests. |

## Repo, Deployment, And Cloud Plugins

| Plugin | Use when | Prefer over | Common fallback |
|---|---|---|---|
| Vercel | Deploy or debug web apps and agents on Vercel. | Manual deployment guessing for Vercel projects. | Vercel CLI, project config, official docs. |
| Netlify | Deploy static sites/apps, preview builds, or debug Netlify releases. | Manual build upload instructions. | Netlify CLI, local build artifacts. |
| Render | Deploy, debug, monitor, or migrate apps on Render. | Generic hosting instructions. | Render dashboard/docs, local Docker/build checks. |
| Cloudflare | Work with Workers, Wrangler, Durable Objects, Agents SDK, or Cloudflare platform APIs. | Generic edge deployment advice. | Wrangler CLI, official docs, local config. |
| Supabase | Manage Supabase projects, tables, auth, storage, or Postgres-backed app work. | Manual SQL guessing for Supabase apps. | Supabase CLI, Postgres tools, local migrations. |
| Neon Postgres | Manage Neon Serverless Postgres projects and databases. | Generic cloud Postgres guidance. | `psql`, migrations, official Neon docs. |
| Convex | Add reactive backend, database, server functions, and type-safe app data layer. | Hand-rolled backend for Convex projects. | Local Convex CLI, project docs. |
| CircleCI | Inspect builds, debug CI, or edit CircleCI configs. | Manual CI log guessing. | Local config validation, CircleCI CLI, repository files. |
| Datadog | Investigate telemetry, logs, monitoring, and production signals. | Guessing from code alone for incidents. | Local logs, exported traces, dashboards provided by user. |
| Sentry | Inspect recent issues and events from Sentry. | Manual stack-trace reconstruction. | Local logs, error reports, source maps. |

## Workspace And Collaboration Plugins

| Plugin | Use when | Prefer over | Common fallback |
|---|---|---|---|
| Google Drive | Search or work with Drive, Docs, Sheets, or Slides. | Asking the user to paste everything manually. | Uploaded files, local exports, document tools. |
| Gmail | Draft, search, summarize, or work with email. | Generic email advice when mailbox context is needed. | User-pasted email text, local drafts. |
| Slack | Search channels, draft messages, summarize threads, or coordinate work. | Manual status reconstruction. | User-pasted thread, local notes. |
| Atlassian Rovo | Manage Jira/Confluence tasks, status, triage, and backlog from company knowledge. | Generic project-management prose. | Exported tickets/docs, local markdown plans. |
| Linear | Find and reference Linear issues and projects. | Manual issue tracking when Linear context is needed. | User-provided issue text, local task list. |
| Notion | Capture knowledge, synthesize research, or work with Notion pages. | Ad hoc markdown when Notion is the system of record. | Local markdown, exported pages. |
| Figma | Inspect, create, or implement design-system work from Figma. | Visual guessing from screenshots only. | Screenshots, local design tokens, manual CSS inspection. |
| Jam | Use screen recordings with console, network, and reproduction context. | Guessing bug reproduction steps. | User-provided video, logs, screenshots. |

## Data, Document, And Reporting Plugins

| Plugin | Use when | Prefer over | Common fallback |
|---|---|---|---|
| Data Analytics | Analyze product/business data, design KPIs, build dashboards, or generate analytics reports. | Manual chart prose for data-heavy work. | Local Python/R/SQL, spreadsheets, provided CSVs. |
| Deepnote | Explore data in notebooks or automate SQL/notebook workflows. | Local-only analysis when Deepnote workspace context matters. | Local notebooks, Python scripts. |
| Spreadsheets | Create, edit, analyze, visualize, or export spreadsheet workbooks. | Plain markdown tables for workbook deliverables. | Python openpyxl/pandas, CSV exports. |
| Documents | Create or edit Word/Google Docs-style artifacts. | Plain text when document formatting matters. | Local DOCX libraries, markdown export. |
| Presentations | Create, edit, render, verify, or export slide decks. | Static outline when a PPTX is required. | Local PPTX libraries, markdown outline. |
| Build Web Data Visualization | Build charts, dashboards, maps, UML, reports, and shareable visualizations. | Generic chart descriptions. | Local chart libraries, HTML, Python plotting. |

## Creative And Product Plugins

| Plugin | Use when | Prefer over | Common fallback |
|---|---|---|---|
| Creative Production | Explore campaign ideas, mood boards, product placements, ads, scenes, shots, and creative directions. | Generic creative brainstorming. | Local prompt library, image generation, web/image search. |
| Product Design | Turn product ideas into prototypes, flow audits, or interactive screenshots. | Generic product notes for prototype work. | Local frontend prototype, Figma/screenshots. |
| Canva | Create, edit, resize, or translate designs in Canva. | Manual design specs when Canva output is requested. | Local images, slides, or HTML mockups. |
| Picsart | Generate or edit images, video, and audio across creative models. | Generic image editing instructions. | Built-in image generation/editing, local image tools. |
| Fal | Run AI image, video, audio, 3D, training, and editing workflows. | Unspecified media generation routes. | Built-in image generation, local assets, other media plugins. |
| Shutterstock | Search or download licensed stock media. | Unlicensed web image reuse for commercial assets. | Public-domain/open-license sources, user assets. |
| Wix | Build or manage Wix sites, domains, eCommerce, CMS, or dashboard extensions. | Generic site instructions when Wix is the target. | Local web app, Wix docs. |
| Replit | Build, inspect, or deploy Replit apps. | Local scaffolding when the user wants Replit Agent. | Local app generation and dev server. |

## Finance, Research, And Domain Plugins

| Plugin | Use when | Prefer over | Common fallback |
|---|---|---|---|
| Fiscal AI | Research company fundamentals, filings, and market insights. | Unverified finance summaries. | SEC/issuer filings, web finance data, local models. |
| Aiera | Earnings calls, transcripts, events, and market commentary. | Manual transcript search. | Company IR pages, SEC filings, web search. |
| Public Equity Investing | Build investment memos, earnings analysis, valuation, catalysts, or thesis tracking. | Generic finance analysis. | Local models, filings, financial APIs. |
| Investment Banking | M&A, sponsor, capital markets, LevFin, restructuring, valuation, diligence, and pitch workflows. | Generic business writing for deal work. | Local spreadsheets, filings, company materials. |
| Life Science Research | Life-science evidence synthesis, datasets, biology, chemistry, structure, and clinical evidence. | General web search for scientific questions. | PubMed, papers, public datasets. |
| Hugging Face | Inspect models, datasets, Spaces, and research. | Guessing model metadata. | Hugging Face website/API, papers. |
| Zotero | Search library, export BibTeX, insert citations, or import references. | Manual citation tracking. | Local BibTeX, web sources, DOI lookup. |
| Midpage | Legal research, cases, statutes, regulations, and cited memos. | General legal web search. | Official court/statute sources, user-provided docs. |

## Auto-Install Decision Packet

Use this packet when a useful plugin is missing:

```text
Needed capability:
Best matching plugin:
Why current tools are insufficient:
Is the user explicitly asking to use/install it:
Install candidate checked:
Exact match found:
Requested installation:
Fallback if unavailable:
Validation after install:
```

Only request installation after exact candidate matching. After installation, re-scan visible tools and plugin skills before execution.
