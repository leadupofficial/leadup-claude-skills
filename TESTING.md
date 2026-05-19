# Testing — LeadUp Claude Skills Pack

Two layers of testing: **structure validation** (automated, run anytime) and
**trigger testing** (manual, in Claude).

## 1. Structure validation (automated, read-only)

```bash
cd leadup-claude-skills
python3 scripts/check_all_skills.py     # full pack
python3 scripts/list_skills.py          # list skills + descriptions
python3 scripts/check_skill_structure.py leadup-project-kickoff   # one skill
python3 scripts/validate_frontmatter.py leadup-project-kickoff    # one skill
```

`check_all_skills.py` verifies, for every skill:

- Folder exists and contains `SKILL.md`.
- Folder name is kebab-case and **equals** frontmatter `name`.
- Frontmatter is valid YAML with `name` **and** `description`.
- No XML tags / angle brackets in `name` or `description`.
- No `README.md` anywhere inside a skill folder. The project README template
  ships as `assets/README.template.md` (not `README.md`) to avoid any
  ambiguity with this rule.
- Each skill is self-contained: every `references/<name>.md` linked in
  SKILL.md exists in that skill's local `references/` folder, in sync with
  the repo-root master (verify with `python3 scripts/sync_references.py
  --check`).
- All 10 required H2 sections present:
  Purpose, When to use, Inputs needed, Step-by-step workflow,
  Required output format, Safety rules, Common mistakes, Troubleshooting,
  Test prompts, Success criteria.
- Test prompts contain ≥5 "Should trigger", ≥3 "Should NOT trigger",
  ≥2 "Functional test cases".
- No leaked-secret patterns anywhere in the skill (`.env.example` placeholders
  using `__SET_ME__` are allowed).

Exit code is non-zero if any skill fails — CI-friendly.

## 2. Trigger testing (manual, in Claude)

For each skill, open Claude (Code or .ai) with the pack installed and:

1. **Should-trigger:** paste each of the 5 trigger prompts → confirm the
   correct skill activates.
2. **Should-NOT-trigger:** paste the 3 negative prompts → confirm this skill
   does *not* activate (the routed-to sibling may instead).
3. **Functional:** run the 2 functional cases → confirm the output matches the
   skill's "Required output format" and "Success criteria".

Record results like:

| Skill | 5 trig | 3 anti | 2 func | Notes |
|---|---|---|---|---|

## 3. Over-/under-trigger tuning

- **Under-triggers** (should fire, didn't): broaden/clarify the discriminating
  trigger phrases in the frontmatter `description`.
- **Over-triggers** (fires when a sibling should): tighten the description and
  strengthen the "use X instead" cross-link in *When to use*.
- Re-run `check_all_skills.py` after any edit.

## 4. Script self-check

```bash
python3 scripts/scan_secrets.py leadup-security-review/   # demo: should be clean
python3 scripts/detect_stack.py .                          # demo on this repo
```
