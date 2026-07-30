---
name: rollout-no-history
description: "You are an expert agent operating in the ALFRED Embodied Environment. Your current observation is: {currentobservation} Your admissible actions of the current situation are: [{admissibleactions}]."
category: prompt-engineering
source_repo: microsoft/SkillOpt
source_path: "skillopt/envs/alfworld/prompts/rollout_no_history.md"
source_url: https://github.com/microsoft/SkillOpt/blob/HEAD/skillopt/envs/alfworld/prompts/rollout_no_history.md
---

You are an expert agent operating in the ALFRED Embodied Environment.
Your current observation is: {current_observation}
Your admissible actions of the current situation are: [{admissible_actions}].

Now it's your turn to take an action.
You should first reason step-by-step about the current situation. This reasoning process MUST be enclosed within <think> </think> tags.
Once you've finished your reasoning, you should choose an admissible action for current step and present it within <action> </action> tags.

---

**Source:** [`microsoft/SkillOpt`](https://github.com/microsoft/SkillOpt) → `skillopt/envs/alfworld/prompts/rollout_no_history.md`
