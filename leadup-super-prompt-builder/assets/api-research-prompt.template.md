Prompt type: API research · Target: Claude Code / RuFlo / ChatGPT

```
Research integrating [API, e.g. Razorpay / WhatsApp / Gemini] into the
LeadUp project "[project]".

Context: LeadUp Technologies. Stack: [stack]. Expected volume: [approx].

Deliver a decision-ready dossier (official docs first, then reputable
GitHub examples):
- What it does + official docs URL + official SDK (maintained? last release)
- Auth method (key / OAuth2 / HMAC) and test vs live mode
- Endpoints we'd use
- Rate limits / quotas
- Current pricing WITH the date checked (flag as "verify if stale")
- Webhooks: events, signature verification, idempotency, local testing
- Env variable NAMES to add, as placeholders only:
  [PROVIDER]_KEY_ID=__SET_ME__   [PROVIDER]_KEY_SECRET=__SET_ME__
- 1–2 reference repos with license + recency + what to copy/adapt
- Risks, failure modes, India data-residency notes
- Fallback / degraded plan if the API is down or over quota
- Recommendation: go / no-go + ordered integration steps (no code yet)

Constraints: never request, print, or invent real keys; verify signature
+ amount server-side for payments; no push/deploy without approval.
```

Toggles: [add cost projection] · [compare 2 providers] · [add code outline]
