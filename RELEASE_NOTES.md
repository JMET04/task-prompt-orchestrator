# Release Notes

## 2026-06-15

- Improved `SKILL.md` trigger description so the skill activates for intake, plugin/skill scanning, sparse-plugin sessions, GitHub/Codex/OpenAI plugin routing, prompt routing, and professional deliverable workflows.
- Added the `Input Information Contract` to make required task inputs explicit before planning.
- Added `references/chinese_introduction.md` with a detailed Chinese explanation of the skill's features, implementation principles, and low-token behavior.
- Added a `SKILL.md` routing rule so the Chinese introduction is loaded only for documentation/explanation tasks, not during normal execution.
- Updated `agents/openai.yaml`:
  - `short_description`: `Collect task inputs and route expert workflows.`
  - `default_prompt`: asks for goal, inputs, constraints, available skills/plugins, and acceptance checks before routing.
- Validated with:
  - `quick_validate.py`
  - `validate_activation_surface.py --json`
  - `route_ai_workflow.py` capability/plugin routing smoke test
