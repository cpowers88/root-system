---
type: review
timeline: now
status: draft
register: ai-directive
tags: [governance, tree, architecture-review, gate-0]
created: 2026-08-08
reviewer: Claude Code
reviewing: PROPOSED_ROOT.md, PROPOSED_SYSTEM.md (Codex, 2026-08-08 11:54)
authority: none — review only; no file placed in .tree
---

# Independent Architecture Review — `PROPOSED_ROOT.md` and `PROPOSED_SYSTEM.md`

**Reviewer:** Claude Code, independent challenger role
**Sources reviewed:** `Documents\Codex\2026-08-08\can\outputs\PROPOSED_ROOT.md`; `PROPOSED_SYSTEM.md`; `Documents\Codex\2026-08-06\realtime-voice-chat\outputs\fall_2026_preparation_draft.md`
**Grounded against (live, read this session):** `01-NORTH_STAR\NORTH_STAR.md`; `00-BRAIN\AGENT.md`; `00-BRAIN\CHRIS_CORE.md`; `00-BRAIN\CLAUDE.md`; `01-NORTH_STAR\System Contracts\ROOT_CAPABILITY_CONTRACT.md`; `00-BRAIN\SYSTEM_FLAGS.md`; `NOW.md`; `EVENING_READING.md`; `03-WIKIS\REVENUE_LAB\README.md`
**Nothing was implemented. Nothing was placed in `.tree`.**

---

## Verdict

**support-with-changes.**

These are the two best-written governance documents in the project's history. The ownership split between them is correct and is the single structural thing `.ROOT` never had. The layer model, the two-axis truth/maturity schema, and the rebuild test are genuine advances.

The changes required are not stylistic. Three of them are load-bearing:

1. `SYSTEM.md` defines a **System Loop and a Return Packet that compete with `.ROOT`'s canonical ones**, violating its own Law 1 and an explicit `AGENT.md` prohibition, on day one.
2. `ROOT.md` **omits the near-term constraint that currently governs everything** — the funding cut that made income a condition of continuing past Fall 2026.  (from chris, Yes the funding cut cannot be carried around at all anymore, that is a good reason for recent activity.)
3. Between them the two files **drop six of the eight Execution Discipline rules** Chris approved July 26 after a full-system interview and independent Claude/Codex review, and drop the person profile entirely.

A system that shipped as written would be more elegant than `.ROOT` and less capable of running Chris's actual semester.

---

## Strongest five provisions

**1. `ROOT.md` §10 + `SYSTEM.md` §12 precedence order — the ownership boundary.**
`ROOT.md` owns purpose, destination, priority, authority, laws, change rule. `SYSTEM.md` owns behavior. Model files load; they do not duplicate or override. Then §12 gives a six-level tie-break with Chris's current explicit instruction at the top. `.ROOT` has never had a written precedence order, and nearly every governance conflict logged in `SYSTEM_FLAGS.md` traces to its absence. Keep this exactly as written.

**2. `SYSTEM.md` §6 — truth support and maturity as independent axes.**
> "A verified fact may never have been applied. A mature working hypothesis may remain uncertain. One dimension must not impersonate the other."

This is the correct encoding of the July design finding and it is stated more clearly here than in the master design report. It is also the fix for the most common `.ROOT` failure: a topic marked "done" because it was read.

**3. `SYSTEM.md` §3 — canonical/generated exclusivity.**
> "No artifact may be canonical and generated at the same time. No generated view may silently accept human edits that cannot be rebuilt from canonical inputs."

This is the rule that prevents the exact defect that fired again this morning (see Material Problem M2 below for the live evidence). Keep verbatim.

**4. `SYSTEM.md` §14 — the generated-view rebuild test.**
> "Deleting all generated views and rebuilding them from canonical state must reproduce the same result within declared nondeterministic fields."

This is the only rule in either document that a script can execute. Everything else is prose an AI grades itself against. More rules should look like this one.

**5. `SYSTEM.md` §18 closing line — "No stage advances because a date arrived or a folder exists."**
Written by an author who had just looked at `.tree`: nine empty folders, one commit containing only a `.gitignore`, created Aug 7. The lesson is correctly drawn and correctly placed.

*Runner-up worth naming:* `ROOT.md` Law 11 — "Real outcomes outrank system maintenance. The system may not consume the time and attention it exists to return." That law, enforced, would have prevented several `.ROOT` weekends.

---

## Material problems

### M1 — `SYSTEM.md` creates two competing System Loops and two competing Return Packets

**This is the most serious finding.**

`SYSTEM.md` §4:
```text
ORIENT -> PREPARE -> LEARN / RESEARCH -> DECIDE -> BUILD / APPLY -> PROVE
EVOLVE <- REVIEW <- RECORD <- MEASURED OUTCOME <- DEPLOY / USE / TRANSFER
```

