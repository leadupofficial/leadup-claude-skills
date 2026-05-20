---
name: leadup-release-manager
description: Prepare a LeadUp release — write a clear release summary, list changed files and modules, flag migration and env changes, capture test status, document known risks, build a rollback plan, draft client communication, and give a single go/no-go recommendation. Use when the user says "release", "release notes", "deploy checklist", "version release", "go live", or "production release".
---

# LeadUp Release Manager

## Purpose

Take a finished work batch (commits, PRs, feature branch, sprint) and
produce a release pack: summary, changed modules, env / migration
changes, test status, risks, rollback plan, client communication, and
a single go/no-go recommendation.

## When to use

Use when the user is approaching a release / deploy. Do **not** trigger
for ongoing project status updates (use `leadup-status-updater`), the
yes-or-no deploy verdict only (use `leadup-deploy-checker`), or writing
QA test cases (use `leadup-qa-test-case-generator`).

Trigger phrases: "release", "release notes", "deploy checklist",
"version release", "go live", "production release", "ship it",
"changelog for release".

## Inputs needed

- Git branch / range (e.g. `main..release/v0.4.0` or last N commits).
- Stack and deploy target (Coolify / `leadup-server` / Vercel / other).
- Migration diff (Prisma / Drizzle / SQL).
- Env var diff (added / changed / removed).
- Test status (manual + automated).
- Known issues and workarounds.
- Audience for the client communication (internal team / paying clients
  / all users).

Ask at most 2 clarifying questions if the branch or audience is unclear.

## Tools/resources to use

- `references/release-checklist.md` — pre-release gate, rollback,
  comms.
- `assets/release-notes.template.md` — output shape.
- `leadup-deploy-checker` — for the READY/NOT READY verdict.
- `leadup-qa-test-case-generator` — to confirm test coverage.
- `leadup-security-review` — for sensitive releases.
- `leadup-pii-risk-reviewer` — if PII surface changes.
- `leadup-human-content-editor` — to polish client-facing release
  notes.
- `leadup-status-updater` — to reflect the release in STATUS.md.

## Step-by-step workflow

1. **Restate the release scope** (branch, target, expected date).
2. **Summarize changes** — group by Feature / Fix / Improvement /
   Internal.
3. **Changed modules / files** — high-level list (modules > files when
   long).
4. **Migrations** — list of schema changes, forward + rollback notes.
5. **Env vars** — added / changed / removed; flag any new secret /
   third-party key.
6. **Test status** — manual sign-off + automated pass/fail summary.
7. **Known risks** — list with severity + mitigation.
8. **Rollback plan** — exact commands (placeholder branch name / tag);
   data rollback strategy.
9. **Client communication** — internal note, paying-clients note,
   public-changelog entry. Pass copy through
   `leadup-human-content-editor` before publishing.
10. **Go / No-Go recommendation** — one line, with the top reason.

## Required output format

One Markdown release pack with these sections, in this order:

1. **Release summary** — name, version, target, date.
2. **What changed** — Feature / Fix / Improvement / Internal.
3. **Modules / files touched**.
4. **Migrations** — forward + rollback notes.
5. **Env vars** — added / changed / removed.
6. **Test status** — manual + automated, with links / paths.
7. **Known risks** — severity + mitigation.
8. **Rollback plan** — exact steps + data plan.
9. **Client communication** — internal / paying-clients / public.
10. **Go / No-Go recommendation** — one line + top reason.
11. **Hand-offs** — to deploy checker, security, PII, status.

## Safety rules

- Do **not** ship if migrations are not reversible OR a rollback plan
  isn't documented.
- Do **not** ship with secrets in commits or env files; flag for
  `leadup-security-review` if anything looks suspicious.
- Do **not** invent test pass numbers. "Pass / fail / unknown" only.
- Do **not** publish public changelog copy without
  `leadup-human-content-editor` polish.
- For paying clients: tell them about breaking changes, downtime
  windows, and data migrations in plain language.
- For India SMB clients: prefer WhatsApp + email for the client
  communication.
- For regulated categories: ensure PII / compliance changes are
  reviewed by `leadup-pii-risk-reviewer`.
- Default to **No-Go** if any of these is true: rollback untested,
  test status unknown, sensitive PII / payment changes unreviewed,
  env vars missing in target.

## Common mistakes

- Long "what changed" section, no rollback plan.
- Marketing tone inside an internal release note.
- Forgetting env var diff — deploy fails on first request.
- Forgetting to update `STATUS.md` after the release.
- Vague risks ("might be issues") without severity or mitigation.
- Pushing to prod on Friday evening without rollback rehearsed.
- Skipping the client communication.

## Troubleshooting

- **Big release (many features)**: stage rollout — internal → 1 client
  → soft → full; reuse `leadup-ai-feature-planner` rollout pattern.
- **DB migration is destructive**: pause; design a non-destructive
  alternative (additive then cleanup later).
- **No QA pass yet**: route to `leadup-qa-test-case-generator` + run;
  block release until pass.
- **Client downtime needed**: schedule in low-traffic window for the
  audience (India weekday 1–4am IST often safest).
- **Coolify / `leadup-server` quirks**: confirm container resources,
  env vars, health checks via `leadup-deploy-checker`.
- **Multi-tenant change**: include tenant isolation regression test in
  the QA pass.

## Test prompts

### Should trigger (5)
1. "Prepare release notes for v0.5 of our SaaS."
2. "Make a deploy checklist + rollback plan for tomorrow's release."
3. "Production release: WhatsApp reminders feature."
4. "Go-live pack for the salon booking SaaS."
5. "Version release pack — what changed since last week."

### Should NOT trigger (3)
1. "Is the deploy ready or not?" (→ `leadup-deploy-checker`)
2. "Generate test cases." (→ `leadup-qa-test-case-generator`)
3. "Update STATUS.md." (→ `leadup-status-updater`)

### Functional test cases (2)
1. Given "main..release/v0.5.0 with WhatsApp BSP wiring + Razorpay
   refund + 1 schema migration", return a release pack with grouped
   changes, migration forward + rollback notes, env-var diff, manual
   + automated test status, top 3 risks with mitigation, a rollback
   plan with exact commands, client-comms templates, and a Go/No-Go.
2. Given "production release with one destructive migration and no
   QA pass yet", return No-Go with the top reason, list what needs to
   change to flip to Go, and route the work to
   `leadup-qa-test-case-generator` and `leadup-deploy-checker`.

## Success criteria

- All 11 sections present in order.
- Rollback plan has exact commands or named ops.
- Test status uses pass / fail / unknown (no invented numbers).
- Risks have severity + mitigation each.
- Client communication includes internal + paying-clients + public.
- Go / No-Go is one line with top reason.
- Hand-offs to `leadup-deploy-checker`, `leadup-human-content-editor`,
  and `leadup-status-updater` explicit.
