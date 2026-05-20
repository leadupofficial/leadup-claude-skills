# n8n workflow framework — LeadUp

How LeadUp designs n8n workflows that stay safe in production.

## 1. One node, one job

Each node should do exactly one thing:

- Trigger (Webhook / Cron / App event).
- Validate (Function / Set with schema check).
- Transform (Set / Function).
- Call (HTTP Request / Native node — CRM / BSP / Razorpay).
- Decide (IF / Switch).
- Persist (Sheets / DB / CRM).
- Notify (Email / WhatsApp / Slack).

If a node looks like 5 jobs squeezed in, split it.

## 2. Trigger patterns

| Trigger | Use |
|---|---|
| Webhook | external system → us (form, BSP, payment) |
| Cron | scheduled job (daily report, reminder N hours before) |
| Native app event | n8n native integrations (Slack, Gmail, Sheets) |
| Inbound email | mail-to-action workflows |
| Manual | dev / ops triggered, never customer-facing |

For webhooks:

- HTTPS only.
- Auth: signed payload + secret (HMAC for Razorpay / Stripe / WhatsApp
  BSP / GitHub).
- Path: `/webhook/<source>/<event>` so logs are readable.

## 3. Credentials (never paste real keys)

- Use n8n's credential store, not inline strings.
- In docs / plans, refer to credentials as `{{n8n_creds.crm_token}}`
  or `{{N8N_CRM_TOKEN}}` placeholders.
- In self-hosted n8n on `leadup-server`, env vars come from Coolify;
  rotate per project.
- Never write a credential value into a Slack message, log, or
  exception output.

## 4. Idempotency

For any workflow that has side effects:

- Pick a **stable key** per inbound event:
  - Razorpay: `payload.payload.payment.entity.id`
  - Stripe: `event.id`
  - WhatsApp BSP: `messages[i].id`
  - Form: a deterministic hash of `(email + ts + form_id)`.
- Look the key up in a dedupe store (small Postgres table / Redis /
  even a Google Sheet for low volume).
- If seen → short-circuit; else continue and record.

## 5. Error handling

Per node:

- Retry on transient errors (5xx, network) with exponential backoff
  (e.g. 2× to 3 attempts).
- On permanent error (4xx, schema mismatch) → on-error branch.

Workflow-level:

- Dead-letter: write the failed payload (redacted PII) to a Google
  Sheet or Postgres table for manual review.
- Alert: Slack / WhatsApp notification to the team.
- Counter: increment a fail counter in observability.

## 6. Manual approval (for sensitive actions)

When the workflow does something money-moving or destructive:

- Add a **wait-for-webhook** node + a Slack message with Approve /
  Reject buttons.
- Or add an in-product approval step (the team clicks a link).
- Time-out after N minutes → cancel + alert.

Use for: refunds, mass emails, bulk WhatsApp campaigns, data
purges, large invoice runs.

## 7. PII handling in n8n

- Mask phone / email in any Slack / email notification the workflow
  fires.
- Truncate IDs in dead-letter logs.
- Don't store full payment metadata in n8n execution data (set
  workflow option to save no execution data for sensitive workflows,
  or save only on error).
- Route the workflow plan to `leadup-pii-risk-reviewer`.

## 8. Test plan (3–5 fixtures minimum)

Each fixture:

```
Name: [happy path / missing field / duplicate event / downstream 500]
Input (sample payload):
  {...}
Expected behavior:
  - branch taken
  - external calls made (mocked)
  - data persisted
  - alerts fired
```

Test in n8n's "Execute Workflow" with the sample payload before going
live.

## 9. Diagram (text form)

Format the workflow as a readable text graph:

```
[Trigger: Webhook /lead]
   ↓
[Validate input]
   ↓ (ok)
[Dedupe by submission_id]
   ↓ (new)
[CRM Upsert: contact]
   ↓
[Decide: opt-in present?]
   ├── yes → [WhatsApp BSP send]
   │           └── on error → [Dead-letter sheet]
   └── no → [Tag: needs-opt-in]
            └── [Notify sales Slack]
   ↓
[Google Sheet log row]
   ↓
[Respond 200 to webhook]
```

Arrows + branches must be unambiguous. The team should be able to
recreate the workflow in the n8n editor without questions.

## 10. Self-hosted on `leadup-server` (Coolify)

- Run in queue mode for any workflow above ~10 executions/min.
- Webhook public URL must be HTTPS via Coolify's reverse proxy.
- Persist execution data: limited days (avoid PII bloat).
- Backups: SQLite or Postgres backed up nightly.

## 11. Honesty rules

- No real secrets in docs.
- One job per node.
- Webhook signature verified.
- Idempotency key chosen.
- Retries + dead-letter defined.
- Manual approval for sensitive actions.
- PII masked in alerts / logs.
- API depth per system handed to `leadup-api-research-builder`.
- LLM nodes handed to `leadup-ai-feature-planner`.
- Sensitive scopes reviewed by `leadup-pii-risk-reviewer` /
  `leadup-security-review`.