Live canonical loop, `ROOT_CAPABILITY_CONTRACT.md` (installed July 15, 2026):
```text
SENSE -> RESEARCH -> TEACH -> STRUCTURE -> DECIDE -> BUILD -> PROVE
EVOLVE <- REVIEW <- LEARN <- MEASURED OUTCOME <- DEPLOY / USE
```

`SYSTEM.md` §16 defines a **six-field** Return Packet. `ROOT_CAPABILITY_CONTRACT.md` §Return Packet defines the **five-field** packet and states it is "the single packet standard in `.ROOT`; every other packet ... is an instance of it." `AGENT.md` line 231 states: *"no file may define a competing loop or packet."*

So on the day `SYSTEM.md` is placed anywhere an AI reads it, it simultaneously violates:
- its own `ROOT.md` Law 1 (one authority per fact),
- its own `ROOT.md` Law 4 (no competing authorities),
- a live explicit `.ROOT` prohibition.

Two further substantive objections to the new loop itself:

- It **deletes TEACH as a named stage** — in a document whose §2 makes Teacher one of four co-equal identities. Teaching becomes a thing that happens somewhere inside "LEARN / RESEARCH," which is where it will get skipped.
- It **deletes SENSE** — which is the Watchtower's only stage. External signal sensing now has no place in the loop, while §8 still expects research to begin from a decision question. The Watchtower is left with neither eyes nor a stage.

The six-field packet is also not an improvement over five: fields 5 ("System learning") and 6 ("Next action") were already carried in `.ROOT` by field 5 plus the handoff ritual, and splitting them invites the packet to become a status report.

**Required:** pick one loop and one packet, and state explicitly when the successor takes effect.

### M2 — `ROOT.md` has no near-term survival constraint, and the destination alone is misleading

`ROOT.md` §2 states the destination: October 8, 2031, ≥$500K/yr, KSU BS ISYE. §4 places revenue evidence third in priority, below the technology/business capability floor.

Live and verified this session, `03-WIKIS\REVENUE_LAB\README.md`:
> "Created July 14, 2026, after the school funding cut made additional income a condition of continuing past Fall 2026."

A fresh AI reading only `ROOT.md` would correctly conclude that revenue is a 2031 problem ranked third. It would be wrong in a way that could cost the degree the constitution declares fixed.

The specific date is operational and belongs in `SYSTEM.md` or a strategy file. What is missing from `ROOT.md` is the **permanent class**: a near-term constraint that threatens the education, the family, or the system's own continuation outranks the long-range plan, because the destination is unreachable through a broken present. `.ROOT`'s `NORTH_STAR.md` has the same gap; this is an inherited omission, not an introduced one, but the successor is the place to fix it.

### M3 — Privacy Law 5 is *weaker* than what `.ROOT` enforces today, and has no structural protection

`ROOT.md` Law 5:
> "Human-designated private material is inaccessible to AI unless Chris explicitly changes that classification for a named item and purpose."

`AGENT.md` rule 8, live:
> "`88-JOURNAL\` is private and never read or written by AI."

No exception clause. The proposal introduces an unlock path that does not currently exist — and introduces it *in the constitution*, the hardest place to take it back out. That may be what Chris wants; it should be a deliberate decision, not a side effect of rewriting.

Second and separate: **Law 5 protects against intent. Nothing protects against a glob.** If private space sits inside a compilable subtree, an instruction to "rebuild every view under `X/`" crosses the boundary with no AI ever forming the intent to read private material. The `.tree` scaffold already demonstrates the risk shape: its `.gitignore` ignores `88-JOURNAL/`, the old name, while the folder present is `journal/`. The structural rule must be in the constitution, not left to a compiler author.

### M4 — "Evidence is immutable to AI" is vaguer than the raw-folder rule it replaces, and contradicts Chris's own July answer

`ROOT.md` Law 6: "Original evidence is immutable to AI."
`SYSTEM.md` §3, Evidence row: "Human intake; AI immutable/read-only."

Live `NORTH_STAR.md` §3:
> "AI may not create, edit, move, rename, archive, or delete any file under a `raw\` folder unless Chris explicitly authorizes the named exception."

Six verbs, a named scope, and a named authorizer. "Immutable" does not obviously forbid *creating* alongside or *moving* out. This is not hypothetical: open flag **#69** is precisely the case where the question was whether AI may move a byte-identical duplicate out of `raw\`, and Chris's recorded answer to the July design questions was *"YES with exceptions to things inside raw folders, those can be copied and moved when needed."*

So the constitution as written is both looser than the current rule (no verb list) and stricter than Chris's actual decision (no exception path). Both directions are wrong.

