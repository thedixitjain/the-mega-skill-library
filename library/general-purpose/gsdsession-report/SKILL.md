---
name: gsdsession-report
description: "Generate a session report with token usage estimates, work summary, and outcomes"
allowed-tools: "Read Bash Write"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/session-report/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/session-report/SKILL.md
---

<objective>
Generate a structured SESSION_REPORT.md document capturing session outcomes, work performed, and estimated resource usage. Provides a shareable artifact for post-session review.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/session-report.md
</execution_context>

<process>
Execute the session-report workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/session-report.md end-to-end.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/session-report/SKILL.md`
