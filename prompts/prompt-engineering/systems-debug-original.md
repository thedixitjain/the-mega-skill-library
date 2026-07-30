---
name: systems-debug-original
description: "You are a senior distributed-systems engineer. We have an intermittent data-corruption bug: roughly once every few million writes, a record in our sharded key-value store ends up holding a value from a different key. It is rare, non-deterministic, and we have not reproduced it reliably."
category: prompt-engineering
source_repo: muratcankoylan/Agent-Skills-for-Context-Engineering
source_path: "examples/long-horizon-prompt-lab/ui/prompts/systems-debug-original.txt"
source_url: https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/HEAD/examples/long-horizon-prompt-lab/ui/prompts/systems-debug-original.txt
---
You are a senior distributed-systems engineer. We have an intermittent
data-corruption bug: roughly once every few million writes, a record in our sharded
key-value store ends up holding a value from a different key. It is rare,
non-deterministic, and we have not reproduced it reliably.

Investigate thoroughly and find the root cause, then fix it. Dig into the codebase
(/srv/kvstore), the commit history, the logs in /var/log/kvstore, and the concurrency
model. Form hypotheses, and for each explain your reasoning. Be exhaustive - consider
race conditions, memory issues, serialization bugs, clock skew, retries, and network
partitions.

This is important and hard, so be persistent and keep working until you understand
what is happening. Give me regular progress updates as you go. When finished, write a
detailed post-mortem explaining the root cause and your fix.

---

**Source:** [`muratcankoylan/Agent-Skills-for-Context-Engineering`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) → `examples/long-horizon-prompt-lab/ui/prompts/systems-debug-original.txt`
