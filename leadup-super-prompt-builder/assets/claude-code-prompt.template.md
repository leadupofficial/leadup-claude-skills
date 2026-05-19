Prompt type: Claude Code coding · Target: Claude Code / opencode

```
Act as a senior full-stack engineer on the LeadUp project "[project]".

Source / inputs: [repo path | spec file | screenshot | rough idea].

Task: [the one concrete feature or fix], in small, reviewable steps.

Context: LeadUp Technologies. Stack: [Next.js / Node-TS / Postgres /
Flutter / Bagisto]. Flow: build → test in Docker locally → GitHub
(leadupofficial) → Coolify on leadup-server → [subdomain].leadup.in.

Constraints:
- Research and propose a short plan first; wait for my "go" before coding.
- Work in small steps; after each, say what changed and how to test it.
- Test locally in Docker / the correct dev command before claiming done.
- DO NOT push to GitHub, deploy, or run remote/SSH commands without my
  explicit approval — stop at that gate and ask.
- Never read or print real .env values or API keys; use __SET_ME__
  placeholders only; never commit secrets.
- UI must be premium, international SaaS standard (empty/loading/error
  states, responsive, accessible).
- When done, update STATUS.md: done / in progress / bugs / blocked /
  next recommended task.

Definition of done: [measurable acceptance criteria].
```

Toggles: [shorter] · [stricter approval gate] · [add Playwright tests]
