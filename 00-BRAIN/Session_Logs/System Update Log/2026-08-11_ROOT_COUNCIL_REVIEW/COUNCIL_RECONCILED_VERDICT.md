---
type: report
timeline: now
register: system-review
status: proposed
tags: [council, governance, instruction-layer, learning, infrastructure, ai-ml]
created: 2026-08-11
---

# Council Review — Reconciled Verdict

### Four independent seats, cold-briefed, read-only. Integrated into one answer per `AGENT.md` § One AI Team rule 6.

**Commissioned by Chris, 2026-08-11:** review all `.ROOT` wiki material for second-brain
and AI-automation technique; give the instruction `.md` files a hard critical evaluation
against both present need and future aspiration; recommend improvements beyond the `.md`
files; optimise for faster, easier learning of technological skills that compound into
value alongside the ISYE degree.

**New controlling fact, surfaced the same day:** Percipio's role advisor names Chris's
current role **Systems Engineer** and his aspirational role **AI/ML Developer** (data
science, algorithms, model building, large datasets, model accuracy and deployment).
The named skill lists failed to capture — see § Data Loss below.

| Seat | Charge |
|---|---|
| 1 | Harvest — what the wikis know vs. what the system does |
| 2 | Hard critic of the instruction layer |
| 3 | Learning velocity |
| 4 | Infrastructure beyond the `.md` files |

No seat could see another's work. Where they agree, they agree independently.

---

## The verdict in one paragraph

`.ROOT`'s governance and instrumentation are genuinely strong — stronger, in places, than
the practice in the books it has read. That is not the problem. The problem is that the
governance layer is the **only** place knowledge converts. The system has seven validators
measuring whether it is internally consistent and **not one** measuring whether the day
produced anything; it has read 3,789 pages of AI/ML material and contains zero lines of ML
code; it names an aspirational role that appears nowhere in the files that tell agents what
to do; and it repeatedly detects its own defects and then fails to propagate the correction
into the prose anyone reads. The fix is not another architecture. It is three small
instruments and one artifact.

---

## Where all four seats converge

These are the findings that arrived independently from different briefs. They carry the
most weight in this document.

### C1 — Detection works. Propagation fails. (Seats 2, 3, 4)

The vault finds its own defects reliably and then leaves the correction unmade in the
documents people read.

- The D: backup was recorded as never having run in **both** `DAILY_2026-08-08` and
  `DAILY_2026-08-09`. Three live documents still describe it as a live daily mirror
  (`START_HERE.md:152`, `vault_map.md:29`, `LOCAL_MACHINE_MAP.md:34-37`).
