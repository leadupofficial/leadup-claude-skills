# Env placeholders — [Provider]

> Date: [YYYY-MM-DD]  ·  Project: [name]
> Provider: [name]  ·  Service that uses it: [apps/web / apps/api / n8n / …]

## How to use this file

- Copy the block below into `.env.example` of the target project.
- Never commit real values.
- Store real values in Coolify env (or your secrets vault), not in
  `.env` in the repo.
- Local dev → `.env.local` (git-ignored).
- For shared LeadUp services, store the placeholder name only; the
  actual value is set per environment.

## Placeholders

```dotenv
# ----- [Provider] integration -----

# Secret key — server-only. Never exposed to the browser.
[PROVIDER]_API_KEY=__SET_ME__

# Public / publishable key — safe in browser, scoped, low-privilege.
# Only present if the provider has a separate public-token model.
[PROVIDER]_PUBLIC_KEY=__SET_ME__

# Base URL — useful when the provider has region-specific endpoints.
[PROVIDER]_API_BASE=https://api.[provider].com/v1

# Region — for India residency where relevant (e.g. payments).
[PROVIDER]_REGION=in

# Webhook secret — verify HMAC signatures on inbound webhooks.
[PROVIDER]_WEBHOOK_SECRET=__SET_ME__

# OAuth (optional, if the provider uses OAuth2 instead of API key).
[PROVIDER]_OAUTH_CLIENT_ID=__SET_ME__
[PROVIDER]_OAUTH_CLIENT_SECRET=__SET_ME__
[PROVIDER]_OAUTH_REDIRECT=https://app.leadup.in/api/oauth/[provider]/callback
[PROVIDER]_OAUTH_SCOPES=read:basic
```

## Examples (illustrative — verify per provider)

```dotenv
# Razorpay (server-side; secret + public key separate)
RAZORPAY_KEY_ID=__SET_ME__
RAZORPAY_KEY_SECRET=__SET_ME__
RAZORPAY_WEBHOOK_SECRET=__SET_ME__

# Exchangerate.host (key-less in many cases — verify on docs)
EXCHANGERATE_API_BASE=https://api.exchangerate.host

# AbstractAPI email validation (server-side; key required)
ABSTRACTAPI_EMAIL_KEY=__SET_ME__
ABSTRACTAPI_EMAIL_BASE=https://emailvalidation.abstractapi.com/v1

# OpenWeather (server-side; key required)
OPENWEATHER_API_KEY=__SET_ME__
OPENWEATHER_API_BASE=https://api.openweathermap.org/data/2.5

# Anthropic (server-only; never in browser)
ANTHROPIC_API_KEY=__SET_ME__
ANTHROPIC_API_BASE=https://api.anthropic.com/v1
```

## Rules

- Always prefix with `<PROVIDER>_` to namespace; never collide with
  unrelated keys.
- `__SET_ME__` is the LeadUp standard placeholder for "not yet set".
  Do not paste real keys, even for testing.
- For each secret, write a one-line comment naming where it sits
  (Coolify env / vault / local dev only).
- Rotation: write the rotation cadence somewhere (operations doc / a
  `SECRETS.md`), e.g. every 12 months or on incident.
- For browser-safe keys, also document the **scope** (read-only, IP-
  restricted, domain-restricted) — never a full admin key.

## Hand-off

- For the integration code that consumes these env vars →
  `leadup-api-research-builder`.
- For workflow nodes that need credential references →
  `leadup-n8n-workflow-builder` (uses `{{n8n_creds.<name>}}`).
- For a security pass before pushing → `leadup-security-review`.
- For PII review of what the API touches → `leadup-pii-risk-reviewer`.
