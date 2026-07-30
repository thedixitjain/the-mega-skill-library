import Anthropic from "@anthropic-ai/sdk";
import { loadEnvLocal } from "./env";

/**
 * Archive everything `npm run setup` created (and any sessions started from
 * the UI). Archive, not delete: the event logs stay readable in the Console.
 * The ROADTRIP_PLANNER_* ids stay in .env.local. `npm run setup -- --force` starts over.
 */

loadEnvLocal();

const client = new Anthropic();

async function attempt(label: string, fn: () => Promise<unknown>) {
  try {
    await fn();
    console.log(`archived  ${label}`);
  } catch (error) {
    const detail = error instanceof Error ? error.message : String(error);
    console.log(`skipped   ${label}  (${detail.slice(0, 80)})`);
  }
}

async function main() {
  const agentId = process.env.ROADTRIP_PLANNER_AGENT_ID;
  const reviewerId = process.env.ROADTRIP_PLANNER_REVIEWER_AGENT_ID;
  const environmentId = process.env.ROADTRIP_PLANNER_ENVIRONMENT_ID;
  const vaultId = process.env.ROADTRIP_PLANNER_VAULT_ID;

  if (!agentId && !reviewerId && !environmentId && !vaultId) {
    console.log("Nothing to tear down: no ROADTRIP_PLANNER_* ids in .env.local.");
    return;
  }

  if (agentId) {
    for await (const session of client.beta.sessions.list({ agent_id: agentId })) {
      await attempt(`session     ${session.id}`, () => client.beta.sessions.archive(session.id));
    }
    await attempt(`agent       ${agentId}`, () => client.beta.agents.archive(agentId));
  }

  // The reviewer never owns a session: it only ever runs as a thread inside
  // the planner's sessions, which the loop above already archived.
  if (reviewerId) {
    await attempt(`agent       ${reviewerId}`, () => client.beta.agents.archive(reviewerId));
  }

  if (vaultId) {
    for (const credentialId of [
      process.env.ROADTRIP_PLANNER_NATIONAL_PARK_SERVICE_CREDENTIAL_ID,
      process.env.ROADTRIP_PLANNER_WINDY_CREDENTIAL_ID,
    ]) {
      if (!credentialId) continue;
      await attempt(`credential  ${credentialId}`, () =>
        client.beta.vaults.credentials.archive(credentialId, { vault_id: vaultId }),
      );
    }
    await attempt(`vault       ${vaultId}`, () => client.beta.vaults.archive(vaultId));
  }

  if (environmentId) {
    await attempt(`environment ${environmentId}`, () =>
      client.beta.environments.archive(environmentId),
    );
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
