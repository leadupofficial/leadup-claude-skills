# API integration plan — [Provider]

> Date: [YYYY-MM-DD]  ·  Project: [name]
> Selected API: [provider + endpoint]
> Backup API: [provider + endpoint]
> Runtime: [browser / server / both]

## 1. Placement

- Where the call runs: [server-side / client-side via public token /
  client-side via backend proxy].
- Why: [one line — secret key, rate-limit caching, PII redaction, CORS].
- Service responsible: [`apps/web`, `apps/api`, `apps/admin`, n8n, etc.]

## 2. Env variables (placeholders only)

```
# .env.example  -- never commit real values
[PROVIDER]_API_KEY=__SET_ME__
[PROVIDER]_API_BASE=https://api.[provider].com/v1
[PROVIDER]_PUBLIC_KEY=__SET_ME__   # optional, browser-safe key
[PROVIDER]_WEBHOOK_SECRET=__SET_ME__   # if webhooks used
[PROVIDER]_REGION=in     # optional, regional endpoint
```

Storage:
- Coolify env (production).
- `.env.local` for dev (git-ignored).
- Never in repo, browser bundle, logs.

## 3. Auth shape

- Header: `Authorization: Bearer {{API_KEY}}` (preferred) OR custom
  header per docs.
- Avoid query-string keys (leak in access logs).
- Key rotation cadence: [12 months / on incident].

## 4. Request shape (quick code skeleton — illustrative)

```ts
// Node / TypeScript pseudo-skeleton
const res = await fetch(`${env.PROVIDER_API_BASE}/lookup`, {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${env.PROVIDER_API_KEY}`,
    "Content-Type": "application/json",
    "Idempotency-Key": idempotencyKey,
  },
  body: JSON.stringify({ email }),
});

if (res.status === 429) {
  // honour Retry-After; degrade gracefully (cache, queue, or fallback API)
}

if (!res.ok) {
  // structured error; log redacted; alert at threshold
}
```

## 5. Rate-limit strategy

- Provider documented limits: [X req/min, Y req/day].
- LeadUp app cap (defensive): [lower than provider, e.g. 80% of limit].
- On 429: respect `Retry-After`; exponential backoff up to 3 attempts;
  then queue / cache / fallback to backup API.
- Cache: cache successful lookups by input hash for [N] minutes where
  safe.

## 6. Error handling

| Error | Action |
|---|---|
| 4xx (auth, validation) | log redacted; surface clear UX message |
| 429 (rate limit) | backoff + retry; degrade |
| 5xx (provider) | retry × 3 with backoff; circuit-breaker |
| network | retry × 3; fallback API |
| signature invalid (webhook) | reject 401; alert |

## 7. Webhooks (if applicable)

- Endpoint: `/api/webhooks/[provider]`
- HMAC: verify with `PROVIDER_WEBHOOK_SECRET` before processing.
- Idempotency: dedupe by `event.id`.
- Dead-letter: write redacted payload to a logs table / sheet on
  permanent failure.

## 8. Security + privacy

- PII categories the API sees: [list].
- Redact before send: [fields].
- DPA / data residency: [provider region, link].
- Logs: never raw PII; phone hashed; email truncated.

Route to `leadup-pii-risk-reviewer` for sign-off.

## 9. Frontend handling (if any)

- If browser-only with a public token: confirm CORS for the exact
  endpoints we call.
- If secret key is required: switch to a backend route at
  `/api/[provider]/...` that proxies the call.
- Never embed a secret key in client code or env exposed at build.

## 10. Backup / fallback

- Trigger fallback to backup API when:
  - 3 consecutive 5xx from primary, OR
  - 429 with no `Retry-After`, OR
  - Status page incident detected (manual or auto).
- Backup API call shape: [link to its docs].
- Behaviour differences worth noting: [list].

## 11. Implementation plan (steps)

1. [Create the .env.example placeholders] (this commit).
2. [Wire the server-side client + auth header].
3. [Add rate-limit cap + retry + 429 handling].
4. [Add cache for safe lookups].
5. [Wire webhook with HMAC + idempotency] (if applicable).
6. [Hide secret behind backend proxy] (if browser-driven).
7. [Add structured logging with redaction].
8. [Add fallback to backup API on circuit break].
9. [Add a kill-switch feature flag for the whole feature].
10. [Write tests — see `api-test-plan.template.md`].

## 12. Hand-offs

- Deeper integration research → `leadup-api-research-builder`.
- Workflow wiring → `leadup-n8n-workflow-builder`.
- PII / security review → `leadup-pii-risk-reviewer`,
  `leadup-security-review`.
- Release coordination → `leadup-release-manager`.
- QA execution → `leadup-qa-test-case-generator`.
