# Asset Format Guide

Pick the right format for each surface. Defaults below are what LeadUp
uses; deviate only when a real constraint forces it.

## Photos / raster images

| Format | When | Notes |
|---|---|---|
| **AVIF** | Modern browsers, smallest size | Excellent quality at low bitrate. Use with WebP fallback. |
| **WebP** | Default for web | ~25–35% smaller than JPG at same quality. |
| **JPG** | Legacy fallback, hero photos | Use for very large gradient-heavy hero photos when WebP loss is visible. |
| **PNG** | Only when transparency is required and SVG won't work | Heavy — avoid for hero. |

Web hero: WebP (or AVIF + WebP). Body photos: WebP. Thumbnails: WebP.
Email-embedded images: JPG (broader email-client support).

## Vectors / icons / illustrations

| Format | When | Notes |
|---|---|---|
| **SVG** | Default for icons, logos, line illustrations, charts | Crisp at any size, recolourable, accessible. |
| **PNG** | Only when an SVG would render very large (3D-baked illustration) | Provide @1x / @2x / @3x. |
| **Icon font** | Legacy / WordPress sites only | Avoid for new projects; SVG components win. |

SVG hygiene:
- Run through SVGO before shipping (strip metadata, IDs, comments).
- Inline SVG when it needs CSS styling or interaction.
- Use a component library (Lucide React etc.) for icon sets instead of
  raw `<img>` tags.

## Animations

| Format | When | Notes |
|---|---|---|
| **Lottie JSON** | Default for UI animations, illustrations in motion | Scalable, recolourable, light if exported well. Target ≤ 50 KB. |
| **MP4 / WebM** | Complex 3D or filmed animations | When Lottie can't capture it cheaply. |
| **GIF** | Messaging / WhatsApp / proposal docs only | Heavy and limited colour — avoid on web hero. |
| **APNG** | Niche transparency animations | Limited browser tooling. |

Lottie best practices:
- Export from After Effects with Bodymovin / LottieFiles plugin.
- Avoid embedded raster images inside Lottie — they balloon size.
- Use the `lottie-web` light player or `@lottiefiles/lottie-player`.
- Respect `prefers-reduced-motion`.

## Video

| Format | When | Notes |
|---|---|---|
| **WebM (VP9 / AV1)** | Modern web, best compression | Pair with MP4 fallback. |
| **MP4 (H.264)** | Universal fallback | Required for iOS Safari for many use-cases. |
| **MOV** | Source only — convert before shipping | Do not serve MOV to the web. |

Video best practices:
- Use a `poster` image (WebP) for instant first paint.
- `playsinline muted autoplay loop` for hero loops.
- `preload="metadata"` unless the video is the LCP element.
- Hero loops ≤ 1.5 MB; longer clips chunked / streamed.
- Captions / subtitles when speech is present.

## 3D

| Format | When | Notes |
|---|---|---|
| **GLB (binary glTF)** | Default for web 3D | Single file, textures embedded. |
| **glTF + bin + textures** | Larger scenes where assets are reused | More files but cacheable. |
| **OBJ** | Static, simple meshes | No PBR materials, no animation. |
| **FBX** | Source pipeline (Blender, Maya) | Convert to GLB before shipping. |
| **USDZ** | iOS AR Quick Look | Use alongside GLB for Apple AR. |

3D best practices:
- Compress with **Draco** or **Meshopt**.
- Bake lighting where possible; avoid runtime ray-traced lighting.
- Lazy-load 3D scenes (don't block first paint).
- Warn on low-end mobile; provide a static fallback image.

## Avatars

| Format | When | Notes |
|---|---|---|
| **SVG (DiceBear / Boring Avatars)** | Default | Seedable, deterministic, recolourable. |
| **PNG initials** | When SVG generator is unavailable | UI Avatars / server-side text avatar. |

Seed deterministically so the same user gets the same avatar across
sessions.

## Emojis

| Format | When | Notes |
|---|---|---|
| **Native Unicode** | Default | No payload, renders per OS. |
| **Twemoji / Noto / OpenMoji (SVG/PNG)** | Cross-platform visual consistency | Twemoji/OpenMoji require attribution per current terms. |

## Sound / music

| Format | When | Notes |
|---|---|---|
| **MP3** | Universal | Heavier but compatible everywhere. |
| **AAC / M4A** | Mobile-first, better compression | iOS-friendly. |
| **OGG / OPUS** | Modern web | Lighter; pair with MP3 fallback. |

## Format decision quick rules

- Icon → SVG (component library).
- Illustration → SVG if flat; WebP if raster.
- Photo → WebP (+ AVIF if you can).
- Animation → Lottie JSON first; MP4/WebM if Lottie can't.
- Hero video loop → WebM + MP4, with a WebP poster.
- 3D → GLB compressed with Draco / Meshopt.
- Avatar → SVG (seeded).
- Emoji → native Unicode unless cross-platform consistency required.
- Music / SFX → MP3 + (AAC or OGG) fallback.
