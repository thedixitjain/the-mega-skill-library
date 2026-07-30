---
name: p
description: "Prompt optimizer — rewrite this request into an optimized prompt (ultrathink), then carry it out"
category: prompt-engineering
source_repo: davepoon/buildwithclaude
source_path: "plugins/claude-prompt/commands/p.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/claude-prompt/commands/p.md
---


You are operating in **PROMPT OPTIMIZER** mode for Claude.

**Step 1 — Optimize.** Rewrite the request below into an optimized prompt that maximizes reasoning quality, applying these techniques:
1. **Structured context** — add explicit reasoning frameworks and step-by-step structure.
2. **Specificity** — turn vague asks into detailed, actionable requirements with clear success criteria.
3. **Meta-instructions** — add guidance that leverages extended thinking and planning.
4. **Skip-comments** — do NOT alter any text inside double quotes ("like this").

**Step 2 — Show it.** Output the rewritten prompt under a short `**Optimized prompt:**` heading.

**Step 3 — Execute.** Immediately carry out the optimized prompt in full.

Request to optimize and execute:

$ARGUMENTS

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/claude-prompt/commands/p.md`
