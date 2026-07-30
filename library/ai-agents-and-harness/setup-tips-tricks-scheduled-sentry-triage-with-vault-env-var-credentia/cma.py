"""Shared client, env loading, and streaming helpers for the triage scripts."""

import os
import sys
import time

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

# The SDK adds the managed-agents beta header automatically for agents,
# environments, sessions, vaults, and deployments. The files resource doesn't:
# without it, /v1/files rejects scope_id ("unknown field"), so pass it
# explicitly when listing session-scoped files (run_now.py).
BETAS = ["managed-agents-2026-04-01"]

client = Anthropic()


def require_env(name: str) -> str:
    value = os.environ.get(name, "")
    if not value or value.endswith("..."):
        sys.exit(f"{name} is not set in .env (see .env.example)")
    return value


def wait_for_idle_status(session_id: str, max_wait: float = 5.0) -> None:
    """Poll until the server-side status is `idle`.

    The `session.status_idle` stream event can arrive slightly before
    `sessions.retrieve` reports `status == "idle"`, so an `archive()`
    issued straight after the stream exits can 400. This absorbs the race.
    """
    deadline = time.monotonic() + max_wait
    while time.monotonic() < deadline:
        if client.beta.sessions.retrieve(session_id).status == "idle":
            return
        time.sleep(0.25)


def stream_until_end_turn(session_id: str) -> None:
    """Stream a session's events and print until the agent finishes its turn.

    `session.status_idle` is not always terminal: with `stop_reason.type ==
    "requires_action"` the agent is waiting on a client event (a tool
    confirmation or custom tool result), so keep streaming. The terminal stop
    reasons are `end_turn` (normal completion) and `retries_exhausted`
    (failure). Breaking only on `end_turn` would hang forever on a failed run.
    """
    with client.beta.sessions.events.stream(session_id) as stream:
        for ev in stream:
            match ev.type:
                case "agent.message":
                    for block in ev.content:
                        if block.type == "text":
                            print(block.text, end="")
                case "agent.tool_use":
                    print(f"\n[{ev.name}]")
                case "session.status_idle" if (
                    ev.stop_reason and ev.stop_reason.type != "requires_action"
                ):
                    if ev.stop_reason.type != "end_turn":
                        print(f"\nsession stopped: {ev.stop_reason.type}")
                    break
                case "session.status_terminated":
                    return
    wait_for_idle_status(session_id)
