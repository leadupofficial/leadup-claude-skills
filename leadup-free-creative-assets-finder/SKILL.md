---
name: leadup-free-creative-assets-finder
description: Find free or safe-to-use creative assets (photos, stock images, vectors, illustrations, icons, animated icons, Lottie animations, GIFs, stickers, 3D models, 3D icons, video clips, emojis, avatars, sound effects, music) for LeadUp websites, SaaS apps, admin panels, Flutter apps, social media, ads, blogs, proposals, and client projects. Verifies licenses for commercial use, attribution, modification, and redistribution before recommending. Use when the user says "free images", "find free assets", "free vector", "free icons", "free animation", "free lottie", "free gif", "free 3d", "free video clip", "free avatar", "free emoji", "asset finder", "design resources", "website assets", "social media assets", "hero image", "illustration for website", "icons for SaaS", "stock video for ad", or "free creative sources".
---

# LeadUp Free Creative Assets Finder

## Purpose

Help a LeadUp team member find free or safe-to-use creative assets (photos,
stock images, vectors, illustrations, icons, animated icons, Lottie
animations, GIFs, stickers, 3D models, 3D icons, video clips, emojis,
avatars, sound effects, background music) for client websites, SaaS
products, admin panels, Flutter apps, social posts, ads, blogs, proposals,
and project pages — with the **license verified** for commercial use,
attribution, modification, and redistribution before recommending.

The output is a ready-to-act asset plan: best source categories, search
keywords, a candidate sources table, license + attribution notes, format
recommendation, implementation + performance notes, a single best
recommendation, backup sources, and risk flags.

## When to use

Trigger when the user needs creative media for a LeadUp project and asks
for free / royalty-free / safe-to-use sources, or names a specific asset
type with no source picked yet.

Trigger phrases: "free images", "find free assets", "free vector", "free
icons", "free animation", "free lottie", "free gif", "free 3d", "free
video clip", "free avatar", "free emoji", "asset finder", "design
resources", "website assets", "social media assets", "hero image",
"illustration for website", "icons for SaaS", "stock video for ad",
"free creative sources".

Do **not** trigger when:
- The user has a specific paid stock account (Shutterstock, Envato,
  Storyblocks, Adobe Stock) and just wants picks from there.
- The user wants you to *generate* an image with AI (use the matching
  generation skill / tool, not this finder).
- The user is asking for brand logos/trademarks they do not own.
- The user wants UI design system review (use
  `leadup-premium-ui-upgrader`) or full design system creation.

## Inputs needed

Ask at most 2 clarifying questions. Defaults are noted.

Required:
- **Asset type** — photo / illustration / icon / animated icon / Lottie /
  GIF / sticker / 3D model / 3D icon / video clip / emoji / avatar /
  sound / music.
- **Use surface** — website hero, landing section, blog header, SaaS
  empty state, dashboard icon set, admin panel, Flutter app screen,
  Instagram reel, Meta ad creative, LinkedIn post, YouTube thumbnail,
  proposal PDF, client report, etc.
- **Project/brand context** — LeadUp project name (Hostendor, Trivasia,
  Jewellery SaaS, Salon SaaS, BRC-Buddy, INET CRM, etc.) or a one-line
  description.

Helpful (assume if unstated):
- **Style direction** — flat / 3D / line / isometric / hand-drawn /
  realistic / photographic / minimal / colourful.
- **Colour or brand palette** — hex codes or "match brand".
- **Format needed** — PNG, SVG, WebP, AVIF, JSON (Lottie), MP4, WebM,
  GLB, OBJ. Default: SVG for icons/illustrations, WebP for photos,
  Lottie JSON for animations, WebM/MP4 for video, GLB for 3D.
- **Quantity** — single hero, set of 12 icons, a series of 5
  illustrations, etc.
- **Commercial use** — assume **yes** for any LeadUp / client work.
- **Attribution allowed?** — for paid client work, default to
  **no-attribution preferred**. Flag if only attribution-required
  sources fit.
- **Aspect / size** — e.g. 1920x1080 hero, 1080x1080 IG, 1080x1920 reel,
  16:9 YouTube thumbnail, 24x24 / 48x48 icon, A4 PDF cover.

Default mode if nothing is stated: "website / SaaS use, commercial,
no-attribution preferred, modern flat style, SVG / WebP / Lottie".

