---
name: launchfast-ppc-research
description: "| Codex-native Amazon PPC keyword research using LaunchFast MCP. Use when the user wants competitor keyword discovery, keyword tiering, or a ready-to-upload Amazon Sponsored Products bulk file from 1-15 ASINs. Requires the LaunchFast MCP tool `amazon_keyword_research`."
category: marketing-and-growth
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/BlockchainHB/launchfast_codex_plugin/skills/launchfast-ppc-research/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/BlockchainHB/launchfast_codex_plugin/skills/launchfast-ppc-research/SKILL.md
---


# LaunchFast PPC Research

## Inputs

If needed, ask once for:

- 1-15 ASINs
- optional campaign name
- optional default CPC bid
- optional daily budget
- optional output path

Defaults:

- campaign name: `LaunchFast-PPC-[YYYY-MM-DD]`
- default bid: `0.75`
- daily budget: `25`
- output path: `./artifacts/launchfast/ppc/launchfast-ppc-[YYYY-MM-DD].tsv`

## Workflow

### 1. Run keyword research

Run one keyword-research call across all ASINs when possible:

```text
amazon_keyword_research(asins=[...], limit=50)
```

If the ASIN set is too large or results are unwieldy, batch them, but do not require delegation.

### 2. Normalize and tier keywords

For each keyword:

- deduplicate across ASIN overlaps
- keep overlap count
- capture search volume, CPC, purchase rate, relevance, and ranking coverage

Tiering:

- Tier 1: high-value terms with strong overlap or standout volume and conversion
- Tier 2: mid-volume growth terms
- Tier 3: discovery and long-tail terms

Match mapping:

- Exact: Tier 1
- Phrase: Tier 1 and Tier 2
- Broad: Tier 2 and Tier 3

Bid guidance:

- Exact: default bid * 1.2
- Phrase: default bid * 1.0
- Broad: default bid * 0.7

### 3. Present a preview

Show:

- ASINs analyzed
- unique keywords found
- tier breakdown
- top 15 keywords preview
- negative keywords or exclusions if obvious

### 4. Generate the bulk file

If the user wants the export, create the parent directory and write a TSV.

Use a deterministic writer such as Python `csv.writer` with a tab delimiter.

Required output:

- one campaign
- ad groups split by tier and match type
- keyword rows with bids

Default to this exact tab-separated header and column order:

```text
Product	Entity	Operation	Campaign ID	Ad Group ID	Portfolio ID	Ad ID	Keyword ID	Product Targeting ID	Campaign Name	Ad Group Name	Start Date	End Date	Targeting Type	State	Daily Budget	SKU	ASIN	Ad Group Default Bid	Bid	Custom Text	Campaign Type	Targeting Expression
```

Deterministic campaign structure:

- `Tier1-Exact`: Tier 1 keywords as Exact
- `Tier1-Phrase`: Tier 1 keywords as Phrase
- `Tier2-Phrase`: Tier 2 keywords as Phrase
- `Tier3-Broad`: Tier 2 and Tier 3 keywords as Broad

Generate three row types only:

- Campaign row: one per campaign
- Ad Group row: one per ad group
- Keyword row: one per keyword and match-type pair

Use:

- `Start Date`: current date in `YYYYMMDD`
- `Targeting Type`: `Manual`
- `State`: `enabled`
- `Campaign Type`: `Sponsored Products`

If the user requests a different Amazon bulk format, switch only with explicit confirmation.

## Output

Default answer structure:

- short summary of keyword landscape
- preview table
- export path and row count if a file was written

If no export is requested, stop after the preview and recommendations.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/BlockchainHB/launchfast_codex_plugin/skills/launchfast-ppc-research/SKILL.md`
