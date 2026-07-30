---
name: epic-publish
description: "Publish a validated epic update back to the issue and local cache."
category: product-and-pm
source_repo: affaan-m/ECC
source_path: "commands/epic-publish.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/commands/epic-publish.md
---
# /epic-publish

Publish a validated coordination update to GitHub.

```bash
node scripts/github-coordination.js publish <issue-number> --repo <owner/repo>
```

What this does:

1. Re-validates the epic before publishing.
2. Updates the coordination block in the issue body.
3. Appends a concise publish comment.
4. Records the final local snapshot.

Compatibility aliases:

- `/pr`
- `/prp-pr`

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `commands/epic-publish.md`