## Source/resource strategy

Always prefer sources with a clear, permissive license over scraping or
hot-linking. Full source matrix and license notes live in
`references/free-asset-source-list.md`. Summary by asset type:

**Photos / stock images** — Unsplash, Pexels, Pixabay, Wikimedia Commons,
Openverse.

**Videos / video clips** — Pexels Videos, Pixabay Videos, Coverr, Mixkit,
Videvo.

**Illustrations / vectors** — unDraw, Storyset, SVG Repo, Open Doodles,
ManyPixels Gallery, IRA Design.

**Icons** — Iconify, Lucide, Heroicons, Tabler Icons, Feather Icons,
Remix Icon, Phosphor Icons, Bootstrap Icons, Material Symbols.

**Animations (Lottie / animated icons)** — LottieFiles, Lordicon,
useAnimations, Potlab Icons, IconScout free assets.

**3D models / 3D icons** — Pixabay 3D Models, IconScout 3D Icons, Spline
Community, Sketchfab (free downloadable filter), BlenderKit free assets.

**Avatars** — DiceBear, Boring Avatars, Avataaars, UI Avatars.

**Emojis** — native Unicode emoji, Twemoji, OpenMoji, Noto Emoji.

**GIFs / stickers** — Pixabay GIFs, GIPHY, Tenor, LottieFiles GIF
exports.

**Sound effects / music** (only if asked) — Pixabay Music, Free Music
Archive, YouTube Audio Library, Freesound (per-track license).

Source selection rules:
- Prefer official source sites over mirrors / re-uploads.
- Prefer CC0, public domain, or "free for commercial use, no
  attribution" first.
- For icons, prefer open-source icon sets with MIT / ISC / Apache 2.0
  licenses (Lucide, Heroicons, Tabler, Feather, Phosphor, Remix,
  Bootstrap Icons, Material Symbols).
- For illustrations, prefer MIT / CC0 sets (unDraw, Open Doodles) where
  possible.
- For 3D, prefer CC0 / CC-BY filters explicitly enabled.
- When a source is gated by sign-in or paid tier for full quality,
  surface that clearly — do **not** suggest scraping watermarked
  previews.

## Step-by-step workflow

1. **Read the brief.** Capture: project, surface, asset type, style,
   quantity, format, aspect, commercial use, attribution preference.
2. **Pick source categories** for the asset type from the matrix above.
   Choose 3–6 candidate sources to compare; do not dump the whole list.
3. **Build search keywords** using
   `references/search-keyword-framework.md`: include subject + style +
   colour + context terms, and a "negative" list (things to avoid like
   "watermark", "lorem ipsum", "AI generated" when the brand wants real).
4. **Check format fit** against `references/asset-format-guide.md`
   (SVG / PNG / WebP / AVIF / JPG / Lottie JSON / GIF / WebM / MP4 / GLB
   / OBJ / FBX). Flag mismatch (e.g. PNG for a hero — prefer WebP).
5. **Verify license** for each candidate source using
   `references/license-checklist.md` and the "License verification
   workflow" below.
6. **Score** each candidate using the scoring framework.
7. **Decide** the single best recommendation and 2 backups.
8. **Add implementation + performance notes** using
   `references/performance-optimization-guide.md` (sizes, formats,
   loading strategy, srcset, Lottie weight, video poster).
9. **Output** in the required format. Always include risk notes for any
   unclear license, attribution requirement, or model/property release
   risk.

## License verification workflow

For every recommended source/asset, check and report:

1. **Source license page** — find the official license / terms URL on
   the source site itself, not a blog post about it.
2. **Commercial use** — explicitly allowed for paid client work? If
   unclear, mark **Needs license verification**.
3. **Attribution** — required? If required, capture the exact required
   credit format (name + link). If the project cannot show attribution
   (e.g. a logo, a hero with no caption space), prefer a no-attribution
   source.
4. **Modification** — allowed to crop, recolour, composite, animate?
   Some sources allow display but not derivative works.
5. **Redistribution / resale** — most free sources forbid resale of the
   asset itself (e.g. you cannot sell the Unsplash photo as a print or
   in a stock pack). Flag this for proposal / template products.
6. **Use in logos / trademarks** — most free sources forbid use in
   client logos or trademark marks. Flag this clearly.
