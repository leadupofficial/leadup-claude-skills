# SaaS MVP plan — [Product name]

> Date: [YYYY-MM-DD]  ·  Idea stage: [napkin / validated / prototype]
> Target market: [India tier-2 / global / both]
> Team size: [N]  ·  Launch goal: [N weeks]

## 1. Brief restate

[One line: who, what, how monetised, by when.]

## 2. The paid job

> "Help [persona] do [job] in [time], so [outcome], for [₹X/month]."

## 3. Target users

### Persona A — [name, e.g. "Salon owner, tier-2 city"]
- Role + market: […]
- Top jobs today: […]
- Top pains: […]
- Where they hang out: […]

### Persona B (optional)
[…]

## 4. First paid feature

> [The one feature that justifies a credit card on day 1.]

Why this and not others: [one paragraph]

## 5. MVP modules (≤ 6)

| # | Module | Primary role | Outcome | Complexity |
|---|---|---|---|---|
| 1 | Auth + onboarding | all | sign in, create org | M |
| 2 | [Core entity CRUD] | org admin | manage [entity] | M |
| 3 | [Schedule / calendar] | staff | daily view | M |
| 4 | [Reminders] | system → customer | reduce no-show | M |
| 5 | [Billing + plan] | org owner | pay monthly | M |
| 6 | [Admin panel basic] | org admin | manage settings | M |

## 6. User roles

| Role | Core jobs |
|---|---|
| Super admin (LeadUp) | manage orgs, billing |
| Org owner | full control inside org |
| Org admin | manage staff + settings |
| Staff | day-to-day work |
| Customer / end-user | books, receives reminders |
| Accountant (opt) | read-only invoices |

## 7. Tenant model

> Decision: **multi-tenant by row** with `org_id` on every queryable
> table, indexed, plus app-level / RLS enforcement.
> Why: simplest viable model for LeadUp's stack, supports India
> tier-2 small-business scale, easy to migrate to schema-multi later
> if compliance demands.

## 8. Admin panel scope (handed to `leadup-admin-panel-planner`)

- Org settings (name, address, GSTIN, logo).
- Staff management (invite, roles).
- Plan + billing (current plan, invoices, payment method).
- Reports (basic KPIs).
- Integrations (WhatsApp BSP, Razorpay).
- Audit log (minimal — who did what).

## 9. Subscription direction

- Model: **per-location** (best fit for service businesses) OR **flat
  monthly per org**.
- Billing period: monthly + annual (annual = monthly × 12 × 0.85, 15%
  discount band).
- Currency: INR (India) / USD (international).
- Tax: GST 18% (India IT services); update if otherwise.

Tier design deferred to `leadup-pricing-package-planner`.

## 10. Database plan

Tables (high-level):

| Table | Key columns | Multi-tenant | PII | Notes |
|---|---|---|---|---|
| `orgs` | id, name, gstin | n/a | maybe (gstin) | tenant root |
| `users` | id, org_id, name, email, phone | org_id | yes (name, email, phone) | role on join |
| `org_users` | org_id, user_id, role | org_id | n/a | many-to-many |
| `bookings` | id, org_id, customer_id, slot, status | org_id | maybe | index on (org_id, slot) |
| `customers` | id, org_id, name, phone, email | org_id | yes | index on (org_id, phone) |
| `payments` | id, org_id, booking_id, amount, status | org_id | financial | sensitive |
| `reminders` | id, org_id, booking_id, channel, status | org_id | n/a |  |
| `invoices` | id, org_id, payment_id, gst | org_id | financial | sensitive |

Indexes flagged: `(org_id, …)` on every table; `(org_id, phone)` on
customers; `(org_id, slot)` on bookings.

PII routed to `leadup-pii-risk-reviewer`.

## 11. Integrations

| Need | Pick | Notes | Hand-off |
|---|---|---|---|
| Payments | Razorpay | UPI + cards + netbanking | `leadup-api-research-builder` |
| WhatsApp | [Gupshup / AiSensy / Wati] | template approval 3–7 days | `leadup-api-research-builder` |
| Email | Postmark / Resend | transactional | `leadup-api-research-builder` |
| Analytics | GA4 + PostHog | events list later | `leadup-api-research-builder` |
| Error logging | Sentry | client + server | `leadup-api-research-builder` |
| File storage | S3 / R2 | images, exports | `leadup-api-research-builder` |

## 12. Launch roadmap

| Week | Focus | Output |
|---|---|---|
| 0 | Kickoff + repo | CLAUDE.md, STATUS.md, DEPLOY.md |
| 1 | Auth + org | working signup |
| 2 | Core entity CRUD | UI + API |
| 3 | Schedule + reminders (email) | first booking flow |
| 4 | WhatsApp BSP wiring | template approved |
| 5 | Razorpay billing | first paid subscription |
| 6 | Admin + roles | org owner usable |
| 7 | QA + Playwright | tests green in Docker |
| 8 | Soft launch | first 2 paid clients |
| 9 | Iterate + polish | bugs cleared |
| 10 | Public launch | growth pack kicks in |

Post-launch (Weeks 11+): Phase 2 features, first AI feature, advanced
reports, more integrations.

## 13. Assumptions and data confidence

- **Verified:** [list]
- **Estimated:** [list — e.g. WhatsApp BSP approval time band]
- **Requires verification:** [list — e.g. final pricing, compliance
  requirements]

## 14. Hand-offs

- Pricing tiers → `leadup-pricing-package-planner`.
- Admin panel → `leadup-admin-panel-planner`.
- AI features → `leadup-ai-feature-planner` (only if in MVP).
- Integrations → `leadup-api-research-builder`.
- PII / payments → `leadup-pii-risk-reviewer`,
  `leadup-security-review`.
- Project kickoff → `leadup-project-kickoff` once approved.
- QA → `leadup-qa-test-case-generator`.
- Launch growth → Growth Marketing Pack.
