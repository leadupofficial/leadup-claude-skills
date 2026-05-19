# Project Docs Templates

Used by `leadup-project-kickoff`. These bootstrap a new LeadUp project's
memory so any future AI session can resume cleanly. Ready-to-fill copies live
in `leadup-project-kickoff/assets/`.

## PROJECT.md
```markdown
# <Project> — PROJECT.md
## What it is
## Client / owner
## Goal & success criteria
## Scope (in / out)
## Stack (decided)
## Architecture (1 diagram or bullets)
## Key decisions (dated)
## Open questions
```

## CLAUDE.md (project-specific AI instructions)
```markdown
# CLAUDE.md — <project>
- Stack: <...>
- Run locally: <command / docker compose up>
- Test: <command>
- Branch/push: leadupofficial/<repo>, ask before push
- Deploy: Coolify → <subdomain>.leadup.in, ask before deploy
- Safety: never read/print .env values; never commit secrets
- Source of truth for "what next": STATUS.md
```

## STATUS.md
See `status-template.md` (in the same references folder).

## DEPLOY.md
```markdown
# DEPLOY — <project>
## Local run
## Build
## Env vars (names only)
## Coolify config (service, port, volumes)
## Domain (<subdomain>.leadup.in)
## Migrations
## Rollback
```

## SECURITY.md
```markdown
# SECURITY — <project>
## Auth model
## Multi-tenant isolation
## Secrets handling (env only)
## Payments / webhooks
## Uploads
## Known risks / TODO
```

## README.md
```markdown
# <Project>
Short description. Setup, env, run, test, deploy pointers.
```

## .env.example (placeholders ONLY)
```
NODE_ENV=development
DATABASE_URL=postgres://user:__SET_ME__@localhost:5432/app
JWT_SECRET=__SET_ME__
RAZORPAY_KEY_ID=__SET_ME__
RAZORPAY_KEY_SECRET=__SET_ME__
# add provider keys as needed — placeholders only, never real values
```

## MVP roadmap shape
- Milestone 0: skeleton + auth + deploy pipeline
- Milestone 1: core value flow (the one thing the product must do)
- Milestone 2: billing / multi-tenant / admin
- Milestone 3: polish (premium UI), hardening, launch
