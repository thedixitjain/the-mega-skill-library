---
name: generate-api-docs
description: "Generate API documentation for endpoints"
allowed-tools: "Bash(find:*)"
category: docs-and-knowledge-mgmt
source_repo: ccplugins/awesome-claude-code-plugins
source_path: "plugins/generate-api-docs/commands/generate-api-docs.md"
source_url: https://github.com/ccplugins/awesome-claude-code-plugins/blob/HEAD/plugins/generate-api-docs/commands/generate-api-docs.md
---


## Context

- API routes: !`find . -path "*/routes/*" -name "*.js" -o -path "*/api/*" -name "*.js" | head -20`
- Current API files: @$ARGUMENTS

## Your task

Generate comprehensive API documentation including:

1. **Endpoint Overview**: Method, URL, purpose
2. **Parameters**: Query params, path params, request body
3. **Request Examples**: Sample requests with curl
4. **Response Examples**: Success and error responses
5. **Status Codes**: All possible HTTP status codes
6. **Authentication**: Required auth if applicable

Format as clear, readable documentation that can be used by other developers.

---

**Source:** [`ccplugins/awesome-claude-code-plugins`](https://github.com/ccplugins/awesome-claude-code-plugins) → `plugins/generate-api-docs/commands/generate-api-docs.md`
