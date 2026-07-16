---
type: plan
tags: [now, governance, audit]
status: active
created: 2026-07-15
---

# Phase 2 — One Truthful Root-Health Gate

## Outcome

One Windows-safe, read-only command reports the health scopes it actually checks,
returns nonzero for a blocker or new metadata debt, distinguishes reviewed baseline
debt from a clean system, and is available through one synchronized shared skill.

## Evidence

- Checkpoint baseline: `bac8ef3` (`Phase 1: centralize Claude safety without
  shrinking capability`).
- Health is fragmented across boot, wiki, frontmatter, and shared-skill commands.
- `wiki_lint.py --strict` reports 0 blockers / 0 review debt / 716 expected, but
  `is_physics_planned()` ends in `or hub.name == "PHYSICS"`; every unresolved
  PHYSICS link is therefore exempt, including a typo on an active page.
- Wiki links are resolved by basename anywhere in the vault, so a path-qualified
  link can falsely pass because an unrelated file shares the same stem.
- `frontmatter_audit.py` reports 620 findings (0 missing frontmatter, 100 missing
  `type`, 520 timeline findings) and exits 0 regardless of debt.
- No reviewed frontmatter baseline, JSON mode, `root_health.py`, or `root-health`
  skill exists.
- `session-close` names `AGENT.md` and `CASTLE\OPERATIONS.md` without their
  vault-relative paths.
- Phase 0 found a validator gap for disallowed control characters and bare CR path
  corruption; no health gate owns that check yet.

## Owned paths

- `00-BRAIN\scripts\wiki_lint.py`
- `00-BRAIN\scripts\frontmatter_audit.py`
- `00-BRAIN\scripts\frontmatter_baseline.json`
- `00-BRAIN\scripts\root_health.py`
- `00-BRAIN\SKILLS\root-health\SKILL.md`
- `00-BRAIN\SKILLS\session-close\SKILL.md`
- generated `.agents\skills\root-health\SKILL.md` and
  `.claude\skills\root-health\SKILL.md`
- generated session-close mirrors
- `00-BRAIN\Session_Logs\ROOT_REMEDIATION_PHASE_LOOP_2026-07-15.md`
- `ROOT_OPERATING_MANUAL.md`
- this phase brief

## Exclusions

- Claude's concurrent school-learning files and its uncommitted DAILY append are
  preserved and excluded. Tests may simulate PHYSICS in a temporary directory but
  may not edit live EDUCATION, PHYSICS, or PYTHON content.
- `.claude` safety policy, `NOW.md`, CASTLE content, metadata migration, source
  routing, project-status repair, review-cadence repair, and broad semantic/path
  cleanup are deferred to their owning phases.
- `88-JOURNAL` is never traversed. Raw files are not read by these checks.
- Root-health PASS must not be described as proof of semantic freshness, project
  truth, source ownership, or zero metadata debt.

## Acceptance tests

1. `python 00-BRAIN\scripts\root_health.py` runs all named scopes and returns 0
   only when there is no blocker or new baseline debt.
2. Default output says `PASS WITH DEBT`, names the 620 reviewed findings as
   baseline debt, and lists scopes not evaluated.
3. `root_health.py --strict` returns nonzero while any frontmatter debt remains;
   `--json` emits parseable machine-readable results.
4. Frontmatter baseline mode detects new finding identities even if another finding
   is resolved in the same run; default report and zero-debt strict modes remain
   distinct.
5. Wiki path-qualified links resolve to the intended path, not a vault-wide stem.
   A temporary active-PHYSICS typo self-test returns nonzero without touching the
   live PHYSICS hub.
6. Boot, wiki, skill, control-character, staged-diff, and unstaged-diff checks are
   represented by name; a failing child check makes root-health return nonzero.
7. Canonical `root-health` and `session-close` skills validate and match both
   generated mirrors.
8. Existing boot, live wiki, and diff checks do not regress.

## Rollback boundary

The Phase 2 diff begins at `bac8ef3`. The generated baseline is review evidence,
not a migration. The phase can be reverted without altering Phase 1 settings or
Claude's concurrent school work.

## Human decision

After Pass 1 and the requested two refinement loops, Chris chooses **approve**,
**revise once more**, **hold**, or **reject**. Phase 3 cannot start before that stop.

## Pass record

### Pass 0 — baseline

- Root-health command/skill: absent.
- Wiki strict: false-clean 0 blockers / 0 review / 716 expected.
- Frontmatter: 620 known findings, unconditional exit 0, no baseline identity set.
- Shared skills: 4 canonical / 2 mirrors, PASS.
- Boot: PASS (30/1094).
- Working tree: Phase 1 clean except Claude's later DAILY school-session append,
  which is excluded from this checkpoint.

### Pass 1 — implementation

