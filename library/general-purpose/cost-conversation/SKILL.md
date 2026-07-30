---
name: cost-conversation
description: "Per-conversation cost view — list every session in cost-tracking with started-at, message count, top model, and total cost"
allowed-tools: "Bash"
category: general-purpose
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-cost-tracker/skills/cost-conversation/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-cost-tracker/skills/cost-conversation/SKILL.md
---


# Cost per Conversation

`cost-report` and `cost-optimize` aggregate by **agent** and **model**. This skill aggregates by **conversation (session)** — a different lens that surfaces *which conversations cost the most*. Useful for retrospectives ("which sessions ran long on Opus?") and for evaluating whether a given project's session pattern is sustainable.

## When to use

- After multiple sessions, to see total spend per conversation.
- Before scoping a long session, to understand typical cost-per-conversation.
- For per-project rollups via `CONV_NAMESPACE=cost-tracking-<project>`.

## Steps

1. **Run the script** from anywhere:

   ```bash
   node plugins/ruflo-cost-tracker/scripts/conversation.mjs
   ```

   Optional env:
   - `CONV_FORMAT=json` — emit JSON instead of markdown
   - `CONV_LIMIT=20` — show only the most recent N conversations
   - `CONV_NAMESPACE=cost-tracking` — override target namespace

2. **Inspect the markdown table** — total cost across all conversations, per-tier rollup, then a per-session table (started-at, sessionId prefix, message count, top model, cost).

## Cross-references

- `cost-track` — the producer that populates `cost-tracking:session-*`
- `cost-report` — same data, per-agent / per-model lens
- `cost-trend` — drift across bench runs (different axis: corpus runs vs conversations)
- `cost-budget-check` — sums across conversations to evaluate the budget threshold

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-cost-tracker/skills/cost-conversation/SKILL.md`
