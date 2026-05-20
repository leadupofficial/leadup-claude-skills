# Microcopy edit — fill-in template

Use this template when humanising in-app or admin-panel microcopy:
buttons, empty states, errors, tooltips, confirm dialogs, onboarding
hints. Keep it short, action-led, and free of marketing tone.

---

## Inputs

- **Surface:** button / empty state / error / tooltip / confirm /
  onboarding hint / toast / [other]
- **Screen / context:** [e.g. "Client list, when there are no clients yet"]
- **Audience:** [end user / admin / staff role]
- **Length limit:** [character or line limit from the design]
- **Must-keep items:** exact action names, exact field names, role names.

---

## Mode + assumptions

> Mode: App/admin panel microcopy · Tone: short, action-led, no marketing
> Assumption: [one line — only if intent is unclear]

---

## Rewritten content

### Buttons

````markdown
- [Verb + object, e.g. "Add client", "Send reminder", "Save changes"]
- [Verb + object — never "Submit" if a more specific verb exists]
````

Rules:
- Lead with the verb.
- Use the exact noun the rest of the UI uses.
- Sentence case unless the design system requires Title Case.

### Empty states

````markdown
[One short sentence stating what is empty and why it matters.]
[One short sentence telling the user the next action.]

[Primary action button — verb + object]
````

Example:
> No clients yet. Add your first client to start sending invoices.
>
> [+ Add client]

### Errors

````markdown
[What went wrong — plain language, no jargon, no blame.]
[What to do next — one clear action.]
````

Example:
> We could not save the invoice. Check your internet and try again.

### Tooltips / hints

````markdown
[One line. Why this exists, or what the field does.]
````

Example:
> Used for WhatsApp reminders. Include the country code.

### Confirm dialogs

````markdown
[Headline — what the user is about to do.]
[One line of consequences if it matters.]

[Confirm button — verb + object]   [Cancel — plain "Cancel"]
````

Example:
> Delete this client?
> Their invoices and reminders will be removed too.
>
> [Delete client]   [Cancel]

---

## Change note

- Removed em dashes (count: __).
- Removed marketing tone: [list any phrases cut, e.g. "seamlessly
  empower" → just removed].
- Shortened to fit length limit: [character count before / after].
- Preserved exact action names and field names from the source.
- Flagged for user verification: [any place where the source said
  something the UI cannot actually do — confirm or rewrite].
