---
name: leadup-premium-ui-upgrader
description: Upgrade a LeadUp app's UI to premium international-SaaS standard. Improves layout, spacing, typography, responsive design, dashboard cards, empty/loading/error states, motion, and accessibility while preserving all functionality. Use when the user says "make UI premium", "international standard design", "improve design", "make attractive", "upgrade UI", or "SaaS level UI".
---

# LeadUp Premium UI Upgrader

## Purpose

Raise an app's visual quality to the polish bar of a funded international SaaS
— spacing, type, components, the missing states (empty/loading/error), motion,
responsiveness, accessibility — without breaking behaviour.

## When to use

Trigger phrases: "make UI premium", "international standard design", "improve
design", "make it attractive", "upgrade UI", "SaaS level UI", "make it look
expensive", "polish the dashboard", "this looks amateur, fix it".

For correctness/console-error testing → `leadup-browser-playwright-tester`.
This skill is about polish, not functional verification.

## Inputs needed

- The app/repo and which screens to upgrade (or "all").
- Any brand constraints (colors, logo, font) or "you choose".
- Framework (Next.js/React, Flutter, Bagisto) for idiomatic changes.

## Step-by-step workflow

Use `references/premium-ui-checklist.md`.

1. **Audit current UI** screen by screen against the checklist; note the worst
   offenders (cramped spacing, no empty/error states, weak hierarchy).
2. **Decide a system**: spacing scale (4/8px), type scale, restrained palette
   + 1 accent, elevation language. Match existing brand if present.
3. **Prioritize**: quick wins (spacing, type, buttons) → components (cards,
   tables, forms) → the differentiating states (empty/loading/error/success)
   → motion → responsive → accessibility.
4. **Implement** changes idiomatically for the framework; keep all behaviour,
   props, routes, and accessibility intact (do not regress a11y).
5. **Verify responsive** at 360/768/1024/1440 and `prefers-reduced-motion`.
6. **Document before/after** per screen and remaining deeper work.

## Required output format

1. **UI audit** — per screen, the issues found.
2. **Design system applied** — spacing/type/color/motion decisions.
3. **Changes made** — per screen, before → after, files touched.
4. **Prioritized remaining work** — quick wins vs deeper.
5. **A11y statement** — confirmed no regression (keyboard/contrast/focus).

## Safety rules

See `references/security-rules.md`. Most relevant here:
- Preserve all functionality, routes, and data flows — visual changes only.
- Do not regress accessibility (keyboard, contrast, focus, labels).
- Do not push/deploy; hand changes back for local review and approval.

## Common mistakes

- Restyling that breaks a form submit or route (visual-only means visual-only).
- Adding a flashy theme but still no empty/loading/error states (the real tell).
- Reducing contrast below WCAG AA for "aesthetic" reasons.
- Heavy animations that ignore `prefers-reduced-motion` or cause layout shift.
- Desktop-only polish on a mobile-first Indian-business SaaS.
- Inventing a brand when one already exists in the codebase.

## Troubleshooting

- **Under-triggers**: user said "this looks cheap" — re-invoke; suggest
  trigger phrases.
- **Over-triggers** when they want functional testing → route to
  `leadup-browser-playwright-tester`.
- **Missing tool/MCP**: no preview available — make changes + describe expected
  result and provide the run command to view locally.
- **No internet/browser**: proceed; rely on the checklist and code; defer
  visual confirmation to the user.
- **Missing project files**: if components can't be found, run
  `leadup-existing-repo-analyzer` first.
- **Build/test failure** after changes: revert the offending change, isolate
  (CSS vs logic), report; never ship UI changes that break the build.

## Test prompts

### Should trigger (5)
1. "Make the jewellery SaaS dashboard premium, international standard."
2. "This salon admin UI looks amateur — upgrade it to SaaS level."
3. "Improve the design of the clinic site, make it attractive."
4. "Upgrade UI for the CRM — proper empty and loading states."
5. "Make the school site look expensive and polished."

### Should NOT trigger (3)
1. "Test that login works in the browser." (→ browser-playwright-tester)
2. "Is the payment flow secure?" (→ security-review)
3. "Research a UI kit repo on GitHub." (→ github-repo-researcher)

### Functional test cases (2)
1. Given a dashboard with no empty/error states, the output adds them and
   lists them under "Changes made" without altering data fetching.
2. After changes, the a11y statement confirms keyboard nav + AA contrast
   preserved and the build still passes.

## Success criteria

- Measurable polish against the premium checklist, screen by screen.
- Empty/loading/error/success states present.
- Responsive + reduced-motion respected; a11y not regressed.
- All functionality intact; nothing pushed/deployed.
