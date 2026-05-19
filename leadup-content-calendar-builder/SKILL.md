---
name: leadup-content-calendar-builder
description: Build a social media content calendar and posting strategy for LeadUp or a client. Produces a dated schedule, per-platform strategy, hooks, captions, video/reel ideas, best publishing times, and a repurposing plan. Use when the user says "content calendar", "social media plan", "posting schedule", "reels ideas", "followers growth", "Instagram plan", or "LinkedIn plan".
---

# LeadUp Content Calendar Builder

## Purpose

Turn a goal (grow followers, promote a launch, fill a month) into a concrete,
dated content calendar with platform strategy, hooks, captions, video ideas,
optimal timing, and a repurposing plan LeadUp can execute.

## When to use

Trigger phrases: "content calendar", "social media plan", "posting schedule",
"reels ideas", "followers growth", "Instagram plan", "LinkedIn plan",
"content strategy for the launch", "what should we post this month".

This is marketing content planning — not app features. For client business
documents (proposals, reports) → `leadup-client-document-generator`.

## Inputs needed

- Whose account (LeadUp, or which client/brand) and the niche.
- Goal (awareness / leads / launch / followers) and timeframe.
- Platforms in scope (Instagram, LinkedIn, YouTube, X, etc.).
- Constraints: cadence, content types possible (reels, carousels, blogs),
  brand voice.

## Step-by-step workflow

1. **Clarify** brand, goal, timeframe, platforms, cadence, voice.
2. **Per-platform strategy**: content pillars, format mix, tone, what wins on
   each platform for this niche.
3. **Calendar**: a dated table for the timeframe — date | platform | pillar |
   format | hook | caption draft | CTA | asset needed.
4. **Hooks & captions**: strong scroll-stopping hooks; captions in brand voice;
   relevant hashtags/keywords.
5. **Video/reel ideas**: concrete concepts with a shot/idea outline.
6. **Best times**: recommended posting windows (note: validate against the
   account's own analytics if available).
7. **Repurposing plan**: one pillar piece → reels/carousel/post/short.
8. **Output** the calendar + strategy; suggest a review cadence.

## Required output format

1. **Strategy summary** — goal, platforms, pillars, cadence.
2. **Content calendar table** — dated rows as above.
3. **Hooks bank** — 10+ reusable hooks for the niche.
4. **Reel/video ideas** — concrete concepts.
5. **Posting times** — per platform, with the "verify with analytics" caveat.
6. **Repurposing flow** — pillar → derivatives.

## Safety rules

See `references/security-rules.md`. Most relevant here:
- No fabricated stats/claims about a client's product; mark assumptions.
- No private client data or secrets in public-facing captions.
- "Best times" are heuristics — flag that real analytics should confirm; do
  not present them as guaranteed.

## Common mistakes

- A vague monthly theme instead of dated, postable rows.
- Same content cross-posted with no per-platform adaptation.
- Hooks that describe instead of stop the scroll.
- Ignoring the actual goal (followers vs leads need different content).
- Inventing testimonials/metrics for a client.

## Troubleshooting

- **Under-triggers**: user said "we need to post more" — re-invoke; suggest
  trigger phrases.
- **Over-triggers** for a client proposal/report → route to
  `leadup-client-document-generator`.
- **Missing tool/MCP**: no trend/research access — use durable niche
  principles and mark trend items "verify".
- **No internet/browser**: deliver the calendar from fundamentals; flag
  timing/trends to validate later.
- **Missing inputs**: ask for brand, goal, platforms, timeframe before
  generating; don't guess the niche.
- **Build/test failure**: not applicable — if exporting, ensure the table is
  valid Markdown/CSV.

## Test prompts

### Should trigger (5)
1. "Build a 30-day Instagram content calendar for LeadUp."
2. "Social media plan to grow followers for the jewellery brand."
3. "Posting schedule + reels ideas for the salon client launch."
4. "LinkedIn plan for LeadUp to get agency leads."
5. "What should we post this month across IG and LinkedIn?"

### Should NOT trigger (3)
1. "Write a client proposal for the website project." (→ client-document-generator)
2. "Update STATUS.md." (→ status-updater)
3. "Make the marketing site UI premium." (→ premium-ui-upgrader)

### Functional test cases (2)
1. For "30-day IG calendar, goal = followers", output 30 dated rows with
   hook + caption + format + CTA per row.
2. Posting-time recommendations include the explicit "verify against the
   account's analytics" caveat.

## Success criteria

- Dated, postable calendar matching goal/timeframe/platforms.
- Per-platform strategy + hooks bank + reel ideas + repurposing flow.
- Timing flagged as heuristic; no fabricated client claims.
