---
name: hookify-configure
description: "Enable or disable hookify rules interactively"
category: general-purpose
source_repo: affaan-m/ECC
source_path: "commands/hookify-configure.md"
source_url: https://github.com/affaan-m/ECC/blob/HEAD/commands/hookify-configure.md
---
Interactively enable or disable existing hookify rules.

## Steps

1. Find all `.claude/hookify.*.local.md` files
2. Read the current state of each rule
3. Present the list with current enabled / disabled status
4. Ask which rules to toggle
5. Update the `enabled:` field in the selected rule files
6. Confirm the changes

---

**Source:** [`affaan-m/ECC`](https://github.com/affaan-m/ECC) → `commands/hookify-configure.md`
