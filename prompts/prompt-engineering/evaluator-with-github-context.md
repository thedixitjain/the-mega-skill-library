---
name: evaluator-with-github-context
description: "{baseevaluatorprompt}"
category: prompt-engineering
source_repo: ed-donner/agents
source_path: "1_foundations/community_contributions/amirna2_contributions/personal-ai/prompts/evaluator_with_github_context.md"
source_url: https://github.com/ed-donner/agents/blob/HEAD/1_foundations/community_contributions/amirna2_contributions/personal-ai/prompts/evaluator_with_github_context.md
---
{base_evaluator_prompt}

## GitHub Tool Results (VALID CONTEXT):
{github_context}


CRITICAL INSTRUCTIONS FOR EVALUATION:
- Use {current_date} as the "current date" for any date-related evaluations

- GitHub tool results above are LEGITIMATE CONTEXT.
- GitHub tool results are VALID and should be considered alongside resume/LinkedIn
  => For example, programming languages found in GitHub repos are FACTUAL, not hallucinations
- The agent should synthesize information from resume/LinkedIn AND GitHub tool results

The agent should synthesize information from resume/LinkedIn AND GitHub tool results

Mark UNACCEPTABLE only if: unsupported claims NOT supported by either the static context OR valid GitHub tool results, missing tool usage when needed, or behavioral rules violated.

---

**Source:** [`ed-donner/agents`](https://github.com/ed-donner/agents) → `1_foundations/community_contributions/amirna2_contributions/personal-ai/prompts/evaluator_with_github_context.md`
