---
name: fix-github-issue
description: "Analyze and fix a GitHub issue with comprehensive testing and verification"
allowed-tools: "Bash(gh *), Read, Edit, Write, Bash(git *)"
category: testing-and-qa
source_repo: davepoon/buildwithclaude
source_path: "plugins/all-commands/commands/fix-github-issue.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/all-commands/commands/fix-github-issue.md
---


Please analyze and fix the GitHub issue: $ARGUMENTS.

Follow these steps:

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message

Remember to use the GitHub CLI (`gh`) for all GitHub-related tasks.

---

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/all-commands/commands/fix-github-issue.md`

**Also appears in:** `davepoon/buildwithclaude/plugins/commands-version-control-git/commands/fix-github-issue.md`
