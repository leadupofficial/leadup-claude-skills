# GitHub Repo Research Template

Used by `leadup-github-repo-researcher`. Goal: decide whether a repo can be
**copied**, **adapted**, or only used as **inspiration** — with license and
maintenance evidence.

## Candidate: <owner/repo> — reviewed <YYYY-MM-DD>

### Snapshot
- URL:
- Stars / forks:
- Last commit date:
- Open issues / PR responsiveness:
- Primary language / framework:
- License: (MIT / Apache-2.0 / GPL / AGPL / none / custom)

### License verdict
- [ ] Permissive (MIT/Apache/BSD) → can copy with attribution
- [ ] Copyleft (GPL/AGPL) → avoid copying into proprietary client/SaaS code
- [ ] No license → treat as all-rights-reserved; **inspiration only**

### Stack compatibility with LeadUp
- Matches target stack? (Next.js / Node-TS / Flutter / Laravel)
- Heavy/abandoned deps?
- TypeScript / typing quality
- Multi-tenant friendly?

### Quality signals
- Tests present? CI? Docs?
- Code health (skim): structure, secrets in repo?, obvious smells
- Security: any known CVEs, unsafe patterns

### Usage decision
| Part | Copy | Adapt | Inspiration only | Reason |
|---|---|---|---|---|

### Integration outline
- What to pull in, what to rewrite, attribution needed, risks

### Recommendation
- Best repo for the job + 1–2 alternatives, with the why
