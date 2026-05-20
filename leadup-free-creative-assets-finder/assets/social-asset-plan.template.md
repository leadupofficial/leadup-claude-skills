# Social Asset Plan — [PROJECT_NAME] · [CAMPAIGN / MONTH]

Per-platform asset plan for a LeadUp social campaign. One row per
planned post; format and weight tied to the platform spec.

## 0. Campaign snapshot

- **Project:** [Hostendor / Trivasia / Salon SaaS / LeadUp / ...]
- **Period:** [e.g. May 2026, 30-day plan]
- **Pillars / themes:** [education / behind-the-scenes / case study /
  product / offer]
- **Tone:** [premium / friendly / technical / playful]
- **Hashtag set:** [#leadup #hostendor ...]
- **Attribution preference:** No-attribution preferred for ad creatives;
  attribution acceptable for organic posts only if it fits the caption.

## 1. Platform format cheatsheet

| Platform | Surface | Aspect | Size | Notes |
|---|---|---|---|---|
| Instagram | Reel / Story | 9:16 | 1080×1920 | ≤ 60 s; safe-zone for UI overlays |
| Instagram | Feed post | 1:1 | 1080×1080 | text legible at thumbnail |
| Instagram | Carousel | 4:5 | 1080×1350 | per-slide weight ≤ 1 MB |
| Facebook | Feed photo | 1.91:1 | 1200×630 | safe-zone away from edges |
| Facebook | Reel / Story | 9:16 | 1080×1920 | same as IG |
| LinkedIn | Feed post | 1.91:1 | 1200×627 | clean type, business tone |
| LinkedIn | Document | 4:5 | 1080×1350 | minimal animation |
| YouTube | Thumbnail | 16:9 | 1280×720 | text legible at 320×180 |
| YouTube | Shorts | 9:16 | 1080×1920 | ≤ 60 s |
| X / Twitter | Image post | 16:9 | 1600×900 | ≤ 5 MB |
| WhatsApp | Status | 9:16 | 1080×1920 | low bandwidth — compress hard |
| WhatsApp | Sticker | 1:1 | 512×512 WebP | ≤ 100 KB |

## 2. Post-by-post plan

| Day | Platform | Surface | Theme | Asset type | Source pick | Format | Size | Weight target | License | Caption / hook | Notes |
|----|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IG | Reel | Education | Stock b-roll + Lottie text | Pexels Videos + LottieFiles | MP4 + JSON | 1080×1920 | ≤ 5 MB total | Pexels + LottieFiles Free | [hook] | reduced-motion text |
| 2 | LinkedIn | Feed | Case study | Custom illustration | unDraw | SVG export → PNG | 1200×627 | ≤ 80 KB | unDraw License | [hook] | brand colour |
| 3 | IG | Carousel | Product walkthrough | UI screenshots + icons | client + Lucide | WebP + SVG | 1080×1350 | ≤ 800 KB / slide | client + MIT | [hook] | strip PII |
| 4 | YouTube | Thumbnail | Tutorial | Photo + icon + text | Unsplash + Tabler | WebP | 1280×720 | ≤ 80 KB | Unsplash + MIT | [title] | text legible @ 320×180 |
| 5 | WhatsApp | Status | Offer | Static graphic | Pixabay + Lucide | WebP | 1080×1920 | ≤ 200 KB | Pixabay + MIT | [hook] | compress hard |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

## 3. Reusable asset kit (build once, use across posts)

| Asset | Source | Format | Where used |
|---|---|---|---|
| Brand colour palette swatches | brand kit | SVG | every slide |
| Logo (light / dark) | brand kit | SVG | every post |
| Icon set (one) | [Lucide / Tabler] | SVG | every slide |
| Background textures (3–5) | Pixabay / SVG Repo | SVG / WebP | rotating |
| Sticker set | LottieFiles + Pixabay GIFs | JSON / WebP | reels / stories |
| Lower-third animation | LottieFiles | JSON | reels |
| Music tracks (3–5) | Pixabay Music / YouTube Audio Library | MP3 | reels |
| Sound effects (5–10) | Freesound (CC0 only) | MP3 / WAV | reels |
| Avatar placeholders | DiceBear | SVG | testimonials |

## 4. Ad-specific rules (paid surfaces)

- **No GIPHY-watermarked stickers** in paid ad creatives.
- **No identifiable people** unless model release is confirmed.
- **No copyrighted music** — every audio track must be cleared for ad
  use (some YouTube Audio Library tracks are personal-use only; check).
- **No trademark / brand logos** that aren't the client's.
- **No AI-generated content** if the client policy prohibits it.
- **Captions** for any spoken audio in reels / ads (accessibility +
  silent-autoplay).
- **Aspect / safe-zones** respected per platform (Reels UI eats the
  bottom ~250 px).

## 5. Performance budget per post

- Reel video ≤ 5 MB (under platform limit, fast upload).
- Carousel slide ≤ 1 MB.
- Static post ≤ 500 KB.
- WhatsApp status ≤ 200 KB.
- Thumbnail ≤ 80 KB.

## 6. Risk register

- [Attribution required for source X — capture in caption /
  description].
- [Model release risk on post day N — switch to illustration if used in
  paid ads].
- [Music track Y — verify YouTube Content ID before ad upload].
- [Source Z — Needs license verification before publish].
- [Children-sensitive asset — replace with safe avatar / illustration].
