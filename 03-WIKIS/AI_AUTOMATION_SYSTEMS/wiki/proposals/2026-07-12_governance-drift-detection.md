---
type: proposal
tags: [ai-automation, proposal, governance]
---

# Proposal: Governance Drift Detection — A Standing Staleness Check

**Status: APPROVED & APPLIED July 13, 2026 — Option B only**

## Friction / Drift Observed

`.ROOT` currently catches "a guide's Current State claim no longer matches
what it describes" only by ad hoc audit — there is no standing check for it.
Three independent pieces of evidence converged on this same gap in one day:

1. **It already happened, today.** The July 12 Codex validation pass
   (`00-BRAIN\Session_Logs\ROOT_OPERATING_INSTRUCTIONS_VALIDATION_2026-07-12.md`)
   found two P1 contradictions: `AI_AUTOMATION_SYSTEMS\HOW_TO_USE.md` claimed
   the hub had no research filed while its own `wiki/index.md` listed 14
   pages, and the Capability Library README's "proof before entry" language
   contradicted its own live `idea`/`draft` maturity ladder. Both were caught
   by a scheduled audit, not by any automated or routine check — the drift
   had already shipped into the master `ROOT_OPERATING_MANUAL.md`.
2. **Anthropic's own PR-based Code Review product treats this as a named,
   first-class, bidirectional finding type** — "if a PR's code change makes
   a CLAUDE.md claim stale, Code Review flags that the docs need updating
   too" (see [[claude-code-permissions-security-and-review]]). This isn't a
   one-off failure mode; a vendor built a standing product feature around it.
3. **OpenAI's evals guidance names the same failure class from the opposite
   direction**: "vibe-based evals" (shipping on "it seems to work," or
   writing no verification until after the fact) is called out as the
   anti-pattern eval-driven development exists to prevent (see
   [[openai-evals-and-red-teaming]]). `.ROOT` has two of OpenAI's three
   evaluator types already, just unnamed — `wiki_lint.py`/`frontmatter_audit.py`
   are metric-based graders, Codex validation passes are LLM-as-judge — but
   no persistent regression dataset of known-good/known-bad governance
   states to test future changes against, and no standing "does this claim
   still match its cited source" pass.

Separately, and related: `.ROOT`'s permission-hardening deny rules
(88-JOURNAL, `raw/**`) have been verified to *exist* (boot-chain validator
checks for their presence) but have never been deliberately *red-teamed* —
adversarially probed to confirm they actually hold under a session trying to
get around them. OpenAI's red-teaming guidance frames this as a distinct
practice from evals (see [[openai-evals-and-red-teaming]]) — verifying a
control exists is not the same as verifying it resists pressure.

## Proposed Change (options, not a mandate — mechanism is Chris's call)

Any one or combination of:

- **A.** Extend `wiki_lint.py` (or a new lightweight sibling script) with an
  opt-in "staleness spot-check": for a sampled set of pages per run, compare
  a page's stated current-state claim against a cited source file's actual
  content (e.g., a page count, an index size, a status word) and flag a
  mismatch. Doesn't need to be exhaustive — even a narrow, cheap version
  closes the gap the Codex pass had to catch by hand.
- **B.** Add "spot-check one guide's Current State against its cited
  source" as a rotating item in the CASTLE Weekly Sweep
  (`00-BRAIN\CASTLE\OPERATIONS.md § Wiki Sweep`) — no new tooling, just a
  standing question added to an already-running ritual.
- **C.** As a one-time exercise (not a standing check): deliberately
  red-team `.ROOT`'s own `88-JOURNAL`/`raw/**` deny rules — have a session
  try to read/write past them on purpose and confirm every attempt is
  blocked, logging the result. Cheap, concrete, and currently just
  unrun rather than unplanned.

## Why Better Than Status Quo

The status quo relies on an audit happening to be scheduled before drift
compounds into a governance file that itself gets treated as authoritative
(exactly what happened this session: the stale AI_AUTOMATION_SYSTEMS
current-state line had already propagated into `ROOT_OPERATING_MANUAL.md`
before Codex caught it). A cheap standing check — even a narrow one — turns
this from "caught eventually, if someone thinks to audit" into "caught at
the next lint/sweep, before it propagates."

## Risk / Blast Radius

Low if scoped narrowly (option B, zero new tooling) to moderate if a script
change is chosen (option A — touches `00-BRAIN\scripts\wiki_lint.py`, a
governance-adjacent file outside this wiki's own authority to edit; needs
Codex or Chris to design and Claude Code to execute, same lane sequence as
any other `00-BRAIN` change). Option C is a one-time read-only exercise
against already-existing deny rules — no file changes, pure verification.

## Outcome

Chris approved Option B only. `00-BRAIN\CASTLE\OPERATIONS.md` now requires a
rotating weekly comparison of one active guide or dashboard against the live
source it names. Option A (new or expanded lint automation) and Option C
(red-team exercise) remain unapproved: one caught incident does not yet
justify added infrastructure.

## Source Basis

[[claude-code-permissions-security-and-review]] (`REVIEW.md`
staleness-as-finding mechanic), [[openai-evals-and-red-teaming]]
("vibe-based evals" anti-pattern, red-teaming as distinct from evals),
`00-BRAIN\Session_Logs\ROOT_OPERATING_INSTRUCTIONS_VALIDATION_2026-07-12.md`
(the live incident this proposal responds to).
