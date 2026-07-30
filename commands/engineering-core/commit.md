---
name: commit
description: "Create a git commit"
allowed-tools: "Bash(git add:*), Bash(git status:*), Bash(git commit:*)"
category: engineering-core
source_repo: anthropics/claude-code
source_path: "plugins/commit-commands/commands/commit.md"
source_url: https://github.com/anthropics/claude-code/blob/HEAD/plugins/commit-commands/commands/commit.md
---
## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task

Based on the above changes, create a single git commit.

You have the capability to call multiple tools in a single response. Stage and create the commit using a single message. Do not use any other tools or do anything else. Do not send any other text or messages besides these tool calls.

---

**Source:** [`anthropics/claude-code`](https://github.com/anthropics/claude-code) → `plugins/commit-commands/commands/commit.md`

**Also appears in:** `anthropics/claude-plugins-official/plugins/commit-commands/commands/commit.md`, `ccplugins/awesome-claude-code-plugins/plugins/commit-commands/commands/commit.md`
