---
name: vibeship-spawner-skills
description: "CLI installer for VibeShip Spawner skills - 260+ specialist skills for AI-powered product building."
category: docs-and-knowledge-mgmt
source_repo: vibeforge1111/vibeship-spawner-skills
source_path: "cli/README.md"
source_url: https://github.com/vibeforge1111/vibeship-spawner-skills/blob/HEAD/cli/README.md
---
# vibeship-spawner-skills

CLI installer for VibeShip Spawner skills - 260+ specialist skills for AI-powered product building.

## Quick Install

```bash
npx vibeship-spawner-skills install
```

This clones the skills repository to `~/.spawner/skills/`.

## Commands

| Command | Description |
|---------|-------------|
| `install` | Install skills to ~/.spawner/skills |
| `update` | Update skills to latest version |
| `status` | Check installation status |
| `list` | List installed skill categories |
| `help` | Show help message |

## Usage Examples

```bash
# First-time installation
npx vibeship-spawner-skills install

# Update to latest skills
npx vibeship-spawner-skills update

# Check if installed
npx vibeship-spawner-skills status

# List all categories
npx vibeship-spawner-skills list
```

## After Installation

Skills are available at: `~/.spawner/skills/`

Load skills in Claude by reading their YAML files:

```
Read: ~/.spawner/skills/development/backend/skill.yaml
Read: ~/.spawner/skills/development/backend/sharp-edges.yaml
```

## Skill Categories

- **development** (62 skills) - Backend, frontend, API, auth, testing
- **marketing** (33 skills) - Content, SEO, social, email
- **integrations** (16 skills) - AWS, Stripe, Discord, Slack, Twilio
- **ai** (12 skills) - LLM, ML, embeddings, RAG
- **agents** (10 skills) - Autonomous agents, multi-agent systems
- **data** (10 skills) - PostgreSQL, Redis, data pipelines
- **mind** (10 skills) - Memory systems, context management
- And 17 more categories...

## Documentation

Full documentation: https://github.com/vibeforge1111/vibeship-spawner-skills

## License

MIT

---

**Source:** [`vibeforge1111/vibeship-spawner-skills`](https://github.com/vibeforge1111/vibeship-spawner-skills) → `cli/README.md`
