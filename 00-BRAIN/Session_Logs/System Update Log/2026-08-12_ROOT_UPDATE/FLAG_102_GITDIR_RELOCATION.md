---
type: procedure
timeline: now
status: active
tags: [governance, flag-102, git, backup]
created: 2026-08-16
---

# Flag #102 — moving the gitdir out of the Drive-mirrored tree

### Written 2026-08-16 because the move cannot be completed from a session running inside VS Code. Everything except the move itself is already done and verified.

---

## ✅ EXECUTED 2026-08-16 18:14 — steps 1–3 complete. Only step 4 remains.

**The VS Code blocker was environmental, not permanent.** A later session the same
evening ran from Windows Terminal — `pwsh <- claude <- powershell <- WindowsTerminal`,
no `Code.exe` in the ancestry — with `Code`, `GoogleDriveFS`, `Obsidian` and
`GitHubDesktop` all confirmed not running. The rename succeeded first try.

| Step | Result |
|---|---|
| **1 — relocate** | `Reinitialized existing Git repository in C:/Users/chris/.root-git/`, exit 0 |
| **2 — verify (5 checks)** | `.git` is now a **33-byte file** (`-a-h-`) reading `gitdir: C:/Users/chris/.root-git` · `status` unchanged (same 6 modified + 1 untracked) · `HEAD 551670a` · `fetch` **exit 0** · `fsck` clean but for the known benign dangling blob |
| **3 — backup dry run** | All three expected markers present: external gitdir detected, **gitdir 751 files**, **estate 5,243 (vault + gitdir)**, third pass announced. Guard C **stayed silent** — the shrink tripwire did not fire, which is the whole point of measuring the gitdir back into the totals |
| **3 — backup real run** | exit 0, robocopy 3. `D:\BACKUPS\.ROOT-git` created: **752 files / 167.88 MB**, sentinel present, `HEAD` readable. Vault mirror 4,947 files / 3.39 GB. `D:\BACKUPS\.ROOT\.git` **purged as designed** — the history now lives in the sibling gitdir mirror, not inside the vault mirror |

**Step 4 could not run and is not a failure:** it requires Drive *live* to prove no
conflict copy returns, and Drive was not loaded. Run it the next time Drive is up.

**Flag #102 stays 🔴 until step 4 passes.** The cause is addressed but not yet
*proven* addressed, and this flag has already been widened once by measurement.

---

## Why this exists

Google Drive mirrors `C:\Users\chris\.ROOT`. Git rewrites `.git\refs\heads\main`
on every commit, fetch and pull. When Drive was mid-upload of that file during a
git write, it wrote a **conflict copy** beside it — `main (1)` — carrying a
null SHA and a refname git considers invalid. `git fetch` then failed outright:

```
fatal: bad object refs/heads/main (1)
```

Eight such files appeared on 2026-08-16, stamped at the exact second of each git
write (11:35:37, 12:16:53, 12:29:59). No object corruption ever occurred —
`git fsck` reported bad ref *names* only, and local and GitHub stayed in sync.

**Google Drive for desktop has no mechanism to exclude a subfolder from a
mirrored folder.** There is no setting to keep Drive and skip `.git`. So the
choice was: abandon the Drive mirror, accept a recurring manual cleanup only
Chris can perform, or move the repo metadata out of the mirrored tree.

**Chris chose the third on 2026-08-16.** It keeps the Drive mirror — which
exists to hold `88-JOURNAL`, every `raw\`, and 351 PDFs that GitHub excludes —
and removes the only part of the tree that breaks under sync. Nothing is lost by
moving `.git` out of Drive, because GitHub already holds the full history.

## What is already done and verified

| | State |
|---|---|
| The 8 conflict copies | ✅ gone |
| `git fetch origin` | ✅ exit 0 |
| `git fsck` | ✅ clean (one harmless dangling blob) |
| Local vs GitHub | ✅ both `52296bf` |
| Safety copy of `.git` | ✅ `C:\Users\chris\.ROOT-quarantine\2026-08-16_git_backup_before_move` — 744 files, byte-verified |
| `backup_to_d_drive.ps1` | ✅ patched, parse-clean, 4 tests passed |
| Empty target dir `C:\Users\chris\.root-git` | ✅ created |

**The immediate breakage is already fixed.** Git works right now. This procedure
is the durable fix that stops it recurring — it is not urgent, and it is safe to
do on any day.

## Why it could not be finished in-session

`git init --separate-git-dir` renames the `.git` directory, and Windows refuses
to rename a directory any process holds a handle on. GitHub Desktop, Obsidian and
Google Drive were all closed and the rename was **still** denied. The remaining
holder was VS Code — and the Claude Code session doing the work was running
inside VS Code's own integrated terminal:

```
pwsh.exe <- claude.exe <- pwsh.exe <- Code.exe <- Code.exe <- explorer.exe
```

Closing the blocker would have ended the session doing the closing.

---

## The procedure

**Run from Windows Terminal or PowerShell directly — NOT from a VS Code
terminal.** That is the whole point.

### Before you start

1. **Pause Google Drive** (tray icon → gear → Pause syncing).
2. **Close VS Code, GitHub Desktop, and Obsidian** entirely.

### Step 1 — relocate the gitdir

```powershell
cd C:\Users\chris\.ROOT
git init --separate-git-dir C:\Users\chris\.root-git
```

Expected: `Reinitialized existing Git repository in C:/Users/chris/.root-git/`

**If it still says `Permission denied`**, something else holds `.git`. Stop and
find it rather than forcing anything — nothing is broken, and retrying later
costs nothing.

### Step 2 — verify

```powershell
cd C:\Users\chris\.ROOT
Get-Item .git | Select-Object Mode, Name      # expect a FILE, not a directory
Get-Content .git                              # expect: gitdir: C:/Users/chris/.root-git
git status --short                            # expect: clean, or only known edits
git log --oneline -1                          # expect: 52296bf or later
git fetch origin; "fetch exit=$LASTEXITCODE"  # expect: exit 0
git fsck --no-progress                        # expect: no bad refs
```

All five must pass. If any fails, the safety copy restores the previous state:
`.git` can be rebuilt by copying
`C:\Users\chris\.ROOT-quarantine\2026-08-16_git_backup_before_move` back to
`C:\Users\chris\.ROOT\.git` and deleting the `.git` pointer file.

### Step 3 — prove the backup still protects the history

```powershell
& 'C:\Users\chris\.ROOT\00-BRAIN\scripts\backup_to_d_drive.ps1' -DryRun
```

Expected in the output — **check for all three**:

```
==> External gitdir in use: C:\Users\chris\.root-git
    gitdir: ~747 files
    estate: ~5,988 files (vault + gitdir)
