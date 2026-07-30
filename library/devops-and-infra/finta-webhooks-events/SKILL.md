---
name: finta-webhooks-events
description: "'Automate Finta pipeline events with Zapier and email triggers. Use when setting up notifications for investor responses, automating follow-up reminders, or syncing events to other tools. Trigger with phrases like \"finta automation\", \"finta notifications\", \"finta pipeline events\", \"finta zapier\". '"
allowed-tools: "Read, Write, Edit"
category: devops-and-infra
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/finta-webhooks-events/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/finta-webhooks-events/SKILL.md
---

# Finta Webhooks & Events

## Overview

Finta supports event automation through its built-in automation rules and Zapier integration. Pipeline stage changes, investor replies, and deal room views can trigger external actions.

## Built-in Automation Rules

Configure in Settings > Automation:

- **Email reply detected** -> Move to next stage
- **Calendar meeting scheduled** -> Log and notify team
- **Deal room viewed** -> Send Slack notification
- **No response in X days** -> Create follow-up reminder

## Zapier Integration

Available triggers:

1. Pipeline stage changed
2. New investor added
3. Deal room accessed
4. Investor update sent

Example Zap: Finta stage change -> Slack message + Google Sheets row

## Custom Reminder System

```python
import pandas as pd
from datetime import datetime, timedelta

def get_followup_reminders(export_path: str, days: int = 5) -> list:
    df = pd.read_csv(export_path)
    df["Last Contact"] = pd.to_datetime(df["Last Contact"])
    cutoff = datetime.now() - timedelta(days=days)
    overdue = df[
        (df["Stage"].isin(["Reaching Out", "Follow-up"]))
        & (df["Last Contact"] < cutoff)
    ]
    return overdue[["Name", "Firm", "Email", "Last Contact", "Stage"]].to_dict("records")
```

## Resources

- [Finta Website](https://www.trustfinta.com)

## Next Steps

For performance, see `finta-performance-tuning`.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/finta-webhooks-events/SKILL.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/finta-pack/skills/finta-webhooks-events/SKILL.md`
