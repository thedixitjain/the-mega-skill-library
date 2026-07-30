// One-time: create the Claude agent + environment. Copy the printed IDs into .env.local.
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const env = await anthropic.beta.environments.create({
  name: `slack-bridge-${Date.now()}`,
  config: { type: "cloud", networking: { type: "unrestricted" } },
});

const agent = await anthropic.beta.agents.create({
  name: "Slack Assistant",
  model: "claude-opus-4-7",
  system:
    "You are a helpful assistant embedded in Slack. Keep replies concise and conversational — they are posted as thread replies. Use plain text or Slack mrkdwn (e.g. *bold*, `code`); avoid Markdown headers.",
  tools: [{ type: "agent_toolset_20260401", default_config: { enabled: true } }],
});

console.log("\nAdd to .env.local:");
console.log(`CLAUDE_ENVIRONMENT_ID=${env.id}`);
console.log(`CLAUDE_AGENT_ID=${agent.id}`);
