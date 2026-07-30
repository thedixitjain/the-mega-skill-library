---
name: kunze-ad-setup
description: "| Codex-native Amazon PPC setup workflow using Kunze's broader ecosystem-driven strategy. Use when the user wants LaunchFast-driven bulk-sheet generation with broad and phrase coverage, gap analysis, and a campaign package written to disk."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/BlockchainHB/launchfast_codex_plugin/skills/kunze-ad-setup/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/BlockchainHB/launchfast_codex_plugin/skills/kunze-ad-setup/SKILL.md
---


# Kunze Ad Setup

## Inputs

Ask once for:

- main keyword
- product SKU
- optional product name
- optional budget level: conservative or aggressive
- optional output path

Defaults:

- budget level: conservative
- output directory: `./artifacts/launchfast/campaigns/`

## Strategy

Kunze’s model favors:

- broad and phrase coverage
- one ad group per campaign
- small keyword sets
- gap-opportunity terms where competitors rank poorly

## Workflow

### 1. Market research

Run:

```text
research_products(keyword="<main_keyword>", focus="balanced", product_limit=20)
```

Collect top 10-15 competitor ASINs plus market context.

### 2. Keyword research

- Research competitor ASINs in manageable batches of 3-4.
- Prefer parallel tool calls where possible.
- Do not require delegation.

Use:

```text
amazon_keyword_research(asins=[...], limit=50, min_search_volume=300)
```

### 3. Build the keyword master list

For each keyword compute:

- overlap across ASIN batches
- search volume
- CPC
- purchase rate
- relevance
- competitor coverage
- gap-opportunity signal

Then select:

- Broad campaign keywords
- Phrase campaign keywords
- ASIN targets
- Category target placeholder if category ID is unknown

### 4. Generate bulksheet

Create:

- Auto campaign
- Broad campaign
- Phrase campaign
- Category targeting campaign
- ASIN targeting campaign

Use deterministic CSV generation with Python `csv.writer`.

Use this exact Amazon Bulksheets 2.0 header and column order:

```text
Product,Entity,Operation,Campaign Id,Ad Group Id,Portfolio Id,Ad Id,Keyword Id,Product Targeting Id,Campaign Name,Ad Group Name,Start Date,End Date,Targeting Type,State,Daily Budget,sku,asin,Ad Group Default Bid,Bid,Keyword Text,Match Type,Bidding Strategy,Placement,Percentage,Product Targeting Expression,Audience ID,Shopper Cohort Percentage,Shopper Cohort Type
```

Deterministic campaign layout:

- Auto: 1 campaign, 1 ad group, 1 product ad, 4 auto targeting rows
- Broad: 1 campaign, 1 ad group, 1 product ad, up to 5 broad-match keywords
- Phrase: 1 campaign, 1 ad group, 1 product ad, up to 5 phrase-match keywords
- Category: 1 campaign, 1 ad group, 1 product ad, 1 category targeting row
- ASIN: 1 campaign, 1 ad group, 1 product ad, up to 15 ASIN target rows

Required defaults:

- start date: current date in `YYYYMMDD`
- bidding strategy: `Dynamic bids - down only`
- one ad group per campaign
- if category ID is unknown, emit a literal placeholder such as `[CATEGORY_ID]`

Write to:

`./artifacts/launchfast/campaigns/[product-name]-kunze-[YYYY-MM-DD].csv`

### 5. Provide an operator summary

Return:

- campaign list
- selected keywords
- budget assumptions
- output file path

If a category ID is missing, leave a clear placeholder and call it out explicitly.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/BlockchainHB/launchfast_codex_plugin/skills/kunze-ad-setup/SKILL.md`
