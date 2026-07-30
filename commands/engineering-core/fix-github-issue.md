---
name: fix-github-issue
description: "Analyzes and fixes GitHub issues using a structured approach with GitHub CLI for issue details, implementing necessary code changes, running tests, and creating proper commit messages."
category: engineering-core
source_repo: ccplugins/awesome-claude-code-plugins
source_path: "plugins/fix-github-issue/commands/fix-github-issue.md"
source_url: https://github.com/ccplugins/awesome-claude-code-plugins/blob/HEAD/plugins/fix-github-issue/commands/fix-github-issue.md
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

**Source:** [`ccplugins/awesome-claude-code-plugins`](https://github.com/ccplugins/awesome-claude-code-plugins) → `plugins/fix-github-issue/commands/fix-github-issue.md`
