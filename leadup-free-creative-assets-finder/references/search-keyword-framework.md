# Search Keyword Framework

Good asset search is a keyword problem. Build the keyword list before
opening any source — it cuts the time per asset by 5–10×.

## The 5-axis formula

For every search, combine terms from these 5 axes:

1. **Subject** — the literal thing in the asset.
   Examples: "server room", "appointment", "child reading", "credit card",
   "gold ring", "map", "happy customer", "team meeting".
2. **Style** — the visual treatment.
   Examples: "flat illustration", "line icon", "3d isometric",
   "hand-drawn", "minimalist", "isometric", "outline", "duotone",
   "watercolour", "photographic", "cinematic".
3. **Colour / palette** — brand-fit colour.
   Examples: "blue", "teal", "navy", "gold", "warm pastel", "monochrome",
   "purple gradient", "earth tones", "dark mode".
4. **Context / scene** — where it lives.
   Examples: "dashboard", "mobile app screen", "landing hero", "empty
   state", "onboarding", "pricing card", "blog header", "instagram
   reel".
5. **Brand / industry** — sector cue.
   Examples: "saas", "fintech", "ecommerce", "healthcare", "travel",
   "education", "real estate", "telecom", "hosting", "jewellery",
   "beauty", "salon".

A strong query uses 3–5 axes. Two-word queries are usually too broad.

## Examples (good ↔ bad)

**Bad:** "server"
**Good:** "server room blue cinematic data center" (Unsplash)

**Bad:** "icons"
**Good:** "dns ssl uptime line icon outline" (Lucide / Iconify search)

**Bad:** "kids"
**Good:** "child reading book flat illustration warm pastel" (Storyset
/ unDraw)

**Bad:** "appointment"
**Good:** "calendar appointment booking flat illustration soft pink"
(Storyset)

**Bad:** "loading"
**Good:** "loading spinner lottie minimal blue" (LottieFiles)

## Source-specific keyword tips

- **Unsplash / Pexels / Pixabay** — they index well on subject + scene;
  add "minimal", "candid", "natural light" to filter out the
  over-staged stock look.
- **unDraw** — search by topic; recolour to brand via the site's
  built-in colour control.
- **Storyset** — search by topic; many illustrations come as a
  "scene + character" set, useful for empty states + onboarding.
- **Iconify / Lucide / Tabler** — search by literal noun ("dns", "ssl",
  "cart", "bookmark", "shield"); browse by category if no exact match.
- **LottieFiles** — search by subject + animation type ("loading",
  "success", "confetti", "drag", "drop"); filter to "Free" +
  "Commercial OK".
- **Sketchfab** — search by subject + filter "Downloadable" + "CC0 /
  CC-BY".
- **Spline Community** — search by subject + style ("3d ring", "3d
  isometric server"); verify licence per file.
- **DiceBear** — pick a *style* first (lorelei, bottts, identicon,
  initials), then seed by user id.
- **Pexels Videos / Coverr** — search by subject + duration; filter to
  short loops for hero.

## Negative keywords

Add to the brief so the user knows what to avoid:

- "watermark" / "preview" / "sample" — flags low-quality scraped
  copies.
- "lorem ipsum" / "dummy text" / "placeholder text" — for mockups
  that bleed into final designs.
- "AI generated" — if the brand wants real / human-made.
- "low resolution" — for hero placements.
- "studio set" — if the brand wants candid feel.
- "vintage filter" — if the brand looks modern.

## Brand-fit keyword cheatsheet (LeadUp projects)

- **Hostendor:** server, data center, cloud, dns, ssl, uptime, network,
  rack, blue, teal, dark, technical, cinematic.
- **LeadUp website:** agency, team, meeting, web design, saas
  dashboard, modern, clean, neutral, professional.
- **Jewellery SaaS:** gold ring, necklace, billing, inventory, gst,
  warm, premium, soft, minimal.
- **Salon SaaS:** salon, hair, appointment, calendar, beauty, soft,
  pastel, rounded.
- **BRC-Buddy:** child, kid, school, therapy, activity, reading,
  drawing, friendly, warm, illustration (no photos).
- **INET CRM:** telecom, pipeline, customer, deal, dashboard, b2b,
  structured, blue, neutral.
- **Trivasia:** travel, destination, beach, mountain, flight, package,
  map, weather, vibrant.

## Keyword-building workflow

1. Write the brief in one sentence.
2. Extract the **subject** noun.
3. Pick the **style** from the brand's existing UI.
4. Pick the **colour** from the brand's palette.
5. Add the **context** (where it'll live).
6. Add the **brand / industry** cue.
7. Add **negatives** for the source.
8. Build 6–15 keyword combinations across the 5 axes.
9. Run the queries on the source; pick the best 3–5 candidates; score.

## Quality filters at search time

While searching:
- Reject anything **watermarked** in preview (most paid-tier markers).
- Reject anything where the **subject is off** (close enough is not
  enough).
- Reject anything with **identifiable people** unless the surface
  allows release risk and the source's licence covers it.
- Reject anything that looks **AI-generated** if the brand prefers
  real / human-made — surface AI suspicion in risk notes.
- Reject anything **too generic** (the "businessman in suit" effect)
  if the brand can afford something specific.

Save the final picks with their direct URLs so the output is
reproducible.
