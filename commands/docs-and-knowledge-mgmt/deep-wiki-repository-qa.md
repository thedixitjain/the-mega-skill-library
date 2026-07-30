---
name: deep-wiki-repository-qa
description: "Ask a question about the repository using wiki context and source file references"
category: docs-and-knowledge-mgmt
source_repo: microsoft/skills
source_path: ".github/plugins/deep-wiki/commands/ask.md"
source_url: https://github.com/microsoft/skills/blob/HEAD/.github/plugins/deep-wiki/commands/ask.md
---


# Deep Wiki: Repository Q&A

Answer a question about this repository grounded in actual source code.

## Source Repository Resolution (MUST DO FIRST)

Before answering, resolve the source repository context:

1. **Check for git remote**: Run `git remote get-url origin`
2. **Ask the user**: _"Is this a local-only repository, or do you have a source repository URL?"_
   - Remote URL → store as `REPO_URL`, use linked citations: `[file:line](REPO_URL/blob/BRANCH/file#Lline)`
   - Local → use `(file_path:line_number)`
3. **Determine default branch**: Run `git rev-parse --abbrev-ref HEAD`
4. **Do NOT proceed** until resolved

## Question

$ARGUMENTS

## Process

1. **Detect language** of the question and respond in the **same language**
2. **Search** the codebase for files relevant to the question
3. **Read** those files to gather evidence
4. **Synthesize** an answer grounded entirely in actual code — never invent or guess

## Response Format

```markdown
## [Concise Answer Title]

[1-2 paragraph direct answer]

### How It Works
[Detailed explanation with inline code citations and at least 1 Mermaid diagram when the answer involves architecture, flow, or relationships]

### Key Files
| File | Purpose | Source |
|------|---------|--------|
| `src/path/file.ts` | [Role in the system] | [linked citation] |

### Code Example
<!-- Source: file_path:line_number -->
[Relevant snippet from actual source, if helpful]

### Related
- [Related concepts or files to explore]
```

## Rules

- ONLY use information from actual source files in this repository
- NEVER invent, guess, or use external knowledge
- ALWAYS cite source files inline using the resolved citation format:
  - **Remote**: `[src/path/file.ts:42](REPO_URL/blob/BRANCH/src/path/file.ts#L42)`
  - **Local**: `(src/path/file.ts:42)`
- Think step by step through complex questions
- If information is insufficient, say so explicitly and suggest which files to examine

---

**Source:** [`microsoft/skills`](https://github.com/microsoft/skills) → `.github/plugins/deep-wiki/commands/ask.md`
