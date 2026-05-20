---
name: leadup-whatsapp-automation-planner
description: Plan compliant WhatsApp Business automation for Indian small businesses and global LeadUp clients — reminders, follow-ups, lead capture, payment reminders, appointment reminders, campaigns, and order updates. Outputs automation goal, trigger, message templates, opt-in handling, CRM fields, workflow steps, failure handling, compliance caution, and integration/API needs. Use when the user says "WhatsApp automation", "WhatsApp reminder", "WhatsApp campaign", "customer follow-up", "payment reminder", or "appointment reminder".
---

# LeadUp WhatsApp Automation Planner

## Purpose

Design a WhatsApp Business automation that LeadUp can actually launch:
opt-in respecting, BSP-approval ready, integrated with a CRM or app, and
honest about Meta policy + India IT Rules. Tuned for salon / clinic /
school / jewellery / SaaS use cases.

## When to use

Use when the user wants a WhatsApp flow planned. Do **not** trigger for
the full lead funnel (use `leadup-lead-funnel-builder`), the n8n graph
build (use `leadup-n8n-workflow-builder`), or paid ads to WhatsApp
(use `leadup-digital-ads-planner`).

Trigger phrases: "WhatsApp automation", "WhatsApp reminder", "WhatsApp
campaign", "customer follow-up", "payment reminder", "appointment
reminder", "BSP template", "WhatsApp flow".

## Inputs needed

- Business + audience (industry, city, language).
- Use case (reminder / follow-up / campaign / order / payment / OTP).
- Volume estimate (messages per day).
- Customer opt-in source (form, website, in-store, prior consent).
- Existing tools (CRM, BSP account: Gupshup / AiSensy / Wati /
  WhatsApp Cloud API / other).
- Languages required (English / Tamil / Hindi / regional).

Ask at most 2 clarifying questions if use case or opt-in source is
unclear.

## Tools/resources to use

- `references/whatsapp-automation-framework.md` — opt-in, templates,
  category rules, integration patterns.
- `assets/whatsapp-automation.template.md` — output shape.
- `leadup-api-research-builder` — for the chosen BSP / WhatsApp Cloud
  API depth.
- `leadup-n8n-workflow-builder` — to actually wire the workflow.
- `leadup-lead-funnel-builder` — for the broader funnel context.
- `leadup-pii-risk-reviewer` — mandatory for customer-data flows.
- `leadup-human-content-editor` — for human-tone template copy.

## Step-by-step workflow

1. **Restate** the automation goal in one line.
2. **Pick the WhatsApp category** (Utility / Marketing / Authentication
   / Service). This determines pricing + template rules.
3. **Confirm opt-in** source and consent record (where, when, how
   stored).
4. **Design the trigger**: form submit / app event / time-based cron /
   user message / external webhook.
5. **Draft message templates**: 1 main + 1–2 follow-up + 1 quick reply
   variant. Each within Meta's template language rules; placeholders
   typed.
6. **CRM / data fields**: what the automation reads / writes, where
   PII lives.
7. **Workflow steps**: ordered list (trigger → check opt-in → render →
   send → log → branch on user reply).
8. **Failure handling**: BSP error codes, retries, fallback to SMS or
   email, dead-letter logging.
9. **Compliance caution**: Meta policy (no cold marketing without
   opt-in, no banned categories), India IT Rules (consent, DLT only if
   SMS gateway, ASCI for marketing claims), DPDP scope when in force.
10. **Integration / API needs**: BSP endpoints, webhooks, signed
    payloads, credential placeholders.

## Required output format

One Markdown plan with these sections, in this order:

1. **Brief restate** — business, use case, audience, language.
2. **WhatsApp category** — Utility / Marketing / Authentication /
   Service + pricing implication.
3. **Opt-in handling** — source, consent text, storage, withdrawal
   path.
4. **Trigger** — what starts the flow.
5. **Message templates** — main + follow-ups, with `{{vars}}` typed and
   character counts.
6. **CRM / data fields** — read / write list, PII flagged.
7. **Workflow steps** — ordered list with branches.
8. **Failure handling** — errors, retries, fallback channel, logging.
9. **Compliance caution** — Meta policy, IT Rules, ASCI, DPDP, sector-
   specific.
