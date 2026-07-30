---
name: summary
description: "Quick one-line summary of today's Codex activity (cost shown if Admin key configured)"
allowed-tools: "Bash(node:*)"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/codex-hud/commands/summary.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/codex-hud/commands/summary.md
---


Run the summary command:

```bash
node "${CLAUDE_PLUGIN_ROOT}/dist/index.js" summary
```

Present the output as-is to the user. It provides a concise one-line summary of today's Codex usage including cost, tokens, sessions, and rate limits.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/codex-hud/commands/summary.md`
