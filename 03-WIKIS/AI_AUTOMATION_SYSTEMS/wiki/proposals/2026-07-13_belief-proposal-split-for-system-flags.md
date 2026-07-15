---
type: proposal
tags: [ai-automation, proposal, governance]
---

# Proposal: Separate "Belief" from "Behavior Change" in the Flag/Review Mechanism

**Status: APPROVED & APPLIED July 13, 2026 — pilot**

## Friction / Drift Observed

`SYSTEM_FLAGS.md`'s current mechanism conflates two different things into one artifact — a flag is simultaneously *the observation* ("X is broken/stale/inefficient") and *the fix* ("do Y about it"). This has three concrete costs, visible in the flag table's own history:

1. **No reusable record of the underlying belief once a flag closes.** When flag #62 ("SYSTEM_FLAGS.md was 90% closed-flag history") closed with "history rule added," the *lesson* (a live governance file re-read every session accumulates unbounded history-tax) isn't recorded anywhere separable from that one fix — if the same class of problem shows up in a different file later (say, a different hub's `log.md` growing unbounded), there's no place that lesson lives to be cited or reapplied. It has to be re-derived from scratch or found by re-reading old closed-flag archives.
2. **No tracking of which fix actually worked.** Flags close on "fix applied," not on "fix verified to have helped" — there's no follow-up review a set period later asking "did this actually solve it, or did the same symptom resurface?" (Flag #63/#66/#70 show a real, if informal, version of this: flag re-raised after being closed comes back as HIGH priority per the stated rule — but that's a manual, memory-dependent catch, not a structural one.)
3. **No record of rejected ideas, so the same question can get re-litigated.** Nothing in the current mechanism captures "this was considered and explicitly declined, here's why" as a distinct, checkable artifact — the July 9 llm-wiki-pattern proposal's own "What Was Rejected, and Why" section is a manually-written analog of exactly this need, done once as prose rather than as a reusable structural pattern.

## Proposed Change

Adapt loopany's belief/proposal split (full mechanics confirmed against the
actual `loopany-reflect/SKILL.md`, not just its README summary — see
[[../self-improving-agent-architectures-gbrain-loopany-closed-loop]]) as an
optional structural addition to the existing flag mechanism — not a
replacement:

- **Keep flags as they are** for the common case (a concrete, single-fix
  issue — most of the current table). No change needed there.
- **Gate on a threshold, not vibes.** loopany's reflect skill only writes a
  belief once evidence clears a stated bar (≥3 flags/incidents showing the
  same class of problem, or ≥2 that contradict an existing belief) — its own
  anti-pattern list calls out "one bad outcome isn't a pattern." Borrow the
  threshold, not the exact numbers: a belief is worth writing only once a
  second, unrelated flag lands in the same class, not on the first
  occurrence.
- **For flags that clear that bar**, split the closure into two linked
  pieces instead of one closing note:
  - A **belief** — the generalized lesson, stated once, independent of any
    specific file, citing the ≥2 flags that support it (e.g., "a live
    governance file re-read every session accumulates unbounded
    history-tax past ~N entries — flags #62, #[future]").
  - A **proposal** — the specific behavior change tied to that belief, with
    a `status: proposed | accepted | rejected` field and (if accepted) a
    scheduled re-check date to confirm it actually helped, not just that it
    shipped.
- **Verify before closing.** loopany requires tracing a proposal back to its
  cited evidence before it's actionable (`loopany trace --direction
  backward`) — the `.ROOT` equivalent is just reading the cited flags back
  before promoting a belief, not a new tool.
- Rejected proposals keep their reason logged in place — visible on the
  next re-raise, so the same idea doesn't get proposed cold twice.

This does **not** require new tooling, a database, or new file types — it's
achievable as a documented convention (two new optional fields/sections in
the existing flag-table format, or a small `lessons.md` sibling file next
to `SYSTEM_FLAGS.md` for the belief side) rather than loopany's full
artifact/kind/CLI machinery, which is overbuilt for `.ROOT`'s current scale
(a handful of open flags at a time, not hundreds of daily artifacts).

## Why Better Than Status Quo

The status quo already has an informal version of "don't re-litigate a closed question" (the re-raise-as-HIGH rule) and an informal version of "generalize the lesson" (this proposal document itself, and the July 9 proposal's own rejected-ideas section) — both done as one-off prose when the moment calls for it, not as a standing, reusable structure. The belief/proposal split makes both of those already-valued behaviors cheap and habitual instead of something that only happens when someone remembers to write it up carefully. It directly strengthens the Review Cadence's own stated goal ("stable repeated lessons promote through reviews") by giving "the lesson" a place to live independent of the specific flag that first surfaced it.

## Risk / Blast Radius

Low. This is an additive convention to `00-BRAIN\SYSTEM_FLAGS.md`'s existing format, not a rewrite — the current table structure, priority tiers, and archive-to-`99-ARCHIVE` history rule are all unaffected. Worth trying on the *next* flag that's clearly a generalizable pattern (not retrofitting the current open-flags table) to see if the split earns its keep before deciding whether to formalize it further. If it doesn't pull its weight after a few uses, drop it — no structural cost to reverting.

## Outcome

Chris approved a lightweight pilot, not a rewrite of `SYSTEM_FLAGS.md`.
`00-BRAIN\SYSTEM_LEARNINGS.md` is now the on-demand home for a generalized
lesson only after two unrelated flags/incidents establish the pattern. Each
entry must cite its evidence, name a `check_at` date, and link any approved
behavior-change proposal. No existing flag was retrofitted; the first entry
waits for the next qualifying pattern.

## Source Basis

[[../self-improving-agent-architectures-gbrain-loopany-closed-loop]]
(full mechanics — pattern thresholds, evidence-chain verify, accept/reject
flow — confirmed 2026-07-13 against the live `loopany-reflect/SKILL.md` on
GitHub, not just the README-level summary in the raw/ clippings);
[[../llm-wiki-pattern-and-second-brain-tools]] (loopany comparison, 2026-07-13
update); `00-BRAIN\SYSTEM_FLAGS.md` (the mechanism this proposal responds
to — flags #62, #63, #66, #70 cited as the friction evidence); `00-BRAIN\AGENT.md
§ Review Cadence` ("stable repeated lessons promote through reviews" — the
existing goal this proposal tries to make cheaper to actually do).
