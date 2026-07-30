"""Pause and archive everything this example created.

Skip this script to leave the schedule running. `pause` stops future
scheduled triggers while in-flight sessions keep running. `archive` is terminal.
"""

import os

from cma import client

deployment_id = os.environ.get("CLAUDE_DEPLOYMENT_ID", "")
if deployment_id and not deployment_id.endswith("..."):
    client.beta.deployments.pause(deployment_id)
    client.beta.deployments.archive(deployment_id)
    print(f"archived deployment {deployment_id}")

for env_name, archive in [
    ("CLAUDE_ENVIRONMENT_ID", client.beta.environments.archive),
    ("CLAUDE_AGENT_ID", client.beta.agents.archive),
    ("CLAUDE_VAULT_ID", client.beta.vaults.archive),
]:
    resource_id = os.environ.get(env_name, "")
    if resource_id and not resource_id.endswith("..."):
        archive(resource_id)
        print(f"archived {resource_id}")

print("done")
