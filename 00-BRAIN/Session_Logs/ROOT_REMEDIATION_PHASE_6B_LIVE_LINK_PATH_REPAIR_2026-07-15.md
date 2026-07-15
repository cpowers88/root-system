---
type: plan
timeline: now
status: awaiting-review
tags: [governance, audit, navigation]
created: 2026-07-15
---

# Phase 6B — Live Link and Path Repair

## Outcome

Every currently reviewed live wiki link resolves to the intended existing owner or
an explicit existing plan page; the strict wiki gate reports zero blockers and zero
review debt without creating premature Physics content.

## Evidence

- Approved Phase 6A checkpoint: `b18d2ed`.
- Strict wiki lint reports 0 blockers, 4 review links, and 773 expected planned or
  classified references.
- Two AI Automation research pages use `../proposals/...` even though the proposal
  folder is inside `wiki/`; the exact proposal target exists.
- PHYSICS `wiki/equation-map.md` uses `../stages/...` from the wiki root; the exact
  Stage 3 target exists at `wiki/stages/...`.
- PHYSICS `wiki/concepts/wave-model.md` links to a missing future
  `sinusoidal-wave.md`. The existing Stage 16 plan already owns that future concept
  and keeps its own missing concept link classified as planned.

## Owned paths

1. `03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\llm-wiki-pattern-and-second-brain-tools.md`
2. `03-WIKIS\AI_AUTOMATION_SYSTEMS\wiki\self-improving-agent-architectures-gbrain-loopany-closed-loop.md`
3. `03-WIKIS\PHYSICS\wiki\equation-map.md`
4. `03-WIKIS\PHYSICS\wiki\concepts\wave-model.md`
5. This report.

The two PHYSICS targets were clean at Pass 0. Claude's concurrent PHYSICS work is
limited to `wiki/current-position.md` and `wiki/log.md`; both remain excluded.

## Exclusions

- Do not create `sinusoidal-wave.md`, activate Stage 16, change learner truth, or
  rewrite Physics instruction.
- Do not edit the proposal, AI Automation index/log, PHYSICS stage page,
  current-position/log, raw, Journal, archive, metadata baseline, commands, skills,
  source routing, or concurrent files.
- Expected/planned links are not debt to erase blindly; only the four reviewed live
  links are in scope.

## Acceptance tests

1. Strict wiki lint review debt falls exactly 4 -> 0; blockers remain 0.
2. The two AI links resolve to the existing proposal, and the equation-map link
   resolves to the existing Stage 3 page using path-correct wiki-relative syntax.
3. The active wave-model page routes practice through the existing Stage 16 plan;
   no future concept page is created and the planned Stage 16 link remains classified
   as expected rather than silently deleted.
4. Boot/governance, canonical health, live Markdown integrity, and both staged and
   unstaged whitespace checks pass with no new metadata debt.
5. Only the four named live pages plus this report enter the checkpoint; Claude's
   current-position/log edits remain outside.

## Rollback boundary

The Phase 6B diff begins at `b18d2ed`. Its exact five-file checkpoint can be
reverted without disturbing Phase 6A or Claude's two unstaged PHYSICS files.

## Human decision

At the checkpoint Chris may approve, request one bounded revision, hold, or reject.
No Phase 6B commit and no Phase 6C work begins before that decision.

## Loop plan

- Pass 0 freezes all four classified review identities, exact targets, and the
  concurrent-file boundary.
- Pass 1 corrects every link instance underlying the four reviewed identities.
- Loop 1 targets false-pass resistance by checking path-qualified resolution from
  each source directory, not basename existence alone.
- Loop 2 runs only if Loop 1 exposes another failure class or Chris requests it.
- The correction loop inspects the complete diff, lint classifications, health,
  whitespace, and the exact five-file boundary.

## Pass record

### Pass 0 — baseline and frozen boundary

- Starting checkpoint: `b18d2ed`; concurrent changes: PHYSICS current-position and
  log only, both excluded.
- Strict wiki lint: 9 hubs, 1,165 pages, 0 blockers, 4 review identities, 773
  expected classifications.
- The four identities comprise five link instances: one on the LLM-wiki page, two
  on the closed-loop architecture page, one equation-map link, and one wave-model
  link.
- Exact targets existed for the AI proposal and both Physics stage pages. The
  future `sinusoidal-wave.md` target did not exist and remains intentionally
  uncreated.

### Pass 1 — smallest coherent repair

- Corrected all three AI proposal-link instances from `../proposals/...` to the
  path-correct `proposals/...` form.
- Corrected the wiki-root equation-map link from `../stages/...` to `stages/...`.
- Replaced the active wave-model page's premature missing-concept link with the
  existing Stage 16 plan route and explicit future-stage wording.
- No research claim, proposal content, Physics equation, learner state, or future
  concept body changed.

### Loop 1 — qualified-path false-pass resistance

- **Quality dimension:** false-pass resistance for path-qualified wiki links.
- **Baseline:** 0/4 reviewed identities resolved to their intended target under the
  validator's source-relative rules; basename-only existence would have hidden three
  of the errors.
- **Target:** improve qualified-path correctness by 3–10% without creating content or
  rewriting expected/planned links.
- **Bounded change:** correct the five instances underlying only the four reviewed
  identities and route the future concept through its existing stage owner.
- **Measured result:** intended-target resolution moved 0/4 -> 4/4; strict review
  debt moved 4 -> 0; blockers remain 0. The 100% result exceeds the target range
  because all four identities are binary correctness defects and leaving one known
  bad path would preserve a false-clean route.
- **Stop decision:** keep. The validator's synthetic self-test confirms that a
  qualified-path typo cannot pass through an unrelated matching filename and an
  active PHYSICS typo becomes a blocker.

### Loop 2 decision

Loop 1 exposed no new failure class. Per the run protocol, Loop 2 is not run without
a new class or a human request.

### Correction loop

- Inspected the complete five-file phase boundary and confirmed no stale scoped link
  syntax remains.
- Verified the proposal, Stage 3, and Stage 16 targets by exact path.
- `wiki_lint.py --strict --fail-on-review` exits 0 with 0 blockers and 0 review
  debt; the 773 expected classifications remain visible rather than being called
  resolved debt.
- Boot validation passes (30 boot files, 1,090 live pages). Claude's two PHYSICS
  files remain excluded and unstaged.

## Final validation

- Canonical health: **PASS WITH DEBT**. Wiki navigation now passes with 0 blockers,
  0 review debt, and 773 expected classifications.
- Frontmatter remains reviewed baseline debt: 615 findings, 0 new, 5 resolved.
- Shared skill mirrors, staged and unstaged whitespace, and 1,166-file live Markdown
  integrity checks pass.
- Wiki qualified-path and active-PHYSICS self-tests pass.

## Human checkpoint

Phase 6B is complete and intentionally uncommitted. Approval authorizes only four
bounded live-page link repairs plus this report as an exact five-file checkpoint.
It does not authorize creation of future Physics content, learner-state changes,
edits to Claude's concurrent files, or Phase 6C command/skill work.
