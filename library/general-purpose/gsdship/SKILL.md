---
name: gsdship
description: "Create PR, run review, and prepare for merge after verification passes"
allowed-tools: "Read Bash Grep Glob Write AskUserQuestion"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/ship/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/ship/SKILL.md
---

<objective>
Bridge local completion → merged PR. After /gsd:verify-work passes, ship the work: push branch, create PR with auto-generated body, optionally trigger review, and track the merge.

Closes the plan → execute → verify → ship loop.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/ship.md
</execution_context>

Execute the ship workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/ship.md end-to-end.

<output_format>
When the ship workflow concludes (PR created and tracked), emit a Next Up continuation block following the pattern in `references/continuation-format.md`:

- Show ship status (e.g., `## ✓ Phase N / Milestone v1.x Shipped — PR #123`) with the PR URL
- Emit a `## ▶ Next Up` heading with the next command (`/gsd:next` if there's more in the milestone, `/gsd:complete-milestone` if this was the last phase)
- Use **`` `/clear` then: ``** before the command
- Include a parenthetical: *(`/clear` is safe — `/gsd:resume-work` restores position from `HANDOFF.json` if you change your mind)*
- Add an "Also available:" section with `/gsd:review` (cross-AI review) or PR-specific actions

PR creation is a clean boundary — review/merge happens out-of-band; the just-finished implementation conversation rarely informs the next phase. Suggesting `/clear` here keeps the next start small.
</output_format>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/ship/SKILL.md`
