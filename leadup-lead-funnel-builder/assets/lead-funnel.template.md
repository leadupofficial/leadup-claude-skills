# Lead funnel plan — [Business / product]

> Date: [YYYY-MM-DD]  ·  Market: [country / city]
> Goal: [calls / WhatsApp / form leads / signups / demos / bookings]
> Monthly budget: [₹ / $] [amount]

## 1. Brief restate

[One line: who, what, market, budget, funnel type.]

## 2. Funnel map

| Stage | Channel | KPI | 30-day target band | Failure mode |
|---|---|---|---|---|
| Traffic | Google + Meta + organic | sessions, CTR | [band] | wrong audience |
| Landing page | dedicated LP | click-to-form/WhatsApp | [band] | weak hook |
| Capture | form / WhatsApp | leads/day | [band] | long form |
| Qualify | sales review | hot ratio | [band] | unclear criteria |
| Follow-up | WhatsApp + email | reply rate | [band] | too few touches |
| Close | sales call | conversion | [band] | weak offer |

## 3. Traffic plan

| Source | Share | KPI | Hand-off skill |
|---|---|---|---|
| Google Search Ads | 35% | CPC, CR | `leadup-digital-ads-planner` |
| Meta (FB+IG) | 30% | CTR, CPL | `leadup-digital-ads-planner` |
| Organic SEO | 15% | rank, CTR | `leadup-seo-strategist` |
| Google Business | 10% | calls, direction taps | manual |
| Referral / lists | 10% | reply rate | `leadup-smm-growth-planner` |

## 4. Landing page spec

- Above-fold: outcome headline + sub + CTA visible on 360×640.
- Mobile-first; LCP < 2.5s.
- Form / WhatsApp toggle (whichever is primary per audience).
- 3–5 real trust signals.
- One primary CTA repeated 2–4 times.

Hand details to `leadup-landing-page-cro-planner`.

## 5. Capture flow

### Form path
- Fields: Name, Phone (+91 default). Optional: email, service.
- Validation: inline.
- Success state: "We'll WhatsApp you within 1 hour" + WhatsApp button.
- CRM event: `generate_lead` fires on submit.
- Auto-reply: WhatsApp template + email within 60 seconds.

### WhatsApp path (recommended for India local services)
- Click-to-chat link with pre-filled message.
- BSP template auto-reply within 1 minute.
- CRM event: `whatsapp_lead` on first message via BSP webhook.

### Call path (optional)
- Click-to-call.
- Call-tracking number.
- CRM event: `call_answered` on >30s duration.

## 6. Qualification

| Tier | Criteria | Routing |
|---|---|---|
| Hot | matches ICP, urgency, decision-maker | sales call within 15 min |
| Warm | matches ICP, no urgency | 5-touch nurture 14 days |
| Cold | out of ICP / freebie hunter | light nurture, then drop |

## 7. Follow-up sequence

| # | Channel | Day | Message (short draft) |
|---|---|---|---|
| 1 | WhatsApp + email | 0 (within 60s) | confirm + next step |
| 2 | WhatsApp | 1 | answer top 1 question + offer call |
| 3 | Email | 3 | real proof / case story |
| 4 | WhatsApp | 7 | "still interested?" + slot link |
| 5 | Email + WhatsApp | 14 | polite final + clear ask |

## 8. Automation

- Tool: n8n / Zapier / native CRM (pick one).
- Trigger: form submit / WhatsApp inbound / call answered.
- Nodes: capture → CRM upsert → auto-reply → assignment → schedule follow-ups.
- Credentials: placeholders `{{CRM_TOKEN}}`, `{{BSP_TOKEN}}`,
  `{{GA4_SECRET}}`.
- Error handling: retry, dead-letter to a Slack channel, manual review.

Hand to `leadup-n8n-workflow-builder` for the actual graph.

## 9. Tracking checklist

- [ ] GA4 events: `generate_lead`, `whatsapp_click`, `call_click`,
      `signup`, `purchase`.
- [ ] Meta Pixel + CAPI live.
- [ ] Google Ads tag + conversion linked.
- [ ] UTM convention defined and preserved.
- [ ] CRM stages: `lead_created`, `qualified`, `demo_booked`, `won`,
      `lost`.
- [ ] Test lead end-to-end before launch.

## 10. Conversion improvement checklist (first 30 days)

- [ ] LP LCP < 2.5s on mobile.
- [ ] Auto-reply within 60s.
- [ ] Hot leads contacted by human < 15 min.
- [ ] UTM preserved through redirects.
- [ ] One test lead pushed end-to-end.
- [ ] Sales briefed on qualification rules.
- [ ] Compliance + consent language present.
- [ ] PII flow reviewed by `leadup-pii-risk-reviewer`.

## 11. Assumptions and data confidence

- **Verified** (sourced): [list]
- **Estimated band** (CTR, CPL, CR): [list]
- **Requires verification**: [list]

## 12. Hand-offs

- LP build → `leadup-landing-page-cro-planner`.
- Ads layer → `leadup-digital-ads-planner`.
- SEO layer → `leadup-seo-strategist`.
- WhatsApp templates → `leadup-whatsapp-automation-planner`.
- Automation graph → `leadup-n8n-workflow-builder`.
- CRM/API integration → `leadup-api-research-builder`.
- Public copy polish → `leadup-human-content-editor`.
- PII / payments review → `leadup-pii-risk-reviewer`,
  `leadup-security-review`.
