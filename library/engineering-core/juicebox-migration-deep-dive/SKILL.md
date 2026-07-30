---
name: juicebox-migration-deep-dive
description: "'Migrate to Juicebox from other tools. Trigger: \"switch to juicebox\", \"migrate to juicebox\". '"
allowed-tools: "Read, Write, Edit, Grep"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/saas-packs/juicebox-pack/skills/juicebox-migration-deep-dive/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/juicebox-pack/skills/juicebox-migration-deep-dive/SKILL.md
---

# Juicebox Migration Deep Dive

## Comparison

| Feature | LinkedIn Recruiter | Juicebox |
|---------|-------------------|----------|
| Search | Boolean only | Natural language (PeopleGPT) |
| Contact data | InMail only | Email + phone |
| ATS integration | Limited | 41+ systems |
| AI features | Basic | AI Skills Map, research profiles |

## Migration Steps

1. Export saved searches from current tool
2. Translate boolean queries to natural language
3. Re-create talent pools in Juicebox
4. Configure ATS integration
5. Set up outreach sequences

## Query Translation

```
# Boolean: ("software engineer" OR "SWE") AND "Python" AND "San Francisco"
# PeopleGPT: software engineer with Python experience in San Francisco
```

## Resources

- PeopleGPT Guide

## Next Steps

Start with `juicebox-install-auth`.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/saas-packs/juicebox-pack/skills/juicebox-migration-deep-dive/SKILL.md`
