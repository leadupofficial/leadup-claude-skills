---
name: leadup-deploy-checker
description: Check whether a LeadUp project is ready to deploy to leadup-server / Coolify. Verifies Docker build, env variable coverage, ports, Coolify config, GitHub branch, domain/subdomain, migrations, and a rollback plan, then outputs a READY / NOT READY verdict. Use when the user says "prepare deploy", "deploy checker", "make Docker work", "Coolify deploy", "leadup-server deploy", or "production ready".
---

# LeadUp Deploy Checker

## Purpose

Determine if a project can be deployed safely and produce an exact readiness
report. This skill **checks and plans only** — it never runs the deploy or
pushes. Deploy happens after explicit approval.

## When to use

Trigger phrases: "prepare deploy", "deploy checker", "is this production
ready", "make Docker work", "Coolify deploy", "leadup-server deploy",
"can we ship this", "pre-deploy check".

For security posture specifically → `leadup-security-review` (deploy-checker
includes a security gate but defers deep auditing to it).

## Inputs needed

- The repo path and target `*.leadup.in` subdomain.
- Intended branch (usually `main`) and Coolify service expectations.
- Whether this is first deploy or an update (affects rollback/migrations).

## Step-by-step workflow

Use `references/deploy-checklist.md`.

1. **Build & run**: Dockerfile builds clean; app serves; prod build succeeds;
   no dev/localhost URLs in prod paths.
2. **Environment**: `.env.example` covers every required key (placeholders);
   `DEPLOY.md` documents them; no secrets in image/repo/bundle.
3. **Ports & networking**: correct exposed port; no collision with other
   `*.leadup.in` apps; reverse-proxy/subdomain planned.
4. **Domain & TLS**: subdomain decided, DNS planned, TLS via Coolify.
5. **Data**: migrations idempotent; persistent volumes mapped (uploads/db);
   no weak default admin.
6. **Source control**: correct branch under `leadupofficial`; tree clean.
7. **Rollback**: previous tag/commit recorded; rollback steps in `DEPLOY.md`.
8. **Verdict + stop**: output READY/NOT READY with failing items and the
   exact commands the user runs. Do not deploy or push.

## Required output format

1. **Verdict**: READY ✅ / NOT READY ❌.
2. **Checklist results** — each section pass/fail with evidence.
3. **Blocking items** — what must be fixed first, with the fix command.
4. **Deploy commands** the user will run (for them to execute, not you).
5. **Rollback plan** — explicit.
6. **Approval gate**: "Awaiting your approval to deploy — I will not push or
   deploy."

## Safety rules

See `references/security-rules.md` and `deploy-checklist.md`. Most relevant:
- Never run `git push`, `coolify` deploy, or remote SSH — output commands and
  stop for approval.
- Never put real env values in `.env.example` or `DEPLOY.md`.
- Block deploy if secrets are in the image/repo or if data volumes aren't
  persisted (deploy would wipe data).

## Common mistakes

- Marking READY while `.env.example` is missing required keys.
- Forgetting persistent volumes → uploads/DB wiped on next deploy.
- Port collision with another app already on `leadup-server`.
- No rollback target recorded before an update deploy.
- Actually running the deploy/push instead of stopping at the gate.

## Troubleshooting

- **Under-triggers**: user said "ship it" — re-invoke; suggest trigger phrases.
- **Over-triggers** for a deep security audit → route to
  `leadup-security-review`.
- **Missing tool/MCP**: if Docker can't be run here, give the exact commands
  for the user to run and check their pasted output.
- **No internet/browser**: fine — checks are local/config; defer DNS/TLS
  verification with a note.
- **Missing project files** (`Dockerfile`/`DEPLOY.md` absent): mark NOT READY,
  list them as blockers, offer to scaffold from kickoff assets.
- **Build/test failure**: capture error, classify (deps/env/Docker), mark NOT
  READY; never disable checks to force a READY verdict.

## Test prompts

### Should trigger (5)
1. "Is the jewellery SaaS production ready for Coolify?"
2. "Prepare deploy for the venus school site to leadup-server."
3. "Deploy checker on the salon repo before we ship."
4. "Make Docker work and tell me if we can deploy."
5. "Pre-deploy check for app.leadup.in."

### Should NOT trigger (3)
1. "Do a full security audit of the payments code." (→ security-review)
2. "Browser test the login flow." (→ browser-playwright-tester)
3. "Update STATUS.md after deploy." (→ status-updater)

### Functional test cases (2)
1. On a repo with a working Dockerfile but missing volumes, verdict is NOT
   READY with "persistent volumes" as a blocker.
2. The output ends with the approval gate line and performs no push/deploy.

## Success criteria

- Every checklist section evaluated with evidence.
- Clear READY/NOT READY verdict + concrete blocking fixes.
- Rollback plan stated; commands provided for the user to run.
- No push, no deploy, no remote command executed.
