---
name: deep-wiki-azure-devops-wiki-export
description: "Generate a Node.js build script that converts the VitePress wiki to Azure DevOps Wiki-compatible markdown in dist/ado-wiki/. Transforms Mermaid syntax, strips front matter, fixes links."
category: docs-and-knowledge-mgmt
source_repo: microsoft/skills
source_path: ".github/plugins/deep-wiki/commands/ado.md"
source_url: https://github.com/microsoft/skills/blob/HEAD/.github/plugins/deep-wiki/commands/ado.md
---


# Deep Wiki: Azure DevOps Wiki Export

You are a Technical Documentation Engineer. Generate a Node.js build script that converts the VitePress wiki output into Azure DevOps (ADO) Wiki-compatible markdown.

## Source Repository Resolution (MUST DO FIRST)

Before generating the build script, resolve the source repository context:

1. **Check for git remote**: Run `git remote get-url origin`
2. **Ask the user**: _"Is this a local-only repository, or do you have a source repository URL?"_
   - Remote URL → store as `REPO_URL`, preserve linked citations in converted output
   - Local → preserve local citations as-is
3. **Do NOT proceed** until resolved

## Context

Azure DevOps Wikis use a markdown dialect that differs from GFM/VitePress in critical ways. This command creates a preprocessing script that reads the generated wiki `.md` files, applies targeted transformations, and writes ADO-compatible copies to `dist/ado-wiki/`.

**Source files are NEVER modified.** Only transformed copies are written to the output directory.

## Process

### Step 1: Scan the Wiki Directory

Locate the generated wiki output (typically `wiki/` or the VitePress source directory). Scan for incompatibilities:

```bash
# Count mermaid code fence blocks
grep -rc '```mermaid' --include="*.md" wiki/ | grep -v ':0$'

# Find flowchart keyword usage
grep -rn '^\s*flowchart ' --include="*.md" wiki/

# Find <br> tags in mermaid labels  
grep -rn '<br>' --include="*.md" wiki/ | head -20

# Count YAML front matter files
for f in $(find wiki/ -name "*.md"); do
  head -1 "$f" | grep -q '^---$' && echo "FRONT MATTER: $f"
done

# Find parent-relative links
grep -rn '](\.\./' --include="*.md" wiki/ | wc -l

# Find VitePress container directives
grep -rn '^:::' --include="*.md" wiki/ | grep -v mermaid
```

Report the scan results before proceeding.

### Step 2: Generate the Build Script

Create `scripts/build-ado-wiki.js` — a Node.js ESM script with **zero external dependencies** (only `node:fs/promises`, `node:path`, `node:url`).

The script must apply these transformations in order:

#### a) Strip YAML Front Matter
Remove `---` delimited YAML blocks at file start. ADO renders these as visible raw text.

#### b) Convert Mermaid Blocks
Process line-by-line, apply fixes ONLY inside mermaid blocks:
- Opening fence: ` ```mermaid ` → `::: mermaid`
- Closing fence: ` ``` ` → `:::`
- `flowchart` → `graph` (preserve direction: TD, LR, TB, RL, BT)
- Strip `<br>`, `<br/>`, `<br />` variants (replace with space)
- Replace long arrows (`---->` with 4+ dashes) with `-->`

#### c) Convert Parent-Relative Source Links
Convert `[text](../../path)` to plain text. Preserve same-directory `.md` links and external URLs.

#### d) Convert VitePress Container Directives
Convert `::: tip` → `> [!TIP]`, `::: warning` → `> [!WARNING]`, `::: danger` → `> [!CAUTION]`, `::: info` → `> [!NOTE]`. Content inside containers becomes blockquoted text.

#### e) Copy Non-Markdown Assets
Copy images, diagrams, and other non-markdown files to `dist/ado-wiki/` preserving relative paths.

### Step 3: Configure the Script

The script should:
- Auto-detect the wiki source directory (`wiki/`, `wiki-site/`, or configurable via CLI arg)
- Output to `dist/ado-wiki/`
- Skip: `node_modules/`, `.vitepress/`, `.git/`, `dist/`
- Print statistics: count of each transformation type applied
- Exit with code 0 on success, 1 on error

### Step 4: Add npm Script

Add to the wiki's `package.json`:

```json
{
  "scripts": {
    "build:ado": "node scripts/build-ado-wiki.js"
  }
}
```

### Step 5: Verify

After generating the script, run it and verify:
1. File count matches source (minus skipped dirs)
2. Zero ` ```mermaid ` fences remaining
3. Zero `flowchart` keywords in mermaid blocks
4. No YAML front matter in output
5. Parent-relative links converted to plain text
6. Same-directory `.md` links preserved
7. Directory structure preserved
8. `index.md` exists at `dist/ado-wiki/` root and is a proper wiki home page (NOT a placeholder)

