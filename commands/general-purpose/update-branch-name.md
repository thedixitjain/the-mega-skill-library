---
name: update-branch-name
description: "Update current git branch name based on analysis of changes made"
allowed-tools: "Bash(git *)"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/all-commands/commands/update-branch-name.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/all-commands/commands/update-branch-name.md
---


# Update Branch Name

Follow these steps to update the current branch name:

1. Check differences between current branch and main branch HEAD using `git diff main...HEAD`
2. Analyze the changed files to understand what work is being done
3. Determine an appropriate descriptive branch name based on the changes
4. Update the current branch name using `git branch -m [new-branch-name]`
5. Verify the branch name was updated with `git branch`

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/all-commands/commands/update-branch-name.md`

**Also appears in:** `davepoon/buildwithclaude/plugins/commands-version-control-git/commands/update-branch-name.md`, `ccplugins/awesome-claude-code-plugins/plugins/update-branch-name/commands/update-branch-name.md`
