---
name: leadup-blog-content-writer
description: Write SEO-aware, human-style blog posts and service-page content for LeadUp client websites and SaaS, with title options, meta description, brief, outline, FAQ, internal links, and a full draft that avoids AI-style wording and em dashes. Use when the user says "write blog", "seo blog", "article writer", "blog content", "write service page", or "human blog".
---

# LeadUp Blog Content Writer

## Purpose

Take a topic or target keyword and produce a complete blog (or service)
content package: brief, SEO outline, title options, meta description, FAQ,
internal link suggestions, and a final human-style draft ready to publish
on a LeadUp client website or SaaS site.

## When to use

Use when the user wants a single post or page written. Do **not** trigger
for keyword research only (use `leadup-keyword-competitor-researcher`), an
SEO audit (use `leadup-seo-strategist`), or a content calendar
(use `leadup-content-calendar-builder`).

Trigger phrases: "write blog", "seo blog", "article writer", "blog
content", "write service page", "human blog", "draft this post", "write
an article on".

## Inputs needed

- Topic or target keyword.
- Audience and market (India tier-2/3, international, languages).
- Page type: blog / pillar / spoke / service / comparison / FAQ.
- Word count target (default 800–1500 for blogs, 600–1000 for service).
- Tone: simple business (default), premium/corporate, or casual.
- Brand name, product name, and CTAs to include.
- Internal pages on the site that the post should link to (URL list).
- Banned items: words, claims, competitor names.

Ask at most 2 clarifying questions if topic or audience is unclear.

## Required resources

- **Keyword input** from `leadup-keyword-competitor-researcher` if
  available (target keyword, intent, target page).
- **SERP scan** of the top 3–5 ranking pages for the target keyword:
  their H2s, word count band, schema, FAQs.
- **PAA / autocomplete** for FAQ questions.
- **Brand guidelines** if the user provides them.
- **Official docs** for any technical claim (product, API, regulation).
- Final polish: `leadup-human-content-editor` for AI-style cleanup if the
  draft starts to feel templated.

## Internet research workflow

1. Confirm intent of the target keyword (info / commercial / transactional).
2. Pull top 3–5 SERP results; record H1, H2 list, word count band, schema.
3. Pull PAA box + autocomplete for FAQ candidates (3–6 questions).
4. Verify any claim with an official source if technical or regulated
   (medical, financial, legal); note source.
5. Note assumptions and any claim that needs the user's confirmation.

If a browser or search MCP is available, hand off to
`leadup-mcp-tool-orchestrator`.

## Step-by-step workflow

1. **Restate** topic, audience, target keyword, intent, word count.
2. **Brief** (one block): goal, target keyword, secondary keywords,
   audience, tone, CTAs, must-include facts, must-avoid items.
3. **Outline** (SEO-aware): H1 (matches intent), 4–8 H2s, H3s where
   needed, FAQ section, CTA placement.
4. **Title options**: 5 titles (≤60 chars), each with a different angle
   (how-to, list, comparison, mistake, case).
5. **Meta description**: 150–160 chars, target keyword + benefit + CTA.
6. **Draft** the body section by section, following the outline:
   - Hook in the first 2 lines.
   - Vary sentence length; no em dashes (unless user asks).
   - No banned AI hype words.
   - Use specific examples (Indian or international, matching market).
7. **FAQ**: 3–6 Q&A pairs derived from PAA; answers 40–80 words each.
8. **Internal links**: 3–7 suggestions from the user's site (anchor +
   target URL + reason).
9. **Final pass**: run the draft through the human writing rules; if AI
   tells remain, route to `leadup-human-content-editor`.

Full framework: `references/blog-writing-framework.md`.
Brief shape: `assets/blog-brief.template.md`.

## Required output format

One Markdown document with these sections, in this order:

1. **Brief** — topic, target keyword, intent, audience, tone, word target.
2. **Title options (5)** — each ≤60 chars, different angle.
3. **Meta description** — single line, 150–160 chars.
4. **Outline** — H1 + H2s + H3s + FAQ + CTA placement.
5. **Draft** — full body in Markdown, headings preserved, no em dashes,
   no banned hype words, sentence rhythm varied.
6. **FAQ** — 3–6 Q&A pairs.
7. **Internal links** — anchor → URL → reason.
8. **Assumptions and verification needs** — sources used, any claim that
   needs user confirmation.

