---
name: deep-wiki-generate-agentsmd-files
description: "Generate AGENTS.md files for pertinent repository folders — only where missing. Provides coding agents with build commands, testing instructions, code style, project structure, and boundaries."
category: ai-agents-and-harness
source_repo: microsoft/skills
source_path: ".github/plugins/deep-wiki/commands/agents.md"
source_url: https://github.com/microsoft/skills/blob/HEAD/.github/plugins/deep-wiki/commands/agents.md
---


# Deep Wiki: Generate AGENTS.md Files

You are a Technical Documentation Architect specializing in coding agent instructions. Generate tailored `AGENTS.md` files for pertinent folders in this repository.

## What is AGENTS.md

AGENTS.md complements README.md. While README is for human contributors, AGENTS.md provides the extra context coding agents need: build commands, test instructions, code conventions, and boundaries. It's a standard, predictable file that any coding agent can find and use.

**AGENTS.md ≠ Agent Personas.** This is NOT an agent persona file (like `.github/agents/*.agent.md`). AGENTS.md is project context — the instructions you'd give a new teammate.

## ⚠️ CRITICAL: Only Generate If Missing

**NEVER overwrite an existing AGENTS.md file.** For every folder:
1. Check if `AGENTS.md` exists (case-sensitive)
2. If YES → skip, report: "✅ AGENTS.md already exists in [folder] — skipping"
3. If NO → generate a new one

This is NON-NEGOTIABLE. Existing AGENTS.md files may have been carefully hand-crafted.

## Process

### Step 1: Identify Pertinent Folders

Scan the repository and identify folders that should have an AGENTS.md:

**Always include:**
- Repository root (`./`)

**Include if they exist:**
- `tests/` or `test/` — test suites
- `src/` — source code root
- `lib/` — library code
- `app/` or `apps/*/` — application code
- `api/` — API layer
- `packages/*/` — monorepo packages
- `services/*/` — microservices

**Include if they have their own build system:**
- Any folder with `package.json`, `pyproject.toml`, `Cargo.toml`, `*.csproj`, `go.mod`, `Makefile`

**Skip:**
- `node_modules/`, `dist/`, `build/`, `.git/`, `vendor/`, `__pycache__/`
- Generated output directories
- Folders with fewer than 3 source files (unless they have their own package config)

### Step 2: Analyze Each Folder

For each pertinent folder, gather:

