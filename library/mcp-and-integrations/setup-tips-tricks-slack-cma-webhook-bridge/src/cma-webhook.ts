import Anthropic from "@anthropic-ai/sdk";
import { WebClient } from "@slack/web-api";

const anthropic = new Anthropic();
const slack = new WebClient(process.env.SLACK_BOT_TOKEN);

// Dedupe retries (same event.id across retries). Swap for Redis/DB in prod.
const seenEventIds = new Set<string>();

export async function handleCmaWebhook(req: Request): Promise<Response> {
  const rawBody = await req.text();

  // Verify HMAC + timestamp and parse. Reads ANTHROPIC_WEBHOOK_SIGNING_KEY
  // from env. unwrap() needs a plain header map, not a fetch Headers object.
  let event: Anthropic.Beta.BetaWebhookEvent;
  try {
    event = anthropic.beta.webhooks.unwrap(rawBody, {
      headers: Object.fromEntries(req.headers),
    });
  } catch (err) {
    console.warn("[cma-webhook] signature verification failed");
    return new Response("bad signature", { status: 401 });
  }

  if (seenEventIds.has(event.id)) return new Response(null, { status: 204 });
  seenEventIds.add(event.id);

  if (
    event.data.type !== "session.status_idled" &&
    event.data.type !== "session.status_terminated"
  ) {
    return new Response(null, { status: 204 });
  }

  const claudeSessionId = event.data.id;

  // Workspace webhooks fire for EVERY session in the workspace. Fetch the
  // session and filter by our metadata FIRST; ignore anything that isn't ours
  // (including sessions our key can't read).
  let session;
  try {
    session = await anthropic.beta.sessions.retrieve(claudeSessionId);
  } catch {
    return new Response(null, { status: 204 });
  }

  const channel = session.metadata?.slack_channel;
  const thread_ts = session.metadata?.slack_thread_ts;
  if (!channel || !thread_ts) {
    return new Response(null, { status: 204 });
  }

  if (event.data.type === "session.status_terminated") {
    await slack.chat.postMessage({
      channel,
      thread_ts,
      text: ":warning: Agent session terminated unexpectedly.",
    });
    return new Response(null, { status: 204 });
  }

  // Pull the agent's reply text from the event history. Iterating the page
  // object auto-paginates.
  const parts: string[] = [];
  for await (const e of anthropic.beta.sessions.events.list(claudeSessionId)) {
    if (e.type === "agent.message") {
      for (const block of e.content ?? []) {
        if (block.type === "text") parts.push(block.text);
      }
    }
  }
  const responseText = parts.join("").trim();
  if (!responseText) return new Response(null, { status: 204 });

  await slack.chat.postMessage({ channel, thread_ts, text: responseText });
  console.log(`[cma-webhook] posted reply slack=${channel}/${thread_ts} claude=${claudeSessionId}`);
  return new Response(null, { status: 204 });
}
