# WhatsApp automation plan — [Use case]

> Date: [YYYY-MM-DD]  ·  Audience: [salon / clinic / school / SaaS / …]
> Market: [city / country]  ·  Language(s): [English / Tamil / Hindi / …]
> BSP / API: [Gupshup / AiSensy / Wati / WhatsApp Cloud API / TBD]

## 1. Brief restate

[One line: what this automation does, for whom, by which trigger.]

## 2. WhatsApp category

- Category: **Utility / Marketing / Authentication / Service**
- Why this category: [one line]
- Pricing implication: [low / mid / high band — verify via
  `leadup-api-research-builder`]

## 3. Opt-in handling

- Source: [booking form / in-store signed / past customer / app event]
- Consent text shown to user (verbatim):
  > "[Plain consent line, e.g. 'By submitting, you agree to receive
  > WhatsApp updates about your booking and reminders. Reply STOP to
  > opt out anytime.']"
- Storage: `customer.consent` (text + ts + source).
- Withdrawal path: STOP keyword + in-app toggle.

## 4. Trigger

- Trigger type: [form submit / app event / time-based / inbound /
  webhook / manual]
- Trigger source: [URL / event name / cron expression]
- Pre-conditions: [opt-in on file, customer in segment X]

## 5. Message templates

### Main template — `[template_name]` (Utility, English)

```
Hi {{1}}, your booking for {{2}} on {{3}} at {{4}} is confirmed.
Reply STOP to opt out.
```

- Placeholders:
  - `{{1}}` = customer first name
  - `{{2}}` = service name
  - `{{3}}` = date (Asia/Kolkata)
  - `{{4}}` = time (24h)
- Length: [N chars]
- Approval status: [submitted / approved / rejected]

### Follow-up reminder — `[template_name_reminder]` (Utility, English)

```
Hi {{1}}, this is a reminder for your {{2}} at {{3}}. See you soon.
Reply RESCHEDULE if you need to change. Reply STOP to opt out.
```

### Tamil variant — `[template_name_ta]` (Utility, Tamil)

```
வணக்கம் {{1}}, உங்கள் {{2}} {{3}} மணிக்கு உறுதி செய்யப்பட்டது.
நிறுத்த "STOP" என்று பதிலளிக்கவும்.
```

(Each language = separate template submission.)

## 6. CRM / data fields

| Field | Action | Notes |
|---|---|---|
| `customer.phone` | read | raw in CRM; hashed in logs |
| `customer.name` | read | first name into `{{1}}` |
| `customer.consent_ts` | read | gate the send |
| `booking.service` | read | into `{{2}}` |
| `booking.slot` | read | into `{{3}}` / `{{4}}` |
| `whatsapp_log` (id, phone_hash, template, status, ts) | write | logs |
| `customer.opt_out_at` | write | on STOP |

PII routed to `leadup-pii-risk-reviewer`.

## 7. Workflow steps

```
1. Trigger fires (booking confirmed).
2. Fetch customer + booking from CRM.
3. Check opt-in on file. If missing → stop + log.
4. Render template with placeholders.
5. Send via BSP / Cloud API.
6. Log delivery status (delivered / read / failed).
7. On inbound reply:
   a. If "STOP" → mark opt_out_at; send Service ack; suppress future.
   b. If "RESCHEDULE" → route to human / reschedule flow.
   c. Else → route to human inbox.
8. On failure:
   a. Retry × 3 with backoff.
   b. Fallback channel: SMS / email.
   c. Dead-letter queue with redacted payload.
```

## 8. Failure handling

| Error code (BSP) | Action |
|---|---|
| 131026 (not on WhatsApp) | fallback SMS / email |
| 131047 (re-engagement) | refresh template / opt-in check |
| 470 (template paused) | block flow; alert team |
| 429 (rate limited) | queue + backoff |
| signature invalid | reject; alert |

## 9. Compliance caution

- Meta policy: opt-in respected; STOP honored within 24h; correct
  template category.
- India IT Rules / DPDP: consent recorded; withdrawal path; sensitive
  data minimised.
- ASCI: marketing claims disclosed where applicable.
- Sector: [clinic / finance / kids → add disclaimers].

## 10. Integration / API needs

- BSP base URL: [from BSP docs]
- Auth: Bearer `{{BSP_TOKEN}}` (in vault / Coolify env, never in repo).
- Webhook URL: `/api/webhooks/whatsapp`
- Signature verification: HMAC of body with `{{BSP_WEBHOOK_SECRET}}`.
- Events handled: `messages`, `statuses`, `template`.
- Idempotency: dedupe on `messages[i].id`.

API depth handled by `leadup-api-research-builder`.

## 11. Hand-offs

- Workflow graph + nodes → `leadup-n8n-workflow-builder`.
- BSP / Cloud API depth → `leadup-api-research-builder`.
- PII / regulated scope → `leadup-pii-risk-reviewer`.
- Template copy polish → `leadup-human-content-editor`.
- Broader funnel context → `leadup-lead-funnel-builder`.
