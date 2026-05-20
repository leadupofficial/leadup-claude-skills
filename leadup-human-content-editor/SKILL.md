---
name: leadup-human-content-editor
description: Convert AI-generated or AI-looking content into natural, human-written, client-ready business copy for LeadUp websites, SaaS products, app screens, client documents, proposals, social posts, and project pages. Removes AI tells (em dashes, hype words like seamless/empower/unlock/robust/cutting-edge, over-polished rhythm, vague benefits) and rewrites in simple, trustworthy, business-specific Indian/international English. Use when the user says "make this human", "humanize this content", "remove AI style", "rewrite naturally", "make website copy natural", "anti AI content", "make this not look AI generated", "remove em dash", "make this client ready", "rewrite for website", "make content sound real", or "make this LeadUp style".
---

# LeadUp Human Content Editor

## Purpose

Take AI-generated or AI-flavoured text and rewrite it so it sounds like it was
written by a real business owner or an experienced copywriter. Output should
be natural, simple, trustworthy, business-specific, and ready to drop into a
LeadUp website, SaaS product, app screen, client document, proposal, or
social post — without losing meaning or important technical detail.

## When to use

Use when the user wants the *content rewritten to sound human*, not when they
want fresh content generated from scratch.

Trigger phrases: "make this human", "humanize this content", "remove AI
style", "rewrite naturally", "make website copy natural", "anti AI content",
"make this not look AI generated", "remove em dash", "make this client
ready", "rewrite for website", "make content sound real", "make this LeadUp
style".

Do **not** trigger when the user wants brand-new content (use the matching
generator skill: `leadup-content-calendar-builder` for social,
`leadup-client-document-generator` for proposals, etc.), or when they want
SEO research, translation, or copy in a different language only.

## Inputs needed

- The source text (paste, file, or section).
- Rewrite mode — one of the 9 modes below (infer if not stated).
- Target audience / industry (LeadUp client, end user, internal team, etc.).
- Tone preference: simple business (default), premium/corporate, or casual.
- Any must-keep items: brand name, product name, SEO keywords, numbers,
  technical terms, CTAs.
- Optional: word/length limit, banned words list, English variant.

Ask at most 2 clarifying questions, only if mode or audience is genuinely
unclear. Default to "simple business English, website-ready" if unstated.

## Step-by-step workflow

1. **Read the source** end-to-end. Identify intent, audience, and any
   must-keep facts (brand, product, numbers, CTAs, SEO keywords).
2. **Detect AI tells** using `references/ai-style-warning-signs.md`
   (em dashes, hype words, parallel "not just X but Y" structures, perfect
   tricolons, vague benefits, repeated sentence rhythm).
3. **Pick the rewrite mode** (1–9 below). Infer from the surrounding context
   if the user did not state it.
4. **Apply the human writing rules** from
   `references/human-writing-rules.md` and the LeadUp tone from
   `references/leadup-copy-tone.md`.
5. **Rewrite section by section**, preserving meaning, facts, and SEO
   keywords. Vary sentence length. Use plain words. Cut hype.
6. **Self-check against the AI-tell list**: no em dashes (unless asked),
   no banned words, no fake claims, no invented case studies / clients /
   awards / numbers.
7. **Output** the rewritten version in the required format below, with a
   short change note and any flagged risks (claims that need verification).

## Human writing rules

- Write the way a real business owner would speak to a customer.
- Short sentences mixed with medium ones. Avoid long perfect paragraphs.
- Use specific nouns and concrete examples instead of vague benefits.
- Prefer plain words over corporate / SaaS jargon.
- Keep verbs active. Cut filler ("in order to", "at the end of the day").
- Use contractions where natural ("we'll", "you're") unless the brand is
  formal/corporate.
- One idea per sentence. One job per paragraph.
- Do not use em dashes (—) unless the user explicitly asks. Replace with a
  comma, full stop, or "and".
- No fake intensifiers ("truly", "literally", "absolutely") unless they earn
  their place.
- Numbers, dates, and product names stay exact. Do not paraphrase facts.
- For Indian business context: use clear international English. Avoid Hindi
  filler unless the brand voice already uses it.
- Match the tone the brand already uses elsewhere on the site or product.
- Full rule set: `references/human-writing-rules.md` and
  `references/leadup-copy-tone.md`.

## AI-style warning signs

Flag and remove these patterns (full list:
`references/ai-style-warning-signs.md`):
- Em dashes used as the default connector.
- Hype words: seamless, empower, unlock, robust, cutting-edge, leverage,
  elevate, harness, supercharge, revolutionize, game-changing, world-class,
  next-generation, holistic, synergy.
