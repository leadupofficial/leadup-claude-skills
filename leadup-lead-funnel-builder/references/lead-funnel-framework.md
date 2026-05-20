# Lead funnel framework — LeadUp

How LeadUp designs end-to-end lead funnels. Honest about numbers,
opt-in friendly, and built for Indian SMBs + global SaaS.

## 1. Stages (every funnel)

```
Traffic → Landing page → Capture → Qualify → Follow-up → Close → Loop
```

Each stage has a **KPI**, a **channel**, and a **failure mode** to watch.

| Stage | KPI | Failure mode |
|---|---|---|
| Traffic | sessions, click-through | wrong audience |
| Landing page | form / WhatsApp click rate | weak hook, slow page |
| Capture | lead created in CRM | form too long, no auto-reply |
| Qualify | hot vs cold split | unclear criteria |
| Follow-up | reply rate, booked calls | too few touches, wrong channel |
| Close | conversion to paying / signed | weak offer, slow sales |
| Loop | referrals, reviews, repeat | no post-purchase ask |

## 2. Funnel types

Pick one (or two parallel):

- **Form funnel** — LP → form → CRM → email + WhatsApp follow-up.
- **WhatsApp funnel** — ad / LP → click-to-chat → opt-in → BSP template
  → CRM → sales.
- **Call funnel** — LP → click-to-call → CRM → sales calls back.
- **Demo funnel** — LP → calendar booking → reminder → demo call.
- **Trial / signup funnel** — LP → free signup → onboarding sequence →
  paid upgrade.

## 3. Traffic mix

Default for an Indian SMB lead-gen with ₹50K/month:

| Source | Share | Why |
|---|---|---|
| Google Search Ads | 35% | active intent buyers |
| Meta (FB+IG) | 30% | discovery + remarketing |
| Organic SEO | 15% | compounding |
| Google Business / Maps | 10% | local intent |
| Referral / WhatsApp lists | 10% | warm |

For a B2B SaaS with $1K/month, swap Meta down and LinkedIn up.

## 4. Landing page rules

- Above-fold: outcome headline + sub + visible CTA on 360×640.
- Mobile-first; LCP < 2.5s.
- Form ≤ N necessary fields (often 2 for India SMB).
- WhatsApp click-to-chat usually beats forms for local services in
  India.
- 3–5 trust signals (only real ones).
- One primary CTA, repeated 2–4 times down the page.

Hand the LP build to `leadup-landing-page-cro-planner`.

## 5. Capture flow

### Form path

- Minimum fields: name + phone (+91 default). Email only if email
  follow-up actually happens.
- Inline validation.
- Auto-reply email + WhatsApp within 60 seconds.
- CRM event fires on submit.
- Success state: "We'll WhatsApp you within 1 hour" + WhatsApp click-
  to-chat button as fallback.

### WhatsApp path

- One-tap click-to-chat (https://wa.me/91XXXXXXXXXX?text=…).
- Opt-in implicit if user initiates the chat.
- BSP template auto-reply within 1 minute with name, service, next step.
- CRM event fires when the message lands (via BSP webhook).

### Call path

- One-tap click-to-call.
- Call-tracking number (CallRail / KooKoo / KnowBe4 / DIY UTM).
- CRM event fires on call answered + duration > 30s.

Never run cold WhatsApp outreach without opt-in (Meta policy + IT Rules
risk).

## 6. Qualification

Hot vs cold criteria:

- **Hot**: matches ICP, named timeline ("this week"), budget hinted at,
  decision-maker.
- **Warm**: matches ICP, no urgency.
- **Cold**: out of ICP, freebie hunter, geography mismatch.

Route:

- Hot → human sales within 15 min.
- Warm → 5-touch nurture over 14 days, then sales call.
- Cold → light nurture (newsletter / WhatsApp broadcast opt-in), then
  drop.

## 7. Follow-up sequence (default 5-touch, 14 days)

| # | Channel | Day | Message |
|---|---|---|---|
| 1 | WhatsApp + email | 0 (within 60s) | confirmation + next step |
| 2 | WhatsApp | 1 | answer top 1 question + offer call |
| 3 | Email | 3 | proof / case story (real only) |
| 4 | WhatsApp | 7 | "still interested?" + slot link |
| 5 | Email + WhatsApp | 14 | final, polite, "what should we do" |

Each touch is short, named, action-led. No 6-paragraph emails.

## 8. Automation

Tools (in order of LeadUp preference):

- **n8n** (self-host / cloud) — most flexible, see
  `leadup-n8n-workflow-builder`.
- **Make / Zapier** — if user is already there.
- **Native CRM automation** — HubSpot / Zoho / Pipedrive.
- **Custom code** — only when n8n hits a real limit.

Credentials always as placeholders (`{{API_KEY}}`).

## 9. Tracking checklist

- GA4 events: `generate_lead`, `whatsapp_click`, `call_click`,
  `signup`, `purchase`.
- Meta Pixel + Conversion API server-side.
- Google Ads tag + conversion linked.
- UTM convention: `utm_source / medium / campaign / content / term`,
  preserved through redirects and into the CRM.
- CRM stage events: `lead_created`, `qualified`, `demo_booked`,
  `won`, `lost`.
- Phone-call tracking if call-funnel.
- Offline conversion upload if CRM doesn't fire events natively.

## 10. Conversion improvement checklist (first 30 days)

- [ ] LP under 2.5s LCP on mobile.
- [ ] Auto-reply within 60s of capture.
- [ ] Hot leads contacted by human within 15 minutes.
- [ ] Tracking validated end-to-end with a test lead.
- [ ] UTM preserved through redirects.
- [ ] Follow-up sequence tested for one real lead.
- [ ] Qualification rules documented and shared with sales.
- [ ] Compliance / consent language present (India IT Rules / GDPR if
      relevant).
- [ ] PII flow reviewed by `leadup-pii-risk-reviewer`.

## 11. Honesty rules

- No invented CR / CPL / ROAS.
- No guarantees on leads, sales, revenue.
- No cold WhatsApp without opt-in.
- No fake urgency / fake stock.
- Public copy through `leadup-human-content-editor`.
- Integrations via `leadup-api-research-builder`.
- PII / payments via `leadup-pii-risk-reviewer` and
  `leadup-security-review`.
