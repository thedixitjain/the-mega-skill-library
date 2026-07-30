---
name: launchfast-full-research-loop
description: "| End-to-end Codex-native Amazon FBA research workflow using LaunchFast MCP. Use when the user wants a single report covering product research, IP risk, supplier sourcing, and PPC keyword intelligence. Requires `research_products`, `ip_check_manage`, `supplier_research`, and `amazon_keyword_research`."
category: research-and-academic
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/BlockchainHB/launchfast_codex_plugin/skills/launchfast-full-research-loop/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/BlockchainHB/launchfast_codex_plugin/skills/launchfast-full-research-loop/SKILL.md
---


# LaunchFast Full Research Loop

## Inputs

If needed, ask once for:

- keyword or keyword list
- target selling price
- first order quantity
- optional competitor ASINs
- optional report path

Default report path:

`./artifacts/launchfast/reports/launchfast-report-[keyword]-[YYYY-MM-DD].html`

## Workflow

### 1. Product research

- Run `research_products` for each keyword with `focus="balanced"` and `product_limit=20`.
- Score each keyword using the same logic as `launchfast-product-research`.
- Pick winners for deeper analysis.

### 2. IP check

For promising keywords, run:

```text
ip_check_manage(action="ip_conflict_check", keyword="<keyword>")
ip_check_manage(action="trademark_search", keyword="<keyword>")
```

Extract:

- conflict level
- notable active marks
- patent concerns if present
- final risk posture: CLEAR, CAUTION, or BLOCKED

### 3. Supplier research

For the strongest keyword, run:

```text
supplier_research(keyword="<keyword>", goldSupplierOnly=true, tradeAssuranceOnly=true, maxResults=10)
```

Summarize the top suppliers with:

- company name
- quality score
- price band
- MOQ
- years in business
- trust signals

### 4. PPC research

If you have competitor ASINs, or can responsibly infer 2-3 strong ASINs from product research, run:

```text
amazon_keyword_research(asins=[...], limit=20)
```

Summarize:

- keyword count
- top search-volume terms
- high-intent terms by purchase rate
- indicative CPCs
- suggested campaign structure

If there are no usable ASINs, state that this phase was skipped.

### 5. Build the report

Create a standalone HTML report with:

- executive verdict banner
- market scorecard
- product findings
- IP findings
- supplier findings
- PPC findings
- concise recommendation section

Design should match the existing LaunchFast visual language:

- clean light theme
- neutral palette
- card layout
- compact tables
- clear GO / INVESTIGATE / PASS styling

Write the file to the requested path and report the final file location.

## Output

Always return:

- overall verdict
- key blockers or strengths
- report path if the file was written

Do not pad the response with generic “next steps” unless the evidence clearly supports a specific recommendation.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/BlockchainHB/launchfast_codex_plugin/skills/launchfast-full-research-loop/SKILL.md`
