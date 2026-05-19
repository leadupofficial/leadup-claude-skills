# API Research Template

Fill this out in `leadup-api-research-builder` before writing any integration
code. Research from **official docs first**, then reputable GitHub examples.
State the date of pricing/limits info (they change).

## API: <name> — researched <YYYY-MM-DD>

### 1. Overview
- What it does / why LeadUp needs it
- Official docs URL(s)
- Official SDK (language, package name, maintained? last release)

### 2. Auth
- Method (API key / OAuth2 / JWT / HMAC)
- Where the secret lives (`.env` key name, e.g. `RAZORPAY_KEY_SECRET`)
- Test vs live mode (key prefixes, sandbox URL)

### 3. Endpoints we will use
| Purpose | Method | Path | Notes |
|---|---|---|---|

### 4. Rate limits & quotas
- Limits (req/min, monthly cap)
- Throttling/backoff guidance
- Cost tier relevant to LeadUp

### 5. Pricing (as of date)
- Free tier limits
- Paid pricing relevant to expected volume
- Gotchas (per-request, per-seat, egress)

### 6. Webhooks (if any)
- Events we subscribe to
- Signature verification method
- Idempotency strategy
- Local testing approach (tunnel/CLI)

### 7. Env variables
```
# .env.example additions (placeholders only)
<PROVIDER>_KEY_ID=__SET_ME__
<PROVIDER>_KEY_SECRET=__SET_ME__
<PROVIDER>_WEBHOOK_SECRET=__SET_ME__
```

### 8. Reference implementations
- GitHub repo(s): URL — license — stars — last commit — what to copy/adapt

### 9. Risks & failure modes
- What breaks in prod, downtime behaviour, vendor lock-in
- Compliance/data-residency notes (India relevance)

### 10. Fallback / contingency plan
- Alternate provider or degraded mode if this API is down or over quota

### 11. Recommendation
- Go / no-go, recommended package, integration outline (steps, no code yet)
