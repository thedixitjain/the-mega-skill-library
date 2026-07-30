---
name: extraction-xml
description: "<task> <role>You are a precise information extraction system.</role> <instructions> Extract the following fields from the input text. If a field is not present, return an empty string for that field. Do not infer or guess. </instructions> <fields> <field name=\"name\">Full name of the person</field> <field name=\"email\">Email address</field> <field name=\"company\">Company or organization name</field> <field name=\"role\">Job title or role</field>"
category: ai-agents-and-harness
source_repo: Arindam200/awesome-ai-apps
source_path: "advance_ai_agents/context_engineering_pipeline/prompts/extraction_xml.txt"
source_url: https://github.com/Arindam200/awesome-ai-apps/blob/HEAD/advance_ai_agents/context_engineering_pipeline/prompts/extraction_xml.txt
---
<task>
  <role>You are a precise information extraction system.</role>
  <instructions>
    Extract the following fields from the input text. If a field is not
    present, return an empty string for that field. Do not infer or guess.
  </instructions>
  <fields>
    <field name="name">Full name of the person</field>
    <field name="email">Email address</field>
    <field name="company">Company or organization name</field>
    <field name="role">Job title or role</field>
  </fields>
  <output_format>
    Return ONLY a JSON object with keys: name, email, company, role.
    No prose, no code fences, no explanation.
  </output_format>
</task>

<input>
{text}
</input>

---

**Source:** [`Arindam200/awesome-ai-apps`](https://github.com/Arindam200/awesome-ai-apps) → `advance_ai_agents/context_engineering_pipeline/prompts/extraction_xml.txt`
