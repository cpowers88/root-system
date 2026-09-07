---
type: report
timeline: now
status: finding-1-implemented
tags: [governance, system-health, git, technical-debt]
created: 2026-07-30
---

# Fresh System Load — Look-Back Review, Evening 2026-07-30

### Scope: full boot chain re-read (`AGENT.md`, `CLAUDE.md`, `CHRIS_CORE.md`, `SYSTEM_FLAGS.md`), `root_health.py`, `NOW.md`, today's `DAILY`, `opportunity-queue.md`, git state, and a structural pass over the vault looking for real, previously-uncaught improvement.

Today already produced heavy system work (physics teaching-method redesign,
a `.ROOT` operating-discipline report delivered in chat, Codex's counter-review).
This pass deliberately did not re-walk that ground. It verified the health
gate fresh, then went looking for a class of defect the gate structurally
cannot see. It found one.

---

## Health Gate

`python 00-BRAIN\scripts\root_health.py` → **PASS**, reviewed baseline, 1,471
files, 0 findings across boot/governance, wiki links (705 expected, 0
blockers), frontmatter, shared-skill mirrors, whitespace, and text integrity.
Not evaluated by the gate (by its own stated scope): semantic freshness,
review-cadence completion, source routing, and ordinary prose. Confirmed
`origin/main` and local `main` are 0 ahead / 0 behind — no push backlog.

---

## Finding 1 — Git's tracked index disagreed with the live folder names across ~200 files (FIXED — Chris approved same session)

**What:** `WHERE_IT_GOES.md` and its July 2026 rename work moved
`02-LIBRARY`'s reference folders and `00-BRAIN\HATS`/`SKILLS` to lowercase.
The disk folders really are lowercase — `00-school`, `ref-business`,
`ref-math`, `ref-meta-how-to-work`, `ref-misc`, `ref-programming`,
`ref-AI-automation`, `hats`, `skills`. But **git's tracked index still has
the old uppercase names** — `00-SCHOOL`, `REF-BUSINESS`, `REF-MATH`,
`REF-META-HOW-TO-WORK`, `REF-MISC`, `REF-PROGRAMMING`,
`REF-AI-AUTOMATION`, `HATS`, `SKILLS` — across **200 tracked file paths**
(184 under `02-LIBRARY`, 16 under `00-BRAIN`).

**Why `root_health.py` and `git status` both show clean:** this repo has
`core.ignorecase = true` (correct default on Windows). The renames almost
certainly happened via a plain OS-level rename/Explorer move, not `git mv`.
On a case-insensitive filesystem, git can't tell the difference between
"same path, different case" and "no change at all" without being told
explicitly — so the working tree looks fine locally, `git status` is silent,
and every doc, wikilink, and script that already uses the correct lowercase
path resolves fine on this machine. Nothing local ever surfaces it.

**Why it's real, not cosmetic:** `git remote -v` confirms this repo pushes
to a real GitHub remote (`cpowers88/root-system`), and local `main` is
fully in sync with `origin/main` — meaning **GitHub.com is showing the
stale uppercase folder names right now**, disagreeing with every internal
document that already treats the lowercase names as canonical
(`WHERE_IT_GOES.md`, `README.md`, `vault_map.md`, `current-position.md`'s
own `REF-AI-AUTOMATION` pointer at line 73 is a live example of the drift
leaking into an owner file). It would also break outright on the first
case-sensitive clone or CI runner (Linux, WSL on a native ext4 mount, any
GitHub Action) — every lowercase path reference in the vault would 404
against a materialized `00-SCHOOL/`.

**This is a distinct defect from `SYSTEM_FLAGS.md` #88.** #88 covered three
things: reconciling *docs* to lowercase (done July 29), `ref-AI-automation`'s
internal casing (`AI` vs `ai`, correctly left alone as not-cheap), and the
undocumented `coding_toolkit` folder. It never checked git's index against
disk. This finding is one layer underneath that — the rename never actually
reached git for any of the nine folders it touched.

**Fix — executed 2026-07-30/31, Chris approved directly:**

```
git mv 02-LIBRARY/00-SCHOOL 02-LIBRARY/00-SCHOOL-tmp
git mv 02-LIBRARY/00-SCHOOL-tmp 02-LIBRARY/00-school
git mv 02-LIBRARY/REF-AI-AUTOMATION 02-LIBRARY/REF-AI-AUTOMATION-tmp
git mv 02-LIBRARY/REF-AI-AUTOMATION-tmp 02-LIBRARY/ref-AI-automation
git mv 02-LIBRARY/REF-BUSINESS 02-LIBRARY/REF-BUSINESS-tmp
git mv 02-LIBRARY/REF-BUSINESS-tmp 02-LIBRARY/ref-business
git mv 02-LIBRARY/REF-MATH 02-LIBRARY/REF-MATH-tmp
git mv 02-LIBRARY/REF-MATH-tmp 02-LIBRARY/ref-math
git mv 02-LIBRARY/REF-META-HOW-TO-WORK 02-LIBRARY/REF-META-HOW-TO-WORK-tmp
git mv 02-LIBRARY/REF-META-HOW-TO-WORK-tmp 02-LIBRARY/ref-meta-how-to-work
git mv 02-LIBRARY/REF-MISC 02-LIBRARY/REF-MISC-tmp
git mv 02-LIBRARY/REF-MISC-tmp 02-LIBRARY/ref-misc
git mv 02-LIBRARY/REF-PROGRAMMING 02-LIBRARY/REF-PROGRAMMING-tmp
git mv 02-LIBRARY/REF-PROGRAMMING-tmp 02-LIBRARY/ref-programming
git mv 00-BRAIN/HATS 00-BRAIN/HATS-tmp
git mv 00-BRAIN/HATS-tmp 00-BRAIN/hats
git mv 00-BRAIN/SKILLS 00-BRAIN/SKILLS-tmp
git mv 00-BRAIN/SKILLS-tmp 00-BRAIN/skills
git commit -m "Reconcile git-tracked folder casing with live disk state (case-only rename, no content change)"
git push
```

Content was untouched — this only corrected the case git already thought
was true. Also fixed `current-position.md`'s two live stale-casing
pointers (`REF-AI-AUTOMATION` → `ref-AI-automation`, `00-SCHOOL` →
`00-school`), since they were live examples of the drift leaking into an
owner file. `root_health.py` re-verified PASS immediately before and after
(1,472 files, 0 findings). Verified the rename didn't disturb the
folder-icon customization system (`FOLDER_ICON_SYSTEM.md`): the renamed
`02-LIBRARY\ref-programming` still carries its `ReadOnly` folder attribute
and its `desktop.ini`'s `Hidden`/`System` attributes intact, because the
icon binding uses an absolute path to the shared `.folder-icons\v1\` asset
set, not a path relative to the folder being renamed — a plain `git mv`
rename can't break it.

**Scoped out on purpose:** a vault-wide grep after the fix found ~100
other live docs (guides, wiki `OPERATIONS.md`/`HOW_TO_USE.md`/`index.md`
files, `WHERE_IT_GOES.md`, `vault_map.md`, `AGENT.md`, `START_HERE.md`,
`ROOT_OPERATING_MANUAL.md`, etc.) that still mention the old uppercase
folder names in prose or path examples. These are functionally harmless —
Windows resolves paths case-insensitively regardless of what git tracks —
so this is cosmetic-consistency debt, not a broken-link defect; historical
`DAILY`/`Report Archive`/`System Update Log` entries were deliberately
excluded since editing them would falsify session history. A dedicated
link-text cleanup pass across the ~15–20 *live* (non-historical) docs in
that list remains open if Chris wants full consistency — not done in this
session to keep the fix scoped to what was actually approved.

**Standing-fix recommendation (still open):** `root_health.py` still can't
see this defect class recur, because the same `core.ignorecase` masking
applies to the next case-only rename too. A cheap permanent check: compare
`git ls-files`'s path casing against the actual on-disk casing for every
tracked directory, flag any mismatch. This is a genuine gap in the
canonical health gate, not a one-time fix — worth scoping as its own
approved change to `root_health.py` rather than folding in silently.

---

## Finding 2 — orphaned 0-byte scratch file in `tmp\` (minor, not fixed — flagging only)

`tmp\path_reference_audit_baseline_2026-07-24.json` is 0 bytes, dated
2026-07-24, and referenced by nothing in the vault (checked). `tmp\` is
explicitly transient/generated scratch space per `.gitignore`'s own
comment, so this carries no real cost — noting it only because it was
found; attempted to delete it directly and the deletion was not authorized
this session, so it's left in place. Not worth a flag-table row; delete on
sight next time `tmp\` gets touched, or ignore indefinitely — it's free.

---

## What did not turn up new findings

- Frontmatter, wikilinks, whitespace, shared-skill mirrors: all clean per
  `root_health.py`.
- `SYSTEM_FLAGS.md`: no HIGH flags open; five MEDIUM/LOW flags, all with a
  named owner and check date, none stale beyond their stated cadence.
- `ref-field-operations\` and `ref-health\` (untracked, disk-only,
  92MB+ of PDFs/xlsm) looked like an integrity gap on first read — verified
  against `.gitignore` and confirmed intentional: binary/reference material
  is Drive-backed by design, not a git gap.
- git push state: local `main` and `origin/main` are even; no commit
  backlog behind today's heavy edit volume.

---

## Recommendation Summary

| # | Finding | Class | Action |
|---|---|---|---|
| 1 | Git index carries stale uppercase casing for 9 folders / 200 files vs. live lowercase disk state; already live on GitHub | structural / cross-surface risk | Chris approves the `git mv` sequence above; then scope a `root_health.py` case-drift check as a separate follow-up |
| 2 | 0-byte orphaned file in `tmp\` | trivial | No action needed; free to delete whenever `tmp\` is next touched |

Nothing here blocks or displaces tomorrow's live physics validation runs or
Python Stage 4b — both remain the real next actions per `NOW.md`.
