---
name: leadup-security-review
description: Run a security review of a LeadUp project. Checks committed secrets and .env handling, auth and admin protection, multi-tenant isolation, database exposure, file uploads, payments and webhook verification, and server/deploy risks, then reports findings by severity. Use when the user says "security review", "check secrets", "is this safe", "audit project", "check .env", or "payment security".
---

# LeadUp Security Review

## Purpose

Find security problems in a LeadUp project before they reach production:
leaked secrets, weak auth, cross-tenant leakage, exposed databases, unsafe
uploads, unverified payments/webhooks, and risky deploy config — reported by
severity with fixes. Read-only; never prints secret values.

## When to use

Trigger phrases: "security review", "check secrets", "is this safe", "audit
project for security", "check .env", "payment security", "are we leaking
keys", "review auth", "is the admin panel protected".

For general "what's left in this repo" (not security) → use
`leadup-existing-repo-analyzer`. For deploy readiness (which includes a
lightweight security gate) → `leadup-deploy-checker`.

## Inputs needed

- The repo path.
- Whether payments/webhooks/uploads/multi-tenant features are in scope.
- Read access to code (not `.env` values — key names only).

## Step-by-step workflow

Use `references/security-rules.md`. Optional helper:
`scripts/scan_secrets.py` (read-only regex sweep; redacts values).

1. **Secrets**: scan for committed keys/tokens/URIs (patterns in
   security-rules.md). Report `path:line` with the value **redacted**. Check
   `.gitignore` covers `.env*`.
2. **Auth & admin**: every admin/API route requires auth; no unauthenticated
   admin endpoints; session/JWT handling sane.
3. **Multi-tenant isolation**: every query scoped by tenant; test for
   cross-tenant access (LeadUp SaaS pattern).
4. **Database**: not publicly exposed; least-privilege users; no creds in code.
5. **Uploads**: type/size validation; no execution; stored safely/scanned.
6. **Payments/webhooks**: Razorpay webhook signature verified; amount verified
   server-side; idempotency; never trust client price/status.
7. **Server/deploy**: non-root containers, TLS, firewall, backups, rotation.
8. **Report** findings by severity with concrete remediation.

## Required output format

1. **Risk summary** — counts by severity (Critical/High/Medium/Low).
2. **Findings table** — id | severity | area | location (redacted) | impact |
   fix.
3. **Secrets** — any leaked secret flagged (value redacted) + rotation steps.
4. **Top 3 must-fix** before any deploy.
5. **Residual risk / accepted** — with rationale.

## Safety rules

See `references/security-rules.md`. Most relevant here:
- Never print a secret's value — redact and reference `path:line` only.
- Never ask the user to paste secrets; recommend rotation + history scrub.
- Read-only: do not "fix" by disabling controls; recommend, don't auto-change.

## Common mistakes

- Printing the leaked key while reporting it (defeats the purpose).
- Checking auth on login but missing an unprotected admin/API route.
- Assuming multi-tenant isolation without tracing a query path.
- Treating Razorpay webhooks as trusted (no signature verification).
- Trusting client-sent amount/status in payment confirmation.
- Calling it "safe" after only a secrets scan.

## Troubleshooting

- **Under-triggers**: user said "is this okay to ship" — re-invoke; suggest
  trigger phrases.
- **Over-triggers** for general repo state → route to
  `leadup-existing-repo-analyzer`.
- **Missing tool/MCP**: run `scripts/scan_secrets.py` locally or apply the
  manual checklist from security-rules.md.
- **No internet/browser**: fine — review is static/local.
- **Missing project files**: review what exists; list absent
  `SECURITY.md`/`.gitignore` as findings.
- **Build/test failure**: not required for a static review; if dynamic checks
  fail, note as inconclusive — never weaken controls to test.

## Test prompts

### Should trigger (5)
1. "Security review of the jewellery SaaS before launch."
2. "Check secrets — are we leaking any API keys in this repo?"
3. "Is the salon app's admin panel actually protected?"
4. "Payment security check on the Razorpay integration."
5. "Audit this project for security — multi-tenant leakage especially."

### Should NOT trigger (3)
1. "What's left to build in this repo?" (→ existing-repo-analyzer)
2. "Is Docker ready for deploy?" (→ deploy-checker)
3. "Make the UI premium." (→ premium-ui-upgrader)

### Functional test cases (2)
1. A repo with a hardcoded `rzp_live_...` key → flagged Critical with value
   redacted and rotation steps; the key value is never printed.
2. A SaaS query missing a tenant filter → flagged as cross-tenant isolation
   High with the file location.

## Success criteria

- All eight areas reviewed; findings ranked by severity with fixes.
- Every secret reported with value redacted; rotation advised.
- Top must-fix items called out before deploy.
- Nothing auto-changed; no control disabled; no secret printed.
