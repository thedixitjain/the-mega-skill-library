---
name: fix-issue
description: "Automatically fix a GitHub issue by analyzing its description and implementing a solution."
category: general-purpose
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/fix-github-issue/commands/fix-issue.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/fix-github-issue/commands/fix-issue.md
---
Automatically fix a GitHub issue by analyzing its description and implementing a solution.

## Steps


1. Fetch the issue details using `gh issue view <number>`.
2. Analyze the issue:
3. Locate the relevant code:
4. Create a feature branch: `git checkout -b fix/<issue-number>-<short-desc>`.
5. Implement the fix:
6. Create a PR linking the issue:
7. Use `gh pr create` with the issue reference.

## Format


```
Issue: #<number> - <title>
Root Cause: <explanation>
Fix: <what was changed>
Files Modified: <list>
```


## Rules

- Always create a branch; never commit directly to main.
- Reference the issue number in the PR with "fixes #N" for auto-closing.
- Keep the fix minimal; do not refactor unrelated code.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/fix-github-issue/commands/fix-issue.md`
