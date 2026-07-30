---
name: audit-bundle-network
description: "Audit a Databricks data-plane VPC for the PrivateLink cost leak — missing S3/STS/Kinesis endpoints that still traverse the NAT — and emit remediation Terraform."
category: security-and-compliance
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "skills/.curated/databricks-bundle-medic/commands/audit-bundle-network.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/skills/.curated/databricks-bundle-medic/commands/audit-bundle-network.md
---


# /audit-bundle-network

Audits a Databricks data-plane VPC for the D9 PrivateLink cost leak using the
`databricks-bundle-medic` skill. Enabling PrivateLink covers the control plane only —
S3, STS, and Kinesis data-plane calls still cross the NAT (billing NAT-processing +
cross-AZ transfer) until each has its own VPC endpoint.

## Usage

```text
/audit-bundle-network [--present s3,sts,kinesis] [--vpc-id <id>] [--region <region>]
```

## What it does

1. Runs `scripts/audit-vpc-endpoints.py` against the endpoints you already have.
2. Reports SAFE, or a COST LEAK finding naming each missing endpoint (S3 → free Gateway
   endpoint; STS + Kinesis → Interface endpoints) with why each service is called and
   the cost line it incurs without an endpoint.
3. Emits ready-to-fill remediation Terraform for the missing endpoints.
4. Points at `references/cost-leak-map.md` for the full per-service map and the
   Azure Private Link / GCP PSC equivalents.

Read-only — it emits a plan and Terraform; it does not change your VPC.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `skills/.curated/databricks-bundle-medic/commands/audit-bundle-network.md`

**Also appears in:** `jeremylongshore/claude-code-plugins-plus-skills/plugins/saas-packs/databricks-pack/skills/databricks-bundle-medic/commands/audit-bundle-network.md`
