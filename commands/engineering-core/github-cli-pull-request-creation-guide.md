---
name: github-cli-pull-request-creation-guide
description: "Provides comprehensive PR creation guidance with GitHub CLI, enforcing title conventions, following template structure, and offering concrete command examples with best practices."
category: engineering-core
source_repo: ccplugins/awesome-claude-code-plugins
source_path: "plugins/create-pull-request/commands/create-pull-request.md"
source_url: https://github.com/ccplugins/awesome-claude-code-plugins/blob/HEAD/plugins/create-pull-request/commands/create-pull-request.md
---


# GitHub CLI Pull Request Creation Guide

This guide provides comprehensive instructions for creating pull requests using GitHub CLI.

## Prerequisites
- Installing GitHub CLI
- Authenticating with GitHub

## Key Features
- Detailed instructions for creating pull requests
- Best practices for PR titles and descriptions
- Example commands for PR management
- Tips for using templates
- Additional GitHub CLI PR commands

## Example PR Creation Command
```bash
gh pr create --title "✨(scope): Your descriptive title" --body-file <(echo -e "## Issue\n\n- resolve:\n\n## Why is this change needed?\nYour description here.") --base main --draft
```

## Best Practices
- Use consistent template structure
- Follow conventional commit formats
- Maintain clear, structured pull request descriptions
- Include proper scope and descriptive titles

---

**Source:** [`ccplugins/awesome-claude-code-plugins`](https://github.com/ccplugins/awesome-claude-code-plugins) → `plugins/create-pull-request/commands/create-pull-request.md`
