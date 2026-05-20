# Website Asset Plan — [PROJECT_NAME]

A page-by-page asset plan for a LeadUp client website or product
marketing site. Fill in once; the dev team and the designer both work
off it.

## 0. Brand snapshot

- **Project:** [Hostendor / LeadUp / Trivasia / Jewellery SaaS / Salon
  SaaS / INET CRM / BRC-Buddy / ...]
- **Primary palette:** [hex codes]
- **Accent palette:** [hex codes]
- **Visual style:** [flat / line / 3D / photographic / mixed]
- **Tone:** [premium / friendly / technical / playful]
- **Attribution preference:** [no-attribution preferred / attribution
  acceptable]
- **Icon set (one):** [Lucide / Heroicons / Tabler / Phosphor / ...]

## 1. Home / landing page

| Slot | Asset | Source pick | Format | Size | Weight target | License | Notes |
|---|---|---|---|---|---|---|---|
| Hero background | [photo / illustration / video loop] | [Unsplash / unDraw / Pexels Video] | [WebP / SVG / WebM] | [1920×1080] | [≤ 200 KB / ≤ 1.5 MB] | [name + URL] | [model release / attribution] |
| Hero foreground / illustration | ... | ... | ... | ... | ... | ... | ... |
| Section icons (×N) | [icon set] | [Lucide] | SVG | [24×24] | inline | MIT | One set only |
| Feature illustrations (×N) | ... | [unDraw / Storyset] | SVG | [600×400] | ≤ 30 KB each | ... | recolour to brand |
| Logo cloud / clients | [client logos] | [client-provided] | SVG | [120×40] | ≤ 5 KB | client-owned | confirm rights |
| Testimonial avatars | [DiceBear / Boring Avatars / real photos] | ... | SVG / WebP | [80×80] | ≤ 5 KB | MIT | seed if generated |
| CTA section graphic | ... | ... | ... | ... | ... | ... | ... |

## 2. Services / features page

| Slot | Asset | Source pick | Format | Size | Weight target | License | Notes |
|---|---|---|---|---|---|---|---|
| Service icons (×N) | [icon set] | [Lucide / Tabler] | SVG | [32×32] | inline | MIT | match home set |
| Per-service illustration | ... | [Storyset / unDraw] | SVG | [600×400] | ≤ 30 KB | ... | ... |
| Process diagram | ... | [SVG Repo / custom] | SVG | [800×400] | ≤ 20 KB | ... | ... |
| Demo screenshot | [in-product screenshot] | [client-provided] | WebP | [1200×750] | ≤ 80 KB | client-owned | strip PII |

## 3. About / team page

| Slot | Asset | Source pick | Format | Size | Weight target | License | Notes |
|---|---|---|---|---|---|---|---|
| Office / team photos | [client-provided preferred] | [Unsplash placeholder if not] | WebP | [1600×900] | ≤ 150 KB | ... | release flag if Unsplash |
| Team member portraits | [client-provided] | — | WebP | [400×400] | ≤ 30 KB | client-owned | release on file |
| Story / mission illustration | ... | [unDraw / Storyset] | SVG | [600×400] | ≤ 30 KB | ... | ... |

## 4. Pricing page

| Slot | Asset | Source pick | Format | Size | Weight target | License | Notes |
|---|---|---|---|---|---|---|---|
| Plan icons / 3D icons | [IconScout free 3D / Lucide] | [...] | SVG / WebP | [80×80] | ≤ 20 KB | ... | ... |
| Comparison check / cross | [Lucide check / x] | Lucide | SVG | [16×16] | inline | MIT | ... |
| FAQ accent | ... | ... | ... | ... | ... | ... | ... |

## 5. Blog / article pages

| Slot | Asset | Source pick | Format | Size | Weight target | License | Notes |
|---|---|---|---|---|---|---|---|
| Article hero | [photo / illustration] | [Unsplash / unDraw] | WebP / SVG | [1600×800] | ≤ 150 KB | ... | per article |
| In-article diagrams | [custom / SVG Repo] | ... | SVG | [800×400] | ≤ 20 KB | ... | ... |
| Author avatar | ... | [DiceBear / real] | SVG / WebP | [64×64] | ≤ 5 KB | MIT | ... |

## 6. Empty states / 404 / loading

| Slot | Asset | Source pick | Format | Size | Weight target | License | Notes |
|---|---|---|---|---|---|---|---|
| Empty state | [Storyset / unDraw] | ... | SVG | [400×300] | ≤ 25 KB | ... | recolour to brand |
| 404 illustration | ... | ... | SVG | [600×400] | ≤ 25 KB | ... | ... |
| Loading spinner | [Lottie / SVG] | LottieFiles | JSON / SVG | [120×120] | ≤ 10 KB | ... | reduced-motion |

## 7. App / dashboard preview (marketing)

| Slot | Asset | Source pick | Format | Size | Weight target | License | Notes |
|---|---|---|---|---|---|---|---|
| Hero device mockup | [Storyset device pack / custom] | ... | SVG / WebP | [1200×800] | ≤ 80 KB | ... | ... |
| Dashboard illustration | [Storyset "dashboard"] | ... | SVG | [1200×800] | ≤ 40 KB | ... | ... |

## 8. Cross-page elements

- **Favicon / app icon** — SVG + PNG fallbacks (16/32/48/192/512).
- **Open Graph / Twitter card image** — 1200×630 WebP, ≤ 100 KB.
- **PWA splash** — per device sizes.
- **Loading skeleton SVGs** — inline, ≤ 1 KB each.

## 9. Performance budget for the page

- LCP ≤ 2.5 s on slow 4G (mobile)
- CLS ≤ 0.1
- INP ≤ 200 ms
- Lighthouse Mobile Performance ≥ 90
- Page-weight target (above-the-fold): ≤ 500 KB

## 10. Risk register

- [Attribution required from source X — captured in footer credits at /credits]
- [Model release risk on hero photo — replace with illustration if used in paid ads]
- [Trademark risk on stock photo Y — do not use in logo / favicon]
- [Lottie at Z KB — over budget, re-export simplified]
- [Source W — Needs license verification before final commit]