### M5 — The layer table has no home for flags or plans, the two things `.ROOT` actually runs on

`SYSTEM.md` §3 enumerates eleven layers. Neither of these exists:

**Flags.** A known open defect that is *not* the current objective, carrying severity, owner, and a dated check trigger. Live example: flag #57, MEDIUM, escalates Aug 17 if PHYS 2211 §54 syllabus has not posted. This is not active state (it is not the current objective), not knowledge (it is not an interpreted claim), not an event (it has not happened yet), and not a view (it is not rebuildable). Under the proposed model it has no owner, so it will be invented ad hoc — which is exactly how `.ROOT` grew the sprawl this successor exists to avoid.

Relatedly, `AGENT.md` Execution Discipline rule 7 — *"Every stop rule names an owner and a check moment. A dated trigger nobody is assigned to evaluate does not exist"* — has no carrier anywhere in `SYSTEM.md`.

**Plans and commitments.** `SYSTEM.md` §5 classifies "weekly plans" as **views**, disposable and compiler-owned. A plan is not a view. A view is derived from current state; a plan is a *commitment made at a point in time*, and its value comes precisely from not being silently regenerated. Classifying it as disposable means a regenerated plan that differs from what Chris agreed to produces no detectable defect.

The `fall_2026_preparation_draft.md` Chris pointed me to is the perfect specimen: `status: proposed`, no canonical status, an explicit "does not alter `.ROOT` operating files" boundary — and yet it is the most detailed statement in existence of what Chris should be doing for the next sixteen days, including a capacity model that quietly settles the unreconciled full-load/reduced-load disagreement. Under the proposed layer model that document is homeless. Under `.ROOT` it is also homeless. That is the gap the successor was supposed to close.

**Live evidence that this is not theoretical, as of today:**

| Source | What it says about Saturday, Aug 8 |
|---|---|
| `NOW.md` (canonical cockpit, dated Aug 6) | queue at **C1 / P1**, explicitly "not date-advanced" |
| `fall_2026_preparation_draft.md` (Codex, Aug 6) | bridge sequence **starts Saturday, August 8 at P1** |
| `EVENING_READING.md` (generated Aug 7) | Saturday's queued items are **P8 / C8** |

Two independent sources agree on P1. The generated view alone says P8, consistent with the date-advance defect. The layer model got this right in principle — the disposable artifact is the wrong one — but **nothing detected it**, and that is what needs a rule (see M9).

### M6 — Six of eight Execution Discipline rules do not survive, and the person profile disappears entirely

`AGENT.md`'s Execution Discipline block is annotated *"Approved by Chris 2026-07-26 after a full-system interview and independent Claude/Codex review."* It is the most expensively earned governance in the vault. `SYSTEM.md` carries rule 6 (§11, one reconciled answer) and part of rule 8 (§7 gate). The rest is gone:

| Rule | Status in proposal |
|---|---|
| 1. Work first — no optional system work before the day's primary proof | **absent** |
| 2. Weekly plan, daily proof | **absent** |
| 3. One visible lane; brief is not a second cockpit | **absent** |
| 4. Prepare the operational, recommend the directional; never a blank menu | **absent** |
| 5. Proof moves the stage immediately; do not wait for a scheduled day | partial — §5 forbids date-advance, but not the reverse |
| 6. One reconciled answer | present (§11) |
| 7. Every stop rule names an owner and a check moment | **absent** |
| 8. Mastery gates need independent evidence | present (§7) |

Rule 1 is Law 11's enforcement mechanism — without it, Law 11 is a sentiment. Rule 4 is the direct counter to a documented `CHRIS_CORE.md` "Do Not": *"Give a wide menu when one recommendation is possible."* Rule 5's forward direction is what makes the Fall 2026 draft's fast-pass rule legal — *"Passing quickly earns faster progression. A time block is a cap, not a sentence."* Without rule 5, an AI reading only `SYSTEM.md` has no basis to let Chris move early.

**Separately and more seriously: `CHRIS_CORE.md` has no successor.** Neither file carries how Chris works — cue-dependent associative memory for arbitrary terms, spatial and quantitative strengths, "treat time as Chris-owned capacity," "do not turn the calendar into a supervisor," "do not assume empty time is available capacity." §7.1 says "begin at Chris's actual frontier" and that is the entire representation of the person in a system whose whole purpose is one person. There is no layer row for a person profile and no loading rule that would pull one in.

### M7 — Academic integrity is a sub-bullet where it is a hard stop

`SYSTEM.md` §7.5: "preserve course-specific academic-integrity boundaries."
`SYSTEM.md` §19: "cross an academic-integrity boundary."

