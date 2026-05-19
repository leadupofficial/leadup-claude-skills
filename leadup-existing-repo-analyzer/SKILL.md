---
name: leadup-existing-repo-analyzer
description: Analyze an existing LeadUp repository to recover its current state. Detects the stack, reads CLAUDE.md/STATUS.md/DEPLOY.md, finds the build/test/run commands, lists bugs, missing files, and the next tasks. Use when the user says "analyze this repo", "what is left", "continue this project", "check existing project", or "where did we leave off".
---

# LeadUp Existing Repo Analyzer

## Purpose

Pick up an existing LeadUp project cold and produce an accurate picture of
where it is: stack, how to run/test it, what's done, what's broken, what's
missing, and the single best next task. Restores project memory so work can
resume without re-discovery.

## When to use

Use on a repo that already has code. Trigger phrases: "analyze this repo",
"what is left", "what still needs doing", "continue this project", "check
existing project", "where did we leave off", "resume this build",
"audit the codebase state".

Not for brand-new ideas with no code → use `leadup-project-kickoff`.
Not for only rewriting STATUS.md after a task → use `leadup-status-updater`.

## Inputs needed

- The repo path (default: current working directory).
- Optional: which area to focus on (bug, feature, deploy).
- Access to read files (no need to read `.env` values — names only).

## Step-by-step workflow

1. **Map structure.** Tree the repo (skip `node_modules`, `.git`, build dirs).
2. **Detect stack** from manifests: `package.json`, `pubspec.yaml`,
   `composer.json`, `requirements.txt`, `Dockerfile`, `docker-compose.yml`,
   framework configs (Next.js, Bagisto, Supabase).
3. **Read project memory** if present: `CLAUDE.md`, `STATUS.md`, `DEPLOY.md`,
   `PROJECT.md`, `SECURITY.md`, `CHANGELOG.md`, `TODO.md`.
4. **Find commands**: install / dev-run / build / test / migrate (from scripts
   + Docker). State the exact command to run locally.
5. **Assess state**: what works, recent commits/branch, half-done areas, TODO/
   FIXME markers, failing or absent tests, missing memory files.
6. **List bugs & blockers** with severity and suspected location.
7. **Recommend next task** — the one highest-value step — and offer to update
   STATUS.md (hand to `leadup-status-updater` or do it inline if asked).

## Required output format

1. **Snapshot** — project name, stack table, multi-tenant? deploy target.
2. **How to run/test** — exact commands (local + Docker).
3. **Current state** — done / in progress / not started.
4. **Bugs & blockers** — table: item | severity | location | suspected cause.
5. **Missing files** — which memory/config files are absent.
6. **Next recommended task** — one concrete step + why.

## Safety rules

See `references/security-rules.md`. Most relevant here:
- List which env keys exist; never read or print their values.
- If a committed secret is found, flag it (redacted) and recommend rotation.
- Read-only analysis: do not modify code, push, or deploy without approval.

## Common mistakes

- Guessing the stack instead of reading the manifest (e.g. assuming Next.js
  when it's Bagisto/Laravel).
- Reporting "no bugs" without checking TODO/FIXME, failing tests, and STATUS.md.
- Ignoring multi-tenant scoping when assessing a SaaS repo.
- Giving five next tasks instead of the one that matters.
- Reading `.env` to "understand config" — use `.env.example` and key names.

## Troubleshooting

- **Under-triggers**: user said "continue X" generically — re-invoke; suggest
  the trigger phrases.
- **Over-triggers** on a fresh idea with no code → route to
  `leadup-project-kickoff`.
- **Missing tool/MCP**: if no shell/file access, ask the user to run a tree/
  manifest dump and paste it (no secrets).
- **No internet/browser**: fine — analysis is local; flag any dependency
  freshness checks as deferred.
- **Missing project files**: report them as gaps; recommend creating them via
  `leadup-status-updater` / `leadup-project-kickoff` assets.
- **Build/test failure** while verifying: capture the error, classify
  (deps / env / code), and put it in Bugs & blockers — do not "fix by
  disabling" tests or checks.

## Test prompts

### Should trigger (5)
1. "Analyze the jewellery SaaS repo and tell me what's left."
2. "Continue this project — where did we leave off?"
3. "Check the existing INET CRM repo state and next steps."
4. "What still needs doing in the saloon repo?"
5. "Audit the codebase state for the venus school site."

### Should NOT trigger (3)
1. "Start a brand-new SaaS idea." (→ project-kickoff)
2. "Just update STATUS.md with what we did." (→ status-updater)
3. "Research the Razorpay API before integrating." (→ api-research-builder)

### Functional test cases (2)
1. On a Next.js + Docker repo with a STATUS.md, output the correct run/test
   commands and a state summary consistent with STATUS.md.
2. On a repo missing CLAUDE.md/STATUS.md, the report lists them under
   "Missing files" and recommends creating them.

## Success criteria

- Stack detected from real manifest evidence, not assumption.
- Exact local + Docker run/test commands stated.
- Bugs/blockers and missing files enumerated honestly.
- Exactly one next recommended task, justified.
- No code modified, no secret printed, nothing pushed/deployed.
