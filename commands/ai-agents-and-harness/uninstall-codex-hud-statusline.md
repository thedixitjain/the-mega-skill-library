---
name: uninstall-codex-hud-statusline
description: "Remove the codex-hud statusline integration (restores your previous statusline)"
allowed-tools: "Bash(node:*)"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/codex-hud/commands/uninstall.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/codex-hud/commands/uninstall.md
---


# Uninstall Codex HUD statusline

Remove the statusline integration. If a previous statusline was saved during setup, it is restored automatically.

```bash
node "${CLAUDE_PLUGIN_ROOT}/dist/index.js" uninstall-statusline
```

Report the output to the user. Then remind them:

- Restart Claude Code or run `/reload-plugins` for the change to take effect.
- This only removes the statusline integration. To remove the plugin entirely afterwards, run `/plugin uninstall codex-hud`.
- The stored configuration (including any saved Admin API key) lives at `~/.claude/plugins/codex-hud/config.json` — delete that file too if they want a clean slate.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/codex-hud/commands/uninstall.md`
