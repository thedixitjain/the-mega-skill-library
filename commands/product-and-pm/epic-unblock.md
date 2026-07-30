---
name: epic-unblock
description: "Sweep blocked epic issues and reopen anything whose dependencies are closed."
category: product-and-pm
source_repo: affaan-m/ECC
source_path: "commands/epic-unblock.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/commands/epic-unblock.md
---
# /epic-unblock

Sweep blocked epics whose declared dependencies are complete.

```bash
node scripts/github-coordination.js unblock --repo <owner/repo>
```

What this does:

1. Scans epic issues in the repository.
2. Checks each blocked epic's dependency list.
3. Moves fully unblocked epics to ready.
4. Updates labels, comments, and local snapshots.

Compatibility aliases:

- `/loop-status`

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `commands/epic-unblock.md`
