Prompt type: RuFlo project intelligence · Target: RuFlo

```
Act as a research + planning agent for the LeadUp project "[project]".

Goal: [research and plan X | evaluate options for Y].

Use project memory and prior art: traverse related patterns, dependencies,
and past decisions before proposing anything.

Context: LeadUp Technologies. Stack: [stack]. Flow: build → test in Docker
→ GitHub (leadupofficial) → Coolify → [subdomain].leadup.in.

Do:
- Surface prior art, reusable patterns, and dependencies relevant to [X].
- Compare options with trade-offs (effort, risk, fit, cost).
- Recommend one approach with a concrete, ordered plan.

Constraints:
- Plan before build — do NOT implement until I approve the plan.
- No push/deploy/remote commands without my approval.
- Never expose .env values or keys; placeholders only.
- Note any premium-UI and multi-tenant implications.

Deliver: findings → options → recommended plan → open questions. Then
stop and wait for my approval.
```

Toggles: [research only] · [add risk register] · [include cost estimate]
