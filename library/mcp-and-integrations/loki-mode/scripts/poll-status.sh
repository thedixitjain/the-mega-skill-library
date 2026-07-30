#!/usr/bin/env bash
# Poll loki status and output structured progress for OpenClaw channel routing
# Usage: poll-status.sh [workdir]
#
# Reads loki status --json output and enriches it with budget data
# from .loki/metrics/budget.json and council verdict from .loki/council/state.json.
# Outputs a single JSON object suitable for channel message formatting.

set -euo pipefail

WORKDIR="${1:-.}"
cd "$WORKDIR" || { echo '{"error": "Cannot access workdir: '"$WORKDIR"'"}'; exit 1; }

# Get base status from loki CLI
STATUS_JSON=$(loki status --json 2>/dev/null)
if [ $? -ne 0 ]; then
    echo '{"error": "loki status failed", "suggestion": "Is loki installed and a session running?"}'
    exit 1
fi

# Enrich with budget and council data (not included in loki status --json)
python3 -c "
import json, sys, os

try:
    s = json.load(sys.stdin)
    tc = s.get('task_counts', {})

    output = {
        'status': s.get('status', 'unknown'),
        'phase': s.get('phase'),
        'iteration': s.get('iteration', 0),
        'tasks_completed': tc.get('completed', 0),
        'tasks_total': tc.get('total', 0),
        'tasks_failed': tc.get('failed', 0),
        'tasks_pending': tc.get('pending', 0),
        'elapsed_minutes': round(s.get('elapsed_time', 0) / 60, 1),
        'provider': s.get('provider', 'claude'),
        'version': s.get('version', 'unknown'),
        'pid': s.get('pid'),
        'dashboard_url': s.get('dashboard_url'),
    }

    # Read budget data from flat file (not in loki status --json)
    budget_file = os.path.join('.loki', 'metrics', 'budget.json')
    if os.path.isfile(budget_file):
        try:
            with open(budget_file) as f:
                budget = json.load(f)
            output['budget_used'] = round(budget.get('budget_used', 0), 2)
            output['budget_limit'] = budget.get('budget_limit')
        except Exception:
            output['budget_used'] = None
            output['budget_limit'] = None
    else:
        output['budget_used'] = None
        output['budget_limit'] = None

    # Read council verdict from flat file (not in loki status --json)
    council_file = os.path.join('.loki', 'council', 'state.json')
    if os.path.isfile(council_file):
        try:
            with open(council_file) as f:
                council = json.load(f)
            output['council_verdict'] = council.get('verdict')
        except Exception:
            output['council_verdict'] = None
    else:
        output['council_verdict'] = None

    print(json.dumps(output, indent=2))
except Exception as e:
    print(json.dumps({'error': str(e)}))
" <<< "$STATUS_JSON"
