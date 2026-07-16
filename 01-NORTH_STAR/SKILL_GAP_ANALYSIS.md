---
type: tracker
timeline: now
tags: [north-star]
---

# SKILL_GAP_ANALYSIS.md — Chris Powers
#AI #system 
### Location: .ROOT/01-NORTH_STAR/
### Last updated: July 16, 2026 (factual reconciliation; July ranking unchanged) | Review: Monthly (first session after 1st of month)

---

## Monthly Weak-Link Question

At the end of every monthly review, ask this one question:

> "What is the single skill gap most likely to block me in the next 90 days — and what is the smallest daily practice that closes it?"

Answer changes every month. Review it. Act on it. One gap at a time.

---

## Current Weak Links — July 2026
(Priority order — reassessed at July 5 monthly review)

**July 15 reconciliation:** the ranking below remains the July 5 monthly decision.
Only factual progress and next actions were corrected after the North Star migration;
the next re-ranking is August 1.

**1. SQL — still the biggest gap, now with a live vehicle**
The Academic Tracker V1 shipped on Python/SQLite, and the Revenue Lab scanner added
a bounded SQLite/API rep. The gap is no longer "no reps"; it is using SQL reliably
with real data. The next meaningful proof arrives when verified D2L/syllabus data
is loaded into the tracker around July 25.
Fix: use and debug the tracker on real course data; use a bounded SQL lesson only
when it supports that frontier and does not displace Physics/Python mastery.

**1.5 Technology landscape breadth — two first reps complete, integration still early**
The possibility map now exists (02-LIBRARY\REF-AI-AUTOMATION\TECHNOLOGY_LIBRARY_STRATEGY.md — 12 categories, need/waste signals, Recommendation Ladder). The gap is now reps, not structure.
The first Make.com landscape rep was completed July 9 and the first private Data
Studio dashboard rep was completed and visually verified July 16.
Fix: one 30-minute landscape rep weekly when school is on track. Next: build
integration depth and ROI judgment through the Advanced Application Capability
Trace in `TECHNOLOGY_LIBRARY_STRATEGY.md`, not another broad reading queue. The
July 16 goal-aligned audit selected the scanner's SQL/reliability boundary as the
first integrated proof and parked premature platform complexity.

**2. Structured business analysis — instinct without framework**
The instinct is there, TOC material is ingested, and one desk-sim observation is
captured. The documented method still lacks live workflow proof.
Fix: run one approved real observation and turn it into an actual-state map or VSM;
record where state, feedback, time, money, or trust leaks.

**3. Data visualization — first rep complete, decision communication unproven**
The private scanner dashboard closed the zero-rep gap. Findings still need to be
shown around a real decision, defensible calculation, and audience.
Fix: use the next justified dashboard to communicate cost, variance, or flow from
a real workflow; do not build a decorative second dashboard.

**4. Python depth — Stage 2 closed; Stage 3 loops active**
Stages 1-2 are independently verified. Stage 3's first live rep is paused during
`break`/`continue`; accumulator initialization and indentation need a light recheck.
Fix: follow the PYTHON wiki's current-position and close each stage through an
independent build/explain/debug gate before advancing.

---

## Side Project That Trains All Four Simultaneously

**Powers Operating Ledger (POL)**

Log your own daily work sessions to a CSV. Store in SQLite. Produce a weekly summary report. You are the test subject — no client needed, no dependency on anyone.

Trains: Python + SQL + data storage + report generation
Output: Something you actually use every day
Size: Stays small, stays completable

**Status: Parked.** It is not a current commitment; revive it only if a future
weak-link review finds it is the smallest useful proof vehicle.
Active repo: `pol` on cpowers88 GitHub.

---

## Audit Methodology — Reading List

### Core frameworks (read these first)

**"The Goal" by Eliyahu Goldratt**
Fiction format, reads fast. Teaches Theory of Constraints — how to find the bottleneck in any system. This is the mental model you already use without knowing its name. Read this one first.

**Value Stream Mapping (VSM)**
Search: "VSM lean manufacturing beginner" — free resources everywhere. Visual method for mapping every step in a process and identifying waste. Learn to draw one before your first audit conversation.

**"The Lean Startup" by Eric Ries**
Less about auditing, more about validated learning. How to test ideas before building full products. Relevant for the build side of the business.

### Online resources (free — bookmark these)

**iSixSigma.com** — Deep free library on process improvement. Search: "process audit checklist" and "waste identification."

**ASQ.org** — American Society for Quality. Professional body for quality and process improvement. Free articles section. This is vocabulary your future clients' operations managers already know.

**MIT OpenCourseWare — Operations Management** — Free university-level material. Use during school breaks when concepts connect to current coursework.

### Construction-specific

**ConstructionDive.com** — Industry news. Read the technology section. 10 minutes once a week.

**AGC.org** — Associated General Contractors. Technology section publishes real adoption data on what tools are and aren't working in the field.

**"Construction Productivity" on Google Scholar** — Skim abstracts only. The vocabulary is worth learning for client conversations.

---

## The Audit Methodology in Plain English

What a workflow audit actually is:

1. **Follow the work** — not the org chart, not the policy doc. Watch what actually happens.
2. **Map the actual process** — every step, every handoff, every wait.
3. **Find the three gaps** — where does state live incorrectly, where is feedback missing, what breaks if you delete this.
4. **Identify waste categories** — waiting, rework, double entry, tribal knowledge, manual handoffs.
5. **Prioritize by impact** — quick wins first, then structural fixes, then automation.
6. **Deliver the report** — process map + friction inventory + quick wins + tool recommendations + retainer proposal.

The audit itself is the first product. Software comes after the audit confirms what to build.

---

## Next Actions
- [ ] Load verified D2L/syllabus data into the shipped Academic Tracker around July 25; test the real workflow
- [ ] Use a bounded SQL segment only when it directly supports the tracker/live SQL gap
- [x] "The Goal" — ingested into the wiki June 2026 (TOC pages live, feeding audit methodology)
- [ ] Bookmark: iSixSigma.com, ASQ.org, ConstructionDive.com, AGC.org
- [ ] First live workflow observation and actual-state map/VSM (July priority #3)
- [x] First 30-min landscape rep — Make.com (July 9)
- [x] First Data Studio dashboard from a Sheet — completed and verified July 16
- [ ] Follow the Advanced Application Capability Trace without opening parallel projects
- [ ] Finish PYTHON Stage 3: break/continue, tracing, guessing game, mastery gate
- [ ] Keep POL parked unless a later weak-link review explicitly reactivates it
- [ ] Review this file at next monthly review — update weak links

---
*Captured: June 5, 2026 | Last reviewed: July 5, 2026 (July monthly review); facts reconciled July 16 without re-ranking*
*Next review: August 1, 2026 (monthly weak-link check)*
