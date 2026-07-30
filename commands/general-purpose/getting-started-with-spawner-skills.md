---
name: getting-started-with-spawner-skills
description: "┌─────────────────────────────────────────────────────────────────┐ │ │ │ ⚡ VIBESHIP SPAWNER SKILLS │ │ 462 Specialist Skills for AI-Powered Product Building │ │ │ │ You're about to give Claude superpowers. │"
category: general-purpose
source_repo: vibeforge1111/vibeship-spawner-skills
source_path: "GETTING_STARTED.md"
source_url: https://github.com/vibeforge1111/vibeship-spawner-skills/blob/HEAD/GETTING_STARTED.md
---
# Getting Started with Spawner Skills

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   ⚡ VIBESHIP SPAWNER SKILLS                                    │
│   462 Specialist Skills for AI-Powered Product Building         │
│                                                                 │
│   You're about to give Claude superpowers.                      │
│                                                                 │
│   https://spawner.vibeship.co/skills                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## What You Just Installed

```
~/.spawner/skills/
│
├── development/          # 57 skills
│   ├── backend/          # APIs, servers, Node.js
│   ├── frontend/         # React, UI components
│   ├── auth-specialist/  # OAuth, JWT, sessions
│   └── ...
│
├── ai/                   # 12 skills
│   ├── llm-architect/    # LLM integration patterns
│   ├── rag-specialist/   # Retrieval-augmented generation
│   └── ...
│
├── agents/               # 10 skills
│   ├── autonomous-agents/
│   └── multi-agent-orchestration/
│
├── maker/               # 11 skills
│   ├── viral-generator-builder/
│   ├── telegram-bot-builder/
│   └── micro-saas-launcher/
│
└── ... (35 categories, 462 total skills)
```

---

## How to Spawn a Skill

### Step 1: Tell Claude to Load the Skill

Copy and paste this into Claude:

```
Read these files and become a backend specialist:
~/.spawner/skills/development/backend/skill.yaml
~/.spawner/skills/development/backend/sharp-edges.yaml
```

### Step 2: Verify It's Working

After Claude reads the files, it should respond with something like:

```
┌─────────────────────────────────────────────────────────────────┐
│  ✓ SKILL LOADED: Backend Specialist                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  I now have expertise in:                                       │
│  • REST API design patterns                                     │
│  • Node.js/Express/Fastify                                      │
│  • Database integration                                         │
│  • Authentication flows                                         │
│  • Error handling patterns                                      │
│                                                                 │
│  Sharp edges I'm watching for:                                  │
│  • N+1 query problems                                           │
│  • Missing input validation                                     │
│  • Insecure direct object references                            │
│                                                                 │
│  Ready to build. What do you want to create?                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**If Claude doesn't show this visual confirmation**, tell it:

```
After loading a skill, always show a visual confirmation box like this:

┌─────────────────────────────────────────────────────────────────┐
│  ✓ SKILL LOADED: [Skill Name]                                  │
├─────────────────────────────────────────────────────────────────┤
│  I now have expertise in: [list key capabilities]               │
│  Sharp edges I'm watching for: [list gotchas]                   │
│  Ready to build.                                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Quick Spawn Commands

Copy-paste these to spawn common skills:

### Backend API Development
```
Read and become a backend specialist. Show a visual confirmation when loaded:
~/.spawner/skills/development/backend/skill.yaml
~/.spawner/skills/development/backend/sharp-edges.yaml
```

### Frontend UI Development
```
Read and become a frontend specialist. Show a visual confirmation when loaded:
~/.spawner/skills/development/frontend/skill.yaml
~/.spawner/skills/development/frontend/sharp-edges.yaml
```

### Full-Stack SaaS
```
Read these skills and become a full-stack SaaS expert. Show what you're now capable of:
~/.spawner/skills/development/backend/skill.yaml
~/.spawner/skills/development/frontend/skill.yaml
~/.spawner/skills/data/postgres-wizard/skill.yaml
~/.spawner/skills/integration/stripe-billing/skill.yaml
~/.spawner/skills/development/auth-specialist/skill.yaml
```

### AI Agent Building
```
Read these skills and become an AI agent architect. Show what you're now capable of:
~/.spawner/skills/agents/autonomous-agents/skill.yaml
~/.spawner/skills/agents/multi-agent-orchestration/skill.yaml
~/.spawner/skills/ai/llm-architect/skill.yaml
```

---

## Confirming It Works

### Test 1: Ask About Sharp Edges

After spawning a skill, ask:

```
What sharp edges should I watch out for with this stack?
```

If the skill loaded correctly, Claude will list specific gotchas from the sharp-edges.yaml file.

### Test 2: Ask for a Pattern

```
Show me the recommended pattern for [relevant task]
```

Claude should show patterns from the skill's best practices, not generic advice.

### Test 3: Build Something

```
Build me a [small example relevant to the skill]
```

Watch for:
- Does Claude follow the skill's patterns?
- Does it avoid the sharp edges?
- Does it mention skill-specific considerations?

---

## Visual Status Check

Ask Claude anytime:

```
Show me which skills are currently active
```

Claude should display:

