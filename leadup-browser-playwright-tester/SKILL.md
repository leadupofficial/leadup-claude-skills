---
name: leadup-browser-playwright-tester
description: Test a LeadUp app end-to-end in the browser. Runs the app locally (Docker or dev server), exercises login, forms, navigation, and admin flows, checks console errors and mobile responsiveness, and creates or updates Playwright specs. Use when the user says "test website", "run Playwright", "browser test", "check UI works", "test admin panel", or "test login".
---

# LeadUp Browser / Playwright Tester

## Purpose

Verify a LeadUp app actually works in a real browser — core flows pass, no
console/network errors, responsive on mobile — and leave behind Playwright
specs so it stays tested.

## When to use

Trigger phrases: "test website", "run Playwright", "browser test", "check UI
works", "test admin panel", "test login", "does the form submit", "e2e test
this", "verify the app in a browser".

This skill *runs* tests. To choose/sequence which browser tool to use →
`leadup-mcp-tool-orchestrator`. For visual polish, not correctness →
`leadup-premium-ui-upgrader`.

## Inputs needed

- The app/repo and how to run it (Docker command or dev server + port).
- Base URL (default `http://localhost:3000`) and which flows matter.
- Test credentials by **env var name only** — never pasted into chat.

## Step-by-step workflow

Use `references/playwright-test-flows.md`.

1. **Run the app locally** (Docker or correct dev command). Confirm it serves.
2. **Pick flows**: home, navigation, forms, login, logout, protected routes,
   admin CRUD, multi-tenant isolation, billing screen (test mode only).
3. **Drive the browser** with the available browser tool/MCP; if none,
   write/update Playwright specs the user can run and give manual steps.
4. **Check health every run**: console errors, failed network (4xx/5xx),
   loading/error/empty states, responsive at 375/768/1280.
5. **Capture evidence**: pass/fail per flow + screenshots of failures.
6. **Write/update specs** under `e2e/` (creds via env vars only).
7. **Report** results and the single most important fix; log bugs for
   `leadup-status-updater`.

## Required output format

1. **Run command used** + base URL.
2. **Results table** — flow | pass/fail | console/network errors | note.
3. **Failure evidence** — screenshots/log excerpts (no secrets).
4. **Specs created/updated** — file paths.
5. **Top fix** — the one issue to address next.

## Safety rules

See `references/security-rules.md`. Most relevant here:
- Test credentials via env vars only; never hardcode real creds in specs or
  print them; never test against production with real customer data.
- Use payment **test mode** only; never trigger live charges.
- Do not disable auth/CORS/CSP to make a test pass — report the blocker.

## Common mistakes

- Testing against a stale build instead of the freshly-run app.
- Hardcoding real login credentials into the spec file.
- Calling a white screen "passing" because the URL loaded — assert content.
- Ignoring console/network errors that don't break the happy path.
- Skipping mobile widths on a mobile-first Indian-business SaaS.
- Running destructive admin actions against real data.

## Troubleshooting

- **Under-triggers**: user said "see if the site works" — re-invoke; suggest
  triggers.
- **Over-triggers** for visual design feedback → route to
  `leadup-premium-ui-upgrader`.
- **Missing tool/MCP** (no browser tool): write/update Playwright specs +
  manual step list instead of live driving.
- **No internet/browser access**: deliver specs and a manual test checklist;
  state that live execution was not possible.
- **Missing project files**: if no run command is discoverable, ask or run
  `leadup-existing-repo-analyzer` first.
- **Build/test failure**: capture the exact error, classify (build / env /
  selector / app bug), report; do not weaken assertions to force green.

## Test prompts

### Should trigger (5)
1. "Test the login on the salon SaaS in the browser."
2. "Run Playwright against the jewellery app and check the admin panel."
3. "Browser test the venus school site — does navigation work?"
4. "Check the contact form actually submits on the clinic site."
5. "E2e test the CRM and update the specs."

### Should NOT trigger (3)
1. "Make the dashboard look premium." (→ premium-ui-upgrader)
2. "Which browser tool should we use?" (→ mcp-tool-orchestrator)
3. "Is this repo ready to deploy?" (→ deploy-checker)

### Functional test cases (2)
1. With the app running, produce a results table covering home + login + one
   admin CRUD, with console-error status per flow.
2. With no browser tool available, output a runnable Playwright spec using
   env-var credentials and a manual test checklist.

## Success criteria

- App run locally and exercised (or specs delivered if no browser tool).
- Console/network/responsive checks reported per flow.
- Specs created/updated with env-var creds (no secrets committed).
- One clear top fix surfaced.
