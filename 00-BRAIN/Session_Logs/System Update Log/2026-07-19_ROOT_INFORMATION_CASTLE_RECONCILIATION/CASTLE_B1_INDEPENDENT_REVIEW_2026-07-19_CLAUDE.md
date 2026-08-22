---
type: report
timeline: log
status: active
tags: [castle, governance, north-star, slice-b1]
---

# CASTLE B1 Independent Review — Claude (Technology Engineer + Operator hats)

## Position of This Record

Independent challenge of Codex's
[[CASTLE_B0_1_CLOSURE_AND_B1_IMPLEMENTATION_PROPOSAL_2026-07-19]], returned in
the exact format that packet requested from its reviewer. B0.1 (already
installed) is verified, not re-litigated. B1 (proposal-only, no target
changed) is reviewed group-by-group below. Filing this record does not
authorize any B1 edit; Chris approves final wording before any B1 target is
archived or edited.

## Verification Performed Before Reviewing

Claims were checked against the live vault, not accepted from the packet:

- `01-NORTH_STAR\NORTH_STAR.md` — confirmed the Spring 2027 funding-constraint
  sentence is restored ("Near-term funding constraint..."), dated July 19.
- `01-NORTH_STAR\Goals & Milestones\CURRENT_STRATEGY.md` — confirmed dated
  July 19 ("mission-stack and capability-first reconciliation").
- `99-ARCHIVE\ARCHIVED_2026-07-19_NORTH_STAR_PRE_FUNDING_FACT_RESTORE.md` —
  confirmed present.
- `00-BRAIN\CASTLE\wiki\log.md` — confirmed the full A0→A2→B0→B0.1 trail is
  consistent with the packet's account, including the real bug B0.1 fixed
  (commit `8b83fc8` installed B0 companions but not `NORTH_STAR.md` itself,
  and `NOW.md` called an already-pushed commit uncommitted).
- Pulled and checked every quoted phrase in the B1 packet against its actual
  target file: `00-BRAIN\CASTLE\wiki\phase-map.md` (copied milestone table
  and "multi-industry client base" at Phase 10 — confirmed present),
  `00-BRAIN\CASTLE\wiki\decision-rules\adding-a-profit-skill.md` (no-orphan
  test wording — confirmed), `00-BRAIN\CASTLE\wiki\phases\phase-4-first-offer-readiness.md`
  (fixed prices, "Charging is non-negotiable — free audits attract non-buyers,"
  "Discounting to free... never $0" — confirmed), `00-BRAIN\CASTLE\wiki\phases\phase-1-school-core-technical-foundation.md`
  ("every course maps to a service," time management in Skills Needed —
  confirmed), `00-BRAIN\CASTLE\templates\phase-template.md` and
  `evidence-template.md` ("Tools to Learn," "Business Capability Unlocked,"
  "Self-use counts. Client use counts more. Paid use counts most." —
  confirmed). All quotes accurate; the diagnosis is real, not invented.

## Overall Verdict

**Approve with two required wording changes (Groups 6 and 8). Every other
group is sound as written and should not be touched further.**

## Per-Group Review

### 1. Phase map — sequence, not a second strategy — **KEEP**

Confirmed: `phase-map.md` carries a copied Current Strategy Milestones table
duplicating `CURRENT_STRATEGY.md`, and an unsupported "multi-industry client
base" requirement at Phase 10. Replacing the table with a pointer and
removing the unsupported requirement is correct and low-risk.

### 2. Phase 0 — generalize headings, preserve tracker proof — **KEEP**

Low-risk heading rename; SQLite/Python specifics stay because the approved
tracker actually uses them. No issue.

### 3. Phase 1 — coursework builds capability, not mandatory service — **KEEP**

"Every course maps to a service" is real and rigid — it forces an artificial
service mapping onto courses that may not have one. The replacement wording
keeps the option to connect coursework to real application without requiring
it. Removing time management from Skills Needed is correct since A2 already
treats capacity as a constraint; no duplication found elsewhere.

### 4. Phase 2 — transferable diagnosis under a current offer hypothesis — **KEEP**

Making Looker Studio a Recommendation-Ladder choice rather than a required
identity matches the Technology Engineer discipline already governing the
rest of the system (tools selected by the problem, not installed as identity).

### 5. Phase 3 — preserve the outcome, loosen the stack — **KEEP**

Same logic as Group 4. The pipeline (messy data → validated structure →
defensible analysis → decision-ready communication) stays fixed; the tool
list becomes options, which is accurate to current evidence — nothing has
locked SQLite/pandas/Looker/Markdown/PDF in as permanent beyond the tracker,
which correctly stays fixed.

### 6. Phase 4 — keep commercial discipline without freezing the offer — **MODIFY (required)**

