# CRO framework — LeadUp

Practical landing-page CRO for LeadUp client and SaaS pages. Honest about
data, light on dark patterns, mobile-first because most India traffic is.

## 1. Above the fold

Five things must be true within 3 seconds:

1. The visitor knows **what this is** (product / service).
2. The visitor knows **who it's for**.
3. The visitor knows **what changes after** (outcome).
4. The visitor sees the **primary CTA** without scrolling.
5. The page **renders fast** (LCP < 2.5s on mobile).

Headline: outcome + audience. Sub: one-line proof or how. CTA: verb +
specific.

Hero visual: relevant to the outcome (real product / real customer), not
generic stock.

## 2. CTA

Repeat the primary CTA 2–4 times down the page:

- Above the fold.
- After the value props block.
- After the social proof block.
- Sticky on mobile (bottom bar).

CTA text rules:
- Verb + outcome ("Book a free site visit", "Get a quote in 24 hours").
- Avoid "Submit" / "Learn more" unless it's a real reason.
- Mobile tap target ≥ 48px.

## 3. Trust signals

Order of impact for most LeadUp categories:

1. Real customer reviews (named + photo or logo).
2. Specific outcomes / numbers (only if real — never invent).
3. Trusted logos (brands you've worked with, with permission).
4. Press / awards (if real and verifiable).
5. Security / compliance badges (where they matter: payments, SaaS).
6. Founder / team (face + credentials for service businesses).

Do not stack 12 badges. Pick 3–5 strongest.

Do not invent reviews, logos, awards, or "as seen on" placements.

## 4. Lead form

Cut to what's necessary. Default LeadUp pattern for India SMB lead-gen:

| Field | Keep? |
|---|---|
| Name | Yes |
| Phone | Yes (with +91 default, autoformat) |
| Email | Only if email follow-up matters |
| Service / requirement | Maybe (dropdown, not free text, if it qualifies) |
| Date/time | Only if booking |
| Address / city | Only if local service |

Best practice:
- One field per line on mobile.
- Country code default.
- Autocomplete attributes set (`autocomplete="name tel email"`).
- Inline validation, not after submit.
- Clear success state ("We'll WhatsApp you within 1 hour.").

For India, **WhatsApp click-to-chat** often outperforms a form. Add it
as the primary or secondary CTA.

## 5. Offer / pricing

If pricing is shown:
- Plan names a normal person can remember.
- Real numbers, not "Contact for pricing" unless absolutely required.
- Compare 2–3 plans, no more (decision fatigue at 4+).
- Highlight one plan as "Most popular" only if it's true.
- FAQ that answers the 3–5 things buyers ask sales most.
- Refund / cancellation terms visible (don't bury them).

If offer-driven (limited time, festival, etc.):
- Real countdown only.
- Real stock indicators only.
- Clear T&C link.

## 6. Mobile

Most India web traffic is mobile. Checks:

- Above-the-fold visible at 360×640.
- Sticky CTA on bottom that doesn't cover form fields when keyboard is up.
- Form inputs trigger the right keyboard (`type="tel"`, `type="email"`,
  `inputmode="numeric"`).
- Tap targets ≥ 48px, with ≥ 8px spacing.
- Font ≥ 16px to prevent iOS auto-zoom on focus.
- No horizontal scroll.
- WhatsApp button visible and tap-able.

## 7. Performance

Core Web Vitals targets (mobile):

| Metric | Good | Action if not |
|---|---|---|
| LCP | < 2.5s | optimize hero image, preload, SSR |
| INP | < 200ms | reduce JS, split heavy handlers |
| CLS | < 0.1 | reserve image dimensions, font swap |

Image tactics:
- WebP/AVIF, width/height set, `loading="lazy"` below fold.
- Hero image preloaded.
- No 4MB jpegs.

Third-party tax:
- Audit every script in `<head>`.
- Defer or remove what isn't needed for first paint.

## 8. A/B test ideas (4–8 per audit)

Each test entry:

```
Hypothesis: [why we believe X will lift Y]
Variant A (control): [current state]
Variant B (test): [the change]
Primary metric: [CR on the goal]
Guardrail: [no drop in bounce or form-fill quality]
Expected lift band: [low / med / high; cite reasoning]
Effort: [S / M / L]
Min traffic to call winner: [estimate; flag if user lacks volume]
```

Common testable items in order of usual lift:
1. Above-the-fold headline.
2. Primary CTA copy.
3. Form field reduction.
4. Social proof block position.
5. Pricing presentation.
6. WhatsApp vs form as primary CTA (India).
7. Mobile sticky bar variants.
8. Hero visual (real customer vs product shot vs founder).

If the user has < 1K visits / month: skip A/B and ship one prioritized
rebuild instead.

## 9. Conversion checklist (25–40 items)

Run as a pre-launch gate. Sample:

- [ ] Headline names audience + outcome in ≤ 12 words.
- [ ] Sub-line states one-line proof.
- [ ] Primary CTA visible above fold on 360×640.
- [ ] CTA repeated 2–4 times down the page.
- [ ] Mobile sticky CTA present.
- [ ] LCP < 2.5s on mobile (Lighthouse / PSI).
- [ ] CLS < 0.1.
- [ ] Trust signals: real, ≤ 5 strongest.
- [ ] Form: ≤ N fields where N matches the offer.
- [ ] Phone field defaults to +91 (India) or detected country.
- [ ] WhatsApp click-to-chat present (India).
- [ ] Pricing visible if applicable; FAQ covers top 3–5 objections.
- [ ] Refund / cancellation terms visible (not buried).
- [ ] GA4 conversion event fires on submit.
- [ ] UTM parameters preserved through redirects.
- [ ] No fake urgency / fake stock / dark patterns.
- [ ] Mobile font ≥ 16px.
- [ ] Tap targets ≥ 48px.
- [ ] Form keyboard types correct.
- [ ] Success state clear and on-brand.
- [ ] 404 / error states handled gracefully.
- [ ] Page works with JS disabled or slow networks.
- [ ] Consent / cookie notice respects user choice.
- [ ] GST / legal footer if invoicing (India).
- [ ] Analytics + heatmap tagging confirmed.

## 10. Output rules

- Every metric labelled **verified** / **estimated** / **requires
  verification**.
- A/B test plan feasible at the user's stated traffic level.
- Mobile section is not optional.
- Rewritten copy passes through `leadup-human-content-editor`.
- Tracking integration handed to `leadup-api-research-builder`.
- Visual / premium UI redesign handed to `leadup-premium-ui-upgrader`.
