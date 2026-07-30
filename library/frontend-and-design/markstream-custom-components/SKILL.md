---
name: markstream-custom-components
description: "Override Markstream node renderers and add trusted custom tags across Vue, React, Svelte, and Angular using scoped or renderer-local mappings."
allowed-tools: "[claude, cursor, gemini, codex]"
category: frontend-and-design
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/markstream-custom-components/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/markstream-custom-components/SKILL.md
---


# Markstream Custom Components

## Overview

Customize specific Markstream nodes or trusted custom tags without replacing the parser or leaking global renderer state. Read [references/patterns.md](references/patterns.md) first.

## When to Use

Use to replace built-ins such as `image`, `link`, `code_block`, `mermaid`, or `inline_code`; render trusted tags such as `thinking`; or scope overrides to one renderer or app. Use parser transforms only when token or AST reshaping is required.

## Workflow

Before changing dependencies or source files, inspect the existing package manager and project conventions, preview the intended edits, and obtain explicit user approval.

1. Classify the change as a built-in override, trusted tag, or parser transform.
2. Prefer scoped mappings. Vue, Vue 2, Svelte, and Angular can use `setCustomComponents(customId, mapping)`; Svelte and Angular can also pass renderer-local maps.
3. In React, prefer `streamingComponents` for parser-backed nodes and `htmlComponents` for sanitized attributes plus children.
4. Start with leaf nodes before containers that must preserve children.
5. For trusted tag bodies containing Markdown, use a nested renderer with the same allowlist. Do not add a second smooth-streaming loop.
6. Preserve node/loading props, identity keys, scope IDs, theme state, and preview-height estimates for async diagrams.
7. Remove temporary scoped registrations on cleanup and validate repeated and nested tags.

## Example

```tsx
import MarkdownRender, {
  type NodeComponentProps,
  setCustomComponents,
} from 'markstream-react'
import 'markstream-react/index.css'

function ThinkingNode({ node }: NodeComponentProps<any>) {
  return <details><summary>Thinking</summary>{node.content}</details>
}

setCustomComponents('assistant-panel', { thinking: ThinkingNode })

export function Answer({ markdown }: { markdown: string }) {
  return (
    <MarkdownRender
      content={markdown}
      customId="assistant-panel"
      customHtmlTags={['thinking']}
      htmlPolicy="safe"
    />
  )
}
```

## Limitations

- Component overrides cannot reproduce arbitrary remark/rehype transforms.
- Container overrides require careful child rendering and accessibility review.
- Framework registration APIs are not interchangeable.

## Security & Safety Notes

Treat custom HTML-like tags as trusted input only. Keep safe HTML enabled and do not pass unsanitized attributes into host components.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/markstream-custom-components/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/markstream-custom-components/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/markstream-custom-components/SKILL.md`
