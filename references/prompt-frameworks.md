# Prompt Frameworks (LeadUp Super-Prompt)

Used by `leadup-super-prompt-builder`. Turns a rough idea into a strong,
copy-paste-ready prompt for an AI coding/research agent, in LeadUp style.

## Core skeleton (use for every prompt)

1. **Role** — what the agent should act as ("senior full-stack engineer for
   a multi-tenant SaaS", "research + planning agent").
2. **Context** — LeadUp + the specific project + stack + where it runs
   (Docker local → GitHub `leadupofficial` → Coolify → `*.leadup.in`).
3. **Source / inputs** — the attached PDF / repo / spec / screenshot / idea.
4. **Task** — the one concrete outcome, stated unambiguously.
5. **Constraints (LeadUp defaults — always include the relevant ones):**
   - Research + plan before code; recommend an approach, wait for "go".
   - Test locally in Docker / correct dev command before claiming done.
   - Do **not** push to GitHub, deploy, or run remote commands without
     explicit approval.
   - Never read or print real `.env` values; never expose API keys; use
     `__SET_ME__` placeholders only.
   - UI must be premium, international SaaS standard.
   - Update `STATUS.md` (done / in progress / bugs / blocked / next task).
6. **Definition of done** — measurable acceptance criteria.
7. **Output expectation** — plan first, then implementation steps; or the
   research dossier; etc.

## Agent variants

- **Claude Code / opencode (agentic, file-aware):** emphasise approval gates,
  small reviewable steps, run/test commands, "stop and ask before push/
  deploy", update STATUS.md. Reference real paths if known.
- **RuFlo (project intelligence / memory / swarm):** frame as research +
  planning + memory; ask it to traverse prior art, surface patterns/
  dependencies, and produce a plan before any build.
- **ChatGPT / generic LLM (no repo access):** include more explicit context
  and paste-in inputs; ask for a plan + code blocks the user will apply
  manually.

## Quality checklist (a good prompt has all)

- [ ] Role + context + single clear task
- [ ] LeadUp stack/deploy context injected
- [ ] Source/input referenced
- [ ] Safety + approval + no-secrets constraints present
- [ ] Premium-UI constraint where UI is involved
- [ ] Definition of done + STATUS.md update step
- [ ] One copy-paste block, no mixed commentary

## 12 supported prompt types → framework

| # | Prompt type | Role focus | Key extra constraints |
|---|---|---|---|
| 1 | Claude Code coding | senior engineer | small steps, tests, approval gate |
| 2 | RuFlo project intelligence | research/plan/memory | prior art, plan before build |
| 3 | New project planning | architect | stack + DB + MVP + deploy plan, no code |
| 4 | Existing repo analysis | reverse-engineer | detect stack, bugs, next task |
| 5 | API research | integration researcher | docs/auth/limits/pricing/webhooks |
| 6 | GitHub repo research | OSS evaluator | license, stars, recency, copy/adapt |
| 7 | Browser/Playwright testing | QA engineer | flows, console errors, responsive |
| 8 | Deployment | release engineer | Docker/Coolify/subdomain, no auto-deploy |
| 9 | Security review | security auditor | secrets/auth/multi-tenant, redact |
| 10 | Premium UI | product designer | premium checklist, keep behaviour |
| 11 | Content calendar | content strategist | dated calendar, hooks, repurposing |
| 12 | Client document | business writer | proposal/report/handoff, no invented terms |
