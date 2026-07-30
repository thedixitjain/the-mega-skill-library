---
name: agentskills-claude
description: "This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. The project defines an open format for teaching AI agents specialized workflows through SKILL.md files."
category: docs-and-knowledge-mgmt
source_repo: agentskills/agentskills
source_path: "docs/CLAUDE.md"
source_url: https://github.com/agentskills/agentskills/blob/HEAD/docs/CLAUDE.md
---
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. The project defines an open format for teaching AI agents specialized workflows through SKILL.md files.

## Documentation

The Agent Skills documentation site, defined in the `docs/` directory, is built with [Mintlify](https://mintlify.com).

### Quick Start Commands

```bash
# Run local development server
npm run dev
```

Local preview available at `http://localhost:3000`

### Development Notes

- **Navigation**: Defined in `docs/docs.json` under `navigation.pages` array
- **Adding pages**: Create new `.mdx` file in `/docs`, add filename (without extension) to navigation
- **Deployment**: Automatic on push to `main` branch
- **Troubleshooting**: If page shows 404, ensure you're running `mint dev` from directory containing `docs.json`

---

**Source:** [`agentskills/agentskills`](https://github.com/agentskills/agentskills) → `docs/CLAUDE.md`
