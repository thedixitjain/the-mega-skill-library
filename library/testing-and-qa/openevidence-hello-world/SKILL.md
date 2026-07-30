---
name: openevidence-hello-world
description: "'Create a minimal working OpenEvidence example. Trigger: \"openevidence hello world\", \"openevidence example\", \"test openevidence\". '"
allowed-tools: "Read, Write, Edit, Bash(npm:*), Grep"
category: testing-and-qa
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/saas-packs/openevidence-pack/skills/openevidence-hello-world/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/openevidence-pack/skills/openevidence-hello-world/SKILL.md
---

# OpenEvidence Hello World

## Overview

Minimal working examples demonstrating core OpenEvidence API functionality.

## Instructions

### Step 1: Clinical Query

```typescript
const result = await client.query({
  question: 'What is the recommended treatment for acute migraine in adults?',
  context: 'emergency_department',
  evidence_level: 'high',  // Filter by evidence quality
  max_citations: 10
});

console.log('Answer:', result.answer);
console.log('Confidence:', result.confidence);
result.citations.forEach(c =>
  console.log(`  [${c.journal}] ${c.title} (${c.year}) — ${c.evidence_level}`)
);
```

### Step 2: Drug Interaction Check

```typescript
const interactions = await client.interactions.check({
  medications: ['metformin', 'lisinopril', 'atorvastatin'],
  patient_context: { age: 65, conditions: ['diabetes', 'hypertension'] }
});

interactions.forEach(i =>
  console.log(`${i.drug1} + ${i.drug2}: ${i.severity} — ${i.description}`)
);
```

### Step 3: Guideline Lookup

```typescript
const guidelines = await client.guidelines.search({
  condition: 'hypertension',
  source: ['ACC/AHA', 'ESC'],
  year_min: 2023
});
guidelines.forEach(g =>
  console.log(`${g.source}: ${g.title} (${g.year})`)
);
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Auth error | Invalid credentials | Check OPENEVIDENCE_API_KEY |
| Not found | Invalid endpoint | Verify API URL |
| Rate limit | Too many requests | Implement backoff |

## Resources

- [OpenEvidence API Docs](https://www.openevidence.com)

## Next Steps

See `openevidence-local-dev-loop`.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/saas-packs/openevidence-pack/skills/openevidence-hello-world/SKILL.md`
