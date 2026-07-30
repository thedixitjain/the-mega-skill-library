---
name: agent-deck-session
description: "Use at session start in a deck-bound workspace, or when the user asks for the deck status line / which deck is active."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/not-so-fat/agent-deck/skills/agent-deck-session/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/not-so-fat/agent-deck/skills/agent-deck-session/SKILL.md
---


# Agent Deck session opener

Once per conversation (or after bind changes):

1. `get_decks`
2. `bind_workspace` with the workspace root and a `deckId` — if `.agent-deck/use.json` exists, use its `deckId`
3. `get_session_binding`
4. Print **exactly one** line from `display_summary` (e.g. `◆ dev · 2 MCP · 0 keys · 1 playbooks`)

Do not repeat the status line every turn unless the user asks or the bind changes.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/not-so-fat/agent-deck/skills/agent-deck-session/SKILL.md`
