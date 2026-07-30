---
name: deep-wiki-generate-llmstxt
description: "Generate llms.txt and llms-full.txt files for the wiki — LLM-friendly project summaries following the llms.txt specification"
category: docs-and-knowledge-mgmt
source_repo: microsoft/skills
source_path: ".github/plugins/deep-wiki/commands/llms.md"
source_url: https://github.com/microsoft/skills/blob/HEAD/.github/plugins/deep-wiki/commands/llms.md
---


# Deep Wiki: Generate llms.txt

You are generating `llms.txt` and `llms-full.txt` files that provide LLM-friendly access to the wiki documentation. These follow the [llms.txt specification](https://llmstxt.org/).

## Source Repository Resolution (MUST DO FIRST)

Before generating, resolve the source repository context:

1. **Check for git remote**: Run `git remote get-url origin`
2. **Ask the user**: _"Is this a local-only repository, or do you have a source repository URL?"_
   - Remote URL → store as `REPO_URL`, use linked references: `[Title](REPO_URL/blob/BRANCH/path)`
   - Local → use relative paths to wiki files
3. **Determine default branch**: Run `git rev-parse --abbrev-ref HEAD`
4. **Do NOT proceed** until resolved

## What is llms.txt

`llms.txt` is a standardized markdown file that helps LLMs quickly understand a project. It provides:

- A concise project summary
- Links to key documentation files with brief descriptions
- Structured sections (Onboarding, Architecture, API, etc.)

Two files are generated:

| File | Purpose | Size |
|------|---------|------|
| `llms.txt` | Links + brief descriptions — fits in small context windows | Small (1-5 KB) |
| `llms-full.txt` | Full inlined content of all linked pages | Large (50-500 KB) |

## Step 1: Gather Project Context

Scan the repository and existing wiki (if generated) to collect:

1. **Project identity** — name, one-sentence description, primary language, key technologies
2. **Wiki pages** — scan `wiki/` directory for all generated `.md` files
3. **Onboarding guides** — check for `onboarding/` folder with audience-tailored guides
4. **README** — extract the core project description
5. **Key entry points** — main files, API surface, configuration

## Step 2: Generate `llms.txt`

Create `wiki/llms.txt` following the llms.txt spec format:

```markdown
# {Project Name}

> {One-paragraph summary: what it does, who it's for, key technologies. Dense and informative.}

{2-3 paragraphs of important context: architectural philosophy, key constraints, what makes this project different. Include things an LLM needs to know to give accurate answers about this project.}

## Onboarding

- [{Contributor Guide}](./onboarding/contributor-guide.md): Step-by-step guide for new contributors — environment setup, first task, testing, and coding conventions
- [{Staff Engineer Guide}](./onboarding/staff-engineer-guide.md): Architectural deep-dive for senior engineers — design decisions, domain model, component types, and failure modes
- [{Executive Guide}](./onboarding/executive-guide.md): Capability overview for engineering leaders — risk assessment, technology investment, and scaling model
- [{Product Manager Guide}](./onboarding/product-manager-guide.md): Feature-focused guide for PMs — user journeys, capabilities, limitations, and data/privacy

## Architecture

- [{Architecture Overview}](./02-architecture/overview.md): System architecture, component boundaries, and deployment topology
- [{Data Model}](./02-architecture/data-model.md): Core entities, relationships, and data invariants
- [{API Reference}](./02-architecture/api-reference.md): Endpoints, authentication, and wire format

## Getting Started

- [{Setup Guide}](./01-getting-started/setup.md): Prerequisites, installation, and first run
- [{Configuration}](./01-getting-started/configuration.md): Environment variables, feature flags, and config files

## Deep Dive

- [{Component Name}](./03-deep-dive/component.md): Description of component purpose and scope
- ...additional pages...

## Optional

- [{Changelog}](./changelog.md): Recent changes and version history
- [{Contributing}](./contributing.md): How to contribute to the project
```

### llms.txt Rules

1. **H1** — Project name (REQUIRED, only one)
2. **Blockquote** — Dense one-paragraph summary (REQUIRED)
3. **Context paragraphs** — Important notes, constraints, non-obvious things (optional but recommended)
4. **H2 sections** — Each contains a markdown list of `[Title](url): Description` entries
5. **"Optional" section** — Special meaning: these links can be skipped for shorter context. Put changelog, contributing guides, and supplementary material here.
6. **All links are relative** to the wiki directory (e.g., `./onboarding/contributor-guide.md`)
7. **Descriptions are concise** — one sentence per link, informative not generic
8. **Order matters** — put the most important sections first (Onboarding → Architecture → Getting Started → Deep Dive → Optional)
9. **Dynamic content** — derive ALL section names and page titles from the actual generated wiki catalogue, not from templates

### Content Quality

- The blockquote summary should be **dense and specific** — not "A project for doing things" but "A distributed task orchestration engine built on Orleans virtual actors, providing reliable workflow execution with at-least-once delivery guarantees for Azure-hosted microservices"
- Context paragraphs should include **non-obvious constraints** — things an LLM would get wrong without being told (e.g., "Although the API surface resembles FastAPI, it uses a custom router that does not support dependency injection")
- Link descriptions should tell the reader **what they'll learn**, not just restate the title

## Step 3: Generate `llms-full.txt`

Create `wiki/llms-full.txt` — same structure as `llms.txt` but with full page content inlined using XML-style tags.

### Format

```markdown
# {Project Name}

> {Same blockquote summary as llms.txt}

{Same context paragraphs as llms.txt}

## Onboarding

<doc title="{Contributor Guide}" path="onboarding/contributor-guide.md">
{Full markdown content of contributor-guide.md}
</doc>

<doc title="{Staff Engineer Guide}" path="onboarding/staff-engineer-guide.md">
{Full markdown content of staff-engineer-guide.md}
</doc>

...

## Architecture

<doc title="{Architecture Overview}" path="02-architecture/overview.md">
{Full markdown content of overview.md}
</doc>

...

## Optional

<doc title="{Changelog}" path="changelog.md">
{Full markdown content of changelog.md}
</doc>
```

### llms-full.txt Rules

1. **Same H1, blockquote, and context** as `llms.txt`
2. **Replace link lists** with `<doc>` blocks containing full page content
3. **Each `<doc>` tag** has `title` and `path` attributes
4. **Strip VitePress frontmatter** (YAML `---` blocks) from inlined content
5. **Preserve Mermaid diagrams** — keep them as-is inside `<doc>` blocks
6. **Preserve citations** — all `[file:line](URL)` links stay intact
7. **Preserve tables** — all markdown tables stay intact
8. **Same section order** as `llms.txt`
9. **"Optional" section** — still present but readers/tools may skip it for context savings

## Step 4: Validate

After generating both files, verify:

1. **All links in `llms.txt` point to files that exist** in the wiki directory
2. **All `<doc>` blocks in `llms-full.txt` contain actual content** (not empty or placeholder)
3. **The blockquote summary is specific** to this project (not generic)
4. **Section ordering** matches: Onboarding → Architecture → Getting Started → Deep Dive → Optional
5. **No duplicate entries** — each wiki page appears in exactly one section
6. **File sizes are reasonable** — `llms.txt` should be 1-5 KB, `llms-full.txt` should contain all wiki pages

## Output

Generate three files:

```
./llms.txt                # Root-level discovery file (repo standard path)
wiki/
├── llms.txt              # Links + descriptions (for VitePress site)
└── llms-full.txt         # Full inlined content (comprehensive reference)
```

### Root `./llms.txt` (Discovery File)

The root `./llms.txt` is the **standard discovery location** per the llms.txt spec. Coding agents and tools (including the GitHub MCP server's `get_file_contents` and `search_code`) look for `/llms.txt` at the repository root. This file should be identical to `wiki/llms.txt` but with paths adjusted to point into the `wiki/` directory:

```markdown
- [{Page Title}](./wiki/onboarding/contributor-guide.md): Description
```

If a root `llms.txt` already exists and was NOT generated by deep-wiki, do NOT overwrite it — report that it was skipped.

Report a summary:

```
## llms.txt Generation Report

- `./llms.txt` — Root discovery file, {N} sections, {M} linked pages
- `wiki/llms.txt` — {N} sections, {M} linked pages, {size} KB
- `wiki/llms-full.txt` — {N} sections, {M} inlined pages, {size} KB

### Sections
| Section | Pages | Notes |
|---------|-------|-------|
| Onboarding | 4 | All audience-tailored guides |
| Architecture | 3 | Core architecture pages |
| Getting Started | 2 | Setup and configuration |
| Deep Dive | {N} | Component documentation |
| Optional | {N} | Changelog, contributing |
```

$ARGUMENTS

---

**Source:** [`microsoft/skills`](https://github.com/microsoft/skills) → `.github/plugins/deep-wiki/commands/llms.md`
