# Playwright / Browser Test Flows

Used by `leadup-browser-playwright-tester`. Test the app **running locally in
Docker or the dev server** first. If a browser tool/MCP is unavailable, write
or update Playwright specs the user can run, and provide manual steps.

## Standard LeadUp flows to cover

### Public site
- Home loads, no console errors, key CTAs visible
- Navigation between main pages works
- Forms (contact / lead capture) submit and show success/validation
- Mobile viewport (375×812) layout not broken
- Lighthouse-ish smell test: no obvious layout shift, images load

### Auth
- Login with valid creds → lands on dashboard
- Login with bad creds → clear error, no crash
- Logout clears session; protected route redirects to login
- Direct visit to protected URL while logged out → redirect

### Admin panel
- Admin login gated (non-admin cannot reach admin routes)
- Core CRUD: create, list, edit, delete one entity
- Empty states render (no rows) without errors
- Destructive actions confirm before acting

### SaaS / multi-tenant
- Tenant A cannot see Tenant B data (switch subdomain/login)
- Billing/plan screen renders; payment screen loads (test mode only)

### Health checks every run
- Browser console: no uncaught errors / failed network (4xx/5xx) on core pages
- Responsive: 375, 768, 1280 widths
- Slow/error API: UI shows loading + error states, not a blank/white screen

## Playwright spec skeleton

```ts
import { test, expect } from '@playwright/test';

const BASE = process.env.BASE_URL ?? 'http://localhost:3000';

test('home loads without console errors', async ({ page }) => {
  const errors: string[] = [];
  page.on('console', m => m.type() === 'error' && errors.push(m.text()));
  await page.goto(BASE);
  await expect(page).toHaveTitle(/.+/);
  expect(errors, errors.join('\n')).toHaveLength(0);
});

test('login flow', async ({ page }) => {
  await page.goto(`${BASE}/login`);
  await page.getByLabel(/email/i).fill(process.env.TEST_USER ?? 'test@example.com');
  await page.getByLabel(/password/i).fill(process.env.TEST_PASS ?? 'changeme');
  await page.getByRole('button', { name: /sign in|log in/i }).click();
  await expect(page).toHaveURL(/dashboard|home/);
});
```

Use env vars for test creds — never hardcode real credentials in specs.
Put specs under `e2e/` or `tests/e2e/`. Report: pass/fail per flow, console
errors, screenshots of failures, and the next fix.
