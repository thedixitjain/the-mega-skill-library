---
name: context7-use-context7
description: "Use Context7 MCP to fetch up-to-date documentation when unsure about library APIs, syntax, or behavior instead of guessing from training data."
category: rag-memory-knowledge
source_repo: upstash/context7
source_path: "plugins/cursor/context7/rules/use-context7.mdc"
source_url: https://github.com/upstash/context7/blob/HEAD/plugins/cursor/context7/rules/use-context7.mdc
---


When you're unsure about a library's API, syntax, configuration, or behavior, use Context7 to fetch current documentation rather than guessing from training data that may be outdated.

Use Context7 when:
- You're not confident about the exact API or syntax for a library
- The user asks about a specific version (e.g., "Next.js 15", "React 19")
- The library or framework has had recent major changes
- You need accurate code examples for a specific use case

You don't need to use Context7 for:
- Well-established language features (e.g., JavaScript array methods, Python builtins)
- Conversations where the user has already provided the relevant code or docs

See the `context7-docs-lookup` skill for detailed instructions on how to resolve libraries and fetch documentation.

---

**Source:** [`upstash/context7`](https://github.com/upstash/context7) → `plugins/cursor/context7/rules/use-context7.mdc`