10. **Integration / API needs** — endpoints, credentials placeholders,
    webhook signature verification.
11. **Hand-offs** — `leadup-n8n-workflow-builder`,
    `leadup-api-research-builder`, `leadup-pii-risk-reviewer`,
    `leadup-human-content-editor`.

## Safety rules

- Do **not** propose cold WhatsApp outreach without explicit opt-in
  (Meta policy + IT Rules risk → account ban).
- Do **not** put real customer numbers in examples; use placeholders.
- Do **not** invent BSP pricing; cite the BSP's docs in
  `leadup-api-research-builder`.
- Do **not** use Marketing templates where Utility is the right
  category (cheaper + safer).
- Do **not** mix authentication content (OTP) into utility / marketing
  templates.
- Respect opt-out / STOP: any "stop" / "unsubscribe" / specific local
  language equivalents must be honored within 24h.
- Keep template language plain; pass copy through
  `leadup-human-content-editor`.
- Avoid banned content categories (gambling, alcohol, weapons,
  dating-explicit, certain financial content).
- For regulated industries (clinic, finance, kids), add disclaimers
  and route to `leadup-pii-risk-reviewer`.
- Webhook payloads must verify signature; do not log raw PII.

## Common mistakes

- Mass-cold WhatsApp blasts → account suspension.
- Marketing template categorized as Utility → Meta rejection / fine.
- No opt-in record → can't prove consent later.
- Template with hard-coded customer name in body → re-approval needed
  for variations.
- Forgetting language localization at template-approval time.
- Logging raw phone + message body in plaintext.
- No fallback to email / SMS when WhatsApp delivery fails.
- Forgetting the STOP / unsubscribe handler.

## Troubleshooting

- **No BSP account yet**: route to `leadup-api-research-builder` to
  pick (Gupshup / AiSensy / Wati / WhatsApp Cloud API) based on
  volume, region, pricing, ease.
- **Template approval delays**: factor 3–7 days; ship the rest of the
  automation behind a feature flag until approved.
- **Hindi / Tamil templates**: submit separately; do not auto-translate
  English template body at runtime.
- **Regulated industry**: tighter wording; review with
  `leadup-pii-risk-reviewer`; add disclaimers.
- **High volume (10k+/day)**: model BSP costs; consider WhatsApp Cloud
  API direct; add rate-limit + queue.
- **User wants a marketing campaign right away**: confirm opt-in
  source first; if none, reframe to opt-in-collection flow.

## Test prompts

### Should trigger (5)
1. "Plan WhatsApp appointment reminders for a dental clinic."
2. "WhatsApp follow-up for our lead form on the salon site."
3. "Build a WhatsApp campaign for Diwali offer (existing customers)."
4. "Payment reminder automation for our SaaS unpaid invoices."
5. "Order update flow on WhatsApp for our jewellery client."

### Should NOT trigger (3)
1. "Build the n8n graph for this flow." (→ `leadup-n8n-workflow-builder`)
2. "Plan the whole lead funnel." (→ `leadup-lead-funnel-builder`)
3. "Compare BSP APIs." (→ `leadup-api-research-builder`)

### Functional test cases (2)
1. Given "salon booking confirmation + reminder in Coimbatore,
   English + Tamil", return a plan categorising both templates as
   Utility, opt-in via the booking form, placeholders typed, workflow
   steps including opt-in check + fallback to SMS, compliance notes
   on India IT Rules, and a hand-off to `leadup-n8n-workflow-builder`.
2. Given "Diwali offer broadcast to past customers" with no recorded
   opt-in, return a plan that refuses to propose a cold broadcast,
   reframes to an opt-in collection flow first, and explains the
   Meta-policy and IT-Rules risk in plain language.

## Success criteria

- All 11 sections present in order.
- Opt-in record source named and storage location specified.
- Template category set correctly (Utility / Marketing / Auth /
  Service).
- Templates use typed placeholders and respect character limits.
- Fallback channel defined.
- STOP / unsubscribe handler in workflow.
- Webhook signature verification required.
- No real PII in examples.
- Hand-offs to `leadup-n8n-workflow-builder`,
  `leadup-api-research-builder`, `leadup-pii-risk-reviewer`,
  `leadup-human-content-editor` explicit.
