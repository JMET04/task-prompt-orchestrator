# Release Notes

## 2026-06-15

- Improved `SKILL.md` trigger description so the skill activates for intake, plugin/skill scanning, sparse-plugin sessions, GitHub/Codex/OpenAI plugin routing, prompt routing, and professional deliverable workflows.
- Added the `Input Information Contract` to make required task inputs explicit before planning.
- Updated `agents/openai.yaml`:
  - `short_description`: `Collect task inputs and route expert workflows.`
  - `default_prompt`: asks for goal, inputs, constraints, available skills/plugins, and acceptance checks before routing.
- Validated with:
  - `quick_validate.py`
  - `validate_activation_surface.py --json`
  - `route_ai_workflow.py` capability/plugin routing smoke test

