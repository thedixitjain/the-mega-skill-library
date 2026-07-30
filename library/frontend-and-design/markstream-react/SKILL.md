---
name: markstream-react
description: "Integrate the beta markstream-react renderer into React 18+ or Next.js with correct client/server entrypoints, CSS, streaming state, and component overrides."
allowed-tools: "[claude, cursor, gemini, codex]"
category: frontend-and-design
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/markstream-react/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/markstream-react/SKILL.md
---


# Markstream React

## Overview

Wire the beta React renderer into React 18+ or Next.js without crossing client/server boundaries or reaching for AST control unnecessarily.

## When to Use

Use for React/Next setup, root/`next`/`server` entrypoints, streaming, component overrides, or migration support. Pair with `markstream-migration` for renderer replacement.

## Workflow

Before changing dependencies or source files, inspect the existing package manager and project conventions, preview the intended edits, and obtain explicit user approval.

1. Confirm React 18+ and acceptance of a beta package.
2. Install only requested peers and import `markstream-react/index.css`.
3. Use the root entry for client rendering, `/next` for Next-specific components, and `/server` for server rendering without client hooks.
4. Start with `content` and `smoothStreaming="auto"`; use `nodes` plus `final` only when another layer owns parsing.
5. For live chat disable fade and opt into the cursor. On completion set `final`, disable pacing/cursor, and enable fade only if desired.
6. Keep browser-only peers inside `'use client'`, dynamic `ssr: false`, or another minimal boundary.
7. Prefer `streamingComponents` for parser-backed tags and `htmlComponents` for sanitized props. Use scoped registry overrides for built-in nodes.
8. Keep `htmlPolicy="safe"` and Mermaid strict; validate client, server, and incremental paths.

## Example

```tsx
import MarkdownRender from 'markstream-react'
import 'markstream-react/index.css'

export function StreamingAnswer({
  content,
  isDone,
}: {
  content: string
  isDone: boolean
}) {
  return (
    <MarkdownRender
      content={content}
      final={isDone}
      fade={isDone}
      typewriter={!isDone}
      smoothStreaming={isDone ? false : 'auto'}
      htmlPolicy="safe"
    />
  )
}
```

## Limitations

- The package is beta and requires React 18+.
- Browser-only peers require client boundaries under SSR.
- Complex parser parity requires separate migration review.

## Security & Safety Notes

Review dependencies and never opt untrusted model output into trusted HTML or loose diagram rendering.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/markstream-react/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/markstream-react/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/markstream-react/SKILL.md`
