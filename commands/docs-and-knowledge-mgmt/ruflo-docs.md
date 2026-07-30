---
name: ruflo-docs
description: "Generate or update documentation for a file, module, or the entire project"
category: docs-and-knowledge-mgmt
source_repo: ruvnet/ruflo
source_path: "plugins/ruflo-docs/commands/ruflo-docs.md"
source_url: https://github.com/ruvnet/ruflo/blob/HEAD/plugins/ruflo-docs/commands/ruflo-docs.md
---

$ARGUMENTS

Generate or update documentation using the document worker and drift detection.

**Full project**: `npx @claude-flow/cli@latest hooks worker dispatch --trigger document`
**Specific scope**: `npx @claude-flow/cli@latest hooks worker dispatch --trigger document --scope api`

Parse $ARGUMENTS to determine scope:
- If a file path is given, generate docs for that file
- If "api" is given, generate API documentation
- If no arguments, run full project documentation generation

Steps:
1. Analyze the target for public APIs and existing documentation
2. Detect drift between code and docs
3. Generate or update documentation
4. Report what was created or changed

---

**Source:** [`ruvnet/ruflo`](https://github.com/ruvnet/ruflo) → `plugins/ruflo-docs/commands/ruflo-docs.md`
