---
name: deep-wiki-full-generation
description: "Generate a complete wiki for the current repository — catalogue + all pages + onboarding guides + VitePress site with dark-mode Mermaid diagrams"
category: docs-and-knowledge-mgmt
source_repo: microsoft/skills
source_path: ".github/plugins/deep-wiki/commands/generate.md"
source_url: https://github.com/microsoft/skills/blob/HEAD/.github/plugins/deep-wiki/commands/generate.md
---


# Deep Wiki: Full Generation

You are a Technical Documentation Architect. Generate a complete, comprehensive wiki for this repository, packaged as a VitePress site with dark-mode Mermaid diagrams and click-to-zoom.

## Process

Execute the following steps in order:

### Step 0: Source Repository Resolution (MUST DO FIRST)

Before any analysis, you MUST determine the source repository context. **Do NOT skip this step.**

1. **Check for git remote**: Run `git remote get-url origin` to detect if a remote URL exists
2. **Ask the user** (if not already provided): _"Is this a local-only repository, or do you have a source repository URL (e.g., GitHub, Azure DevOps)?"_
   - If the user provides a URL (e.g., `https://github.com/org/repo`): store it as `REPO_URL` and use **linked citations** throughout ALL output
   - If local-only: use **local citations** (file path + line number without URL)
3. **Determine default branch**: Run `git rev-parse --abbrev-ref HEAD` or check for `main`/`master`
4. **Store the citation format** for use in all subsequent steps:
   - **Remote**: `[file_path:line_number](REPO_URL/blob/BRANCH/file_path#Lline_number)` — e.g., `[src/auth.ts:42](https://github.com/org/repo/blob/main/src/auth.ts#L42)`
   - **Local**: `(file_path:line_number)` — e.g., `(src/auth.ts:42)`
   - **Line ranges**: `#Lstart-Lend` — e.g., `[src/auth.ts:42-58](https://github.com/org/repo/blob/main/src/auth.ts#L42-L58)`
   - **Mermaid diagrams**: Every diagram MUST be followed by a `<!-- Sources: file_path:line, file_path:line -->` comment block
   - **Tables**: Include a "Source" column with linked citations when listing components, APIs, or configurations

### Step 1: Repository Scan

Examine the repository structure. Identify:
- Entry points (`main.*`, `index.*`, `app.*`, `server.*`, `Program.*`)
- Configuration files (`package.json`, `*.csproj`, `Cargo.toml`, `pyproject.toml`, `go.mod`)
- Build/deploy configs (`Dockerfile`, `docker-compose.yml`, CI/CD)
- Documentation (`README.md`, `docs/`, `CONTRIBUTING.md`)
- Architecture signals: directory naming, layer separation, module boundaries
- Language composition and framework detection
- Key technologies (databases, messaging, actors, caching, API protocols)

### Step 2: Generate Catalogue

Produce a hierarchical JSON documentation structure with two top-level modules:

1. **Getting Started** — overview, environment setup, basic usage, quick reference
2. **Deep Dive** — architecture, data layer, business logic, integrations, frontend

Follow these rules:
- Max nesting depth: 4 levels; ≤8 children per section
- Derive all titles dynamically from actual repo content
- Include file citations in each section's `prompt` field
- For small repos (≤10 files), emit only Getting Started

Output the catalogue as a JSON code block.

### Step 3: Generate Onboarding Guides

Generate **four** audience-tailored onboarding guides in an `onboarding/` folder:

