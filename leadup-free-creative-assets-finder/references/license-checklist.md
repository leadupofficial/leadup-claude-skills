# License Checklist

Run this checklist on every source / asset before recommending it for a
LeadUp client surface. If any item is unclear after a reasonable check,
mark the asset as **Needs license verification** and surface it in the
risk notes. Never claim safety you cannot confirm.

## 1. Locate the official terms

- [ ] Open the **license / terms page on the source site itself** — not
      a blog post about the source, not a Reddit thread, not a YouTube
      summary.
- [ ] Capture the **exact URL** of the terms page for the output.
- [ ] Note the **license name** (e.g. "Unsplash License", "Pexels
      License", "Pixabay Content License", "MIT", "CC0", "CC-BY 4.0",
      "CC-BY-SA 4.0").

## 2. Commercial use

- [ ] Is commercial use **explicitly allowed**?
- [ ] Is paid client work covered, or only "personal projects"?
- [ ] Are there industry restrictions (gambling, adult, political,
      pharma, weapons) that affect the project?

## 3. Attribution

- [ ] Is attribution **required, optional, or not required**?
- [ ] If required: what is the **exact required credit text**?
- [ ] Where must the credit be placed (caption, page footer, credits
      page, video end-card)?
- [ ] Can the project actually show that attribution on this surface?
      (Logo, app icon, social ad creatives usually cannot show credit —
      avoid attribution-required assets on those surfaces.)

## 4. Modification / derivatives

- [ ] Can the asset be **cropped, recoloured, resized, composited,
      animated**?
- [ ] If using SVG/Lottie, can colours / strokes be edited?
- [ ] Are derivative works restricted (e.g. CC-BY-ND forbids derivatives)?

## 5. Redistribution / resale

- [ ] Can the asset be redistributed as part of a template / theme /
      stock pack? Most free sources say **no** to resale.
- [ ] Can the asset be embedded in a downloadable product (Flutter
      app, plugin, theme)?
- [ ] Can the asset be sold as a print / poster / merchandise? Usually
      **no** for free sources.

## 6. Trademarks / logos / brand marks

- [ ] Can the asset be used as part of a **client logo or trademark**?
      Most free sources forbid this.
- [ ] Does the asset itself contain a recognisable **brand, logo,
      product, character, or art**? If yes, the source's licence does
      not clear the brand owner's rights.

## 7. People & property releases

- [ ] Does the photo contain **identifiable people**?
- [ ] Does the source explicitly state model releases are cleared? (Most
      free sources do **not** clear releases.)
- [ ] Does the photo contain **recognisable buildings, branded
      products, art, or signage**? Property release risk applies.
- [ ] For ads (paid media), the bar is higher than for editorial — flag
      release risk explicitly.

## 8. Sensitive contexts

- [ ] Children-facing surface (BRC-Buddy, kids products) — avoid real
      child photos; prefer illustrations / safe avatars.
- [ ] Health / medical — verify the content is accurate; flag if it
      could mislead.
- [ ] Cultural / religious — verify respectful representation; avoid
      sacred symbols out of context.

## 9. AI-generated content

- [ ] Is any of the source's library AI-generated?
- [ ] If yes, flag it — some clients refuse AI content, and IP status
      for AI-generated work varies by jurisdiction.

## 10. API / programmatic use

- [ ] Does API use require an API key?
- [ ] What is the rate limit / quota?
- [ ] Are there branding requirements (e.g. Unsplash requires linking
      back to photographer + Unsplash on dynamic API use; GIPHY / Tenor
      have brand attribution rules)?
- [ ] Are bulk-download and caching allowed or forbidden by TOS?

## 11. Hot-link vs download

- [ ] Recommend **download + serve from project storage / CDN**, not
      hot-link from the source CDN.
- [ ] If using a CDN-hosted icon library (Iconify, Material Symbols
      web font), that is fine; flag any availability / latency risk.

## 12. Decision rule

- All items above resolved → safe to recommend.
- Any item unclear → **Needs license verification**; surface in risk
  notes.
- Commercial use unclear, or attribution can't be shown, or
  trademark / release risk for a logo-like use → do **not** recommend
  for that surface; suggest an alternative.

## Per-source quick notes

- **Unsplash / Pexels / Pixabay** — commercial OK, attribution not
  required, but **no resale unmodified**, **no use in trademarks**,
  **no claim of model release**.
- **CC-BY** — attribution required; capture the exact credit format.
- **CC-BY-SA** — attribution + share-alike (derivative must use same
  licence) — usually not suitable for proprietary client work; flag.
- **CC-BY-ND** — no derivatives; usually not suitable for design work.
- **CC0 / Public Domain** — no attribution; safest for commercial work.
- **MIT / Apache 2.0 / ISC** — include the licence text in third-party
  notices when shipping a downloadable app; safe for SaaS UI.
- **Storyset (free tier)** — attribution required; flag.
- **Lordicon (free tier)** — Lordicon branding required; flag.
- **LottieFiles** — per-file; filter to "Free" + "Commercial OK".
- **GIPHY / Tenor** — per-file + brand watermark risk.
- **Sketchfab** — filter to "Downloadable" + "CC0/CC-BY".
- **YouTube Audio Library** — per-track; some require attribution.
