---
name: ringcentral-automation
description: "RingCentral automation via Rube MCP -- toolkit not currently available in Composio; no RING_CENTRAL_ tools found"
category: mcp-and-integrations
source_repo: ComposioHQ/awesome-claude-skills
source_path: "composio-skills/ring-central-automation/SKILL.md"
source_url: https://github.com/ComposioHQ/awesome-claude-skills/blob/HEAD/composio-skills/ring-central-automation/SKILL.md
---


# RingCentral Automation

> **Status: Toolkit Not Available** -- RUBE_SEARCH_TOOLS returned no `ring_central`-specific tools. The RingCentral toolkit is not currently available in Composio's tool catalog. Searches returned tools from unrelated toolkits (ClickSend, Telnyx, Slack) instead.

**Toolkit docs:** [composio.dev/toolkits/ring_central](https://composio.dev/toolkits/ring_central)

---

## Setup

1. Add the Rube MCP server to your environment: `https://rube.app/mcp`
2. Check availability by calling `RUBE_SEARCH_TOOLS` with RingCentral-related queries
3. If `RING_CENTRAL_*` tools appear in the future, connect via `RUBE_MANAGE_CONNECTIONS` with toolkit `ring_central`

---

## Current Status

As of the last tool discovery scan, no `RING_CENTRAL_*` tool slugs were returned by RUBE_SEARCH_TOOLS. Queries for RingCentral messaging, call logs, fax, and extension management all returned tools from other toolkits:

- SMS/messaging queries returned **ClickSend** tools (`CLICKSEND_CREATE_SMS_SEND`, etc.)
- Call management queries returned **Pipedrive** call log tools
- Telephony/VoIP queries returned **Telnyx** notification tools
- Fax queries returned **ClickSend** fax automation tools

This indicates the `ring_central` toolkit either has no tools registered or is not yet integrated into the Composio platform.

---

## Alternatives

If you need telephony, SMS, or communication automation, consider these available toolkits:

| Need | Alternative Toolkit | Example Tool |
|------|-------------------|--------------|
| SMS messaging | ClickSend | `CLICKSEND_CREATE_SMS_SEND` |
| VoIP/telephony | Telnyx | `TELNYX_CREATE_NOTIFICATION_CHANNEL` |
| Team messaging | Slack / Webex | `SLACK_SEND_MESSAGE` / `WEBEX_MESSAGING_CREATE_MESSAGE` |

---

## When Tools Become Available

Once RingCentral tools are added to Composio, this skill should be updated with real tool slugs, schemas, and pitfalls following the same pattern as other automation skills in this collection.

---

*Powered by [Composio](https://composio.dev)*

---

**Source:** [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) → `composio-skills/ring-central-automation/SKILL.md`

**Also appears in:** `composio-community/awesome-codex-skills/composio-skills/ring-central-automation/SKILL.md`
