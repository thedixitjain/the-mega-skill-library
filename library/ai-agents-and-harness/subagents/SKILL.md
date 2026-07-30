---
name: subagents
description: "Use when a plan has parallel tasks and the harness supports dispatching subagents."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/ouonet/praxis/skills/subagents/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/ouonet/praxis/skills/subagents/SKILL.md
---

# Subagents

Fresh context per task. No session history.

## Dispatch: reference, don't copy
Subagents have file-read tools. Don't inline what they can read.

```
TASK: <one sentence>
FILES: <paths>
SPEC: <docs/staging/specs/...#anchor>
ACCEPTANCE: <test or cmd>
EXTRA: <only what's NOT in referenced files>
```

Pasting >10 lines from the spec? Stop - let the subagent read it.

Expand milestone -> atomic steps **at dispatch time**, not in the plan.

## Loop per task
implementer -> on DONE: spec-reviewer (matches spec?) -> quality-reviewer (`review`) -> mark complete, continue.
The coordinator marks `- [x]`, never the subagent.

## Status
- `DONE_WITH_CONCERNS` - address if correctness; note if observation.
- `NEEDS_CONTEXT` - supply the fact, re-dispatch.
- `BLOCKED` - diagnose (missing context / stronger model / too big / plan wrong). Never silently retry.

## Model
1-2 files mechanical -> cheap. Multi-file integration -> standard. Design/review -> strongest.

All done -> `review` whole diff -> `ship`.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/ouonet/praxis/skills/subagents/SKILL.md`
