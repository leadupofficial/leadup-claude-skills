---
name: leadup-smm-growth-planner
description: Build a 30-day social media growth plan for a LeadUp client or SaaS across Instagram, LinkedIn, X/Twitter, YouTube Shorts, and WhatsApp broadcast, with content pillars, reels ideas, hooks, captions, posting schedule, engagement plan, and KPI tracking tuned for Indian and international audiences. Use when the user says "smm plan", "social media growth", "instagram strategy", "followers growth", "posting time", "reels plan", or "linkedin strategy".
---

# LeadUp SMM Growth Planner

## Purpose

Produce a complete social media growth plan: platform strategy, content
pillars, a 30-day calendar with reels and post ideas, hooks, caption
patterns, posting schedule, engagement plan, and the KPIs to track.
Designed for LeadUp client businesses (salons, clinics, jewellery,
schools, restaurants, etc.) and LeadUp's own SaaS marketing.

## When to use

Use when the user wants a social media strategy or calendar built. Do
**not** trigger for paid ads (use `leadup-digital-ads-planner`), a single
blog post (use `leadup-blog-content-writer`), or content for an existing
calendar already created by `leadup-content-calendar-builder` (the
existing core-pack skill — they complement each other; this one is the
growth/strategy planner).

Trigger phrases: "smm plan", "social media growth", "instagram strategy",
"followers growth", "posting time", "reels plan", "linkedin strategy",
"social media 30 day plan", "grow our instagram".

## Inputs needed

- Business / product description.
- Target audience (city, age, role, language).
- Current social presence (handles, follower bands, engagement state).
- Top 3 competitors' handles.
- Platforms to focus (Instagram, LinkedIn, X/Twitter, YouTube Shorts,
  WhatsApp).
- Goal: awareness, leads, bookings, signups, retention.
- Posting capacity (how many posts per week the team can ship).
- Banned items: claims, competitor mentions, sensitive topics.

Ask at most 2 clarifying questions if goal or capacity is unclear.

## Required resources

- **Native analytics**: Instagram Insights, LinkedIn analytics, YouTube
  Studio, X analytics.
- **Public signals**: competitor handles, hashtag explorer, trending
  reels, Google Trends for topic seasonality.
- **Tools (if available)**: Meta Business Suite, Buffer, Later, Notion,
  Google Sheets for the calendar.
- **LeadUp memory**: prior content calendars and what performed.
- Final caption polish: `leadup-human-content-editor` to keep tone human.

## Internet research workflow

1. Confirm the audience and the platform mix that fits them (e.g. salons
   → Instagram + WhatsApp; B2B SaaS → LinkedIn + X).
2. Look at the user's last 30 days of posts (handles or screenshots):
   pillar mix, hooks, post types, engagement bands.
3. Look at 3 competitors: post cadence, top-performing post type, hooks,
   hashtag patterns.
4. Pull 5–10 trending hooks / reel formats for the niche (Instagram
   Explore, YouTube Shorts trending, LinkedIn top posts).
5. Note assumptions and which numbers are **verified** (from native
   analytics) vs **estimated** (eyeballed from public posts).

If a browser or social MCP is available, hand off to
`leadup-mcp-tool-orchestrator`.

## Step-by-step workflow

1. **Restate brief** in one line (audience, goal, capacity).
2. **Platform strategy**: pick the 1–3 platforms with the best
   audience-fit + capacity ratio. Say why per platform.
3. **Content pillars**: 4–6 pillars (e.g. Education, Behind-the-scenes,
   Social proof, Offers, Community, Product). Each pillar gets a % of
   the calendar.
4. **30-day calendar**: 3–5 posts/week per chosen platform. Each entry:
   date, platform, format (reel/carousel/static/story/short/post), pillar,
   hook, caption draft, hashtags, CTA, asset note.
5. **Reels / Shorts ideas**: 8–12 specific concepts with hooks for the
   month.
6. **Hooks library**: 15–25 hook patterns the team can reuse.
7. **Caption patterns**: 3–5 caption templates (story → insight → CTA,
   list → CTA, contrarian → reframe, etc.).
8. **Posting schedule**: per-platform best times based on the niche +
   audience timezone (state the source / reasoning).
9. **Engagement plan**: comments, DMs, story replies, collabs, UGC
   prompts — what the team does in the first 60 minutes after posting.
10. **KPIs**: 4–6 metrics with target bands and where to read them.

Full framework: `references/smm-framework.md`.
Calendar shape: `assets/content-calendar.template.md`.

## Required output format

One Markdown plan with these sections, in this order:

