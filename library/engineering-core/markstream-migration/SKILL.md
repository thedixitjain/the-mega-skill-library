---
name: markstream-migration
description: "Audit and migrate an existing Markdown renderer to Markstream while preserving custom renderers, security policy, streaming behavior, and explicit parity gaps."
allowed-tools: "[claude, cursor, gemini, codex]"
category: engineering-core
source_repo: sickn33/agentic-awesome-skills
source_path: "skills/markstream-migration/SKILL.md"
source_url: https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/markstream-migration/SKILL.md
---


# Markstream Migration

## Overview

Replace an existing Markdown renderer without silently dropping transforms, custom components, URL policy, raw-HTML behavior, or streaming semantics. Read [references/adoption-checklist.md](references/adoption-checklist.md) first.

## When to Use

Use when replacing `react-markdown`, `markdown-it`, `marked`, or another renderer; migrating node renderers; or choosing between Markstream `content`, smooth streaming, and `nodes`.

## Workflow

Before changing dependencies or source files, inspect the existing package manager and project conventions, preview the intended edits, and obtain explicit user approval.

1. Inventory renderer imports, call sites, plugins, HTML policy, URL transforms, allowlists, custom renderers, CSS, and tests.
2. Classify the migration as direct, renderer-custom, plugin-heavy, or security-heavy.
3. Install the framework package and explicit CSS. Preserve visible behavior before optional features.
4. Map built-ins to scoped overrides; in React prefer renderer-local component maps.
5. Use trusted custom tags only for trusted content and reserve parse transforms for irreducible token/AST requirements.
6. Keep `content` with smooth streaming for ordinary token streams. Use `nodes` only for worker parsing, shared AST ownership, or structural transforms.
7. Preserve safe HTML and strict Mermaid defaults; scope and document any trusted legacy exception.
8. Run relevant builds and behavior tests. Report mappings, intentional differences, and unresolved review.

## Example

```tsx
// Before:
// import ReactMarkdown from 'react-markdown'
// return <ReactMarkdown>{markdown}</ReactMarkdown>

import MarkdownRender from 'markstream-react'
import 'markstream-react/index.css'

export function AssistantAnswer({
  markdown,
  isDone,
}: {
  markdown: string
  isDone: boolean
}) {
  return (
    <MarkdownRender
      content={markdown}
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

- Markstream cannot reproduce every remark, rehype, or markdown-it plugin automatically.
- Visual parity does not prove security or URL-policy parity.
- Large migrations may require staged conversion.

## Security & Safety Notes

Do not weaken sanitization for screenshot parity. Review dependencies, raw HTML, URL transforms, and trust boundaries explicitly.

---

**Source:** [`sickn33/agentic-awesome-skills`](https://github.com/sickn33/agentic-awesome-skills) → `skills/markstream-migration/SKILL.md`

**Also appears in:** `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills/skills/markstream-migration/SKILL.md`, `sickn33/agentic-awesome-skills/plugins/agentic-awesome-skills-claude/skills/markstream-migration/SKILL.md`
