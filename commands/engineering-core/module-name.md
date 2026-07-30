---
name: module-name
description: "Auto-document the entire codebase by generating module-level docs, function signatures, and API references."
category: engineering-core
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/codebase-documenter/commands/document-all.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/codebase-documenter/commands/document-all.md
---
Auto-document the entire codebase by generating module-level docs, function signatures, and API references.

## Steps


1. Scan the project structure to identify all source files and their organization.
2. For each module or directory:
3. For each public function or method:
4. Generate an API reference organized by module.
5. Create a dependency graph showing how modules relate.
6. Identify undocumented or poorly documented areas.
7. Output documentation in the project's preferred format (JSDoc, docstrings, etc.).

## Format


```
# Module: <name>
Purpose: <what this module does>
Exports: <list of public APIs>
Dependencies: <what it imports>
```


## Rules

- Follow existing documentation conventions in the project.
- Only document public/exported APIs, not internal helpers.
- Include real usage examples found in the codebase, not fabricated ones.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/codebase-documenter/commands/document-all.md`