1. **Contributor Guide** (1000–2500 lines) — For new contributors (assumes Python/JS proficiency). Progressive: Part I (language/framework foundations with cross-language comparisons), Part II (this codebase's architecture and domain model), Part III (getting productive — setup, testing, contributing). Includes glossary, key file reference, and appendices.

2. **Staff Engineer Guide** (800–1200 lines) — For staff/principal engineers. Dense, opinionated, architectural. Includes pseudocode in a DIFFERENT language, comparison tables, the ONE core architectural insight, system diagrams, design tradeoff discussion, and decision log.

3. **Executive Guide** (400–800 lines) — For VP/director-level engineering leaders. Capability map, risk assessment, technology investment thesis, cost/scaling model, and actionable recommendations. NO code snippets — service-level diagrams only.

4. **Product Manager Guide** (400–800 lines) — For PMs and non-engineering stakeholders. User journey maps, feature capability map, known limitations, data/privacy overview, and FAQ. ZERO engineering jargon.

### Step 4: Generate Pages

For each leaf node in the catalogue, generate a full documentation page:

- Add VitePress frontmatter: `title` and `description`
- Start with an Overview paragraph explaining WHY this component exists
- Start with an **at-a-glance summary table** (component, responsibility, key file, source) so readers grasp the system in 30 seconds
- Include **minimum 3–5 Mermaid diagrams** per page using at least 2 different diagram types (architecture, sequence, class, state, ER, or flowchart)
- Use `autonumber` in all `sequenceDiagram` blocks
- Cite at least 5 different source files per page using the resolved citation format (linked or local)
- Use Markdown tables for APIs, config options, and component summaries — include "Source" column with citations
- **Tables over prose**: Convert any list of structured items into a table. Use comparison tables for technologies and alternatives.
- **Cross-references between pages**: When a page mentions a concept, component, or pattern documented on another wiki page, link to it with a relative Markdown link (e.g., `[Authentication](../02-architecture/authentication.md)`). Add a "Related Pages" section at the end of each page listing connected wiki pages with one-line descriptions.
- End with a References section

### Step 5: Post-Processing & Validation

Before assembling:

1. **Escape generics** — Wrap bare `Task<string>`, `List<T>` etc. in backticks outside code fences
2. **Fix Mermaid `<br/>`** — Replace with `<br>` (self-closing breaks Vue compiler)
3. **Fix Mermaid inline styles** — Replace light-mode colors with dark equivalents
4. **Validate** — Verify file paths exist, class/method names are accurate, Mermaid syntax is correct

### Step 6: Package as VitePress Site

Scaffold a complete VitePress project in `wiki/` with:
- Daytona-inspired dark theme (Inter + JetBrains Mono fonts)
- Dark-mode Mermaid rendering (theme variables + CSS overrides)
- Click-to-zoom for diagrams (custom SVG overlay with pan/zoom) and images (medium-zoom)
- Dynamic sidebar from catalogue structure
- Onboarding section first (uncollapsed)
- **Proper `index.md` landing page** — Developer-focused, NOT a marketing page. No `hero:` frontmatter. Must contain: Quick Start with runnable commands, architecture overview diagram, documentation map table linking to all sections, key files table with source citations, and tech stack summary. See `/deep-wiki:build` for full template.

See `/deep-wiki:build` for full VitePress packaging details.

### Step 7: Generate AGENTS.md Files (Only If Missing)

Generate `AGENTS.md` files for pertinent repository folders. These files provide coding agents with project-specific context — build commands, testing instructions, code conventions, and boundaries.

> **⚠️ CRITICAL: NEVER overwrite an existing AGENTS.md file.** For each folder, check if `AGENTS.md` already exists. If it does, skip it and report that it was skipped.

1. **Identify pertinent folders** — repository root, `wiki/` (the generated VitePress site), plus `tests/`, `src/`, `lib/`, `app/`, `packages/*/`, `services/*/`, and any folder with its own build manifest (`package.json`, `pyproject.toml`, `Cargo.toml`, `*.csproj`, `go.mod`)
2. **For each folder**, check if `AGENTS.md` exists:
   - If YES → skip, report: `"✅ AGENTS.md already exists — skipping"`
   - If NO → analyze the folder's language, framework, build commands, test commands, conventions, and CI config
3. **Generate tailored AGENTS.md** covering the six core areas: Build & Run Commands (first!), Testing, Project Structure, Code Style, Git Workflow, and Boundaries (✅ always / ⚠️ ask first / 🚫 never)
4. **Generate CLAUDE.md companion** in every folder where AGENTS.md was created (only if `CLAUDE.md` doesn't already exist). Content is always: a heading, a generated-file comment, and a directive to read `AGENTS.md`.
5. **Root AGENTS.md** covers the whole project (tech stack, architecture, global conventions). **Nested AGENTS.md** covers folder-specific details only — don't repeat the root.
6. **Wiki AGENTS.md** (`wiki/AGENTS.md`) — Generate this for the wiki folder **only if it doesn't already exist** (same guard as all other AGENTS.md files). It must cover: VitePress build/dev/preview commands, wiki structure (sections, onboarding, llms.txt), content conventions (Mermaid dark-mode rules, citation format, frontmatter), and boundaries (don't delete generated pages, don't modify theme without testing). Reference `wiki/llms.txt` and `wiki/llms-full.txt` in the Documentation section.
7. **Output a summary** listing which files were created, which were skipped (already exist), and which folders were not applicable.

See `/deep-wiki:agents` for full AGENTS.md generation details.

### Step 8: Generate llms.txt Files

Generate `llms.txt` files — LLM-friendly project summaries following the [llms.txt specification](https://llmstxt.org/).

1. **`./llms.txt`** (repo root) — Standard discovery location. Coding agents and tools (GitHub MCP `get_file_contents`, `search_code`) look here first. Contains H1 project name, blockquote summary, and H2 sections with links into `wiki/` directory.
2. **`wiki/llms.txt`** — Same structure but with wiki-relative paths (for VitePress deployment).
3. **`wiki/llms-full.txt`** — Full page content inlined in `<doc title="..." path="...">` blocks. Strip YAML frontmatter, preserve Mermaid diagrams and citations.
4. **Section order**: Onboarding → Architecture → Getting Started → Deep Dive → Optional (changelog, contributing)
5. **"Optional" H2** has special meaning — content there can be skipped for shorter context windows

See `/deep-wiki:llms` for full llms.txt generation details.

## Mermaid Diagram Rules (ALL diagrams)

- Use dark-mode colors: node fills `#2d333b`, borders `#6d5dfc`, text `#e6edf3`
- Subgraph backgrounds: `#161b22`, borders `#30363d`
- Lines: `#8b949e`
- If using inline `style` directives, use dark fills with `,color:#e6edf3`
- Do NOT use `<br/>` in labels (use `<br>` or line breaks)
- Use `autonumber` in all `sequenceDiagram` blocks

## Depth Requirements (NON-NEGOTIABLE)

1. **TRACE ACTUAL CODE PATHS** — Do not guess from file names. Read the implementation.
2. **EVERY CLAIM NEEDS A SOURCE** — File path + function/class name for every architectural claim.
3. **DISTINGUISH FACT FROM INFERENCE** — If you read the code, say so. If inferring, mark it.
4. **FIRST PRINCIPLES, NOT WIKIPEDIA** — Explain WHY something exists before explaining what it does.

$ARGUMENTS

---

**Source:** [`microsoft/skills`](https://github.com/microsoft/skills) → `.github/plugins/deep-wiki/commands/generate.md`
