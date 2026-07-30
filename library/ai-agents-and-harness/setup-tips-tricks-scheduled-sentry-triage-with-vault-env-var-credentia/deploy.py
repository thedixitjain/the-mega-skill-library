"""Create the scheduled deployment: weekday mornings, 9 AM Eastern.

Copy the printed deployment ID into .env.
"""

from cma import client, require_env

CLAUDE_AGENT_ID = require_env("CLAUDE_AGENT_ID")
CLAUDE_ENVIRONMENT_ID = require_env("CLAUDE_ENVIRONMENT_ID")
CLAUDE_VAULT_ID = require_env("CLAUDE_VAULT_ID")
SENTRY_ORG = require_env("SENTRY_ORG")
SENTRY_PROJECT = require_env("SENTRY_PROJECT")

TRIAGE_PROMPT = (
    "Run today's Sentry triage. Pull the last 24 hours of unresolved issues for "
    f"{SENTRY_ORG}/{SENTRY_PROJECT}, triage them per your instructions, and write "
    "the report to /mnt/session/outputs/TRIAGE_REPORT.md. "
    "Reply with the Summary section when you're done."
)

# The schedule is a POSIX cron expression plus an IANA timezone, matched on
# wall-clock time (see skill.md for the DST edges). Sessions start themselves
# on Anthropic infra; nothing keeps running on this machine.
deployment = client.beta.deployments.create(
    name="Weekday morning Sentry triage",
    agent=CLAUDE_AGENT_ID,
    environment_id=CLAUDE_ENVIRONMENT_ID,
    vault_ids=[CLAUDE_VAULT_ID],
    initial_events=[
        {
            "type": "user.message",
            "content": [{"type": "text", "text": TRIAGE_PROMPT}],
        }
    ],
    schedule={
        "type": "cron",
        "expression": "0 9 * * 1-5",  # weekday mornings
        "timezone": "America/New_York",
    },
)

print(f"deployment: {deployment.id} ({deployment.status})")
print("next runs:")
for ts in deployment.schedule.upcoming_runs_at:
    print(f"  {ts}")
print("\nAdd to .env:")
print(f"CLAUDE_DEPLOYMENT_ID={deployment.id}")
