---
name: leadup-client-document-generator
description: Generate professional LeadUp client and business documents — proposals, project briefs, estimates, status reports, developer docs, API-access request emails, and handoff documents — in clean PDF-ready Markdown. Use when the user says "create document", "client proposal", "developer document", "API request email", "project report", or "handoff document".
---

# LeadUp Client Document Generator

## Purpose

Produce polished, client-ready business and technical documents for LeadUp:
proposals, briefs, estimates, reports, developer docs, API-access request
emails, and handoff docs — structured, professional, and PDF-ready.

## When to use

Trigger phrases: "create document", "client proposal", "project brief",
"developer document", "API request email", "project report", "handoff
document", "write an estimate", "draft a proposal for the client".

For social/marketing content calendars → `leadup-content-calendar-builder`.
For internal STATUS/TODO bookkeeping → `leadup-status-updater`.

## Inputs needed

- Document type (proposal / brief / estimate / report / dev doc / API email /
  handoff).
- Audience (client, vendor, developer) and the project.
- Key facts: scope, timeline, price/estimate basis, contacts (no secrets).
- Brand tone (LeadUp = professional, clear, confident, no fluff).

## Step-by-step workflow

1. **Identify document type + audience**; pick the matching template in
   `assets/` (proposal, api-request-email, handoff, report).
2. **Collect/confirm facts**: scope, deliverables, timeline, price basis,
   assumptions, exclusions. Ask if missing — don't invent commitments.
3. **Draft** in clean Markdown with clear headings, tables for scope/pricing,
   and a professional LeadUp tone.
4. **Tailor**: proposals → value + scope + price + terms; estimates →
   line items + assumptions; reports → progress + risks + next; dev docs →
   setup/run/API; API emails → who/why/which scopes/contact.
5. **Review** for clarity, correctness, and that nothing confidential leaks.
6. **Output** PDF-ready Markdown; offer an export note (no auto-send).

## Required output format

A complete document in clean Markdown:
- Title, date, parties/contacts (no secrets)
- Structured sections per type (scope/pricing/timeline/terms or
  progress/risks/next, etc.)
- Tables for scope/line-items/pricing
- Clear next step / call to action
- "Draft for your review — not sent" footer line

## Safety rules

See `references/security-rules.md`. Most relevant here:
- Never include API keys, passwords, or real `.env` values in any document or
  email (API-access emails request access, never expose credentials).
- Do not invent prices, legal terms, or client commitments — mark assumptions
  and ask for confirmation.
- Do not auto-send emails or share documents externally without approval.

## Common mistakes

- Inventing a price/timeline instead of asking for the basis.
- Putting credentials into an "API request email" (request, never expose).
- Vague scope with no exclusions → scope creep risk in proposals.
- Over-promising in client tone; LeadUp tone is confident but precise.
- Sending/sharing without explicit approval.

## Troubleshooting

- **Under-triggers**: user said "write this up for the client" — re-invoke;
  suggest trigger phrases.
- **Over-triggers** for a content calendar → route to
  `leadup-content-calendar-builder`.
- **Missing tool/MCP**: deliver Markdown; note how to export to PDF; never
  auto-send.
- **No internet/browser**: fine — documents are generated from provided facts.
- **Missing inputs**: ask for scope/price-basis/contacts; never fabricate
  commitments or numbers.
- **Build/test failure**: not applicable; if a PDF export step fails, deliver
  the Markdown and the manual export steps.

## Test prompts

### Should trigger (5)
1. "Create a client proposal for the jewellery SaaS project."
2. "Write an API access request email to the WhatsApp BSP."
3. "Draft a project status report for the clinic client."
4. "Make a developer handoff document for the CRM."
5. "Write an estimate for the school website with line items."

### Should NOT trigger (3)
1. "Build a 30-day content calendar." (→ content-calendar-builder)
2. "Update STATUS.md after this task." (→ status-updater)
3. "Security review the payment flow." (→ security-review)

### Functional test cases (2)
1. For "client proposal", output scope (with exclusions), pricing table,
   timeline, terms, and a clear next step — no invented price (asks for basis).
2. An API-access request email requests access/scopes and a contact, and
   contains no keys or credentials.

## Success criteria

- Correct document type/structure for the audience, PDF-ready Markdown.
- Facts confirmed; assumptions marked; no invented commitments.
- No secrets/credentials anywhere; nothing sent without approval.