`AGENT.md`, live:
> "CSE 1321 and ENGR 1000 prohibit AI on submitted coursework unless the course explicitly permits it. AI may teach concepts, vocabulary, study methods, and fresh examples. When a task appears graded, stop and ask whether AI help is permitted for that specific task."

"Preserve boundaries" is satisfiable by an AI that does not know what the boundaries are. The permanent class — *some work is Chris's alone by external rule, and the default on ambiguity is stop and ask* — belongs in `ROOT.md` as a law. The course list is operational and belongs in `SYSTEM.md`, refreshed each semester.

This is the one omission with a consequence that cannot be rolled back from a checkpoint.

### M8 — Wording that will cause overreach, hesitation, or competing truth

**Overreach:**

- §11 "Any authorized AI surface may perform any in-scope task **it can safely complete**." Correct and matching `.ROOT`, but self-assessed with no counterweight. `AGENT.md` pairs the same permission with a hard stop for "operations the current tools cannot safely perform" *and* rule 5: "complete everything still possible and state the exact missing capability." Add the counterweight or the permission is unbounded.
- §12 row "Change active state — **Controlled transition with visible proof**." This is the most consequential row in the matrix and the vaguest phrase in the document. "Controlled" is undefined. Define it mechanically.
- §12 row "Promote a material claim to verified fact — **Evidence rule; Chris for consequential cases**." "The evidence rule" is not stated anywhere as a rule; §6 describes states, not a promotion threshold. As written an AI promotes claims on its own judgment.

**Hesitation:**

- §19's stop list ends with "require a choice that materially changes purpose, authority, or system scope" — combined with `ROOT.md` §5's "When authority is unclear, the system preserves the current state and asks Chris," an AI facing ordinary ambiguity has two independent instructions to stop. `.ROOT` deliberately counterweights this: *"Do not manufacture disagreement, repeated confirmation gates, or model-boundary refusals"* and *"Clear requests get completed. Relevant risks get stated once."* §19's closing sentence gestures at it but is far weaker than the rule it replaces. Chris has corrected AI hesitation more than once; this needs the explicit prohibition.

**Competing truth:**

- §5 classifying weekly plans as views — see M5.
- §1's eight required answers and §17's thirteen acceptance criteria overlap heavily but are not identical, and §17 is written as a checklist a session could claim to satisfy. Two lists of "what good looks like" is the seed of a third.

### M9 — No rule for what happens when two views disagree

Given that the NOW/EVENING_READING contradiction has now fired three times, this is the most conspicuous missing rule in the entire proposal. The layer model implies the answer (canonical wins, view is rebuilt) but nothing states it, nothing detects it, and nothing records it. `ROOT.md` §8's anti-goal — "several dashboards or agents independently describing what is current" — has no matching acceptance test in §17.

### M10 — Recovery requirements are correct in spirit and untestable in practice

§13: "Maintain dated recovery checkpoints and test restoration before risky changes."
§17: "structural changes reversible from a verified checkpoint."

Every word of that is satisfied, as prose, by the current `.ROOT` backup arrangement — which this session verified to be: a configured destination (`D:\BACKUPS\.ROOT`) **that does not exist**, a script that **excludes `.git`** and therefore discards 158 commits of rollback history, and a copy mode (`robocopy /MIR`) that **deletes in the destination**. A checkpoint requirement that the current broken state passes is not a requirement.

Also absent from both files: **off-machine copy**. `ROOT.md` Law 9 says local-first, portable, recoverable; §13 says version control "where appropriate." As of this morning, six commits containing the entire ROOT V2 design basis existed on exactly one disk. Law 9 as written was fully satisfied.

### M11 — Multi-device gets the order backwards, and has no offline mode

§13: "Connect additional devices sequentially; test conflict surfacing, credential recovery, rollback, and privacy **before granting writes**."

Better than anything in `.ROOT`. Two gaps:

- **Credential recovery is a precondition for the device, not a post-connection test.** The HP Victus campus laptop needs a wipe and reinstall and its admin password may be unrecoverable (`HANDOFF_0807_CLAUDE.md`; first attempt Aug 10, hard checkpoint Aug 19). Under the wording as written, an AI would sequence "connect, then test credential recovery" — on a machine that cannot pass that test.
- **No offline mode.** Chris will be on campus with a laptop and no sync. Neither file says what is authoritative during divergence or how it resolves on reconnection. Undefined means the first implementation silently picks one, and Law 1 is broken by accident.

### M12 — Business value never connects to demonstrated capability

`ROOT.md` §1's permanent value path runs `capability -> useful work -> economic value`. `SYSTEM.md` §10's business chain starts at `person or organization -> costly problem`. The two chains never meet: nothing requires a business capability to trace back to a demonstrated entry in the learner state.

