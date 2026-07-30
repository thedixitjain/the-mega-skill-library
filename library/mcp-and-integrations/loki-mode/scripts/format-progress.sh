#!/usr/bin/env bash
# Format loki status into human-readable progress message
# Reads JSON from stdin (output of poll-status.sh), outputs formatted text
# suitable for posting to Slack, Discord, or web channels.
#
# Usage: ./poll-status.sh /path/to/project | ./format-progress.sh

set -euo pipefail

python3 -c "
import json, sys

try:
    s = json.load(sys.stdin)

    # Check for error
    if 'error' in s:
        print('Loki Mode [ERROR] - ' + s['error'])
        suggestion = s.get('suggestion')
        if suggestion:
            print('Suggestion: ' + suggestion)
        sys.exit(0)

    status = s.get('status', 'unknown').upper()
    phase = s.get('phase') or 'N/A'
    iteration = s.get('iteration', 0)
    completed = s.get('tasks_completed', 0)
    total = s.get('tasks_total', 0)
    failed = s.get('tasks_failed', 0)
    pending = s.get('tasks_pending', 0)
    budget_used = s.get('budget_used')
    budget_limit = s.get('budget_limit')
    elapsed = s.get('elapsed_minutes', 0)
    provider = s.get('provider', 'unknown')
    verdict = s.get('council_verdict')
    version = s.get('version', '')

    lines = []

    # Header line
    header = 'Loki Mode [' + status + '] - ' + phase + ' (iteration ' + str(iteration) + ')'
    if version:
        header += ' | v' + version
    lines.append(header)

    # Task progress
    task_line = 'Tasks: ' + str(completed) + '/' + str(total) + ' complete'
    if failed:
        task_line += ', ' + str(failed) + ' failed'
    if pending:
        task_line += ', ' + str(pending) + ' pending'
    lines.append(task_line)

    # Cost and timing
    info_parts = []
    if budget_used is not None:
        cost_str = '\$' + '{:.2f}'.format(budget_used)
        if budget_limit:
            cost_str += ' / \$' + '{:.2f}'.format(budget_limit) + ' budget'
        info_parts.append('Cost: ' + cost_str)
    info_parts.append('Time: ' + '{:.0f}'.format(elapsed) + 'm')
    info_parts.append('Provider: ' + provider)
    lines.append(' | '.join(info_parts))

    # Council verdict (if available)
    if verdict:
        lines.append('Council: ' + verdict)

    # Warnings
    if failed > 0:
        lines.append('WARNING: ' + str(failed) + ' task(s) failed -- check loki logs')
    if status == 'UNKNOWN':
        lines.append('WARNING: Session status unknown -- process may have crashed')

    print('\\n'.join(lines))
except json.JSONDecodeError:
    print('Loki Mode [ERROR] - Failed to parse status JSON')
except Exception as e:
    print('Loki Mode [ERROR] - ' + str(e))
"
