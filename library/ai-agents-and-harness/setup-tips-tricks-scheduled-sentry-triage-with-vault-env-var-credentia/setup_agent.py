"""One-time: create the vault, credential, agent, and environment.

Copy the printed IDs into .env.
"""

from agent_config import MODEL, build_system_prompt
from cma import client, require_env

SENTRY_AUTH_TOKEN = require_env("SENTRY_AUTH_TOKEN")
SENTRY_ORG = require_env("SENTRY_ORG")
SENTRY_PROJECT = require_env("SENTRY_PROJECT")

vault = client.beta.vaults.create(
    display_name="cookbook-sentry-triage",
    metadata={"purpose": "sentry-triage-cookbook"},
)

# The credential exposes SENTRY_AUTH_TOKEN inside any session this vault is
# attached to. The sandbox only ever holds an opaque placeholder; the egress
# proxy substitutes the real token on requests to allowed_hosts and nothing
# else. *.sentry.io covers regional hosts (us.sentry.io, de.sentry.io) but
# not the apex, so list both.
credential = client.beta.vaults.credentials.create(
    vault.id,
    auth={
        "type": "environment_variable",
        "secret_name": "SENTRY_AUTH_TOKEN",
        "secret_value": SENTRY_AUTH_TOKEN,
        "networking": {
            "type": "limited",
            "allowed_hosts": ["sentry.io", "*.sentry.io"],
        },
    },
    display_name="Sentry org auth token (read-only scopes)",
)

agent = client.beta.agents.create(
    name="cookbook-sentry-triage",
    model=MODEL,
    system=build_system_prompt(SENTRY_ORG, SENTRY_PROJECT),
    tools=[
        {
            "type": "agent_toolset_20260401",
            "default_config": {
                "enabled": True,
                "permission_policy": {"type": "always_allow"},
            },
        }
    ],
)

# The environment's networking is separate from the credential's: this one
# gates what the sandbox can connect to, the credential's gates where the
# secret is substituted. Both need Sentry's hosts. The PyPI package ships
# the sentry-cli binary.
env = client.beta.environments.create(
    name="cookbook-sentry-triage-env",
    config={
        "type": "cloud",
        "networking": {
            "type": "limited",
            "allow_package_managers": True,
            "allowed_hosts": ["sentry.io", "*.sentry.io"],
        },
        "packages": {"pip": ["sentry-cli"]},
    },
)

print(f"vault: {vault.id}")
print(f"credential: {credential.id}")
print(f"agent: {agent.id} (version {agent.version})")
print(f"environment: {env.id}")
print("\nAdd to .env:")
print(f"CLAUDE_VAULT_ID={vault.id}")
print(f"CLAUDE_AGENT_ID={agent.id}")
print(f"CLAUDE_ENVIRONMENT_ID={env.id}")
