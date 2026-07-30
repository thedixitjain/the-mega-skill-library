#!/bin/bash
# run_sleep_cron.sh — wrapper for cron-driven nightly sleep cycle
#
# Usage: bash run_sleep_cron.sh [category1 category2 ...]
#   No args: run on all categories in tests/
#   With args: run only on listed categories (research-cron, devops, wiki)
#
# Cron (3am MYT daily):
#   0 3 * * * cd /home/ethanclaw/.openclaw/workspace/skills/skillopt-sleep && bash run_sleep_cron.sh >> ~/.skillopt-sleep/nightly.log 2>&1

set -euo pipefail

SKILL_DIR="/home/ethanclaw/.openclaw/workspace/skills/skillopt-sleep"
TESTS_DIR="$SKILL_DIR/tests"
LOG_DIR="$HOME/.skillopt-sleep/logs"
mkdir -p "$LOG_DIR"

TIMESTAMP=$(date +%Y%m%d-%H%M%S)
LOG_FILE="$LOG_DIR/night-$TIMESTAMP.log"

# category → test file map
declare -A CATEGORIES=(
    ["research-cron"]="research-cron-tasks.json"
    ["devops"]="devops-tasks.json"
    ["wiki"]="wiki-tasks.json"
)

# Determine which categories to run
if [ $# -eq 0 ]; then
    CATS=("research-cron" "devops" "wiki")
else
    CATS=("$@")
fi

{
    echo "=========================================="
    echo "SkillOpt-Sleep nightly — $TIMESTAMP"
    echo "Categories: ${CATS[*]}"
    echo "=========================================="
} | tee -a "$LOG_FILE"

# Pre-flight: check DeepSeek API key
if ! grep -q "DEEPSEEK_API_KEY=" "$HOME/.openclaw/.env" 2>/dev/null; then
    echo "ERROR: DEEPSEEK_API_KEY not found in ~/.openclaw/.env" | tee -a "$LOG_FILE"
    exit 1
fi

EXIT_CODE=0
for cat in "${CATS[@]}"; do
    tasks_file="$TESTS_DIR/${CATEGORIES[$cat]:-}"
    if [ ! -f "$tasks_file" ]; then
        echo "SKIP: $cat (no tasks file: $tasks_file)" | tee -a "$LOG_FILE"
        continue
    fi

    echo "" | tee -a "$LOG_FILE"
    echo "--- [$cat] starting cycle ---" | tee -a "$LOG_FILE"

    cd "$SKILL_DIR"
    if python3 run_sleep.py --tasks "$tasks_file" 2>&1 | tee -a "$LOG_FILE"; then
        echo "--- [$cat] OK ---" | tee -a "$LOG_FILE"
    else
        EC=$?
        echo "--- [$cat] FAILED (exit $EC) ---" | tee -a "$LOG_FILE"
        EXIT_CODE=$EC
    fi
done

{
    echo ""
    echo "=========================================="
    echo "Done. Exit: $EXIT_CODE"
    echo "=========================================="
} | tee -a "$LOG_FILE"

exit $EXIT_CODE
