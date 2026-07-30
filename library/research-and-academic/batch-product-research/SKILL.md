---
name: batch-product-research
description: "| Codex-native batch Amazon keyword research using LaunchFast MCP. Use when the user wants a ranked comparison across many keywords and optionally wants HTML and CSV artifacts written to disk."
category: research-and-academic
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/BlockchainHB/launchfast_codex_plugin/skills/batch-product-research/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/BlockchainHB/launchfast_codex_plugin/skills/batch-product-research/SKILL.md
---


# Batch Product Research

Use this skill for 1-20 keywords.

## Inputs

Accept:

- comma-separated keywords
- numbered lists
- a local file path containing keywords

Defaults:

- maximum 20 keywords per run
- report path: `./artifacts/launchfast/batch-research/report-[YYYY-MM-DD].html`
- csv path: `./artifacts/launchfast/batch-research/report-[YYYY-MM-DD].csv`

## Workflow

### 1. Normalize input

- trim whitespace
- deduplicate case-insensitively
- if there are more than 20 keywords, split into chunks of 20 and process chunk-by-chunk

### 2. Run balanced product research

- run `research_products` for every keyword
- prefer parallel tool calls where practical
- do not require delegation

### 3. Score each keyword

For each keyword compute:

- search volume
- total niche revenue
- average price
- average reviews
- average revenue per seller
- top-seller dominance
- estimated margin using conservative assumptions
- opportunity score and verdict

Use verdicts:

- VIABLE
- MARGINAL
- NOT RECOMMENDED
- ERROR

### 4. Optional deeper passes

For VIABLE or MARGINAL keywords only:

- run `research_products(... focus="financial")`
- optionally run `amazon_keyword_research` on the top 2-3 ASINs if keyword depth matters for the user’s goal

### 5. Present ranked results

Always include a comparison table first.

Then provide concise cards or sections for the strongest keywords.

### 6. Write artifacts when useful

If the user asked for files, or a file materially improves the result:

- write an HTML report
- write a CSV export

Keep the file generation deterministic. Prefer Python for CSV writing.

## Output

At minimum return:

- number of keywords processed
- ranking table
- top recommendations
- artifact paths when files were written

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/BlockchainHB/launchfast_codex_plugin/skills/batch-product-research/SKILL.md`
