# AI feature plan — [Feature name]

> Date: [YYYY-MM-DD]  ·  Product: [name]
> User: [role + market]  ·  Tier price impact: [₹/$ per user/month]
> Regulated category? [yes / no]

## 1. Brief restate

> [One line: the AI feature, who it's for, the user job it solves.]

## 2. AI shape

Pick one:
- [ ] Generation
- [ ] Classification
- [ ] Retrieval / RAG
- [ ] Vision
- [ ] Voice
- [ ] Agentic (high risk — justify)

## 3. User flow

```
User does [action]
  → system gathers [inputs from product]
  → AI generates [output]
  → user sees [UI]
  → user can [accept / edit / regenerate / fallback]
```

Step-by-step:

1. Trigger: [e.g. user opens admin → clicks "Summarize this week"]
2. Backend collects: [inputs]
3. Prompt built with: [system prompt + user prompt + few-shot]
4. Model returns: [output schema]
5. UI shows: [layout]
6. User action: [accept / edit / regen / fallback]

## 4. Model recommendation

| Slot | Model | Reason | Notes |
|---|---|---|---|
| Primary | [e.g. Claude Sonnet 4.6 with prompt caching] | quality + India lang | streaming on/off |
| Fallback | [e.g. Claude Haiku 4.5] | cost, latency | smaller context |
| Backup vendor | [GPT-4o / Gemini Flash / OSS] | vendor outage | requires plumbing |

Verify pricing + limits with `leadup-api-research-builder`.

## 5. Prompt + data design

**System prompt outline:**
```
You are [role]. You will receive [input shape].
Constraints: [language, length, format, refusal rules].
Output format: JSON matching [schema], no extra prose.
If you cannot answer with high confidence, return {"status": "needs_human"}.
```

**User prompt structure:**
```
[Context block, redacted PII placeholders]

[Task block: one sentence]

[Optional: few-shot examples]
```

**Output schema (JSON):**
```json
{
  "summary": "string, <= 200 chars",
  "highlights": ["string", "..."],
  "confidence": "low | med | high",
  "needs_human": false
}
```

Caps: input ≤ [N] tokens, output ≤ [N] tokens, temperature [0.2–0.4].

## 6. Cost ledger

| Variable | Value |
|---|---|
| Input tokens / call | [N] |
| Output tokens / call | [N] |
| Calls / user / month | [N] |
| Cost per 1M input / output | [$ from model card] |
| Cost / call | [₹ / $] |
| Cost / user / month | [₹ / $] |
| Tier price | [₹ / $] |
| Cost as % of tier | [%] |
| Verdict | ship / cap / batch / smaller-model / block |

Hard rules: cap if > 25%; block if > 100%.

## 7. Privacy + data flow

- What leaves the tenant: [list]
- Provider seeing it: [Anthropic / OpenAI / Gemini / OSS local]
- DPA / training opt-out: [link or status]
- Retention at provider: [days]
- Redaction at edge: [PII fields → placeholders]
- Sensitive category: [yes / no — health / finance / kids]
- Encryption: in transit (TLS), at rest (cached results), key rotation

Routed to `leadup-pii-risk-reviewer` on [YYYY-MM-DD]: [status].

## 8. Fallback behavior

If model fails (down, > N seconds, error):

- UI shows: [exact text user sees]
- Non-AI path: [template / manual picker / source docs / manual entry]
- Retry policy: [N attempts × M ms]
- Feature flag: [name] — turning OFF returns the non-AI experience.

## 9. Logging + observability

Per call, log (redacted):

| Field | Value |
|---|---|
| feature_key | [str] |
| model | [str] |
| latency_ms | [int] |
| input_tokens | [int] |
| output_tokens | [int] |
| cost_usd | [float] |
| success | [bool] |
| error_code | [str / null] |
| user_org_id | [str] |

Sampled prompt + response in a separate restricted store (≤ 5% of
traffic, redacted PII).

Dashboard: latency p50/p95, error rate, cost/day, top error codes.

## 10. Test plan

| Set | Cases | Pass criteria |
|---|---|---|
| Golden | 10–20 typical | output matches expected within tolerance |
| Edge | 5–10 (empty, long, non-English) | graceful, no crash |
| Jailbreak | 5–10 injections | refuse / `needs_human` |
| Regulated | if applicable | refuse / disclaimer / `needs_human` |
| Load | if real-time | p95 latency under budget |

Overall pass rate ≥ 90% before launch.

Test cases drafted in `leadup-qa-test-case-generator` if a wider QA pass
is needed.

## 11. Launch sequence

- [ ] Internal pilot — 1 week (LeadUp team)
- [ ] 1 client pilot — 1 week (named client)
- [ ] Soft launch — 10% traffic, monitor cost + quality (1 week)
- [ ] Full launch — kill switch ready
- [ ] Post-launch review — week 4

## 12. Assumptions and data confidence

- **Verified** (model card / docs): [list]
- **Estimated** (token counts, calls/user): [list, with reasoning]
- **Requires verification**: [list]

## 13. Hand-offs

- LLM API research → `leadup-api-research-builder`.
- PII review → `leadup-pii-risk-reviewer`.
- Sensitive scope security → `leadup-security-review`.
- Public AI copy polish → `leadup-human-content-editor`.
- Broader QA test cases → `leadup-qa-test-case-generator`.
- Release coordination → `leadup-release-manager`.
