---
type: report
timeline: now
status: open-for-codex-review
tags: [tree, improvement, gate-0, codex-handoff]
created: 2026-08-08
authority: none — proposal for Chris's decision
---

# Improvement Brief — `.tree` V2

**For Codex review, and for Chris's decision.** Chris asked both surfaces to
attempt a 20–25% improvement on the live design, using `.ROOT`'s failures and
this project's own interaction record as the evidence base.

Part 1 states what is live and verified. Part 2 is the gap analysis, and it is
the part that matters. Part 3 is Claude's six proposals. Part 4 makes "20–25%"
measurable, because right now it is not. Part 5 is what Codex is asked to do.

---

## Part 1 — What is live, verified 2026-08-08

Codex completed B1–B6 of the work order. Claude built the first registered wiki.
Both were run, not reported.

```text
treeq check                    20 Markdown files, 16 stable IDs,
                               4 insertion templates. Exit 0.
treeq wiki PHYS2211            Full controlling packet. Exit 0.
treeq ask "…about torque"      Resolves to PHYS2211. Exit 0.
treeq ask "…business proposal" NO_WIKI_OWNER. Exit 3.
17 kernel tests                PASS.
```

The packet returns the academic-integrity boundary, proof rule, learner
frontier, proof gate, owns/does-not-own, evidence roots, and page inventory —
**none of which the invocation named.** That is the resolver thesis working: an
agent asking about torque is handed the integrity rule it did not know to ask
for.

Nothing migrated. Nothing committed. Nothing pushed. `.ROOT` untouched and
canonical.

---

## Part 2 — Gap analysis: `.ROOT`'s failures against `.tree`'s coverage

Ten failure classes, all observed in `.ROOT` with evidence from this session.

| # | `.ROOT` failure | Evidence | `.tree` status |
|---:|---|---|---|
| 1 | **Competing state owners** | `NOW.md` C1/P1 vs. Codex draft P1 vs. `EVENING_READING` P8/C8 — third occurrence of the class, no open flag | **Partial.** One `STATE.md`, but `PHYS2211-state.md` already reintroduces a mirror |
| 2 | **Duplicate basenames vault-wide** | `CLAUDE.md`, `AGENTS.md`, `README.md`, `HOW_TO_USE.md`, `OPERATIONS.md`, `index.md`, `log.md`, `current-position.md` × 8 wikis | **Fixed** — hard error in `check` |
| 3 | **Interface bloat** | Five governance files per wiki × 8 wikis = 40 files | **Fixed** — three namespaced files |
| 4 | **Stale citations propagate silently** | Removing one syllabus duplicate broke citations in 8 files; nothing detected it | **Fixed** — Markdown-link and wikilink validation |
| 5 | **Built content is never studied** | `learning-path.md`: *"All 18 stage packets are generated, but generated content is not studied content."* ~250 physics pages; frontier at Stage 4; Stages 1–2 "provisionally cleared, unconfirmed" | **Not addressed** |
| 6 | **Pre-building ahead of need** | Empty `.tree` scaffold; 18 stage packets built before Stage 5 | **Partial** — a rule exists, no enforcement |
| 7 | **Plans that never ran, still reading as live** | "Jul 31 Live Validation Runs (never ran)"; Seven-Day Plan superseded by a pause but still printed; the school pilot that never ran | **Not addressed** |
| 8 | **System work displacing real output** | Aug 7 plan named this explicitly; Aug 8 went entirely to architecture during a Week B that allocated 16 of 18 core blocks to physics and Python | **Not addressed** |
| 9 | **Source data-quality errors found late** | Syllabus recycled dates (3rd catch), wrong chapter numbers, `HAT_ECON` wrong grade structure, final exam printed twice with different dates | **Not addressed** |
| 10 | **No decision records** | ADR-001 is the first in the project's history; the July 24 no-move → Aug 8 move reversal has no recorded rationale to check against | **Fixed** — ADR pattern established |

### The finding

**`.tree` has fixed the mechanical failures and almost none of the behavioral
ones.** Four of ten fixed, two partial, four untouched — and the four untouched
(5, 7, 8, 9) are the ones that actually cost a semester. A vault with perfect
link integrity and an unstudied 250-page physics wiki has not improved Chris's
position.

