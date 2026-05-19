# SECURITY — <project>

## Auth model
<how users/admins authenticate; session/JWT; password policy>

## Multi-tenant isolation
<shared schema + tenant_id | schema-per-tenant; how every query is scoped>

## Secrets handling
Env only. Never in code, client bundle, repo, or chat. `.env.example`
placeholders only.

## Payments / webhooks
<Razorpay: verify webhook signature, verify amount server-side, idempotency>

## Uploads
<type/size validation, storage location, scanning>

## Known risks / TODO
- 
