# Performance Optimization Guide

Asset weight is the #1 LCP killer on LeadUp client sites. Use this guide
to keep weight low and the page fast on mobile.

## Weight targets (per asset)

| Asset | Target | Hard cap |
|---|---|---|
| Hero photo (WebP) | ≤ 200 KB | 400 KB |
| Body photo (WebP) | ≤ 80 KB | 150 KB |
| Thumbnail (WebP) | ≤ 30 KB | 60 KB |
| Icon (SVG) | ≤ 2 KB inline / ≤ 10 KB file | 20 KB |
| Illustration (SVG) | ≤ 30 KB | 80 KB |
| Lottie JSON | ≤ 50 KB | 120 KB |
| Hero video loop (WebM) | ≤ 1.5 MB | 3 MB |
| Video poster (WebP) | ≤ 80 KB | 150 KB |
| 3D model (GLB) | ≤ 1 MB | 3 MB |
| Avatar (SVG) | ≤ 5 KB | 10 KB |

Page-level target: LCP ≤ 2.5 s on a slow 4G profile (mobile), CLS ≤ 0.1,
INP ≤ 200 ms.

## Photo optimisation

- Convert to **WebP** (and AVIF if generation pipeline supports it).
- Resize to actual display size; do not ship 4000×3000 to a 1200×800 slot.
- Use `srcset` + `sizes` for responsive images:
  ```html
  <img
    src="hero-1200.webp"
    srcset="hero-600.webp 600w, hero-1200.webp 1200w, hero-1920.webp 1920w"
    sizes="(max-width: 768px) 100vw, 60vw"
    alt="Hostendor data center hero"
    width="1200" height="800"
    decoding="async"
    fetchpriority="high"
  >
  ```
- Always set explicit `width` and `height` (or CSS aspect-ratio) to
  avoid CLS.
- `loading="lazy"` for below-the-fold; `fetchpriority="high"` only for
  the LCP image.

## Vector / icon optimisation

- Run SVGs through **SVGO** to strip metadata, comments, hidden IDs.
- Prefer a tree-shakeable icon library (Lucide React, Heroicons,
  Tabler) — only the icons you use ship in the bundle.
- For many static icons on one page, use an **SVG sprite** and
  `<use href="#icon-name" />`.
- Decorative icons get `aria-hidden="true"`; meaningful icons get an
  `aria-label`.

## Illustration optimisation

- Flat illustrations → SVG, run through SVGO.
- Heavily raster-textured illustrations → WebP at 2× display size.
- Strip embedded fonts; convert text to outlines if the file ships as a
  static asset.

## Lottie optimisation

- Keep paths simple; reduce keyframe count.
- Avoid embedded raster bitmaps in Lottie files (they balloon size).
- Loop only when needed; pause off-screen.
- Honour `prefers-reduced-motion`:
  ```js
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) lottie.stop();
  ```

## GIF → video

- Convert any GIF over 200 KB to MP4 / WebM — it'll be 5–20× smaller.
- Use `ffmpeg` to convert; keep GIF only when the destination doesn't
  support video (WhatsApp, some proposal PDFs).

## Video optimisation

- Encode WebM (VP9 / AV1) + MP4 (H.264) fallback.
- Use a **WebP poster** for instant first paint.
- `playsinline muted autoplay loop` for hero loops.
- `preload="metadata"` unless the video is the LCP element.
- For long videos, stream from a CDN (Bunny, Cloudflare Stream) rather
  than serving the full file.

## 3D optimisation

- Compress with **Draco** (geometry) and **Meshopt** (advanced).
- Use baked lighting; avoid runtime ray-tracing.
- Lazy-load the 3D scene; show a static fallback while it loads.
- Provide a low-poly fallback or static image for mobile.

## Avatar optimisation

- Use seeded SVG generators (DiceBear, Boring Avatars).
- Cache server-side if you generate many per request.

## Loading strategy

- **Preload** only the LCP image and critical fonts.
- `loading="lazy"` for everything below the fold.
- `decoding="async"` for non-critical images.
- `fetchpriority="high"` only for the LCP image; `low` for nice-to-have.
- Lazy-load `<iframe>` videos (YouTube embeds) with the
  `loading="lazy"` attribute and a click-to-play poster.

## Delivery

- Serve all assets from a **CDN** (Cloudflare / Bunny / Vercel /
  Cloudflare R2).
- Set long `Cache-Control` (1 year) with versioned filenames or hashed
  paths.
- Enable Brotli (or at least gzip) for SVG / Lottie JSON / fonts.
- HTTP/2 or HTTP/3 multiplexing — bundle small icons via sprite or
  component library.

## Accessibility (don't trade weight for inclusion)

- Every meaningful image has descriptive `alt`.
- Decorative images use `alt=""` or `aria-hidden="true"`.
- Videos with speech need captions / subtitles.
- Animations respect `prefers-reduced-motion`.
- Icons used as buttons have `aria-label`.

## Quick audit checklist

- [ ] Hero ≤ 200 KB WebP, with explicit width / height set.
- [ ] All below-the-fold images `loading="lazy"` and `decoding="async"`.
- [ ] No GIF over 200 KB; convert to MP4 / WebM.
- [ ] Lottie ≤ 50 KB target.
- [ ] Video poster present; `preload="metadata"`.
- [ ] 3D scene lazy-loaded; static fallback for mobile.
- [ ] Icons via tree-shakeable library or SVG sprite.
- [ ] Brotli / gzip enabled; CDN cache headers set.
- [ ] All assets pass Lighthouse mobile ≥ 90 on Performance.
