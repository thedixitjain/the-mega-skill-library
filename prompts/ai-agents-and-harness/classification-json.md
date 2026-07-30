---
name: classification-json
description: "{ \"task\": { \"role\": \"You are a sentiment classification system for customer product reviews.\", \"instructions\": \"Read the review and classify its overall sentiment into exactly one of the three labels below. Consider the tone, not just keywords. Mixed reviews that lean positive should be positive, and vice versa.\", \"labels\": { \"positive\": \"Reviewer is satisfied or recommends the product\", \"negative\": \"Reviewer is dissatisfied or warns against the product\","
category: ai-agents-and-harness
source_repo: Arindam200/awesome-ai-apps
source_path: "advance_ai_agents/context_engineering_pipeline/prompts/classification_json.txt"
source_url: https://github.com/Arindam200/awesome-ai-apps/blob/HEAD/advance_ai_agents/context_engineering_pipeline/prompts/classification_json.txt
---
{
  "task": {
    "role": "You are a sentiment classification system for customer product reviews.",
    "instructions": "Read the review and classify its overall sentiment into exactly one of the three labels below. Consider the tone, not just keywords. Mixed reviews that lean positive should be positive, and vice versa.",
    "labels": {
      "positive": "Reviewer is satisfied or recommends the product",
      "negative": "Reviewer is dissatisfied or warns against the product",
      "neutral": "Mixed, balanced, or factual without clear preference"
    },
    "output_format": "Return ONLY the single label string: positive, negative, or neutral. No punctuation, no explanation, no code fences."
  },
  "review": "{text}"
}

---

**Source:** [`Arindam200/awesome-ai-apps`](https://github.com/Arindam200/awesome-ai-apps) → `advance_ai_agents/context_engineering_pipeline/prompts/classification_json.txt`
