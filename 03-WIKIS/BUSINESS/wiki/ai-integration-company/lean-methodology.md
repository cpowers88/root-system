---
tags:
  - phase-3
  - audit
  - delivery
  - framework
---

# Lean Methodology (VSM, Seven Wastes, Five Principles)

> Sources: Rother & Shook's *Learning to See* (via an MSE507 lecture-deck condensation)
> and Womack & Jones's *Lean Thinking*. Migrated from FORGE July 7, 2026 — consolidates
> 10 FORGE pages. The field-walking method (VSM) and waste taxonomy are used directly
> in [[smb-ai-audit-method|SMB AI Audit Method]] Steps 2 and 4; this page holds the
> fuller framework, including the five-year Action Plan referenced from
> [[retainer-model|Retainer Model]].

## Purpose
Give the audit method its underlying discipline — how to actually walk and map a
client's operation, name waste precisely instead of vaguely, and (for larger
engagements) structure a multi-year retainer around a proven transformation roadmap.

## Key Idea
Most improvement efforts optimize one process in isolation and produce "isolated
victories" that don't reach the bottom line, because the fixed piece is still
surrounded by the same handoffs, batching, and inventory. **Map the entire flow before
fixing anything** — in practice this typically reveals 80–90% of total steps are waste
from the customer's standpoint. Waste is a **symptom**, not the problem itself; the
discipline is finding the cause behind each symptom, not just removing what's visible.

## Practical Actions

### Value Stream Mapping — The Field Method
Select one process/product family to map (start narrow — one workflow, not "the whole
business"). Walk it twice, both in person: first pass, no data — just observe how work
and information move and where things pile up. Second pass, collect real numbers by
hand — time per step, batch size, how often work sits waiting, who's involved. Draw the
map with pencil and paper in the work area itself, showing the customer first, then
material flow (left to right) and information flow (right to left, how work gets
triggered/scheduled). Key metrics: **process lead time** (total time a unit takes to
get through the whole flow) vs. **processing time** (time actually spent working on
it) — the gap between them is usually enormous, and that gap is the waste.

### The Seven Wastes (plus an eighth)
A naming checklist for what you're looking for during the walk:
1. **Overproduction** — doing/producing more than currently needed (the primary
   waste — it hides most of the others).
2. **Waiting** — idle time between steps.
3. **Transportation** — unnecessary movement of material, documents, or people.
4. **Unnecessary processing** — extra steps that add no value (re-entering data
   that was already captured once).
5. **Inventory** — excess WIP or stock, which also hides other problems (a long
   changeover time stays invisible if there's always a buffer covering for it).
6. **Unnecessary motion** — searching, walking, reaching for something that should
   be at hand.
7. **Correction** — reworking mistakes.
8. **(Eighth, added by Womack & Jones)** — delivering something that doesn't
   actually meet the customer's real need, no matter how efficiently it was produced.

### The "Monument" Diagnostic
Any machine, software system, or process too large or rigid to adapt, forcing
batch-style operation regardless of actual demand. A real example from the source: an
$80M grinding system that sped up one step but required 8-hour changeovers and 22
extra technicians — production actually got slower and more expensive despite the
individual machine being faster. **Automating a monument makes the waste more
expensive, not less** — always confirm a process isn't a monument before recommending
more automation on top of it.

### Takt Time and Pull
Once waste is named, the next question is pace, not speed: **takt time = available
work time ÷ customer demand** — the rate work should move, no faster (overproduction)
and no slower (a shortage). Use continuous flow wherever possible; where it breaks down
(long setups, unreliable steps, physical distance), use a pull mechanism — nothing
gets produced/started until the next step actually asks for it — instead of scheduling
every step independently from a forecast.

### The Five-Year Action Plan (Retainer Engagement Template)
For larger, multi-year retainer relationships, Womack & Jones's four-phase plan is a
directly adaptable structure:
- **Months 1–6**: find a named change agent with real authority, seize (or name) a
  visible crisis, map the current value stream, demand fast, visible early results.
- **Months 6–24**: reorganize around the value stream rather than department
  boundaries, put someone in charge of driving it forward, address the people question
  honestly (freed capacity needs a growth plan, not silent layoffs).
- **Months 24–48**: install new scorecards (a simple three-metric model — productivity,
  service, quality — works), make progress visible to everyone, right-size tools to
  the actual flow rate instead of maximum batch throughput.
- **Months 48–60**: shift from top-down direction to the client's own team driving
  further improvement — the point where the engagement can genuinely wind down rather
  than staying permanently necessary.

The pointed closing lesson worth quoting directly to a client: *"Toyota gets brilliant
results from average managers using brilliant procedures... don't search for brilliant
managers, perfect your processes."*

### The Lean Enterprise (Multi-Firm Waste)
Sometimes a client's waste isn't internal — it's inherited from suppliers or
subcontractors running batch-and-queue around them. When an audit finds waste that
traces upstream or downstream of the client's own firm, the fix may require convening
multiple firms, not just optimizing the one you were hired to look at. Worth naming
explicitly during scoping rather than quietly limiting the diagnosis to what's inside
one company's walls.

## Why It Matters
This is the discipline that separates a real audit from a guess: specific, nameable
waste categories instead of vague impressions, a field method for finding them, and (at
the high end) a proven multi-year structure for turning a single audit into a
sustained, valuable retainer relationship.

## Beginner Version
Walk-twice, seven-wastes-checklist, and takt-time framing on every audit's Step 2 and
Step 4 — see [[smb-ai-audit-method|SMB AI Audit Method]]. No formal VSM diagram needed
yet.

## Intermediate Version
Draw an actual current-state map (pencil, butcher paper, on-site) for engagements
where the client's process is genuinely complex or multi-department — the visual is
itself a strong sales artifact for the findings presentation.

## Advanced Version
Structure a multi-year retainer around the five-year Action Plan for clients ready for
a sustained transformation relationship, not just a one-time fix — see
[[retainer-model|Retainer Model]].

## Revenue Connection
The "monument" diagnostic directly protects against a bad recommendation (selling
automation on top of a process that isn't ready for it, which would fail and damage
trust). The five-year Action Plan is a template for the highest-value tier of retainer
relationship this business can sell.

## Human-Agent Management Connection
Right-sizing tools to actual flow rate (not maximum throughput) is the same discipline
[[quality-control-and-risk-gates|gate calibration]] applies to AI workflows — match the
system to real demand, not to what looks impressive.

## Risks / Failure Modes
- **Recommending automation on a monument** — makes the underlying waste more
  expensive and harder to reverse, not less.
- **Naming waste vaguely** ("things feel inefficient") instead of using the seven-wastes
  categories — vague findings don't convert to sold projects as well as specific ones.
- **Scoping only the client's own firm when the waste is actually upstream/downstream**
  — see the Lean Enterprise note above.

## Links to Related Pages
- [[smb-ai-audit-method]] — where the field method and waste taxonomy get applied directly
- [[retainer-model]] — the five-year Action Plan as an engagement structure
- [[theory-of-constraints]] — the sibling framework for prioritizing which waste to fix first