1. **Brief** — business, audience, goal, capacity, platforms chosen.
2. **Platform strategy** — table: platform · audience-fit · format · why.
3. **Content pillars** — pillar · % of calendar · sample topic.
4. **30-day calendar** — table with date, platform, format, pillar, hook,
   caption, hashtags, CTA, asset note. (CSV shape via
   `assets/content-calendar.template.md`.)
5. **Reels / Shorts ideas** — 8–12 specific concepts with hooks.
6. **Hooks library** — 15–25 reusable hook patterns.
7. **Caption patterns** — 3–5 templates with examples.
8. **Posting schedule** — per platform, with source/reasoning for times.
9. **Engagement plan** — first 60 minutes, weekly rituals, DM script.
10. **KPIs** — 4–6 metrics with target bands and where to read.
11. **Assumptions and data confidence** — verified vs estimated vs
    requires verification.

Defer caption polish to `leadup-human-content-editor`.

## Safety rules

- Do **not** invent follower counts, reach, engagement %, or growth
  numbers. Use bands and label as **verified** (from native analytics)
  or **estimated**.
- Do **not** promise specific follower growth ("10K in 30 days"). Frame
  targets as **plan-driven bands** with assumptions.
- Do **not** copy competitor captions or steal creator content; reference
  patterns only.
- Avoid platform-policy risk: no engagement pods, no fake giveaways
  ("follow + tag 10 friends for cash"), no buy-followers, no shadow-bots.
- Respect copyright and music licensing on reels.
- For regulated industries (health, finance, alcohol, gambling, real
  estate), flag claims for legal review.
- For India audience: clear international English (or vernacular where
  appropriate); avoid Indian-English filler unless the brand uses it.
- Defer integrations to `leadup-api-research-builder`; defer browser /
  search tooling to `leadup-mcp-tool-orchestrator`; defer caption polish
  to `leadup-human-content-editor`.

## Common mistakes

- Calendar with no pillar mix — every post the same type.
- 7 posts/week when the team can only ship 3.
- Hooks that all start with "Did you know…".
- Hashtag stuffing (30 hashtags, all huge).
- Ignoring stories and DMs (where the actual conversion happens).
- Promising growth numbers ("10K followers in 30 days").
- Treating LinkedIn and Instagram the same way.
- Forgetting that Indian audiences over-index on Reels and WhatsApp,
  while global B2B over-indexes on LinkedIn and X.

## Troubleshooting

- **No analytics access**: deliver plan with **estimated** KPIs; list the
  native analytics screens to check to upgrade to **verified**.
- **Tiny team / 1 post per week**: build a 4-post plan instead of 30;
  prioritize the highest-leverage pillar.
- **Highly regulated industry**: cap claims; flag every promotional post
  for compliance review.
- **Multi-location business**: split the calendar by location-specific
  pillars; consider one master account vs per-location accounts.
- **Pure B2B SaaS**: drop Instagram unless the buyer is on it; focus
  LinkedIn + X + YouTube.
- **User wants only Reels**: deliver a Reels-only 30-day plan with hooks
  and shot lists; flag what gets left on the table.

## Test prompts

### Should trigger (5)
1. "Build a 30-day Instagram + LinkedIn plan for our SaaS."
2. "SMM plan for a jewellery client in Coimbatore."
3. "Reels strategy for a dental clinic targeting tier-2 India."
4. "LinkedIn strategy for our B2B booking tool."
5. "How do we grow our salon client's Instagram?"

### Should NOT trigger (3)
1. "Run a Meta Ads campaign for bookings." (→ `leadup-digital-ads-planner`)
2. "Write one blog post on no-shows." (→ `leadup-blog-content-writer`)
3. "Audit our website's SEO." (→ `leadup-seo-strategist`)

### Functional test cases (2)
1. Given "salon in Coimbatore, 1 person can post 4× a week, Instagram +
   WhatsApp only", return a 30-day calendar with 16–20 posts, 4–6
   content pillars, 8–12 Reels ideas with hooks, a posting schedule
   sourced from IST audience activity, and KPIs with target bands.
2. Given a B2B SaaS targeting global founders, return a LinkedIn + X
   plan with no Instagram, content pillars weighted toward education
   and product, a 30-day calendar of 12–16 posts, and KPIs labelled
   **estimated** until native analytics confirm them.

## Success criteria

- Plan has all 11 required sections in order.
- Calendar matches the team's stated posting capacity.
- Pillars sum to 100% with sample topics each.
- 8–12 Reels/Shorts ideas with explicit hooks.
- Posting schedule is sourced/reasoned, not generic "9am, 12pm, 6pm".
- KPIs are bands, not invented numbers.
- Engagement plan covers the first 60 minutes after posting + weekly
  rituals + DM script.
- No platform-policy-risky tactics anywhere in the plan.
