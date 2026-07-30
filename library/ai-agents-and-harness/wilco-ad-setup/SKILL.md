---
name: wilco-ad-setup
description: "| Codex-native Amazon PPC setup workflow using Wilco's exact-match and analytics-first strategy. Use when the user wants stricter keyword control, exact-match campaigns, and a LaunchFast-driven bulk-sheet export."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/BlockchainHB/launchfast_codex_plugin/skills/wilco-ad-setup/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/BlockchainHB/launchfast_codex_plugin/skills/wilco-ad-setup/SKILL.md
---


# Wilco Ad Setup

## Inputs

Ask once for:

- main keyword
- product SKU
- optional product name
- optional budget level
- optional output path

Defaults:

- budget level: conservative
- output directory: `./artifacts/launchfast/campaigns/`

## Strategy

Wilco’s model favors:

- exact match only for manual keyword campaigns
- tight budget isolation
- proven converting keywords
- strong emphasis on purchase rate and competitor coverage

## Workflow

### 1. Market research

Run:

```text
research_products(keyword="<main_keyword>", focus="balanced", product_limit=20)
```

Capture top 10-12 ASINs and market context.

### 2. Keyword research

- batch ASINs in groups of 3-4
- prefer parallel tool calls when practical
- do not require delegation

Use:

```text
amazon_keyword_research(asins=[...], limit=50, min_search_volume=300)
```

### 3. Score keywords

Rank keywords with a weighted score based on:

- purchase rate
- competitor coverage
- search volume
- relevance

Prioritize keywords where multiple competitors already rank well.

Select:

- Exact A: top converters
- Exact B: volume converters
- Exact C: niche converters
- Product targets: top competitor ASINs

### 4. Generate bulksheet

Create:

- Auto campaign
- Product targeting campaign
- 3 exact-match manual campaigns

Use Python `csv.writer` and write to:

Use this exact Amazon Bulksheets 2.0 header and column order:

```text
Product,Entity,Operation,Campaign Id,Ad Group Id,Portfolio Id,Ad Id,Keyword Id,Product Targeting Id,Campaign Name,Ad Group Name,Start Date,End Date,Targeting Type,State,Daily Budget,sku,asin,Ad Group Default Bid,Bid,Keyword Text,Match Type,Bidding Strategy,Placement,Percentage,Product Targeting Expression,Audience ID,Shopper Cohort Percentage,Shopper Cohort Type
```

Deterministic campaign layout:

- Auto: 1 campaign, 1 ad group, 1 product ad, 4 auto targeting rows
- Product targeting: 1 campaign, 1 ad group, 1 product ad, up to 10 ASIN target rows
- Exact A: 1 campaign, 1 ad group, 1 product ad, up to 5 exact-match keywords
- Exact B: 1 campaign, 1 ad group, 1 product ad, up to 5 exact-match keywords
- Exact C: 1 campaign, 1 ad group, 1 product ad, up to 5 exact-match keywords

Required defaults:

- start date: current date in `YYYYMMDD`
- bidding strategy: `Dynamic bids - down only`
- one ad group per campaign
- exact match for all three manual keyword campaigns

`./artifacts/launchfast/campaigns/[product-name]-wilco-[YYYY-MM-DD].csv`

### 5. Return summary

Include:

- why Wilco is a better fit or not for this niche
- keyword selection logic
- bids and budget assumptions
- export path

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/BlockchainHB/launchfast_codex_plugin/skills/wilco-ad-setup/SKILL.md`
