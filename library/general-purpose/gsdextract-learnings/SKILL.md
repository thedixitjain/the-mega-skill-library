---
name: gsdextract-learnings
description: "Extract decisions, lessons, patterns, and surprises from completed phase artifacts"
allowed-tools: "Read Write Bash Grep Glob Agent"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/extract_learnings/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/extract_learnings/SKILL.md
---

<objective>
Extract structured learnings from completed phase artifacts (PLAN.md, SUMMARY.md, VERIFICATION.md, UAT.md, STATE.md) into a LEARNINGS.md file that captures decisions, lessons learned, patterns discovered, and surprises encountered.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/extract-learnings.md
</execution_context>

Execute the extract-learnings workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/extract-learnings.md end-to-end.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/extract_learnings/SKILL.md`
