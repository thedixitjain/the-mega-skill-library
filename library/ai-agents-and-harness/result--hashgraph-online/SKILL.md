---
name: result
description: "Show the stored final output for a finished Claude Code job in this repository. Args: [job-id]. Use when the user already has, or needs, a tracked job id."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/sendbird/cc-plugin-codex/skills/result/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/sendbird/cc-plugin-codex/skills/result/SKILL.md
---


# Claude Code Result

Use this skill when the user wants the stored final output for a finished Claude Code job.

Resolve `<plugin-root>` as two directories above this `SKILL.md` file. Always run the companion from that active plugin root:
`node "<plugin-root>/scripts/claude-companion.mjs" result $ARGUMENTS`

Supported arguments: `[job-id]`

Output:
- Present the full companion stdout exactly as returned.
- Do not summarize or condense it.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/sendbird/cc-plugin-codex/skills/result/SKILL.md`
