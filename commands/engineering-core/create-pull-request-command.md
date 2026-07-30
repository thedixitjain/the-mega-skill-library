---
name: create-pull-request-command
description: "Create a new branch, commit changes, and submit a pull request with automatic commit splitting"
allowed-tools: "Bash(git *), Bash(gh *), Bash(biome *)"
category: engineering-core
source_repo: davepoon/buildwithclaude
source_path: "plugins/all-commands/commands/create-pr.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/all-commands/commands/create-pr.md
---


# Create Pull Request Command

Create a new branch, commit changes, and submit a pull request.

## Behavior
- Creates a new branch based on current changes
- Formats modified files using Biome
- Analyzes changes and automatically splits into logical commits when appropriate
- Each commit focuses on a single logical change or feature
- Creates descriptive commit messages for each logical unit
- Pushes branch to remote
- Creates pull request with proper summary and test plan

## Guidelines for Automatic Commit Splitting
- Split commits by feature, component, or concern
- Keep related file changes together in the same commit
- Separate refactoring from feature additions
- Ensure each commit can be understood independently
- Multiple unrelated changes should be split into separate commits

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/all-commands/commands/create-pr.md`

**Also appears in:** `davepoon/buildwithclaude/plugins/commands-version-control-git/commands/create-pr.md`, `wesammustafa/Claude-Code-Everything-You-Need-to-Know/.claude/commands/pr.md`
