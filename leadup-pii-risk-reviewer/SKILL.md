---
name: leadup-pii-risk-reviewer
description: Review a LeadUp app, SaaS project, CRM, or client website for personal-data and privacy risks. Builds a PII inventory, identifies storage and access scope, scores risk levels, recommends masking and encryption, sets retention windows, designs export/delete flows, and drafts consent and privacy-policy notes aligned with India DPDP, IT Rules, and GDPR where applicable. Use when the user says "PII review", "personal data", "privacy risk", "customer data", "data protection", "sensitive data", "GDPR", or "India DPDP".
---

# LeadUp PII Risk Reviewer

## Purpose

Take a project (codebase, schema, admin panel, automation, AI feature)
and produce a structured PII risk review that the LeadUp team can act
on: what PII exists, where it lives, who can see it, how risky it is,
how to mask / encrypt / retain / delete it, and what to put in the
privacy policy / consent flow.

## When to use

Use when the user wants privacy / PII risk assessed. Do **not** trigger
for security review only (use `leadup-security-review`), pure deploy
gating (use `leadup-deploy-checker`), or admin panel design only (use
`leadup-admin-panel-planner`).

Trigger phrases: "PII review", "personal data", "privacy risk",
"customer data", "data protection", "sensitive data", "GDPR", "India
DPDP", "privacy audit", "consent flow".

## Inputs needed

- Project context (stack, schema if available, sample data shape).
- Industry (regulated? clinic / finance / kids / real estate).
- Markets served (India, EU, US, Middle East, global).
- Tenant model (single / multi-tenant).
- Existing privacy policy / consent flow (link or text).
- Sub-processors (Razorpay, BSP, email, analytics, AI providers,
  hosting).
- Any past incident or audit findings.

Ask at most 2 clarifying questions if industry or markets are unclear.

## Tools/resources to use

- `references/pii-risk-framework.md` — categories, scoring, defaults.
- `assets/pii-risk-review.template.md` — output shape.
- `leadup-security-review` — for sensitive scopes / secrets handling.
- `leadup-admin-panel-planner` — to wire masking + audit log.
- `leadup-api-research-builder` — for sub-processor DPA / data flow
  questions.
- `leadup-saas-mvp-planner` / `leadup-feature-option-planner` — when
  the review feeds back into product design.
- `leadup-human-content-editor` — for the public-facing privacy
  policy + consent copy.

## Step-by-step workflow

1. **Restate** the project + markets + tenant model + regulated
   status.
2. **PII inventory**: list every PII field (table.column or form
   field), with category (Identifier / Contact / Financial / Health /
   Demographic / Behavioral / Government ID / Biometric / Child).
3. **Data flow**: where each PII field enters, where it lives, who
   accesses it (role), where it leaves (sub-processors), how it's
   logged.
4. **Risk score** per field: low / med / high / critical, with one-
   line reason.
5. **Masking** rules: default mask + reveal path + audit-log event.
6. **Encryption** rules: in transit (TLS), at rest (column-level for
   sensitive, full-disk otherwise), key rotation cadence.
7. **Retention** windows: per category; how long, why, deletion job.
8. **Export / delete (DSR)**: how a user can request export / delete;
   internal SLA.
9. **Consent flow**: where, when, what text, where stored, withdrawal
   path.
10. **Privacy policy notes**: short bullets for the policy page; pass
    final copy through `leadup-human-content-editor`.
11. **Developer checklist**: concrete code-level checks for the team.

## Required output format

One Markdown review with these sections, in this order:

1. **Brief restate** — project, markets, tenant model, regulated.
2. **PII inventory** — table: field · category · table.column /
   form · scope · sensitivity.
3. **Data flow** — per field: entry → storage → access roles →
   exits (sub-processors) → logs.
4. **Risk scores** — per field: low / med / high / critical + reason.
5. **Masking rules** — table: field · default mask · reveal role +
   audit.
6. **Encryption** — in transit / at rest / column-level / key
   management.