7. **People & property releases** — for photos containing
   identifiable people, recognisable buildings, branded products, or
   art: flag model / property release risk. Do **not** assume the
   source has cleared releases unless its license explicitly states it.
8. **API / programmatic use** — if the user wants to pull via API
   (Unsplash, Pexels, GIPHY, Tenor, Iconify, LottieFiles, DiceBear),
   note API key requirements, rate limits, attribution/branding rules,
   and TOS limits.
9. **Mass-download / scraping** — never recommend bulk scraping a
   source against its TOS, even if the assets are individually free.
10. **Unclear cases** — if any of the above is ambiguous after one good
    check, mark the asset/source as **Needs license verification** and
    surface it in the risk notes. Do not claim safety you cannot
    confirm.

Full checklist with per-source notes is in
`references/license-checklist.md`.

## Asset scoring framework

Score each candidate source/asset on a 1–5 scale (5 = best) for:

- **Visual fit** — matches required style, mood, palette.
- **License clarity** — explicit, easy-to-read commercial terms.
- **Commercial safety** — safe for paid client work without future risk
  (attribution, redistribution, trademarks, releases).
- **Format availability** — SVG/PNG/WebP/AVIF/Lottie/MP4/WebM/GLB as
  needed; vector preferred where it applies.
- **Performance impact** — file weight, loading strategy, mobile cost.
- **Customization ability** — recolour, resize, edit, animate.
- **Implementation ease** — drop-in component library (e.g. Lucide React),
  CDN availability, copy-paste embed.
- **Brand fit** — matches LeadUp / target client brand (trust + clarity
  for business; friendly + soft for jewellery, salon, BRC-Buddy; clean +
  technical for Hostendor, INET CRM).

Recommendation rules:
- Top pick must score **≥ 4** on visual fit, license clarity, commercial
  safety, and brand fit.
- If no candidate scores ≥ 4 on commercial safety, do **not** recommend
  — output a "Needs license verification" entry and stop.
- Tiebreaker order: license clarity → commercial safety → format
  availability → performance → visual fit.

## Required output format

Return a single Markdown block with these sections, in this order:

1. **Requirement summary** — 4–8 lines restating the brief (project,
   surface, asset type, style, quantity, format, aspect, attribution
   preference).
2. **Best source categories** — 2–4 bullets, e.g. "Open-source SVG icon
   sets" + "Illustration libraries with MIT/CC0".
3. **Search keywords to use** — 6–15 keyword phrases including subject,
   style, colour, context, and negatives.
4. **Candidate sources table** — Markdown table with columns: Source ·
   Asset Type · License Summary · Attribution · Commercial Use ·
   Modification · Format · Score (sum or weighted) · Notes.
5. **License and attribution notes** — per recommended source: license
   name, URL of the official terms (label `[official terms]`), required
   credit format (if any), and restrictions (trademarks, releases,
   redistribution).
6. **Recommended asset format** — single best format and reason; fallback
   format if browser/app support is a concern.
7. **Implementation notes for website / app / social** — where the asset
   goes, component / tag to use, lazy-load, responsive sizes, caching,
   accessibility (alt text, aria-label, captions, reduced-motion).
8. **Performance optimization notes** — target weight (e.g. hero
   ≤ 200 KB WebP, Lottie ≤ 50 KB JSON, video ≤ 1.5 MB with poster), CDN,
   `loading="lazy"`, `decoding="async"`, `prefers-reduced-motion`.
9. **Best final recommendation** — exactly one pick, with the search
   keywords to use on that source, and what to do if nothing fits.
10. **Backup source recommendations** — 2 alternatives in priority order.
11. **Risk notes** — anything unclear, any "Needs license verification"
    flags, any model/property release risk, any API/TOS limit, any
    attribution that the project cannot show.

Use the asset template in `assets/asset-search-brief.template.md` and the
comparison table in `assets/asset-comparison-table.template.md` as the
output shape. License capture is in `assets/license-check.template.md`.
For website-heavy briefs, use `assets/website-asset-plan.template.md`;
for social, use `assets/social-asset-plan.template.md`.

## Safety rules

- **Never claim safety you cannot confirm.** If license terms are
  ambiguous after a reasonable check, label the candidate **Needs
  license verification** and explain why.
- **Do not assume "free" means "commercial-safe".** Many free sources
  forbid resale, trademarks, or use in client logos.
