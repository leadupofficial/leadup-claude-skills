# Proposal framework — LeadUp

How LeadUp structures client proposals so a busy owner reads them in 5
minutes and can decide. No hype. Honest scope. Clear money.

## 1. Section order (every proposal)

1. **Cover line** — one sentence stating who this is for and what for.
2. **Objective** — what the client wants, in their words.
3. **Scope (In)** — what LeadUp will do.
4. **Scope (Out / exclusions)** — what is NOT included.
5. **Deliverables** — concrete artefacts the client will receive.
6. **Optional add-ons** — items the client can pick later.
7. **Timeline** — milestones and dates (or `[fill in]`).
8. **Pricing** — fees, GST, currency (or `[fill in]` / band).
9. **Payment terms** — split, due dates, channel, late-payment.
10. **Acceptance criteria** — how we agree a milestone is done.
11. **Assumptions and dependencies** — what we expect from the client.
12. **Next steps** — exact actions for the client today.

## 2. Tone

- Simple business English.
- Confident but not boastful.
- No em dashes. No banned hype words (seamless, empower, unlock, robust,
  cutting-edge, leverage, elevate, harness, supercharge, revolutionize,
  game-changing, world-class, next-generation, holistic, synergy).
- No "we believe in dreams" energy. Specific examples beat slogans.

## 3. Pricing rules

- Never invent a number. If pricing is unknown, write `[fill in]` or a
  recommended band with a question for the user.
- Always split between **one-time** and **recurring**.
- For India: state GST treatment (18% standard for IT services unless
  otherwise), HSN/SAC code if known, invoice currency (INR), payment
  channel (UPI / bank / Razorpay).
- For international: state currency, GST/TCS implications, payment
  channel (Stripe / wire / Wise / Razorpay Intl).
- Late-payment: state interest or service-pause clause if needed.

## 4. Scope rules

- "In" lines are short, verb + object ("Design 6 pages", "Set up
  WhatsApp reminders", "Train one admin user").
- "Out" lines protect the team from scope creep. Common exclusions:
  - Copywriting (unless explicitly scoped).
  - Photography / video / graphic design (unless scoped).
  - Paid ad spend (separate from management fee).
  - Domain, hosting, third-party tool fees.
  - Translation / localization.
  - Bug fixes beyond the support window.
  - Major redesigns mid-project.

## 5. Timeline rules

- Phase-based when possible (Design → Build → Test → Launch).
- Each phase has a duration band, not a single point.
- Note dependencies (client review SLAs, content delivery).
- Note holidays / blackout windows.

## 6. Acceptance criteria

- One short, testable bullet per deliverable.
- Examples:
  - "Pages render under 2s on mobile (Lighthouse)."
  - "Client can add a new staff member from admin without help."
  - "WhatsApp template is approved by Meta and sends end-to-end."
- Avoid subjective tests ("looks nice").

## 7. AMC / retainer specifics

For ongoing AMC or retainers:

- State **what's covered** per month (hours, scope, types of fixes).
- State **what's NOT covered** (new features, redesigns).
- State **response SLA** (e.g. 1 business day) and **resolution SLA**
  (e.g. critical < 24h, minor < 5 business days).
- State **renewal terms** (auto-renew or manual, notice period).

## 8. Follow-up message (always include)

A short message the team sends 3 days after sharing:

```
Hi [Client name], just checking in on the proposal we shared on [date].
Happy to walk through any sections or adjust scope. If you'd like to
move forward, the next step is [signing / token payment / kickoff
call]. Let me know what works.

— [Sales / PM name], LeadUp
```

## 9. Safety + accuracy

- Do not invent pricing, awards, ISO numbers, client logos, or
  certifications.
- Do not promise SEO rankings, leads, or revenue. Use "aim",
  "target band", "based on similar projects".
- Do not skip exclusions.
- Do not soften refund / cancellation terms without flagging the change.
- Defer public copy polish to `leadup-human-content-editor`.
- Defer integrations or API references to `leadup-api-research-builder`.
- Defer PII / sensitive-data scope to `leadup-pii-risk-reviewer`.
