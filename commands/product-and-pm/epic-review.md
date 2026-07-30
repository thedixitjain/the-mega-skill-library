---
name: epic-review
description: "Mark epic review requested, approved, or changes requested."
category: product-and-pm
source_repo: affaan-m/ECC
source_path: "commands/epic-review.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/commands/epic-review.md
---
# /epic-review

Coordinate review state for an epic issue.

```bash
node scripts/github-coordination.js review <issue-number> --repo <owner/repo> --review approved
```

What this does:

1. Updates the review state in the coordination block.
2. Syncs review labels to GitHub.
3. Records the review outcome in an audit comment.
4. Keeps the local cache aligned with the issue body.

Compatibility aliases:

- `/review-pr`
- `/code-review`

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `commands/epic-review.md`
