# Workflow sequence — [request shortname]

> Use this template inside the router output to show the chain in
> detail. Section 4 of the router report can reference this for
> longer / multi-step plans.

## Sequence at a glance

```
[1] leadup-[skill-1]
       ↓
[2] leadup-[skill-2]
       ↓
[3] leadup-[skill-3]   <-- approval gate before this step
       ↓
[4] leadup-[skill-4]
       ↓
[5] leadup-[skill-5]
       ↓
[CLOSE] leadup-status-updater (update STATUS.md / TODO.md / CHANGELOG.md)
```

## Per-step detail

### Step 1 — `leadup-[skill-1]`

- Job: [one line]
- Model: [DeepSeek / Claude Sonnet / Claude Opus]
- Inputs: [files / docs / links]
- Output expected: [shape; per the skill's "Required output format"]
- Approval needed?: no
- Memory side-effect: none

### Step 2 — `leadup-[skill-2]`

- Job: [one line]
- Model: [model]
- Inputs: [refs]
- Output: [shape]
- Approval?: no / yes (reason)
- Memory: none / `STATUS.md`

### Step 3 — `leadup-[skill-3]`

- **Approval gate before this step.** [Reason — payments / auth /
  push / deploy / migration / external send.]
- Job: [one line]
- Model: Claude Sonnet (forced — high-risk)
- Inputs: [refs]
- Output: [shape]
- Approval: required
- Memory: `STATUS.md`, `DEPLOY.md`

### Step 4 — `leadup-[skill-4]`

- Job: [one line]
- Model: [model]
- Approval?: yes / no (reason)
- Memory: …

### Step 5 — `leadup-[skill-5]`

- Job: [one line]
- Model: [model]
- Approval?: yes / no (reason)
- Memory: …

### Close — `leadup-status-updater`

- Job: update memory.
- Files: `STATUS.md`, `TODO.md`, `CHANGELOG.md`, and `DEPLOY.md` if
  shipped.

## Substitutions (planned skills)

| Referenced | Substitute (until shipped) | Note |
|---|---|---|
| `leadup-multi-tenant-architect` | tenant section of `leadup-saas-mvp-planner` | flag the gap |
| `leadup-backup-rollback-planner` | rollback section of `leadup-release-manager` | flag the gap |

## Hand-offs after this chain

- Public-facing copy → `leadup-human-content-editor` (already in
  chain).
- Privacy review → `leadup-pii-risk-reviewer` (already in chain if
  applicable).
- Security review → `leadup-security-review` (already in chain if
  applicable).
- Release coordination → `leadup-release-manager` (already in chain
  if shipping).
- Memory close-out → `leadup-status-updater` (always last).

## Done = all of these true

- [ ] Each step has produced its expected output.
- [ ] Approval gates honored.
- [ ] No real secrets / PII in any artifact.
- [ ] Memory files updated.
- [ ] User confirmed the chain is closed.
