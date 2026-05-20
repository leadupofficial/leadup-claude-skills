---
name: leadup-ai-feature-planner
description: Plan a single, useful AI feature for a LeadUp website, SaaS, admin panel, CRM, mobile app, or automation workflow with goal, user flow, model recommendation, prompt and data design, cost risk, privacy risk, fallback behavior, logging and observability plan, and a test plan. Designed so AI features ship safely and stay profitable for Indian SMB SaaS and global products. Use when the user says "AI feature", "add AI", "make app intelligent", "AI chatbot", "AI report", "AI assistant", or "automation AI".
---

# LeadUp AI Feature Planner

## Purpose

Design ONE AI feature end-to-end: who it's for, the named user job, the
model and prompt design, the data it touches, fallback when the model
fails, observability, cost ceiling, and a real test plan. Built so AI
features actually ship and stay profitable, not "AI sticker on top".

## When to use

Use when the user wants a specific AI feature planned. Do **not**
trigger for the broader product roadmap (use
`leadup-feature-option-planner`), for SaaS MVP scope (use
`leadup-saas-mvp-planner`), or to integrate an LLM API only (use
`leadup-api-research-builder`).

Trigger phrases: "AI feature", "add AI", "make app intelligent", "AI
chatbot", "AI report", "AI assistant", "automation AI", "smart
suggestion", "summarize with AI".

## Inputs needed

- Product / feature context in 2–3 lines.
- Who the AI feature is for (named role: owner, staff, customer,
  admin).
- The user job it should solve (named, concrete).
- Data the AI will see (must specify: PII, financial, medical, child).
- Cost budget per user per month, if known.
- Latency budget (real-time chat vs background batch).
- Audience market (India / global / both).
- Constraints: regulated industry, brand voice, language.

Ask at most 2 clarifying questions if the user job or data scope is
unclear.

## Tools/resources to use

- `references/ai-feature-framework.md` — design rules, cost ledger,
  fallback patterns.
- `assets/ai-feature-plan.template.md` — output shape.
- `leadup-api-research-builder` — for the actual LLM / vector DB API
  research.
- `leadup-pii-risk-reviewer` — mandatory if PII is in scope.
- `leadup-security-review` — for payments / sensitive scopes.
- `leadup-human-content-editor` — for any user-facing AI output that
  becomes public copy.
- `leadup-qa-test-case-generator` — for the test suite.

## Step-by-step workflow

1. **Restate** the feature in one line. Name the user, the role, and
   the job.
2. **Decide the AI shape**: classify into one of:
   - Generation (summary, draft, reply assist).
   - Classification (tag, route, score).
   - Retrieval / RAG (Q&A on owned data).
   - Vision (image classify, OCR, before/after).
   - Voice (transcribe, voice → action).
   - Agentic (multi-step tool use).
3. **Pick a model recommendation** with a fallback (e.g. Claude
   Opus → Sonnet / Haiku, OpenAI GPT, Gemini, open-source — chosen by
   cost × accuracy × privacy fit).
4. **Prompt + data design**: inputs the model sees, system prompt
   shape, output schema, length limits, language.
5. **Cost ledger**: tokens per call × calls per user per month × model
   price; compare to user-month price. Hard cap if cost > price.
6. **Privacy + data flow**: what leaves the user's tenant? Where does
   it go (model provider, logs, vector DB)? Route to
   `leadup-pii-risk-reviewer`.
7. **Fallback behavior**: what the user sees when model is down, slow,
   or wrong. Always design a non-AI fallback path.
8. **Logging + observability**: prompt + response logged where, with
   what redaction; latency, cost, error metrics; a way to replay.
9. **Test plan**: golden inputs + expected outputs, edge cases,
   regulated cases, jailbreak attempts, load tests if real-time.
10. **Launch sequence**: gated rollout (internal → 1 client → full).

## Required output format

One Markdown plan with these sections, in this order:

1. **Brief restate** — feature, user, role, job.
2. **AI shape** — generation / classification / RAG / vision / voice /
   agentic.
3. **User flow** — step-by-step what the user does and sees.
4. **Model recommendation** — primary + fallback + reason.
5. **Prompt + data design** — inputs, system prompt outline, output
   schema, length limits.
6. **Cost ledger** — tokens/call · calls/user/mo · cost/call · monthly
   cost vs user-month price.
