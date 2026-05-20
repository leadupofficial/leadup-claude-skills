---
name: leadup-client-requirement-analyzer
description: Convert messy client input — WhatsApp messages, PDFs, screenshots, voice notes, sales-call notes, or a vague one-liner — into a clean LeadUp requirements document with goal, must-haves, optional features, missing questions, complexity, risks, recommended phases, quote scope, and the next reply to send the client. Use when the user says "analyze client requirement", "client message", "what client wants", "make requirement", "convert to scope", or "understand this client".
---

# LeadUp Client Requirement Analyzer

## Purpose

Take whatever a client has actually sent (forwarded WhatsApp threads,
voice-note transcripts, half-finished briefs, two-line emails, PDF
exports, screenshots of references) and convert it into a clean
LeadUp requirements doc that the team can quote and start work from.

## When to use

Use when the user has raw client input and needs structured requirements
before quoting or building. Do **not** trigger for proposal generation
(use `leadup-sales-proposal-builder`), pricing only (use
`leadup-pricing-package-planner`), or full project kickoff (use
`leadup-project-kickoff`).

Trigger phrases: "analyze client requirement", "client message", "what
client wants", "make requirement", "convert to scope", "understand this
client", "structure these notes", "what's the actual scope".

## Inputs needed

- Raw client input (paste, file, or transcript).
- Project type guess (website / SaaS / Flutter app / CRM / hosting /
  unknown).
- Industry and city if known.
- LeadUp's role guess (full build / redesign / fix / support).
- Stated budget / timeline if any.

Ask at most 2 clarifying questions only if the project type or LeadUp's
role is genuinely ambiguous.

## Tools/resources to use

- `references/client-requirement-framework.md` — how to extract intent
  from messy input.
- `assets/client-requirements.template.md` — output shape.
- `leadup-sales-proposal-builder` for the next step once requirements
  are confirmed.
- `leadup-pricing-package-planner` when packaging is the gap.
- `leadup-pii-risk-reviewer` if the project touches sensitive data
  (clinic, school, finance, kids).
- `leadup-api-research-builder` if the client named third-party tools
  (Razorpay, Tally, Zoho, WhatsApp BSP).

## Step-by-step workflow

1. **Extract the client's words** — copy direct phrasing so the goal
   stays in their voice.
2. **Translate to LeadUp categories**:
   - Goal (one line)
   - Must-have features
   - Optional features
   - Out-of-scope items (what they said no to or didn't mention)
3. **Mark unknowns** — every fact you can't confirm becomes a "missing
   question".
4. **Score complexity** (S/M/L/XL) and effort band per feature.
5. **List risks** — technical, legal/compliance, payment, content
   readiness, stakeholder.
6. **Recommend phases** (MVP → Phase 2 → Later).
7. **Draft a quote scope** the salesperson can plug into a proposal.
8. **Draft the next reply** to send the client — a short message asking
   the missing questions in a friendly, non-pushy tone.

## Required output format

One Markdown document with these sections, in this order:

1. **Brief** — restate of raw input in one paragraph, in plain English.
2. **Client goal** — one line in the client's own words.
3. **Must-have features** — bulleted, each with role + outcome.
4. **Optional / nice-to-have features** — bulleted.
5. **Out of scope** — bulleted, with why.
6. **Missing questions** — numbered list the salesperson should ask.
7. **Complexity per feature** — table: feature · complexity · effort
   band · risk note.
8. **Risks** — technical, legal, content, vendor.
9. **Recommended phases** — MVP / Phase 2 / Later.
10. **Quote scope** — short block the proposal builder can plug in.
11. **Next reply to client** — short message, polite, asking the top 3–5
    missing questions, with a clear next step.
12. **Hand-offs** — `leadup-sales-proposal-builder`,
    `leadup-pricing-package-planner`, `leadup-pii-risk-reviewer`, etc.

## Safety rules

- Do **not** invent client details (industry, budget, location) the
  client did not state. Mark unknowns as "missing question".
- Do **not** translate vague client emotion into hard commitments
  ("urgent" → "by Friday") without a missing question.
- Do **not** drop legal / regulated context (clinic, finance, kids,
  payments) — flag it for `leadup-pii-risk-reviewer` /
  `leadup-security-review`.
- Do **not** put the client's exact verbatim into the public proposal —
  paraphrase respectfully when it becomes external copy.
- Keep India context (UPI, GST, WhatsApp BSP, regional language) when
  the client implies it.
- Do not delete the client's actual words; quote them where useful.

## Common mistakes

- Inventing features the client did not ask for.
- Over-scoping into a 6-month project from a 2-line message.
- Ignoring the optional / out-of-scope buckets.
- Missing PII / payment / compliance flags for regulated industries.
- Replying to the client with 12 questions in one go — pick top 3–5.
- Treating ambiguity as confirmation. If unclear, it's a question.

## Troubleshooting

- **Voice-note / audio transcript only**: paraphrase carefully, mark
  uncertain phrases, and add "verify transcript" as a missing question.
- **PDF / screenshot input**: extract bullet points; cite which page /
  image each came from.
- **Multiple stakeholders contradict each other**: list both versions
  side by side; ask which is final.
- **Client lists 20 features**: bucket them — 4–6 must-haves, the rest
  optional or later.
- **Regulated industry**: flag PII / payments early; route to
  `leadup-pii-risk-reviewer` before quoting.
- **Client is non-technical**: rewrite jargon into plain English and
  show the rewrite in the next reply.

## Test prompts

### Should trigger (5)
1. "Here's a WhatsApp thread from a salon owner — what do they actually want?"
2. "Convert this client message into a clear scope."
3. "Analyze this PDF brief from a dental clinic."
4. "Make requirements from these sales-call notes."
5. "Structure this client's voice note into our requirements format."

### Should NOT trigger (3)
1. "Send a final proposal." (→ `leadup-sales-proposal-builder`)
2. "Design Basic/Standard/Premium packages." (→ `leadup-pricing-package-planner`)
3. "Bootstrap a new project." (→ `leadup-project-kickoff`)

### Functional test cases (2)
1. Given a messy 6-message WhatsApp thread from a clinic owner asking
   for "a website with bookings, WhatsApp reminders, and maybe
   payments", return a structured doc with goal, 4–6 must-haves, 2–3
   optional, an out-of-scope block, a top-5 missing-question list, a
   risks block flagging PII for `leadup-pii-risk-reviewer`, and a
   ready-to-send next-reply message.
2. Given a 2-line vague brief ("we want an app for tutoring center"),
   return a doc that says exactly what the team needs to learn before
   quoting (audience, platforms, scale, payments, roles), with 5 missing
   questions and a polite client reply, and does NOT invent features
   beyond the brief.

## Success criteria

- All 12 sections present in order.
- Missing-question list has 3–5 high-leverage questions, not 12.
- Must-have / optional / out-of-scope buckets are filled honestly.
- Regulated-industry flags routed to the right LeadUp skill.
- Next-reply message is short, polite, and ends with a clear next step.
- No invented features, budgets, or timelines.
