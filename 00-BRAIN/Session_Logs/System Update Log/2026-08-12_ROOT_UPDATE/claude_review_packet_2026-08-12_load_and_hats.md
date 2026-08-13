---
type: report
timeline: now
register: system-review
status: proposed
tags: [update, phase-d, load, hats, instruction-layer, review]
created: 2026-08-12
session_date: 2026-08-12
---

# Review packet — the load `.md` files and the hats

**For Chris. Nothing has been moved.** This is the proposal-first table Phase D requires
before anything changes, and it is the review Chris asked for on 2026-08-12 evening.

**How to read this:** every section of every always-loaded file is listed with its measured
word count and one recommendation. Read the ⛔ and 🟡 rows carefully — those are the ones
that can go wrong. Skim the ✅ rows; they are "keep, no change."

| Verdict | Meaning |
|---|---|
| ✅ **KEEP** | Needed in every session. Does not move. |
| 🔵 **MOVE** | Situational — only fires in a specific circumstance. Moves to a named file, loads when that circumstance arises. |
| 🟡 **SPLIT** | The rule stays; its forensic history or implementation detail moves. |
| ⛔ **DO NOT TOUCH** | Cutting this repeats a known failure. Flagged explicitly. |

**The governing rule, from the Aug 10 handoff, which is what made flag #94:**

> **Situational procedures may move. Methods used every time may not.**

**Word-count targets are not the objective.** Seat 2's "cut to ~1,000 words" was the wrong
shape. Every row below is judged on *"does an agent need this in EVERY session?"* — the
savings are the consequence, not the goal.

---

## Part 1 — The always-load

**Total measured 2026-08-12 evening: 6,859 words** across six files. This is everything an
agent reads before it can do anything at all.

| File | Words | Share | Proposed |
|---|---|---|---|
| `00-BRAIN\AGENT.md` | 2,642 | 39% | → ~1,900 |
| `00-BRAIN\SYSTEM_FLAGS.md` | 2,197 | 32% | → ~700 |
| `00-BRAIN\CHRIS_CORE.md` | 892 | 13% | → ~790 |
| `01-NORTH_STAR\NORTH_STAR.md` | 569 | 8% | → 569 (law, untouched) |
| `00-BRAIN\CLAUDE.md` (profile) | 458 | 7% | → ~400 |
| root `CLAUDE.md` (pointer) | 101 | 1% | → 101 |
| **Total** | **6,859** | | **~4,460 (−35%)** |

---

### 1.1 `AGENT.md` — 2,642 words, 39% of every session

Measured section by section:

| Section | Words | Verdict | Reasoning |
|---|---|---|---|
| System in One Sentence | 37 | ✅ KEEP | The frame. Cheapest orienting words in the file |
| Direction and Priority Policy | 232 | 🟡 SPLIT (−110) | **The 4-item priority order stays.** The companion-file table ("business question → CURRENT_STRATEGY.md") is a routing lookup — an agent consults it *when* it has that question, not at boot |
| **Execution Discipline** | **517** | ⛔ **DO NOT TOUCH THIS PASS** | Biggest section, and the highest-risk cut in the file. These 8 rules govern how work is selected every single day. Rules 3, 7, 8 carry parenthetical implementation notes that *look* trimmable — but this is precisely the shape of the July 11 cut that produced flag #94. **Recommend deferring to a separate, dedicated pass with its own review.** Deferred, not declined |
| One AI Team | 138 | 🔵 MOVE (−90) | The surface-strengths table is *descriptive* ("Claude Chat: strategy, synthesis"). Every surface already carries this in its own profile — `00-BRAIN\CLAUDE.md` says it in more detail. The operative sentence, "any AI may complete any in-scope task," stays |
| Task Completion / Constructive Challenge | 129 | ✅ KEEP | Behavior on every request. **This is also where the safe word clause lands** (Phase I) |
| Work Modes | 58 | ✅ KEEP | Cheap, and shapes every response |
| Profile and Local-File Precedence | 74 | ✅ KEEP | This *is* the load path |
| Session Start Protocol | 100 | ✅ KEEP + **FIX** | This is the load path. **It also contains the L134/L153 contradiction** — see §1.6 |
| **File Safety — Non-Negotiable** | **460** | 🟡 **SPLIT (−200)** | **All 12 rules stay, in full, word for word.** What moves is the ~200 words of *forensic history* appended to rule 12 — "Enforced since 2026-08-11," which probe was wrong, the six negative dimensions, the 2,713-file incident narrative. **`.claude\CONTROL_INVENTORY.md` already exists for exactly this** and is already the file the system says to read before citing a control as live. **This is the single cleanest large win in the file: prohibition stays, archaeology moves** |
| Wikis and CASTLE | 93 | ✅ KEEP | Short, orients the whole folder structure |
| Wiki Shared Layer | 73 | 🟡 SPLIT (−30) | **The heading stays — 26 files reference it by name.** The explanation of what the 8 rules are can shrink to the pointer |
| Extension and Shared-Skill Rules | 124 | 🔵 MOVE (−124) | Fires only when someone is *building* an extension. Pure situational procedure. **Note: this section contains the `00-BRAIN\SKILLS\` casing mismatch (real folder is `skills`) — fix it in the same pass** |
| System Evolution Authority | 117 | 🟡 SPLIT (−40) | **The two-path rule stays** (Chris-directed vs AI-initiated) — it governs every proposal an agent makes. The Return Packet / System Loop pointer can compress |
| Agent Evaluation Gate | 80 | 🔵 MOVE (−80) | Fires only when building or deploying an agent. Situational by definition |
| Academic Integrity | 43 | ⛔ KEEP | Hard boundary, 43 words. Never move a boundary to save 43 words |
| Report Chain and Handoff Ritual | 172 | 🟡 SPLIT (−90) | **The four handoff fields and the DAILY rule stay.** The Aug 2 "entry discipline" paragraph is session-close procedure — `session-close` skill already owns that moment |
| Review Cadence | 39 | ✅ KEEP | Cheap |
| Communication Development | 26 | ✅ KEEP | Situational, but 26 words — not worth the churn |
| Final Rule | 30 | ✅ KEEP | |

**AGENT.md: 2,642 → ~1,900 (−742), with Execution Discipline deliberately untouched.**

Every removed word is either a routing table, a forensic record, or a procedure that fires
in one specific circumstance. **No rule, prohibition, or method is cut.**

---

### 1.2 `SYSTEM_FLAGS.md` — 2,197 words, 32%, the only unbounded term

Already worked out in `PHASE_D_FLAG_LOAD_PROPOSAL.md`. Summarized here for one-place review:

- **1,668 of 2,197 words are the seven open-flag table rows.** Flag #96 alone is 590.
- **Only three of seven flags forbid an action.** The other four are work items no session
  can act on at boot anyway.
- **Keeps:** the PAUSE banner, § The Rule, the *Last updated* line, **the three prohibitions
  in full imperative form**, and a one-line index of every other open flag.
- **Moves** to a new, non-loaded `SYSTEM_FLAGS_DETAIL.md`: the forensic entries — measurement
  history, which probe was wrong, provenance disputes.

**The three prohibitions that must survive the trim verbatim:**

| # | Constraint |
|---|---|
| **97** | **DO NOT DEDUPE `raw\` ON HASH.** Five sources survive only as filenames. AI may not write under `raw\` at all |
| **96** | **The bulk-work gate covers `Bash`, NOT `PowerShell`.** Windows bulk work is governed by discipline alone. Never describe the gate as covering "bulk work" |
| **94** | **Methods moved behind a conditional load stop being applied.** Situational procedures may move; methods used every time may not |

⛔ **The one way this goes badly wrong:** if #97's line degrades into a pointer instead of
carrying "DO NOT DEDUPE ON HASH" itself, a future cleanup pass destroys the only surviving
record of five lost sources. **The summary line carries the imperative, never a pointer to it.**

**Growth evidence, measured today:** 1,933 → 2,091 → **2,197 words in a single day** (+13.7%),
entirely from that day's own flag work. **This file is why the boot load grows while nobody
decides that it should.**

---

### 1.3 `CHRIS_CORE.md` — 892 words, 13%

**Recommendation: keep almost all of it.** This is the file that makes teaching work for the
way Chris actually learns. Cutting it to save words risks flag #94's failure mode aimed at
the person contract instead of the teaching methods.

| Section | Words (approx) | Verdict |
|---|---|---|
| Chris in One Sentence | 55 | ✅ KEEP |
| Stable Context | 130 | ✅ KEEP |
| **Runtime Contract (8 rules)** | **390** | ⛔ **DO NOT TOUCH.** These are methods used every session — item 3 ("make arbitrary knowledge retrievable") is the direct mechanism for the knowledge→skill conversion Chris is trying to speed up |
| Aptitude Interaction Map | 110 | 🔵 **MOVE (−110)** — the only real candidate. It is *descriptive background*, and `CHRIS.md` already owns the full 12-dimension evidence. The Runtime Contract already encodes the operative behavior |
| Do / Do Not | 160 | 🟡 Candidate, **not recommended.** It overlaps the Runtime Contract, but it is the compressed, scannable form an agent actually applies mid-response. Overlap here is redundancy that works |
| Read Live Owners | 90 | ✅ KEEP — this is routing that fires every session |

**CHRIS_CORE.md: 892 → ~790 (−110).** Small, and that is the correct answer for this file.

---

### 1.4 `NORTH_STAR.md` — 569 words, 8%

⛔ **Untouched. It is law, it is already minimal, and §3 forbids AI writing to it without
Chris's explicit approval.** It states function, destination, authority, priority order, and
the change rule, and explicitly delegates everything else via its ownership map. **There is
no fat here — the separation was already taken.**

---

### 1.5 `00-BRAIN\CLAUDE.md` (profile) — 458 words, and root `CLAUDE.md` — 101 words

- **Profile: −~60.** If `AGENT.md`'s "One AI Team" table moves here (§1.1), the two
  overlapping surface descriptions merge instead of both loading. Also carries the same
  `00-BRAIN\SKILLS\` casing mismatch — fix in the same pass.
- **Root pointer: keep at 101.** It does one job correctly.

---

### 1.6 The contradiction to fix in the same pass

`AGENT.md` disagrees with itself about when `SYSTEM_FLAGS.md` loads:

| Where | What it says |
|---|---|
| **L134** — Session Start Protocol step 3 | "Check `SYSTEM_FLAGS.md` for the active task" → **always** |
| **L153** — File Safety 7 | "required context for **system, file-write, and review** sessions" → **situational** |
| **The file's own header** | "Check at every session start" → **always** |

Two say always, one says situational. **An ambiguity in a load rule is exactly how a file
ends up loaded by default forever without anyone deciding it should be.** Whatever Chris
rules, the three lines must be made to agree.

---

## Part 2 — The hats (12 files, 7,486 words)

**None of these are always-loaded**, so nothing here costs boot words. The problem with the
hats is the opposite of the flags problem: **not that they load too much, but that they load
too little, at the wrong time.**

| Hat | Words | Notes |
|---|---|---|
| `HAT_OPERATOR.md` | 288 | Slimmed July 11 |
| `HAT_ENGR1000.md` | 321 | Subject hat |
| **`HAT_EDUCATOR.md`** | **480** | **⛔ The flag #94 file — see below** |
| `HAT_PHYSICS.md` | 510 | Subject hat |
| `HAT_TCOM.md` | 512 | Subject hat — **and TCOM has no wiki hub** (Phase H) |
| `HAT_ECON.md` | 594 | Subject hat |
| `HAT_EDUCATOR_PLAYBOOKS.md` | 608 | Split out July 11. **"Load when running a teaching session"** — a judgment call |
| `HAT_PYTHON.md` | 643 | Subject hat |
| `HAT_TECHNOLOGY_ENGINEER.md` | 775 | Core mode |
| `HAT_SOFTWARE_ENGINEER.md` | 866 | Core mode |
| `HAT_OPERATOR_PLAYBOOKS.md` | 908 | Split out July 11. Explicit per-procedure triggers — **this one is done right** |
| `HAT_ENGINEERING_PLAYBOOKS.md` | 981 | "Load only the procedure whose trigger fires" — **also done right** |

### 2.1 The one real defect — flag #94

`HAT_EDUCATOR.md` names **seven teaching methods**: Skeleton First, One Concept at a Time,
Term Anchoring, Explain-It-Back, Cold Checks, Physical Anchors, Short Corrections.

**Their substance is not in the hat.** It sits in `HAT_EDUCATOR_PLAYBOOKS.md` behind
*"Load when running a teaching session"* — a judgment call, not a trigger. And **none of the
five subject hats** (`HAT_PHYSICS`, `HAT_PYTHON`, `HAT_TCOM`, `HAT_ECON`, `HAT_ENGR1000`)
reference the playbooks. So after the educator hat loads, nothing downstream mentions the
methods again.

**Result: when the playbook loads, teaching follows the method. When it doesn't, the agent
has seven bare names and improvises.** The same hat behaving as two different teachers —
which is exactly what Chris reported when he said the hats are "iffy sometimes."

**Cause: the July 11 slim pass, which moved substance behind a conditional load to save ~300 words.**

**Recommended fix (Thursday, ~45 min):** inline the seven method definitions back into
`HAT_EDUCATOR.md` (~300 words). Hats are already an optional load, **so the boot chain is
untouched and this costs zero always-load words.** Keep the four SKILL procedures in the
playbook — those are genuinely situational.

**Why this is the highest-value item in the whole packet for Chris's stated goal:** the seven
methods *are* the knowledge→skill conversion step. Everything else in this update makes the
system faster; this one makes the learning actually stick.

### 2.2 The structural lesson

Compare the three playbook files:

- `HAT_ENGINEERING_PLAYBOOKS.md` — *"Load only the procedure whose trigger fires"* ✅
- `HAT_OPERATOR_PLAYBOOKS.md` — per-procedure triggers, named explicitly ✅
- `HAT_EDUCATOR_PLAYBOOKS.md` — *"Load when running a teaching session"* ❌

**The first two name a firing condition. The third names a vibe.** That is the whole
difference between a split that works and the one that produced flag #94 — and it is the
test every 🔵 MOVE row in Part 1 must pass before it moves.

---

## Part 3 — What Chris decides

| # | Decision | Recommendation |
|---|---|---|
| 1 | Approve the `AGENT.md` moves in §1.1 (−742, Execution Discipline untouched)? | **Yes.** Every removed word is a routing table, a forensic record, or a single-circumstance procedure |
| 2 | Approve the `SYSTEM_FLAGS.md` split (−1,390)? | **Yes** — already proposed and detailed; biggest single win |
| 3 | `CHRIS_CORE.md` — move the Aptitude Interaction Map (−110)? | **Marginal. Chris's call.** Recommend keeping if there is any doubt — 110 words is not worth risking the person contract |
| 4 | Defer Execution Discipline to its own pass? | **Yes.** It is the highest-risk 517 words in the system |
| 5 | Inline the seven teaching methods into `HAT_EDUCATOR.md` (flag #94)? | **Yes** — zero boot cost, direct effect on learning quality |
| 6 | Which word is the safe word? | Chris picks; wording drafted in `UPDATE_PLAN.md` Phase I |

**If 1, 2 and 5 are approved: always-load goes 6,859 → ~4,460 words, a 35% cut, with every
prohibition, method, and rule still loading — and teaching stops being a coin flip.**

---

## Verification if approved

1. `validate_boot_chain.py` — must stay PASS (all six files are in `BOOT_FILES`).
2. `root_health.py` — must stay exit 0.
3. Re-measure always-load; record the new figure in `UPDATE_PLAN.md`.
4. **Behavioural check, not structural:** a fresh session states all three prohibitions
   without opening `SYSTEM_FLAGS_DETAIL.md`, and names the seven teaching methods under the
   educator hat without being asked for the playbook.
5. Named check date per `AGENT.md` § System Evolution Authority.

*`AGENT.md` File Safety 10: editing an instruction file does not change the session already
running. Every check above requires a **fresh** session — that is the Friday morning test.*