- **Always check attribution.** For client websites and ads, default to
  no-attribution sources. If attribution is required, include the exact
  required credit text and where to place it.
- **Flag people / property release risk** for photos with identifiable
  people, branded products, recognisable buildings, or artwork. Do not
  assume releases are cleared.
- **Do not recommend copyrighted brand assets** (logos, mascots, game
  characters, film stills, sports team marks, celebrity faces) unless
  the user owns the rights or has a licensed source.
- **No scraping / mass-download against TOS.** Even if individual assets
  are free, bulk-pulling against site terms is not allowed.
- **No hot-linking** from third-party sites — recommend downloading +
  serving from the project's own CDN / storage.
- **API use rules** — surface API key requirements, rate limits, and
  required brand display (Unsplash, Pexels, GIPHY, Tenor, etc.).
- **Trademark / logo use** — most free sources forbid use in a logo or
  trademark; flag for any client where the asset goes into branding.
- **AI-generated assets** — if a source mixes AI-generated content,
  flag it; some clients reject AI content, and license + IP status of
  AI content varies.
- **Children / sensitive contexts** (e.g. BRC-Buddy) — prefer
  illustrations and avatars over real-child photos; flag any photo that
  shows identifiable children.
- **Stickers / GIFs with watermarks** — do not recommend assets where
  the source platform's watermark is baked in (e.g. some GIPHY brand
  watermarks) for paid client work.
- **Music / sound** — confirm both the audio license and any platform
  rights (e.g. YouTube Content ID) before recommending for ads / reels.

## Performance rules

- **Photos:** WebP or AVIF first, JPG fallback. Hero ≤ 200 KB target,
  body images ≤ 80 KB. Use `srcset` + `sizes` for responsive. Always
  set explicit `width` / `height` to avoid CLS.
- **Vectors / icons:** SVG. Inline for small sets that need styling, or
  via a component library (Lucide, Tabler, Heroicons). Sprite for many
  static icons. Use `aria-hidden="true"` on decorative.
- **Illustrations:** SVG for flat / line; WebP for raster. Compress
  with SVGO. Avoid 2 MB SVGs from generic exporters — strip metadata
  and IDs.
- **Animations:** Lottie JSON first (≤ 50 KB target). Fall back to MP4
  / WebM for complex 3D motion. Honour `prefers-reduced-motion`.
- **GIFs:** Avoid for anything large — convert to MP4 / WebM (5–20×
  smaller). Reserve GIFs for messaging / WhatsApp / proposal docs.
- **Video:** WebM (VP9 / AV1) with MP4 (H.264) fallback. Use `poster`,
  `playsinline`, `muted`, and `preload="metadata"`. Hero loops ≤ 1.5 MB.
- **3D:** GLB (binary glTF) preferred; compress with Draco / Meshopt.
  Lazy-load 3D scenes; warn that 3D is heavy on low-end mobile.
- **Avatars:** Use SVG generators (DiceBear, Boring Avatars) and seed
  them deterministically so the same user always gets the same avatar.
- **Emojis:** Use native first (no payload). Use Twemoji / OpenMoji
  only when cross-platform consistency is required.
- **Loading strategy:** `loading="lazy"` for below-the-fold,
  `decoding="async"` for images, `fetchpriority="high"` only for the
  LCP image. Preload hero image when needed.
- **Accessibility:** every image needs `alt`; decorative icons get
  `aria-hidden="true"`; videos need captions when there is speech;
  animations honour reduced-motion.

Full checklist in `references/performance-optimization-guide.md`.

## Common mistakes

- Recommending a source as "free" without checking its actual license.
- Missing the attribution requirement and shipping client work without
  the required credit.
- Suggesting Google Image Search results (these are not licensed).
- Using a logo / brand mark / celebrity / film still without rights.
- Hot-linking from Unsplash / Pexels / Pixabay instead of downloading
  and serving from the project's storage.
- Recommending GIPHY-watermarked GIFs for paid client websites or ads.
- Choosing PNG for a hero image instead of WebP / AVIF.
- Choosing a heavy Lottie (≥ 200 KB) for a small UI accent.
- Choosing a generic stock photo instead of an illustration when the
  brand needs a unique, ownable feel.
- Choosing an icon set that does not match the visual weight of the
  rest of the UI (mixing Heroicons and Material Symbols randomly).
- Picking a 3D model that is too high-poly for mobile.
- Forgetting model / property release risk for photos with people or
  branded products.
