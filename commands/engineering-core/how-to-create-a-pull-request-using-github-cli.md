---
name: how-to-create-a-pull-request-using-github-cli
description: "Guide for creating pull requests using GitHub CLI with proper templates and conventions"
allowed-tools: "Bash(gh *)"
category: engineering-core
source_repo: davepoon/buildwithclaude
source_path: "plugins/all-commands/commands/create-pull-request.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/all-commands/commands/create-pull-request.md
---


# How to Create a Pull Request Using GitHub CLI

This guide explains how to create pull requests using GitHub CLI in our project.

## Prerequisites

1. Install GitHub CLI if you haven't already:

   ```bash
   # macOS
   brew install gh

   # Windows
   winget install --id GitHub.cli

   # Linux
   # Follow instructions at https://github.com/cli/cli/blob/trunk/docs/install_linux.md
   ```

2. Authenticate with GitHub:
   ```bash
   gh auth login
   ```

## Creating a New Pull Request

1. First, prepare your PR description following the template in @.github/pull_request_template.md

2. Use the `gh pr create --draft` command to create a new pull request:

   ```bash
   # Basic command structure
   gh pr create --draft --title "✨(scope): Your descriptive title" --body "Your PR description" --base main 
   ```

   For more complex PR descriptions with proper formatting, use the `--body-file` option with the exact PR template structure:

   ```bash
   # Create PR with proper template structure
   gh pr create --draft --title "✨(scope): Your descriptive title" --body-file .github/pull_request_template.md --base main
   ```

## Best Practices

1. **PR Title Format**: Use conventional commit format with emojis

   - Always include an appropriate emoji at the beginning of the title
   - Use the actual emoji character (not the code representation like `:sparkles:`)
   - Examples:
     - `✨(supabase): Add staging remote configuration`
     - `🐛(auth): Fix login redirect issue`
     - `📝(readme): Update installation instructions`

2. **Description Template**: Always use our PR template structure from @.github/pull_request_template.md:

3. **Template Accuracy**: Ensure your PR description precisely follows the template structure:

   - Don't modify or rename the PR-Agent sections (`pr_agent:summary` and `pr_agent:walkthrough`)
   - Keep all section headers exactly as they appear in the template

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/all-commands/commands/create-pull-request.md`

**Also appears in:** `davepoon/buildwithclaude/plugins/commands-version-control-git/commands/create-pull-request.md`
