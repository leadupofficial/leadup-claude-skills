# Rewrite examples — before / after

Concrete before/after pairs for every rewrite mode. These show what the
human-content-editor should produce. Do **not** copy these texts into a real
client site as-is; they are pattern examples.

---

## 1. Website landing page (hero + sub-hero)

**Before (AI):**
> Empower your business with seamless solutions that unlock growth — our
> cutting-edge platform helps you elevate operations, harness data, and
> revolutionize the way you connect with customers in today's fast-paced
> world.

**After (human):**
> Run your salon's bookings, reminders, and payments from one screen.
> Built for busy owners in tier-2 cities who do not have time to chase
> no-shows. Set up in one evening. WhatsApp reminders included.

**What changed:** removed em dash, replaced "empower / seamless / unlock /
cutting-edge / elevate / harness / revolutionize" with concrete actions,
named the audience, gave a real outcome.

---

## 2. SaaS feature copy

**Before (AI):**
> Our robust analytics suite empowers teams to seamlessly leverage
> data-driven insights and make game-changing decisions.

**After (human):**
> Daily and weekly reports for revenue, no-shows, and top services. Mail
> them to yourself or your accountant automatically. No setup needed.

**What changed:** dropped "robust / empowers / seamlessly / leverage /
data-driven / game-changing", said what the analytics actually shows and
who uses it.

---

## 3. About company page

**Before (AI):**
> We are a passionate team of innovators dedicated to revolutionizing the
> way businesses operate. Our holistic approach combines world-class
> technology with a human-centric ethos.

**After (human):**
> LeadUp is a small team in Coimbatore that builds websites, apps, and
> SaaS for Indian businesses. We pick projects we can deliver well, ship
> in weeks, and stay around for support after launch.

**What changed:** removed "passionate / innovators / revolutionizing /
holistic / world-class / human-centric", named the location, what is
actually built, and the working style.

---

## 4. Service page

**Before (AI):**
> Our comprehensive web development services empower brands to elevate
> their digital presence through next-generation solutions.

**After (human):**
> What we build for clients:
>
> - Marketing websites in Next.js, ready in 3–4 weeks.
> - Booking systems with WhatsApp and email reminders.
> - Admin panels so your team can update content without us.
>
> Pricing starts at ₹45,000 for a 5-page site. Quote in 24 hours.

**What changed:** broke into a list of specific deliverables, added time
and price ranges, dropped every hype word.

---

## 5. App / admin panel microcopy

**Before (AI):**
> Seamlessly empower your workflow by unlocking the full potential of our
> intuitive client management dashboard.

**After (human):**
> No clients yet. Add your first client to start sending invoices and
> reminders.
>
> [+ Add client]

**What changed:** UI copy is one short line + one action. No marketing
language inside a product.

---

## 6. Proposal / client document tone

**Before (AI):**
> We are thrilled to present this game-changing proposal that will
> revolutionize your brand's digital journey through our cutting-edge
> approach.

**After (human):**
> This proposal covers the new website for Sundar Jewellers, including
> design, development, and one month of support after launch.
>
> Scope, timeline, and pricing are listed below. Anything not listed is
> out of scope for this engagement.

**What changed:** dropped hype, opened with what the document is for,
stated scope boundaries clearly.

---

## 7. Social media content (LinkedIn)

**Before (AI):**
> 🚀 Excited to share that we are unlocking next-generation possibilities
> for our clients through our revolutionary, cutting-edge approach to
> digital transformation! 🔥

**After (human):**
> We shipped a new booking flow for a dental clinic in Coimbatore last
> week. Bookings went from a Google Form to a real schedule with WhatsApp
> reminders. Cut no-shows by about a third in the first 10 days. Happy to
> share the build notes if useful.

**What changed:** removed emojis-as-decoration, named a real audience,
gave a concrete outcome, offered a useful next step.

---

## 8. WhatsApp / email message

**Before (AI):**
> Dear valued customer, we are thrilled to inform you that we have
> seamlessly unlocked a transformative offer just for you!

**After (human):**
> Hi Priya, your invoice for October is ready. Total ₹4,800. You can pay
> via UPI to leadup@upi or reply here if you need a copy.

**What changed:** named the person, named the amount, gave one clear
action, dropped every marketing word.

---

## 9. Technical / project explanation (STATUS update)

**Before (AI):**
> We have seamlessly integrated a robust authentication system that
> empowers users to securely navigate our cutting-edge platform.

**After (human):**
> Auth: Clerk wired up for the admin panel. Magic-link login works
> end-to-end on staging. Pending: role-based access for the `staff`
> role, blocked on the org schema change.

**What changed:** internal/technical copy is plain facts. No marketing
words at all. Names the blocker.

---

## Common anti-patterns these examples fix

- Em dashes everywhere → removed.
- Hype words → replaced with concrete actions.
- Vague benefits → replaced with named audience + outcome.
- Perfect tricolons → broken into uneven, specific bullets.
- Marketing tone in product UI → cut entirely.
- Pep-talk closers → replaced with a clear next step or removed.