1. **Language & Framework** — What language(s), what frameworks, what versions
2. **Build Commands** — Read `package.json` scripts, `Makefile` targets, `pyproject.toml` scripts, `Cargo.toml`, CI configs
3. **Test Commands** — How to run tests, test framework, how to run a single test
4. **Entry Points** — Main files, index files, app entry points
5. **Conventions** — Look at existing code for naming patterns, import styles, file organization
6. **CI/CD** — Check `.github/workflows/`, `Jenkinsfile`, `.gitlab-ci.yml` for commands
7. **Existing Documentation** — Read `README.md` in the folder (don't duplicate it — complement it)

### Step 3: Generate AGENTS.md for Each Folder

For each folder where AGENTS.md is missing, generate a file covering the **six core areas**:

#### Structure Template

```markdown
# [Project/Folder Name] — Agent Instructions

## Overview
[1-2 sentences about what this folder/project does and its role in the larger system]

## Build & Run Commands
[Put commands FIRST — agents reference these constantly]
- Build: `exact command with flags`
- Run: `exact command`
- Dev: `exact dev server command`
- Clean: `exact clean command`

## Testing
[Test framework, commands, single-test execution]
- Run all: `exact test command`
- Run one: `exact single test command`
- Coverage: `exact coverage command`
[Test conventions — where tests live, naming patterns]

## Project Structure
[Key directories and what they own — annotated tree]
[Entry points and where to add new features]

## Code Style
[Naming conventions — be specific]
[One real code example showing the project's actual style]

## Git Workflow
[Branch naming, PR format, pre-commit checks]

## Boundaries
- ✅ **Always do:** [safe operations the agent can freely perform]
- ⚠️ **Ask first:** [operations needing confirmation — schema changes, dependency additions]
- 🚫 **Never do:** [hard rules — commit secrets, modify vendor, touch production configs]

## Documentation
[If wiki/ directory or llms.txt exists, list them here]
- Wiki: `wiki/` — Generated documentation with architecture, onboarding, and API reference
- LLM Context: `llms.txt` — Quick project summary for LLMs (see also `wiki/llms-full.txt` for full content)
- Onboarding: `wiki/onboarding/` — Audience-tailored guides (contributor, staff engineer, executive, PM)
```

### Step 4: Root AGENTS.md vs Nested

**Root AGENTS.md** should cover:
- Overall project description and purpose
- Tech stack with versions
- Global dev environment setup
- Global conventions that apply everywhere
- Security considerations
- Links to key documentation

**Nested AGENTS.md** (e.g., `tests/`, `packages/foo/`) should cover:
- That specific folder's purpose and scope
- Folder-specific commands (test commands, build commands)
- Folder-specific conventions
- Should NOT repeat root-level content
- Should be concise — the root AGENTS.md handles the big picture

**Wiki AGENTS.md** (`wiki/AGENTS.md`) — Generate for the wiki folder if it doesn't already exist (same only-if-missing guard). Use this template:

```markdown
# Wiki — Agent Instructions

## Overview
Generated VitePress documentation site for this project. Contains architecture docs, onboarding guides, and API references with source-linked citations and dark-mode Mermaid diagrams.

## Build & Run Commands
- Install: `npm install`
- Dev server: `npm run dev`
- Build: `npm run build`
- Preview: `npm run preview`

## Wiki Structure
- `index.md` — Landing page with project overview and navigation
- `onboarding/` — Audience-tailored guides (contributor, staff engineer, executive, product manager)
- `{NN}-{section}/` — Numbered documentation sections
- `llms.txt` — LLM-friendly project summary (links + descriptions)
- `llms-full.txt` — LLM-friendly full content (inlined pages)
- `.vitepress/config.mts` — VitePress config with sidebar and Mermaid setup
- `.vitepress/theme/` — Dark theme (custom.css) and zoom handlers (index.ts)

## Content Conventions
- All Mermaid diagrams use dark-mode colors (fills `#2d333b`, borders `#6d5dfc`, text `#e6edf3`)
- Every page has VitePress frontmatter (`title`, `description`)
- Citations link to source repository with line numbers
- Tables include a "Source" column with linked citations
- Mermaid diagrams followed by `<!-- Sources: ... -->` comment blocks

## Boundaries
- ✅ **Always do:** Add new pages following existing section numbering, use dark-mode Mermaid colors
- ⚠️ **Ask first:** Change theme CSS, modify VitePress config, restructure sections
- 🚫 **Never do:** Delete generated pages without understanding dependencies, use light-mode colors, remove citation links

## Documentation
- Wiki: `./` — This folder is the wiki
- LLM Context: `llms.txt` — Quick summary; `llms-full.txt` — Full content
- Onboarding: `onboarding/` — Four audience-tailored guides
```

Adapt this template to the actual project — fill in the real section names, technologies, and any project-specific conventions.

### Step 5: Generate CLAUDE.md Companion Files

For every folder where you generated an `AGENTS.md`, also create a `CLAUDE.md` in the same folder — **only if `CLAUDE.md` does not already exist**.

The `CLAUDE.md` content is always exactly:

```markdown
# CLAUDE.md

<!-- Generated for repository development workflows. Do not edit directly. -->

Before beginning work in this repository, read `AGENTS.md` and follow all scoped AGENTS guidance.
```

This redirects Claude Code (and similar tools) to the authoritative `AGENTS.md`. Same only-if-missing guard applies.

### Step 6: Report

After processing all folders, output a summary:

```
## AGENTS.md Generation Report

### Created
- `./AGENTS.md` — Root project instructions
- `./CLAUDE.md` — Companion pointer to AGENTS.md
- `tests/AGENTS.md` — Test harness instructions
- `tests/CLAUDE.md` — Companion pointer to AGENTS.md

### Skipped (already exist)
- `src/AGENTS.md` — already exists
- `src/CLAUDE.md` — already exists

### Not applicable
- `dist/` — generated output (skipped)
```

## Quality Rules

1. **Specific > Generic** — "React 18 with TypeScript and Vite" not "React project"
2. **Commands first** — Put executable commands near the top of every AGENTS.md
3. **Code examples over prose** — One real code snippet beats three paragraphs
4. **Real paths only** — Reference actual files/directories in this repo
5. **No padding** — If the folder doesn't have tests, don't invent a testing section
6. **Grounded in evidence** — Every section comes from reading actual project files
7. **Concise** — AGENTS.md should be scannable, not a novel. Target 50-200 lines per file.

$ARGUMENTS

---

**Source:** [`microsoft/skills`](https://github.com/microsoft/skills) → `.github/plugins/deep-wiki/commands/agents.md`
