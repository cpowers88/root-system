---
type: reference
tags: [reference, governance, ai-automation]
---

# SYSTEM_LEARNINGS — Durable Evidence-Based Lessons

## Purpose

This is an on-demand registry for reusable lessons about how `.ROOT` should
operate. It is not a task list, a session log, or a replacement for
`SYSTEM_FLAGS.md`.

## Promotion Rule

An ordinary flag remains a flag. Create a learning only when at least **two
unrelated flags or incidents** establish the same general pattern, or when
two incidents materially contradict an existing active learning. Read the
cited evidence before promotion; one bad outcome is not a pattern.

## Required Entry Shape

```markdown
## L-YYYY-NN — <declarative lesson>
**Status:** active | superseded
**Evidence:** flag/incident references (at least two unrelated)
**Check at:** YYYY-MM-DD

<The general lesson, independent of one file or fix.>

**Behavior proposal:** <linked approved/rejected proposal, or none>
**Outcome:** <added at check-at review>
```

## Lifecycle

`flag or incident → repeated evidence → learning → proposal → Chris-approved
change → check_at review`

Rejected proposals retain their reason. Accepted changes are committed with
their proposal/rationale. A learning may remain active without requiring a
behavior change.

## Active Learnings

None yet. This pilot begins with the next qualifying pattern; existing flags
are not retrofitted.
