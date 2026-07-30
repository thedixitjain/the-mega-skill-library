---
name: agents-020-agent-skill-authoring
description: "Authoring agent, skill, and command markdown for cross-harness portability"
category: ai-agents-and-harness
source_repo: wshobson/agents
source_path: ".cursor/rules/020-agent-skill-authoring.mdc"
source_url: https://github.com/wshobson/agents/blob/HEAD/.cursor/rules/020-agent-skill-authoring.mdc
---


# Authoring portable plugin content

This content ships to Claude Code, Codex CLI, Cursor, OpenCode, and Gemini CLI. The adapter
framework handles per-harness mechanics, but content choices affect portability.

## Frontmatter

- Agents: `name`, `description` (with "Use when…" trigger), `model: opus|sonnet|haiku|inherit`, optional `tools:`, optional `color:`.
- Skills: `name`, `description`. Other Anthropic SKILL.md fields are optional and respected only on Claude Code.
- Commands: `description`, `argument-hint`.

## Body

- Use action verbs, not tool-name vocabulary: prefer *"open the file"* over *"use the Read tool"*. The adapter rewrites a conservative set, but the unrewritten cases bleed through.
- Cap skill body at ~8 KB. Push longer reference material into `skills/<name>/references/` files. Codex will hard-truncate at 8 KB anyway.
- Don't name agents `default`, `worker`, or `explorer` — they collide with Codex built-ins.
- Don't reference `TodoWrite`, the `Task` spawn tool, or hooks as load-bearing — they don't exist in Codex or Cursor.

See `docs/authoring.md` for the full guide.

---

**Source:** [`wshobson/agents`](https://github.com/wshobson/agents) → `.cursor/rules/020-agent-skill-authoring.mdc`

**Also appears in:** `wshobson/agents/tools/adapters/cursor_rules/020-agent-skill-authoring.mdc`
