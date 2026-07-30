---
name: amend
description: "Amend the most recent commit with additional changes or an updated message."
category: engineering-core
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/commit-commands/commands/amend.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/commit-commands/commands/amend.md
---


Amend the most recent commit with additional changes or an updated message.

## Steps


1. Verify the last commit has not been pushed to remote:
2. If there are additional file changes to include:
3. Decide whether to update the commit message:
4. Verify the amended commit looks correct:
5. If the original commit was already pushed:

## Format


```
Amended Commit: <hash>
Message: <commit message>
Files Changed: <list>
Force Push Required: <yes|no>
```


## Rules

- Never amend a commit that has been pushed without explicit user approval.
- Always verify no unintended changes are included in the amendment.
- Preserve the original commit type (feat, fix, etc.) unless instructed otherwise.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/commit-commands/commands/amend.md`
