---
name: agent-deck-setup
description: "Use when setting up Agent Deck, the MCP is disconnected, or the local daemon is down. Guides install/start with read-only checks; the user runs install commands."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/not-so-fat/agent-deck/skills/agent-deck-setup/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/not-so-fat/agent-deck/skills/agent-deck-setup/SKILL.md
---


# Agent Deck setup

1. Check `http://127.0.0.1:1110/health` (or `<mcp-url>/health` from `.agent-deck/use.json` if present).
2. If healthy, skip to the session skill / bind flow.
3. If down, tell the user to run:
   - `npm i -g agent-deck`
   - `agent-deck setup --client codex --start` (or `cursor` / `claude` for those hosts)
   - Restart the host so MCP reconnects.
4. Do not invent credentials, ports, or shell install pipelines. Keep guidance read-only; the user executes commands.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/not-so-fat/agent-deck/skills/agent-deck-setup/SKILL.md`
