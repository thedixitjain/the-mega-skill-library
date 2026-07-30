---
name: product-research
description: "| Deep Codex-native Amazon FBA product validation using LaunchFast MCP and the LegacyX criteria. Use when the user wants a serious viability review for a keyword, niche, or adjacent niche expansion."
category: research-and-academic
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/BlockchainHB/launchfast_codex_plugin/skills/product-research/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/BlockchainHB/launchfast_codex_plugin/skills/product-research/SKILL.md
---


# Amazon FBA Product Research

This skill is the deeper, criteria-driven version of `launchfast-product-research`.

## Core criteria

Evaluate every market against these baselines:

| Criteria | Threshold |
|---|---|
| Total niche revenue | > $200,000/month |
| Average price | >= $25, ideally >= $40 |
| Average reviews | <= 500 |
| Revenue per seller | >= $5,000/month |
| Top-seller dominance | top 2-3 sellers < 50% of revenue |
| Search volume | must exist |
| Estimated margin | >= 30% before ad costs |

Large-market exception:

- If niche revenue is above $1M, higher review counts can still be acceptable when multiple sellers under 200 reviews are doing strong revenue.

## Workflow

### 1. Initial scan

Run:

```text
research_products(keyword="<keyword>", focus="balanced", product_limit=20)
```

Extract:

- search volume
- average price
- average reviews
- opportunity score
- market grade
- brand concentration
- dominant brand
- total niche revenue
- average revenue per seller
- top-seller share

### 2. Financial trend check

Run:

```text
research_products(keyword="<keyword>", focus="financial", product_limit=20)
```

Look for:

- growing vs stable vs declining products
- average MoM growth
- short-term momentum using 7d trend fields

### 3. Listing quality check

Run:

```text
research_products(keyword="<keyword>", focus="titles", product_limit=10)
```

Look for:

- low listing quality scores with high revenue
- listing quality gaps
- weak copy or obvious differentiation openings

### 4. Keyword validation

Pick 2-3 relevant ASINs and run:

```text
amazon_keyword_research(asins=["ASIN1", "ASIN2", "ASIN3"], limit=20)
```

Evaluate:

- keyword diversity
- CPC and sponsored density
- purchase rate
- obvious ranking gaps

### 5. Profitability estimate

Present a conservative estimate:

```text
Selling Price
- Amazon Fees (~15%)
- Manufacturing
- Shipping
= Estimated Profit per Unit
= Estimated Margin %
```

If manufacturing cost is unknown, say so and state the assumption used.

## Output format

Use a scorecard first:

```markdown
## Market Scorecard: [keyword]

| Criteria | Threshold | Actual | Status |
|---|---|---|---|
```

Then include:

- market grade
- opportunity score
- trend summary
- verdict: VIABLE, MARGINAL, or NOT RECOMMENDED
- concise rationale

## Rabbit-hole expansion

Use adjacent-niche exploration only when it is helpful:

- identify variations from the first result set
- rerun `research_products` on the most promising adjacent keywords
- keep the branching tight; do not explode the scope without user intent

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/BlockchainHB/launchfast_codex_plugin/skills/product-research/SKILL.md`
