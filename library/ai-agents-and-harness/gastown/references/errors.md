# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| gt: command not found | Gas Town CLI not installed | Run `go install github.com/steveyegge/gastown/cmd/gt@latest` |
| bd: command not found | Beads CLI not installed | Run `go install github.com/steveyegge/beads/cmd/bd@latest` |
| Prefix mismatch error | Routes.jsonl misconfigured for rig | Run `gt doctor --fix` or manually edit routes.jsonl |
| Polecat stuck/unresponsive | Worker crashed or infinite loop | Use `gt nudge` first, then `gt polecat kill` if needed |
| Beads daemon timeout | Daemon not running or crashed | Run `bd doctor` then restart with `bd daemon restart` |
| Missing patrol molecules | Rig setup incomplete | Run `gt doctor --fix` to create missing patrol templates |
| Refinery not processing | Refinery not started for rig | Start with `gt refinery start` |
| Engine won't start | Configuration or dependency issue | Run `gt doctor` for diagnostics, fix blockers first |

---
*[Tons of Skills](https://tonsofskills.com) by [Intent Solutions](https://intentsolutions.io) | [jeremylongshore.com](https://jeremylongshore.com)*
