---
name: brand-use
description: "List the available brands and switch which one is active for generation."
category: marketing-and-growth
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/design/brand-forge/commands/brand-use.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/design/brand-forge/commands/brand-use.md
---


# /brand-use

Switch the active brand in a multi-brand repo.

## Steps

1. **List brands** with `lib/brand.mjs` → `listBrands`. Show the current active slug
   (from `brand/.active`).
2. **If a slug was given**, verify it exists under `brands/<slug>/` (or is `brand`).
   If not, list the valid slugs and stop.
3. **Set active** by writing the slug to `brand/.active`.
4. **Confirm** by running `/brand-status` so the newly active kit is shown.

No network. Only reads/writes local profile files.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/design/brand-forge/commands/brand-use.md`
