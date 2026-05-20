# Client requirement framework — LeadUp

How LeadUp turns messy client input into clear requirements without
inventing things.

## 1. Read everything once, in their voice

- Don't summarize on the first pass.
- Copy the client's exact phrasing in 5–8 short quotes.
- Keep words that signal intent ("must", "by Diwali", "like Naturals
  salon", "WhatsApp like Zomato").

## 2. Translate into categories

Four buckets, every time:

| Bucket | What goes here |
|---|---|
| Goal | one-line outcome the client cares about |
| Must-have | features they explicitly named or strongly implied |
| Optional | "nice to have", "maybe later", "if budget allows" |
| Out of scope | items they said no to, or that don't fit budget/timeline |

If something doesn't fit, it's a **missing question**, not a guess.

## 3. Mark unknowns honestly

Common unknowns to surface:

- Audience and scale (how many users, where).
- Platforms (web only, mobile only, both).
- Payments (online / offline / both; currency).
- Timeline / launch date.
- Budget band.
- Stakeholders (who decides, who signs).
- Content readiness (logo, photos, text).
- Vendor preferences (CRM, payments, BSP).
- Legal context (GST, KYC, sector-specific licences).

## 4. Score complexity

Per feature:

| Band | Effort | Examples |
|---|---|---|
| S | < 1 week | static page, WhatsApp link, basic form |
| M | 1–3 weeks | admin CRUD, payment integration, multi-language |
| L | 3–6 weeks | multi-tenant SaaS module, advanced search, dashboards |
| XL | 6+ weeks | AI feature, marketplace, complex compliance |

Add a one-line risk note per feature (payments, PII, third-party, SLA).

## 5. Common risks to flag

- **PII / sensitive data** — clinic, school, finance, kids → route to
  `leadup-pii-risk-reviewer`.
- **Payments / KYC** — Razorpay / Cashfree onboarding, refund handling,
  reconciliation.
- **WhatsApp BSP** — template approval lag, BSP fees, opt-in handling.
- **Content readiness** — if the client doesn't have copy / photos, the
  project waits.
- **Approval flow** — if 3+ stakeholders, build a sign-off matrix.
- **Vendor lock-in** — proprietary tools the client requested.
- **Regional language / Unicode** — Tamil/Hindi/Marathi forms, fonts,
  SMS, WhatsApp.
- **Timeline overlap with holidays** — Diwali, Pongal, regional exams.

## 6. Phase the work

- **MVP** = the smallest version that delivers the client's stated goal.
- **Phase 2** = upgrades that earn paid extensions or upsells.
- **Later** = nice-to-have items that don't fit MVP or Phase 2.

Default rule: MVP ≤ 6 features for a small team.

## 7. Quote scope (for the proposal)

A short paragraph the salesperson can paste into a proposal:

> Scope: build a [project type] for [client], covering [must-haves].
> Out of scope: [list]. Optional add-ons: [list]. Timeline:
> [phases]. Pricing: [confirmed / placeholder]. Dependencies:
> [content delivery, stakeholder reviews, vendor onboarding].

## 8. Next reply to client (always)

Short, polite, asks 3–5 highest-leverage missing questions, ends with a
clear next step. Template:

```
Hi [Client name],

Thanks for sharing this. Before we put together a clear plan and
quote, a few quick questions:

1. [Question]
2. [Question]
3. [Question]
4. [Question]
5. [Question]

Once we have these, we'll send a proposal within [N] business days.

— [Sales / PM name], LeadUp
```

## 9. Honesty rules

- Don't invent features.
- Don't invent budgets or timelines.
- Don't translate emotion into commitment.
- Don't dismiss optional items — list them, let the client decide.
- Flag PII / regulated industry signals early.
- Use the client's actual words where possible.
- Reply with 3–5 questions, not 15.

## 10. Output to the next skill

Hand the structured doc to:
- `leadup-sales-proposal-builder` once requirements are confirmed.
- `leadup-pricing-package-planner` if packaging is the open question.
- `leadup-pii-risk-reviewer` if PII is in scope.
- `leadup-api-research-builder` if a new third-party tool is named.
- `leadup-saas-mvp-planner` if this is a new SaaS idea.
