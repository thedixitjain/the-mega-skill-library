---
name: launchfast-product-research
description: "| Codex-native multi-keyword Amazon opportunity scan using LaunchFast MCP. Use when the user wants to research 1-10 keywords, compare niches, or decide whether a product idea is a GO, INVESTIGATE, or PASS. Requires the LaunchFast MCP tool `research_products`."
category: research-and-academic
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/BlockchainHB/launchfast_codex_plugin/skills/launchfast-product-research/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/BlockchainHB/launchfast_codex_plugin/skills/launchfast-product-research/SKILL.md
---


# LaunchFast Product Research

Use this skill for a fast, opinionated market scan across up to 10 keywords.

## Inputs

If missing, ask once for:

- keywords to research
- optional target price band
- optional competition tolerance

## Workflow

### 1. Run research

- Run `research_products` for each keyword.
- Prefer parallel tool calls when researching more than one keyword.
- Use `focus="balanced"` and `product_limit=20` unless the user asks otherwise.

### 2. Extract core metrics per keyword

From the response, compute:

- products analyzed
- grade distribution
- median monthly revenue
- top product revenue
- average or median price
- average or median reviews
- brand concentration
- dominant brand

### 3. Score the market

Use this score out of 100:

```text
score =
  (% of products graded B5 or better) * 30
+ (median revenue >= 8000 ? 30 : (median revenue / 8000) * 30)
+ (median reviews < 300 ? 20 : (300 / median reviews) * 20)
+ (median price between 18 and 60 ? 20 : 10)
```

Competition bands:

- Low: median reviews < 200
- Medium: median reviews 200-800
- High: median reviews > 800

Verdicts:

- GO: score >= 65
- INVESTIGATE: score 40-64
- PASS: score < 40

### 4. Present results

Always show:

- a ranked summary table for all keywords
- a short deep dive for the top 3

Use this table shape:

```markdown
## Product Opportunity Scan

| Rank | Keyword | Score | Market Grade | Top Revenue | Avg Price | Competition | Verdict |
|------|---------|-------|--------------|-------------|-----------|-------------|---------|
```

For each top-3 keyword include:

- products analyzed
- grade distribution
- revenue range
- price range
- review range
- best product snapshot
- one-sentence key insight
- risk flags
- verdict with 1-2 sentence rationale

## Notes

- If a keyword has missing or zero search volume, explicitly call that out.
- If the results look too narrow or too broad, suggest the better keyword variant inline.
- Do not force a follow-up question at the end; only recommend next actions when the result is borderline or strong enough to justify it.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/BlockchainHB/launchfast_codex_plugin/skills/launchfast-product-research/SKILL.md`
