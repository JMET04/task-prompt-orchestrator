# Package Manifest

Generated: 2026-06-15

## Package

- Repository staging path: `D:\github\task-prompt-orchestrator`
- Skill folder: `task-prompt-orchestrator/`
- Archive: `dist/task-prompt-orchestrator.zip`

## Included Runtime Files

- `task-prompt-orchestrator/SKILL.md`
- `task-prompt-orchestrator/agents/openai.yaml`
- `task-prompt-orchestrator/references/`
- `task-prompt-orchestrator/scripts/`

## Validation

Validated from the repository staging copy:

```text
Skill is valid!
activation surface ok: true
route_count: 13
starter_pack_count: 12
regression_count: 9
```

Routing smoke test:

```text
Input: 扫描已安装插件和skill，推荐GitHub和Codex常用插件并生成工作流
Top routes:
- capability-plugin-routing
- github-codex-openai
```

## GitHub Upload Status

Local repository packaging is prepared. Remote upload requires either:

- an existing GitHub repository URL to add as `origin`, or
- GitHub CLI / token / authenticated Git credentials that can create or push a repository.

