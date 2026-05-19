# LeadUp Deploy Checklist

Used by `leadup-deploy-checker` (and referenced by `leadup-status-updater`).
This produces a **readiness report** — it does not deploy. Deploy only after
explicit approval.

## 1. Build & run

- [ ] `Dockerfile` present and builds clean (`docker build .`)
- [ ] `docker-compose.yml` (or Coolify config) defines all services
- [ ] App starts and serves locally (correct dev/prod command verified)
- [ ] Production build succeeds (`next build` / `npm run build` / etc.)
- [ ] No hardcoded `localhost` / dev URLs in production code paths
- [ ] Health/readiness endpoint responds (if applicable)

## 2. Environment

- [ ] `.env.example` lists every required key (placeholders only)
- [ ] All required env vars documented in `DEPLOY.md`
- [ ] No secrets in the image, repo, or client bundle
- [ ] Correct values to be set in Coolify env UI by the user (not in chat)

## 3. Ports & networking

- [ ] Container exposes the right port; mapped correctly in Coolify
- [ ] No port collision with other `*.leadup.in` apps on the server
- [ ] Reverse proxy / domain routing planned (subdomain chosen)

## 4. Domain & TLS

- [ ] Target subdomain decided (e.g. `app.leadup.in`)
- [ ] DNS record planned/exists
- [ ] TLS via Coolify/Let's Encrypt confirmed in plan

## 5. Data

- [ ] Database migrations runnable and idempotent
- [ ] Seed/admin bootstrap plan (no default weak admin password)
- [ ] Backup/restore path noted in `DEPLOY.md`
- [ ] Persistent volumes mapped (uploads, db) so deploys don't wipe data

## 6. Source control

- [ ] On the intended branch (usually `main`) under `leadupofficial`
- [ ] Working tree clean or changes intentional
- [ ] CI (if any) green

## 7. Rollback

- [ ] Previous image/tag or commit recorded to roll back to
- [ ] Rollback steps written in `DEPLOY.md`
- [ ] Down-time expectation stated

## Output

Produce: readiness verdict (READY / NOT READY), the failing items, exact
commands the user can run, and an explicit "awaiting approval to deploy" line.
Never run the deploy or `git push` yourself.
