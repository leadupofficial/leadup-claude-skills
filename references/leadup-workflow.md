# LeadUp Standard Workflow

Shared reference for every skill in the LeadUp Claude Skills Pack. This is the
loop LeadUp Technologies follows on almost every project. Skills should respect
this order and never skip ahead (e.g. never deploy before testing).

## The loop

1. **Attach a source** — PDF, screenshot, repo, spec file, Google Drive notes,
   API doc, or a client requirement message.
2. **Analyze deeply + research** — understand the source, do real research
   (official docs, GitHub, current pricing/limits). Plan before code.
3. **Plan** — propose a recommended approach with trade-offs. Wait for the
   user's "do recommended" / approval on scope.
4. **Build** — implement the recommended task only. Small, reviewable steps.
5. **Test locally** — run in Docker or the correct dev command on localhost.
   The user wants to *see* it working before believing it.
6. **Push to GitHub** — org `leadupofficial`, only after approval.
7. **Deploy** — `leadup-server` / Coolify v4, under a `*.leadup.in`
   subdomain, only after approval.
8. **Update project memory** — STATUS.md / TODO.md / CHANGELOG.md with
   done, in-progress, bugs, blocked, and the next recommended task.

## Environment facts

- **GitHub org:** `leadupofficial`
- **Server:** `ssh deploy@leadup-server` (do not run remote commands without approval)
- **Orchestration:** Docker locally, Coolify v4 on the server
- **Domains:** `*.leadup.in` subdomains (e.g. `app.leadup.in`, `vibe.leadup.in`)
- **Common stacks:** Next.js, Node/TypeScript, Postgres, Flutter, Laravel/Bagisto (PHP 8.3), Supabase (self-hosted)
- **Common integrations:** Razorpay, WhatsApp, Gemini, DeepSeek, OpenAI, SMTP
- **Recurring pattern:** multi-tenant SaaS for small Indian businesses, each wanting AI features and "international standard" UI

## Approval gates (hard rules)

A skill may **plan, draft, and check**, but must **stop and ask** before:

- `git push` to `leadupofficial`
- Any deploy to `leadup-server` / Coolify
- Any remote SSH command
- Any destructive change (drop DB, rm -rf, force-push, history rewrite)
- Zipping/packaging this pack for distribution
- Installing this pack into `~/.claude/skills`

Default to producing a checklist or plan and handing control back.

## Project memory files

Every LeadUp project should carry these so any AI session can resume cleanly:

- `PROJECT.md` — what it is, scope, stack, decisions
- `CLAUDE.md` — project-specific AI instructions
- `STATUS.md` — current state (single source of truth for "what next")
- `DEPLOY.md` — how to deploy this project
- `SECURITY.md` — security posture and known risks
- `README.md` — human-facing setup
- `.env.example` — placeholder env keys only (never real values)
