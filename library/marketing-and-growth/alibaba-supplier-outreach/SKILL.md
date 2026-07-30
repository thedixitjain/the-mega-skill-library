---
name: alibaba-supplier-outreach
description: "| Codex-native supplier sourcing and outreach workflow for Alibaba using LaunchFast research. Use when the user wants supplier shortlists, outreach messages, reply triage, or negotiation support. Requires `supplier_research`. Browser automation is optional but useful when the user wants Codex to interact with Alibaba directly."
category: marketing-and-growth
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/BlockchainHB/launchfast_codex_plugin/skills/alibaba-supplier-outreach/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/BlockchainHB/launchfast_codex_plugin/skills/alibaba-supplier-outreach/SKILL.md
---


# Alibaba Supplier Outreach

This skill has three modes: outreach, reply review, and follow-up drafting.

## Mode detection

- Product keyword or “find suppliers” -> OUTREACH
- “check replies”, “any responses” -> REPLY REVIEW
- “follow up”, “reply to supplier” -> FOLLOW-UP

## Shared defaults

Use these defaults when the user does not care:

- first order quantity: 500 units
- shortlist size: top 5 suppliers
- conversation notes path: `./artifacts/launchfast/supplier-conversations/`

## OUTREACH

### 1. Gather context

Ask once for:

- product keyword
- target price or landed-cost goal
- target first order quantity
- sign-off name or company
- optional Amazon selling experience

### 2. Research suppliers

Run:

```text
supplier_research(keyword="<keyword>", goldSupplierOnly=true, tradeAssuranceOnly=true, maxResults=10)
```

Present a compact shortlist with:

- supplier name
- quality score
- price
- MOQ
- years in business
- trust signals

### 3. Draft the outreach

Use this structure:

1. Mention the supplier by name and one concrete credibility signal.
2. Establish buyer credibility briefly.
3. State quantity and target pricing clearly.
4. Ask exactly 3 questions:
   - best price at target quantity
   - lead time
   - private-label capability
5. End with a warm but direct close.

Always show the message to the user before sending it anywhere.

### 4. Browser automation, if requested

If the user wants Codex to send messages and browser automation tools are available, use this concrete flow:

1. Open Alibaba in the browser automation session.
2. Confirm the user is already logged in before proceeding.
3. Navigate to the supplier page or Alibaba messaging UI.
4. Use page inspection or accessibility snapshot tooling to find the `Contact Supplier` or reply form.
5. Click into the message textarea and paste the approved message verbatim.
6. Submit the form.
7. Confirm success by checking for a sent-state confirmation or the new message appearing in the thread.
8. Save the conversation summary to the local notes path.

If browser automation is unavailable, stop after drafting the approved message set.

### 5. Save notes

Store outreach notes under:

`./artifacts/launchfast/supplier-conversations/[supplier-slug]/conversation.md`

Keep a simple index file at:

`./artifacts/launchfast/supplier-conversations/index.md`

## REPLY REVIEW

When the user asks to check replies:

- use browser automation if available and authenticated
- open Alibaba messages
- inspect the conversation list for unread or recent threads
- open each relevant thread
- extract pricing, MOQ, lead time, sample terms, and direct supplier questions
- summarize supplier-by-supplier
- update the conversation note files

If browser automation is unavailable, ask the user to provide exported text or screenshots and continue from that material.

## FOLLOW-UP

When drafting or sending a reply:

- read the relevant conversation note file first if it exists
- preserve negotiation context
- answer supplier questions directly
- push toward quote clarity, samples, lead time, packaging, and payment terms
- ask for approval before sending any reply through the browser

If browser automation is used for the send:

1. Open the supplier thread.
2. Locate the reply textarea.
3. Paste the approved response.
4. Submit.
5. Verify the message appears in the thread.
6. Update the local notes file with the sent reply and timestamp.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/BlockchainHB/launchfast_codex_plugin/skills/alibaba-supplier-outreach/SKILL.md`
