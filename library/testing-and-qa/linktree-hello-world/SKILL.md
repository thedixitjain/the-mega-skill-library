---
name: linktree-hello-world
description: "'Create a minimal working Linktree example. Trigger: \"linktree hello world\", \"linktree example\", \"test linktree\". '"
allowed-tools: "Read, Write, Edit, Bash(npm:*), Grep"
category: testing-and-qa
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/saas-packs/linktree-pack/skills/linktree-hello-world/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/linktree-pack/skills/linktree-hello-world/SKILL.md
---

# Linktree Hello World

## Overview

Minimal working examples demonstrating core Linktree API functionality.

## Instructions

### Step 1: Get Profile

```typescript
const profile = await client.profiles.get('myprofile');
console.log(`Bio: ${profile.bio}`);
console.log(`Links: ${profile.links.length}`);
```

### Step 2: Create a Link

```typescript
const link = await client.links.create({
  profile_id: profile.id,
  title: 'My Website',
  url: 'https://example.com',
  position: 0,  // Top of list
  thumbnail: 'https://example.com/icon.png'
});
console.log(`Created link: ${link.id}`);
```

### Step 3: Update Link

```typescript
await client.links.update(link.id, {
  title: 'Updated Title',
  archived: false
});
```

### Step 4: List All Links

```typescript
const links = await client.links.list({ profile_id: profile.id });
links.forEach(l => console.log(`${l.position}: ${l.title} → ${l.url}`));
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| Auth error | Invalid credentials | Check LINKTREE_API_KEY |
| Not found | Invalid endpoint | Verify API URL |
| Rate limit | Too many requests | Implement backoff |

## Resources

- [Linktree API Docs](https://linktr.ee/marketplace/developer)

## Next Steps

See `linktree-local-dev-loop`.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/saas-packs/linktree-pack/skills/linktree-hello-world/SKILL.md`
