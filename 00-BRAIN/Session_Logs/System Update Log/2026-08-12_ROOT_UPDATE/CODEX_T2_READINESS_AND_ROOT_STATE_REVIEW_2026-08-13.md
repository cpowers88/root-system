---
type: report
timeline: now
status: complete
tags: [update, phase-d, t2, root-state, governance, codex-review]
created: 2026-08-13
---

# Codex T2 readiness and `.ROOT` state review — August 13, 2026

## Verdict first

**Correction from Chris after this review was filed:** T2 does not wait for or trigger the
completed `OK TO START`. It is one bounded component of a broader pre-release program. The
pause remains until the live Markdown estate is justified, an operational and optimized
`.ROOT` has been tested, semester-critical paths are ready, and the remaining release
evidence is added to the `OK TO START` statement next week.

**Proceed with T2 inside that readiness program, but execute a narrower, current-state
version of the approved proposal.** The direction is right: always-load the
constraints needed to act safely, load the forensic history only when a flag is being
reviewed or worked. `SYSTEM_FLAGS.md` is still the only unbounded boot-load term and is
currently 1,976 words—29% of the measured 6,881-word Codex boot chain.

The proposal must be reconciled before execution because its “three live prohibitions” are
now stale. Flag #94 closed this morning. **Do not resurrect it as an open flag or keep it in
the live prohibition register.** Its durable lesson is already embodied in the restored
Educator hat and should govern T2's design review, not remain as false open state.

T2 should therefore preserve **two currently open boot-time prohibitions** in full:

1. **#97 — DO NOT DEDUPE `raw\` ON HASH; never write under `raw\`.** The five missing
   sources survive only as filenames, and hash-only reasoning loses evidence.
2. **#96 — the enforced bulk-work hook covers Bash, not PowerShell.** Do not claim the
   control covers bulk work generally; Windows bulk execution still depends on discipline
   plus the safe-shell route where applicable.

