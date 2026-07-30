---
name: validate-plugin
description: "Validate plugin structure, schema, and naming. Use for plugin creation, debugging, or verification."
category: engineering-core
source_repo: athola/claude-night-market
source_path: "plugins/abstract/commands/validate-plugin.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/abstract/commands/validate-plugin.md
---


# Validate Plugin Structure

This command validates a Claude Code plugin's structure against the official documentation requirements.

## Usage

```bash
# Validate current directory
/validate-plugin

# Validate specific plugin
/validate-plugin ~/claude-night-market/plugins/archetypes

# Validate relative path
/validate-plugin ../my-plugin
```

## What It Checks

The validator performs detailed checks:

### Critical Requirements
- `.claude-plugin/plugin.json` exists and is valid JSON
- Required `name` field is present
- Plugin name follows kebab-case convention
- Referenced files and paths exist
- Directories are in correct locations (not nested in `.claude-plugin/`)

### Warnings
- Path format (should be relative with `./`)
- Semantic versioning format
- Directory structure matches references

### Recommendations
- Recommended metadata fields (version, description, author, license)
- Enhanced Claude configuration options
- Skill frontmatter completeness

## Examples

### Validate Current Plugin

```bash
cd ~/claude-night-market/plugins/archetypes
/validate-plugin
```

### Batch Validate Multiple Plugins

```bash
for plugin in ~/claude-night-market/plugins/*; do
  /validate-plugin "$plugin"
done
```

## Implementation

Run the Python validation script:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/validate_plugin.py "${1:-.}"
```

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/abstract/commands/validate-plugin.md`
