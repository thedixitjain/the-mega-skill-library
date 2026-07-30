---
name: gsdnote
description: "Zero-friction idea capture. Append, list, or promote notes to todos."
allowed-tools: "Read Write Glob Grep"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/note/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/note/SKILL.md
---

<objective>
Zero-friction idea capture — one Write call, one confirmation line.

Three subcommands:
- **append** (default): Save a timestamped note file. No questions, no formatting.
- **list**: Show all notes from project and global scopes.
- **promote**: Convert a note into a structured todo.

Runs inline — no Task, no AskUserQuestion, no Bash.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/note.md
@${CLAUDE_PLUGIN_ROOT}/references/ui-brand.md
</execution_context>

<context>
$ARGUMENTS
</context>

<process>
Execute the note workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/note.md end-to-end.
Capture the note, list notes, or promote to todo — depending on arguments.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/note/SKILL.md`
