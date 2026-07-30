---
name: chat-rerun
description: "{basesystemprompt}"
category: prompt-engineering
source_repo: ed-donner/agents
source_path: "1_foundations/community_contributions/amirna2_contributions/personal-ai/prompts/chat_rerun.md"
source_url: https://github.com/ed-donner/agents/blob/HEAD/1_foundations/community_contributions/amirna2_contributions/personal-ai/prompts/chat_rerun.md
---
{base_system_prompt}

## Previous answer rejected
You just tried to reply, but the quality control rejected your reply

## Your attempted answer:
{reply}

## Reason for rejection:
{feedback}

Please provide a corrected structured response that addresses the feedback.

---

**Source:** [`ed-donner/agents`](https://github.com/ed-donner/agents) → `1_foundations/community_contributions/amirna2_contributions/personal-ai/prompts/chat_rerun.md`
