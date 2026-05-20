# Safety routing rules — LeadUp

The router never executes. It plans. These rules pin the approval
gates the worker step must respect.

## 1. Approval gates (default rules)

| Action | Approval |
|---|---|
| Planning / research / writing drafts | not required |
| Reading the repo / `STATUS.md` / `DEPLOY.md` | not required |
| Editing local files (non-secret) | required (one-line confirm) |
| `git add` / `git commit` | required |
| `git push` | required (especially for `main` / `master` / `release/*`) |
| `git push --force` to shared branches | required + explicit "force push" approval |
| Deploy to Coolify / `leadup-server` / Vercel / prod | required |
| DB migration (forward) | required |
| DB rollback / destructive change | required + named approver |
| Razorpay / Stripe live charge / refund | required + named approver |
| Sending email / WhatsApp to real customers | required |
| Posting to social / publishing public copy | required |
| Rotating secrets / issuing new keys | required |
| Running production server commands (SSH) | required |
| Pasting / sending data outside the tenant | required + PII review |

When in doubt → approval required.

## 2. Hard "never do this" rules

- **Never read or print real `.env` values** in router output.
- **Never ask the user to paste secrets** (API keys, tokens, card
  numbers, passwords, OTPs).
- **Never send real customer PII to a third-party model** for a
  routing decision.
- **Never plan tactics that violate platform policy** (Meta cold
  WhatsApp, Google misleading ad copy, fake reviews, fake countdowns).
- **Never commit changes the user did not authorise.**
- **Never deploy without `leadup-deploy-checker` passing.**
- **Never run mass actions** (bulk email / WhatsApp / refunds /
  deletions) without an explicit approval line + dry-run.

## 3. Pack-specific safety overrides

### Development Pack
- Add `leadup-security-review` if the change touches secrets / auth /
  payments / PII.
- Add `leadup-pii-risk-reviewer` if the change touches new customer
  data.
- Always end with `leadup-deploy-checker` + `leadup-release-manager`
  + `leadup-status-updater`.

### New Project Pack
- `leadup-project-kickoff` writes only docs + `.env.example`; never
  real secrets.
- `leadup-saas-mvp-planner` must run `leadup-pii-risk-reviewer` if the
  product handles customer data.

### Growth Marketing Pack
- Planning is low-risk. Approval kicks in at:
  - Publishing copy (pass through `leadup-human-content-editor`).
  - Posting to client social accounts.
  - Spending ad budget.
  - Touching production website code (route into Development Pack).

### Human Content Pack
- No real PII or secrets inside rewrites. Use placeholders.

### Sales and Client Pack
- Never invent pricing, awards, certifications, or client names.
  `[fill in]` is mandatory until the user confirms.

### SaaS / Product Pack
- All MVPs that touch payments or PII must run
  `leadup-security-review` + `leadup-pii-risk-reviewer` before code.
- AI features must pass `leadup-ai-feature-planner` cost ledger + non-
  AI fallback + redacted logs.

### QA / Release Pack
- No live keys in test environments.
- Razorpay / Stripe **test mode** only.
- Tenant isolation must be tested before any multi-tenant release.
- Default to **No-Go** when destructive migration + no rollback plan.

### Automation Pack
- WhatsApp: opt-in recorded or no broadcast. Cold outreach is banned.
- n8n: credentials as placeholders only. Webhook signatures verified.
  Manual approval for refunds / mass actions.
- API integrations: never expose secret keys in client code.

### Security and Compliance Pack
- Always Claude Sonnet / Opus.
- Always approval-required for any change.
- Always update `STATUS.md` + `DEPLOY.md` after a sensitive change.

### Creative Assets Pack
- License verified before recommendation. "Free for personal" is not
  free for LeadUp client work.
- No competitor copy or design used as-is.

### API and Resource Research Pack
- Public-apis directory is discovery only — never quoted as truth.
- Official docs + access date required for every claim.
- Backend proxy for any browser flow that needs a secret key.

## 4. Memory updates the worker must make

At the end of any worker run, the router report must list which memory
files to update:

- `STATUS.md` — what shipped / what's blocked / next single task.
- `TODO.md` — outstanding work.
- `CHANGELOG.md` — user-visible changes.
- `DEPLOY.md` — deploy steps, env vars, rollback.
- `PROJECT.md` — high-level architecture and decisions.
- `AGENTS.md` — agent-specific notes for the next session.
- `SECURITY.md` — any new sensitive scope.

Default chain for a code release:

> `leadup-status-updater` updates `STATUS.md` + `TODO.md` +
> `CHANGELOG.md`. The worker also bumps `DEPLOY.md` if env vars
> changed.

## 5. Regulated industries

Trigger automatic additions to the chain:

| Industry | Auto-add |
|---|---|
| Clinic / dental / hospital | `leadup-pii-risk-reviewer`, disclaimer copy |
| Finance / lending / wallet | `leadup-security-review`, `leadup-pii-risk-reviewer`, KYC flag |
| Real estate | RERA flag, listing claim review |
| Kids / education | parental consent flag, minimal data collection |
| Gambling / alcohol / adult | drop unless licence confirmed |

## 6. India-specific gates

- GST invoicing format for any paid product.
- DPDP (when in force) for PII flows.
- IT Rules for content + WhatsApp.
- ASCI for marketing claims.
- DLT for SMS (not WhatsApp).
- Razorpay KYC for payments.

The router report names which of these apply.

## 7. Final rule of thumb

If a request can be planned without sending data, doing IO, or
touching production — do it. If it can't — output the plan, the
super-prompt, and stop. Let the worker request approval at the gate.
