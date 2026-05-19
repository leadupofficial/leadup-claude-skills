# LeadUp Security Rules (pack-wide)

Every skill in this pack must obey these rules. Each SKILL.md carries a short
"Safety rules" block that points back here plus the 2–3 rules most relevant to
that skill.

## Secrets

- **Never read or print real `.env` / `.env.local` / `.env.production` values.**
  You may list which keys exist, never their values.
- **Never echo, log, or paste API keys, tokens, passwords, or connection
  strings**, even if they appear in a file you opened.
- **Never ask the user to paste a secret** into chat. If a value is needed,
  ask them to set it in `.env` themselves and reference it by key name.
- **Never commit secrets.** Only `.env.example` with placeholder values like
  `RAZORPAY_KEY_ID=__SET_ME__`. Placeholders must not look like real keys.
- If you detect a real secret committed or about to be committed, **stop**,
  warn clearly, and recommend rotation + `.gitignore` + history scrub.

## Patterns that indicate a leaked secret (flag, never print the value)

- `sk-...`, `sk-proj-...` (OpenAI), `AIza...` (Google), `ghp_...` / `github_pat_`
- `xox[bpas]-...` (Slack), `rzp_live_...` / `rzp_test_...` (Razorpay)
- `AKIA...` + 40-char secret (AWS), `-----BEGIN ... PRIVATE KEY-----`
- Postgres/Mongo URIs with embedded credentials, JWT signing secrets

Report as: "Possible <provider> key found in `path:line` — value redacted."

## Actions

- **No push without approval.** No deploy without approval. No remote SSH
  without approval. No destructive commands without approval.
- Prefer **read-only** operations and dry-runs. Escalate to write/exec only
  with explicit user go-ahead.
- Do not disable security controls (auth, CORS, rate limits, CSP) to "make it
  work". Flag the blocker instead.

## Application security baseline (what reviews check)

- Auth on every admin/API route; no admin endpoints reachable unauthenticated
- Multi-tenant isolation: every query scoped by tenant; no cross-tenant leakage
- DB not exposed to the public internet; least-privilege DB users
- File uploads: type/size validation, no execution, stored off web root or scanned
- Payments (Razorpay): verify webhook signatures, verify amount server-side,
  never trust client-sent price/status
- Webhooks: signature verification + idempotency
- Secrets in env, not in code or client bundles
- Dependencies: no known-critical CVEs in shipped deps
- Server/deploy: firewall, non-root containers, TLS, backups, rotation plan