The single most useful question this system could answer, given the funding cut, is **"what can Chris sell today, with evidence behind it?"** Neither file requires the system to be able to answer it.

Secondary: §10's "protect client-specific and private information outside the reusable knowledge system" is softer than `AGENT.md` rule 11, which says active client work lives *in a separate workspace or repository outside `.ROOT`*. "Outside the knowledge system" could be read as a folder.

### M13 — The teaching contract has no failure cost control

§7's gate defines what proof is required. Nothing defines what happens when the gate keeps failing — so an AI will loop until Chris stops it. The Fall 2026 draft has the missing pieces and they are good: a 90-minute repair cap, "repair only the failed connection," "recheck two days later," and "repeated cold-check miss → build a narrow repair sequence, not a broad restart." `.ROOT`'s Move-On Gate has the two-block cap. None of it reaches `SYSTEM.md`.

Related: §7.6 says record errors "without turning every attempt into permanent documentation" — right instinct, but it leaves learner-state updates with no defined carrier. §5 lists "links to ... capability state" and §3 has no capability/learner-state row.

### M14 — Duplicated authority between the two files

Three real duplications, in descending severity:

1. **`ROOT.md` §7 evolution ratchet vs `SYSTEM.md` §15 evolution protocol.** Two diagrams of the same process with different stages (§15 adds "smallest proposal," "fixture/regression test," "versioned change"; §7 has "impact review," "bounded implementation"). A future AI must choose. `ROOT.md` should state only the *rule* — nothing changes without evidence, a gate, and a reversal path — and `SYSTEM.md` should own the only diagram.
2. **`ROOT.md` §5 authority list vs `SYSTEM.md` §12 matrix.** Same rule, two enumerations that differ: §5 omits schema; §12 omits relationships and commitments. Make §12 the only enumeration.
3. **`ROOT.md` §8 anti-goals vs `SYSTEM.md` §17 acceptance suite.** Same content in negative and positive form. Tolerable, but every anti-goal should have exactly one matching test, and one currently does not (see M9).

### M15 — No authority model for unattended operation

Both documents assume Chris is in the session. The evening-reading generator is already a scheduled unattended task, and it is already the source of the contradiction in M5. §12's matrix does not distinguish an AI acting in a live session from an AI acting on a timer with no human to challenge it. That is a live authority gap, not a future one.

---

## Exact edits, by section

Disagreements are preserved as written, not smoothed. Where I recommend against a Codex choice, both versions are shown.

### `ROOT.md` §2 — Destination

**Add, after the Life outcome bullet:**

> - **Continuation constraint:** the destination is unreachable through a broken present. A near-term constraint that threatens the education, the family, or the system's own continuation outranks the long-range plan until it is resolved. The current such constraint and its evidence live in `SYSTEM.md` and the owning strategy file, not here.

*Rationale: M2. The class is permanent; the December 2026 instance is not.*

### `ROOT.md` §3 — Permanent capability base

**Replace the eight bullets with:**

> `tree` must compound Chris's ability to diagnose systems of people, process, data, and technology; to learn unfamiliar technical material and transfer it into real use; to build and validate dependable technical work; and to convert proven capability into measured value. The current enumerated capability set lives in `SYSTEM.md`.

*Rationale: eight bullets that include "research, writing, teaching, and communication" approximate "everything," which makes the section non-binding. The enumeration is also the thing most likely to change. Codex's list is good content in the wrong file.*

### `ROOT.md` §4 — Priority

**Keep the four-item order.** Note for `SYSTEM.md`: `.ROOT` carries a numeric floor — "protect a 5–10 hour weekly technology/business floor whenever deadlines allow." Correctly dropped from the constitution as operational, but it currently exists in **neither** file. It must land in `SYSTEM.md`.

### `ROOT.md` Law 5 — Privacy

**Codex:**
> Private means private. Human-designated private material is inaccessible to AI unless Chris explicitly changes that classification for a named item and purpose.

**Proposed replacement:**
> **5. Private means private.** Human-designated private space is never read, written, indexed, summarized, or compiled by AI. Its declassification is not an AI-initiated action and does not occur inside the session that wants the access. Private space is a top-level sibling of the compiled tree, never nested inside it, so that no instruction to rebuild a subtree can reach it.

*Disagreement preserved: Codex's version permits a named-item exception; `.ROOT`'s current rule permits none. I recommend keeping the absolute form and adding the structural clause. If Chris wants the exception, it should be added deliberately with its own approval record — not inherited from a redraft.*

### `ROOT.md` Law 6 — Evidence

**Proposed replacement:**
> **6. Evidence remains preserved.** AI may not create, edit, move, rename, archive, or delete any file in an evidence store except under an exception Chris names by item and purpose. Interpretation may evolve without rewriting the source.

