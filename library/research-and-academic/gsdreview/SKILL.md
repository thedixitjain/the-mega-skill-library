---
name: gsdreview
description: "Request cross-AI peer review of phase plans from external AI CLIs"
allowed-tools: "Read Write Bash Glob Grep"
category: research-and-academic
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/review/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/review/SKILL.md
---


<objective>
Invoke external AI CLIs (Gemini, Claude, Codex, OpenCode, Qwen Code, Cursor) to independently review phase plans.
Produces a structured REVIEWS.md with per-reviewer feedback that can be fed back into
planning via /gsd:plan-phase --reviews.

**Flow:** Detect CLIs → Build review prompt → Invoke each CLI → Collect responses → Write REVIEWS.md
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/review.md
</execution_context>

<context>
Phase number: extracted from $ARGUMENTS (required)

**Flags:**
- `--gemini` — Include Gemini CLI review
- `--claude` — Include Claude CLI review (uses separate session)
- `--codex` — Include Codex CLI review
- `--opencode` — Include OpenCode review (uses model from user's OpenCode config)
- `--qwen` — Include Qwen Code review (Alibaba Qwen models)
- `--cursor` — Include Cursor agent review
- `--all` — Include all available CLIs
</context>

<process>
Execute the review workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/review.md end-to-end.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/review/SKILL.md`
