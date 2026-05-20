# Install & Configure Guide — LeadUp Claude Skills Pack

This is the install + configure guide for the 14-skill LeadUp Claude Skills
Pack. It covers Claude Code (global + per-project), opencode, and Claude.ai,
plus a short "verify it works" section.

## Prerequisites

- Python 3.8+ (only needed for the validation scripts). PyYAML optional —
  the frontmatter validator falls back to a built-in parser if PyYAML is
  absent.
- For Claude Code: a `.claude/skills/` (project) or `~/.claude/skills/`
  (global) directory.
- For opencode: a `~/.config/opencode/skills/` directory.

## A. Validate before installing

```bash
cd leadup-claude-skills
python3 scripts/check_all_skills.py
```

All **14 skills** must report PASS. Fix any failures before installing.

## B. Install in Claude Code

**Global (all projects):**

```bash
# from the repo root: copy every skill folder into ~/.claude/skills/
mkdir -p ~/.claude/skills
for d in leadup-*; do cp -R "$d" ~/.claude/skills/; done
```

**Per-project:**

```bash
mkdir -p /path/to/project/.claude/skills
for d in leadup-*; do cp -R "$d" /path/to/project/.claude/skills/; done
```

## C. Install in opencode

```bash
mkdir -p ~/.config/opencode/skills
for d in leadup-*; do cp -R "$d" ~/.config/opencode/skills/; done
```

Note: **each skill is self-contained.** Every skill folder bundles its own
`references/` subfolder containing only the reference files it links
(relative paths like `references/security-rules.md`), so copying a single
skill folder works with no extra steps. The repo-root `references/` folder
is the **master/source** copy — edit there, then re-sync (see "Updating").
The repo-root `scripts/` folder is pack tooling/validation, not required at
runtime by the skills.

## D. Install in Claude.ai

1. Settings → Skills.
2. Upload each skill folder, or upload a zip produced by
   `scripts/package_all_skills.sh` (run only after the pack is approved).
3. Claude uses each skill's `description` to decide when to trigger it.

## E. Verify it works

After install, open a Claude Code or opencode session and test a trigger
phrase from any skill's "Test prompts" section. Examples:

| Skill | Trigger phrase |
|---|---|
| `leadup-project-kickoff` | "Start a new LeadUp project for a salon booking app." |
| `leadup-existing-repo-analyzer` | "Analyze this repo and tell me where we left off." |
| `leadup-api-research-builder` | "Research the Razorpay API before we integrate it." |
| `leadup-github-repo-researcher` | "Vet this open-source repo for our project." |
| `leadup-mcp-tool-orchestrator` | "Pick the right MCP tools for this task." |
| `leadup-browser-playwright-tester` | "Run the app and write Playwright tests." |
| `leadup-deploy-checker` | "Prepare deploy — ready or not ready?" |
| `leadup-security-review` | "Security review this project." |
| `leadup-premium-ui-upgrader` | "Make this UI feel premium international SaaS." |
| `leadup-status-updater` | "Update STATUS.md. What is next?" |
| `leadup-content-calendar-builder` | "Build a 30-day content calendar." |
| `leadup-client-document-generator` | "Generate a client proposal." |
| `leadup-super-prompt-builder` | "Make this a Claude Code super prompt." |
| `leadup-human-content-editor` | "Humanize this website copy, remove em dashes." |

The matching skill should activate on the trigger phrase. If it does not
fire, re-state the request using one of the exact trigger phrases listed in
that skill's `SKILL.md` → `## When to use` section.

## F. Configure (optional)

Skills run with no configuration by default. You only need to touch settings
if you want one of these:

- **Per-project skills only:** drop the skill folders into the project's
  `.claude/skills/` (Section B above) instead of the global directory.
- **Fewer permission prompts:** add the read-only commands the LeadUp
  skills tend to run (e.g. `python3 scripts/check_all_skills.py`,
  `python3 scripts/list_skills.py`, `git status`, `git diff`, `git log`,
  `ls`, `cat`) to your `.claude/settings.json` or
  `~/.claude/settings.json` allowlist. The `update-config` /
  `fewer-permission-prompts` Claude Code skills can do this for you.
- **MCP / tool inventory:** skills do not hard-code MCP tool names. The
  inventory is read per session. See `leadup-mcp-tool-orchestrator` and
  `references/mcp-tool-policy.md` for the discover → prefer read-only →
  escalate-with-approval pattern.

You do **not** need to commit any LeadUp-specific config to the repo for
the skills to work.

## G. Packaging (only after approval)

```bash
# Do NOT run until the pack is reviewed and approved.
bash scripts/package_all_skills.sh        # zips every skill into dist/
bash scripts/package_skills.sh <skill>    # zip one skill
```

## H. Updating

The repo-root `references/` is the **master**. Per-skill `references/`
folders are synced copies. To change shared knowledge:

1. Edit the master file in repo-root `references/` (and/or the `SKILL.md`).
2. Re-sync copies into the skills that link them:
   `python3 scripts/sync_references.py` (idempotent; copies only files each
   skill already links — never bloats skills with unused references).
3. Update `CHANGELOG.md`.
4. `python3 scripts/check_all_skills.py` (must pass).
5. Re-copy / re-upload the affected skill folder(s) to the install
   locations above.

## Safety reminder

These skills never auto-push, auto-deploy, print secrets, or read real
`.env` values. Deployment and git push remain manual, approval-gated steps.
Skills also never invent client names, awards, certifications, or numbers
in generated copy.
