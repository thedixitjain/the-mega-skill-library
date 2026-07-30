---
name: gsdcleanup
description: "Archive accumulated phase directories from completed milestones"
allowed-tools: "Read Write Bash AskUserQuestion"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/cleanup/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/cleanup/SKILL.md
---

<objective>
Archive phase directories from completed milestones into `.planning/milestones/v{X.Y}-phases/`.

Use when `.planning/phases/` has accumulated directories from past milestones.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/cleanup.md
</execution_context>

<process>
Follow the cleanup workflow at @${CLAUDE_PLUGIN_ROOT}/workflows/cleanup.md.
Identify completed milestones, show a dry-run summary, and archive on confirmation.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/cleanup/SKILL.md`
