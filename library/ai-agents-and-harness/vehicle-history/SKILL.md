---
name: vehicle-history
description: "Retrieve a vehicle history report from a VIN using the CarsXE API. Use this when a user wants to know a car's history — past owners, accidents, title status, odometer readings, or whether it's been in a crash."
category: ai-agents-and-harness
source_repo: hashgraph-online/awesome-codex-plugins
source_path: "plugins/carsxe/carsxe-codex-plugin/skills/vehicle-history/SKILL.md"
source_url: https://github.com/hashgraph-online/awesome-codex-plugins/blob/HEAD/plugins/carsxe/carsxe-codex-plugin/skills/vehicle-history/SKILL.md
---


When the user asks about a vehicle's history, past accidents, title status, or ownership:

1. Make an HTTP GET request to the CarsXE History API:
   ```
   GET https://api.carsxe.com/history?key={CARSXE_API_KEY}&vin={VIN}&source=codex_plugin
   ```
2. Summarize the history report:
   - Number of previous owners
   - Accident / damage records
   - Title status (clean, salvage, rebuilt, lemon)
   - Odometer history
   - Theft records
3. Clearly highlight any red flags (salvage title, accidents, odometer rollback).
4. If the API key is missing, tell the user to set the `CARSXE_API_KEY` environment variable (see AGENTS.md).

---

**Source:** [`hashgraph-online/awesome-codex-plugins`](https://github.com/hashgraph-online/awesome-codex-plugins) → `plugins/carsxe/carsxe-codex-plugin/skills/vehicle-history/SKILL.md`
