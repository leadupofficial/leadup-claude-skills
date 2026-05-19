# Install Guide — LeadUp Claude Skills Pack

## Prerequisites

- Python 3.8+ (for the validation scripts). PyYAML optional — the frontmatter
  validator falls back to a built-in parser if PyYAML is absent.
- For Claude Code: a `.claude/skills/` (project) or `~/.claude/skills/`
  (global) directory.

## A. Validate before installing

```bash
cd leadup-claude-skills
python3 scripts/check_all_skills.py
```

All 12 skills must report PASS. Fix any failures before installing.

## B. Install in Claude Code (recommended for LeadUp)

**Global (all projects):**
```bash
# copy each skill folder (the one containing SKILL.md) into ~/.claude/skills/
for d in leadup-*; do cp -R "$d" ~/.claude/skills/; done
```

**Per-project:**
```bash
mkdir -p /path/to/project/.claude/skills
for d in leadup-*; do cp -R "$d" /path/to/project/.claude/skills/; done
```

Note: **each skill is self-contained.** Every skill folder bundles its own
`references/` subfolder containing only the reference files it links (relative
paths like `references/security-rules.md`), so copying a single skill folder
into `~/.claude/skills/` works with no extra steps. The repo-root
`references/` folder is the **master/source** copy — edit there, then
re-sync (see "Updating"). The repo-root `scripts/` folder is pack
tooling/validation, not required at runtime by the skills.

## C. Install in Claude.ai

1. Settings → Skills.
2. Upload each skill folder, or upload a zip from
   `scripts/package_all_skills.sh` (run only after the pack is approved).
3. Claude uses each skill's `description` to decide when to trigger it.

## D. Packaging (only after approval)

```bash
# Do NOT run until the pack is reviewed and approved.
bash scripts/package_all_skills.sh        # zips every skill into dist/
bash scripts/package_skills.sh <skill>    # zip one skill
```

## E. Updating

The repo-root `references/` is the **master**. Per-skill `references/` folders
are synced copies. To change shared knowledge:

1. Edit the master file in repo-root `references/` (and/or the `SKILL.md`).
2. Re-sync copies into the skills that link them:
   `python3 scripts/sync_references.py` (idempotent; copies only files each
   skill already links — never bloats skills with unused references).
3. Update `CHANGELOG.md`.
4. `python3 scripts/check_all_skills.py` (must pass).
5. Re-copy / re-upload the affected skill folder(s).

## Safety reminder

These skills never auto-push, auto-deploy, print secrets, or read real
`.env` values. Deployment and git push remain manual, approval-gated steps.
