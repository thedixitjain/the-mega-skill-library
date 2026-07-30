---
name: hootsuite-reference-architecture
description: "'Implement Hootsuite reference architecture with best-practice project layout. Use when designing new Hootsuite integrations, reviewing project structure, or establishing architecture standards for Hootsuite applications. Trigger with phrases like \"hootsuite architecture\", \"hootsuite best practices\", \"hootsuite project structure\", \"how to organize hootsuite\", \"hootsuite layout\". '"
allowed-tools: "Read, Grep"
category: engineering-core
source_repo: jeremylongshore/claude-code-plugins-plus-skills
source_path: "plugins/saas-packs/hootsuite-pack/skills/hootsuite-reference-architecture/SKILL.md"
source_url: https://github.com/jeremylongshore/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/hootsuite-pack/skills/hootsuite-reference-architecture/SKILL.md
---

# Hootsuite Reference Architecture

## Architecture

```
┌──────────────────────────────────────┐
│         Your Application              │
├──────────────────────────────────────┤
│  Content Manager → Scheduler → Publisher │
├──────────────────────────────────────┤
│      Hootsuite API Client             │
│  (OAuth, Token Refresh, Rate Limit)   │
├──────────────────────────────────────┤
│      Hootsuite REST API v1            │
│  platform.hootsuite.com/v1/           │
└──────────────────────────────────────┘
```

## Project Structure

```
hootsuite-integration/
├── src/
│   ├── hootsuite/
│   │   ├── client.ts        # API client with token management
│   │   ├── auth.ts          # OAuth 2.0 flow
│   │   ├── publishing.ts    # Message scheduling + media
│   │   ├── analytics.ts     # Metrics + URL shortening
│   │   └── types.ts         # TypeScript interfaces
│   ├── services/
│   │   ├── scheduler.ts     # Content calendar logic
│   │   ├── content.ts       # Post formatting per platform
│   │   └── media.ts         # Media processing + upload
│   ├── api/
│   │   └── schedule.ts      # REST endpoint
│   └── store/
│       └── tokens.ts        # Persistent token storage
├── tests/
│   ├── unit/
│   └── fixtures/
└── .env.example
```

## Key Decisions

| Decision | Recommendation | Why |
|----------|---------------|-----|
| Token storage | Database/KV, not env vars | Refresh tokens change each use |
| Scheduling | Queue-based, not direct API | Rate limit compliance |
| Media upload | Pre-process images | Reduce REJECTED media states |
| Multi-profile | Batch schedule per profile | Separate errors per profile |

## Resources

- [Hootsuite Developer Platform](https://developer.hootsuite.com)
- [API Overview](https://developer.hootsuite.com/docs/api-overview)

## Next Steps

Start with `hootsuite-install-auth` to set up OAuth.

---

**Source:** [`jeremylongshore/claude-code-plugins-plus-skills`](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) → `plugins/saas-packs/hootsuite-pack/skills/hootsuite-reference-architecture/SKILL.md`
