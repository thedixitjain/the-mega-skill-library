import { cookies } from "next/headers";
import { SESSION_COOKIE, client } from "@/lib/client";

/**
 * One chat turn is one `user.message` event. That is the entire route: the
 * reply streams to the client over its own session tail (`/api/stream`), so
 * nothing here waits for the agent, and the answer outlives this request:
 * close the tab mid-paragraph and the finished reply is in the event log
 * when you come back.
 */
export async function POST(request: Request) {
  const { text } = (await request.json()) as { text?: string };
  const jar = await cookies();
  const sessionId = jar.get(SESSION_COOKIE)?.value;
  if (!sessionId) {
    return Response.json({ error: "unknown session - reload the page" }, { status: 400 });
  }
  if (!text?.trim()) {
    return Response.json({ error: "empty message" }, { status: 400 });
  }

  try {
    await client.beta.sessions.events.send(sessionId, {
      events: [{ type: "user.message", content: [{ type: "text", text }] }],
    });
    return Response.json({ ok: true });
  } catch (error) {
    const detail = error instanceof Error ? error.message : String(error);
    return Response.json({ error: `send failed: ${detail}` }, { status: 502 });
  }
}
