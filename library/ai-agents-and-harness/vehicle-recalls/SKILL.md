---
name: vehicle-recalls
description: "Check for open safety recalls on a vehicle using the CarsXE API. Use this when a user asks whether a car has any recalls, safety issues, or wants to know if their vehicle needs a recall repair."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/carsxe/carsxe-codex-plugin/skills/vehicle-recalls/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/carsxe/carsxe-codex-plugin/skills/vehicle-recalls/SKILL.md
---


When the user asks about recalls or safety issues for a vehicle (by VIN):

1. Make an HTTP GET request to the CarsXE Recalls API:
   ```
   GET https://api.carsxe.com/v1/recalls?key={CARSXE_API_KEY}&vin={VIN}&source=codex_plugin
   ```
2. Present recall details:
   - Total number of open recalls
   - For each recall: campaign number, component, defect description, remedy status
3. If no recalls exist, clearly confirm the vehicle has no open recalls.
4. Emphasize any safety-critical recalls.
5. If the API key is missing, tell the user to set the `CARSXE_API_KEY` environment variable (see AGENTS.md).

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/carsxe/carsxe-codex-plugin/skills/vehicle-recalls/SKILL.md`
