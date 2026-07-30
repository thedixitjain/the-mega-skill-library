import Anthropic from "@anthropic-ai/sdk";

/**
 * The shared pieces of the server side: one SDK client (auth comes from
 * ANTHROPIC_API_KEY or the credentials `ant auth login` saves) and the
 * httpOnly cookie that is this app's entire notion of identity. Every API
 * call lives in the route that triggers it. There is no service layer.
 */
export const client = new Anthropic();

export const SESSION_COOKIE = "roadtrip_planner_session_id";
