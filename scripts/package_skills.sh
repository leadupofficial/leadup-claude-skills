#!/usr/bin/env bash
# Package a SINGLE skill folder into dist/<skill>.zip
#
# Do NOT run until the pack is reviewed and approved.
# Usage: bash scripts/package_skills.sh <skill-folder>
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL="${1:-}"

if [[ -z "$SKILL" ]]; then
  echo "usage: bash scripts/package_skills.sh <skill-folder>" >&2
  exit 2
fi
if [[ ! -f "$ROOT/$SKILL/SKILL.md" ]]; then
  echo "error: '$SKILL' is not a skill folder (no SKILL.md)" >&2
  exit 1
fi

# Validate before packaging.
python3 "$ROOT/scripts/check_skill_structure.py" "$ROOT/$SKILL"

mkdir -p "$ROOT/dist"
( cd "$ROOT" && zip -r -q \
    -x '*/__pycache__/*' -x '*.pyc' \
    "dist/${SKILL}.zip" "$SKILL" )
echo "Packaged: dist/${SKILL}.zip"
