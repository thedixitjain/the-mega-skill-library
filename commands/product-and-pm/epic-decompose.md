---
name: epic-decompose
description: "Break an epic into task children without creating task branches."
category: product-and-pm
source_repo: affaan-m/ECC
source_path: "commands/epic-decompose.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/commands/epic-decompose.md
---
# /epic-decompose

Reconcile the task breakdown for one epic issue.

```bash
node scripts/github-coordination.js decompose <issue-number> --repo <owner/repo>
```

What this does:

1. Reads the epic issue body for task checklists and dependency references.
2. Stores the decomposition in the coordination block.
3. Leaves task branches out of the workflow.
4. Appends a concise audit comment.

Compatibility aliases:

- `/plan`
- `/prp-plan`

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `commands/epic-decompose.md`