- Added `root_health.py` as one read-only Windows-safe command over six named
  scopes: boot/governance, wiki navigation, frontmatter/timeline metadata,
  shared-skill mirrors, working-tree whitespace, and live Markdown text bytes.
- Default health result: `PASS WITH DEBT`, exit 0, with 0 wiki blockers, 4 wiki
  review findings, 773 expected unresolved links, and 620 reviewed frontmatter
  findings (0 new / 0 resolved).
- Strict result: `STRICT FAILURE`, exit 1, because the four review links and 620
  metadata findings violate a zero-debt acceptance condition. They are not
  mislabeled as live blockers.
- Added deterministic JSON output, reviewed finding identities, baseline-writing
  mode, and an explicit list of scopes the gate does not evaluate.
- Corrected path-qualified wiki resolution and narrowed the PHYSICS planned-page
  exemption. The four newly visible review findings are two proposed
  AI_AUTOMATION links and two PHYSICS links; Phase 2 reports them but does not edit
  their owning content.
- Added and validated the canonical `root-health` skill; synchronized five
  canonical skills across both generated mirrors. Updated `session-close` with
  exact rule paths and a conditional health step for system changes only.
- Documented the health command and status meanings in `ROOT_OPERATING_MANUAL.md`.
- Claude's concurrent changes to the DAILY, `NOW.md`, PHYSICS current position,
  and PHYSICS log remain excluded and unstaged by this phase.

### Loop 1 — adversarial refinement

- The first wiki self-test used a temporary directory, which exposed a Windows
  temporary-folder permission failure. Replaced it with a fully synthetic,
  no-write fixture so the check is deterministic and never touches live school
  files.
- The first path resolver was too narrow and exposed hundreds of false review
  links. Adding the hub's `wiki` anchor retained path truth while reducing live
  review debt to the four genuinely unresolved items.
- Added a frontmatter identity self-test proving that one new and one resolved
  finding are detected even when the total remains unchanged.
- Compacted root-health JSON so it reports counts and only changed identities
  instead of printing all 620 baseline records. Child launch, timeout, and JSON
  parse failures now become explicit gate failures.
- Refined strict wording to distinguish zero-debt failure from a live blocker,
  while preserving nonzero exit behavior.

### Validation after Loop 1

- `root_health.py`: `PASS WITH DEBT`, exit 0.
- `root_health.py --strict`: `STRICT FAILURE`, exit 1 as designed.
- `root_health.py --json`: parseable compact result.
- Wiki synthetic typo self-test: PASS.
- Frontmatter equal-count identity self-test: PASS.
- Boot chain: PASS (30 boot files; 1095 live pages).
- Shared skills: PASS (5 canonical; 2 mirrors).
- Root-health and session-close skill validation: PASS.
- Live Markdown text integrity: PASS (1155 checked; 0 findings; raw, archive,
  journal, and other named excluded areas not traversed).
- Working-tree whitespace: PASS.

### Loop 2 — requested final refinement

Improvement contract:

- **Quality dimension:** false-pass resistance at the commit boundary.
- **Baseline:** the gate checked one of two Git diff states—unstaged changes—but
  did not inspect content already staged for commit.
- **Target:** 3–10% improvement without widening Phase 2.
- **Bounded change:** add a separate read-only `git diff --cached --check` child
  and keep the existing unstaged check; name both in human and JSON output.
- **Measured result:** commit-state whitespace coverage moved from one of two
  states to two of two; named health checks moved from six to seven. This exceeds
  10% because the uncovered state is binary and closing it removes a concrete
  false-PASS path rather than adding optional scope.
- **Stop decision:** keep. Both staged and unstaged checks pass, the default and
  strict health contracts remain unchanged, and no school/raw/private file was
  edited.

The run-level loop procedure was also refined. Every future loop must now name a
quality dimension, observable baseline, 3–10% target, bounded causal change,
measured result, and stop decision. The range is explicitly a design target—not a
quota—and binary correctness exceptions must be explained.

### Final validation after Loop 2

- `root_health.py`: `PASS WITH DEBT`, exit 0; JSON lists seven named checks.
- `root_health.py --strict`: `STRICT FAILURE`, exit 1 as designed.
- Wiki: 0 blockers / 4 review / 773 expected.
- Frontmatter baseline: 620 reviewed / 0 new / 0 resolved.
- Staged whitespace: PASS.
- Unstaged whitespace: PASS.
- Wiki synthetic typo self-test: PASS.
- Frontmatter equal-count identity self-test: PASS.
- Boot, shared-skill mirrors, and live Markdown text integrity: PASS.

## Phase 2 review stop

Implementation and two refinement loops are complete. Phase 3 remains closed
until Chris chooses **approve**, **revise once more**, **hold**, or **reject**.
