---
type: report
timeline: now
status: active
tags: [scripts, governance, review, reconciliation]
created: 2026-08-16
session_date: 2026-08-16
---

# Scripts Layer — reconciled review of Codex's audit

### Requested by Chris 2026-08-16 (Sunday night). Codex reviewed `00-BRAIN\scripts\`; this is the lead's independent verification and integration, per `AGENT.md` Execution Discipline 6. **Every claim below was re-measured against the live tree — no Codex finding was adopted on trust.** No scripts changed.

---

## Verdict in three sentences

**Codex's file-by-file analysis is accurate and worth keeping** — I confirmed its two
most important findings and one of them is worse than it reported. **Its sequencing is
wrong for this week.** It proposes seven new scripts eight days before classes begin,
during an explicit finding freeze, while the rehearsal gate has carried three days —
which is the exact failure mode (`UPDATE_PLAN.md`: *"Thursday finds new defects and
expands"*) that ended the three previous attempts at this update.

---

## 1. What Codex got right — verified, not assumed

| Claim | Verification |
|---|---|
| 21 files reviewed | ✅ 22 at top level, of which one is a hidden Windows `desktop.ini`. Codex correctly excluded it. **`vault_map.md`'s "22 scripts" counts the stub as a script — the map is wrong** |
| `path_reference_audit.py` does not exclude `raw` | ✅ Line 23–24: `SKIP_DIRS = {".git", ".obsidian", ".trash", ".tmp.driveupload", "88-JOURNAL", ".venv", "venv", "node_modules", "__pycache__"}`. No `raw` |
| `folder_icons.ps1 -Mode Audit` is not read-only | ✅ **and worse — see §3** |
| Graph colors have drift | ⚠️ **half stale — see §2** |
| Both scheduled tasks healthy | ✅ `ROOT Daily Backup to D` and `ROOT Evening Reading Brief`, both last result **0**, next runs Aug 17 12:30 and 17:00 |
| The two tag converters are archive candidates | ✅ **Both return zero.** `convert_legacy_tag_families --check` → *0 files would be changed; 0 skipped*. `convert_domain_stack_tags --check` → *0 files would be changed*. **This is the "final zero-match check" Codex asked for, and it passes** |
| Exclusion logic is inconsistently duplicated | ✅ real, but the cause is different from what Codex described — see §4 |

---

## 2. What Codex got wrong or stale

**1. The graph-colors finding is half stale.** Codex reported *"Unclassified folders:
outputs and tmp."* Live `--check` now says:

```
DRIFT CHECK — clean: every folder is either colored or excluded.
```

`tmp\` was deleted this evening, and nothing is unclassified. **What remains is only the
`.vs` exclusion** — 16 groups vs 17 generated. One real item, not three.

**2. "Not safe for AI use across the live vault" overstates the path auditor's risk.**
Codex's framing implies a write hazard. It is not one: `path_reference_audit.py` writes
**only to stdout** (`json.dump(report, sys.stdout)`, line 246). It cannot touch `raw\`.

`raw\` immutability governs **writes** — `NORTH_STAR.md` §3 and `AGENT.md` File Safety 9.
Reading `raw\` is not prohibited; only `88-JOURNAL` is never-read, and that **is** excluded.

The real defect is narrower and still worth fixing: the tool **reads immutable evidence
content into a report**, and it is inconsistent with every sibling tool. That is a
correctness and disclosure problem, not a safety-boundary breach. **Getting this right
matters** — misclassifying it as a raw-immutability violation would justify emergency
work that the finding does not warrant.

**3. `_validation_yaml\` is missing from the inventory entirely.** Codex reviewed 21 files
and 0 of the 2 subdirectories. `00-BRAIN\scripts\_validation_yaml\` contains nothing but
`__pycache__\yaml.cpython-314.pyc` — **a compiled cache whose source `.py` no longer
exists**, dated July 15. It is untracked in git. Harmless, but it is exactly the kind of
orphan a folder audit exists to catch.

---

## 3. What Codex under-reported — `folder_icons.ps1` has a safety flag that does nothing

Codex: *"Audit mode is not actually read-only: it always exports folder-icon-audit.csv.
The name and behavior should agree."* True, and three details make it materially worse:

```powershell
[string]$Mode = 'Audit',     # line 4  — Audit is the DEFAULT
[switch]$DryRun,             # line 5  — the script HAS a dry-run switch
...
[System.IO.Directory]::CreateDirectory($AssetRoot) | Out-Null   # line 619 — creates a directory
$rows | Export-Csv -LiteralPath ... 'folder-icon-audit.csv'     # line 620 — writes a file
```

Neither line 619 nor 620 is guarded by `$DryRun`.

1. **`Audit` is the default mode** — running the script with no arguments writes.
2. **It creates a directory**, not only a file.
3. **`-DryRun` is silently ignored in this path.** Passing the script's own safety flag
   does not prevent the writes.

Point 3 is the finding. A dry-run flag that does not suppress writes is a **false control**
— precisely the category `AGENT.md` File Safety 12 names as *"not a control."* Someone
reaching for `-DryRun` believes they are safe and is not. That belongs in the same class
as the inert `sandbox` block, and it should be recorded as such.

---

## 4. Where I disagree on the diagnosis — the shared library largely already exists

Codex's recommendation #2 (priority 36) is to build a shared vault-scanning module and
migrate five tools onto it. **The shared exclusion set already exists and three tools
already import it.**

`frontmatter_audit.py` line 28 owns the complete, correct set:

```python
EXCLUDED = {"99-ARCHIVE", "raw", ".raw ARCHIVE", ".git", ".obsidian",
            "Report Archive", "77-INBOX", "88-JOURNAL", ".claude", ".agents",
            "SKILLS", "skills", ".venv", "venv", "node_modules", ".pytest_cache",
            "oracleJdk-26"}
```

And three scripts consume it directly:

| Script | Line |
|---|---|
| `metadata_migration_plan.py` | 17 — `import frontmatter_audit as audit` |
| `convert_legacy_tag_families.py` | 27 — `import frontmatter_audit as audit` |
| `convert_domain_stack_tags.py` | 64 — `audit.EXCLUDED.intersection(rel.parts)` |

**So the pattern is established, and `path_reference_audit.py` is the one script that
declined it** and rolled its own weaker set. That reframes the fix:

- **Codex's read:** no shared library → build one → migrate five tools. Effort 2.
- **What is actually true:** an informal shared set exists with 3 of 4 consumers already
  on it. **Pointing the fourth at `audit.EXCLUDED` closes the safety inconsistency in
  roughly one line.**

The proper library — vault-root resolution, safe iteration, frontmatter parsing,
read-only helpers — is still worth building. But it is a **refactor for value, not a
safety fix**, and it should not be priced as though the safety gap depends on it.
The safety gap costs one line; the library costs a weekend.

---

## 5. What Codex missed — the path-audit cluster is a dead subsystem

Codex issued four separate "Keep" verdicts to four files without noticing they are one
unintegrated unit:

- `path_reference_audit.py`
- `path_reference_baseline.json`
- `path_reference_audit.schema.json`
- `test_path_reference_audit.py`

**Measured:**

| Question | Answer |
|---|---|
| Is it in the health gate? | **No.** `root_health.py` orchestrates exactly four subprocesses: `wiki_lint.py`, `frontmatter_audit.py`, `validate_boot_chain.py`, `sync_shared_skills.py --check` |
| Does anything invoke its test? | **No.** `test_path_reference_audit.py` has **zero references anywhere in the vault** — not in `root_health.py`, not in `settings.json`, not in any document |
| Where is it referenced at all? | 11 files, and **every one is a session log, an archived DAILY, a CASTLE log entry, or a July 24 architecture-update document.** Zero operational references |
| Does its test pass? | Yes — `path_reference_audit fixtures: PASS` |

**Reading: it was built for the 2026-07-24 architecture update, used for that job, and
never integrated.** Four files — **19% of the folder** — sit in the permanent operational
layer, called by nothing, carrying the one exclusion gap in the whole layer.

That is the single largest structural finding in `scripts\`, and it deserves a decision
rather than four "keeps." **It is not mine to make** — the honest options are: wire it
into the health gate (after fixing the exclusion set), move it to a `maintenance\`
grouping as an on-demand tool, or archive it with the July 24 update it served. My
recommendation is the second: it does real work, it is simply not a daily gate.

---

## 6. The sequencing disagreement — this is the part that matters this week

Codex proposes **seven new scripts**. Several are genuinely good ideas; the stale-overwrite
guard (its #1) directly addresses flag #100, and the restore-verification harness (#5)
addresses a real gap between *"the backup job succeeded"* and *"the backup restores."*

**Three reasons not to start them now:**

1. **The finding freeze is operative and binds every surface, Codex included.**
   `SYSTEM_FLAGS.md`: new findings are **filed** to `UPDATE_PLAN.md`, not worked. A report
   commissioned during the freeze does not lift it.
2. **Codex's #1 collides with a ruling already on record.** `NOW.md` risk 0 states a real
   control for the stale-overwrite class is *"worth designing after the semester starts,
   not before."* Codex scores it 40 and puts it first. It is not wrong on merit — it is
   proposing to reverse a dated decision without knowing it exists. **That is Chris's call
   to reverse, not the report's.**
3. **Eight days to Aug 24, and the rehearsal gate has carried three days.** Building seven
   tools is exactly the expansion the freeze exists to prevent.

---

## 7. Recommended sequence

**Now — under the freeze, because each is a correction, not a new finding (≈20 minutes):**

| | Action | Why now |
|---|---|---|
| 1 | Point `path_reference_audit.py` at `frontmatter_audit.EXCLUDED` | One line; closes the only exclusion inconsistency in the layer |
| 2 | Guard `folder_icons.ps1` lines 619–620 with `$DryRun` | A safety flag that does nothing is worse than no flag |
| 3 | Archive the two tag converters to `99-ARCHIVE\...\completed-migrations\` | Codex's own gate passed — both report zero |
| 4 | Correct `vault_map.md`'s script count 22 → 21 | The map is wrong today |

**After `OK TO START` — filed to `UPDATE_PLAN.md`, not worked:**

- Decide the path-audit cluster's home (§5)
- Codex's structure proposal (`core\` / `safety\` / `maintenance\` / `domain\`) — good, and
  purely cosmetic until the above is settled
- The script manifest (its #4) — the right container for everything this review measured
- The shared scanning library as a **refactor**, correctly priced (§4)
- Relocate `fetch_fred.py` out of system infrastructure
- Delete `_validation_yaml\` — an orphaned `.pyc` with no source

**Chris's decision, not filed:** whether to reverse the risk-0 ruling and build the
stale-overwrite guard before Aug 24. **My recommendation: no.** It is the right tool and
the wrong month; it guards a failure mode whose procedural mitigation (`git diff` before
committing) has held since it was written this morning.

---

## 8. One live data point this review produced

The reference-tracing step was **blocked by the bulk-work gate** — a read-only loop
counting how many files mention each script name. This is **flag #101 firing during a
review of the scripts layer it governs**, and it is the sixth recorded instance. The
finding stands as filed: the gate matches shell *shape*, not write intent.

---

*Method: live filesystem inventory; `SKIP_DIRS`/`EXCLUDED` read from source; import graph
traced; `root_health.py` subprocess list read directly; reference counts measured across
the vault excluding `99-ARCHIVE` and `.git`; `build_graph_colors --check`,
`convert_legacy_tag_families --check`, `convert_domain_stack_tags --check` and
`test_path_reference_audit.py` all executed. No script modified. Scheduled-task state read
from the Windows task store, not from documentation.*
