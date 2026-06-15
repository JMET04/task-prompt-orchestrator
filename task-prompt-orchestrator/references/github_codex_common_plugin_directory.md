# GitHub And Codex Common Plugin Directory

Use this directory when a user has a sparse plugin setup and wants Codex to handle repository, coding, OpenAI, security, delivery, or automation work with stronger installed capabilities.

## Capability-First Workflow

| Step | Action | Evidence to record |
|---|---|---|
| 1 | Inspect visible session plugins, skills, tools, apps, and MCP capabilities. | Enabled route or confirmed gap. |
| 2 | Run dynamic tool discovery for the exact needed capability when available. | Callable tool found, or no callable tool. |
| 3 | Run `scripts/capability_inventory.py --include-common-plugin-directory` when local skill/cache inventory matters. | Local skills and cached plugin packages. |
| 4 | If the user explicitly asked to use/install missing plugins, list install candidates. | Exact candidate name or no exact match. |
| 5 | Request installation only for an exact match. | Install request submitted, declined, or unavailable. |
| 6 | Re-scan visible tools and skills before using the new plugin. | Confirmed callable route or labeled fallback. |

Do not claim a plugin can access private data until the current session exposes the relevant callable tool or connector and, when needed, authentication is available.

## Explicit Install Intent

Treat these as enough intent to check install candidates:

| User wording | Meaning |
|---|---|
| "install the missing plugin" | Broad install authorization for the current task only. |
| "use the right plugin automatically" | Check exact plugin candidates for the current task. |
| "set up GitHub/OpenAI/Codex plugins" | Check the named plugin candidates. |
| "if I do not have enough plugins, install what is needed" | Install only the smallest exact plugin for the active goal. |
| "use GitHub for this repo/PR/issue" when GitHub is missing | Check `GitHub` install candidate. |

Treat these as recommendation intent only:

| User wording | Meaning |
|---|---|
| "what plugins would help?" | Recommend a shortlist; do not request install. |
| "make this stronger someday" | Suggest a profile; do not request install. |
| "this could use GitHub" without an active GitHub task | Mention the option; continue with fallback. |

## GitHub And Codex Core Map

| Task signal | First exact candidate | Add only when needed | Main gain | Fallback |
|---|---|---|---|---|
| Repository, issue, PR, branch, release, GitHub Actions, review comments, hosted checks | GitHub | CircleCI for CircleCI pipelines | Repo-hosted context and repo-side actions. | Local `git`, GitHub CLI, pasted PR/issue text, repo files. |
| OpenAI API, Agents SDK, Responses API, ChatGPT Apps, plugin/connector creation, API keys, model/tool behavior | OpenAI Developers | Build Web Apps for UI, Cloudflare/Vercel for hosting | Current OpenAI developer workflows and official docs routing. | Official OpenAI docs, local SDK inspection, repo examples. |
| Codex agent safety, secrets, auth, permissions, dependency risk, threat model, finding validation | Codex Security | Sentry/Datadog for production evidence | Security scans, threat models, validation, and fix guidance. | Local static analysis, dependency audit, manual review. |
| Structured coding process, planning, TDD, debugging, reusable delivery loops | Superpowers | GitHub for repo state | Stronger planning, test, and debugging workflows. | Local plan, repo tests, this orchestrator. |
| Frontend app build, browser testing, responsive UI, app polish | Build Web Apps | Figma/Product Design for design source | Frontend implementation and browser verification. | Local package scripts, Playwright, screenshots. |
| Web app or agent deployment | Vercel, Netlify, Render, or Cloudflare | GitHub for repo integration | Preview/prod deploy and platform debugging. | Local build, platform CLI, official docs. |
| CI/CD failure | GitHub | CircleCI when the project uses CircleCI | Hosted checks, logs, and pipeline metadata. | Local reproduction, config validation, pasted logs. |
| Runtime incident, stack trace, customer bug recording | Sentry, Datadog, or Jam | GitHub for source context | Real telemetry, trace, replay, or recording context. | Local logs, screenshots, reproduction script. |

## Minimal Profiles

Use profiles for recommendations, but request only the exact plugin needed for the active goal unless the user explicitly asks to install a whole profile.

| Profile | Install/request first | Add only when the task needs it | Covers |
|---|---|---|---|
| Codex core coding | GitHub, OpenAI Developers, Codex Security, Superpowers | Build Web Apps, CircleCI, Sentry | Repo context, OpenAI/Codex work, security review, delivery discipline. |
| Web app shipping | GitHub, Build Web Apps, Vercel or Netlify or Render | Cloudflare, Supabase, Neon Postgres, Sentry | UI work, browser verification, deploy previews, backend, incidents. |
| Agent/app platform | OpenAI Developers, GitHub, Cloudflare or Vercel | Build Web Apps, Supabase, Codex Security | OpenAI APIs, Agents SDK, ChatGPT apps, tool calling, hosting. |
| Secure delivery | GitHub, Codex Security, Sentry or Datadog | CircleCI, Cloudflare | Code review, threat models, incidents, CI, edge/security posture. |

## Exact Candidate Rules

| Candidate | Request when | Do not request when |
|---|---|---|
| GitHub | The task needs GitHub-hosted repo/issue/PR/release/check context or the user named GitHub. | Local files and `git` are enough. |
| OpenAI Developers | The task needs current OpenAI platform implementation, API keys, Agents SDK, ChatGPT Apps, or plugin/connector guidance. | The task is generic prompting with no OpenAI platform dependency. |
| Codex Security | The task touches secrets, auth, private data, payments, webhooks, dependencies, sandboxing, or explicit security review. | The task is a normal low-risk code edit. |
| Superpowers | The user asks for stronger process automation, TDD, debugging discipline, or a broad risky build. | The task is small and already has a clear local workflow. |
| Build Web Apps | The task is UI/app-building heavy and needs browser verification. | The task is backend-only or document-only. |

## Install Decision Packet

Use this packet before requesting installation:

```text
Needed capability:
Visible enabled route:
Dynamic discovery result:
Local inventory result:
Exact candidate:
Why fallback is insufficient:
User install intent:
Install request:
Post-install re-scan:
Fallback if blocked:
```

If any field is unknown, resolve it before requesting installation unless the user explicitly asked for a recommendation instead of execution.
