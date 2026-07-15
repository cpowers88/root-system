---
type: plan
tags: [now, governance, audit]
status: active
created: 2026-07-15
---

# `.ROOT` Remediation Phase Loop — July 15, 2026

## Purpose

Execute the July 15 system-integrity remediation as a sequence of small,
independently reviewable phases. Improve each phase through evidence-based loops
without turning optimization into endless churn.

This is a run-specific execution protocol. It does not modify or supersede
`AGENT.md`, any `CLAUDE.md`, or the permanent review cadence.

## Ownership during the run

| Lane | Owner | May edit | Must not edit concurrently |
|---|---|---|---|
| System remediation | Codex | root settings, `00-BRAIN\scripts`, CASTLE, root governance, named non-school targets | school-learning files owned by Claude |
| School learning | Claude + Chris | `03-WIKIS\EDUCATION`, `03-WIKIS\PHYSICS`, `03-WIKIS\PYTHON`, their current-position/log pages, and directly owned school artifacts | `.claude`, `00-BRAIN\scripts`, CASTLE, root governance, `NOW.md` |

If a task crosses lanes, stop and reconcile the working tree before either agent
continues. Do not let two surfaces edit the same file.

## The phase command structure

Every phase brief must state all seven fields before editing:

1. **Outcome:** the observable condition that will be true when the phase is done.
2. **Evidence:** the files, checks, or behavior proving the problem exists.
3. **Owned paths:** the exact files or directories this phase may change.
4. **Exclusions:** explicit protected paths and deferred issues.
5. **Acceptance tests:** deterministic checks plus any required human behavior test.
6. **Rollback boundary:** the isolated diff or commit that can be reversed without
   disturbing another phase.
7. **Human decision:** approve, revise once more, hold, or reject.

## Required loop

### Pass 0 — baseline

- Read every target and its governing instruction.
- Capture `git status --short`, relevant counts, and current validator output.
- Check for concurrent edits and equivalent artifacts.
- Freeze the owned paths and exclusions for the phase.

### Pass 1 — smallest coherent implementation

- Make only the changes required to meet the stated outcome.
- Preserve historical meaning, private/raw boundaries, and unrelated work.
- Run the phase-specific acceptance tests.
- Inspect the complete diff, not only the command output.

### Loop 1 — adversarial refinement

Ask:

- Where could the new design falsely report PASS?
- What assumption depends on launch directory, path syntax, ignored files, or a
  human remembering something?
- Did the edit repair the cause or merely one observed instance?
- Did wording become clearer without creating another authority copy?

Before editing, write a compact improvement contract:

1. **Quality dimension:** choose one primary dimension—false-pass resistance,
   completeness, command clarity, rollback safety, or maintenance cost.
2. **Baseline:** name a count, test case, human step, ambiguity, uncovered state,
   output size, or other observable starting measure.
3. **Target:** aim for a 3–10% improvement in that dimension.
4. **Bounded change:** repair one cause inside the phase's owned paths.
5. **Measured result:** record the same measure after the change and run every
   affected acceptance test.
6. **Stop decision:** keep the change only when the gain is real and no protected
   scope or previously passing check regresses.

The percentage is a design target, not a quota. Do not manufacture files, tests,
or scope to reach it. Binary correctness and newly discovered safety failures may
justify a gain above 10%; explain the exception. A measured gain below 3% is kept
only when it closes a concrete correctness gap or materially reduces future risk.

### Loop 2 — optional final refinement

Run only when Chris requests it or Loop 1 exposes a new failure class. Write a new
improvement contract; do not reuse Loop 1's percentage or claim cumulative gains
without measuring them. Focus on one of the named quality dimensions and do not
use Loop 2 to begin the next phase.

### Human-review stop

Report:

- files changed and excluded;
- baseline → final measurements;
- what each refinement loop improved;
- each loop's baseline, target, measured result, and any justified target-range
  exception;
- validators passed, known debt, and tests still requiring a person;
- exact uncommitted diff/commit boundary;
- the next phase, without starting it.

No phase self-approves. After Chris approves, preserve the phase as an isolated
checkpoint before opening the next phase.

## Standard validation floor

Run these when their scope is relevant; Phase 2 will replace this list with the
unified root-health command:

```powershell
python 00-BRAIN\scripts\validate_boot_chain.py
python 00-BRAIN\scripts\wiki_lint.py --strict
python 00-BRAIN\scripts\frontmatter_audit.py
python 00-BRAIN\scripts\sync_shared_skills.py --check
git diff --check
git status --short
```

A command exiting successfully is not proof when its output still reports findings.
Record both exit behavior and classified totals.

## Phase sequence

0. Stabilize the baseline and concurrency lanes.
1. Establish canonical launch-independent Claude safety.
2. Build one truthful root-health gate.
3. Reconcile live semantic interfaces.
4. Design and pilot the separated metadata schema.
5. Migrate metadata realm by realm.
6. Repair links, paths, navigation, skills, commands, and source routing.
7. Run final cross-system acceptance and independent review.

## Stop conditions

Stop immediately if a phase encounters concurrent edits in an owned file, requires
authority outside the approved scope, would alter raw/private content, cannot prove
a safe rollback boundary, or causes a previously passing high-confidence check to
fail. Report the exact condition instead of widening scope silently.
