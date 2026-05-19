---
name: leadup-github-repo-researcher
description: Research open-source GitHub repos for code or design inspiration before reusing them in a LeadUp project. Checks license, stars, activity, last commit, stack compatibility, and decides what can be copied, adapted, or used only as inspiration. Use when the user says "use open source repo", "best GitHub repo", "find repo inspiration", "research GitHub examples", or "best design repo".
---

# LeadUp GitHub Repo Researcher

## Purpose

Find and vet open-source repositories so LeadUp can reuse code/design safely:
licence-clean, maintained, stack-compatible, with a clear verdict on what to
copy, what to adapt, and what is inspiration-only.

## When to use

Trigger phrases: "use open source repo", "best GitHub repo", "find repo
inspiration", "research GitHub examples", "best design repo", "is there a
library for", "open-source starter for", "good reference implementation".

For a hosted third-party API (Razorpay, Gemini, etc.) → use
`leadup-api-research-builder`.

## Inputs needed

- What is being built / the component or feature needing a reference.
- Target stack (Next.js / Node-TS / Flutter / Laravel) for compatibility.
- Whether output will ship in proprietary client/SaaS code (licence matters).

## Step-by-step workflow

1. **Clarify the need** (feature, component, or design pattern) and the stack.
2. **Search GitHub** for strong candidates; shortlist 2–4.
3. For each, fill `references/github-research-template.md`: stars, last
   commit, issues/PR responsiveness, language, **licence**.
4. **Licence verdict**: permissive (copy w/ attribution) vs copyleft
   (GPL/AGPL — avoid in proprietary client/SaaS) vs none (inspiration only).
5. **Stack & quality check**: compatibility, abandoned deps, tests, secrets in
   repo, obvious smells.
6. **Usage decision** per part: copy / adapt / inspiration-only, with reason.
7. **Recommend** the best repo + 1–2 alternatives and an integration outline.

## Required output format

A comparison of candidates following `github-research-template.md`, ending
with: **Recommendation** (best repo + alternatives), a copy/adapt/inspiration
table, required attribution, and integration risks.

## Safety rules

See `references/security-rules.md`. Most relevant here:
- Treat no-licence / GPL/AGPL repos as **do not copy** into proprietary LeadUp
  client/SaaS code; inspiration only — say so explicitly.
- Never copy code containing committed secrets; flag and exclude such repos.
- Do not clone/run untrusted code without stating the risk and getting an ok.

## Common mistakes

- Recommending a repo by stars alone while ignoring an AGPL licence.
- Missing that the repo is abandoned (last commit years ago, open security PRs).
- Suggesting a React repo for a Flutter project (stack mismatch).
- Not separating "copy" vs "inspiration" — leading to licence violations.
- Overlooking heavy/unmaintained dependencies that become LeadUp's problem.

## Troubleshooting

- **Under-triggers**: user said "is there something open source for X" —
  re-invoke; suggest triggers.
- **Over-triggers** for a hosted API → route to `leadup-api-research-builder`.
- **Missing tool/MCP** (no GitHub/web access): ask the user for repo URLs to
  evaluate, or give vetting criteria to apply manually.
- **No internet**: provide the evaluation checklist and licence guidance; defer
  the live lookup.
- **Missing project files**: not required — compatibility judged from the
  stated target stack.
- **Build/test failure** when trialing a repo: isolate (deps vs config),
  report; do not adopt a repo that won't build without a clear fix path.

## Test prompts

### Should trigger (5)
1. "Find the best open-source admin dashboard repo for Next.js."
2. "Is there a good GitHub repo for Flutter chat UI I can adapt?"
3. "Research GitHub examples for multi-tenant Postgres."
4. "Best design repo to take inspiration from for a SaaS landing page."
5. "Use an open source starter for the hosting panel — which one?"

### Should NOT trigger (3)
1. "Add Razorpay payments, research the API." (→ api-research-builder)
2. "Analyze our existing repo's state." (→ existing-repo-analyzer)
3. "Upgrade this dashboard to premium UI." (→ premium-ui-upgrader)

### Functional test cases (2)
1. Given "Flutter chat UI", returns 2–4 repos with licence, last-commit, and a
   copy/adapt/inspiration verdict per repo.
2. An AGPL repo is explicitly marked "inspiration only — do not copy into
   proprietary code".

## Success criteria

- Each candidate has licence + maintenance + stack evidence.
- Clear, per-part copy/adapt/inspiration decision with attribution noted.
- One recommended repo + alternatives; licence risk never glossed over.