**Hidden conflict found:** the proposal adds "Chris may explicitly authorize a
bounded $0 test after naming the evidence, displacement, and stop condition."
Phase 4's own live page already states "Charging is non-negotiable — free
audits attract non-buyers" and separately lists "Discounting to free —
discounted-for-case-study is the floor, never $0" as a named risk to avoid.
As drafted, B1 would quietly loosen a floor the system deliberately hardened,
without naming that it is doing so.

**Required exact wording insert**, tying the exception to the same mechanism
the profit-gate already uses rather than inventing a new one:

> Chris may authorize a bounded $0 test only as a named exception, on the
> same terms as [[adding-a-profit-skill]] § When to Break It — proof
> sentence, displacement, and stop condition recorded before it starts. This
> exception never redefines the audit's paid-floor default.

Everything else in Group 6 (prices/conversions/target counts as testable
source-derived assumptions, broadened contact pool, keeping rehearsal/pricing
logic as proof) is sound and should stay as proposed. On the contact-pool
broadening specifically: confirmed this does not relabel `CURRENT_STRATEGY.md`'s
S-02/S-03 wedge assumptions, only generalizes phase-level language to track
whichever wedge is live — consistent with Group 1's "CASTLE tracks, never
invents" principle.

### 7. Templates — capability and evidence before monetization — **KEEP**

All quoted phrases verified accurate. The generalization away from forced
service-connection and the tiered evidence-strength language ("independent
performance may be strongest for mastery; real operational use for
usefulness; willingness to pay or paid use for commercial proof") is a real
improvement — it replaces a single collapsed hierarchy with a claim-appropriate
standard.

### 8. Profit gate — broaden value without opening the floodgates — **MODIFY (required, highest priority)**

This is the load-bearing group. The no-orphan test is the system's named
mechanical defense against exactly the failure mode `NORTH_STAR.md` calls
"ideas are not commitments" and "planning can imitate progress" — and against
Chris's own documented high-tier idea-generation trait (`CHRIS_CORE.md`).

The proposed replacement adds "another credible North Star value path" as a
qualifying condition. That clause is too elastic: the North Star is
deliberately broad (learning, technology, business, systems), so nearly any
idea can be rationalized against it in one sentence. This is the precise
failure mode the rule's own "Why This Rule Exists" section warns against, and
it would convert a mechanical 60-second gate back into a judgment call — the
exact thing the rule exists to remove.

The genuinely good additions — "active capability gap" and "employability" —
are not currently covered by "school, a defined service, or an active
project" and should stay. Only the open-ended catch-all needs to go.

**Required exact replacement wording:**

> The idea must serve at least one of: a fixed commitment, an active
> capability gap named in a live phase, a real workflow or project already
> underway, employability tied to the current degree, or a current strategy
> assumption (S-01–S-05) it would generate evidence for. A general appeal to
> North Star alignment alone does not pass — name the specific phase,
> project, or assumption. If profit is claimed, name the economic mechanism
> and the evidence needed.

**Additional required check:** confirm the existing two-quarter phase-distance
rule ("If that phase is more than two quarters away, it does not enter the
skill map") survives the edit in explicit, checkable form. The packet's
"phase or activation condition" phrasing is vague enough to lose this rule by
accident during implementation — it must be restated explicitly, not implied.

## Falsifiability Concerns

Only Group 8's catch-all clause weakens falsifiability materially. Every
other group either preserves or improves it (Group 3 and 7 specifically
replace collapsed/rigid claims with claim-appropriate evidence standards).

## Tool-Specific Requirements to Preserve

None beyond what the packet already preserves: SQLite/Python in the Phase 0
tracker (correctly untouched, since the approved tracker actually uses them).

## Hidden Conflicts

One found and addressed above: Group 6's original $0-test language against
Phase 4's existing paid-floor doctrine. No other hidden conflicts found
across North Star, `CURRENT_STRATEGY.md`, or owner-truth boundaries.

## Final Implementation Order

Endorse the packet's proposed sequence (archive eleven B1 predecessors as one
batch → edit phase map, phases, profit gate, then templates → run scoped
semantic checks and canonical health → update CASTLE log/DAILY/NOW.md only if
the live action changed → stop broad system editing and return to real proof
→ Slice C + R1 on July 26). Add two validation items to the packet's existing
acceptance tests:

1. Grep confirms no B1 phase page still hard-codes a tool name (e.g. Flask)
   as a requirement without a live proof having selected it.
2. Grep confirms the profit-gate's two-quarter phase-distance rule string is
   present, unchanged, after the edit.

## Next Exact Action

Send this record's Group 6 and Group 8 exact wording to Codex for
incorporation. Once both are folded in, the packet's own acceptance tests are
the correct gate for implementation — no further review round needed from
Claude unless the wording changes introduce a new conflict.
