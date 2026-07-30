---
name: runapi-models
description: ">- List and compare RunAPI models by modality, service, or action."
category: mcp-and-integrations
source_repo: wshobson/agents
source_path: "plugins/runapi-mcp/commands/models.md"
source_url: https://github.com/wshobson/agents/blob/HEAD/plugins/runapi-mcp/commands/models.md
---


# RunAPI Models

List current RunAPI models from the embedded catalog.

## Instructions

1. Interpret `$ARGUMENTS` as a modality, service, action, or free-form filter.
2. Call `mcp__runapi__list_models` with the narrowest matching filter.
3. Present a compact table with model slug, service, action, modality, and required fields.
4. If the user asks about one model, call `mcp__runapi__get_model_info`; include service and action when the row is already known.
5. If the user asks about cost, call `mcp__runapi__check_pricing`.

Keep output concise.

---

**Source:** [`wshobson/agents`](https://github.com/wshobson/agents) → `plugins/runapi-mcp/commands/models.md`
