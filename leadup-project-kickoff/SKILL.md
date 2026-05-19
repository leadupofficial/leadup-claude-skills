---
name: leadup-project-kickoff
description: Bootstrap a new LeadUp project from an idea, spec, or client requirement. Produces PROJECT.md, CLAUDE.md, STATUS.md, DEPLOY.md, SECURITY.md, README.md, a placeholder .env.example, plus a stack recommendation, database plan, MVP roadmap, and deployment plan. Use when the user says "start new project", "new SaaS idea", "build new app", "create project", "project kickoff", or "new LeadUp project".
---

# LeadUp Project Kickoff

## Purpose

Turn a new idea, spec, PDF, screenshot, or client requirement into a clean,
resumable LeadUp project foundation: the project memory files, a recommended
stack, a database plan, an MVP roadmap, and a deployment plan — before any
feature code is written. Follows the LeadUp loop in
`references/leadup-workflow.md`.

## When to use

Use when starting something new and there is no existing project memory yet.

Trigger phrases: "start new project", "new SaaS idea", "build new app",
"create project", "project kickoff", "new LeadUp project", "spin up a new
client site", "scaffold a new app", "begin a new build".

Do **not** use for an existing repo that already has code/STATUS.md — use
`leadup-existing-repo-analyzer` instead.

## Inputs needed

- The source: idea description, PDF, screenshot, spec file path, Google Drive
  notes, or client requirement message. Ask for it if missing.
- Target: client name / working title, rough scope, any hard constraints
  (deadline, must-use stack, budget).
- Whether it is multi-tenant SaaS, a single client site, a Flutter app, etc.

If the source is thin, ask 3–5 sharp scoping questions before planning.

## Step-by-step workflow

1. **Read the source deeply.** Summarize what is being built, for whom, and
   the one core value flow. Restate it back for confirmation.
2. **Research + plan (no code yet).** Note unknowns, similar LeadUp projects,
   and risks. Identify integrations (Razorpay, WhatsApp, Gemini/DeepSeek, SMTP).
3. **Recommend a stack** with a one-line rationale and 1 alternative. Default
   to LeadUp norms: Next.js / Node-TS / Postgres / Docker / Coolify; Flutter
   for mobile; Laravel/Bagisto for ecommerce when it fits.
4. **Database plan.** Core entities, relationships, multi-tenant strategy
   (shared schema + tenant_id vs schema-per-tenant), key indexes.
5. **MVP roadmap.** Milestones 0–3 (skeleton+auth+deploy → core flow →
   billing/admin → polish/launch), each with a definition of done.
6. **Deployment plan.** Docker shape, Coolify service, target
   `*.leadup.in` subdomain, env keys needed (names only), rollback note.
7. **Generate project files** from `references/project-docs-template.md`
   and this skill's `assets/`: `PROJECT.md`, `CLAUDE.md`, `STATUS.md`,
   `DEPLOY.md`, `SECURITY.md`, `README.md`, `.env.example` (placeholders only).
8. **Present the plan + file list, then stop.** Do not write feature code,
   create a GitHub repo, push, or deploy without approval.

## Required output format

1. **Project summary** (3–5 lines).
2. **Stack recommendation** (table: layer | choice | why | alternative).
3. **Database plan** (entities + multi-tenant strategy).
4. **MVP roadmap** (milestones with done-criteria).
5. **Deployment plan** (Docker/Coolify/subdomain/env-key-names/rollback).
6. **Files created** (list with paths).
7. **Next recommended task** (one concrete step) + "awaiting approval to
   start coding / create repo".

## Safety rules

See `references/security-rules.md`. Most relevant here:
- `.env.example` uses placeholders only (`KEY=__SET_ME__`); never real values.
- Do not create a GitHub repo, push, or deploy without explicit approval.
- Do not invent client/legal commitments; mark assumptions as assumptions.

## Common mistakes

- Writing feature code during kickoff (kickoff is plan + scaffolding only).
- Generating `.env` with realistic-looking fake keys instead of `__SET_ME__`.
- Skipping the multi-tenant decision (it shapes the schema — decide early).
- Vague MVP with no definition of done per milestone.
- Forgetting `CLAUDE.md`, so future sessions lose project context.

## Troubleshooting

- **Skill under-triggers** (user said "set up X" and it didn't fire): re-invoke
  explicitly; suggest the trigger phrases above.
- **Skill over-triggers** on an existing project: hand off to
  `leadup-existing-repo-analyzer`; do not overwrite existing memory files.
- **Missing tool/MCP** (no web research available): proceed with stated
  assumptions, mark research gaps, recommend revisiting before build.
- **No internet/browser**: skip live research; flag pricing/limits as
  "verify before integration".
- **Missing project files / empty source**: ask scoping questions; do not
  fabricate scope.
- **Build/test failure**: not applicable at kickoff (no code yet) — if asked
  to scaffold runnable code, keep it minimal and verify it builds in Docker.

## Test prompts

### Should trigger (5)
1. "Start a new project — salon booking SaaS for a client."
2. "New SaaS idea: city gold-rate alerts app, kick it off."
3. "Create project from this PDF spec and plan the stack."
4. "Project kickoff for a new LeadUp client website."
5. "Build a new Flutter app for a clinic — scaffold the foundation."

### Should NOT trigger (3)
1. "Analyze this existing repo and tell me what's left." (→ existing-repo-analyzer)
2. "Update STATUS.md after this task." (→ status-updater)
3. "Make the dashboard UI look premium." (→ premium-ui-upgrader)

### Functional test cases (2)
1. Given a 1-paragraph SaaS idea, produce all 7 memory files with a stack
   table, multi-tenant DB decision, and a 4-milestone MVP — and write no
   feature code.
2. Given a thin one-line idea, the skill asks ≥3 scoping questions before
   producing the plan (does not fabricate scope).

## Success criteria

- All 7 project files created with correct, LeadUp-appropriate content.
- `.env.example` contains only `__SET_ME__`-style placeholders.
- Stack + DB + MVP + deploy plan are concrete and decision-ready.
- No feature code, repo creation, push, or deploy performed.
- Output ends with one clear "next recommended task" + approval gate.