- "Not just X but Y" / "It's not just A — it's B" parallel structures.
- Perfect tricolons ("faster, smarter, better") on every line.
- Generic openers ("In today's fast-paced world…", "In the ever-evolving
  landscape of…").
- Vague benefits ("boost your business", "take it to the next level")
  with no specific outcome.
- Over-balanced sentence rhythm across a whole paragraph.
- Long, perfect bullet lists where every line has the same shape.
- Hedging filler ("it's worth noting that", "as we all know").
- Closing pep-talks ("the future is bright", "let's embrace the journey").

## Rewrite modes

Pick the closest mode and apply the matching template in `assets/`.

1. **Website landing page** — hero, sub-hero, value props, social proof,
   CTAs. Asset: `assets/website-copy-edit.template.md`.
2. **SaaS feature copy** — feature blocks, in-product explainers, pricing.
   Asset: `assets/saas-copy-edit.template.md`.
3. **About company page** — story, mission, team, what we do, why us.
4. **Service page** — what's included, process, deliverables, FAQs.
5. **App/admin panel microcopy** — buttons, empty states, errors, tooltips.
   Asset: `assets/microcopy-edit.template.md`.
6. **Proposal / client document tone** — scope, timeline, pricing,
   acceptance. Keep formal but plain; no hype.
7. **Social media content** — LinkedIn, Instagram, X/Twitter, WhatsApp
   broadcast. Match platform length and voice.
8. **WhatsApp / email message** — short, direct, polite, one ask per
   message.
9. **Technical / project explanation** — internal docs, handoff notes,
   STATUS updates. Keep technical accuracy; remove marketing tone.

Worked before/after pairs for every mode live in
`references/rewrite-examples.md`.

## Required output format

Return one Markdown block with three parts, in this order:

1. **Mode + assumptions** — one line: `Mode: <mode> · Tone: <tone>` plus a
   one-line note if the source had unclear intent.
2. **Rewritten content** — inside a single fenced code block when the user
   will paste it (website/app/microcopy), or as plain Markdown when it's a
   document section. Preserve headings, lists, and any explicit CTAs from
   the source.
3. **Change note** — 3–6 bullets: what was changed and why (em dashes
   removed, hype words replaced, structure simplified, claims softened),
   and any flagged risks (claims that need the user to verify a number,
   client name, or certification).

No commentary mixed inside the rewritten block. Keep it copy-paste-ready.

## Safety rules

- Never invent case studies, client names, awards, certifications, ISO
  numbers, revenue figures, user counts, ratings, or testimonials. If the
  source has them, keep as-is; if not, do not add.
- Never insert real secrets, API keys, tokens, or `.env` values into copy.
  Use placeholders like `__SET_ME__` or `[fill in]` if the source does.
- Do not soften disclaimers, refund terms, legal language, or compliance
  statements without flagging it in the change note.
- Keep SEO keywords the user marked as required; place them naturally,
  never stuff.
- Do not change prices, dates, deadlines, or scope wording in proposals or
  contracts.
- Flag any claim that looks unverifiable ("best in India", "trusted by
  thousands") and ask the user to confirm or remove.
- For client websites, prefer believable, conversion-focused copy over
  hype; for app UI, prefer short and clear.
- Full rules: `references/leadup-copy-tone.md` and
  `references/human-writing-rules.md`.

## Common mistakes

- Removing AI tells but also removing meaning or important facts.
- Replacing one hype word with another hype word.
- Adding em dashes back in "for flow".
- Inventing specifics (numbers, clients, awards) to make the copy feel
  real — never invent.
- Over-casualising a proposal or compliance section.
- Stripping SEO keywords the user marked as required.
- Producing one long block instead of preserving the original structure
  (headings, bullets, CTAs).
- Mixing change notes inside the rewritten block, breaking copy-paste.
- Treating this skill as a content generator (it is not — use the matching
  generator skill for new content).

## Troubleshooting

- **Under-triggers**: user said "rewrite this for the website" and it did
  not fire — re-invoke and suggest the trigger phrases.
- **Over-triggers**: user wanted brand-new content, not a rewrite → route
  to `leadup-content-calendar-builder` (social) or
  `leadup-client-document-generator` (proposals/docs).
- **Source too short** (one line): rewrite it directly; no need for change
  note bullets beyond one line.
- **Source in another language**: rewrite only into the same language unless
  the user asked for translation; flag if mixed.
- **Source contains legal / compliance text**: do minimal stylistic edits;
  do not change meaning; flag in change note.
- **Source contains unverifiable claims**: keep them but flag for the user
  to confirm or cut; do not delete silently.
- **No clear brand tone**: default to simple business English and say so in
  the assumptions line.

## Test prompts

### Should trigger (5)
1. "Make this About Us page sound human, the AI vibes are too strong."
2. "Humanize this SaaS feature copy and remove the em dashes."
3. "Rewrite this landing hero naturally, no 'unlock' or 'empower'."
4. "Make this proposal client-ready in LeadUp style."
5. "Anti-AI rewrite this WhatsApp broadcast so it sounds like a real owner."

### Should NOT trigger (3)
1. "Write a new About Us page from scratch." (→ `leadup-client-document-generator`)
2. "Plan 30 days of Instagram posts." (→ `leadup-content-calendar-builder`)
3. "Translate this page from English to Hindi only." (translation, not rewrite)

### Functional test cases (2)
1. Given a paragraph full of em dashes, "empower", "seamless", and
   "cutting-edge", return a rewrite with zero em dashes, zero banned hype
   words, same meaning preserved, and a 3–6 bullet change note listing
   exactly what was changed.
2. Given a SaaS feature block with vague benefits ("boost your business")
   and no specific outcomes, return rewritten copy that replaces vague
   claims with concrete actions/outcomes from the source, keeps any SEO
   keyword the user marked as required, and flags any claim that needs
   user verification.

## Success criteria

- Output preserves meaning, facts, and SEO keywords from the source.
- Zero em dashes unless the user explicitly asked for them.
- Zero banned hype words from the AI-style warning list.
- Structure (headings, bullets, CTAs) preserved or improved, not flattened.
- No invented case studies, clients, awards, certifications, or numbers.
- Change note clearly lists what changed and flags any risky claims.
- Copy reads like a real business owner / experienced copywriter wrote it,
  in LeadUp's simple, trustworthy, business-specific voice.
