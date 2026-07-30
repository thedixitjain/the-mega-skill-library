---
name: refi-quote
description: "Mortgage refinance quote, analysis, and application submission"
category: general-purpose
source_repo: davepoon/buildwithclaude
source_path: "plugins/mortgage/commands/refi-quote.md"
source_url: https://github.com/davepoon/buildwithclaude/blob/HEAD/plugins/mortgage/commands/refi-quote.md
---


# /refi-quote

Complete mortgage refinance workflow from data collection through application submission. Guides borrowers through a structured, compliance-aware conversation.

## Workflow

| Phase | Name | Purpose |
|-------|------|---------|
| 1 | Data Collection | Upload mortgage statement, extract data, interview borrower, validate inputs |
| 2 | Pricing | Call mortgage pricing engine via MCP, handle response and errors |
| 3 | Analysis & Recommendation | Savings breakdown, breakeven analysis, weighted recommendation scoring |
| 4 | Application | Direct borrower to secure application portal |

## Example

```
/mortgage:refi-quote
```

**User**: "I'd like to refinance my home in Georgia"

The assistant will:
1. Request the borrower's mortgage statement or ask interview questions
2. Collect property details, credit score range, loan balance, current rate
3. Call the pricing engine for real-time institutional rates
4. Present a comparison table with savings analysis and recommendation score
5. Offer to direct the borrower to the secure application portal

## Features

- Automatic FHA Streamline and VA IRRRL detection
- State-specific closing cost calculation for 10 states
- Weighted recommendation scoring (1-10 scale)
- Full regulatory compliance (TRID, RESPA, TILA, ECOA)
- Prompt injection defense on uploaded documents
- PII protection (no SSN/DOB collection in chat)

## Installation

This command is part of the mortgage plugin. Install via:

```
/plugin marketplace add lendtrain/mortgage
/plugin install mortgage@mortgage
```

Full source: [github.com/lendtrain/mortgage](https://github.com/lendtrain/mortgage)

---

**Source:** [`davepoon/buildwithclaude`](https://github.com/davepoon/buildwithclaude) → `plugins/mortgage/commands/refi-quote.md`