7. **Privacy + data flow** — what leaves the tenant; where it lives;
   retention; PII routed to `leadup-pii-risk-reviewer`.
8. **Fallback behavior** — what users see when AI is down / slow /
   wrong.
9. **Logging + observability** — what's logged, redaction rules,
   metrics dashboard.
10. **Test plan** — golden cases, edge cases, jailbreak attempts,
    regulated cases.
11. **Launch sequence** — internal → 1 client → full.
12. **Assumptions and data confidence** — verified / estimated /
    requires verification.
13. **Hand-offs** — to other LeadUp skills.

## Safety rules

- Every AI feature must name a real user job. "AI dashboard" is not a
  job; "summarize last 30 bookings in 10 seconds" is.
- Do **not** propose AI features whose monthly cost exceeds the
  user's plan price. Cap, batch, or use a smaller model.
- Do **not** send PII to a model provider without an explicit data
  agreement; flag and route to `leadup-pii-risk-reviewer`.
- For regulated industries (health, finance, kids, legal), avoid AI
  outputs that look like professional advice. Add disclaimers.
- Always design a non-AI fallback.
- Never log raw PII / payment data; redact in logs.
- For Indian audience: respect IT Rules, DPDP scope when in force, and
  language sensibilities (Hindi / Tamil / regional).
- Use `leadup-human-content-editor` for any AI-generated copy that
  becomes public.
- Defer model / vendor API depth to `leadup-api-research-builder`.

## Common mistakes

- "AI chat" with no defined intents → users get confused, model gets
  jailbroken.
- No fallback path → outage = feature dies.
- Cost not modelled → bills explode at scale.
- PII silently sent to a public model.
- Same prompt for every user → personalisation absent.
- No test set → quality is "vibes".
- Streaming output with no token cap → users can rack up costs.
- One model, no fallback model → vendor outage kills the feature.

## Troubleshooting

- **Cost > tier price**: batch (nightly), cache, smaller model, or
  scope down the feature.
- **PII risk**: route to `leadup-pii-risk-reviewer`; consider local /
  open models for sensitive scopes.
- **Latency too high for real-time**: move to background + notify; or
  pre-compute.
- **Quality inconsistent**: write a 20-case test set, evaluate, tune
  prompt / few-shot; consider a retrieval grounding step.
- **Regulated category**: add disclaimers, restrict topics, monitor
  outputs.
- **Multilingual user base**: test in each language; do not assume
  English-only quality transfers.

## Test prompts

### Should trigger (5)
1. "Add an AI summary of last 30 bookings to our admin."
2. "Plan an AI WhatsApp reply assist for our staff."
3. "Add a smart no-show prediction AI feature."
4. "AI chatbot on our salon website to answer FAQs."
5. "Make an AI report writer for our SaaS dashboard."

### Should NOT trigger (3)
1. "Plan all features for our SaaS." (→ `leadup-feature-option-planner`)
2. "Research the Anthropic API for us." (→ `leadup-api-research-builder`)
3. "Polish this AI-generated copy." (→ `leadup-human-content-editor`)

### Functional test cases (2)
1. Given "AI WhatsApp reply assist for salon staff, average 50 replies
   per staff per day, tier price ₹999/staff/month", return a plan with
   primary Claude Haiku + fallback Sonnet, a tokens-per-call estimate,
   a monthly cost band per staff vs tier price, PII redaction rules,
   a non-AI fallback (template replies), test cases including Tamil
   and Hindi inputs, and a gated rollout.
2. Given a regulated category (an AI summary feature for a dental
   clinic that touches patient notes), return a plan that routes PII
   to `leadup-pii-risk-reviewer`, prefers on-prem / closed-network
   model where possible, adds disclaimers in output, redacts logs,
   and includes a jailbreak test set.

## Success criteria

- One AI feature, one named user job.
- Cost ledger present and within tier price (or capped).
- Privacy flow explicit; PII routed.
- Non-AI fallback designed.
- Logging redaction rules documented.
- Test plan has at least 10 golden + edge + jailbreak cases.
- Launch is gated (internal → 1 client → full).
- Hand-offs to `leadup-api-research-builder`,
  `leadup-pii-risk-reviewer`, and `leadup-human-content-editor` are
  explicit.
