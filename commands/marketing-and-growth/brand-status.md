---
name: brand-status
description: "Print the active brand kit summary plus setup and preflight status, on demand (the same checks the SessionStart hook runs)."
category: marketing-and-growth
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/design/brand-forge/commands/brand-status.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/design/brand-forge/commands/brand-status.md
---


# /brand-status

Show the current brand state at any time — reuses the same emitters as the
SessionStart hook, so the output matches what loads at session start.

## Steps

1. Set `BRAND_FORGE_ROOT` to the plugin root (`${CLAUDE_PLUGIN_ROOT}`).
2. From the repo root, run each emitter and print its output:

   ```bash
   for f in "${CLAUDE_PLUGIN_ROOT}"/lib/context/*; do bash "$f"; done
   ```

3. If nothing prints, there's no brand profile yet — suggest `/brand-new`.

The emitters cover: the active kit (name, palette, fonts, tone), a setup nudge, and
a raster preflight warning (only when the opt-in raster engine is enabled). No network.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/design/brand-forge/commands/brand-status.md`
