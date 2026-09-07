---
type: report
timeline: now
status: live
tags: [governance, security, wsl, hooks, flag-96, flag-93, file-safety]
created: 2026-08-11
---

# Bulk-Work Gate — August 11, 2026 (late session)
### Claude Code · WSL-launched · answers Chris's "put up that firewall, flag 94 or 92"

## Direct conclusion

**The firewall is up in WSL, not on Windows, and it is not the thing flag 92 or 94
described.**

`AGENT.md` File Safety 12 already required bulk work to run through
`safe_shell.sh`. Nothing checked it. That requirement is now enforced by a
`PreToolUse` hook that denies bulk or scripted `Bash` not launched through the
wrapper. Measured **ENFORCED** from WSL; **NOT YET MEASURED** on Windows and
recorded that way rather than assumed.

**Flag #96 stays OPEN.** The gate raises the cost of reaching the exposure. It
does not close it, and `safe_shell.sh` remains the only control in this stack
that actually enforces.

---

## The flag numbers were wrong, and the correction mattered

| Flag | What it actually is | Status |
|---|---|---|
| 92 | Windows sandbox does not constrain a spawned shell | CLOSED this morning |
| 95 | Config declaring controls that silently do not apply | CLOSED this morning |
| 94 | Teaching-hat methods load conditionally | OPEN — unrelated |
| **96** | **Residual: spawned child can write `88-JOURNAL` and every `raw\`** | **OPEN** |

The firewall lineage is **92 → 95 → 96**. This was worth stating before building
anything, because flag #96 records the inert `sandbox` block as *not fixable
here* — it is Claude Code platform behavior, not a `.ROOT` misconfiguration.
There was no un-built config change waiting behind the request. Writing
plausible-looking rules into the `sandbox` block would have re-created flag #95
by hand: a control that reads as protection in an audit and enforces nothing.

What was actually missing was **enforcement of item 12**, not another rule. Same
defect class as open flag #93 — a governance rule that exists only as prose.

Chris chose the hook over patching the deny list's relative-path hole. That was
the right call: the permission layer matches command *strings*, so it can never
see a path resolved at runtime, and patching it would have produced a second
control that looks like protection without being it.

---

## What was built

| File | Role |
|---|---|
| `.claude\hooks\require_safe_shell.py` | The gate — classifies commands, emits the deny decision |
| `.claude\hooks\require_safe_shell.sh` | Launcher — resolves the interpreter, fails closed |
| `.claude\hooks\test_require_safe_shell.py` | Evaluation evidence — 59 + 11 cases |
| `.claude\settings.json` | `hooks.PreToolUse` entry matching `Bash` |
| `00-BRAIN\scripts\verify_controls.py` | New `check_bulk_gate()` — measures the hook |

It is a **redirect, not a refusal**. The deny message contains the exact wrapped
command to run instead:

```
BLOCKED by require_safe_shell — AGENT.md File Safety 12.

This segment runs the script `fetch_fred.py`, and a script can touch
any number of files in one pass:
    python3 00-BRAIN/scripts/fetch_fred.py

Run it through the wrapper instead:
    00-BRAIN/scripts/safe_shell.sh python3 00-BRAIN/scripts/fetch_fred.py
```

Both known incidents are shapes it blocks: the 2026-08-10 glob that rewrote 2,713
files, and this morning's unintended `fetch_fred.py` execution.

---

## Three design decisions that must not be quietly undone

**1. No command-string override.** Any escape hatch spelled in the command — an
env prefix, a magic comment — is one an AI can type for itself. A wall with an
AI-accessible door is not a wall. The only ways past are the wrapper, or Chris
editing `ALLOWED_SCRIPTS` / the hook entry. Both are human acts.

**2. Fail-closed on every error path.** Missing gate file, no Python interpreter,
empty or unparseable stdin, non-string command, internal crash — all exit 2.
This is deliberately against the usual hook convention. Claude Code treats any
exit code other than 0 or 2 as a *non-blocking error*, so a hook that merely
breaks lets the tool call through. A gate that fails open is flag #95 with extra
steps. A visibly broken gate is recoverable; a silently absent one is not.

**3. Quoted text is data; quoted text fed to `-c` is code.** `git commit -m
"while testing, do not skip"` must pass and `bash -c 'for f in *; do rm $f;
done'` must not, though both contain the same loop-shaped words. This is not
polish — a gate that blocks ordinary commit messages is one its user switches off
within a day, and a switched-off gate protects nothing.

---

## Two portability traps, found by measuring rather than assuming

