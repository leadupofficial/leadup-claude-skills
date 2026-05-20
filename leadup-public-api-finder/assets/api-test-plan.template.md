# API test plan — [Provider]

> Date: [YYYY-MM-DD]  ·  Project: [name]
> Selected API: [provider + endpoint]
> Test scope: [integration smoke + edge cases + webhook]

## 1. Test environments

- Local: `.env.local` with test / sandbox keys (never live keys).
- Staging: Coolify env with test keys; real network; mock external
  side effects where relevant.
- Prod: live keys; only smoke + canary.

## 2. Test fixtures (3–5 minimum)

### Fixture 1 — Happy path

```
Name: happy path
Input: [valid sample input]
Expected:
  - HTTP 200
  - response schema matches docs
  - downstream side effect occurs (CRM upsert / sheet log / WhatsApp send)
```

### Fixture 2 — Auth failure

```
Name: invalid key
Input: same as happy path
Setup: temporarily replace key with an invalid value (env override)
Expected:
  - HTTP 401 / 403
  - structured error surfaced to UI
  - no secret leaked in logs
  - alert at threshold (e.g. > 3 in 5 min)
```

### Fixture 3 — Rate-limited

```
Name: 429 rate-limited
Input: same as happy path
Setup: force 429 via provider sandbox OR test double
Expected:
  - retry × 3 with backoff respecting `Retry-After`
  - on final failure → degrade (cache / queue / fallback API)
  - app stays responsive (no thread / queue starvation)
```

### Fixture 4 — Downstream 5xx

```
Name: provider 5xx
Input: same as happy path
Setup: force 503 via test double
Expected:
  - retry × 3 with backoff
  - circuit-break after threshold
  - fallback API engaged
  - alert raised
```

### Fixture 5 — Malformed payload (provider)

```
Name: malformed provider response
Input: same as happy path
Setup: stub provider to return non-JSON / missing fields
Expected:
  - graceful failure with structured error
  - no crash; no PII leaked
  - alert raised
```

### Fixture 6 (if webhooks) — Inbound webhook + signature

```
Name: inbound webhook good
Input: signed POST to /api/webhooks/[provider]
Setup: valid HMAC with PROVIDER_WEBHOOK_SECRET
Expected:
  - 200
  - dedupe by event id
  - side effect applied once even on replay
```

```
Name: inbound webhook bad signature
Input: POST with tampered body
Expected:
  - 401
  - no side effect
  - alert raised
```

## 3. Security tests

- [ ] Secret key never appears in client bundle.
- [ ] Secret key never logged or echoed in error messages.
- [ ] CORS preflight behaves as documented (browser flows only).
- [ ] Webhook endpoint rejects unsigned requests.
- [ ] Replay of an old webhook is deduped.
- [ ] Logs redact PII (phone hashed, email truncated, body summarised).

## 4. Performance / cost tests

- [ ] Latency p50 / p95 within acceptable band for the feature.
- [ ] Cap on calls/user/min in our code, below provider limit.
- [ ] Cache hit rate for safe lookups (where applicable).
- [ ] Monthly call estimate × provider price ≤ tier price (for AI /
      paid APIs).

## 5. Compliance / PII tests

- [ ] No PII fields leave the tenant beyond what the API needs.
- [ ] DPA / region settings confirmed.
- [ ] Consent recorded (if customer-facing).
- [ ] Retention windows respected for cached responses.

## 6. Acceptance criteria

- [ ] All happy paths green.
- [ ] All failure modes degrade gracefully (no crash, no PII leak).
- [ ] Rate-limit + fallback engaged when forced.
- [ ] Webhook signature verified end-to-end.
- [ ] Monitoring shows latency, error rate, and cost per day.
- [ ] Feature flag tested (off → returns the non-API fallback).

## 7. Hand-offs

- Wider QA pass → `leadup-qa-test-case-generator`.
- Test execution → `leadup-browser-playwright-tester`.
- Release gating → `leadup-deploy-checker`,
  `leadup-release-manager`.
- Security pass → `leadup-security-review`.
- PII pass → `leadup-pii-risk-reviewer`.