Every fix so far is something a validator can check. Every remaining failure is
something a validator *could* check but nobody has asked it to. That is the 20%.

---

## Part 3 — Claude's proposals

Six, ordered by expected return. All are kernel changes, so they sit in Codex's
area under the collision rule. None is large.

### I1 — Make "built but never studied" countable

**The failure:** `.ROOT` holds roughly 250 physics pages against a Stage 4
frontier. Nobody knows what fraction has ever been worked, because nothing
records it. This is failure 5, and it is the largest single waste in the project.

**Proposal.** Content pages carry `last_used:` — the date the page was actually
*worked*, distinct from when it was edited. `treeq check` reports per wiki:

```text
PHYS2211: 41 content pages, 12 used (29%), 29 never used
```

A wiki above a declared over-build threshold is flagged. Law 10 stops being a
sentence and becomes a number.

**Cost:** one optional frontmatter field, one counter in `check`.
**Return:** the first honest measure of whether building is helping.

### I2 — Confidence travels with the claim

**The failure:** `.ROOT` catches source errors by hand, late, and inconsistently
— recycled syllabus dates caught on the third pass, a wrong grade structure that
survived weeks. It *already* invented the fix informally: *"every OpenStax
mapping past Chapter 1 is inferred, not verified"*, *"all paths verified present
on disk 2026-07-26."* It works. It is ad hoc.

**Proposal.** Any page carrying a date, deadline, grade weight, or external fact
requires `confidence: verified | inferred | unverified` and, when verified,
`verified_on:`. **`treeq wiki` surfaces every non-verified item in the packet.**

A session opening PHYS2211 would then be told, unprompted, that four of five exam
anchors are unverified — instead of finding out in November.

**Cost:** one required field on a narrow page class, one packet section.
**Return:** directly attacks failure 9, the class that has already fired three
times.

### I3 — Plans declare their own expiry

**The failure:** `.ROOT` is layered with superseded plans that still read as
current — the Seven-Day Plan, the July 31 validation runs, the pre-semester
coverage plan. A fresh session cannot tell which is live without reading the
history.

**Proposal.** `type: plan` requires `review_trigger:` and `expires:`.
`check` **errors** on any plan past its trigger that still carries
`timeline: now`. A plan cannot outlive its own gate silently.

`.ROOT` already uses `review_trigger` in some frontmatter. This formalizes a
pattern that is already proving itself.

**Cost:** two required fields on one page type, one date comparison.
**Return:** kills failure 7 outright.

### I4 — One state owner, enforced by the tool

**The failure:** failure 1, three occurrences, no open flag. **And Claude just
reopened it** — `PHYS2211-state.md` is a second copy of learner truth. The file
says `.ROOT` wins; that is intent, and intent is exactly what failed three times.

**Proposal.** One `state` page per `wiki_id`, enforced. A mirror must declare
`authority: mirror` and `mirrors: <path>`, must carry `timeline: reference`
rather than `now`, and `check` **errors** on a `timeline: now` state page that
declares a mirror target. Two writable owners becomes impossible rather than
discouraged.

**Cost:** two fields, one check.
**Return:** closes the failure class that has cost the most rework, and closes
the hole this session opened.

### I5 — The session-start command must cost less than the workaround

**The failure, unnamed so far:** `.ROOT` is not unused because it is wrong. It is
underused because using it correctly costs more than working around it — five
files and ~5,000 words of governance before any work begins.

`treeq wiki PHYS2211` currently emits ~60 lines of JSON. **JSON is a machine
format being read by a human in a terminal.**

**Proposal.** Human-readable default output, one screen, `--json` for machines.
If the packet costs more to read than the file it replaces, it will not be used,
and an unused router is worse than no router because it also has to be
maintained.

**Cost:** a formatter.
**Return:** this is the adoption question, and no other improvement matters if
the answer is wrong.

### I6 — A decision ledger, not a decision log