The remaining open flags (#57, #16, #69, #93) should stay visible as compact index rows with
severity, owner, next check/action, and a direct detail pointer. Their forensic narratives
may move; their existence and firing conditions may not disappear from discoverable state.

## Current direction and state

`.ROOT` is pointed correctly at its North Star: convert learning and judgment into verified
capability, useful output, and durable economic value while preserving school commitments
and Chris's authority. The current update is improving the right target—**pathways and load,
not folder-name churn**—and today moved seven of eight planned items to completion. T2 is the
only unfinished update item.

The architecture is increasingly coherent:

- `NORTH_STAR.md` owns durable direction and authority.
- CASTLE and `NOW.md` own sequencing and visible state.
- Domain hubs own evidence and learner truth.
- The System Loop and Return Packet provide a single cross-system lifecycle.
- Hats are conditional operating modes; skills hold repeatable procedures.
- Session logs preserve proof and decisions without silently becoming governance.

The update also produced real proof rather than cosmetic organization: skill mirrors now
fail on missing references, the teaching model again loads where it is used, the backup was
restore-tested with a negative control, TCOM gained a testable course structure, stale live
references were repaired, and GitHub is now synchronized with local `main`.

## Health evidence

The canonical read-only gate returned **PASS WITH DEBT**, exit 0:

- boot and governance: PASS;
- wiki navigation: 0 blockers, 4 review items against an expected-debt baseline of 710;
- frontmatter/timeline metadata: 0 findings across 1,479 checked files;
- shared skill mirrors: PASS, with `_staged\handoff\` still explicitly awaiting disposition;
- staged and unstaged whitespace: PASS;
- live Markdown text integrity: 1,528 files, 0 findings.

This is healthy enough for T2, but it is not a clean-system claim. The gate does **not**
evaluate semantic freshness, review-cadence completion, source ownership/routing,
duplicate-source disposition, or ordinary prose outside its named contracts.

## Best current reading of the folder structure

The top-level structure is not the main problem. The owner boundaries are understandable and
mostly sound: brain/governance, North Star, library/projects, domain wikis, school, business,
inbox, and archive. The strongest optimization is to reduce duplicated state and make every
transition discoverable through its owner—not to rename or flatten the vault.

Three structural risks remain:

1. **Truth propagation is the dominant reliability risk.** The council's C1 pattern—correct
   detection followed by stale downstream state—reappeared in `NOW.md` and in the T2 proposal
   itself. Every phase close needs an explicit owner/index/cockpit propagation check.
2. **Controls are uneven across execution surfaces.** Bash bulk work has a measured gate;
   PowerShell does not. The system must describe this boundary exactly until it changes.
3. **The health gate is intentionally bounded.** Four known wiki review items remain, and a
   passing structural gate cannot certify semantic truth or source routing.

The empty `tmp\`, `outputs\`, and `...projectSuccess\` shells are cleanup residue, not a T2
dependency. They should remain Chris-owned because removing them is destructive and current
controls correctly stopped automated deletion attempts.

## T2 optimized execution contract

### Scope to execute now

1. Create `00-BRAIN\SYSTEM_FLAGS_DETAIL.md` as the complete forensic owner for all current
   open-flag narratives.
2. Rewrite `SYSTEM_FLAGS.md` as the always-loaded operational register:
   - PAUSED banner and finding-freeze state;
   - severity/fix-by rule;
   - full imperatives for open #97 and #96;
   - one compact row for every other open flag, retaining severity, owner, check moment, and
     detail link;
   - closed-ledger pointer.
3. Align the three load statements in the same change:
   - session start continues to load slim `SYSTEM_FLAGS.md` every session;
   - File Safety rule 7 points system/file-write/review work to
     `SYSTEM_FLAGS_DETAIL.md` in addition to the slim register;
   - the slim file continues to identify itself as every-session context.
4. Update the controlling plan and current-state records in the same session so the T2
   proposal cannot remain marked proposed after execution.

### Do not mix into T2

- Do not touch `AGENT.md` Execution Discipline; Chris deferred it to a dedicated pass.
- Do not perform the broader proposed `AGENT.md`, profile, or `CHRIS_CORE.md` slimming in
  this change. Those rows require their own counter-example review and are not needed to
  close T2's core defect.
- Do not work the newly filed freeze findings.
- Do not modify `raw\`, access `88-JOURNAL\`, remove folder shells, or change historical logs.

This smaller scope produces most of the benefit with materially less governance blast
radius. It also makes rollback and behavioral attribution straightforward.

## Acceptance gate

T2 is complete only if all of the following pass:

1. Every open flag number appears in the slim file and resolves to its full detail.
2. #97 and #96 retain their operative prohibitions in the slim file itself—not only behind a
   link.
3. Closed #94 does not reappear as open state.
4. `validate_boot_chain.py` passes with no dangling reference.
5. `root_health.py` returns exit 0 and is reported honestly as PASS or PASS WITH DEBT.
6. Shared-skill mirror check and both whitespace checks remain green.
7. Always-load word count is re-measured from the actual Codex/Claude boot chains, not from
   `BOOT_FILES`, and the measurement method is recorded.
8. A fresh session that does not open `SYSTEM_FLAGS_DETAIL.md` can state the pause/freeze,
   #97, and #96 correctly; a session asked to work #93 can find its owner, approval state,
   proposal, and next exact action.
9. `UPDATE_PLAN.md`, `NOW.md` when materially changed, and the DAILY record agree that T2 is
   complete. No stale “proposed/not started” live status remains.
10. Name a check moment: re-test the split at the Friday gate and again at the next monthly
    review; keep/modify/revert based on fresh-session behavior and flag discoverability.

## Priority after T2

1. Run Friday's technical gate, then the TCOM/CSE/PHYS structure test Chris defined. This is
   the real proof that the system supports learning, not merely files.
2. At the next authorized review, address the PowerShell enforcement gap and the
   read-only-classification false positives as one control-design problem.
3. Preserve the four known wiki-navigation review items as debt; do not let them displace the
   Friday learner test unless one becomes a blocker.
4. Decide `_staged\handoff\` disposition at its named review point rather than allowing a
   permanent warning to become background noise.

## Return Packet

- **Outcome:** independent review supports T2 with a reduced, current-state scope and ten-part
  acceptance gate.
- **Evidence:** live boot/governance files, current update packet, council verdict, relevant
  Operator/Software Engineer hats, current Git state, and the canonical health gate.
- **Capability/status movement:** the review now feeds the broader readiness program; T2
  remains not started, and `.ROOT` remains PAUSED through the Markdown-justification and
  operational-testing gate.
- **Reusable-asset candidate:** no; this is vault-specific governance evidence.
- **System-learning candidate:** yes—proposal artifacts must be reconciled against live flag
  state immediately before execution. File this under the current finding freeze; do not add
  a new flag unless the pattern repeats or causes material failure.

No `raw\` content or `88-JOURNAL\` was accessed or modified. No external action was taken.
