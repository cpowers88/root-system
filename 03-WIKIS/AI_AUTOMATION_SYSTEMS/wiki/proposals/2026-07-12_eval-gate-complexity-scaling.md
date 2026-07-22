---
type: proposal
tags: [ai-automation, proposal, governance, verification]
timeline: reference
---

# Proposal: Scale the Agent Evaluation Gate with Architecture Complexity

**Status: APPROVED & APPLIED July 12, 2026** — applied to `AGENT.md` §
Agent Evaluation Gate, rule 2, as drafted: typical/edge/failure-recovery
stay the floor for any workflow; tool-selection/data-precision,
handoff-accuracy, and adversarial/permission-boundary cases now trigger on
what the workflow actually introduces, rather than being demanded
uniformly. Rule count unchanged (still item 2 of 5); kept to one sentence.

## Friction / Drift Observed

`00-BRAIN\AGENT.md § Agent Evaluation Gate` (added as closed SYSTEM_FLAGS
flag #67, July 12) currently specifies a **fixed** five-case verification
model: typical / edge / adversarial / permission-boundary / failure-recovery,
applied uniformly regardless of what's being verified.

This was built from CASTLE's shallow morning read of the OpenAI docs pack,
which extracted the principle "traces/evals before multi-agent scale" but
not the mechanics behind it. Today's full ingest of that same material (see
[[openai-evals-and-red-teaming]]) found the actual mechanism is sharper: the
number of nondeterminism *categories* needing their own evals **grows with
architecture complexity** — tool-selection and data-precision evals only
become relevant once tools exist; agent-handoff-accuracy evals only become
relevant once multiple agents exist. A single-turn task and a multi-agent
workflow don't need the same five checks; the multi-agent case needs more,
and a trivial single-turn case may not need all five either.

A fixed five-case list can therefore under-test a complex multi-agent
change (missing handoff/tool-selection-specific cases) or over-specify a
simple one (demanding adversarial/permission-boundary cases for something
with no permission surface).

## Files Touched

`00-BRAIN\AGENT.md § Agent Evaluation Gate` — replace or supplement the
fixed five-case list with a complexity-scaled version: name the base cases
(typical, edge, failure-recovery) as the floor for any agent change, and add
category-specific cases keyed to what the change actually introduces (tool
calls → tool-selection/data-precision cases; multiple agents/handoffs →
handoff-accuracy cases; permission-sensitive actions → adversarial/
permission-boundary cases).

## Why Better Than Status Quo

Matches the verification burden to the actual architecture being verified,
instead of a one-size-fits-all count. Prevents both under-testing (a
multi-agent change passing five generic cases without ever exercising a
handoff) and needless ceremony (demanding permission-boundary cases for
something that has no permissions to boundary-test).

## Risk / Blast Radius

Low-moderate. Touches an always-loaded section of `AGENT.md`; needs care to
keep the addition short (the whole point of the fixed five-case rule was
simplicity — this proposal trades some of that simplicity for accuracy, so
the rewritten rule should stay as compact as possible).

## Source Basis

[[openai-evals-and-red-teaming]] — "The single most load-bearing structural
finding" section (architecture-complexity-to-nondeterminism-category
mapping). `00-BRAIN\SYSTEM_FLAGS.md` closed flag #67 (the rule this proposal
would revise).

## Post-Change Check (added 2026-07-15, check_at discipline)

- **Expected behavior:** new agent workflows get testing proportional to their complexity per `AGENT.md § Agent Evaluation Gate` rule 2; no consequential workflow enters recurring use untested.
- **Evidence for improvement or regression:** an eval record exists for the next new workflow (scanner/tracker automation are the likely candidates). Regression = a workflow incident that the scaled test tiers would have caught, or a consequential workflow with no eval record.
- **check_at:** 2026-08-24 (next new agent workflow is expected with the fall setup window)
- **Outcome:** (blank until the check date — record what actually happened, with an evidence link)
- **Verdict:** (keep / modify / revert — blank until the check date)
