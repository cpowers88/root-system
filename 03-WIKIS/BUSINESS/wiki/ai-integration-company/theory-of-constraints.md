---
tags:
  - phase-2
  - audit
  - framework
---

# Theory of Constraints (TOC)

> Source: Goldratt & Cox, *The Goal* (3rd Revised Edition, 2004). Migrated from FORGE
> July 7, 2026 — this page consolidates FORGE's `theory-of-constraints.md` and
> `the-goal-goldratt.md`. The applied version of this framework (the Five Focusing
> Steps run against a client engagement) lives in
> [[smb-ai-audit-method|SMB AI Audit Method]] Steps 4 and 6 — this page is the
> underlying theory those steps draw on.

## Purpose
Give the audit method a rigorous definition of "the constraint" and why fixing it first — rather than improving everything a little — is the only move that changes a system's total output.

## Key Idea
A business is a chain of dependent processes. At any moment its overall output is capped by exactly one constraint (a resource, policy, or market condition whose capacity is at or below the demand on it) — improving anything else doesn't help until the constraint itself is addressed.

The goal of a business is to make money, now and in the future — not efficiency, quality, market share, or any other proxy metric pursued for its own sake. Three measurements connect that goal to daily decisions:

- **Throughput** — the rate the system generates money *through sales*. Producing something unsold isn't throughput.
- **Inventory** — money invested in things the system intends to sell.
- **Operational expense** — money spent turning inventory into throughput.

Reframed goal: increase throughput while reducing both inventory and operational expense — and the three are coupled, so evaluate any change against all three, not just one.

**Dependent events + statistical fluctuation:** when steps happen in a fixed sequence and each has natural variation, the variations don't average out — they accumulate. The slowest dependent step sets the pace for the entire chain, regardless of how fast everything else can move. This is why a bottleneck's effect isn't "one slow part among many" — it determines total system output.

**The asymmetry rule:** an hour lost at the bottleneck is an hour lost for the entire system. An hour saved at a non-bottleneck is a mirage — it doesn't increase total throughput, because the bottleneck still caps the system regardless of how efficient everything else becomes.

**Cost-world vs. throughput-world:** traditional cost accounting pushes toward optimizing every resource independently ("local optimums"). TOC optimizes the system's throughput instead — a locally "efficient" decision (running a non-bottleneck at full utilization to look productive) can hurt the business by building unsold inventory that ties up cash without producing sales.

## The Five Focusing Steps

1. **Identify** the constraint — the resource, policy, or market condition whose capacity is at or below demand.
2. **Exploit** it — squeeze every bit of usable capacity from it before spending money to add more (eliminate idle time, fix upstream defects before they waste constraint time).
3. **Subordinate** everything else to it — schedule every other resource to serve the constraint's needs, even at less than their own local maximum efficiency.
4. **Elevate** it — only once exploitation and subordination are exhausted, actually invest in more capacity at the constraint.
5. **Repeat, beware inertia** — once the constraint is broken, it moves elsewhere. Policies built to protect the old constraint (special handling, workarounds) become dead weight — and can themselves become the new constraint if left in place.

## Why It Matters
This is the conceptual root of the audit method: a digital audit is, structurally, an exercise in finding a client's constraint before recommending fixes. Without this discipline, an audit produces a long list of plausible-sounding inefficiencies with no way to rank which one actually matters — and clients correctly sense when a roadmap wasn't prioritized by real impact.

## Practical Actions
- In Step 1 (identify), resist the pull toward "improve everything a little." Use the client's own data — CRM timestamps, queue lengths, volumes — to point at the one stage that's actually capping output.
- In Step 2 (exploit), always check for free/cheap fixes at the constrained stage before scoping a paid build there.
- In Step 5 (repeat), build the re-audit expectation into the sales conversation from day one — a single audit finds today's constraint, not a permanent fix.

## Beginner Version
Apply Step 1 only, informally: in every audit, explicitly name "the one stage where work piles up most" before writing any findings. Don't yet build the full five-step sequence into the report.

## Intermediate Version
Run the full five-step sequence explicitly in Step 4 (waste diagnosis) and Step 6 (priority scoring) of every audit — see [[smb-ai-audit-method|SMB AI Audit Method]].

## Advanced Version
Use TOC as the theoretical spine of quarterly re-audits under a retainer: each re-audit is fundamentally "the constraint moved, run Step 1 again," not a generic check-in. This is a differentiated, book-backed reason for the client to keep paying for re-diagnosis rather than treating a build as a one-time deliverable.

## Revenue Connection
TOC is the reasoning that justifies prioritized, high-confidence findings in the audit deliverable — which is what converts a diagnostic sale into an implementation sale. It's also the direct argument for [[retainer-model|retainer]] pricing: constraints move, so the value of re-diagnosis recurs.

## Human-Agent Management Connection
The constraint in an SMB's operations is very often a human bottleneck (the owner personally reviewing everything, one employee who's the only one who knows a process). TOC's "elevate" step, applied through the [[human-agent-operating-model|human-agent operating model]], often means inserting AI-first production at exactly that bottleneck stage — not everywhere in the business — so the redesign is targeted rather than diffuse.

## Risks / Failure Modes
- **Diagnosing waste everywhere instead of the constraint specifically** — a report that lists twenty minor inefficiencies with no clear ranking fails the "balance flow, not capacity" discipline and reads as unfocused to a sophisticated buyer.
- **Elevating before exploiting/subordinating** — recommending a paid build at the constrained stage before checking for a free policy fix wastes the client's money and undercuts trust.
- **Treating an audit as one-and-done** — ignoring Step 5's inertia warning loses the retainer argument entirely.

## Links to Related Pages
- [[smb-ai-audit-method]] — where the Five Focusing Steps get applied directly to Steps 4 and 6
- [[retainer-model]] — the "constraint moves" argument for recurring re-diagnosis
- [[human-agent-operating-model]] — targeting the redesign at the actual constraint, not diffusely
