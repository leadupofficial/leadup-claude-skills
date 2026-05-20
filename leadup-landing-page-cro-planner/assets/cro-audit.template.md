# CRO audit — [Page URL]

> Date: [YYYY-MM-DD]  ·  Auditor: [name]
> Goal: [leads / bookings / signups / purchase / demo]
> Traffic source mix: [paid Meta / Google / SEO / mixed]
> Current CR (if known): [%]  ·  Source: [GA4 / GTM / CRM / requires verification]

## 1. Summary

- **Page:** [URL]
- **Audience / market:** [India tier-2, global SaaS buyers, …]
- **Top 3 wins (next 14 days):**
  1. […]
  2. […]
  3. […]
- **Top 3 risks:**
  1. […]
  2. […]
  3. […]

## 2. Above-the-fold

| Element | Current | Proposed |
|---|---|---|
| Headline | […] | […] |
| Sub-line | […] | […] |
| Primary CTA | […] | […] |
| Hero visual | […] | […] |
| LCP (mobile) | [s] | < 2.5s |

## 3. CTA

| Placement | Present? | Text | Mobile reach |
|---|---|---|---|
| Above the fold | […] | […] | […] |
| After value props | […] | […] | […] |
| After social proof | […] | […] | […] |
| Sticky mobile | […] | […] | […] |

## 4. Trust signals

- What's there: [list]
- What's missing: [list]
- What to add (verified only): [list]

## 5. Lead form

Current fields:

| # | Field | Required? | Keep / cut / change |
|---|---|---|---|
| 1 | […] | […] | […] |

Proposed minimal form:

| Field | Notes |
|---|---|
| Name | autocomplete=name |
| Phone | +91 default, autoformat, type=tel |
| (optional) Email | only if email follow-up matters |
| (optional) Service | dropdown, qualifies the lead |

WhatsApp click-to-chat: [Yes / No, with phone number]

## 6. Offer / pricing

- Plan clarity: [issue + fix]
- Pricing transparency: [issue + fix]
- FAQ coverage of top 3–5 objections: [present / missing]
- Refund / cancellation visibility: [present / missing]

## 7. Mobile

- Above-the-fold visible at 360×640: [yes / no]
- Sticky CTA: [present / missing]
- Font ≥ 16px: [yes / no]
- Tap targets ≥ 48px: [yes / no]
- Form keyboard types: [tel / email / numeric set?]
- WhatsApp button: [present / missing]
- Horizontal scroll: [no / found in: …]

## 8. Performance (mobile)

| Metric | Value | Status |
|---|---|---|
| LCP | [s] | […] |
| INP | [ms] | […] |
| CLS | [score] | […] |

Top 3 perf fixes:
1. […]
2. […]
3. […]

## 9. A/B test plan (4–8 tests)

| # | Hypothesis | Variant | Primary metric | Expected lift | Effort | Min traffic |
|---|---|---|---|---|---|---|
| 1 | Outcome headline > generic | new headline | CR | med | S | 1k visits |
| 2 | Cut form to 2 fields | 2-field form | CR | high | S | 1k visits |
| 3 | WhatsApp as primary CTA (India) | swap CTA | CR | high | S | 1k visits |
| 4 | Sticky mobile CTA | add sticky | CR | med | S | 500 visits |
| 5 | Social proof above pricing | reorder | CR | med | S | 1k visits |
| 6 | Real customer hero vs stock | swap hero | CR | med | M | 1k visits |

If user traffic < 1k/month: skip A/B; ship a single prioritized rebuild.

## 10. Conversion checklist

(See `references/cro-framework.md` for the full 25–40 item list; tick
each here.)

- [ ] Headline names audience + outcome in ≤ 12 words.
- [ ] Sub-line states one-line proof.
- [ ] Primary CTA visible above fold on 360×640.
- [ ] CTA repeated 2–4 times.
- [ ] Mobile sticky CTA present.
- [ ] LCP < 2.5s mobile.
- [ ] CLS < 0.1.
- [ ] Form: minimum necessary fields.
- [ ] Phone field +91 default (India).
- [ ] WhatsApp click-to-chat present (India).
- [ ] Pricing visible if applicable; FAQ in place.
- [ ] No dark patterns.
- [ ] GA4 conversion event fires on submit.
- [ ] UTM preserved through redirects.
- [ ] Mobile font ≥ 16px; tap targets ≥ 48px.
- [ ] Success state clear.
- [ ] Refund / cancellation terms visible.
- [ ] Legal / GST footer (if invoicing).
- [ ] Consent / cookie respects user choice.
- [ ] Heatmap / session recording installed.
- [ ] No render-blocking 3rd-party scripts.
- [ ] Images compressed + sized.
- [ ] Page works on 3G / slow networks.
- [ ] 404 / error states tested.
- [ ] Accessibility: alt text, contrast, focus states.

## 11. Assumptions and data confidence

- **Verified** (analytics / Lighthouse / heatmap): [list]
- **Estimated band**: [list]
- **Requires verification**: [list]

## 12. Hand-offs

- Premium visual redesign → `leadup-premium-ui-upgrader`.
- Rewritten public copy → `leadup-human-content-editor`.
- Tracking / CAPI / server-side → `leadup-api-research-builder`.
- Ads context → `leadup-digital-ads-planner`.
