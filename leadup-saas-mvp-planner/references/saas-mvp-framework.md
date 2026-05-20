# SaaS MVP framework — LeadUp

How LeadUp plans paid SaaS MVPs that ship in 6–10 weeks.

## 1. One paid job

Write it on one line:

> "Help [persona] do [job] in [time], so [outcome], for [price/month]."

If you can't write this, the idea isn't ready. Loop back to the user.

## 2. Personas (1–2 max)

Each persona has:

- Role (e.g. "salon owner", "ops manager", "founder").
- Industry + market.
- Top 3 jobs they do today.
- Top 3 pains.
- Where they hang out (used for distribution).

## 3. First paid feature

The one feature that justifies a credit card on day 1. Examples:

| Audience | First paid feature |
|---|---|
| Salon owner | Online booking + WhatsApp reminders |
| Dental clinic | Calendar + payment + reminders |
| Hostel manager | Bed allotment + invoicing + GST report |
| Tutoring centre | Class schedule + parent WhatsApp updates |
| Indie SaaS | The one workflow the founder couldn't get done elsewhere |

Everything else in MVP exists to support this one feature.

## 4. MVP modules (≤ 6)

Default shape for a service-business SaaS:

1. **Auth + onboarding** (login, signup, org create).
2. **Core entity CRUD** (the main object — booking, patient, student).
3. **Schedule / calendar** (the user-facing primary view).
4. **Reminders / notifications** (email + WhatsApp at minimum).
5. **Billing / pricing** (Razorpay or Stripe, plan + invoice).
6. **Admin panel** (org admin can manage staff, settings).

If your idea needs 8 modules to be useful, you have a Phase 2.

## 5. User roles

Default for a multi-tenant SaaS:

- **Super admin** (LeadUp side; never client-facing).
- **Org owner** (the paying customer; full control inside their org).
- **Org admin** (delegated; manages staff and config).
- **Staff** (does day-to-day work).
- **Customer / end-user** (books, receives reminders).
- **Accountant** (read-only on invoices + exports).

Each role's permissions are spelled out in the admin panel design.

## 6. Tenant model

Three options:

| Model | When |
|---|---|
| Single tenant | one client per deployment; rare for SaaS |
| Multi-tenant by row (`org_id`) | most LeadUp SaaS; simple, cheap |
| Multi-tenant by schema | strict isolation needed (clinics, finance); higher ops cost |

Default for LeadUp: **multi-tenant by row** with `org_id` on every
queryable table + RLS or app-level checks.

Decide early. Migrating later is expensive.

## 7. Subscription direction (high-level only)

- **Monthly + annual** (annual gets 10–20% discount).
- Per-user OR per-location OR flat — pick one.
- Freemium only if the free tier brings users into paid (rare for India
  SMB).
- Currency: INR-first for India market; USD for global.
- GST in India; tax handled per market.

Detailed tier design is deferred to `leadup-pricing-package-planner`.

## 8. Database plan

Required outputs:

- Tables with key columns and primary keys.
- Relationships (FK).
- Multi-tenant strategy (`org_id` on every row + index).
- PII fields flagged (name, phone, email, address, medical, financial).
- Sensitive tables (payments, KYC, medical) marked.
- Indexes flagged for the top 5 queries.
- Soft-delete strategy if needed.

PII flags routed to `leadup-pii-risk-reviewer`.

## 9. Integrations

Common stack for India SaaS:

| Need | Default | Hand-off |
|---|---|---|
| Payments | Razorpay (UPI + cards + netbanking) | `leadup-api-research-builder` |
| WhatsApp | BSP (Gupshup / AiSensy / Wati) | `leadup-api-research-builder` |
| Email | Postmark / Resend / SES | `leadup-api-research-builder` |
| Analytics | GA4 + PostHog | `leadup-api-research-builder` |
| Error logging | Sentry | `leadup-api-research-builder` |
| File storage | S3 / R2 / Bunny | `leadup-api-research-builder` |
| Search | Postgres FTS or Meilisearch | `leadup-api-research-builder` |

For global: Stripe + Twilio + SendGrid + Mixpanel.

## 10. Launch roadmap (6–10 weeks default)

| Week | Focus |
|---|---|
| 0 | Kickoff, repo, CLAUDE.md, STATUS.md, DEPLOY.md |
| 1 | Auth + org + onboarding |
| 2 | Core entity CRUD |
| 3 | Schedule + reminders (email) |
| 4 | WhatsApp BSP wiring (in parallel: BSP template approval) |
| 5 | Billing + plans (Razorpay) |
| 6 | Admin panel + roles |
| 7 | QA + Playwright tests (`leadup-qa-test-case-generator`) |
| 8 | Soft launch (staging → first 2 paid clients) |
| 9 | Iterate, fix, polish |
| 10 | Public launch, marketing kicks in (Growth Pack) |

Post-launch (Weeks 11+):
- Add Phase 2 modules (advanced reports, more integrations).
- Add first AI feature with `leadup-ai-feature-planner`.

## 11. AI features in MVP — careful

If the MVP includes an AI feature:

- Each must name the real user job.
- Cost = LLM tokens × calls/user/month must be < tier price.
- Fallback behavior defined for model down / wrong output.
- Logging + observability planned.
- Route to `leadup-ai-feature-planner`.

## 12. Honesty rules

- ≤ 6 MVP modules.
- One named first paid feature.
- Multi-tenant decision documented.
- PII flagged and routed.
- Integration depth deferred to `leadup-api-research-builder`.
- No invented ARR / customer counts.
- Compliance routed before committing.
- Roadmap is week-by-week, not "by Q3".