```
┌─────────────────────────────────────────────────────────────────┐
│  ACTIVE SKILLS                                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ✓ Backend Specialist     (development/backend)                 │
│  ✓ PostgreSQL Wizard      (data/postgres-wizard)                │
│  ✓ Auth Specialist        (development/auth-specialist)         │
│                                                                 │
│  3 skills loaded | Session started 10 mins ago                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Common Workflows

### Building a SaaS Product

```
┌─────────────────────────────────────────────────────────────────┐
│  WORKFLOW: SaaS Product                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Step 1: Spawn the skills                                       │
│  ────────────────────────                                       │
│  Read and become a full-stack SaaS expert:                      │
│  ~/.spawner/skills/development/backend/skill.yaml               │
│  ~/.spawner/skills/development/frontend/skill.yaml              │
│  ~/.spawner/skills/data/postgres-wizard/skill.yaml              │
│  ~/.spawner/skills/integration/stripe-billing/skill.yaml        │
│  ~/.spawner/skills/development/auth-specialist/skill.yaml       │
│                                                                 │
│  Step 2: Plan                                                   │
│  ────────────────────────                                       │
│  "Plan a SaaS for [your idea]. Show the architecture."          │
│                                                                 │
│  Step 3: Build                                                  │
│  ────────────────────────                                       │
│  "Build the [component]. Follow the skill patterns."            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Building AI Agents

```
┌─────────────────────────────────────────────────────────────────┐
│  WORKFLOW: AI Agent                                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Step 1: Spawn the skills                                       │
│  ────────────────────────                                       │
│  Read and become an AI agent architect:                         │
│  ~/.spawner/skills/agents/autonomous-agents/skill.yaml          │
│  ~/.spawner/skills/agents/multi-agent-orchestration/skill.yaml  │
│  ~/.spawner/skills/ai/llm-architect/skill.yaml                  │
│                                                                 │
│  Step 2: Design                                                 │
│  ────────────────────────                                       │
│  "Design an agent that [your goal]. Show the architecture."     │
│                                                                 │
│  Step 3: Build                                                  │
│  ────────────────────────                                       │
│  "Build the agent. Use the patterns from the skills."           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Skill Categories

```
┌─────────────────────────────────────────────────────────────────┐
│  SKILL CATEGORIES (35 total)                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  game-dev        51 skills    Unity, Godot, Phaser, multiplayer │
│  marketing       36 skills    AI video, copy, SEO, content      │
│  integrations    25 skills    AWS, Stripe, Discord, Slack       │
│  ai              24 skills    LLM, embeddings, RAG, fine-tuning │
│  strategy        24 skills    Growth, product, competitive      │
│  ai-agents       23 skills    Autonomous, multi-agent, RAG      │
│  creative        23 skills    Memes, viral hooks, gamification  │
│  devops          22 skills    CI/CD, Docker, K8s, observability │
│  backend         21 skills    APIs, microservices, caching      │
│  blockchain      20 skills    Smart contracts, DeFi, NFTs       │
│  security        13 skills    Auth, OWASP, compliance           │
│  ai-tools        12 skills    Code gen, image, multimodal       │
│  design          12 skills    UI, UX, branding, landing pages   │
│  frameworks      12 skills    Next.js, React, Svelte, Supabase  │
│  community       11 skills    Discord, Telegram, DevRel         │
│  data            11 skills    Postgres, Redis, vectors, graphs  │
│  maker           11 skills    Viral tools, bots, SaaS, Telegram │
│  mind            10 skills    Debugging, decision-making        │
│  + 17 more categories                                           │
│                                                                 │
│  Total: 462 skills | Browse: spawner.vibeship.co/skills         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Troubleshooting

### "Claude doesn't seem different after loading the skill"

1. Make sure Claude actually read the files (check for any errors)
2. Ask explicitly: "What patterns from the backend skill should we use?"
3. Try: "Apply the sharp edges from your loaded skills to this code"

### "I'm not sure which skill to use"

List all skills:
```bash
npx github:vibeforge1111/vibeship-spawner-skills list
```

Or ask Claude:
```
I want to build [your goal]. Which skills from ~/.spawner/skills/ should I load?
```

### "How do I know skills are working?"

Ask Claude to show its active skills and demonstrate knowledge from them:
```
List your active skills and give me one specific insight from each
```

---

## Updating Skills

New skills are added regularly:

```bash
npx github:vibeforge1111/vibeship-spawner-skills update
```

```
┌─────────────────────────────────────────────────────────────────┐
│  ✓ UPDATE COMPLETE                                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Skills updated: 462 → 470                                      │
│  New skills: 8                                                  │
│                                                                 │
│  • maker/telegram-mini-app                                      │
│  • maker/micro-saas-launcher                                    │
│  • ai-agents/computer-use-agents                                │
│  • game-dev/procedural-generation                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│  SPAWNER SKILLS - QUICK REFERENCE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  INSTALL         npx github:vibeforge1111/vibeship-spawner-skills install  │
│  UPDATE          npx github:vibeforge1111/vibeship-spawner-skills update   │
│  LIST            npx github:vibeforge1111/vibeship-spawner-skills list     │
│  STATUS          npx github:vibeforge1111/vibeship-spawner-skills status   │
│                                                                 │
│  SPAWN A SKILL   "Read: ~/.spawner/skills/[cat]/[skill]/*.yaml" │
│  CHECK ACTIVE    "Show me which skills are currently active"    │
│  TEST SKILL      "What sharp edges should I watch out for?"     │
│                                                                 │
│  DOCS            ~/.spawner/skills/GETTING_STARTED.md           │
│  GITHUB          github.com/vibeforge1111/vibeship-spawner-skills│
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

**Source:** [`vibeforge1111/vibeship-spawner-skills`](https://github.com/vibeforge1111/vibeship-spawner-skills) → `GETTING_STARTED.md`
