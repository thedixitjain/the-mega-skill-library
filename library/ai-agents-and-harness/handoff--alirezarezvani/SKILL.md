---
name: handoff
description: "Compact the current conversation into a handoff document for another agent to pick up. References existing artifacts (PRDs, plans, ADRs, issues, commits, diffs) by path or URL instead of duplicating them. Use when user wants to hand off the conversation to a fresh agent or starts a new session that picks up prior work."
category: ai-agents-and-harness
source_repo: alirezarezvani/claude-skills
source_path: "engineering/handoff/skills/handoff/SKILL.md"
source_url: https://github.com/alirezarezvani/claude-skills/blob/HEAD/engineering/handoff/skills/handoff/SKILL.md
---


# Handoff

> Derived from [Matt Pocock's handoff](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) (MIT). Matt's no-duplication discipline preserved verbatim. Additions: tools + references + cs-* wrapper (see [references/companion_tooling.md](references/companion_tooling.md)).

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save it to a path produced by `mktemp -t handoff-XXXXXX.md` (read the file before you write to it).

Suggest the skills to be used, if any, by the next session.

Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.

## Sections

- **Goal of next session** (from user argument or inferred)
- **State of play** (what's done, what's blocking)
- **Open decisions** (what the next agent must decide)
- **Skills to use** (concrete list)
- **Artifacts** (paths/URLs to PRDs, plans, ADRs, issues, branches, PRs — do not duplicate)

## Tooling

See [references/companion_tooling.md](references/companion_tooling.md). Tools: template + dedup + recommender. Agent: `cs-handoff-author`. Command: `/cs:handoff`.

---

**Version:** 1.0.0
**Derived:** Matt Pocock (MIT) + this repo's wrapper

---

**Source:** [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) → `engineering/handoff/skills/handoff/SKILL.md`
