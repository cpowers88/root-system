---
domain: tech
type: concept
tags: [subject/devops, subject/change-management]
timeline: later
status: wiki-only
---

# Why Change Management Programs Collapse (and What Bill Tries Instead)

**Summary**: The Phoenix Project's case study in how formal change-management processes die in practice — an unused tool, an unenforced CAB, and an ambiguous definition of "change" — and the crude-but-working alternative the protagonist substitutes (index cards, a whiteboard, mandatory attendance).

**Sources**: The Phoenix Project, thePhoenixProject.pdf (Ch. 3-4, 6, 8-9, 11, 22; pp. 42-44, 56-83, 98-103, 119-124, 226-230)

**Last updated**: 2026-06-18

---

## How it failed the first time

Parts Unlimited had already invested in a proper change-management program: ITIL training, a consultant-built ITIL-compliant tool, a weekly Change Advisory Board (CAB) (p. 58). Two years later: the tool requires twenty minutes of mandatory fields for a five-minute change, has UI limitations that make it physically hard to enter real data (a 64-character field for what needs hundreds of server names), and the CAB meeting has been attended by almost no one for over a year — not even the CISO who originally pushed the policy (pp. 60, 79). The Networking and Server team staged an outright rebellion against using it. The CISO (John) routinely bypasses the process entirely for "urgent" compliance work, which is exactly the unauthorized/untested change that caused the book's opening payroll outage (pp. 41-43).

The root dynamics, as the characters name them:
- **No enforcement, so it decayed.** A process with no consequence for skipping it gets skipped under any deadline pressure, and deadline pressure is constant in IT.
- **Tooling friction kills adoption faster than the policy can save it.** A burdensome tool doesn't make people safer — it makes them route around the tool, taking the safety net with it.
- **Everyone marks everything "urgent" or "emergency"** once they learn that's the only way to get attention — which makes the urgent flag meaningless and defeats the prioritization the process was supposed to provide (p. 79).
- **No one had even agreed on what counts as a "change."** Is restarting a server a change? Turning one off? On? (Turning *on* a duplicate DHCP server once took down the entire network for 24 hours, which settled that debate — p. 81.) Without a shared definition, you can't have a shared process.

## What Bill tries instead

Rather than fix the existing tool, Bill restarts from zero with the lowest-tech possible mechanism: one index card per planned change (who, what system, one-sentence summary), pinned to a whiteboard calendar, reviewed at a *mandatory* CAB meeting with no exceptions (pp. 78-80). The group spends 30 minutes just agreeing on a working definition of "change": *"any activity that is physical, logical, or virtual to applications, databases, operating systems, networks, or hardware that could impact services being delivered"* (p. 81).

This immediately surfaces the real scale of the problem: once people actually believe their changes will get reviewed and supported rather than blocked, submissions go from an expected ~50/week to 437 in the first week, with Patty (the change manager) projecting 400+ ongoing (pp. 82, 99). Bill's instinct — don't freeze changes to "catch up," because that would punish the people now doing the right thing and kill the fragile new buy-in (p. 83) — leaves the org with a visibility problem (too many changes to review) rather than a compliance problem (no visibility at all), which he treats as the better problem to have.

## Making 437-a-week reviewable: risk tiering

Reviewing every change with equal scrutiny doesn't scale, so the team splits changes into three tiers using an explicit 80/20 framing — "twenty percent of the changes pose eighty percent of the risk" (p. 100):

1. **Fragile/high-risk** — changes to the ~10 most fragile services/apps (legacy systems prone to crashing, anything touching shared databases or core infrastructure). These require full CAB authorization and scheduling, with standby support lined up in advance (pp. 100, 101).
2. **Standard/pre-approved** — low-risk changes done many times before successfully (ITIL's "standard change" category, e.g. a recurring tax-table upload). Still logged, but scheduled without case-by-case review (p. 101).
3. **The "messy middle"** — medium-risk changes that don't fit either bucket. Rather than have the CAB evaluate the technical merits of work it doesn't understand, the responsibility shifts to the submitter: get sign-off from everyone the change could affect, document it, and the CAB checks that this *process* was followed rather than re-judging the change itself (p. 102).

The first real CAB meeting under this scheme processes 9 high-risk changes in under a minute combined and clears 147 standard changes after a 10% spot-check — but then surfaces a second-order problem: 173 of the week's changes (nearly half) were all scheduled for the same day Phoenix was set to deploy, an unplanned "change collision" risk nobody had been watching for until the visibility existed to see it (pp. 107-108).

## What the data shows once it exists: changes don't complete

A week later, completion tracking reveals 60% of scheduled changes aren't actually getting done — discovered only because the new process bothered to check (p. 120). The dominant cause: changes silently depend on Brent, and he's now walled off from non-Phoenix work (see [[it-operations-bottleneck-management]]). Bill explicitly maps this onto the plant-floor WIP problem Erik described: incomplete changes don't disappear, they pile up and recombine with the next batch — "we're like the Bates Motel of changes... changes go in but never come out" — heading toward thousands of pending changes within weeks if nothing changes about how dependencies are surfaced *before* scheduling (pp. 121-122).

## From change board to work board

Part 2 extends the whiteboard idea beyond CAB scheduling. Patty builds kanban lanes for frequent service requests and later color-codes work cards by business-priority work, internal IT improvement work, and blocked work; each card also carries the change ID so the physical board and tracking tool remain connected (source: thePhoenixProject.pdf, pp. 226-230). This is no longer only "approve or reject changes." It is a work-management system that shows demand, WIP, blocked work, and whether the right mix of work is flowing.

## Connects to

- [[it-operations-bottleneck-management]] — change volume is itself a form of demand competing for the same constrained resources; surfacing 437 changes/week is the change-management analog of discovering 70+ untracked internal projects.
- [[four-types-of-work]] — "changes" is one of the four categories this book treats as chronically under-visible.
- [[the-phoenix-project]] — tracker page.
- [[it-work-centers-and-kanban]] - Patty's kanban boards generalize the early CAB whiteboard into visible queues and pull-based execution.
