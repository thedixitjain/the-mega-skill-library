---
name: release
description: "Use when the user asks to release, version, tag, or publish."
category: general-purpose
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/ouonet/praxis/skills/release/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/ouonet/praxis/skills/release/SKILL.md
---

# Release

Use only when the user asks to release.

1. Confirm version/bump.
2. Start from green tests and clean tree.
3. Update version files.
4. Move CHANGELOG `Unreleased` to `version - date`; create new `Unreleased`.

`<gate>` Steps 5-7 touch shared or irreversible state. Get explicit user approval before **each** step — never chain them on one confirmation. `</gate>`

5. Commit release edits.
6. Create annotated tag.
7. Push commit/tag, or publish.

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/ouonet/praxis/skills/release/SKILL.md`
