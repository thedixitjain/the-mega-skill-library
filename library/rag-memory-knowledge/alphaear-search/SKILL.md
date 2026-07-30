---
name: alphaear-search
description: "Perform finance web searches and local context searches. Use when the user needs general finance info from the web (Jina/DDG/Baidu) or needs to retrieve finance information from a local document store (RAG)."
category: rag-memory-knowledge
source_repo: RKiding/Awesome-finance-skills
source_path: "skills/alphaear-search/SKILL.md"
source_url: https://github.com/RKiding/Awesome-finance-skills/blob/HEAD/skills/alphaear-search/SKILL.md
---


# AlphaEar Search Skill

## Overview

Unified search capabilities: web search (Jina/DDG/Baidu) and local RAG search.

## Capabilities

### 1. Web Search

Use `scripts/search_tools.py` via `SearchTools`.

-   **Search**: `search(query, engine, max_results)`
    -   Engines: `jina`, `ddg`, `baidu`, `local`.
    -   Returns: JSON string (summary) or List[Dict] (via `search_list`).
-   **Smart Cache (Agentic)**: If you want to avoid redundant searches, use the **Search Cache Relevance Prompt** in `references/PROMPTS.md`. Read the cache first and decide if it's usable.
-   **Aggregate**: `aggregate_search(query)`
    -   Combines results from multiple engines.


### 2. Local RAG

Use `scripts/hybrid_search.py` or `SearchTools` with `engine='local'`.

-   **Search**: Searches local `daily_news` database.

## Dependencies

-   `duckduckgo-search`, `requests`
-   `scripts/database_manager.py` (search cache & local news)

---

**Source:** [`RKiding/Awesome-finance-skills`](https://github.com/RKiding/Awesome-finance-skills) → `skills/alphaear-search/SKILL.md`
