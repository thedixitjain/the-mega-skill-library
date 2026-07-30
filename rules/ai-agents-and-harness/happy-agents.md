---
name: happy-agents
description: "When the user says sync to main or synt to main, they mean:"
category: ai-agents-and-harness
source_repo: slopus/happy
source_path: "AGENTS.md"
source_url: https://github.com/slopus/happy/blob/HEAD/AGENTS.md
---
# Agent Workflow

## Sync To Main

When the user says `sync to main` or `synt to main`, they mean:

1. Fetch `origin/main`.
2. Rebase the current branch on `origin/main`.
3. Push the current HEAD directly to `main` with a normal push, for example:
   `git push origin HEAD:main`

Do not force push for this workflow.

---

**Source:** [`slopus/happy`](https://github.com/slopus/happy) → `AGENTS.md`