## ADO Wiki Incompatibility Reference

### CRITICAL (Must Fix)

| Issue | GFM/VitePress | ADO Wiki | Transform |
|-------|--------------|----------|-----------|
| Mermaid fences | ` ```mermaid ` | `::: mermaid` | Convert fences |
| `flowchart` keyword | `flowchart TD` | `graph TD` | Replace keyword |
| `<br>` in Mermaid | `Node[A<br>B]` | Breaks diagram | Strip (→ space) |
| Long arrows | `---->` | Not supported | → `-->` |
| YAML front matter | `---`...`---` | Raw visible text | Strip |
| Parent source links | `[t](../../src)` | Broken path | → plain text |
| Container directives | `::: tip` | Not supported | → `> [!TIP]` |

### Compatible As-Is (No Action Needed)

- ✅ Tables, blockquotes, horizontal rules, emoji
- ✅ Fenced code blocks, relative `.md` links, external URLs
- ✅ Bold, italic, strikethrough, inline code, lists, headings

### ADO Mermaid Supported Types

✅ `sequenceDiagram`, `gantt`, `graph`, `classDiagram`, `stateDiagram`, `journey`, `pie`, `erDiagram`, `gitGraph`, `timeline`
❌ `flowchart` (use `graph`), `mindmap`, `sankey`, `quadrantChart`, `xychart`, `block`

## Index Page Generation (CRITICAL)

The ADO Wiki's `index.md` (root home page) **MUST be a proper wiki landing page**, NOT a generic placeholder. The build script must handle this:

### Logic

1. **If the VitePress source has an `index.md`**: Transform it (strip VitePress-specific hero/features blocks, strip front matter) and use it as the ADO wiki home page
2. **If no VitePress `index.md` exists, or it's a VitePress hero-only page**: Generate a proper `index.md` at `dist/ado-wiki/` root with:
   - **Project title** as `# heading` (from `package.json` name, README, or repo name)
   - **Overview paragraph** — what the project does (from README or generated wiki overview)
   - **Table of Contents** — linked list of all wiki sections/pages with descriptions
   - **Quick Navigation table** — Section, Description, Link columns for the top-level wiki sections
   - **Links to onboarding guides** (if they exist)
3. **NEVER leave `index.md` as a generic "TODO" placeholder** — if the existing `index.md` contains placeholder text like "TODO:", "Give a short introduction", or "TSA bug filing", **replace it entirely** with a proper generated landing page

### Generated Index Template

```markdown
# [Project Name] — Wiki

[1-2 sentence project description]

## Quick Navigation

| Section | Description |
|---------|-------------|
| [Onboarding Hub](./onboarding/index.md) | Guide selector for all audiences |
| [Contributor Guide](./onboarding/contributor-guide.md) | For new contributors (assumes Python/JS) |
| [Staff Engineer Guide](./onboarding/staff-engineer-guide.md) | Architectural deep-dive for senior engineers |
| [Executive Guide](./onboarding/executive-guide.md) | Capability & risk overview for engineering leaders |
| [Product Manager Guide](./onboarding/product-manager-guide.md) | Feature-focused guide for PMs |
| [Getting Started](./01-getting-started/...) | Setup, installation, first steps |
| [Architecture](./02-architecture/...) | System design and component overview |
| ... | ... |

## Wiki Contents

- [Full table of contents with links to all pages]
```

### VitePress Hero Block Stripping

VitePress `index.md` files often contain YAML `hero:` and `features:` blocks inside front matter. The script must:
- Strip the entire YAML front matter (already handled)
- If the remaining content is empty or only whitespace after stripping, generate the landing page from the template above
- If meaningful markdown content remains after stripping, use that content

## Citation & Diagram Preservation

The ADO conversion must preserve the quality of the generated wiki:

- **Linked citations** (`[file:line](URL)`) MUST be preserved — these are standard markdown links and work in ADO
- **`<!-- Sources: ... -->` comment blocks** after Mermaid diagrams MUST be preserved (HTML comments are compatible with ADO)
- **Tables with "Source" columns** MUST be preserved — standard markdown tables work in ADO
- **Mermaid diagrams** are converted (fences only) but the diagram content and structure are preserved
- **All diagram types** that work in ADO (graph, sequenceDiagram, classDiagram, stateDiagram, erDiagram, etc.) are preserved

## ADO Wiki Page Ordering

ADO Wikis use a `.order` file in each directory to control page order in the sidebar. The build script should generate `.order` files:

```javascript
// For each directory in dist/ado-wiki/, create a .order file
// listing page names (without .md extension) in desired order
// Onboarding guides first, then numbered sections
```

$ARGUMENTS

---

**Source:** [`microsoft/skills`](https://github.com/microsoft/skills) → `.github/plugins/deep-wiki/commands/ado.md`
