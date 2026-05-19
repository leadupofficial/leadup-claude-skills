# DEPLOY — <project>

## Local run
<command>

## Build
<command, e.g. docker build . / npm run build>

## Env vars (names only — set real values in Coolify, never in repo/chat)
- DATABASE_URL
- JWT_SECRET
- <provider keys>

## Coolify config
- Service:
- Port:
- Persistent volumes: <uploads, db>

## Domain
- `<subdomain>.leadup.in` (TLS via Coolify/Let's Encrypt)

## Migrations
<command, idempotent>

## Rollback
- Previous tag/commit: <fill on each deploy>
- Steps: <...>