==> [dry run] Mirroring gitdir C:\Users\chris\.root-git -> D:\BACKUPS\.ROOT-git
```

If it instead says `Gitdir is inside the vault`, the move did not take effect.

Then run it for real:

```powershell
& 'C:\Users\chris\.ROOT\00-BRAIN\scripts\backup_to_d_drive.ps1'
```

### Step 4 — resume Drive, then confirm the fix held

Resume Drive syncing, do one git write, and check that no conflict copy returns:

```powershell
cd C:\Users\chris\.ROOT
git fetch origin
Get-ChildItem C:\Users\chris\.root-git -Recurse -Force -Filter '*(1)*'
```

Expected: **no output** from the last line. That is the proof the flag is closed.
`.root-git` sits outside every Drive-mirrored folder, so Drive never touches it.

---

## What changed in `backup_to_d_drive.ps1`

The script previously mirrored `.ROOT` with `/MIR`, `.git` deliberately
included — its header records that excluding `.git` once produced *"a restore
from D: that produced an unversioned vault"* (defect 3). Moving the gitdir out
would have re-created that defect by a different route, and would also have
broken the backup outright. Both are handled:

| Problem | Fix |
|---|---|
| `/MIR` would purge `.git` from `D:\BACKUPS\.ROOT`, leaving a working tree with no history | **Third pass** mirrors the external gitdir to `D:\BACKUPS\.ROOT-git`, sentinel-guarded like the vault mirror |
| The gitdir is 747 files — **14.4%** of the measured 5,200. Removing it trips guard C's 10% shrink tripwire on **every** run, training the operator to reach for `-Force` | The gitdir is measured back **into** the totals guard C compares, so the tripwire stays continuous across the move |
| A hardcoded gitdir path could silently go stale | The path is **read from the `.git` pointer file at run time**. No second copy of it exists in the script |

The script now works **unchanged in either layout** and fails closed in three new
ways. All negative-tested 2026-08-16 in a scratch harness:

| Test | Result |
|---|---|
| Valid external gitdir → detected, measured, third pass runs | ✅ |
| `.git` points to a missing directory → guard trips, exit 1 | ✅ |
| `.git` is a file with no `gitdir:` line → guard trips, exit 1 | ✅ |
| Gitdir destination exists but unmarked → guard trips, **the file `/MIR` would have purged survived** | ✅ |
| Pre-move layout still behaves as before (5,241 files, exit 0) | ✅ |

## Do not do these

- **Do not sweep `*(1)*` files across the vault.** Live `(1)` files exist in
  `raw\`, `99-ARCHIVE` and `77-INBOX` dating to June–August and are **not** Drive
  debris. Only ones inside the gitdir, stamped at a git-write moment, are.
  This is `SYSTEM_FLAGS.md` prohibition 1 — flag #97's exact failure in a new
  costume.
- **Do not exclude `.git` from the backup** to make the shrink tripwire quiet.
  That is defect 3, already made once.
- **Do not widen `ALLOWED_SCRIPTS`** to work around any permission block met
  here. `AGENT.md` File Safety 12 names that as not-a-control.

## Still open, and separate

The stale **`G:\My Drive\desktop_folder_maybe\.ROOT`** — 16,091 files, 3.77 GB,
an **Aug 9 pre-restructure tree** — was supposed to be deleted *before* the new
Drive link was added (`UPDATE_PLAN.md` § Ruling 5). It was not, so Drive is
currently holding two `.ROOT` trees with different structures. Deleting it is
Chris's; AI cannot. This is independent of the gitdir move and does not block it.