- Recommending real-child photos for BRC-Buddy or any children-related
  surface (use illustrations / safe avatars).
- Failing to flag a source as "Needs license verification" when the
  terms page is missing or ambiguous.
- Returning 30 sources without scoring or a single recommendation.

## Troubleshooting

- **Under-triggers**: user asked for "background image for a section"
  and the skill did not fire — re-invoke and surface trigger phrases.
- **Over-triggers**: user wanted full UI design or design system → route
  to `leadup-premium-ui-upgrader`. User wanted AI-generated images →
  route to the matching generation tool.
- **No source fits**: if no candidate scores ≥ 4 on commercial safety
  and brand fit, say so explicitly and recommend either commissioning
  the asset or buying from a paid stock site (note the user's existing
  Shutterstock / Envato / Adobe Stock if relevant).
- **License page unreachable**: mark **Needs license verification** and
  do not claim safety. Suggest the user verify directly on the source.
- **Identifiable people in photos**: flag release risk; prefer an
  illustration alternative or a photo of hands / objects / scenes.
- **Children-sensitive surfaces (BRC-Buddy, kids products)**: default
  to illustrations and safe avatars; never recommend real-child photos.
- **Cross-asset consistency**: when the brief needs many assets (full
  icon set, illustration series), recommend sticking to a single source
  / family for visual consistency.
- **Brand colour mismatch**: prefer SVG / Lottie so colours can be
  edited; raster images are harder to recolour and may need a paid
  alternative.
- **Quota / rate limit hit on API** (Unsplash, Pexels, GIPHY): suggest
  caching to the project CDN and respecting the source's brand-display
  rules.

## Test prompts

### Should trigger (5)
1. "Find free icons for our Hostendor admin dashboard — need a 24-icon
   set, SVG, MIT-licensed if possible, matching a clean technical look."
2. "I need a free hero illustration for the LeadUp website services page
   — flat style, blue/teal palette, no attribution preferred."
3. "Find free Lottie animations for the Salon SaaS onboarding screen,
   under 50 KB each, friendly tone."
4. "Where can I get free stock video clips for a Trivasia travel ad on
   Instagram reels, vertical 1080x1920?"
5. "Need free 3D icons for the INET CRM pricing page, isometric style,
   commercial use safe."

### Should NOT trigger (3)
1. "Upgrade the UI of our admin panel to look premium." (→
   `leadup-premium-ui-upgrader`)
2. "Generate a custom hero image with AI for the jewellery SaaS." (AI
   image generation, not a free-asset finder.)
3. "Add the Mercedes-Benz logo to our client deck." (Copyrighted brand
   mark — refuse / out of scope.)

### Functional test cases (2)
1. Given a brief: "free hero illustration for Hostendor website, flat
   style, blue palette, commercial use, no attribution", return a
   Markdown report with all 11 output sections, a candidate sources
   table with at least 3 sources (e.g. unDraw / Storyset / SVG Repo)
   scored on the 8-criterion framework, a single best recommendation
   that scores ≥ 4 on visual fit, license clarity, commercial safety,
   and brand fit, 2 backups, performance notes targeting SVG with
   gzip / brotli, and at least one risk note if any candidate has
   unclear redistribution / trademark terms.
2. Given a brief: "free stock photo with identifiable people for a
   Salon SaaS landing hero", return the report and explicitly flag
   model release risk in the Risk notes section, suggest an
   illustration alternative (Storyset / unDraw) if release risk is too
   high, and do **not** mark the photo as commercially safe unless the
   source's license explicitly covers model release.

## Success criteria

- Output contains all 11 required output sections, in order.
- Every recommended source has its license verified against the
  checklist; ambiguous cases are labelled "Needs license verification".
- The top pick scores ≥ 4 on visual fit, license clarity, commercial
  safety, and brand fit, or no top pick is given.
- Attribution requirements, redistribution limits, trademark/logo
  limits, and model/property release risks are surfaced — never hidden.
- Format and performance notes match the surface (SVG / WebP / Lottie /
  WebM / GLB) and include weight targets and loading strategy.
- No copyrighted brand assets, no real-child photos in
  children-sensitive contexts, no GIPHY-watermarked content for paid
  client surfaces, no hot-linking advice.
- Output is copy-paste-ready for a LeadUp project page or proposal.
