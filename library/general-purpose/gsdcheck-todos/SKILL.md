---
name: gsdcheck-todos
description: "List pending todos and select one to work on"
allowed-tools: "Read Write Bash AskUserQuestion"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/check-todos/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/check-todos/SKILL.md
---


<objective>
List all pending todos, allow selection, load full context for the selected todo, and route to appropriate action.

Routes to the check-todos workflow which handles:
- Todo counting and listing with area filtering
- Interactive selection with full context loading
- Roadmap correlation checking
- Action routing (work now, add to phase, brainstorm, create phase)
- STATE.md updates and git commits
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/check-todos.md
</execution_context>

<context>
Arguments: $ARGUMENTS (optional area filter)

Todo state and roadmap correlation are loaded in-workflow using `init todos` and targeted reads.
</context>

<process>
**Follow the check-todos workflow** from `@${CLAUDE_PLUGIN_ROOT}/workflows/check-todos.md`.

The workflow handles all logic including:
1. Todo existence checking
2. Area filtering
3. Interactive listing and selection
4. Full context loading with file summaries
5. Roadmap correlation checking
6. Action offering and execution
7. STATE.md updates
8. Git commits
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/check-todos/SKILL.md`
