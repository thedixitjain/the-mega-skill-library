---
name: create-workflow
description: "Generate an n8n workflow JSON from a natural language description of the automation."
category: mcp-and-integrations
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/n8n-workflow/commands/create-workflow.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/n8n-workflow/commands/create-workflow.md
---
Generate an n8n workflow JSON from a natural language description of the automation.

## Steps


1. Parse the automation description:
2. Design the workflow node graph:
3. Generate the n8n workflow JSON:
4. Add error handling:
5. Add workflow metadata:
6. Test the workflow structure for validity.
7. Provide setup instructions for required credentials.

## Format


```json
{
  "name": "<workflow name>",
  "nodes": [...],
  "connections": {...},
```


## Rules

- Use the latest n8n node types and API formats.
- Include credential placeholders, never hardcode secrets.
- Add error handling nodes for production workflows.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/n8n-workflow/commands/create-workflow.md`
