---
name: seo-audit
description: "Run a Maestro-style SEO assessment for meta tags, structured data, crawlability, and Core Web Vitals"
category: marketing-and-growth
source_repo: josstei/maestro-orchestrate
source_path: "plugins/maestro/skills/seo-audit/SKILL.md"
source_url: https://github.com/josstei/maestro-orchestrate/blob/HEAD/plugins/maestro/skills/seo-audit/SKILL.md
---


Read `../../references/runtime-guide.md`.
Call `get_skill_content` with resources: ["architecture", "delegation"].
Call `get_agent` with agents: ["seo-specialist"].

## Workflow

1. Define the SEO audit scope (page or site)
2. Identify web-facing output files (HTML, templates, routes)
3. Audit meta tags, schema markup, crawlability, canonicalization, internal linking, and Core Web Vitals
4. Present findings with severity, SEO impact, location, and remediation guidance
5. Note any checks that require live-site verification if the current environment cannot provide it

---

**Source:** [`josstei/maestro-orchestrate`](https://github.com/josstei/maestro-orchestrate) → `plugins/maestro/skills/seo-audit/SKILL.md`
