---
name: leadup-n8n-workflow-builder
description: Plan an n8n workflow for a LeadUp business or client — connecting webhooks, APIs, CRMs, WhatsApp BSPs, Google Sheets, email, payment events, and AI calls into a clear graph with triggers, nodes, data mapping, credential placeholders, error handling, manual approval points, a test plan, and a text-form workflow diagram. Use when the user says "n8n workflow", "automation workflow", "build workflow", "webhook automation", "connect APIs", or "workflow builder".
---

# LeadUp n8n Workflow Builder

## Purpose

Design an n8n workflow LeadUp can paste into the editor: trigger,
nodes, data mapping, credentials (as placeholders), error handling,
manual approval points, and a test plan. Output works for cloud n8n or
self-hosted on `leadup-server`.

## When to use

Use when the user wants an n8n graph designed. Do **not** trigger for
the WhatsApp template / opt-in design only (use
`leadup-whatsapp-automation-planner`), AI feature design (use
`leadup-ai-feature-planner`), or the broader funnel (use
`leadup-lead-funnel-builder`).

Trigger phrases: "n8n workflow", "automation workflow", "build
workflow", "webhook automation", "connect APIs", "workflow builder",
"n8n graph", "automate this".

## Inputs needed

- Business outcome the workflow drives (lead capture, reminder send,
  CRM sync, invoice creation, AI-summary on event, etc.).
- Trigger source (webhook / cron / inbound email / app event / manual).
- Systems involved (CRM, BSP, Razorpay, Google Sheets, Stripe, Slack,
  Anthropic API, OpenAI, n8n itself).
- Data shape (what comes in, what goes out, what must be validated).
- Volume / rate expectations.
- Failure tolerance (must-not-miss / can-retry / fire-and-forget).
- Approval requirement (human in the loop?).

Ask at most 2 clarifying questions if the trigger or systems are
unclear.

## Tools/resources to use

- `references/n8n-workflow-framework.md` — node patterns, error
  handling, credential rules.
- `assets/n8n-workflow.template.md` — output shape (workflow as text
  graph).
- `leadup-api-research-builder` — for each external API.
- `leadup-whatsapp-automation-planner` — for the WhatsApp side.
- `leadup-ai-feature-planner` — if an LLM call lives inside the
  workflow.
- `leadup-pii-risk-reviewer` — if customer data passes through.
- `leadup-security-review` — for payments / sensitive scopes.
- `leadup-status-updater` — to record the new automation in project
  memory.

## Step-by-step workflow

1. **Restate** the workflow outcome in one line.
2. **Pick the trigger** (webhook URL pattern / cron / event / inbound).
3. **Map data shape** end-to-end: input → transforms → outputs.
4. **Plan nodes** in order; one job per node.
5. **Credentials**: list each required credential with a placeholder
   (`{{n8n_creds.crm_token}}`); never paste real values.
6. **Error handling**: per-node retries, on-error branch (Slack alert,
   dead-letter Google Sheet), idempotency keys.
7. **Manual approval point**: add a wait-for-webhook / approval step
   for sensitive actions (refund, mass email, destructive).
8. **Test plan**: 3–5 input fixtures + expected outputs.
9. **Workflow diagram (text)**: a clear textual flow the team can
   recreate in the n8n editor without ambiguity.

## Required output format

One Markdown plan with these sections, in this order:

1. **Brief restate** — outcome, trigger, systems.
2. **Trigger** — type, URL pattern (if webhook), schedule (if cron),
   sample payload.
3. **Data shape** — input JSON schema, key transforms, output schema.
4. **Nodes (ordered)** — list with name · type · purpose · input ·
   output.
5. **Credentials** — list with placeholder name and where the secret
   lives (vault / env / n8n credentials store).
6. **Error handling** — per-node + workflow-level (alerts, dead-letter,
   idempotency).
7. **Manual approval points** — where + who + via what channel.
8. **Test plan** — fixtures with expected outputs.
9. **Workflow diagram (text)** — ASCII/Markdown graph the team can
   recreate.
10. **Hand-offs** — to other LeadUp skills.

## Safety rules

- Do **not** paste real API keys, tokens, webhooks, or customer data.
  Use placeholders.
- Do **not** log full PII in n8n executions. Mask phone / email /
  payment fields; truncate IDs.
- For payment-changing nodes (Razorpay refund, Stripe charge), add a
  manual approval step or restrict to a verified caller.
- Webhook endpoints must verify signature where the source supports it
  (Razorpay HMAC, Stripe signature, WhatsApp BSP signature, GitHub
  X-Hub-Signature).
- Idempotency: dedupe on a stable key (event id, message id) before
  side-effect nodes.
- Retries with backoff for transient errors; dead-letter for permanent.
- For India: respect IT Rules / DPDP scope on customer data; document
  consent gate where relevant.
- Defer LLM API specifics to `leadup-api-research-builder` and
  `leadup-ai-feature-planner`.

## Common mistakes

- One node doing 5 jobs — hard to debug.
- No idempotency → duplicate side effects on retries.
- Real secrets pasted into "HTTP Request" node URL.
- No error branch → silent failures.
- No retry policy → flaky third-party kills the workflow.
- Manual triggers used in prod for time-sensitive flows.
- No test fixtures → "it worked once" is the only proof.
- Workflows that hit rate limits without backoff.

## Troubleshooting

- **Self-hosted n8n on `leadup-server`**: confirm container resources,
  webhook public URL via Coolify, queue mode for high volume.
- **Cloud n8n**: confirm execution data retention + plan limits.
- **High volume**: switch to queue mode, batch nodes, or off-load to
  a dedicated worker.
- **AI inside workflow**: cap token use per execution; cache by input
  hash; route through `leadup-ai-feature-planner` for cost ledger.
- **Cross-system data shape mismatch**: add a "Set" / "Function" node
  early to normalize; document the canonical shape.
- **Manual approval needed sometimes only**: use a router (if condition
  → approval; else → continue).

## Test prompts

### Should trigger (5)
1. "Build an n8n workflow that captures lead form → CRM → WhatsApp follow-up."
2. "Automate Razorpay payment webhook → invoice → email."
3. "n8n graph: Google Sheet new row → AI summary → Slack."
4. "Workflow to sync new bookings to Google Sheets every hour."
5. "Connect our CRM to WhatsApp BSP via n8n."

### Should NOT trigger (3)
1. "Design the WhatsApp template + opt-in." (→ `leadup-whatsapp-automation-planner`)
2. "Plan the AI feature itself." (→ `leadup-ai-feature-planner`)
3. "Research the Razorpay webhook docs." (→ `leadup-api-research-builder`)

### Functional test cases (2)
1. Given "lead form on website → CRM upsert → WhatsApp Utility
   template → Google Sheet log", return an ordered node list,
   credential placeholders, signature-verified webhook trigger,
   idempotency key on submission id, retry + dead-letter on
   downstream failures, fixtures with expected outputs, and a text
   workflow diagram.
2. Given "Razorpay payment webhook → refund a payment under
   conditions", return a plan with HMAC signature verification,
   manual-approval node for any refund, audit-log node, and a
   hand-off to `leadup-security-review` and `leadup-pii-risk-reviewer`.

## Success criteria

- All 10 sections present in order.
- Nodes are atomic (one job each).
- All credentials are placeholders.
- Webhook signature verification specified.
- Idempotency key chosen.
- Error handling per node + workflow-level.
- Manual approval used for sensitive actions.
- Test fixtures with expected outputs.
- Text workflow diagram unambiguous.
- Hand-offs explicit.
