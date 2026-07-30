---
name: create-workflow
description: "Generate a YAML workflow from natural language"
category: general-purpose
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/community/llm-box/commands/create-workflow.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/community/llm-box/commands/create-workflow.md
---


# Create Workflow

Generate a YAML workflow file from a natural language description.

## Usage

```
/llm-box:create-workflow "<description>"
```

## Examples

```
/llm-box:create-workflow "Fetch the GitHub trending page and save to file"
/llm-box:create-workflow "Read package.json and generate release notes"
/llm-box:create-workflow "Fetch news from multiple sources and summarize with Ollama"
```

## What it does

1. Parses your natural language description
2. Generates a structured YAML workflow
3. Saves it to the current directory
4. Shows you the workflow steps

## Next steps

After creating a workflow, you can:
- Edit the YAML file manually to tweak things
- Run it with `/llm-box:run-workflow <filename>`
- Validate it with `/llm-box:validate-workflow <filename>`

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/community/llm-box/commands/create-workflow.md`
