---
name: leadup-sales-proposal-builder
description: Build a clear, client-ready LeadUp proposal, project scope, quotation, retainer offer, AMC plan, or follow-up proposal from a rough brief. Produces objective, scope, deliverables, optional add-ons, timeline and pricing placeholders, exclusions, next steps, and a follow-up message. Use when the user says "proposal", "client proposal", "quote", "quotation", "project scope", "send proposal", "website package", or "maintenance package".
---

# LeadUp Sales Proposal Builder

## Purpose

Turn a rough client brief into a complete, professional, LeadUp-style
proposal that an Indian small business or international client can read in
5 minutes and act on. Covers websites, SaaS builds, Flutter apps, hosting
panels, SEO/SMM retainers, AMC, and follow-up proposals.

## When to use

Use when the user wants a proposal or quote produced. Do **not** trigger
when the user wants a full project plan (use `leadup-project-kickoff`),
pricing-package design only (use `leadup-pricing-package-planner`), or a
client message rewritten (use `leadup-client-document-generator`).

Trigger phrases: "proposal", "client proposal", "quote", "quotation",
"project scope", "send proposal", "website package", "maintenance
package", "make AMC plan", "retainer proposal".

## Inputs needed

- Client name, industry, location.
- Project type (website / SaaS / app / SEO retainer / AMC / other).
- Brief (one paragraph from the client or sales call notes).
- Known budget band or "ask user for pricing".
- Timeline if discussed.
- LeadUp's role (full build, redesign, support, ongoing).
- Any must-include items (logo, GST, terms) or must-avoid items.

Ask at most 2 clarifying questions if scope or pricing is genuinely
ambiguous.

## Tools/resources to use

- `references/proposal-framework.md` — section structure and tone rules.
- `assets/proposal.template.md` — fill-in proposal shape.
- Prior LeadUp proposals if the user references them.
- `leadup-human-content-editor` for final stylistic polish before sending.
- `leadup-pricing-package-planner` when packaging is the bigger question.
- `leadup-client-requirement-analyzer` when the brief is messy and needs
  to be turned into requirements first.

If the user does not have official pricing yet, use placeholders
`[fill in]` or a recommended range and flag it.

## Step-by-step workflow

1. **Restate the brief** in one line (who, what, why, by when).
2. **Pick the proposal type** (website / SaaS / app / retainer / AMC /
   follow-up).
3. **Build the structure** using `references/proposal-framework.md`:
   - Cover line and objective
   - Scope (in / out)
   - Deliverables
   - Optional add-ons
   - Timeline (placeholders if not finalised)
   - Pricing (placeholders or band if not confirmed)
   - Exclusions
   - Acceptance criteria
   - Payment terms
   - Next steps
4. **Write in LeadUp tone**: simple, trustworthy, business-specific. No
   em dashes. No banned hype words.
5. **Add a short follow-up message** the team can send 3 days later.
6. **Self-check**: every section present, all numbers either confirmed by
   the user or marked as `[fill in]` / `[recommended range]`.
7. **Hand off** the rewritten public-facing copy to
   `leadup-human-content-editor` before sending.

## Required output format

One Markdown document with these sections, in this order:

1. **Brief restate** — one line.
2. **Proposal (client-ready)** — full document in the
   `assets/proposal.template.md` shape, ready to paste into a PDF.
3. **Internal notes** — what's confirmed, what's `[fill in]`, what to
   confirm with the client before sending.
4. **Follow-up message** — short message to send 3 days after sharing
   the proposal.
5. **Hand-offs** — to `leadup-human-content-editor`,
   `leadup-pricing-package-planner`, or `leadup-client-document-
   generator` as relevant.

## Safety rules

- Do **not** invent pricing. Use `[fill in]` placeholders or a stated
  recommended range, and tell the user to confirm before sending.
- Do **not** invent client logos, awards, ISO numbers, or "trusted by"
  claims.
- Do **not** promise outcomes you cannot guarantee (rankings, sales,
  leads, revenue). Use language like "aim", "based on similar projects",
  "with the assumptions below".
- Keep payment terms explicit: who pays how much, when, by which channel
  (UPI, bank transfer, Razorpay).
- For India: include GST handling, invoice format, and HSN/SAC where
  relevant; flag if the client is outside India for currency / TCS
  considerations.
- Include an exclusions block — what is **not** included is as
  important as what is.
- Defer public-facing copy polish to `leadup-human-content-editor`.
- Defer integrations or API mentions to `leadup-api-research-builder`.
- Defer privacy / PII handling notes for sensitive industries to
  `leadup-pii-risk-reviewer` / `leadup-security-review`.

## Common mistakes

- One mega-paragraph instead of clear sections.
- Pricing that "looks right" but was invented.
- No exclusions block, leading to scope creep later.
- Promising delivery dates without the dependency block.
- Marketing copy inside a contractual section.
- Forgetting the follow-up message entirely.
- AI-hype language ("revolutionary", "world-class", "seamless").

## Troubleshooting

- **No budget shared**: use a recommended range with two tiers and a
  question to confirm.
- **Vague brief**: route first to `leadup-client-requirement-analyzer`,
  then come back here.
- **Multiple stakeholders**: split next steps by stakeholder + by date.
- **Repeat client / retainer renewal**: keep the proposal short, focus on
  what's changing, and reuse prior scope blocks.
- **International client**: switch currency, note timezone for milestones,
  flag GST/TCS implications.
- **User wants a one-pager**: deliver only objective + scope + price band
  + next step.

## Test prompts

### Should trigger (5)
1. "Build a proposal for a salon website redesign in Coimbatore."
2. "Send a quote for a 6-month SEO retainer for a dental clinic."
3. "Make an AMC proposal for our hosting client."
4. "Draft a website package proposal for a jewellery shop."
5. "Write a retainer proposal for SMM + ads for a real-estate client."

### Should NOT trigger (3)
1. "Kick off the actual project after the client signs." (→ `leadup-project-kickoff`)
2. "Just polish this proposal copy." (→ `leadup-human-content-editor`)
3. "Design Basic/Standard/Premium packages first." (→ `leadup-pricing-package-planner`)

### Functional test cases (2)
1. Given "website redesign for a dental clinic, no budget shared",
   return a proposal with placeholders for price/timeline, an
   exclusions block, payment terms with GST, a follow-up message, and
   internal notes flagging exactly what the salesperson must confirm.
2. Given "SEO retainer for an Indian SaaS, 6 months, budget
   ₹40K/month", return a proposal with confirmed monthly fee, scope,
   deliverables, exclusions, KPIs framed as targets not guarantees, and
   a hand-off to `leadup-human-content-editor` before sending.

## Success criteria

- Proposal has all required sections in order.
- No invented pricing, awards, or claims.
- All unknown numbers are explicit placeholders.
- Exclusions block present.
- Payment terms + GST handling explicit (for India).
- Follow-up message included.
- Hand-off to `leadup-human-content-editor` called out.
