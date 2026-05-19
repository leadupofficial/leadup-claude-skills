# Premium UI Checklist ("international standard")

Used by `leadup-premium-ui-upgrader`. The goal is the polish bar of a funded
international SaaS, not a template. Preserve behaviour and accessibility while
upgrading visuals.

## Layout & spacing
- [ ] Consistent spacing scale (4/8px system), no arbitrary margins
- [ ] Max content width + generous gutters; not edge-to-edge text
- [ ] Visual hierarchy: clear primary action per screen
- [ ] Grid alignment; nothing visually "off by a few px"

## Typography
- [ ] One type scale, max 2 families, sensible line-height (1.4–1.6 body)
- [ ] Readable contrast (WCAG AA: 4.5:1 text)
- [ ] No orphaned all-caps walls; numerals tabular where tabular data

## Color & theme
- [ ] Restrained palette + 1 accent; semantic colors for success/warn/error
- [ ] Dark mode parity if app supports it
- [ ] Consistent elevation/shadow language

## Components
- [ ] Dashboard cards: aligned, equal heights, clear metric + label + trend
- [ ] Buttons: clear primary/secondary/tertiary, disabled + loading states
- [ ] Forms: labels, inline validation, helpful errors, focus rings
- [ ] Tables: sticky header, zebra/hover, pagination, responsive collapse

## The states that separate amateur from premium
- [ ] **Empty state** — illustration/explanation + primary action, not blank
- [ ] **Loading state** — skeletons, not just a spinner on white
- [ ] **Error state** — human message + retry, never a stack trace
- [ ] **Success feedback** — toast/inline confirmation
- [ ] **Partial/long content** — truncation, "show more", overflow handled

## Motion
- [ ] Subtle, fast (150–250ms), eased; respects `prefers-reduced-motion`
- [ ] No janky layout shift; transitions on enter/leave of key elements

## Responsive
- [ ] 360 / 768 / 1024 / 1440 all clean
- [ ] Touch targets ≥ 44px; no horizontal scroll on mobile
- [ ] Nav collapses sensibly; modals usable on mobile

## Accessibility (do not regress)
- [ ] Keyboard navigable, visible focus, semantic landmarks
- [ ] Alt text, labelled controls, ARIA only where needed
- [ ] Color not the only signal

## Output
Before/after notes per screen, the specific changes, and a prioritized list
(quick wins → deeper work). Keep all existing functionality.
