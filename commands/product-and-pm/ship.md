---
name: ship
description: "Execute a complete feature shipping workflow from code to production deployment."
category: product-and-pm
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/product-shipper/commands/ship.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/product-shipper/commands/ship.md
---


Execute a complete feature shipping workflow from code to production deployment.

## Steps


1. Verify the feature is ready to ship:
2. Prepare the release:
3. Run pre-deployment checks:
4. Deploy to staging:
5. Deploy to production:
6. Post-deployment verification:
7. Announce the release to stakeholders.

## Format


```
Feature: <name>
Version: <version>
Deployment:
  Staging: <status>
```


## Rules

- Never ship without passing tests and code review.
- Always deploy to staging before production.
- Have a documented rollback plan before deploying.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/product-shipper/commands/ship.md`
