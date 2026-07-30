---
name: git-worktree-commands
description: "Creates git worktrees for all open PRs or specific branches, handling branches with slashes, cleaning up stale worktrees, and supporting custom branch creation for development."
category: engineering-core
source_repo: ccplugins/awesome-claude-code-plugins
source_path: "plugins/create-worktrees/commands/create-worktrees.md"
source_url: https://github.com/ccplugins/awesome-claude-code-plugins/blob/HEAD/plugins/create-worktrees/commands/create-worktrees.md
---


# Git Worktree Commands

This documentation provides two main bash scripts for Git worktree management:

## 1. Create Worktrees for All Open PRs
- Uses GitHub CLI to fetch open pull requests
- Creates git worktrees for each PR branch
- Handles branch names with slashes
- Includes an optional cleanup script for stale worktrees

## 2. Interactive Branch and Worktree Creation
- Prompts for a new branch name
- Validates branch name
- Creates a worktree in a `./tree/` directory
- Supports creating branches from different base commits

## Key Features
- Error handling
- Directory management
- Flexible branch creation options
- Streamlined Git workflow by making branch and worktree management more efficient

---

**Source:** [`ccplugins/awesome-claude-code-plugins`](https://github.com/ccplugins/awesome-claude-code-plugins) → `plugins/create-worktrees/commands/create-worktrees.md`
