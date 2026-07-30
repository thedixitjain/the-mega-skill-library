---
name: c7-docs
description: "Fetch Context7 documentation for a library"
category: docs-and-knowledge-mgmt
source_repo: upstash/context7
source_path: "packages/pi/prompts/c7-docs.md"
source_url: https://github.com/upstash/context7/blob/HEAD/packages/pi/prompts/c7-docs.md
---


Look up documentation for `$1` using Context7.

1. Determine what to look up in the library's documentation from `${@:2}`.
2. Call the `resolve-library-id` tool with `libraryName="$1"` and what to look up as `query` to find the best matching library.
3. Call the `query-docs` tool with the selected library ID and what to look up as `query`.
4. Summarize the answer for the user with code examples from the returned snippets. Cite the Context7 library ID you used.

If `$1` is already in `/org/project` or `/org/project/version` format, skip library resolution and call `query-docs` directly.

---

**Source:** [`upstash/context7`](https://github.com/upstash/context7) → `packages/pi/prompts/c7-docs.md`
