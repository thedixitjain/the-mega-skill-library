---
name: alphaear-deepear-lite
description: "Fetch the latest financial signals and transmission-chain analyses from DeepEar Lite. Use when the user needs immediate insights into financial market trends, stock performance factors, and reasoning from the DeepEar Lite dashboard."
category: business-and-finance
source_repo: RKiding/Awesome-finance-skills
source_path: "skills/alphaear-deepear-lite/SKILL.md"
source_url: https://github.com/RKiding/Awesome-finance-skills/blob/HEAD/skills/alphaear-deepear-lite/SKILL.md
---


# DeepEar Lite Skill

## Overview

Fetch high-frequency financial signals, including titles, summaries, confidence scores, and reasoning directly from the DeepEar Lite platform's real-time data source.

## Capabilities

### 1. Fetch Latest Financial Signals

Use `scripts/deepear_lite.py` via `DeepEarLiteTools`.

-   **Fetch Signals**: `fetch_latest_signals()`
    -   Retrieves all latest signals from `https://deepear.vercel.app/latest.json`.
    -   Returns a formatted report of signal titles, sentiment/confidence metrics, summaries, and source links.

## Dependencies

-   `requests`, `loguru`
-   No local database required for this skill.

## Testing

Run the test script to verify the connection and data fetching:
```bash
python scripts/deepear_lite.py
```

---

**Source:** [`RKiding/Awesome-finance-skills`](https://github.com/RKiding/Awesome-finance-skills) → `skills/alphaear-deepear-lite/SKILL.md`
