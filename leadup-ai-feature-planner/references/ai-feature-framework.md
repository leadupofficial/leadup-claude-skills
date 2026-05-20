# AI feature framework — LeadUp

How LeadUp designs AI features that ship, stay profitable, and don't
leak PII.

## 1. Six AI shapes

Pick one shape per feature:

| Shape | Examples |
|---|---|
| Generation | summary, draft, email/WhatsApp reply assist, content |
| Classification | tag a ticket, route a lead, score a booking risk |
| Retrieval / RAG | Q&A on owned docs (policies, manuals, past bookings) |
| Vision | OCR invoices, classify damage photo, before/after grading |
| Voice | transcribe call notes, voice → action command |
| Agentic | multi-step tool use (carefully — high risk + cost) |

Default first AI feature for a service-SaaS = generation or classification.
Agentic = later, with strict guardrails.

## 2. Model recommendation

Default LeadUp picks (verify pricing in
`leadup-api-research-builder`):

| Need | Primary | Fallback | Why |
|---|---|---|---|
| High-quality text generation | Claude Sonnet 4.x | Claude Haiku / GPT | quality + India language |
| Fast / cheap text | Claude Haiku 4.x | GPT-4o-mini | low cost, low latency |
| RAG with citations | Claude Sonnet 4.x with citations | GPT-4o | citation support |
| Long-context analysis | Claude Opus 4.7 (1M ctx) | Sonnet | huge inputs |
| Vision OCR | Claude / GPT-4o vision | OSS layout model | quality |
| Speech-to-text | Whisper | local Whisper | multilingual |
| Open-source / on-prem | Llama 3.x / Qwen / Mistral | — | sensitive data |

Always pick a primary + fallback. Vendor outages happen.

## 3. Prompt + data design

- **System prompt**: role + constraints + output format.
- **User prompt**: structured (markdown / JSON), short, explicit.
- **Output schema**: enforce JSON where possible; cap length.
- **Few-shot**: 2–4 examples when format is tricky.
- **Citations**: turn on for RAG.
- **Language**: explicit language flag; tested per language.
- **PII handling**: redact before send, restore after; or use closed-
  network model for sensitive scopes.

## 4. Cost ledger (mandatory)

For every AI feature, write down:

| Variable | Value |
|---|---|
| Input tokens per call | [N] |
| Output tokens per call | [N] |
| Calls per user per month | [N] |
| Cost per 1M input / output tokens | [$ / model] |
| Estimated cost per user per month | [₹ / $] |
| User's tier price | [₹ / $] |
| Cost as % of tier price | [%] |

Hard rules:

- If cost > 25% of tier price, **cap or batch or shrink**.
- If cost > 100% of tier price, **block** the feature.

Cheap design patterns:

- **Cache** by input hash.
- **Batch** non-real-time work nightly.
- **Smaller model** for routine cases; escalate to bigger model only on
  hard cases.
- **Prompt compression** for repeated context (e.g. cached system
  prompt with Anthropic prompt caching).
- **Token cap** on output.

## 5. Privacy + data flow

For every AI feature:

- What data leaves the user's tenant?
- Which provider sees it (Anthropic, OpenAI, Gemini, OSS local)?
- Is there a data processing agreement?
- Retention: how long does the model provider keep logs? (E.g.
  Anthropic API: no training; logs per their policy.)
- Encryption in transit + at rest for any cached AI output.
- PII redaction before send.
- Sensitive scopes (medical, financial, kids) — prefer closed-network
  / on-prem models.

Route to `leadup-pii-risk-reviewer` for sign-off.

## 6. Fallback behavior (mandatory)

When the model is down, slow, or wrong, the user must still get a
useful experience. Default fallback patterns:

- **Generation**: show a template the user can edit.
- **Classification**: show a manual picker.
- **RAG**: show "no AI answer right now, here are the source docs".
- **Vision**: ask user to confirm the result.
- **Voice**: offer manual text entry.
- **Agentic**: stop, show what was done so far, ask the user.

Always design the path **without** AI.

## 7. Logging + observability

- Log: feature key, model used, latency, input token count, output
  token count, cost, success/fail, error code.
- DO NOT log raw PII / payment data. Redact at the edge.
- Sample full prompts + responses for QA in a separate, restricted store.
- Dashboard: latency p50/p95, error rate, cost per day, top error
  codes.
- Replay tool: take a redacted prompt and re-run for debugging.

## 8. Test plan

Required test sets:

1. **Golden cases** (10–20): typical inputs, expected outputs.
2. **Edge cases** (5–10): empty, very long, non-English, ambiguous.
3. **Jailbreak attempts** (5–10): prompt injection, role-play attacks,
   data exfiltration attempts.
4. **Regulated cases** (if applicable): PII present, refusal expected.
5. **Load test** (if real-time): peak concurrent users.

Score each: pass / fail / partial. Aim ≥ 90% pass before launch.

## 9. Launch sequence (gated)

1. **Internal**: LeadUp team uses the feature for 1 week.
2. **1 client**: pilot with one friendly client; gather feedback.
3. **Soft launch**: 10% of users; monitor cost + quality.
4. **Full launch**: everyone; keep a kill switch.

Always keep a feature flag to disable the AI feature instantly.

## 10. Honesty rules

- Name the real user job.
- Cost ≤ % of tier price.
- PII routed to `leadup-pii-risk-reviewer`.
- Non-AI fallback designed.
- Logging redacted.
- Test set written before launch.
- Gated rollout.
- Defer LLM API research to `leadup-api-research-builder`.
- Defer public AI copy polish to `leadup-human-content-editor`.
