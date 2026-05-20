# API verification checklist — LeadUp

Before recommending an API, open its **official docs** and verify each
of the items below. The public-apis directory is **not** truth.

## 1. Authentication

- [ ] Auth method named in the docs (none / API key / OAuth2 / JWT /
      mTLS / signed request).
- [ ] If API key: where it sits (header / query / body). Query strings
      are a leak risk in logs.
- [ ] If OAuth2: scopes documented, refresh-token flow documented,
      token lifetime stated.
- [ ] Key rotation supported.

If unclear → label **requires verification** and link the docs.

## 2. Transport

- [ ] HTTPS (no HTTP fallback).
- [ ] TLS version stated, if available.
- [ ] No mixed-content issues for browser use.

If HTTPS is missing → drop for production.

## 3. CORS / browser use

- [ ] CORS headers documented for the endpoints we need.
- [ ] If no CORS, plan a **backend proxy**.
- [ ] Public token vs secret token cleanly separated (Stripe-style
      `pk_*` vs `sk_*` ideal).

Never embed a secret key in client code.

## 4. Pricing + free tier

- [ ] Current free-tier limits (per day / month / minute).
- [ ] Trial vs forever-free distinction stated.
- [ ] Paid tiers and per-call pricing visible.
- [ ] India INR billing + GST invoice (if relevant).
- [ ] Hard caps + behavior beyond cap (throttle vs error vs charge).
- [ ] Commercial use **allowed without restriction** for LeadUp client
      work (NOT "personal use only").

If pricing isn't visible → label **requires verification** and link
the pricing page.

## 5. Rate limits

- [ ] Per-minute / per-day limits.
- [ ] Burst behavior (does it spike OK or fail at the second over?).
- [ ] HTTP 429 response shape + retry headers (`Retry-After`).
- [ ] Whether limits are per key, per IP, or per account.

## 6. Reliability + maintenance

- [ ] Status page URL exists.
- [ ] Recent incident history is acceptable.
- [ ] Changelog or release notes recent (< 24 months).
- [ ] GitHub repo / SDK actively maintained (if applicable).
- [ ] SLA stated for paid tiers.

If last release > 24 months and no incident page → recommend
"prototype only" at best.

## 7. SDK + ecosystem

- [ ] Official SDK for the LeadUp stack (Node / Python / Dart /
      PHP / Go / Java).
- [ ] OpenAPI / Swagger spec available.
- [ ] Postman collection or sample requests.
- [ ] Community libraries listed (with stars / last commit).

## 8. Webhooks (if needed)

- [ ] Events documented.
- [ ] Retry policy (count, backoff, dead-letter).
- [ ] Signature verification documented (HMAC + secret).
- [ ] Idempotency keys recommended on inbound.
- [ ] Local testing / replay tools (e.g. ngrok-friendly).

## 9. Data privacy + residency

- [ ] What PII the API sees (contact / financial / health / location /
      kids / govt ID).
- [ ] Where data is processed (India / EU / US / global).
- [ ] DPA / Subprocessor list link.
- [ ] Training opt-out for AI providers.
- [ ] Retention of request logs at the provider.

Route to `leadup-pii-risk-reviewer` if PII is involved.

## 10. Commercial use safety

- [ ] License / terms allow paid commercial deployment.
- [ ] Attribution requirement noted (some free maps APIs require
      visible attribution).
- [ ] Brand-use restrictions (e.g. "powered by X" badges).
- [ ] Region-specific restrictions (some APIs ban export to specific
      countries).

If "free for personal use only" — drop for LeadUp client work.

## 11. India / global specifics

- India:
  - GST invoice with GSTIN.
  - INR billing.
  - India region option (lower latency for payments / BSP).
  - For payments: KYC, RBI guidance; route to
    `leadup-security-review`.
- Global:
  - GDPR / SCC if EU.
  - SOC 2 path for B2B enterprise.

## 12. Backend proxy decision

Default to backend proxy if **any** of these is true:

- Secret API key needed.
- Pricing scales with calls (rate-limit + cache at proxy).
- Provider has no CORS.
- PII passes through (so we can redact / log responsibly).
- We need to swap providers without changing the client.

## 13. What goes into the report

Per candidate, write down:

- Verified items (from above).
- Items labelled **requires verification** with the exact docs URL +
  what to confirm.
- The access date (so reviewers know how fresh the verification is).

Never quote a number from the public-apis directory as truth.
