#!/usr/bin/env bash
# Package EVERY skill folder into dist/ (one zip per skill) plus a
# combined dist/leadup-claude-skills.zip.
#
# Do NOT run until the pack is reviewed and approved by the owner.
# Packaging/zipping/committing/pushing are explicit, approval-gated steps.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Validating pack before packaging..."
python3 "$ROOT/scripts/check_all_skills.py"

mkdir -p "$ROOT/dist"
SKILLS=()
for d in "$ROOT"/*/; do
  name="$(basename "$d")"
  [[ -f "$d/SKILL.md" ]] || continue
  SKILLS+=("$name")
  ( cd "$ROOT" && zip -r -q \
      -x '*/__pycache__/*' -x '*.pyc' \
      "dist/${name}.zip" "$name" )
  echo "  packaged dist/${name}.zip"
done

if [[ ${#SKILLS[@]} -eq 0 ]]; then
  echo "No skills found." >&2
  exit 1
fi

( cd "$ROOT" && zip -r -q \
    -x '*/__pycache__/*' -x '*.pyc' -x 'dist/*' \
    "dist/leadup-claude-skills.zip" "${SKILLS[@]}" references )
echo "Combined: dist/leadup-claude-skills.zip (${#SKILLS[@]} skills + references)"
