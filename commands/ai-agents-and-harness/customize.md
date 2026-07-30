---
name: customize
description: "Guided workflow profile setup for overstory. Walks through four questions to build a custom canopy profile and seed mulch domain structure, then optionally runs a discovery swarm."
category: ai-agents-and-harness
source_repo: jayminwest/overstory
source_path: ".claude/commands/customize.md"
source_url: https://github.com/jayminwest/overstory/blob/HEAD/.claude/commands/customize.md
---
## intro

Guided workflow profile setup for overstory. Walks through four questions to build a custom canopy profile and seed mulch domain structure, then optionally runs a discovery swarm.

**Argument:** `$ARGUMENTS` — optional profile name to use (e.g., `my-project`). If empty, the name is derived during setup.

## steps

This is an interactive guided setup. Ask each question in turn and wait for the user's response before proceeding to the next step.

---

### Step 1: What kind of work do you do?

Ask the user: *"What kind of work does this project involve? Choose a base profile to extend:"*

Present these options:

| # | Profile | Best for |
|---|---------|----------|
| 1 | `ov-co-creation` | Collaborative development where the human reviews each step before proceeding |
| 2 | `ov-research` | Exploratory work: spike investigations, feasibility studies, unknown territory |
| 3 | `ov-architecture` | System design, cross-cutting refactors, structural decisions |
| 4 | `ov-red-hat` | Adversarial review: find flaws, stress-test assumptions, challenge designs |
| 5 | `ov-discovery` | Brownfield codebase onboarding — map what exists before building |
| 6 | `ov-delivery` | Straight implementation: spec is clear, deliver and ship |

Wait for the user to select a number or name. Store the selected base profile.

---

### Step 2: What are your review/approval gates?

Ask the user: *"Do you want human approval gates during agent runs? These pause agents and require your sign-off before continuing."*

Offer these gate types:

- **none** — fully autonomous, no pauses
- **before-merge** — pause before merging any branch into canonical
- **before-spec** — pause before agents write task specs (review scope before work starts)
- **on-escalation** — pause only when agents escalate (default for most profiles)
- **full** — pause at every major phase (spec → build → review → merge)

Wait for the user's choice. If they choose any gates other than `none`, note them.

---

### Step 3: What domains matter for this project?

Ask the user: *"What knowledge domains should mulch track for this project? List the main areas of your codebase or workflow (e.g., `auth`, `api`, `database`, `frontend`, `deployment`)."*

Wait for the user's list. Then seed initial mulch structure by running:

```bash
ml record <domain> --type guide --description "Domain seeded during customize setup — add conventions and patterns as you discover them."
```

Run this for each domain the user named. Inform the user that these are empty stubs — they grow as agents work.

---

### Step 4: Run a discovery swarm?

Ask the user: *"Do you want to run a discovery swarm now? Scouts will explore your codebase and populate the mulch domains you just created with real conventions, patterns, and architecture notes."*

- If **yes**: run `ov discover` and tell the user to monitor progress with `ov status`. The mulch records from step 3 will be enriched automatically.
- If **no**: skip. The user can run `/discover` later at any time.

---

### Step 5: Create the custom profile

Determine the profile name:
- If `$ARGUMENTS` was provided, use it as-is.
- Otherwise, derive a name from the project directory: use the basename of the current working directory, lowercased and hyphenated (e.g., `my-project`).

Create a custom canopy prompt that extends the selected base:

```bash
cn create \
  --name <profile-name> \
  --extends <selected-base-profile> \
  --tag delivery-profile \
  --description "Custom workflow profile for <profile-name>"
```

If the user selected review gates (from step 2), add a `decision-gates` section to the created profile:

```bash
cn update <profile-name> \
  --section "decision-gates=Human approval required at: <gate-list>. Pause and send a decision_gate mail to the orchestrator before proceeding past these checkpoints."
```

---

### Step 6: Set as default profile

Update `.overstory/config.yaml` to use the new profile by default:

```bash
# Read the current config, update defaultProfile, write it back
```

Use the Read and Edit tools to update `defaultProfile` in `.overstory/config.yaml` to the new profile name.

If `defaultProfile` is not already present, add it under the top-level config keys.

---

### Step 7: Confirm and summarize

Print a summary of what was configured:

```
✓ Profile created: <profile-name> (extends <base-profile>)
✓ Default profile set in .overstory/config.yaml
✓ Mulch domains seeded: <domain-list>
✓ Review gates: <gate-selection>
✓ Discovery swarm: <started | skipped>

Next steps:
  - Run /discover to populate mulch domains with real codebase knowledge
  - Run ov coordinator start to begin an agent session
  - Use --profile <profile-name> on any ov sling call to apply your profile
  - Run cn render <profile-name> to inspect your profile
```

Commit the canopy changes:
```bash
cn sync
```

---

**Source:** [`jayminwest/overstory`](https://github.com/jayminwest/overstory) → `.claude/commands/customize.md`
