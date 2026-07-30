---
name: hookify-list
description: "List all configured hookify rules"
category: general-purpose
source_repo: affaan-m/ECC
source_path: "commands/hookify-list.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/commands/hookify-list.md
---
Find and display all hookify rules in a formatted table.

## Steps

1. Find all `.claude/hookify.*.local.md` files
2. Read each file's frontmatter:
   - `name`
   - `enabled`
   - `event`
   - `action`
   - `pattern`
3. Display them as a table:

| Rule | Enabled | Event | Pattern | File |
|------|---------|-------|---------|------|

4. Show the rule count and remind the user that `/hookify-configure` can change state later.

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `commands/hookify-list.md`
