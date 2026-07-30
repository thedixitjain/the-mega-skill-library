---
name: ctx-doctor
description: "| Run context-mode diagnostics. Checks runtimes, hooks, FTS5, plugin registration, npm and marketplace versions. Trigger: /context-mode:ctx-doctor"
category: ai-agents-and-harness
source_repo: mksglu/context-mode
source_path: "skills/ctx-doctor/SKILL.md"
source_url: https://github.com/mksglu/context-mode/blob/HEAD/skills/ctx-doctor/SKILL.md
---
# Context Mode Doctor

Run diagnostics and display results directly in the conversation.

## Instructions

1. Call the `ctx_doctor` MCP tool directly. It runs all checks server-side and returns a plain-text status report.
2. Display the results verbatim — they are already formatted with plain-text status prefixes: `[OK]` PASS, `[FAIL]` FAIL, `[WARN]` WARN. Renderer-safe (no markdown task-list syntax) for cross-client compatibility (e.g., Z.ai GLM).
3. **Fallback** (only if MCP tool call fails): Derive the **plugin root** from this skill's base directory (go up 2 levels — remove `/skills/ctx-doctor`), then run with Bash:
   ```
   CLI="<PLUGIN_ROOT>/cli.bundle.mjs"; [ ! -f "$CLI" ] && CLI="<PLUGIN_ROOT>/build/cli.js"; node "$CLI" doctor
   ```
   Re-display results verbatim with the same `[OK]`/`[FAIL]`/`[WARN]` prefixes.

---

**Source:** [`mksglu/context-mode`](https://github.com/mksglu/context-mode) → `skills/ctx-doctor/SKILL.md`
