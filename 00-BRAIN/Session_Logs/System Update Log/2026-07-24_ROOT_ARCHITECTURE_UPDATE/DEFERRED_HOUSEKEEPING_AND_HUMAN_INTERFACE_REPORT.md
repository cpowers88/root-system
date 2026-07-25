---
type: decision-note
timeline: later
status: preserved-for-housekeeping
tags: [architecture, housekeeping, human-interface]
created: 2026-07-24
---

# Deferred Housekeeping and Human Interface Report

## Purpose

Preserve the architectural notes recovered from Chris's saved review copy
without expanding the current implementation scope. These items belong in a
later housekeeping pass after the skeleton, validator, and CASTLE impact gate
have been reviewed.

## Deferred housekeeping items

1. Clarify the division of labor between `01-NORTH_STAR\NORTH_STAR.md` as
   durable truth and `Goals & Milestones` as the changeable goal/execution
   layer.
2. Strengthen the Watchtower contract and test its handoff to CASTLE.
3. Add a concise routing document for `77-INBOX`.
4. Review whether root-level entry surfaces are all still necessary.
5. Evaluate a small `README.md` and `HOW_TO_USE.md` convention for major
   folders, starting with a pilot rather than applying it everywhere.
6. Evaluate a possible `04-Chris` human-facing area for Chris-specific
   operating rules, human-readable reports, and other material intended for
   Chris rather than machine execution.
7. Evaluate a `human_eye_log` or equivalent end-of-day reporting surface.
8. Evaluate whether wiki pages can be reduced through durable source pointers
   and structured placeholders without weakening learning, citation, or
   offline usability.
9. Update the role/lane documentation so Atlas is retired as a named lane and
   Codex's broader audit and execution-brief responsibility is explicit.

## Human/machine interface hypothesis

Chris's concern is valid enough to test: repeatedly placing machine-oriented
status, implementation notes, and report detail in the same surfaces Chris
must use to stay informed may increase cognitive load for both sides. A
separate human-facing report surface could let the machine layer remain terse
and operational while giving Chris a deliberate, readable briefing channel.

This is a hypothesis, not a settled architecture. The test should compare:

- current mixed reports;
- a concise machine state plus a human-facing daily brief; and
- the maintenance cost, duplication risk, and actual reading burden of each.

The design must preserve one source of truth. A human report should be a
derived briefing or return packet, not a second authoritative state file.

## Boundary for later work

Do not create `04-Chris`, `human_eye_log`, or a vault-wide README/HOW_TO_USE
rollout during the current update. Treat them as housekeeping candidates and
require a small pilot, owner/return rules, and a rollback path before adoption.

## Source note

These notes were recovered from the review copy:
`# .ROOT Vault Skeleton — mynotedversionsorry.md`.

That file remains untouched so Chris can remove or archive it after completing
the current review. This report is the preserved working record.

## Later acceptance test

The candidate human interface is worth adopting only if Chris can find the
needed daily state faster, machine instructions become less noisy, and no
duplicate authoritative facts are introduced.