7. **Retention** — per category: window + reason + deletion job.
8. **Export / delete** — DSR flow + SLA.
9. **Consent flow** — copy + storage + withdrawal.
10. **Privacy policy notes** — bullets to feed
    `leadup-human-content-editor`.
11. **Developer checklist** — code-level checks the team must
    complete.
12. **Hand-offs** — security, admin, API research, copy editor.

## Safety rules

- Do **not** read or print real `.env` values, secrets, or production
  data.
- Do **not** invent compliance status ("we are GDPR compliant"). State
  what's covered, what's gap, what's pending.
- Do **not** ignore sub-processors. Each one that touches PII gets a
  named row + a DPA status (signed / pending / requires action).
- For India: DPDP scope when in force, IT Rules consent, ASCI claims,
  KYC for fintech / payments.
- For EU users: GDPR lawful basis named, DSR SLA defined, cookie
  consent.
- For children's data: extra care — parental consent, minimal
  collection, no profiling.
- For health: stricter masking, audit on every reveal, route to legal
  if uncertain.
- For payments: don't store card details server-side (use Razorpay /
  Stripe tokenization).
- For AI features: name the model provider, confirm data-training
  opt-out, mask before send.
- Use `leadup-human-content-editor` before publishing privacy /
  consent copy.

## Common mistakes

- Listing PII without mapping who can see it.
- "We encrypt everything" — handwave. Name the layer.
- No retention window → data piles up forever.
- No DSR flow → can't comply with deletion requests.
- Logging full phone / email in plaintext.
- Sending raw PII to an LLM without redaction.
- Cookie banner that ignores user choice.
- Privacy policy written in AI-template style → low trust.

## Troubleshooting

- **No schema available**: work from form fields + admin screenshots;
  flag as **requires verification** until schema is reviewed.
- **Multi-region**: split data flows by region; respect data-residency
  if customer requires.
- **Regulated industry**: tighten masking and retention; route uncertain
  questions to a privacy / legal pro.
- **Old project with no consent record**: prioritize a consent re-
  collection flow before any new marketing automation.
- **Sub-processor without DPA**: flag as gap; pause the integration
  until DPA signed.
- **AI feature touching PII**: route to `leadup-ai-feature-planner` +
  prefer providers with no-training-by-default and DPA.

## Test prompts

### Should trigger (5)
1. "PII review for our salon booking SaaS."
2. "Privacy risk audit on the clinic app (patient notes + payments)."
3. "Data protection review for our hostel-management product."
4. "India DPDP readiness check on our CRM."
5. "GDPR review for our EU customers."

### Should NOT trigger (3)
1. "Run a full security audit." (→ `leadup-security-review`)
2. "Is the deploy ready?" (→ `leadup-deploy-checker`)
3. "Design the admin panel." (→ `leadup-admin-panel-planner`)

### Functional test cases (2)
1. Given "multi-tenant salon SaaS with phone, email, name, address,
   GSTIN, Razorpay payments, WhatsApp BSP, Anthropic AI summary",
   return a PII inventory with risk scores, masking rules, encryption
   layers, retention windows, DSR flow, consent copy, sub-processor
   list (Razorpay / BSP / Anthropic) with DPA status, and a developer
   checklist.
2. Given a clinic SaaS storing patient notes + insurance IDs in EU
   and India, return a review with tighter masking and audit on every
   reveal, residency notes, parental-consent flag if under-18 users
   exist, sub-processor scrutiny including AI provider, and routes
   uncertain compliance items to a privacy professional.

## Success criteria

- All 12 sections present in order.
- PII inventory covers every field (no "etc.").
- Each field has risk score + reason.
- Masking rules align with admin panel design.
- Encryption layers named (in transit, at rest, column where needed).
- Retention windows named per category.
- DSR flow has a stated SLA.
- Sub-processors listed with DPA status.
- Privacy policy notes ready for `leadup-human-content-editor`.
- Developer checklist is concrete (code-level).
- No invented compliance claims.
- No real secrets or PII in the output.