*Rationale: M4. Restores the six verbs from `NORTH_STAR.md` §3 and restores the exception path Chris actually granted in July. Flag #69 is the live test case.*

### `ROOT.md` — new Law 13

> **13. Some work is Chris's alone.** Where an external rule — academic integrity, licensure, client contract, or law — reserves work to Chris, AI may teach the underlying concept but may not produce the deliverable. On ambiguity the default is stop and ask, not proceed.

*Rationale: M7. Currently a §7 sub-bullet. It is the one rule whose breach cannot be rolled back.*

### `ROOT.md` §5 — Authority

**Delete the five-bullet "Chris owns" enumeration; replace with:**

> Chris owns purpose, direction, timing, relationships, commitments, final judgment of quality and value, and every consequential action. The complete authority matrix lives in `SYSTEM.md` §12 and is the only enumeration.

*Rationale: M14.2.*

### `ROOT.md` §7 — Human-governed evolution

**Delete the ASCII ratchet diagram.** Replace with:

> The system changes only through: evidence of friction or opportunity, a bounded proposal, an authority gate, validation, and a stated reversal path. `SYSTEM.md` §15 owns the single canonical form of this process. No model may silently change this constitution, loosen privacy or security, alter canonical ownership, or redefine success.

*Rationale: M14.1.*

### `SYSTEM.md` §4 — The System Loop

**This section must be resolved before either file is approved.** Three options, in my order of preference:

**Option A (recommended).** Adopt `.ROOT`'s canonical loop verbatim — `SENSE → RESEARCH → TEACH → STRUCTURE → DECIDE → BUILD → PROVE → DEPLOY/USE → MEASURED OUTCOME → LEARN → REVIEW → EVOLVE` — and add one line: *"This is the same loop `ROOT_CAPABILITY_CONTRACT.md` defines. It is restated here, not redefined; if they diverge, the predecessor governs until `tree` is canonical."*

**Option B.** Keep Codex's loop and add an explicit supersession clause naming the date and the capability: *"This loop supersedes `ROOT_CAPABILITY_CONTRACT.md`'s only for capabilities whose canonical ownership has transferred to `tree` under §18.7. Until then the predecessor's loop governs."*

**Option C (reject).** Ship as written. Two loops, no precedence, Law 1 violated at birth.

**Regardless of option, two substantive changes to Codex's loop if it survives:** restore **TEACH** as a named stage (§2 makes Teacher a co-equal identity; a stage it does not appear in is a stage it gets skipped in), and restore **SENSE** (the Watchtower currently has no stage in this loop).

### `SYSTEM.md` §16 — Return Packet

**Replace the six fields with `.ROOT`'s five**, or add the same supersession clause as §4. `AGENT.md` line 231: "no file may define a competing loop or packet." Field 6 ("Next action") belongs in the handoff ritual, which is where `.ROOT` already carries it and where it does not encourage the packet to become a status report.

### `SYSTEM.md` §3 — Canonical layers

**Add three rows:**

| Layer | Responsibility | Canonical? | Default write authority |
|---|---|---:|---|
| Person profile | How Chris works, learns, decides, and is best supported | Yes | AI proposes from evidence; Chris approves |
| Open issues (flags) | Known defects and risks that are not the current objective, each with severity, owner, and dated check trigger | Yes | AI opens and updates; closure requires evidence |
| Commitments and plans | What was agreed, when, for what period — weekly plan, semester plan, stop rules | Yes | Chris approves; AI drafts; **never regenerated** |

**Add after "No artifact may be canonical and generated at the same time":**

> A commitment is not a view. A plan records what was agreed at a point in time and is never silently regenerated; a compiler may display it but may not rewrite it.

*Rationale: M5, M6.*

### `SYSTEM.md` §5 — One active state

**Delete "weekly plans" from the list of views.** Current text:

> "Morning briefs, weekly plans, dashboards, model memories, and device interfaces are views."

**Replacement:**

> "Morning briefs, dashboards, model memories, and device interfaces are views. Plans and commitments are canonical and live in their own layer; a view may display a plan but may not restate or regenerate it."

**Add:**

> **When a view contradicts canonical state, the view is defective.** The contradiction is recorded as an open issue, the canonical state is not altered to match, and the generator is corrected before the view is regenerated. A view that has contradicted canonical state twice is disabled until its generator is fixed.

*Rationale: M5, M9. Three occurrences to date; today's is live.*

### `SYSTEM.md` §7 — Teaching contract

**Add as rules 8–10:**

> 8. Cap repair. A failed gate earns a bounded repair of the specific failed connection, not a broad restart, and not more than two blocks or ninety minutes without Chris's explicit decision to continue.
> 9. A pass moves the next topic forward immediately. Do not hold a passed gate for a scheduled day; do not advance a topic because a date arrived. A time block is a cap, not a sentence.
> 10. Record the miss where it survives the session. Learner state is canonical and is updated by demonstrated evidence only; a session transcript is not learner state.