- Five live files claimed the wiki rules were "defined once in `AGENT.md § Wiki Shared
  Layer`" hours after they moved. The session enforcing the rule committed the violation.
- `sync_shared_skills.py --check` returns **PASS** over a skill whose `SKILL.md` links
  twice to a `SKILL-MECHANICS.md` that is absent from both mirrors.
- `WHERE_IT_GOES.md` described hub `CLAUDE.md` loaders that were removed 2026-08-10.

This is one failure class, not four incidents: **a validator that confirms presence is
repeatedly mistaken for one that confirms function.** `.claude\CONTROL_INVENTORY.md`
(written today) is the antidote and should be the template.

### C2 — The rule exists; the instrument does not. (Seats 1, 2, 3)

`AGENT.md` rule 1 says no optional system work begins before the day's primary proof.
Seat 2 counted the six days to Aug 11: **20+ sessions, one touched learning.** Every one of
those sessions read rule 1 before starting.

Seat 3 reached the identical conclusion from the learning side: the teaching loop is
measurably fast (worked-step to independent transfer in ~6 minutes on the accumulator rep,
by file timestamp; Stage 4 opened cold and closed in three days). **The loop is not the
bottleneck. The study window gets consumed by the control plane.**

Seat 1 named the mechanism from the agent-engineering literature the vault already holds:
*maintain state with code, not narration* — and observed that `NOW.md` and
`MORNING_BRIEF.md` have been stale for five days, which is precisely the failure that
chapter predicts.

Three seats, three routes, one conclusion: **the system does not lack the rule. It lacks
the instrument.**

### C3 — The aspiration has no presence and no path. (Seats 1, 2, 3)

Seat 2's scan across every governing file:

```
machine learning | AI/ML | data scien* | model training | neural | scikit | pytorch  →  0 matches
```

Worse, `capability_development_goal.md:32` caps the AI capability at *"Select and connect AI
or automation only when the workflow and risk justify it"* — a **procurement** skill. An
AI/ML Developer builds models; the system's stated ceiling is knowing when to buy one.
`03-WIKIS\TECHNOLOGY\OPERATIONS.md:102-105` explicitly deprioritises `data-science-ml\`,
the one folder matching the target.

Seat 1 verified the consequence: **23 `data-science-ml\` pages, 30 named ML design patterns,
1,108 pages of AI Engineering — and no `.ipynb` anywhere in the vault, no pandas/numpy/
sklearn import outside a vendored `.venv`.** `skill-map.md` lists "Probability and
statistics: not-started", "LLM extraction, structured outputs, and evaluations:
not-started", "Provider APIs: not-started".

### C4 — Reading converts to governance, never to code. (Seat 1 headline; corroborated by 2, 3)

Seat 1's sharpest finding is that the gap is **asymmetric, not uniform**:

> Knowledge that converts into a governance rule gets applied within days. Knowledge that
> would require writing code, running a measurement, or standing up a tool stays on the
> page indefinitely.

10 of 11 system-evolution proposals are `APPROVED & APPLIED`, most within 0–1 days. The one
proposal requiring something to be *built* — the session-close hook — has been open 30 days
and approved for 4. `.claude\hooks\` does not exist. Hooks are the one extension type in
`AGENT.md`'s own trigger table the vault has never built.

Seat 3 found the learning-side version: **content readiness has not been the constraint for
months.** PYTHON holds 269 wiki files against a learner at Stage 4b of 11; PHYSICS holds 335
against Stage 4 of 18. On Aug 8 the just-in-time gate was retired and 12 calculus-link pages
were pre-built for stages Chris reaches between September and December — converting learner
blocks into generation blocks in the exact window where completion was already 41%.

---

## Where the seats are in tension — and how it resolves

### T1 — Is AI/ML the target, or a distraction from December?

**Seat 2** says name AI/ML Developer as the role of record in `NORTH_STAR.md` now, because
an agent can execute this instruction set perfectly and still work on the wrong thing.
**Seat 3** says AI/ML Developer is ~36 months out, lands *with* the degree, and is **not**
the answer to income by December 2026 — the nearer capability is data cleaning and
defensible analysis (pandas + SQL + a one-page finding), 3–6 months out, already specified
as CASTLE Phase 3's exit criterion.

**Resolution: both, and they are not actually in conflict.** Write AI/ML Developer into
`NORTH_STAR.md` as the **destination with named prerequisites**, precisely so it stops
competing silently for present attention. The near-term artifact is data analysis. Seat 1's
top-ranked item — cross-validation and leakage discipline on data already on disk — is the
bridge: it is simultaneously the first real ML rep and the first defensible-analysis rep.
One artifact serves both horizons.

### T2 — Three seats recommend structural change. Seat 1 warns structural change is the disease.

Seat 2 proposes cutting `AGENT.md` from 2,548 → ~1,000 words and the profiles from 859 →
~120. Seat 3 proposes collapsing CASTLE's phase/skill layer. Both are well-argued.

But seat 1's headline is that **this vault reliably does architecture instead of output**,
and seat 3 documented an architecture (`.tree`) proposed Aug 8 and retired Aug 10.
A large restructure undertaken now would *be* the failure mode all four seats diagnosed.

**Resolution: sequence by artifact, not by size.** The instruction-layer cut is real work
and should happen — but it is worth less than one working artifact, and it must not go
first. Anything that produces an executable output precedes anything that produces a
cleaner document.

---

## Data loss — act on this before any cleanup

Seat 4 hashed all 2,277 non-journal `.md` files. **This is not a duplication bug. Sources
are gone.**

```
x4 identical bytes in 03-WIKIS\SYSTEMS\raw\ — 4 filenames, 1 article
x3 identical bytes in 03-WIKIS\SYSTEMS\raw\ — 3 filenames, 1 article
```

The **filename** is from the intended page; the **frontmatter and body** are from a
different one. Seven files hold two articles. **Five sources were never captured at all** —
"Eight Principles of Good Data Management", "Data Management for Researchers", "13 Project
management", "Why Trust Science", and the O'Dea talk exist as filenames and nothing else.

> **Do not dedupe on hash.** The filenames are the only surviving record of what is missing.
> A cleanup pass would delete the evidence and make the loss permanent and invisible.
> Reconcile filename against frontmatter `title`/`source` first and build a recovery list.

**Root cause:** the clipper pre-fills the note name from whichever tab was active when the
popup opened, then re-extracts content at save time. Clipping several tabs quickly produces
a name and a body from different pages.

**A second, distinct defect** produced today's Percipio failure: the skills list is injected
by JavaScript after page load, and the clipper serialised the DOM before it resolved. The
same page failed the same way previously — a truncated copy has been sitting in
`02-LIBRARY\ref-meta-how-to-work\` since before today. The clipper also wrote
`created: 2226-28-12` (year 2226, month 28) and mapped page *duration* into `published`.
Since the list is behind KSU auth, no clipper will retrieve it; manual copy is the path.

---

## Backup posture — verified, and largely fictional

| Claimed | Verified reality |
|---|---|
| `D:\BACKUPS\.ROOT`, daily scheduled mirror | Does not exist. No scheduled task. Never ran. D: has 1,688 GB free |
| `G:\My Drive\.ROOT` | Wrong path. Real copy is `G:\My Drive\New folder\.ROOT` — a one-time manual upload dated Aug 9, already stale |
| *(undocumented)* | A third copy at `D:\ARCHIVE\.ROOT` — 3,964 `.md` files, dated Jul 19, containing a nested `.ROOT\.ROOT`. Unowned |

**GitHub is the only working off-machine backup, and `.gitignore` excludes `88-JOURNAL`,
every `raw/`, `77-INBOX`, `99-ARCHIVE`, and all PDFs.** So 1.71 GB of source material, the
journal, and the inbox rest on one hand-made copy in a folder named "New folder".

Also: ~150 MB of the stripped Oracle JDK remains pinned in `.git` by four Codex checkpoint
refs — unreachable from any branch, so pushes succeed, but `git gc` can never reclaim it.

---

## Recommended sequence

Ordered so that every step produces something executable or prevents irreversible loss.
Steps 1–2 are reversible-loss prevention and come first regardless of anything else.

| # | Action | Cost | Why here |
|---|---|---|---|
| **1** | **Reconcile the `raw\` clipper queues** — filename vs. frontmatter across all 9 queues, produce the recovery list. Do **not** delete anything. | ~1 session | The only item on this list that gets *worse* with time. A well-meant cleanup destroys the evidence. |
| **2** | **Make one backup real** — fix `backup_to_d_drive.ps1`'s `.git` exclusion and `/MIR` deletion risk, run once manually, verify, then schedule. Correct the three documents that describe it as live **in the same session.** | ~2 hrs | 1.71 GB of irreplaceable source currently has one stale manual copy. Doing the doc edit in the same session is the discipline C1 says is missing. |
| **3** | **The proof instrument** — a script computing days-since-last-learner-proof, days-since-income-evidence, days-to-Aug-24, days-to-December, emitted into `NOW.md`; plus a session-close check that fails when a day has system work and no learner artifact and no recorded reason. | ~4–6 hrs | The single change three seats converged on. Would have flagged Aug 8, 10, and 11 while they were happening. |
| **4** | **One ML rep on real data** — k-fold cross-validation with mean *and* standard deviation, the leakage question asked variable-by-variable, a heuristic benchmark first. Against `scanner.db` or the ECON FRED datasets already on disk. | ~3–4 hrs | Highest value ÷ effort in the vault. First line of ML code; simultaneously the first defensible-analysis rep. Resolves T1. |
| **5** | **Goal rewording** — put the December 2026 income condition and the AI/ML destination into `NORTH_STAR.md`; swap priority 2 and 3 so income evidence outranks the discretionary study floor. | ~1 hr | Cheap, and until it lands an agent can execute this system perfectly and still work on the wrong thing. |
| **6** | **The session-close hook (flag #93)** — build warn-only this week, promote to blocking after a week of observed behaviour. | ~2–3 hrs | Approved 4 days ago, open 30. Gives the vault its first working hook. Do not wait for further design. |
| **7** | **Fix `sync_shared_skills.py`** to mirror whole directories and fail when `SKILL.md` references an absent file. | ~2 hrs | Verified live bug; a validator returning PASS over a broken reference. |
| **8** | **Instruction-layer cut** — `AGENT.md` and the two profiles, per seat 2's tagged keep/move/cut table. | ~1 session | Real and worth doing. Deliberately last: it produces a cleaner document, not an artifact. |

**Cheap items worth folding into whichever session touches them:** `git gc` after clearing
the four Codex refs (~150 MB); run `build_graph_colors.py` for real (the graph currently
renders `88-JOURNAL`, `99-ARCHIVE`, `77-INBOX` and `Session_Logs` as nodes, making the one
retrieval surface decorative); gitignore `.vs\` (39.7 MB); give `fetch_fred.py` argument
parsing so it cannot fire a live API call when probed.

---

## What to stop reading (seat 1, corroborated by seat 3)

- **AI governance / safety philosophy** — 24 pages already compiled; no application path for
  a solo operator with no model to align. Leave the remaining books in the backlog permanently.
- **Prompt engineering** — three overlapping sources ingested. There is no prompting problem
  here; there is a no-code-written problem.
- **Second-brain and digital-garden architecture** — three separate self-audits reached the
  same verdict: the architecture is ahead of the sources. A fourth comparison is pure cost.
- **Platform feature catalogs** — the vault knows every feature it does not use. Rule: no new
  platform page until hooks, subagents, or slash commands are actually running.
- **`data-science-ml\`** — the one area where more reading may still pay, but **inverted:**
  no new data-science page until an existing one has been executed in code.

---

## Decisions required from Chris

1. **Approve the sequence**, or reorder it. Steps 1–2 are loss-prevention and are recommended
   regardless.
2. **T1 — confirm the framing:** AI/ML Developer as named destination with prerequisites,
   data analysis as the near-term income-facing capability.
3. **The priority swap** in `NORTH_STAR.md` §4 — does income evidence outrank the study floor
   between now and December?
4. **Step 8 scope** — full instruction-layer cut, or the provenance trim only.

Nothing in this document has been implemented. Repairs already made today are recorded in
`DAILY_2026-08-11.md` and are limited to factual corrections in authority files.
