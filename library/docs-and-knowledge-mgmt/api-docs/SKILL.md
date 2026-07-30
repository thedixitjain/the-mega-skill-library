---
name: api-docs
description: "Generate API documentation from source code with JSDoc and OpenAPI support"
allowed-tools: "Bash(npx *) mcp__plugin_ruflo-core_ruflo__hooks_worker-dispatch Read Write Grep"
category: docs-and-knowledge-mgmt
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-docs/skills/api-docs/SKILL.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-docs/skills/api-docs/SKILL.md
---

Generate API documentation from TypeScript/JavaScript source:

1. **Scan exports**: Find all public functions, classes, and interfaces
2. **Extract JSDoc**: Parse `@param`, `@returns`, `@throws`, `@example` annotations
3. **Generate missing docs**: Add JSDoc for undocumented public APIs
4. **OpenAPI spec**: For HTTP endpoints, generate OpenAPI 3.0 definitions

Dispatch via MCP: `mcp__plugin_ruflo-core_ruflo__hooks_worker-dispatch({ trigger: "document", scope: "api" })`

Conventions:
- Every public export must have a JSDoc comment
- Include `@param` with type and description
- Include `@returns` with type and description
- Include `@throws` for known error conditions
- Include `@example` for non-obvious usage

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-docs/skills/api-docs/SKILL.md`
