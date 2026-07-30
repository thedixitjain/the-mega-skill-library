---
name: update-infra
description: "Plan and execute infrastructure updates with safety checks and rollback procedures."
category: devops-and-infra
source_repo: rohitg00/awesome-claude-code-toolkit
source_path: "plugins/infrastructure-maintainer/commands/update-infra.md"
source_url: https://github.com/rohitg00/awesome-claude-code-toolkit/blob/HEAD/plugins/infrastructure-maintainer/commands/update-infra.md
---


Plan and execute infrastructure updates with safety checks and rollback procedures.

## Steps


1. Identify what needs updating:
2. Assess update risk:
3. Create the update plan:
4. Prepare the update:
5. Execute the update:
6. Post-update verification:
7. Clean up old resources after confirmation period.

## Format


```
Update: <what is being updated>
From: <current version>
To: <target version>
Risk: <low|medium|high>
```


## Rules

- Always test updates in staging before production.
- Create backups before any destructive update.
- Have a documented rollback procedure ready.

---

**Source:** [`rohitg00/awesome-claude-code-toolkit`](https://github.com/rohitg00/awesome-claude-code-toolkit) → `plugins/infrastructure-maintainer/commands/update-infra.md`
