---
name: gsdlist-workspaces
description: "List active GSD workspaces and their status"
allowed-tools: "Bash Read"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/gsd/skills/list-workspaces/SKILL.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/gsd/skills/list-workspaces/SKILL.md
---

<objective>
Scan `~/gsd-workspaces/` for workspace directories containing `WORKSPACE.md` manifests. Display a summary table with name, path, repo count, strategy, and GSD project status.
</objective>

<execution_context>
@${CLAUDE_PLUGIN_ROOT}/workflows/list-workspaces.md
@${CLAUDE_PLUGIN_ROOT}/references/ui-brand.md
</execution_context>

<process>
Execute the list-workspaces workflow from @${CLAUDE_PLUGIN_ROOT}/workflows/list-workspaces.md end-to-end.
</process>

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/gsd/skills/list-workspaces/SKILL.md`
