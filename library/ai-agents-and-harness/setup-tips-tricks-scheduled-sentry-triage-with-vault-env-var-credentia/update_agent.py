"""Push prompt or model changes to the existing agent, then re-pin the deployment.

Edit agent_config.py, then run this. `agents.update` writes a new agent
version, but the deployment keeps the version it pinned when it was created,
so scheduled runs would keep using the old prompt. `deployments.update` with
the bare agent ID re-pins to the latest version.
"""

import os

from agent_config import MODEL, build_system_prompt
from cma import client, require_env

CLAUDE_AGENT_ID = require_env("CLAUDE_AGENT_ID")
SENTRY_ORG = require_env("SENTRY_ORG")
SENTRY_PROJECT = require_env("SENTRY_PROJECT")

# `version` is an optimistic lock: send the agent's current version, and the
# update fails if something else bumped it in between.
current = client.beta.agents.retrieve(CLAUDE_AGENT_ID)
agent = client.beta.agents.update(
    CLAUDE_AGENT_ID,
    version=current.version,
    model=MODEL,
    system=build_system_prompt(SENTRY_ORG, SENTRY_PROJECT),
)
print(f"agent: {agent.id} (version {current.version} -> {agent.version})")

deployment_id = os.environ.get("CLAUDE_DEPLOYMENT_ID", "")
if deployment_id and not deployment_id.endswith("..."):
    client.beta.deployments.update(deployment_id, agent=CLAUDE_AGENT_ID)
    print(f"deployment: {deployment_id} re-pinned to version {agent.version}")
else:
    print("no CLAUDE_DEPLOYMENT_ID in .env; run deploy.py to schedule this version")
