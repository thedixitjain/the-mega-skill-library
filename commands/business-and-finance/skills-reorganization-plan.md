---
name: skills-reorganization-plan
description: "- data (12) - frameworks (11) - integrations (25) - game-development → rename to game-dev (40) - blockchain (20) - marketing (43) - strategy (18) - product (7) - mind (10) - trading (6) - biotech (6) - space (5) - climate (5) - hardware (6) - finance (6) - legal (5) - science (4) - simulation (5) - enterprise (6) - communications (5)"
category: business-and-finance
source_repo: vibeforge1111/vibeship-spawner-skills
source_path: "REORGANIZATION_PLAN.md"
source_url: https://github.com/vibeforge1111/vibeship-spawner-skills/blob/HEAD/REORGANIZATION_PLAN.md
---
# Skills Reorganization Plan
## Current: 476 skills across 32 categories
## Target: 476 skills across 28 categories

---

## Categories That Stay As-Is (19 categories, ~180 skills)
- data (12)
- frameworks (11)
- integrations (25)
- game-development → rename to game-dev (40)
- blockchain (20)
- marketing (43)
- strategy (18)
- product (7)
- mind (10)
- trading (6)
- biotech (6)
- space (5)
- climate (5)
- hardware (6)
- finance (6)
- legal (5)
- science (4)
- simulation (5)
- enterprise (6)
- communications (5)

---

## Merges

### 1. AI (merge ai + ai-ml) → 26 skills
FROM ai (12):
- ai-code-generation
- ai-image-editing
- ai-music-audio
- ai-observability
- ai-personalization
- ai-safety-alignment
- document-ai
- multimodal-ai
- on-device-ai
- semantic-search
- synthetic-data
- text-to-video

FROM ai-ml (14):
- art-consistency
- causal-scientist
- computer-vision-deep
- distributed-training
- llm-architect
- llm-fine-tuning
- ml-memory
- model-optimization
- neural-architecture-search
- nlp-advanced
- reinforcement-learning
- transformer-architecture

### 2. CREATIVE (merge vibe-lab + survival-kit + creative-tech) → 23 skills
FROM vibe-lab (11):
- absurdist-voice
- anti-marketing
- cliffhanger-craft
- cultural-remix
- easter-egg-design
- gamification-loops
- lore-building
- meme-engineering
- roast-writing
- viral-hooks

FROM survival-kit (10):
- code-review-diplomacy
- demo-day-theater
- documentation-that-slaps
- git-time-travel
- incident-postmortem
- legacy-archaeology
- regex-whisperer
- scope-creep-defense
- side-project-shipping
- tech-debt-negotiation

FROM creative-tech (3):
- demoscene-coding
- generative-art
- hand-gesture-recognition

---

## Development Split (91 skills → 5 new categories)

### BACKEND (~25 skills)
- backend
- database-architect
- api-design
- api-designer
- graphql-architect
- microservices-patterns
- queue-workers
- rate-limiting
- caching-patterns
- event-architect
- realtime-engineer
- websocket-realtime
- websockets-realtime
- python-backend
- python-craftsman
- rust-craftsman
- error-handling
- structured-output
- prisma
- infrastructure-as-code
- monorepo-management

### FRONTEND (~15 skills)
- frontend
- state-management
- react-native-specialist
- ios-swift-specialist
- expo
- v0-dev
- cursor-ai
- accessibility

### SECURITY (~12 skills)
- security
- security-hardening
- security-owasp
- cybersecurity
- auth-specialist
- authentication-oauth
- privacy-guardian
- supabase-security
- ai-code-security
- llm-security-audit
- prompt-injection-defense
- smart-contract-engineer
- wallet-integration

### DEVOPS (~20 skills)
- devops
- docker
- docker-containerization
- docker-specialist
- kubernetes
- kubernetes-deployment
- infra-architect
- ci-cd-pipeline
- cicd-pipelines
- mcp-deployment
- mcp-developer
- mcp-product
- mcp-security
- mcp-server-development
- mcp-testing
- claude-code-cicd
- claude-code-commands
- claude-code-hooks
- observability
- observability-sre
- logging-strategies
- git-workflow

### TESTING (~8 skills)
- test-architect
- testing-automation
- testing-strategies
- qa-engineering
- code-review
- code-reviewer
- code-architecture-review
- chaos-engineer

### AI-AGENTS (~20 skills)
FROM agents (8):
- agent-evaluation
- agent-memory-systems
- agent-tool-builder
- autonomous-agents
- browser-automation
- computer-use-agents
- multi-agent-orchestration
- voice-agents
- workflow-automation

FROM development (AI-related):
- ai-agents-architect
- ai-product
- agent-communication
- crewai
- langfuse
- langgraph
- rag-engineer
- rag-implementation
- prompt-engineer
- prompt-caching
- context-window-management
- conversation-memory
- voice-ai-development
- zapier-make-patterns

### Remaining in DEVELOPMENT (~10 skills, general)
- docs-engineer
- sdk-builder
- migration-specialist
- performance-hunter
- performance-optimization
- codebase-optimization
- code-cleanup
- technical-debt-strategy

### Game-related (move to game-dev)
- game-development
- game-ai-behavior-trees
- llm-game-development
- llm-npc-dialogue
- godot-llm-integration
- unity-llm-integration
- unreal-llm-integration
- procedural-generation

---

## Final Category Count: 28

1. backend
2. frontend
3. ai
4. ai-agents
5. data
6. security
7. devops
8. testing
9. frameworks
10. integrations
11. game-dev
12. blockchain
13. marketing
14. strategy
15. product
16. design
17. mind
18. creative
19. trading
20. biotech
21. space
22. climate
23. hardware
24. finance
25. legal
26. science
27. simulation
28. enterprise

Note: communications (5 skills) merged into marketing or kept as 29th category

---

**Source:** [`vibeforge1111/vibeship-spawner-skills`](https://github.com/vibeforge1111/vibeship-spawner-skills) → `REORGANIZATION_PLAN.md`
