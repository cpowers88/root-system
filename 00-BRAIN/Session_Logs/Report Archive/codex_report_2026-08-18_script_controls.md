---
type: report
timeline: reference
status: complete
tags: [governance, system-review]
created: 2026-08-18
---

# Codex Report — Stale-Overwrite Guard and Restore Verification

## Executive outcome

Codex implemented the two script-layer controls Chris approved on August 18, 2026:

1. `00-BRAIN\scripts\stale_overwrite_guard.py` — an on-demand Git guard that closes
   flag #100's uncontrolled stale-overwrite failure mode.
2. `00-BRAIN\scripts\verify_backup_restore.py` — an on-demand harness that proves a
   backup can be restored into a disposable target and that the restored repository
   passes `git fsck`.

Both tools ship with deterministic tests. Neither is wired into `root_health.py`.
Promotion into the health gate remains deferred until after August 24, per Chris's
explicit condition.

## Authority and scope

Chris approved implementation of proposal items #1 and #5 only. The following remained
out of scope:

- the script manifest;
- the `core\` / `safety\` / `maintenance\` / `domain\` restructure;
- the shared scanning-library refactor;
- the path-audit cluster disposition;
- any `.claude\` change, including flag #101's matcher;
- any `root_health.py` integration before August 24.

No `raw\` or `88-JOURNAL\` content was read or modified. No deletion, commit, push,
external message, credential action, or scheduled-task change occurred.

## Control 1 — stale-overwrite guard

### Failure addressed

Flag #100 recorded two authoritative files being silently replaced by stale content and
then committed as `1c7bebc`. The only live mitigation was remembering to inspect `git diff`,
which was session discipline rather than a deterministic control.

### Implemented behavior

The guard accepts explicit repository-relative paths or, by default, checks all currently
changed tracked files. It compares the worktree against Git history and returns:

- exit `0` — no high-confidence stale-overwrite signal;
- exit `1` — block: historical reversion or material shrink detected;
- exit `2` — the check itself could not run reliably.

It blocks on either of two evidence-backed signals:

- the worktree content exactly matches an older committed version, with CRLF/LF
  normalization for text; or
- the file has lost at least 20 lines and at least 35% of its `HEAD` line count.

The thresholds are intentionally conservative. The tool catches the measured #100 shapes
without treating small edits as failures. It does not claim to identify whether Drive or
an editor buffer caused the overwrite; it detects the dangerous result.

### Usage

Check all currently changed tracked files:

```powershell
python 00-BRAIN\scripts\stale_overwrite_guard.py --root .
```

Check named authoritative files:

```powershell
python 00-BRAIN\scripts\stale_overwrite_guard.py --root . -- `
  00-BRAIN\SYSTEM_FLAGS.md NOW.md
```

## Control 2 — restore-verification harness

### Failure addressed

The backup layer had evidence that backup jobs completed, but no deterministic proof that
the resulting mirror or snapshot could be restored as a working repository. Job success
and restore success are different claims.

### Implemented behavior

The harness:

1. accepts the sentinel-owned live mirror or selects the newest snapshot carrying
   `.snapshot_complete`;
2. refuses to write into a non-empty restore target;
3. copies through quiet `robocopy` output (`/NFL /NDL`) so it does not enumerate or print
   journal filenames;
4. verifies the restored tree contains `00-BRAIN\AGENT.md`;
5. optionally restores the separately backed-up external gitdir and rewrites the disposable
   restore's `.git` pointer to that restored copy;
6. requires `git fsck --no-dangling` to pass; and
7. retains the restored target for human inspection instead of deleting it.

The harness never purges or reuses a populated target.

### August 23 live-review command

Use a newly created, empty target path. The expected current layout is:

```powershell
python 00-BRAIN\scripts\verify_backup_restore.py `
  --mirror 'D:\BACKUPS\.ROOT' `
  --git-backup 'D:\BACKUPS\.ROOT-git' `
  --restore-target 'D:\BACKUPS\restore-tests\2026-08-23'
```

To test the newest completed retained snapshot instead of the live mirror:

```powershell
python 00-BRAIN\scripts\verify_backup_restore.py `
  --mirror 'D:\BACKUPS\.ROOT' `
  --snapshot-root 'D:\BACKUPS\snapshots' `
  --latest-snapshot `
  --git-backup 'D:\BACKUPS\.ROOT-git' `
  --restore-target 'D:\BACKUPS\restore-tests\2026-08-23-snapshot'
```

The August 23 run is still required. Unit tests prove harness logic and safety boundaries;
they do not substitute for restoring the live D: backup.

## Verification evidence

Seven deterministic unit tests passed on Python 3.14:

- exact historical reversion blocks;
- material shrink blocks;
- a small ordinary edit passes;
- incomplete snapshots are ignored;
- a non-empty restore target is rejected;
- an unmarked mirror is rejected; and
- robocopy aggregate totals parse correctly.

Both production scripts passed `py_compile`. The stale-overwrite guard ran against its own
live five-file tracked change set and passed. `git diff --check` passed.

The unchanged canonical health gate returned **PASS WITH DEBT**:

- boot and governance: pass;
- wiki/navigation: 0 blockers, 1 reviewed item, 710 expected items;
- metadata: 0 total and 0 new findings;
- shared-skill mirrors: pass;
- whitespace: pass;
- live Markdown text integrity: 1,552 files, 0 findings.

This is a passing result, not a claim that `.ROOT` is clean. The one reviewed navigation
item remains baseline debt.

## State changes

- Flag #100 moved from `SYSTEM_FLAGS.md` to the August closed-flags ledger.
- Its temporary forensic stub was removed from `SYSTEM_FLAGS_DETAIL.md`.
- `NOW.md` no longer presents #100's obsolete procedural mitigation as an open risk.
- Flag #101 remains open and unchanged.
- The session DAILY records implementation, evidence, boundaries, and next action.

## Findings and cautions

1. The bulk-work gate's read-only false positives are confirmed operating context. On
   Windows, expect the redirect when a Bash command has a bulk-shaped form. Do not widen
   `ALLOWED_SCRIPTS`; flag #101's proposed fix remains an explicit read-only verb exemption
   inside `.claude\`, which still requires Chris's separate approval.
2. The stale-overwrite guard is deliberately on-demand. Its thresholds need real-use
   observation before promotion into a recurring gate.
3. The restore harness has not yet run against the live D: backup. That is the decisive
   proof scheduled for August 23.
4. An unrelated untracked TCOM syllabus appeared while this work was being closed. It was
   preserved and excluded from this change.

## Deferred decisions

- **August 23:** run and inspect the live restore test; also perform flag #102's scheduled
  conflict-copy recheck.
- **After August 24 / monthly review:** decide whether to promote either control into
  `root_health.py`, based on false-positive behavior and the live restore result.
- **After August 24:** decide the path-audit cluster's disposition. The existing
  recommendation remains `maintenance\`, not health-gate integration or archive.
- Hold the manifest, folder restructure, shared scanning refactor, and `.claude\` changes
  until their separately approved decision points.

## Final status

The approved implementation is complete. Flag #100 has a deterministic on-demand control;
the backup layer now has a restore-test harness ready for its August 23 live consumer. The
working tree remains uncommitted and unpushed for Chris's review.
