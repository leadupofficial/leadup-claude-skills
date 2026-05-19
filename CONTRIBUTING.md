# Contributing to the LeadUp Claude Skills Pack

Thanks for contributing. This repo is a pack of Claude skills for the LeadUp
Technologies workflow. Contributions must keep every skill **self-contained,
validated, and safe**. Read this before opening a PR.

By contributing you agree your work is licensed under the repo's MIT
`LICENSE`.

## Ground rules (non-negotiable)

- **No secrets, ever.** No real API keys, tokens, passwords, connection
  strings, or real `.env` values — in code, docs, examples, commits, or
  history. Use `__SET_ME__` placeholders only.
- **Skills never auto-push or auto-deploy.** A skill plans, checks, and
  produces output; it stops at an approval gate before any push/deploy/remote
  command. Don't add behaviour that violates this.
- **No `README.md` inside a skill folder** (at any depth). Project README
  templates ship as `README.template.md`.
- `python3 scripts/check_all_skills.py` **must pass** before you open a PR.

## Repo model

- Each skill is a kebab-case folder containing `SKILL.md` plus its own
  `references/` (and optional `scripts/`, `assets/`).
- Repo-root `references/` is the **master/source**. Per-skill `references/`
  folders are **synced copies** containing only the files that skill links —
  never edit a per-skill copy by hand.
- Edit shared knowledge in the master, then run the sync.

## Dev setup

- Python 3.8+ (PyYAML optional; validators fall back to a built-in parser).
- No build step. All tooling lives in `scripts/`.

## Workflow

1. Branch from `main` (e.g. `feat/new-skill`, `fix/deploy-checker-typo`).
2. Make changes:
   - **Editing shared knowledge?** Edit the master file in repo-root
     `references/`, then `python3 scripts/sync_references.py` to propagate it
     into the skills that link it. Verify with
     `python3 scripts/sync_references.py --check` (must say `in sync`).
   - **Editing a skill?** Edit its `SKILL.md`. If you add a new
     `references/<name>.md` link, add the master file first, then sync.
3. Validate:
   - `python3 scripts/check_all_skills.py` — all skills must PASS.
   - `python3 scripts/validate_frontmatter.py <skill>` for frontmatter-only
     changes.
   - `python3 leadup-security-review/scripts/scan_secrets.py .` — must be
     clean.
4. Update `CHANGELOG.md` under `[Unreleased]`.
5. Commit (see conventions) and open a PR.

## SKILL.md requirements

Frontmatter (YAML, concise, no XML tags / angle brackets):

```yaml
---
name: leadup-skill-name        # must equal the folder name (kebab-case)
description: One sentence on what it does + when to use it, including the
  discriminating trigger phrases users would say.
---
```

The body must contain these 10 H2 sections, with these exact headings:

`## Purpose` · `## When to use` · `## Inputs needed` ·
`## Step-by-step workflow` · `## Required output format` ·
`## Safety rules` · `## Common mistakes` · `## Troubleshooting` ·
`## Test prompts` · `## Success criteria`

`## Test prompts` must contain:

- `### Should trigger (5)` — ≥5 numbered prompts
- `### Should NOT trigger (3)` — ≥3 numbered prompts (route to the sibling
  skill they belong to)
- `### Functional test cases (2)` — ≥2 numbered cases

The validator greps these strings — keep them byte-identical.

## Adding a new skill

1. Create `leadup-<name>/` (kebab-case) with a `SKILL.md` following an
   existing skill as the template.
2. In `SKILL.md`, link any shared reference as `references/<file>.md`
   (local path, never `../references/...`).
3. Add any new shared reference to the **master** repo-root `references/`.
4. `python3 scripts/sync_references.py` to bundle the linked references.
5. Cross-link confusable sibling skills in *When to use* to prevent
   over-triggering.
6. `python3 scripts/check_all_skills.py` must PASS.
7. Add the skill to the README skills table and the `CHANGELOG.md`.

## Testing

See `TESTING.md` for structure validation and manual trigger testing
(should-trigger / should-not-trigger / functional). Include trigger-test
results in your PR description for skill changes.

## Commit & PR conventions

- Conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`,
  `test:`. Example: `feat: add leadup-i18n-helper skill`.
- Small, focused PRs. One skill or one concern per PR where possible.
- PR description: what changed, why, validation output, and (for skills)
  trigger-test results.
- Do not commit `.env`, `*.db`, `__pycache__/`, `dist/`, `.DS_Store`
  (already in `.gitignore`).

## Reporting issues

Open a GitHub issue with: the skill name, what you said (trigger phrase),
what happened vs. expected, and whether it under- or over-triggered. Never
paste secrets or real `.env` contents into an issue.

— LeadUp Technologies · https://leadup.in