**Interpreter names.** WSL has `python3` and no `python`; Windows has `python`
(`C:\Python314`) and no `python3`. A hook is one command string read from two
environments — either spelling hardcoded is dead in one of them, and a dead hook
fails open. Hence the launcher, which resolves `python3`/`python`/`py` at run
time and denies if none exists.

**`jq` is absent in both environments,** so the documented jq-based hook pattern
was unusable. The gate parses its own JSON.

---

## The evaluation earned its place

`for f in *.md; do rm $f; done` **passed the gate** on the first run.
`split_segments` splits on `;`, which is *inside* the loop construct, leaving
three harmless-looking fragments. Loop detection moved to a whole-command pass.

The fix then appeared to fail — because the test walked its own copy of the
decision path rather than calling it. A test that reimplements the logic it
checks passes while the real path is broken. `evaluate()` is now the single path
both the hook and the test call.

A separate 20-command false-positive sweep produced two blocks on ordinary work
(a commit message, and the gate's own test suite) and drove design decision 3
above.

---

## Measured state

| Check | Result |
|---|---|
| `verify_controls.py` — PreToolUse bulk-work gate | **ENFORCED** (bulk rc=2, ordinary rc=0) |
| `verify_controls.py` — `safe_shell.sh` | ENFORCED (selftest 3/3) |
| `verify_controls.py` — `sandbox` block | **INERT** (unchanged, both dimensions) |
| Evaluation suite | 59 classification + 11 end-to-end, all pass |
| `validate_boot_chain.py` | PASS |
| `root_health.py` | PASS WITH DEBT, exit 0 |

8 controls checked, the same 2 INERT as before this session.

---

## What this gate does NOT do

State this plainly wherever it is cited. Overstating a control is the failure
this vault keeps hitting.

- It reads `Bash` **tool calls**. It does not constrain a process once started.
- It does not inspect what an allowlisted script does once allowed.
- It is **pattern-based**. A sufficiently novel shape will not be recognised.
- `ALLOWED_SCRIPTS` is a **trust assertion, not a measurement** — adding a name
  asserts someone read that script and confirmed it does not write `88-JOURNAL`
  or any `raw\`.
- It does **not** retire copy-first. It routes work behind the wall; it does not
  inspect what the work does once inside.

---

## Handoff

**Current state.** The gate is live and measured in WSL. Documentation is
updated in five places: `AGENT.md` item 12, `SYSTEM_FLAGS.md` flag #96
mitigation (3), `.claude\CONTROL_INVENTORY.md` (new section plus a status row and
a step 3 in the change protocol), today's DAILY, and this report. All gates pass.
**Nothing is committed** — the working tree carries 6 modified files plus the
untracked `.claude\hooks\` directory.

**Open question / blocker.** Windows is unmeasured. `bash` on the Windows PATH
resolves to the WSL launcher (`...\WindowsApps\bash.exe`), not Git Bash
(`C:\Program Files\Git\bin\bash.exe`), so the invocation path there is genuinely
untested. If the hook cannot launch on Windows it fails open silently, which
means the Windows side would have no bulk-work gate while the config reads as
though it does.

**Next exact action.** From a **Windows** Claude Code session, run
`python 00-BRAIN\scripts\verify_controls.py` and read the `PreToolUse bulk-work
gate` row. If ENFORCED, update the Windows column in
`.claude\CONTROL_INVENTORY.md` from NOT YET MEASURED. If INERT, record that the
Windows side has no gate and treat it as the open item — do not leave it silent.

**Details likely to be forgotten.**

- The `sandbox` block in `settings.json` is still INERT and must never be cited
  as a live control. Do not delete it either — it is kept deliberately so
  protection activates if platform support lands.
- A Windows `NOT MEASURABLE` is not evidence of safety.
- `root_health.py` emitted a **false BLOCKER** (`wiki links and navigation -
  blockers ?; review ?; expected ?`) when two heavy scans ran concurrently on the
  9p mount. The `?` marks are unparsed JSON from a starved `wiki_lint.py`, not a
  finding. Clean isolated run: PASS WITH DEBT, exit 0. Logged as friction in
  DAILY, **not flagged** — one occurrence is not evidence yet. Worth watching: a
  gate that can cry blocker under load teaches people to discount blockers.
- Still awaiting Chris's disposition from earlier today, untouched by this
  session: the three ECON dataset rows from the unintended `fetch_fred.py` run,
  and `REVENUE_LAB\README.md`'s unreconciled July funding-cut survival claim.
- Re-run `python3 .claude/hooks/test_require_safe_shell.py` after any change to
  the gate. A regression returns the hook to supervised use.

---

*Claude Code (WSL) · August 11, 2026 · implements the mechanism behind
`AGENT.md` File Safety 12; mitigates but does not close flag #96*
