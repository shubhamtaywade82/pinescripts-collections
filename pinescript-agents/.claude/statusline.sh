#!/bin/bash
# PineScript Agents - Statusline
# by TradersPost

input=$(cat)

PROJECT_DIR=$(echo "$input" | jq -r '.workspace.project_dir // ""')

# Check for active video processing status first
STATUS_FILE="$PROJECT_DIR/.claude/.video_status"
if [ -f "$STATUS_FILE" ]; then
    VIDEO_STATUS=$(cat "$STATUS_FILE" 2>/dev/null)
    if [ -n "$VIDEO_STATUS" ]; then
        echo "$VIDEO_STATUS"
        exit 0
    fi
fi

# Get version from package.json
VERSION="1.3.0"
if [ -f "$PROJECT_DIR/package.json" ]; then
    VERSION=$(cat "$PROJECT_DIR/package.json" | jq -r '.version // "1.3.0"')
fi

# Count projects (pine files excluding blank.pine)
PROJECT_COUNT=$(ls -1 "$PROJECT_DIR/projects/"*.pine 2>/dev/null | grep -v blank.pine | wc -l | tr -d ' ')

# Count skills
SKILL_COUNT=$(ls -1d "$PROJECT_DIR/.claude/skills/"*/ 2>/dev/null | wc -l | tr -d ' ')

echo "PineScript Agents v$VERSION | 🗀  $PROJECT_COUNT projects | ⚡︎$SKILL_COUNT skills | by TradersPost"
