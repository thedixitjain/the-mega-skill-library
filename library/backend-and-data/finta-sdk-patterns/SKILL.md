---
name: finta-sdk-patterns
description: "'Integration patterns for Finta fundraising CRM with email and calendar APIs. Use when building automated investor outreach, syncing data from Finta exports, or creating custom fundraising dashboards. Trigger with phrases like \"finta integration\", \"finta patterns\", \"finta automation\", \"finta data pipeline\". '"
allowed-tools: "Read, Write, Edit"
category: backend-and-data
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/finta-sdk-patterns/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/finta-sdk-patterns/SKILL.md
---

# Finta SDK Patterns

## Overview

Finta does not expose a public REST API. Integrate via: (1) CSV export + Python processing, (2) email integrations (Gmail/Outlook), (3) Zapier/Make webhooks, or (4) Stripe/payment integrations for capital collection.

## CSV-Based Pipeline Tracker

```python
import pandas as pd
from pathlib import Path

class FintaPipelineTracker:
    def __init__(self, export_path: str):
        self.df = pd.read_csv(export_path)

    def investors_by_stage(self) -> dict:
        return self.df.groupby("Stage")["Name"].apply(list).to_dict()

    def conversion_funnel(self) -> list[dict]:
        stages = self.df["Stage"].value_counts()
        return [{"stage": s, "count": c} for s, c in stages.items()]

    def overdue_followups(self, days: int = 7) -> pd.DataFrame:
        self.df["Last Contact"] = pd.to_datetime(self.df["Last Contact"])
        cutoff = pd.Timestamp.now() - pd.Timedelta(days=days)
        return self.df[
            (self.df["Stage"].isin(["Follow-up", "Due Diligence"]))
            & (self.df["Last Contact"] < cutoff)
        ]

    def total_committed(self) -> float:
        closed = self.df[self.df["Stage"] == "Closed"]
        return closed["Check Size"].sum()
```

## Gmail Integration for Investor Tracking

```python
# Track investor email responses via Gmail API
from googleapiclient.discovery import build

def get_investor_emails(service, investor_email: str, after_date: str):
    query = f"from:{investor_email} after:{after_date}"
    results = service.users().messages().list(
        userId="me", q=query
    ).execute()
    return results.get("messages", [])
```

## Zapier/Make Webhook Pattern

Finta supports Zapier triggers for pipeline stage changes:

1. Create a Zap with "Finta - Pipeline Stage Changed" trigger
2. Connect to your destination (Slack, Sheets, CRM)
3. Map fields: investor name, new stage, deal amount

## Resources

- [Finta Website](https://www.trustfinta.com)
- [Finta Integrations](https://www.trustfinta.com)

## Next Steps

Apply in `finta-core-workflow-a` for fundraise pipeline management.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/finta-sdk-patterns/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/finta-pack/skills/finta-sdk-patterns/SKILL.md`
