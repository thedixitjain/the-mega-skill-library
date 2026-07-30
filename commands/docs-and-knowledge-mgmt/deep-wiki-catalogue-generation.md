---
name: deep-wiki-catalogue-generation
description: "Generate only the hierarchical wiki structure (table of contents) as JSON for the current repository"
category: docs-and-knowledge-mgmt
source_repo: microsoft/skills
source_path: ".github/plugins/deep-wiki/commands/catalogue.md"
source_url: https://github.com/microsoft/skills/blob/HEAD/.github/plugins/deep-wiki/commands/catalogue.md
---


# Deep Wiki: Catalogue Generation

Analyze this repository and generate a hierarchical JSON documentation structure.

## Source Repository Resolution (MUST DO FIRST)

Before any analysis, resolve the source repository context:

1. **Check for git remote**: Run `git remote get-url origin`
2. **Ask the user**: _"Is this a local-only repository, or do you have a source repository URL?"_
   - Remote URL → store as `REPO_URL`, use linked citations: `[file:line](REPO_URL/blob/BRANCH/file#Lline)`
   - Local → use `(file_path:line_number)`
3. **Determine default branch**: Run `git rev-parse --abbrev-ref HEAD`
4. **Do NOT proceed** until resolved

## Analysis Phase

1. Read the repository file tree and README
2. Detect project type, language composition, frameworks
3. Identify architectural layers and module boundaries
4. Map key components, services, controllers, and their relationships

## Output Requirements

Generate a JSON structure following this schema:

```json
{
  "items": [
    {
      "title": "getting-started",
      "name": "[Derived from project]",
      "prompt": "[Generation instruction]",
      "children": [
        {
          "title": "[auto-derived]",
          "name": "[Section Name]",
          "prompt": "[1-3 sentence instruction with file citations]",
          "children": []
        }
      ]
    },
    {
      "title": "deep-dive",
      "name": "[Derived from project]",
      "prompt": "[Generation instruction]",
      "children": []
    }
  ]
}
```

### Rules

- Max nesting depth: 4; ≤8 children per section
- Cite real files using the resolved citation format (linked or local) in every prompt
- Getting Started: overview, setup, basic usage, quick reference
- Deep Dive layers: Architecture → Subsystems → Components → Key methods/interfaces
- Component analysis: classes, services, controllers; dependencies; design patterns (Repository, Factory, Strategy, Observer)
- Small repo mode (≤10 files): Getting Started only, 1-2 children, skip Deep Dive

$ARGUMENTS

---

**Source:** [`microsoft/skills`](https://github.com/microsoft/skills) → `.github/plugins/deep-wiki/commands/catalogue.md`
