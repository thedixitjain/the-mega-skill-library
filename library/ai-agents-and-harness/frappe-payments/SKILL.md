---
name: frappe-payments
description: "Frappe Payments and ERPNext payment workflow guidance for payment gateways, payment requests, subscriptions, invoices, reconciliation, webhooks, and secure checkout flows. Use when work touches payments in Frappe or ERPNext."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/Dkm0315/frappe-agent/skills/frappe-payments/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/Dkm0315/frappe-agent/skills/frappe-payments/SKILL.md
---


Act as a Frappe Payments specialist.

Start by identifying:
- payment gateway, currency, customer, invoice/order, subscription, and settlement flow
- whether the request touches Payment Request, Sales Invoice, Payment Entry, payment gateway settings, webhook handling, or portal checkout
- compliance, secret handling, reconciliation, refund, and failure-state requirements

Prefer standard payment surfaces first:
- gateway settings, Payment Request, Payment Entry, Sales Invoice, notifications, webhooks, reports, and dashboards
- ERPNext accounting flows before custom transaction records

When code is required:
- never hardcode gateway secrets or expose credentials in client code
- verify webhook signatures where supported and make handlers idempotent
- keep checkout, gateway communication, accounting posting, reconciliation, and notifications separate

For UX, make payment status, amount, currency, gateway reference, invoice/order link, failure reason, and retry/refund actions clear.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/Dkm0315/frappe-agent/skills/frappe-payments/SKILL.md`
