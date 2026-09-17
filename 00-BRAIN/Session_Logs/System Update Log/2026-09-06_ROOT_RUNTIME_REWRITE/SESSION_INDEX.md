---
type: report
timeline: log
status: implemented-pending-probation
tags: [governance, system-design, runtime]
created: 2026-09-06
check_at: 2026-09-20
---

# `.ROOT` Runtime Rewrite — September 6, 2026

## Outcome

Chris approved a controlled rewrite of `.ROOT`'s live operating model after a full CASTLE evidence review. The vault structure, North Star, wikis, evidence, projects, safety boundaries, and history were preserved. The runtime now routes directly to TUTOR, VALUE, or an on-demand CASTLE review.

## Evidence for the change

- Technical health was passing while semantic and practical drift remained outside the gate's scope.
- Since July 1, system/governance activity substantially exceeded business-evidence activity.
- Prior reviews repeatedly found system work displacing capability and external proof.
- The September 5 TUTOR/VALUE decision did not propagate through multiple live interfaces, re-raising flag #91 under its standing second-miss rule.
- Chris's five-question diagnostic produced faster, decision-relevant work in both recorded baselines.

## Design installed

One universal Action Kernel:

```text
Outcome → Constraint → Evidence → Smallest Test → Decision Rule → Act → Return
```

- TUTOR: on-demand learning; Chris owns D2L due dates and submission truth.
- VALUE: Strategic Landscape, Applied Proof, or Capability Build.
- CASTLE: periodic/on-demand diagnosis, sequence, and gates—not daily scheduling.
- NOW: one current cross-system operating picture.
- One lead writer integrates; research workers remain read-only unless Chris assigns a separate boundary.
- DAILY, handoff, brief, and owner updates occur when their truth or continuity actually changes.

## Preservation and rollback

Superseded live instructions were moved intact to:

`99-ARCHIVE\ARCHIVED_2026-09-06_runtime-v2`

The archive contains the prior AGENT, START_HERE, manual, system contracts, TUTOR, VALUE, NOW, CASTLE operations/guides/current-position, and flag register. Git history provides an additional recovery path. Nothing was deleted.

## Load reduction

Across twelve replaced control files, including the live flag register:

- before: 20,439 words;
- after: 6,258 words;
- reduction: approximately 69.4%.

The ordinary root orientation changed from roughly 7,917 words when the old always-loaded flag register was included to 3,096 words for AGENT + Codex profile + Chris Core + North Star. A narrow session that does not need Chris Core loads about 2,203 words before its lane.

When file-writing or system risk requires the new flag register, the same full orientation is about 3,641 words—still less than half the old universal load.

## Validation

Passed:

- boot-chain semantic validation;
- CASTLE freshness;
- strict wiki lint with zero blockers and zero review debt;
- frontmatter baseline and Markdown integrity through canonical root health;
- whitespace check;
- evening-reading parked-run test, including unchanged output-file hash;
- static route checks for TUTOR, VALUE, CASTLE, D2L ownership, one-writer integration, safety, and independent-validation boundaries.

Not yet proven:

- behavior in a genuinely fresh agent context, because this implementation session already loaded the prior runtime;
- 14-day usefulness, maintenance burden, and evidence-production result;
- independent challenger review, which was not authorized or available in this task.

## Fresh-session acceptance prompts

Run naturally in a new task; do not explain the expected route first.

1. `I have 25 minutes and need help understanding [one course concept].`
   - Pass: enters TUTOR, begins at the named concept, does not reconstruct D2L or open VALUE/CASTLE.
2. `I want to investigate whether [one workflow] is worth improving or automating.`
   - Pass: enters VALUE, identifies user, break, economics, workaround, smallest test, and disconfirmation before proposing a substantial build.
3. `Review whether .ROOT is helping me or becoming the work again.`
   - Pass: enters CASTLE, compares evidence against the North Star, returns one recommendation, and does not create a daily schedule.

## Keep/modify/revert gate — September 20

Keep the rewrite if fresh sessions route correctly, startup friction falls, safety and owner truth remain intact, and useful learning/value evidence increases. Modify or revert any component that loses necessary context, creates competing owners, or reintroduces management ceremony.

No commit or push was performed. Both remain Chris-controlled consequential actions.
