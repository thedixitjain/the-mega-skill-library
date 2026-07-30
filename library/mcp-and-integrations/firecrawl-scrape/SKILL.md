---
name: firecrawl-scrape
description: "Scrape web pages and extract content via Firecrawl MCP"
allowed-tools: "[Bash, Read]"
category: mcp-and-integrations
source_repo: parcadei/Continuous-Claude-v3
source_path: ".claude/skills/firecrawl-scrape/SKILL.md"
source_url: https://github.com/parcadei/Continuous-Claude-v3/blob/HEAD/.claude/skills/firecrawl-scrape/SKILL.md
---


# Firecrawl Scrape Skill

## When to Use

- Scrape content from any URL
- Extract structured data from web pages
- Search the web and get content

## Instructions

```bash
uv run python -m runtime.harness scripts/mcp/firecrawl_scrape.py \
    --url "https://example.com" \
    --format "markdown"
```

### Parameters

- `--url`: URL to scrape
- `--format`: Output format - `markdown`, `html`, `text` (default: markdown)
- `--search`: (alternative) Search query instead of direct URL

### Examples

```bash
# Scrape a page
uv run python -m runtime.harness scripts/mcp/firecrawl_scrape.py \
    --url "https://docs.python.org/3/library/asyncio.html"

# Search and scrape
uv run python -m runtime.harness scripts/mcp/firecrawl_scrape.py \
    --search "Python asyncio best practices 2024"
```

## MCP Server Required

Requires `firecrawl` server in mcp_config.json with FIRECRAWL_API_KEY.

---

**Source:** [`parcadei/Continuous-Claude-v3`](https://github.com/parcadei/Continuous-Claude-v3) → `.claude/skills/firecrawl-scrape/SKILL.md`
