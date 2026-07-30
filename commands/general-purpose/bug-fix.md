---
name: bug-fix
description: "Systematic workflow for fixing bugs including issue creation, branch management, and PR submission"
allowed-tools: "Bash(git *), Bash(gh *)"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/all-commands/commands/bug-fix.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/all-commands/commands/bug-fix.md
---


Understand the bug: $ARGUMENTS

Before Starting:
- GITHUB: create an issue with a short descriptive title.
- GIT: checkout a branch and switch to it.

Fix the Bug

On Completion:
- GIT: commit with a descriptive message.
- GIT: push the branch to the remote repository.
- GITHUB: create a PR and link the issue.

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/all-commands/commands/bug-fix.md`

**Also appears in:** `davepoon/buildwithclaude/plugins/commands-version-control-git/commands/bug-fix.md`
