---
name: gsdfast
description: "Execute a trivial task inline — no subagents, no planning overhead"
allowed-tools: "Read Write Edit Bash Grep Glob"
category: ai-agents-and-harness
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/fast/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/fast/SKILL.md
---


<objective>
Execute a trivial task directly in the current context without spawning subagents
or generating PLAN.md files. For tasks too small to justify planning overhead:
typo fixes, config changes, small refactors, forgotten commits, simple additions.

This is NOT a replacement for /gsd:quick — use /gsd:quick for anything that
needs research, multi-step planning, or verification. /gsd:fast is for tasks
you could describe in one sentence and execute in under 2 minutes.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/fast.md
</execution_context>

<process>
Execute the fast workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/fast.md end-to-end.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/fast/SKILL.md`
