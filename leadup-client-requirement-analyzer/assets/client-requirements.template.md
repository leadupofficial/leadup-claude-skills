# Client requirements — [Client name]

> Date: [YYYY-MM-DD]  ·  Source of input: [WhatsApp / email / PDF / voice / call notes]
> Industry: [salon / clinic / jewellery / school / SaaS / …]
> City / market: [Coimbatore / India / global]
> LeadUp role guess: [full build / redesign / fix / support / SaaS partner]

## 1. Brief (plain English)

[2–4 sentences restating the raw input. No invention.]

## 2. Client goal (in their own words)

> "[Quote, kept close to original phrasing]"

## 3. Must-have features

| # | Feature | Role | Outcome |
|---|---|---|---|
| 1 | [e.g. Online booking] | customer | book a slot without calling |
| 2 | [e.g. WhatsApp reminder] | staff | reduce no-shows |
| 3 | […] | […] | […] |

## 4. Optional / nice-to-have features

- [Item]
- [Item]
- [Item]

## 5. Out of scope

- [Item — and one-line reason: "client said no", "doesn't fit budget", "needs separate license"]
- [Item]

## 6. Missing questions (3–5)

1. [Question — one line]
2. [Question]
3. [Question]
4. [Question]
5. [Question]

## 7. Complexity per feature

| Feature | Complexity | Effort band | Risk note |
|---|---|---|---|
| [Online booking] | M | 1–3 weeks | needs payments scope |
| [WhatsApp reminder] | M | 1–3 weeks | BSP template approval lag |
| […] | […] | […] | […] |

## 8. Risks

- **Technical:** [list]
- **Legal / regulatory:** [PII, KYC, sector licence, GST]
- **Content readiness:** [logo, photos, copy]
- **Stakeholders / approvals:** [who decides, who signs]
- **Vendor / lock-in:** [payment processor, BSP, CRM]

## 9. Recommended phases

**MVP (weeks 0–N):**
- [feature]
- [feature]
- [feature]

**Phase 2 (after MVP):**
- [feature]
- [feature]

**Later or never:**
- [item]

## 10. Quote scope (for `leadup-sales-proposal-builder`)

> Scope: build a [project type] for [client], covering [must-haves].
> Out of scope: [list]. Optional add-ons: [list]. Timeline: [phases].
> Pricing: [confirmed / placeholder]. Dependencies: [content delivery,
> stakeholder reviews, vendor onboarding].

## 11. Next reply to client

```
Hi [Client name],

Thanks for sharing this. Before we put together a clear plan and quote,
a few quick questions:

1. [Top missing question]
2. [Next missing question]
3. [Next missing question]
4. [Next missing question]
5. [Next missing question]

Once we have these, we'll send a proposal within [N] business days.

— [Sales / PM name], LeadUp
```

## 12. Hand-offs

- Proposal → `leadup-sales-proposal-builder`.
- Pricing tiers → `leadup-pricing-package-planner`.
- PII / sensitive data → `leadup-pii-risk-reviewer`.
- API / vendor research → `leadup-api-research-builder`.
- New SaaS plan → `leadup-saas-mvp-planner`.
- Public copy polish → `leadup-human-content-editor` before sending.
