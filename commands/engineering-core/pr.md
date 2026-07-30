---
name: pr
description: "Create a pull request from the current branch."
category: engineering-core
source_repo: alirezarezvani/claude-skills
source_path: ".claude/commands/git/pr.md"
source_url: https://github.com/alirezarezvani/claude-skills/blob/HEAD/.claude/commands/git/pr.md
---


## Variables

TARGET_BRANCH: $1 (defaults to `main`)
SOURCE_BRANCH: current branch (`git branch --show-current`)

## Workflow

1. Ensure `/review` and `/security-scan` have passed locally.
2. Confirm `ci-quality-gate` workflow succeeded for `SOURCE_BRANCH`.
3. Create the PR using GitHub CLI:
   ```bash
   gh pr create \
     --base "$TARGET_BRANCH" \
     --head "$SOURCE_BRANCH" \
     --title "<Conventional PR title>" \
     --body-file .github/pull_request_template.md
   ```
   If no template exists, provide a summary referencing Context, Testing, and Security results.
4. Add labels (`gh pr edit --add-label "status: in-review"`).
5. Share the PR link with reviewers and ensure at least one human approval is obtained.

---

**Source:** [`alirezarezvani/claude-skills`](https://github.com/alirezarezvani/claude-skills) → `.claude/commands/git/pr.md`
