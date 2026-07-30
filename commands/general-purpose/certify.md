---
name: certify
description: "Full quality certification with badge"
category: general-purpose
source_repo: wshobson/agents
source_path: "plugins/plugin-eval/commands/certify.md"
source_url: https://github.com/wshobson/agents/blob/HEAD/plugins/plugin-eval/commands/certify.md
---


Run the complete PluginEval certification pipeline (all three layers + Elo ranking) and assign a quality badge.

This takes 15-20 minutes and uses your Max plan for all LLM calls.

## Running

```bash
cd plugins/plugin-eval
uv run plugin-eval certify {argument} --output markdown
```

---

**Source:** [`wshobson/agents`](https://github.com/wshobson/agents) → `plugins/plugin-eval/commands/certify.md`
