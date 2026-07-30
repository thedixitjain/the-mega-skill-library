---
name: shipwright-projects
description: "List and manage existing Shipwright projects"
category: ai-agents-and-harness
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/ai-agency/shipwright/commands/shipwright-projects.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/ai-agency/shipwright/commands/shipwright-projects.md
---


# /shipwright-projects

List and manage projects previously built with Shipwright.

## Steps

1. Scan the current directory and common project locations for Shipwright-generated projects (identified by `.shipwright` config or `product-agent` metadata).
2. Display a table of projects with name, stack, creation date, and status.
3. Offer actions: open, rebuild, enhance, or view build logs.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/ai-agency/shipwright/commands/shipwright-projects.md`
