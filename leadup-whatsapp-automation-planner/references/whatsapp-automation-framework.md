# WhatsApp automation framework — LeadUp

How LeadUp designs WhatsApp Business automations that ship, get
approved, and don't get the BSP / WhatsApp Cloud API account banned.

## 1. Template categories (pick correctly)

| Category | Use |
|---|---|
| Utility | transactional confirmations, reminders, alerts (cheapest, fastest approval) |
| Marketing | promotional content, offers, campaigns (highest scrutiny, opt-in mandatory) |
| Authentication | OTPs only (strict format) |
| Service | reply to a user-initiated thread within 24h (no template needed) |

Most LeadUp use cases are **Utility** (booking confirmations,
reminders, order updates, payment reminders). Mis-categorising as
Marketing increases cost; mis-categorising Marketing as Utility risks
template ban.

## 2. Opt-in (non-negotiable)

Sources LeadUp can use:

- Web form / booking form with a tick-box and clear copy.
- In-store written / signed consent.
- Existing customer relationship (within scope of the original
  service) — but Meta + India guidance is stricter than people think;
  document the basis.
- User-initiated message in last 24h (Service window, no template
  needed).

Consent record stores:
- Phone number.
- Timestamp.
- Source URL or in-store signed form ID.
- Consent text shown verbatim.
- Withdrawal path (STOP keyword, link, in-app toggle).

## 3. Template language rules

Each template body:

- Plain language. No banned hype.
- Placeholders typed: `{{1}}` to `{{N}}` in order; example values
  supplied during submission.
- One language per template. Translations submitted as separate
  templates.
- Character limits per WhatsApp policy.
- No URLs that look spammy; use the business's official domain.
- No promotional content inside a Utility template.

Pass copy through `leadup-human-content-editor` so it reads human, not
AI-templated.

## 4. Trigger types

| Trigger | When |
|---|---|
| Form submit | website lead form, booking |
| App event | new order, status change, payment captured |
| Time-based | reminder N hours before appointment |
| Inbound message | user-initiated reply (no template needed within 24h) |
| External webhook | CRM, Razorpay, BSP delivery report |
| Manual | sales team triggers from CRM |

## 5. Workflow shape (default)

```
Trigger
  → fetch customer record
  → check opt-in on file (else stop + log)
  → render template variables
  → send via BSP / Cloud API
  → log delivery (delivered / read / failed)
  → on user reply: route to handler / human inbox
  → on failure: retry (≤3) → fallback channel (SMS / email)
  → branch on user choice (confirm / reschedule / STOP)
```

Always include a STOP handler that:
- Marks the customer opt-out in CRM.
- Acknowledges with a final WhatsApp Service message within 24h.
- Suppresses future templates immediately.

## 6. CRM / data fields

For each automation, list:

- Reads: `customer.phone`, `customer.name`, `booking.slot`,
  `booking.id`, etc.
- Writes: `whatsapp_log` (id, phone hash, template, status, ts),
  `customer.last_whatsapp_at`, `customer.opt_out_at` (if applicable).
- PII fields routed to `leadup-pii-risk-reviewer`.

Default redactions in logs:
- Phone stored hashed in logs; raw phone only in CRM.
- Message body not logged in plaintext for sensitive flows; store
  template id + variables hash.

## 7. Failure handling

| Error | Action |
|---|---|
| Template rejected by Meta | block flow; alert team; resubmit |
| User not on WhatsApp | fallback to SMS / email |
| Phone unreachable | retry × 3 with backoff; then fallback |
| Webhook signature invalid | reject; alert |
| Rate limit hit | queue + backoff |
| Opt-out registered | suppress permanently; only send a final ack |

Dead-letter queue: log failed messages with redacted payload for
manual review.

## 8. Compliance caution

### Meta policy (global)
- No promotional outreach without opt-in.
- No banned categories (alcohol, weapons, tobacco, adult, gambling,
  drugs, certain financial categories).
- Honor STOP / unsubscribe.
- Templates must reflect approved content; runtime variable injection
  cannot smuggle promotional content into Utility.

### India IT Rules + DPDP
- Consent + purpose documented.
- Withdrawal path easy.
- Sensitive personal data (health, finance, biometric) needs explicit
  consent.
- For broadcasts: DLT registration applies for SMS gateways (not
  WhatsApp), but ASCI guidelines apply to influencer-style claims.

### ASCI guidelines (India advertising)
- Disclosures for paid promotions / brand collaborations.
- No misleading claims.

For regulated categories (clinic, finance, real estate, kids), add
disclaimers and route to `leadup-pii-risk-reviewer`.

## 9. Integration / API patterns

BSP / Cloud API basics:

- HTTPS only.
- Bearer token in `Authorization` header (placeholder
  `{{BSP_TOKEN}}`).
- Webhook signature: verify HMAC over body before processing.
- Idempotency: dedupe on `(message_id)` to avoid double-processing.
- Webhook events: `messages` (inbound), `statuses` (delivery
  reports), `template` (status changes).

Cite the chosen BSP's API depth via `leadup-api-research-builder`.

## 10. Pricing model (high-level)

WhatsApp moved to per-template-conversation pricing (Meta charges by
template category, opened by template, valid for 24h). Bands vary by
country.

For India (verify in `leadup-api-research-builder` against the latest
BSP price sheet):

| Category | Band per conversation |
|---|---|
| Utility | low |
| Marketing | high |
| Authentication | low-mid |
| Service (user-initiated) | free within 24h window |

Always cap monthly cost in the automation plan; switch heavy flows to
Utility templates where possible.

## 11. Honesty rules

- Opt-in recorded or no broadcast.
- Correct category or no submission.
- Fallback channel defined.
- STOP handler implemented.
- Webhook signature verified.
- No raw PII in logs.
- Copy through `leadup-human-content-editor`.
- BSP API depth via `leadup-api-research-builder`.
- Workflow graph by `leadup-n8n-workflow-builder`.
- PII / regulated scope reviewed by `leadup-pii-risk-reviewer`.
