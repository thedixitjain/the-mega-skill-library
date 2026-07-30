import Anthropic from "@anthropic-ai/sdk";
import { loadCredentials } from "@anthropic-ai/sdk/core/credentials";
import {
  MODEL,
  NATIONAL_PARK_SERVICE_HOST,
  REVIEWER_MODEL,
  REVIEWER_SYSTEM,
  SYSTEM,
  WINDY_HOST,
} from "./config";
import { requireEnv, saveEnvLocal } from "./env";

/**
 * One-time provisioning. Creates, in order:
 *
 *   environment   a cloud sandbox that can reach exactly two hosts
 *   reviewer      a second agent: Opus, review-only prompt, no vendor calls
 *   agent         bash on, web_search/web_fetch off, the trip-planner prompt,
 *                 and a multiagent roster naming the reviewer
 *   vault         holds the two vendor keys
 *   2 credentials same credential type, opposite injection locations:
 *                   NATIONAL_PARK_SERVICE_API_KEY -> developer.nps.gov, header only
 *                   WINDY_API_KEY                 -> api.windy.com,     body only
 *
 * Idempotent: if .env.local already names a live agent it does nothing
 * (pass --force to provision a fresh copy). Prints and saves every id.
 */

async function main() {
  // `new Anthropic()` resolves ANTHROPIC_API_KEY first and falls back to the
  // credentials `ant auth login` saves. Fail before creating anything only
  // when neither exists.
  if (!process.env.ANTHROPIC_API_KEY && !(await loadCredentials())) {
    requireEnv(
      "ANTHROPIC_API_KEY",
      "https://console.anthropic.com/settings/keys, or sign in with `ant auth login`",
    );
  }
  const nationalParkServiceKey = requireEnv(
    "NATIONAL_PARK_SERVICE_API_KEY",
    "free, instant: https://www.nps.gov/subjects/developer/get-started.htm",
  );
  const windyKey = requireEnv("WINDY_API_KEY", "free tier: https://api.windy.com/point-forecast/docs");

  const client = new Anthropic();
  const force = process.argv.includes("--force");

  const existing = process.env.ROADTRIP_PLANNER_AGENT_ID;
  if (existing && !force) {
    const alive = await client.beta.agents.retrieve(existing).catch(() => null);
    if (alive && !alive.archived_at) {
      if (!alive.multiagent) {
        // Provisioned before the reviewer existed: the stored agent has no
        // roster, so the review handoff would silently never happen.
        console.log(`Agent ${alive.id} predates the reviewer roster.`);
        console.log("Run `npm run setup -- --force` to provision the two-agent copy.");
        return;
      }
      console.log(`Already provisioned: agent ${alive.id} (v${alive.version}).`);
      console.log("Run `npm run setup -- --force` for a fresh copy, or `npm run teardown` first.");
      return;
    }
  }

  // 1. The sandbox. `limited` networking is the outer wall: the container can
  //    only open connections to these two hosts (no package registries, no
  //    MCP servers, nothing else).
  const environment = await client.beta.environments.create({
    name: "roadtrip_planner",
    description: "Road trip planner sandbox: National Park Service + Windy only",
    config: {
      type: "cloud",
      networking: { type: "limited", allowed_hosts: [NATIONAL_PARK_SERVICE_HOST, WINDY_HOST] },
    },
    metadata: { cookbook: "roadtrip_planner" },
  });
  console.log(`environment  ${environment.id}`);

  // 2. The reviewer: a second, deliberately small agent. It never calls a
  //    vendor API and never sees the vault - it reads the draft itinerary
  //    out of a thread message and sends back a short critique. Running it
  //    on Opus while the planner defaults to Sonnet is the point: route the
  //    gut-check to a stronger model without touching the planner. It must
  //    exist before the planner, whose roster references it by id.
  const reviewer = await client.beta.agents.create({
    name: "Plan reviewer",
    description: "Quick-reviews itineraries the road trip planner drafts",
    model: REVIEWER_MODEL,
    system: REVIEWER_SYSTEM,
    tools: [
      {
        // Deny-by-default: the reviewer judges the draft text alone, so no
        // tool is reachable even if a poisoned draft asks it to run one.
        // The prompt says the same thing, but this enforces it.
        type: "agent_toolset_20260401",
        default_config: { enabled: false },
        configs: [],
      },
    ],
    metadata: { cookbook: "roadtrip_planner" },
  });
  console.log(`reviewer     ${reviewer.id}  (model ${REVIEWER_MODEL})`);

  // 3. The agent. web_search and web_fetch are OFF on purpose: with them on,
  //    the model can answer from the open web and never touches the vaulted
  //    APIs, and the whole demo evaporates. The multiagent roster makes it a
  //    coordinator: it may spawn the reviewer as a session thread and trade
  //    messages with it. Roster agents may not have rosters of their own
  //    (depth limit 1).
  const agent = await client.beta.agents.create({
    name: "Road trip planner",
    description: "Plans national-park road trips from the NPS and Windy APIs only",
    model: MODEL,
    system: SYSTEM,
    multiagent: { type: "coordinator", agents: [reviewer.id] },
    tools: [
      {
        type: "agent_toolset_20260401",
        default_config: { enabled: true },
        configs: [
          { name: "web_search", enabled: false },
          { name: "web_fetch", enabled: false },
        ],
      },
    ],
    metadata: { cookbook: "roadtrip_planner" },
  });
  console.log(`agent        ${agent.id}  (model ${MODEL})`);

  // 4. The vault. Credentials live here, not in the environment and not in
  //    the prompt. Sessions opt in with vault_ids at create time.
  const vault = await client.beta.vaults.create({
    display_name: "roadtrip_planner vendor keys",
    metadata: { cookbook: "roadtrip_planner" },
  });
  console.log(`vault        ${vault.id}`);

  // 5. The credentials. Both are `environment_variable` credentials: the
  //    sandbox sees $NATIONAL_PARK_SERVICE_API_KEY / $WINDY_API_KEY as
  //    opaque placeholders, and the real key is substituted into a request
  //    only when
  //      - the request host is in the credential's allowed_hosts, AND
  //      - the placeholder sits somewhere injection_location allows.
  //    NPS wants its key in a request header and Windy wants it in the
  //    POST body, so each credential sets the location its vendor
  //    documents. Same vault, same mechanism, opposite locations.
  const nationalParkService = await client.beta.vaults.credentials.create(vault.id, {
    display_name: "National Park Service API key (header)",
    auth: {
      type: "environment_variable",
      secret_name: "NATIONAL_PARK_SERVICE_API_KEY",
      secret_value: nationalParkServiceKey,
      networking: { type: "limited", allowed_hosts: [NATIONAL_PARK_SERVICE_HOST] },
      injection_location: { header: true, body: false },
    },
    metadata: { cookbook: "roadtrip_planner", vendor: "nps" },
  });
  console.log(
    `credential   ${nationalParkService.id}  NATIONAL_PARK_SERVICE_API_KEY -> ${NATIONAL_PARK_SERVICE_HOST} (header)`,
  );

  const windy = await client.beta.vaults.credentials.create(vault.id, {
    display_name: "Windy API key (body)",
    auth: {
      type: "environment_variable",
      secret_name: "WINDY_API_KEY",
      secret_value: windyKey,
      networking: { type: "limited", allowed_hosts: [WINDY_HOST] },
      injection_location: { header: false, body: true },
    },
    metadata: { cookbook: "roadtrip_planner", vendor: "windy" },
  });
  console.log(`credential   ${windy.id}  WINDY_API_KEY -> ${WINDY_HOST} (body)`);

  saveEnvLocal({
    ROADTRIP_PLANNER_ENVIRONMENT_ID: environment.id,
    ROADTRIP_PLANNER_AGENT_ID: agent.id,
    ROADTRIP_PLANNER_REVIEWER_AGENT_ID: reviewer.id,
    ROADTRIP_PLANNER_VAULT_ID: vault.id,
    ROADTRIP_PLANNER_NATIONAL_PARK_SERVICE_CREDENTIAL_ID: nationalParkService.id,
    ROADTRIP_PLANNER_WINDY_CREDENTIAL_ID: windy.id,
  });

  console.log(`
Saved ids to .env.local.

| secret                        | host               | injected in |
|-------------------------------|--------------------|-------------|
| NATIONAL_PARK_SERVICE_API_KEY | developer.nps.gov  | header      |
| WINDY_API_KEY                 | api.windy.com      | body        |

Two agents: "${MODEL}" plans, "${REVIEWER_MODEL}" reviews the draft in a session thread.

Next: npm run dev  ->  http://localhost:3000`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
