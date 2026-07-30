---
name: node-tools
description: "Run a TypeScript script via tsx to fetch an HTTP endpoint and stream the response. Use when you need a small Node.js helper for HTTP calls."
category: general-purpose
source_repo: sno-ai/mda
source_path: "examples/skill-md/node-tools/SKILL.md"
source_url: https://github.com/sno-ai/mda/blob/HEAD/examples/skill-md/node-tools/SKILL.md
---


# Node Tools

This is the compiled SKILL.md form of `examples/source-only/node-tools.mda`.
The MDA-extended top-level fields are relocated under `metadata.mda.*`, and
the typed footnote is mirrored to `metadata.mda.relationships`. The output is
acceptable to any agentskills.io v1 consumer.

A consumer that recognizes `metadata.mda.requires` (§10) can decide
programmatically whether it can satisfy `runtime: ["node>=20"]`,
`network: ["api.example.com"]`, and the `tsx` / `undici` packages before
activating the skill.

## A relationship

This skill cites the MDA capabilities specification[^capabilities-spec].

[^capabilities-spec]: {"rel-type": "cites", "doc-id": "spec-capabilities-v1.0", "rel-desc": "MDA capabilities (metadata.mda.requires) reference"}

---

**Source:** [`sno-ai/mda`](https://github.com/sno-ai/mda) → `examples/skill-md/node-tools/SKILL.md`
