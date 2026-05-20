# Pricing package framework — LeadUp

How LeadUp designs Basic / Standard / Premium tiers that clients can
compare in 30 seconds without confusion.

## 1. The value ladder

Each tier must add at least one **real, named upgrade** over the previous
one. If Standard is just "Basic with more pages", the ladder is fake.

Good ladder for a website service:

| Basic | Standard | Premium |
|---|---|---|
| 5 pages, mobile-first, contact form | + WhatsApp booking flow, blog setup, basic SEO | + Admin panel, 3 months of content updates, advanced SEO + GA4 |

Good ladder for an SEO retainer:

| Basic | Standard | Premium |
|---|---|---|
| Audit + 2 pages/mo | Audit + 4 pages/mo + GSC review | Audit + 6 pages/mo + monthly call + technical SEO |

## 2. Anchors and "Most popular"

- **Basic** anchors the floor.
- **Standard** is where you want most clients to land. Mark it "Most
  popular" if and only if it actually is.
- **Premium** anchors the ceiling and increases Standard's perceived
  value.

Do not mark "Most popular" on Basic.

## 3. Pricing rules

- Don't invent. Use the user's confirmed numbers, or `[fill in]` with a
  recommended band and a confirm prompt.
- One-time vs recurring is always separate.
- Annual price = (monthly × 12) × discount band (10–20% common). State
  the discount.
- Currency stated (INR / USD / AED).
- GST shown for India (18% for IT services is the default unless
  otherwise; verify per service).
- For international: drop GST, note tax / TCS / TDS where relevant.

## 4. Includes / excludes

Per tier, list 4–8 included features. Each is concrete:

- ✅ "WhatsApp booking flow with reminders"
- ❌ "Empower seamless growth" (banned hype, vague)

Across all tiers, an **exclusions block**:

- Paid ad spend (separate from management fee).
- Hosting / domain / SSL fees.
- WhatsApp BSP fees.
- Photography / video / graphic design.
- Translation / regional language.
- Copywriting beyond X words.
- Bug fixes beyond support window.

## 5. Upsells

- One-time: SEO audit, schema setup, ad creative pack, brand kit.
- Recurring: AMC, content writing per article, ad management %, support
  hours, monitoring/observability.

Each upsell is named and priced (or `[fill in]`).

## 6. SaaS subscription specifics

- Billing period: monthly + annual (annual with stated discount).
- Fair-use limits: bookings/month, MAU, storage, integrations,
  reminders/month.
- Free tier or trial: define if used (length, what's included).
- Cancellation: when, where, refund handling.
- Refund: full / pro-rated / none — state it.
- Tax: GST in India; clarify B2B vs B2C if it matters.
- Add-ons: per-user, per-location, per-integration.

## 7. AMC / retainer specifics

- What's covered per month (hours, scope, types of tickets).
- What's NOT covered (new features, redesigns).
- Response SLA + resolution SLA.
- Working hours / time zone.
- Notice period / renewal terms.

## 8. India / global considerations

- India: ASCI compliance for marketing claims; GST; HSN/SAC; UPI; KYC
  for payment integrations; DPDP scope when finalised.
- Global: GDPR for EU users, SOC 2 path for enterprise B2B, currency
  exchange / Wise / Stripe.
- Regional language: Tamil / Hindi / Marathi packs as add-ons, not core
  inclusions.

## 9. Margin / risk notes (internal)

For every tier, write the internal version:

- Hours per month at this tier.
- Who delivers (PM / designer / developer / SEO / ops).
- Estimated cost per delivery.
- Margin band (if the user shared pricing).
- Risk lines: scope creep, third-party fee changes, refund handling,
  delivery dependency.

These notes are NEVER shown to the client.

## 10. Pricing-page copy

A short marketing block for the website:

- One-line value prop for the service.
- Three tiers in a comparison.
- "Most popular" badge on Standard if true.
- 2–3 trust signals (only real ones).
- FAQ covering the top 3 questions (cancellation, GST, what's included).
- One clear CTA per tier.

This block should pass through `leadup-human-content-editor` before
publishing.

## 11. Honesty rules

- No invented prices.
- No invented client logos, awards, or "as seen on" badges.
- No guarantee language for SEO / ads / leads / revenue.
- No fake "limited time" if it isn't.
- No hidden inclusions / exclusions.
- Refund and cancellation in plain language.
- Public copy through `leadup-human-content-editor`.