**Add to the loading rule (§14):** the person profile loads with `SYSTEM.md`, always.

*Rationale: M6, M13. Rules 8 and 9 are drawn from the Fall 2026 draft's fast-pass rule and `.ROOT`'s Move-On Gate.*

### `SYSTEM.md` §11 — AI team contract

**Add to the responsibilities list:**

> - complete everything still possible when a tool or access limit blocks a step, then state the exact missing capability or handoff artifact;
> - do not manufacture disagreement, repeated confirmation gates, or model-boundary refusals. State a material risk once with a recommendation, then continue unless a hard stop in §19 applies.

*Rationale: M8, hesitation. This is the counterweight `.ROOT` carries and this draft dropped.*

### `SYSTEM.md` §12 — Authority matrix

**Replace two rows:**

| Action | Default authority |
|---|---|
| Change active state | Only when the named proof gate for that item is written to the event log. The surface that records the proof may record the transition. Date passage, plan text, AI narration, and a checked box are never transitions. |
| Promote a material claim to verified fact | Requires an independent check — a second surface, a deterministic validator, or Chris. Self-corroboration by the surface that produced the claim does not promote it. |

**Add one row:**

| Act unattended (scheduled task, no human in session) | Read and generate views only. No canonical write, no state transition, no external action. Anything else waits for a live session. |

*Rationale: M8, M15.*

### `SYSTEM.md` §13 — Privacy, security, and recovery

**Replace "Maintain dated recovery checkpoints and test restoration before risky changes" with:**

> - A recovery checkpoint counts only when all three hold: it was restored to a scratch location and the restored copy opened successfully; it includes version-control history, not only working files; and it was produced by a copy mode that cannot delete in the destination. A backup command exiting zero is not a checkpoint.
> - Canonical truth exists in at least two physical locations, one of them off this machine, before any structural change begins.

**Replace the device bullet with:**

> - Before a device is connected, its administrative access must be independently recoverable. Then connect one device at a time and test conflict surfacing, rollback, and privacy before granting writes.
> - Declare an offline mode: which side is authoritative while a device is disconnected, and how divergence resolves on reconnection. Undefined is not a mode.

*Rationale: M10, M11.*

### `SYSTEM.md` §10 — Business-partner contract

**Add:**

> - Maintain a current answer to "what can Chris deliver today, with evidence behind it," derived from demonstrated learner and capability state rather than from intent.
> - Active client-specific work lives in a separate workspace or repository outside this system. Only sanitized methods, templates, lessons, metrics, and approved case evidence return.

*Rationale: M12. The second bullet restores `AGENT.md` rule 11 at its original strength.*

### `SYSTEM.md` §17 — Acceptance suite

**Add:**

> - no two artifacts making contradictory claims about the same current fact, tested against the fixed contradiction set;
> - a checkpoint restored, opened, and verified within the current review period;
> - a work-first check: the day's primary proof recorded before any optional system work in the same session.

*Rationale: M9, M10, M6 rule 1.*

### `SYSTEM.md` §18 — Build and migration gates

**Move this section out of `SYSTEM.md` entirely**, into a dated migration plan.

*Rationale: §18 is a one-time project plan sitting inside a permanent operating contract. It will be obsolete within six months and will then be nine stale paragraphs that every session loads forever. `.ROOT` accumulated exactly this way. The closing line — "No stage advances because a date arrived or a folder exists" — is a permanent rule and should be promoted into §15 before the rest moves out.*

### `SYSTEM.md` §19 — Stop and escalate

**Replace the closing sentence:**

> Otherwise, complete clear in-scope work through validation and report the result. Ambiguity that is not on this list is resolved by stating the assumption and proceeding, not by stopping. Do not add confirmation gates this list does not require.

*Rationale: M8, hesitation.*

---

## Recommended final length and loading behavior

