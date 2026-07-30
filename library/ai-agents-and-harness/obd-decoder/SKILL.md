---
name: obd-decoder
description: "Decode an OBD-II diagnostic trouble code (DTC) using the CarsXE API. Use this when a user mentions a check engine light code, DTC, or OBD code like P0300, C1234, B0001, or U0100."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/carsxe/carsxe-codex-plugin/skills/obd-decoder/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/carsxe/carsxe-codex-plugin/skills/obd-decoder/SKILL.md
---


When the user mentions an OBD/DTC code and wants to know what it means:

1. Make an HTTP GET request to the CarsXE OBD Codes Decoder API:
   ```
   GET https://api.carsxe.com/obdcodesdecoder?key={CARSXE_API_KEY}&code={CODE}&source=codex_plugin
   ```
2. Present the decoded fault clearly: code, description, system affected, possible causes, and suggested fixes.
3. Add context on severity — whether it requires immediate attention or can wait.
4. If the API key is missing, tell the user to set the `CARSXE_API_KEY` environment variable (see AGENTS.md).

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/carsxe/carsxe-codex-plugin/skills/obd-decoder/SKILL.md`
