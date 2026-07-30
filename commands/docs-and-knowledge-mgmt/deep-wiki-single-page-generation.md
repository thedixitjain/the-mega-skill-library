---
name: deep-wiki-single-page-generation
description: "Generate a single wiki page with dark-mode Mermaid diagrams, source citations, and first-principles depth"
category: docs-and-knowledge-mgmt
source_repo: microsoft/skills
source_path: ".github/plugins/deep-wiki/commands/page.md"
source_url: https://github.com/microsoft/skills/blob/HEAD/.github/plugins/deep-wiki/commands/page.md
---


# Deep Wiki: Single Page Generation

Generate a comprehensive wiki page for the specified topic.

## Source Repository Resolution (MUST DO FIRST)

Before generating any page, resolve the source repository context:

1. **Check for git remote**: Run `git remote get-url origin`
2. **Ask the user**: _"Is this a local-only repository, or do you have a source repository URL?"_
   - Remote URL → store as `REPO_URL`, use linked citations: `[file:line](REPO_URL/blob/BRANCH/file#Lline)`
   - Local → use `(file_path:line_number)`
3. **Determine default branch**: Run `git rev-parse --abbrev-ref HEAD`
4. **Do NOT proceed** until resolved

## Inputs

The user will provide a topic/title and optionally specific file paths. Use $ARGUMENTS to determine what to document.

## Depth Requirements (NON-NEGOTIABLE)

1. **TRACE ACTUAL CODE PATHS** — Do not guess from file names. Read the implementation. If function A calls B calls C, follow it all the way.
2. **EVERY CLAIM NEEDS A SOURCE** — File path + function/class name. "X calls Y" must include where.
3. **DISTINGUISH FACT FROM INFERENCE** — If you read the code, say so. If inferring, mark it explicitly.
4. **FIRST PRINCIPLES** — Explain WHY something exists before explaining what it does.
5. **NO HAND-WAVING** — Don't say "this likely handles..." — read the code and state what it ACTUALLY does.

## Mandatory Three-Phase Process

### Phase 1: Strategic Planning (ALWAYS FIRST)

1. Clarify the page's goals, audience, and deliverables
2. Determine scope based on relevant file count:
   - ≤50 files: full coverage
   - 50–300 files: prioritize critical paths
   - >300 files: tiered sampling (entry points, domain models, data access, integration edges)
3. Set documentation budget:
   - Small scope: ~2,000–3,000 words, 3 diagrams (2+ types)
   - Medium scope: ~3,000–5,000 words, 4 diagrams (3+ types)
   - Large/Complex: ~5,000–8,000+ words, 5–8 diagrams (4+ types)

### Phase 2: Deep Code Analysis

1. Read ALL relevant source files completely
2. Identify: architecture patterns, design patterns, algorithms, data flow, state management
3. Map: component dependencies, external integrations, API contracts
4. Record citation anchors: `file_path:line_number` for every claim

### Phase 3: Document Generation

Structure the page with:

- **VitePress frontmatter**: `title` and `description`
- **Overview**: purpose, scope, executive summary — explain WHY this exists
- **At-a-glance summary table**: Key components/concepts with one-line descriptions and source links — readers should grasp the system in 30 seconds
- **Architecture / System Design**: with `graph TB/LR` Mermaid diagram
- **Core Components**: purpose, implementation, design patterns — use a table per component group with "Component", "Responsibility", "Key File", "Source" columns
- **Data Flow / Interactions**: with `sequenceDiagram` (use `autonumber`)
- **State / Lifecycle**: with `stateDiagram-v2` if the system has meaningful state transitions
- **Data Model**: with `erDiagram` if the system has entities or database tables
- **Implementation Details**: key algorithms, error handling, state management
- **Configuration & Deployment**: use tables for config options (Key, Default, Description, Source)
- **References**: inline citations throughout using resolved format
- **Cross-references**: Link to related wiki pages using relative Markdown links (e.g., `[Data Flow](../02-architecture/data-flow.md)`). Whenever a concept, component, or pattern is covered in more depth on another wiki page, link to it inline. Also add a "Related Pages" section at the end listing connected wiki pages.

### Content Organization Rules

- **Progressive disclosure**: Big picture first → drill into specifics. Don't front-load implementation details.
- **Distill, don't dump**: Every paragraph should earn its place. If a section is just listing things, convert it to a table.
- **Tables over prose**: For any structured data (APIs, parameters, configs, components, comparisons), ALWAYS use a table.
- **One idea per paragraph**: Keep paragraphs focused and scannable. Use bold for key terms.
- **Section summaries**: Start complex sections with a 1-2 sentence TL;DR before the details.
- **Visual rhythm**: Alternate between prose, diagrams, tables, and code blocks — avoid long walls of text.

### Mermaid Requirements

Include **minimum 3 diagrams** using at least 2 different types. More is better — aim for one diagram per major section:

| Type | Best For | When to Use |
|------|----------|-------------|
| `graph TB/LR` | Architecture, component relationships | Structural overviews, dependency graphs |
| `sequenceDiagram` | API flows, interactions (always use `autonumber`) | Multi-step processes, request lifecycles |
| `classDiagram` | Class hierarchies, interfaces | Domain models, type relationships |
| `stateDiagram-v2` | State machines, lifecycle | Status transitions, workflow states |
| `erDiagram` | Database schema, entities | Data models, table relationships |
| `flowchart` | Data pipelines, decision trees | Conditional logic, error handling paths |

**Dark-mode colors (MANDATORY)**:
- Node fills: `#2d333b`, borders: `#6d5dfc`, text: `#e6edf3`
- Subgraph backgrounds: `#161b22`, borders: `#30363d`
- Lines: `#8b949e`
- If using inline `style` directives, use dark fills with `,color:#e6edf3`
- Do NOT use `<br/>` in labels (use `<br>` or line breaks)

### Citation Rules (MANDATORY)

- Every non-trivial claim uses the resolved citation format:
  - **Remote**: `[src/path/file.ts:42](REPO_URL/blob/BRANCH/src/path/file.ts#L42)`
  - **Local**: `(src/path/file.ts:42)`
  - **Line ranges**: `[src/path/file.ts:42-58](REPO_URL/blob/BRANCH/src/path/file.ts#L42-L58)`
- Approximate: `[src/path/file.ts:~ClassName](REPO_URL/blob/BRANCH/src/path/file.ts)` or `(src/path/file.ts:~ClassName)`
- Missing evidence: `(Unknown – verify in path/to/check)`
- Minimum 5 different source files cited per page
- **Mermaid diagrams**: Add `<!-- Sources: file_path:line, file_path:line -->` comment block after each diagram
- **Tables**: Include a "Source" column with linked citations when listing components, APIs, or configurations

### VitePress Compatibility

- Escape generics outside code fences: use `` `List<T>` `` not bare `List<T>`
- No `<br/>` in Mermaid blocks
- All hex colors must be 3 or 6 digits (not 4 or 5)

## Validation Checklist

Before finalizing, verify:
- [ ] Source repository context resolved (remote URL or confirmed local)
- [ ] All file paths mentioned actually exist in the repo
- [ ] All class/method names are accurate (not hallucinated)
- [ ] All citations use correct format (linked for remote, local otherwise)
- [ ] Every Mermaid diagram has a `<!-- Sources: ... -->` comment block
- [ ] Mermaid diagrams use dark-mode colors
- [ ] No bare generics outside code fences
- [ ] Every architectural claim has a file reference

$ARGUMENTS

---

**Source:** [`microsoft/skills`](https://github.com/microsoft/skills) → `.github/plugins/deep-wiki/commands/page.md`