Current: `ROOT.md` ≈ 1,500 words; `SYSTEM.md` ≈ 2,900 words. Both always loaded, plus a surface profile — roughly 5,000 words of mandatory context before any work begins. `.ROOT` already has evidence that always-loaded governance crowds out the work it governs (Law 11's whole reason for existing).

**Target:**

| File | Target | Loading |
|---|---|---|
| `ROOT.md` | ~1,100–1,300 words | Always. Never abridged. |
| `SYSTEM.md` | ~1,300–1,500 words | Always. |
| Person profile | ~600 words | Always — this is not optional context in a one-person system. |
| Surface loader (`CLAUDE.md` / `AGENT.md`) | ≤ 300 words | Always. Local differences only. |
| Playbooks | any length | On trigger only. |

**Total mandatory: ~3,300 words**, down from ~5,000 while *adding* the person profile.

**Move to on-demand playbooks** (question 5), each named in one routing table in `SYSTEM.md`, matching the "Active question → Additional file" pattern `AGENT.md` already uses successfully:

| Playbook | From | Trigger |
|---|---|---|
| Research | §8 | a research or intake session |
| Engineering | §9 | a build or system change |
| Business | §10 | client, offer, revenue, or delivery work |
| Teaching | §7's thirteen-step chain and seven sub-rules — **keep the three-line demonstrated-understanding gate in `SYSTEM.md`** | any teaching session |
| Change proposals | §15's eight-item proposal checklist — **keep the ratchet in `SYSTEM.md`** | proposing a system change |
| Acceptance suite | §17 | review, or next to the fixtures that execute it |
| Migration plan | §18 | the migration, then archived |

Two loading rules worth stating explicitly in `SYSTEM.md`:

1. A playbook may add local detail. It may not restate or override `ROOT.md` or `SYSTEM.md` — same rule already applied to model loaders in §14.
2. If a session cannot determine what to load, it loads the four always-files and asks. It does not load everything.

---

## Unresolved questions requiring Chris

These cannot be settled by review. Each changes the text.

**Q1 — Privacy: absolute or unlockable?** `.ROOT` today: journal is never read, no exception. Codex's Law 5: unlockable for a named item and purpose. Which is the constitution? *(I recommend absolute, and that any change get its own approval record rather than arriving inside a redraft.)*

**Q2 — Which loop and which packet, and effective when?** `.ROOT`'s canonical loop and five-field packet, or Codex's new ones — and does the successor take effect on approval, or per-capability as ownership transfers under §18.7? Nothing else in either file can be finalized until this is answered. *(I recommend `.ROOT`'s, restated not redefined, with per-capability supersession.)*

**Q3 — Does the continuation constraint belong in the constitution?** M2 proposes adding the *class* of near-term survival constraint to §2 without naming December 2026. Alternative: leave `ROOT.md` purely long-range and carry the constraint in `SYSTEM.md`. *(I recommend the constitution, because a fresh AI reading only `ROOT.md` currently gets the priority wrong.)*

**Q4 — Where do plans and flags live, and are they canonical?** M5 proposes two new layers. This is the largest structural change I am recommending and it affects the folder map, so it should be answered before any structure is created.

**Q5 — Does `CHRIS_CORE.md` get a successor, and is it always loaded?** Currently it has neither. If yes, it needs a layer row, a loading rule, and an owner for updating it from evidence.

**Q6 — Academic integrity as Law 13, or a `SYSTEM.md` rule?** M7 argues constitution. It is the only breach with no rollback.

**Q7 — What is authoritative when the laptop is offline?** Not answerable by review; it depends on how Chris will actually work on campus. It must be answered before a second device is connected, which is currently gated behind the wipe and the Aug 19 checkpoint anyway.

---

## What I did not change and deliberately left alone

- `ROOT.md` §2's "$1M planning band" is strategy content in a constitution. `NORTH_STAR.md` has the identical flaw, so this is inherited, not introduced. Not worth reopening now; noted for the next ratchet.
- Codex's §12 precedence order, §14 naming rule, §14 rebuild test, §6 relationship vocabulary, §18's closing line, and §11's "model names describe strengths, not ownership" are all correct and should be preserved verbatim.
- I have not proposed a folder structure. That is Gate 0 work and is unreconciled.

---

## Bearing of `fall_2026_preparation_draft.md` on this review

Chris asked me to read it alongside. Four things it contributes:

1. **It is the specimen for M5.** `status: proposed`, explicitly non-authoritative, no canonical home — and simultaneously the most detailed operational statement in existence of the next sixteen days. Both `.ROOT` and the proposal leave it homeless.
2. **It supplies the missing teaching rules.** The fast-pass rule and the 90-minute repair cap are exactly what §7 lacks; I lifted them into the proposed rules 8–9 rather than inventing new ones.
3. **It quietly settles the capacity disagreement** — 29.5 hr firm floor, 21–25 committed, remainder deliberately uncommitted, with "do not budget sleep, Benjamin time, or recovery as study capacity." That is a good answer to a question that has been open since the full-load/reduced-load split, and neither proposed file has anywhere to keep it.
4. **It corroborates P1, not P8.** Its bridge sequence starts at P1 on Saturday, August 8, matching `NOW.md`. `EVENING_READING.md` alone says P8. Two independent sources against one generated view.

---

**Status:** Review only. No file created in `.tree`. No structural, governance, backup, or Git action taken. Nothing in this document has authority; it is input to the three-way reconciliation.
