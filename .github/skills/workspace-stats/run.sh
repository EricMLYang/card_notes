#!/bin/bash
# Mac/Linux shell script to run workspace stats

# Get the script's directory and navigate to project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/../../.." || exit 1

# Run the Python script
python3 .github/skills/workspace-stats/workspace_stats.py
