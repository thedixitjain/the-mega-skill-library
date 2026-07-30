---
name: revoke-override
description: "Revoke a previously-created AxonFlow session override — emits an audit event and ensures subsequent policy evaluations no longer consult it"
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/getaxonflow/axonflow-codex-plugin/skills/revoke-override/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/getaxonflow/axonflow-codex-plugin/skills/revoke-override/SKILL.md
---


Use this skill when a user is done with the work that needed an override and wants to tear it down explicitly rather than waiting for it to expire.

Required argument: `override_id` (typically obtained from `list-overrides` or returned by `create-override`).

Call the `delete_override` MCP tool. The platform records an `override_revoked` audit event so the revocation is part of the compliance trail.

After revocation:

- The next policy evaluation will not consult the revoked override
- The override remains visible via `list-overrides` only when `include_revoked=true`
- An attempt to revoke an already-revoked or non-existent override returns 404; surface this as "override not found or already revoked" rather than a hard error

Confirm to the user: "Override `<id>` revoked. The previously-blocked tool will now require a fresh override or policy change before it succeeds."

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/getaxonflow/axonflow-codex-plugin/skills/revoke-override/SKILL.md`
