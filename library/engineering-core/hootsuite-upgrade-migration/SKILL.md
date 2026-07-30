---
name: hootsuite-upgrade-migration
description: "'Analyze, plan, and execute Hootsuite SDK upgrades with breaking change detection. Use when upgrading Hootsuite SDK versions, detecting deprecations, or migrating to new API versions. Trigger with phrases like \"upgrade hootsuite\", \"hootsuite migration\", \"hootsuite breaking changes\", \"update hootsuite SDK\", \"analyze hootsuite version\". '"
allowed-tools: "Read, Write, Edit, Bash(npm:*), Bash(git:*)"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/saas-packs/hootsuite-pack/skills/hootsuite-upgrade-migration/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/hootsuite-pack/skills/hootsuite-upgrade-migration/SKILL.md
---

# Hootsuite Upgrade & Migration

## Overview

Hootsuite REST API is versioned at `/v1/`. Monitor the developer changelog for deprecations and new endpoints.

## Instructions

### Step 1: Check Current API Usage

```bash
# List all Hootsuite API calls in your codebase
grep -r "platform.hootsuite.com" src/ --include="*.ts" --include="*.py"
```

### Step 2: Migration Patterns

```typescript
// If Hootsuite introduces v2 endpoints:
// BEFORE
const response = await fetch('https://platform.hootsuite.com/v1/messages', ...);
// AFTER
const API_VERSION = process.env.HOOTSUITE_API_VERSION || 'v1';
const response = await fetch(`https://platform.hootsuite.com/${API_VERSION}/messages`, ...);
```

### Step 3: Social Network Changes

When Hootsuite adds/removes social network support:

```typescript
const SUPPORTED_NETWORKS = ['TWITTER', 'FACEBOOK', 'INSTAGRAM', 'LINKEDIN', 'PINTEREST', 'YOUTUBE', 'TIKTOK'] as const;
type SocialNetwork = typeof SUPPORTED_NETWORKS[number];
```

## Resources

- [Hootsuite Developer Changelog](https://developer.hootsuite.com/changelog)
- [API Guides](https://developer.hootsuite.com/docs/api-guides)

## Next Steps

For CI, see `hootsuite-ci-integration`.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/saas-packs/hootsuite-pack/skills/hootsuite-upgrade-migration/SKILL.md`
