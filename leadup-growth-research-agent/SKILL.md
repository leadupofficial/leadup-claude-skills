---
name: leadup-growth-research-agent
description: Orchestrator for LeadUp's growth pack. Takes an open-ended growth or research request, picks the right LeadUp growth skill (SEO, keyword/competitor, blog, SMM, ads, CRO, feature) or runs cross-cutting internet research, collects sources, summarizes competitors, lists assumptions, marks data confidence, and recommends the next action. Use when the user says "do internet research", "research all resources", "growth research", "market research", "find competitors", "research deeply", or "what should we do for growth".
---

# LeadUp Growth Research Agent

## Purpose

Be the front door for any open-ended growth / research request. Decide
which LeadUp growth skill (or skills) applies, run the cross-cutting
internet research the request needs, summarize competitors and signals,
list assumptions, mark every number's confidence level, and recommend
the single next action.

## When to use

Use when the user wants research or a "what should we do for growth"
answer, not a single concrete skill output. If the request clearly maps
to one skill (e.g. "write a blog"), route directly to that skill instead.

Trigger phrases: "do internet research", "research all resources",
"growth research", "market research", "find competitors", "research
deeply", "what should we do for growth", "audit our marketing",
"benchmark us", "research everything for X".

## Inputs needed

- Business or product description in 1–3 lines.
- Audience and market.
- Goal (leads / signups / bookings / awareness / retention).
- Constraints (budget, team size, deadline, regulated category).
- Any specific competitors or sources to include.
- Available tools (Search Console, GA4, Meta Ads, GKP, browser MCP, etc.).

Ask at most 2 clarifying questions if goal or market is genuinely
ambiguous.

## Required resources

### LeadUp growth pack skills (route to these where they fit)

- `leadup-seo-strategist` — SEO audit + roadmap.
- `leadup-keyword-competitor-researcher` — keyword map + competitor.
- `leadup-blog-content-writer` — blog / service page drafts.
- `leadup-smm-growth-planner` — social strategy + calendar.
- `leadup-digital-ads-planner` — paid ads plan.
- `leadup-landing-page-cro-planner` — landing-page CRO.
- `leadup-feature-option-planner` — feature roadmap.

### Cross-cutting LeadUp skills

- `leadup-human-content-editor` — final copy polish.
- `leadup-api-research-builder` — tool / API integration research.
- `leadup-mcp-tool-orchestrator` — browser / search / MCP routing.
- `leadup-existing-repo-analyzer` / `leadup-project-kickoff` — code
  / repo work.

### External sources

See `references/growth-research-source-list.md` for the full list.
Headline categories:

- Search: Google, Bing, DuckDuckGo; Google "People also ask",
  autocomplete, related searches.
- SEO: Google Search Console, Google Keyword Planner, Google Trends,
  PageSpeed Insights, web.dev, Schema.org, Search Central.
- Social: Instagram Explore / Reels, LinkedIn search, YouTube
  Shorts, X search, Reddit, Quora.
- Ads: Meta Ad Library, Google Ads Transparency, LinkedIn Ad Library,
  YouTube ad signals.
- Analytics: GA4, Hotjar / Microsoft Clarity.
- Competitor sites: their public HTML, sitemap.xml, pricing page,
  changelog, blog index.
- Public communities + reviews: G2, Capterra, ProductHunt, Trustpilot,
  Reddit threads, niche forums.
- India-specific: ASCI, IT Rules, DPDP (when finalised in scope), GST
  rules, Razorpay docs, RBI guidance where finance is involved.

## Internet research workflow

1. Confirm the brief in one line. Restate.
2. Decide if this is **single-skill** or **multi-skill**.
3. List the **sources** to consult (from the list above) and what each
   source is expected to answer.
4. Hand off browser / search to `leadup-mcp-tool-orchestrator` if a
   browser or search MCP is available; otherwise document the manual
   research path.
