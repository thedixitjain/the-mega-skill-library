---
name: ecc-ecc-agent-data-home
description: "ECC Cursor memory boundary — keeps session data out of Claude Code's ~/.claude"
category: ai-agents-and-harness
source_repo: affaan-m/ECC
source_path: "scaffolds/cursor/rules/ecc-agent-data-home.mdc"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/scaffolds/cursor/rules/ecc-agent-data-home.mdc
---
# ECC agent data home (Cursor)

This project uses ECC with **isolated memory persistence** for Cursor:

- Default data root: `~/.cursor/ecc` (not `~/.claude`)
- Env var: `ECC_AGENT_DATA_HOME` (set automatically by ECC's Cursor `sessionStart` hook when hooks are wired)
- Project override: `.cursor/ecc-agent-data.json` → `agentDataHome`

If the user asks where ECC stored session context or learned skills, point them at `$ECC_AGENT_DATA_HOME/session-data/` and `$ECC_AGENT_DATA_HOME/skills/learned/`.

To **share** memory with Claude Code intentionally (not recommended for parallel use), set `ECC_AGENT_DATA_HOME` to `~/.claude` in the shell or in `.cursor/ecc-agent-data.json`.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `scaffolds/cursor/rules/ecc-agent-data-home.mdc`
