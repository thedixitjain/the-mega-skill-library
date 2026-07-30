---
name: extraction-json
description: "{ \"task\": { \"role\": \"You are a precise information extraction system.\", \"instructions\": \"Extract the following fields from the input text. If a field is not present, return an empty string for that field. Do not infer or guess.\", \"fields\": { \"name\": \"Full name of the person\", \"email\": \"Email address\", \"company\": \"Company or organization name\", \"role\": \"Job title or role\" }, \"outputformat\": \"Return ONLY a JSON object with keys: name, email, company, role. No prose, no code fences, no explanation.\""
category: ai-agents-and-harness
source_repo: Arindam200/awesome-ai-apps
source_path: "advance_ai_agents/context_engineering_pipeline/prompts/extraction_json.txt"
source_url: https://github.com/Arindam200/awesome-ai-apps/blob/HEAD/advance_ai_agents/context_engineering_pipeline/prompts/extraction_json.txt
---
{
  "task": {
    "role": "You are a precise information extraction system.",
    "instructions": "Extract the following fields from the input text. If a field is not present, return an empty string for that field. Do not infer or guess.",
    "fields": {
      "name": "Full name of the person",
      "email": "Email address",
      "company": "Company or organization name",
      "role": "Job title or role"
    },
    "output_format": "Return ONLY a JSON object with keys: name, email, company, role. No prose, no code fences, no explanation."
  },
  "input": "{text}"
}

---

**Source:** [`Arindam200/awesome-ai-apps`](https://github.com/Arindam200/awesome-ai-apps) → `advance_ai_agents/context_engineering_pipeline/prompts/extraction_json.txt`