5. Run the research; capture findings with **source + date** per claim.
6. Build the **competitor summary** (3–5 competitors max).
7. Build the **signal summary** (what's working in the category, what
   isn't).
8. List **assumptions** explicitly.
9. Mark every numerical claim as **verified** / **estimated** /
   **requires verification**.
10. Recommend the **single next action** and the LeadUp skill to run
    next.

## Step-by-step workflow

1. **Restate the request** in one line.
2. **Classify** the request into one of:
   - SEO question → `leadup-seo-strategist`.
   - Keywords / competitors → `leadup-keyword-competitor-researcher`.
   - Blog / service page → `leadup-blog-content-writer`.
   - Social growth → `leadup-smm-growth-planner`.
   - Paid ads → `leadup-digital-ads-planner`.
   - Landing page conversion → `leadup-landing-page-cro-planner`.
   - Feature / roadmap → `leadup-feature-option-planner`.
   - Cross-cutting (audit, benchmark, "what to do") → run this skill.
3. **Pick sources** to consult; record what each source is expected to
   answer (use `references/growth-research-source-list.md`).
4. **Run research**; cite every claim with source + access date.
5. **Build the report** in the format below.
6. **Recommend** the single next LeadUp skill to run + the file shape it
   should produce.

Full source list: `references/growth-research-source-list.md`.
Report shape: `assets/growth-research-report.template.md`.

## Required output format

One Markdown report with these sections, in this order:

1. **Brief** — business, audience, market, goal, constraints, restated
   in one line.
2. **Classification** — single-skill or multi-skill; which skill(s) apply
   and why.
3. **Sources consulted** — table: source · what we asked · what we
   learned · confidence.
4. **Competitor summary** — 3–5 competitors, one block each (domain,
   what they do, top angle, gap to attack).
5. **Signal summary** — what's working / what's not in the category,
   based on the consulted sources.
6. **Strategy recommendation** — 3–5 specific moves, ordered by impact
   × cost.
7. **Assumptions** — explicit list of what was assumed.
8. **Data confidence** — verified / estimated / requires verification,
   per cell.
9. **Next action** — exactly ONE next LeadUp skill to run, with the
   file shape the user should expect from it.
10. **Hand-offs** — the wider chain (e.g. SEO → blog → CRO → ads).

## Safety rules

- Cite a **source + access date** for every claim that isn't general
  knowledge. If a claim can't be cited, mark **estimated** or **requires
  verification**.
- Do **not** invent traffic, market size, revenue, funding, or follower
  numbers.
- Do **not** copy competitor copy, designs, or trademarked material.
- Respect robots.txt, paywalls, terms of service, and copyright.
- Do **not** propose tactics that violate platform policy (ads,
  search engine spam, fake reviews, follower buying, scraping at scale).
- For regulated industries, flag every claim that needs legal review.
- Defer browser / search execution to `leadup-mcp-tool-orchestrator`
  when MCP is available.
- Defer the specific deliverable to the matched growth skill.
- Defer public copy polish to `leadup-human-content-editor`.

## Common mistakes

- Running this skill when the user wanted a single concrete deliverable
  (route to the matching growth skill directly).
- Citing sources but not dates (signals go stale).
- Producing 30 actions with no priority — the team can't ship 30.
- Inventing market-size or traffic numbers to look thorough.
- Skipping the assumptions block.
- Forgetting the "next single action" — research without a decision is
  noise.
- Copy/paste competitor positioning instead of identifying the user's
  honest gap.

## Troubleshooting

- **No browser / search MCP available**: document the manual research
  path step by step and what the user / agent should do offline.
- **User wants "research everything"**: scope it down — pick the top 3
  questions; deliver depth on those, not breadth on 30.
- **Highly regulated category**: research extra-cautious; flag every
  claim for compliance; do not propose tactics that need licences the
  user doesn't have.
- **Tiny team**: bias the next-action recommendation toward the highest
  leverage-per-hour skill (often `leadup-landing-page-cro-planner` or
  `leadup-seo-strategist`).
- **Brand new product, no audience yet**: lean on category + competitor
  research; flag user-side numbers as **requires verification** until
  the product has traffic.
- **The user is impatient**: deliver a 1-page version (brief +
  classification + 3 sources + next action), then offer the full report.

## Test prompts

### Should trigger (5)
1. "Do deep growth research for our salon booking SaaS."
2. "Research everything for our jewellery client — SEO, social, ads."
3. "What should we do for growth in the next 30 days?"
4. "Benchmark us against competitors in the dental SaaS space."
5. "Run internet research on the hostel-management software market."

### Should NOT trigger (3)
1. "Write one blog post on no-shows." (→ `leadup-blog-content-writer`)
2. "Audit our SEO." (→ `leadup-seo-strategist`)
3. "Plan a Google Ads campaign." (→ `leadup-digital-ads-planner`)

### Functional test cases (2)
1. Given "Indian salon booking SaaS, ₹50K/month total marketing budget,
   no existing analytics", return a report classifying the request as
   multi-skill, citing 5+ sources with access dates, summarizing 3
   competitors, listing assumptions, marking every numeric claim
   verified/estimated/requires verification, and recommending exactly
   ONE next LeadUp skill to run.
2. Given a single-skill request masquerading as research ("research
   how to write our about page"), correctly route to
   `leadup-blog-content-writer` (service page mode) or
   `leadup-client-document-generator`, decline to produce a full
   research report, and explain why.

## Success criteria

- Report has all 10 required sections in order.
- Every claim has a source + access date OR is labelled estimated /
  requires verification.
- 3–5 competitor blocks (not 20).
- Strategy recommendation has ≤ 5 moves, ordered by impact × cost.
- Exactly ONE next LeadUp skill recommended.
- Hand-off chain is explicit.
- No invented numbers, no copied competitor copy, no platform-policy
  tactics.