**The failure:** `Session_Logs` holds 179 files of real decision history in
unstructured prose. The cost shows up as re-litigation. **In this session alone**,
`water`/`leaves` was reopened twice, `craft` vs `life` twice, and `.tree` vs
`tree` three times — each already settled, each re-argued because settled
decisions live in narrative rather than in a register.

**Proposal.** `00-trunk/wiki/decisions.md` — one row per settled decision: date,
decision, who decided, evidence link, and status (`settled` / `reopened` /
`superseded`). Not a log; a ledger. The AI contract requires reading it before
proposing a change to anything it covers.

Part A of the current work order is a hand-built prototype of exactly this, and
it worked — Codex executed six items without reopening one of them.

**Cost:** one page and one line in the AI contract.
**Return:** the cheapest item here and possibly the highest return, because
re-litigation consumes whole sessions.

---

## Part 4 — Making "20–25%" measurable

The target is currently unfalsifiable. Three countable measures, baselines taken
2026-08-08:

| Measure | `.ROOT` baseline today | `.tree` now | V2 target |
|---|---|---|---|
| **Session-start context** — words that must be read before work begins | ~5,000 (AGENT + CHRIS_CORE + SYSTEM_FLAGS + OPERATIONS + current-position + index) | 4 root files + a 60-line JSON packet | **≤ 2,500 words, one screen** |
| **Live contradictions detectable by tooling** | 3 known, 0 open flags, 0 detectable | 0 detectable — no check exists | **All state and plan contradictions are `check` errors** |
| **Content utilization** — built pages ever worked | Unknown and unmeasurable | Unknown | **Known per wiki, reported by `check`** |

If all three land, the improvement is real and demonstrable. If they do not, the
percentage is a feeling.

**The one test that overrides all three:** on a real study night between August 9
and 22, does Chris open `.tree` first? If he opens `.ROOT` instead, nothing in
this brief has worked, regardless of what `check` reports.

---

## Part 5 — Asked of Codex

1. **Review Part 2.** Is the four-of-ten reading fair? Name any failure class
   that is miscategorized, and any `.ROOT` failure this table omits.
2. **Challenge or accept each of I1–I6.** State cost, risk, and what could
   regress. Reject any that fail Law 10 — complexity must earn its place, and six
   proposals is already close to the limit.
3. **Add Codex's own proposals.** Independent, from the same evidence base. Codex
   has read `.ROOT` structurally more than Claude has; the inspection findings
   from the August 8 PC audit are relevant here and were never folded into the
   design.
4. **Rank the combined set.** One recommended set for Chris, ordered, with a
   stated stopping point — what to build now versus what to defer past August 24.
5. **Answer the adoption question in I5 directly.** It is the one with no
   engineering answer, only a judgment.

### Constraints

- **Do not reopen Part A of the work order.** Those decisions are settled.
- **Nothing migrates from `.ROOT`.** Evidence stays read-only.
- **Collision rule holds.** Codex owns the kernel and `00-trunk/ai_os/`; Claude
  owns `00-trunk/branches/`.
- **August 24 is sixteen days out and the semester outranks the system.** Any
  proposal that cannot ship before August 22 should be marked *defer*, not
  *build*. Failure 8 is the one this brief is most at risk of repeating.

---

## Appendix — What Claude got wrong this session

Recorded because a brief about failure classes should hold itself to the same
standard.

1. **Called `00-turnk` a fabricated path** and grouped it with `root_seed` and
   `D:\BACKUPS\.ROOT` as a Codex pattern. It was a propagated typo of a real
   folder. Withdrawn.
2. **Called `02-LIBRARY\00-school\01-CSE-Python\` a Law 1 violation.**
   `syllabus-alignment.md` documents it as a deliberate personal workspace,
   byte-identical, not a citation target. A bounded duplicate with a stated
   owner, not an unmanaged second authority. Overstated.
3. **Created `PHYS2211-state.md` as a mirror of learner truth** while the same
   session's review identified competing state owners as `.ROOT`'s most expensive
   failure class. I1–I4 exist partly because of this; I4 specifically closes it.

---

*Prepared by Claude Code, 2026-08-08. No authority. Input to Chris's decision.
Nothing here authorizes a push, migration, deletion, or device connection.*
