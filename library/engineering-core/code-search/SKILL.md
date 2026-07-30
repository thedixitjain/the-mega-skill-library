---
name: code-search
description: "Searches GitHub for existing implementations, libraries, or patterns. Use when finding code examples or prior art on a topic during a research session."
category: engineering-core
source_repo: athola/claude-night-market
source_path: "plugins/tome/skills/code-search/SKILL.md"
source_url: https://github.com/athola/claude-night-market/blob/HEAD/plugins/tome/skills/code-search/SKILL.md
---

# Code Search

## When To Use

- Finding existing implementations or libraries on GitHub
- Part of a `/tome:research` session or standalone search

## When NOT To Use

- Searching local codebase (use Grep or Explore agent)
- Academic literature (use `/tome:papers`)

Search GitHub for implementations of a given topic.

## Usage

Invoked as part of `/tome:research` or standalone.

## Workflow

1. Build search queries using
   `tome.channels.github.build_github_search_queries()`
2. Execute queries via WebSearch
3. Parse results via `parse_github_result()`
4. Optionally use GitHub API via
   `build_github_api_search()` for richer metadata
5. Rank via `rank_github_findings()`
6. Return Finding objects

## Exit Criteria

- [ ] At least one GitHub search query built and executed via
      WebSearch for the requested topic
- [ ] Results parsed into Finding objects containing repo metadata
      (name, URL, stars) and a relevance score
- [ ] Findings returned from `rank_github_findings()` sorted by
      relevance score descending
- [ ] If no results are found for the query, this is reported
      explicitly rather than returning an empty list silently

---

**Source:** [`athola/claude-night-market`](https://github.com/athola/claude-night-market) → `plugins/tome/skills/code-search/SKILL.md`
