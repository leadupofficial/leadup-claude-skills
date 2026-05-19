// Example LeadUp Playwright spec. Copy into the project's e2e/ folder.
// Credentials come from env vars ONLY — never hardcode real creds.
import { test, expect } from '@playwright/test';

const BASE = process.env.BASE_URL ?? 'http://localhost:3000';

test('home loads without console errors', async ({ page }) => {
  const errors: string[] = [];
  page.on('console', (m) => m.type() === 'error' && errors.push(m.text()));
  page.on('response', (r) => {
    if (r.status() >= 400) errors.push(`HTTP ${r.status()} ${r.url()}`);
  });
  await page.goto(BASE);
  await expect(page).toHaveTitle(/.+/);
  expect(errors, errors.join('\n')).toHaveLength(0);
});

test('login flow reaches dashboard', async ({ page }) => {
  await page.goto(`${BASE}/login`);
  await page.getByLabel(/email/i).fill(process.env.TEST_USER ?? 'test@example.com');
  await page.getByLabel(/password/i).fill(process.env.TEST_PASS ?? 'changeme');
  await page.getByRole('button', { name: /sign in|log in/i }).click();
  await expect(page).toHaveURL(/dashboard|home/);
});

test('protected route redirects when logged out', async ({ page }) => {
  await page.context().clearCookies();
  await page.goto(`${BASE}/dashboard`);
  await expect(page).toHaveURL(/login/);
});

test('mobile viewport has no horizontal scroll', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 812 });
  await page.goto(BASE);
  const overflow = await page.evaluate(
    () => document.documentElement.scrollWidth > document.documentElement.clientWidth,
  );
  expect(overflow, 'page scrolls horizontally on mobile').toBeFalsy();
});
