---
name: gsdprogress
description: "Check project progress, show context, and route to next action (execute or plan). Use --forensic to append a 6-check integrity audit after the standard report."
allowed-tools: "Read Bash Grep Glob SlashCommand"
category: security-and-compliance
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/progress/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/progress/SKILL.md
---

<objective>
Check project progress, summarize recent work and what's ahead, then intelligently route to the next action - either executing an existing plan or creating the next one.

Provides situational awareness before continuing work.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/progress.md
</execution_context>

<process>
Execute the progress workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/progress.md end-to-end.
Preserve all routing logic (Routes A through F) and edge case handling.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/progress/SKILL.md`
