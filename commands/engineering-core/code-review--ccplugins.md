---
name: code-review
description: "Perform a comprehensive code review of recent changes"
allowed-tools: "Bash(git diff:*), Bash(git log:*)"
category: engineering-core
source_repo: ccplugins/awesome-claude-code-plugins
source_path: "plugins/code-review/commands/code-review.md"
source_url: https://github.com/ccplugins/awesome-claude-code-plugins/blob/HEAD/plugins/code-review/commands/code-review.md
---


## Context

- Current git status: !`git status`
- Recent changes: !`git diff HEAD~1`
- Recent commits: !`git log --oneline -5`
- Current branch: !`git branch --show-current`

## Your task

Perform a comprehensive code review focusing on:

1. **Code Quality**: Check for readability, maintainability, and adherence to best practices
2. **Security**: Look for potential vulnerabilities or security issues
3. **Performance**: Identify potential performance bottlenecks
4. **Testing**: Assess test coverage and quality
5. **Documentation**: Check if code is properly documented

Provide specific, actionable feedback with line-by-line comments where appropriate.

---

**Source:** [`ccplugins/awesome-claude-code-plugins`](https://github.com/ccplugins/awesome-claude-code-plugins) → `plugins/code-review/commands/code-review.md`
