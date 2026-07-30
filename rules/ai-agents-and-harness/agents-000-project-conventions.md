---
name: agents-000-project-conventions
description: "claude-agents marketplace project conventions"
category: ai-agents-and-harness
source_repo: wshobson/agents
source_path: ".cursor/rules/000-project-conventions.mdc"
source_url: https://github.com/wshobson/agents/blob/HEAD/.cursor/rules/000-project-conventions.mdc
---


# claude-agents conventions

This is a multi-harness plugin marketplace. Source lives under `plugins/`; per-harness
artifacts (`.codex/`, `.cursor-plugin/`, `.opencode/`, `commands/`) are generated.

- Don't hand-edit anything under `.codex/`, `.cursor-plugin/`, `.opencode/`, or top-level `commands/`, `agents/`, `skills/` — regenerate via `make generate HARNESS=<x>`.
- Python tooling: `uv` (package manager), `ruff` (lint/format), `ty` (type check). Do not use pip/mypy/black.
- Plugin files: `plugins/<name>/{.claude-plugin/plugin.json, agents/*.md, skills/<name>/SKILL.md, commands/*.md}`. Auto-discovered.
- Cursor reads `.claude/skills/` and `.claude/agents/` directly — no separate `.cursor/skills/` is generated.

## Never

- Never commit secrets or hardcode credentials.
- Never hand-edit generated registries (`.agents/plugins/marketplace.json`, `.cursor-plugin/`) — plugin PRs register the plugin in `.claude-plugin/marketplace.json`, then run `make generate-all` (see CONTRIBUTING.md).
- Never run destructive git operations (force-push, reset --hard, branch -D) without explicit ask.

See `docs/authoring.md` for the portable-content style guide.

---

**Source:** [`wshobson/agents`](https://github.com/wshobson/agents) → `.cursor/rules/000-project-conventions.mdc`

**Also appears in:** `wshobson/agents/tools/adapters/cursor_rules/000-project-conventions.mdc`
