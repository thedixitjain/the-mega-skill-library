---
name: intro-example
description: "Minimal MDA source demonstrating relationship-graph footnotes and metadata.mda.* MDA-extended fields. Use as a reference fixture when learning the MDA source format."
category: general-purpose
source_repo: sno-ai/mda
source_path: "examples/skill-md/intro/SKILL.md"
source_url: https://github.com/sno-ai/mda/blob/HEAD/examples/skill-md/intro/SKILL.md
---


# Intro

This is a minimal MDA source file. It demonstrates MDA-extended frontmatter
fields at the top level and the relationship-graph footnote pattern.

## A relationship

This document references the SKILL.md target schema as its conceptual parent[^skill-md-spec].

[^skill-md-spec]: {"rel-type": "parent", "doc-id": "spec-skill-md-v1.0", "rel-desc": "MDA SKILL.md target schema"}

---

**Source:** [`sno-ai/mda`](https://github.com/sno-ai/mda) → `examples/skill-md/intro/SKILL.md`
