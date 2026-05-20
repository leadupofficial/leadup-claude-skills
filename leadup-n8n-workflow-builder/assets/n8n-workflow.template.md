# n8n workflow plan — [Workflow name]

> Date: [YYYY-MM-DD]  ·  Environment: [cloud n8n / self-hosted on leadup-server]
> Volume: [N executions/day]  ·  SLA: [must-not-miss / can-retry / fire-and-forget]

## 1. Brief restate

[One line: outcome, trigger, systems.]

## 2. Trigger

- Type: [Webhook / Cron / App event / Inbound email / Manual]
- Path / URL: `/webhook/<source>/<event>` (HTTPS, signed)
- Schedule (if cron): `0 9 * * *` (example)
- Sample payload:
  ```json
  { "id": "evt_123", "type": "payment.captured", "data": { ... } }
  ```

## 3. Data shape

Input schema (key fields):

| Field | Type | Notes |
|---|---|---|
| id | string | event id; idempotency key |
| type | string | event type |
| customer.phone | string (E.164) | redact in logs |
| customer.email | string | redact in logs |
| amount_paise | number | INR amount (×100) |

Output: written to CRM + Google Sheet log + WhatsApp BSP send.

Canonical normalisation in early "Set" / "Function" node.

## 4. Nodes (ordered)

| # | Node name | Type | Purpose | Input | Output |
|---|---|---|---|---|---|
| 1 | Trigger | Webhook (POST) | receive event | external HTTP | parsed body |
| 2 | Verify signature | Function | HMAC check | body + secret | ok / fail |
| 3 | Dedupe | Postgres / Sheets | check `id` seen? | id | new / dup |
| 4 | Normalize | Set | canonical shape | raw | normalized |
| 5 | CRM Upsert | HTTP Request | upsert contact | normalized | crm_id |
| 6 | Branch: opt-in? | IF | gate WhatsApp | crm record | yes / no |
| 7 | WhatsApp send | HTTP Request (BSP) | send template | template + vars | msg_id |
| 8 | Sheet log | Google Sheets | append log row | redacted summary | row_id |
| 9 | Notify Slack | Slack | success / fail summary | run summary | n/a |
| 10 | Respond | Respond to Webhook | 200 OK | n/a | HTTP 200 |

Each node = one job. No mega-nodes.

## 5. Credentials

| Placeholder | Stored where | Notes |
|---|---|---|
| `{{n8n_creds.bsp_token}}` | n8n credential store | Bearer for BSP |
| `{{n8n_creds.bsp_webhook_secret}}` | n8n credentials | HMAC for inbound verification |
| `{{n8n_creds.crm_token}}` | n8n credentials | CRM API key |
| `{{n8n_creds.sheets_oauth}}` | n8n credentials | Google OAuth |
| `{{n8n_creds.slack_bot}}` | n8n credentials | Slack bot token |

No raw values in this doc or in node fields.

## 6. Error handling

- Per node retries: 3× exponential backoff for 5xx and network errors.
- On-error branch: writes redacted payload to `dead_letter` Google
  Sheet + Slack alert.
- Idempotency: dedupe table on `(id)` before any side-effect node.
- Webhook signature mismatch: reject 401, log + alert.
- Rate limits: backoff + retry up to N; then dead-letter.

## 7. Manual approval points

| Action | Approval | Channel |
|---|---|---|
| Refund > [amount] | yes | Slack approve/reject button |
| Bulk WhatsApp campaign | yes | in-product approval link |
| Data purge | yes | Slack with named approver |

Time-out: cancel after N minutes + alert.

## 8. Test plan

| # | Fixture name | Input | Expected |
|---|---|---|---|
| 1 | happy path | payment.captured payload | CRM upsert, opt-in yes, WhatsApp sent, sheet logged, 200 |
| 2 | duplicate event | same id replayed | dedupe short-circuits, 200, no double send |
| 3 | bad signature | tampered body | 401, no downstream calls |
| 4 | downstream 500 | BSP returns 500 | retry × 3, dead-letter, Slack alert |
| 5 | opt-in missing | normalized has consent=false | tag + sales Slack; no WhatsApp |

## 9. Workflow diagram (text)

```
[Trigger: Webhook /webhook/razorpay/payment]
   ↓
[Verify signature (HMAC)]
   ↓ ok
[Dedupe by event id]
   ↓ new
[Normalize payload]
   ↓
[CRM Upsert]
   ↓
[Decide: opt-in present?]
   ├── yes → [WhatsApp BSP send]
   │           ├── ok → [Sheet log] → [Notify Slack: ok] → [Respond 200]
   │           └── error → [Dead-letter sheet] → [Notify Slack: alert] → [Respond 200]
   └── no  → [Tag: needs-opt-in] → [Notify sales Slack] → [Respond 200]
```

## 10. Hand-offs

- API depth per system → `leadup-api-research-builder`.
- WhatsApp template + opt-in → `leadup-whatsapp-automation-planner`.
- LLM node inside the workflow → `leadup-ai-feature-planner`.
- PII / sensitive scope → `leadup-pii-risk-reviewer`.
- Payments / refunds → `leadup-security-review`.
- Record this automation in project memory → `leadup-status-updater`.
