---
name: game-story-world-character
description: "Design or evaluate game story, world, characters, spaces, presence, aesthetics, and indirect control. Use when adding narrative, quests, levels, environments, character arcs, worldbuilding, environmental storytelling, or emotional context to gameplay."
category: media-and-creative
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/LVTD-LLC/skills/skills/game-story-world-character/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/LVTD-LLC/skills/skills/game-story-world-character/SKILL.md
---


# Game Story World Character

Use this skill to make narrative and world design serve play instead of competing with it. The output should give the coding agent clear content structures, state needs, triggers, and constraints.

## Source Traceability

Primary source: *The Art of Game Design: A Book of Lenses, Third Edition* by Jesse Schell, especially chapters 17-23 on story, indirect control, worlds, characters, spaces, presence, and aesthetics. The workflow is transformed and paraphrased.

Supporting source: MDA for separating authored mechanics from player-experienced dynamics and aesthetics.

## Workflow

1. Define the role of story: premise, motivation, context, consequence, mystery, comedy, identity, or emotional payoff.
2. Align story beats with player action and system state.
3. Use indirect control through goals, affordances, layout, rewards, information, and character cues.
4. Specify world rules, character functions, spaces, mood, and aesthetic constraints.
5. Convert narrative intent into implementable triggers, content schema, and test cases.

## Required Output

- `Narrative Function`: why the game needs story or world detail.
- `Story-Gameplay Map`: beats tied to player actions and system state.
- `World Rules`: facts, boundaries, tone, and contradictions to avoid.
- `Character Specs`: role, desire, behavior hooks, dialogue constraints, and gameplay purpose.
- `Implementation Notes`: state flags, triggers, content data, level cues, and tests.

## Local References

Before producing a story/world spec, read:

- `references/core/guide.md`
- `workflows/narrative-systems-spec.md`

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/LVTD-LLC/skills/skills/game-story-world-character/SKILL.md`
