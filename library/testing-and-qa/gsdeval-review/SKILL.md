---
name: gsdeval-review
description: "Retroactively audit an executed AI phase's evaluation coverage — scores each eval dimension as COVERED/PARTIAL/MISSING and produces an actionable EVAL-REVIEW.md with remediation plan"
allowed-tools: "Read Write Bash Glob Grep Task AskUserQuestion"
category: testing-and-qa
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/eval-review/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/eval-review/SKILL.md
---

<objective>
Conduct a retroactive evaluation coverage audit of a completed AI phase.
Checks whether the evaluation strategy from AI-SPEC.md was implemented.
Produces EVAL-REVIEW.md with score, verdict, gaps, and remediation plan.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/eval-review.md
@${CLAUDE_PLUGIN_ROOT}/references/ai-evals.md
</execution_context>

<context>
Phase: $ARGUMENTS — optional, defaults to last completed phase.
</context>

<process>
Execute @${CLAUDE_PLUGIN_ROOT}/workflows/eval-review.md end-to-end.
Preserve all workflow gates.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/eval-review/SKILL.md`
