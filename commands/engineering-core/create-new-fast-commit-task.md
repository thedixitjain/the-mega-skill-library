---
name: create-new-fast-commit-task
description: "Automatically create and execute a git commit using the first suggested commit message"
allowed-tools: "Bash(git *)"
category: engineering-core
source_repo: davepoon/buildwithclaude
source_path: "plugins/all-commands/commands/commit-fast.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/all-commands/commands/commit-fast.md
---


# Create new fast commit task

This task uses the same logic as the commit task (.claude/commands/commit.md) but automatically selects the first suggested commit message without asking for confirmation.

- Generate 3 commit message suggestions following the same format as the commit task
- Automatically use the first suggestion without asking the user
- Immediately run `git commit -m` with the first message
- All other behaviors remain the same as the commit task (format, package names, staged files only)
- Do NOT add Claude co-authorship footer to commits

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/all-commands/commands/commit-fast.md`

**Also appears in:** `davepoon/buildwithclaude/plugins/commands-version-control-git/commands/commit-fast.md`