Defer final stylistic polish to `leadup-human-content-editor` if needed.

## Safety rules

- Do **not** use em dashes unless the user explicitly asks.
- Do **not** use the LeadUp banned hype words (seamless, empower, unlock,
  robust, cutting-edge, leverage, elevate, harness, supercharge,
  revolutionize, game-changing, world-class, next-generation, holistic,
  synergy) unless explicitly required by the brand.
- Do **not** invent statistics, citations, case studies, client names,
  awards, or quotes. If a stat is needed, mark `[verify: source]`.
- Do **not** copy competitor content; reference structure only.
- Do **not** make medical, legal, or financial claims without an official
  source — flag for user verification.
- Keep prices, dates, and product names exact from the source.
- For India audience: clear international English; avoid Indian-English
  habits ("do the needful", "kindly revert") unless the brand uses them.
- Respect copyright. Quote sparingly with attribution.
- Defer integrations to `leadup-api-research-builder`; defer browser /
  search tooling to `leadup-mcp-tool-orchestrator`; defer final polish to
  `leadup-human-content-editor`.

## Common mistakes

- Hero paragraph that says nothing (filler before getting to the answer).
- Every H2 the same length and shape (AI rhythm).
- Em dashes sneaking back in for "flow".
- Inventing a statistic to make the intro feel authoritative.
- Long bullets where every line has the same verb form.
- Forgetting the FAQ — that's where most informational ranking lives now.
- Stuffing the target keyword in every H2.
- Vague benefits ("boost your business") with no concrete outcome.
- Treating a service page like a blog — service pages need pricing,
  process, and a strong CTA, not a 1500-word essay.

## Troubleshooting

- **No keyword research available**: pick the most obvious target from the
  topic and flag it as **estimated**; recommend a follow-up research pass
  with `leadup-keyword-competitor-researcher`.
- **User wants ultra-short post** (200–400 words): drop the FAQ, keep one
  CTA, one H2 maximum.
- **User wants long pillar (3000+ words)**: split into clear H2s,
  include a TOC, add 6+ FAQ entries.
- **Regulated topic** (medical, finance, legal, real estate): flag every
  claim for user verification; do not state outcomes as guarantees.
- **Translation request**: do not translate inside this skill; flag and
  route to a translator/translation pass.
- **Brand voice is highly casual / Gen-Z**: ask for 2 reference posts and
  match their pattern instead of defaulting to neutral business tone.

## Test prompts

### Should trigger (5)
1. "Write an SEO blog on 'WhatsApp reminders for clinics'."
2. "Draft a service page for our salon booking SaaS."
3. "Write a human-style article on 'reduce no-shows in dental clinics'."
4. "Write a comparison post: LeadUp Booking vs Calendly for Indian salons."
5. "Blog post on 'best invoicing for tier-2 city retailers' — no AI vibes."

### Should NOT trigger (3)
1. "Find me 100 keywords on dental marketing." (→ `leadup-keyword-competitor-researcher`)
2. "Plan 30 days of social posts." (→ `leadup-content-calendar-builder`)
3. "Audit our site's SEO." (→ `leadup-seo-strategist`)

### Functional test cases (2)
1. Given target keyword "salon software pricing in India" (commercial
   intent), return brief + 5 title options ≤60 chars + 150–160 char meta
   + outline with FAQ + 800–1200 word draft with zero em dashes, zero
   banned hype words, and 3+ internal link suggestions.
2. Given a regulated topic ("teeth whitening at home" for a dental
   clinic site), return a draft that flags every medical claim with
   `[verify: source]`, avoids guarantee language, and includes an
   "Assumptions and verification needs" block listing what the clinic
   must confirm before publishing.

## Success criteria

- Output has all 8 required sections in order.
- Draft has zero em dashes (unless user asked) and zero banned hype words.
- Title options under 60 chars; meta under 160 chars.
- FAQ is derived from real PAA / autocomplete signals, not invented.
- Internal links point to plausible user-site URLs with reasoning.
- Every statistic, citation, or claim is either sourced or marked
  `[verify: source]`.
- Tone matches LeadUp's simple, trustworthy, business-specific voice; if
  it doesn't, the user is told to run `leadup-human-content-editor`.
