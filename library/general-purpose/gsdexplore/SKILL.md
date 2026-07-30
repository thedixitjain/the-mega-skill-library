---
name: gsdexplore
description: "Socratic ideation and idea routing — think through ideas before committing to plans"
allowed-tools: "Read Write Bash Grep Glob Task AskUserQuestion"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/explore/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/explore/SKILL.md
---

<objective>
Open-ended Socratic ideation session. Guides the developer through exploring an idea via
probing questions, optionally spawns research, then routes outputs to the appropriate GSD
artifacts (notes, todos, seeds, research questions, requirements, or new phases).

Accepts an optional topic argument: `/gsd:explore authentication strategy`
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/explore.md
</execution_context>

<process>
Execute the explore workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/explore.md end-to-end.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/explore/SKILL.md`
