---
name: security-audit
description: "Run a Maestro-style security assessment for authentication, authorization, data exposure, secret handling, and exploitability risks"
category: security-and-compliance
source_repo: josstei/maestro-orchestrate
source_path: "plugins/maestro/skills/security-audit/SKILL.md"
source_url: https://github.com/josstei/maestro-orchestrate/blob/HEAD/plugins/maestro/skills/security-audit/SKILL.md
---


Read `../../references/runtime-guide.md`.
Call `get_skill_content` with resources: ["architecture", "delegation"].
Call `get_agent` with agents: ["security-engineer"].

## Workflow

1. Define the audit scope from the user request and relevant code paths
2. Trace trust boundaries, auth flows, secret handling, and data exposure paths
3. Review for exploitable flaws, unsafe defaults, OWASP Top 10 vulnerabilities, and high-risk dependencies
4. Classify findings by severity (CVSS-aligned) with file references and exploitability assessment
5. Provide remediation guidance with the highest-risk issues first

---

**Source:** [`josstei/maestro-orchestrate`](https://github.com/josstei/maestro-orchestrate) → `plugins/maestro/skills/security-audit/SKILL.md`
