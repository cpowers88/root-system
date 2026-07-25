---
type: log
timeline: log
tags: [physics]
---

# Physics Education Log

Append-only session record.

## 2026-06-24 — Vault Initialized

### Objective
- Initialize physics education vault structure.

### Sources touched
- None yet.

### Files created/updated
- CLAUDE.md
- README.md
- FIRST_CLAUDE_PROMPT.md
- wiki core files
- templates

### Concepts/equations/problem types added
- None yet.

### Parked material
- None yet.

### Next action for Chris
- Add syllabus and textbook/chapter sources to `raw/`, then run `FIRST_CLAUDE_PROMPT.md` in Claude Code.

## 2026-06-25 — Source Intake and Stage 1 Packet

### Objective
- Run `FIRST_CLAUDE_PROMPT.md`: read syllabus and textbook, build the full learning path and core maps, and generate the first stage packet.

### Sources touched
- `raw/syllabus/syllabus.pdf` (PHYS 2211, KSU, Fall 2026, Dr. Behera)
- `raw/textbook/physic.pdf` (Serway & Jewett, *Physics for Scientists and Engineers*, 10th ed.)

### Files created/updated
- `wiki/source-map.md`, `wiki/learning-path.md`, `wiki/current-position.md`, `wiki/parking-lot.md`, `wiki/index.md`
- `wiki/concept-map.md`, `wiki/equation-map.md`, `wiki/calculus-map.md`, `wiki/problem-type-map.md`, `wiki/units-and-dimensions.md`
- `wiki/stages/stage-1-physics-and-measurement.md`
- `wiki/concepts/si-base-units.md`, `particle-model.md`, `dimensional-analysis.md`, `unit-conversion.md`, `order-of-magnitude-estimation.md`, `significant-figures.md`
- `wiki/equations/density.md`
- `wiki/problem-types/dimensional-consistency-check.md`, `unit-conversion.md`, `order-of-magnitude-estimation.md`, `sig-fig-arithmetic.md`
- `wiki/glossary/si-unit.md`, `dimension.md`, `order-of-magnitude.md`, `significant-figure.md`, `density.md`
- `wiki/flashcards/stage-1-physics-and-measurement.md`
- `wiki/drills/dimensional-analysis-drill.md`, `unit-conversion-drill.md`, `order-of-magnitude-drill.md`, `sig-fig-drill.md`
- `wiki/common-errors/stage-1-physics-and-measurement.md`
- `wiki/worked-examples/unit-conversion-speeding-example.md`

### Concepts/equations/problem types added
- Concepts: SI base units, particle model, dimensional analysis, unit conversion, order-of-magnitude estimation, significant figures.
- Equations: density (ρ = m/V).
- Problem types: dimensional consistency check, unit conversion, order-of-magnitude estimation, sig-fig arithmetic.

### Parked material
- Ch 10–12 (rotation, angular momentum, static equilibrium) and Ch 14 (fluid mechanics) — not mentioned in the syllabus course description; likely out of scope for PHYS 2211 specifically. Needs instructor/calendar confirmation.
- Full course calendar beyond Ch 5 (Sep 16, 2026) — the syllabus PDF's posted schedule table cuts off there.

### Next action for Chris
- ~~Confirm with the instructor or the full D2L calendar whether Ch 6, Ch 10–12, and Ch 14 are part of this course's scope.~~ **RESOLVED 2026-06-25.**
- Work through Stage 1: read the six concept pages, drill unit conversion and dimensional analysis until automatic, then check off the mastery checklist in `wiki/stages/stage-1-physics-and-measurement.md` before requesting the Stage 2 (Motion in One Dimension) packet.

## 2026-06-25 — Scope Confirmation: Ch 6–12 and Ch 14

### Objective
- Confirm and integrate Chris's report that Ch 6–12 and Ch 14 are all in scope for PHYS 2211.

### Sources touched
- `raw/textbook/Physics book-0101-0200.pdf` — sampled to confirm chapter locations
- `raw/textbook/Physics book-0201-0300.pdf`, `0301-0400.pdf`, `0401-0500.pdf`, `0501-0600.pdf` — first pages sampled to map chapter-to-file layout

### Files created/updated
- `wiki/source-map.md` — Ch 10, 11, 12, 14 moved from parked/uncertain to confirmed spine; textbook entry updated to reflect five split PDF files with textbook page ranges
- `wiki/learning-path.md` — Stage sequence expanded from 14 to 18 stages; Stage 10 (Ch 10), Stage 11 (Ch 11), Stage 12 (Ch 12), Stage 14 (Ch 14) added; Stages 13–18 renumbered
- `wiki/current-position.md` — confirmation note removed; full 18-stage scope noted
- `wiki/parking-lot.md` — Ch 10, 11, 12, 14, and Ch 6 calendar entry removed; only remaining parked item is full D2L lecture/exam calendar

### Concepts/equations/problem types added
- None (scope update only).

### Parked material
- Full D2L lecture/exam calendar for Ch 6+ — still needed to align stage dates to the syllabus schedule.

### Next action for Chris
- Share the full D2L course calendar (exam dates, Ch 6+ lecture dates) when available so stages can be aligned to deadlines.
- Continue working through Stage 1 — still the active unit. Do not move to Stage 2 until the mastery checklist in `wiki/stages/stage-1-physics-and-measurement.md` is complete.

## 2026-06-25 — Appendix Section Built

### Objective
- Extract all vital reference material from Serway & Jewett appendix PDFs and build a permanent wiki appendix section usable across all 18 stages.

### Sources touched
- `raw/textbook/Physics book-1201-1300-part-2.pdf` — Appendix A (Tables A.1–A.2) and Appendix B pp. A-4 to A-12
- `raw/textbook/Physics book-1301-1370.pdf` — Appendix B pp. A-13 to A-21, Appendix C (Periodic Table), Appendix D (SI Units)

### Files created/updated
- `wiki/appendix/index.md` — navigation page with quick-reference by stage
- `wiki/appendix/si-units.md` — 7 SI base units, all derived SI units (Table D.1, D.2), full SI prefix table
- `wiki/appendix/conversion-factors.md` — Table A.1: length, mass, time, speed, force, energy, pressure, angle
- `wiki/appendix/quantity-table.md` — Table A.2: all PHYS 2211 physical quantities with symbol, dimensions, SI unit; mechanics quantities organized by stage group
- `wiki/appendix/math-algebra.md` — B.1 scientific notation; B.2 algebra (fraction rules, Table B.1 exponents, factoring, quadratic formula, linear equations, simultaneous equations, logarithms)
- `wiki/appendix/math-geometry-trig.md` — B.3 geometry (areas, volumes, curve equations, radian measure); B.4 trigonometry (definitions, common angle table, Table B.3 identities, law of cosines/sines, vector decomposition diagram)
- `wiki/appendix/math-calculus.md` — B.5 series expansions and small-angle approximations; B.6 differential calculus (Table B.4 derivatives, chain/product/quotient/sum rules); B.7 integral calculus (Table B.5 indefinite integrals, Table B.6 definite integrals, integration by parts); calculus-physics quick reference table
- `wiki/appendix/uncertainty.md` — B.8 propagation of uncertainty (three rules: multiply/divide → percent, add/subtract → absolute, powers → multiply percent by exponent)
- `wiki/source-map.md` — two appendix PDF entries added
- `wiki/index.md` — appendix section added to top of index

### Concepts/equations/problem types added
- All core math tools from Appendix B fully documented
- All conversion factors from Table A.1 reproduced
- All PHYS 2211 physical quantities catalogued with symbols and units

### Parked material
- Appendix C (Periodic Table): not reproduced — minimal relevance for mechanics
- Table B.6 (Gauss's probability integrals): included in math-calculus.md but marked as beyond Stage 17 scope

### Next action for Chris
- The appendix section is now complete. Use `wiki/appendix/index.md` as a quick-reference during all problem-solving work.
- Continue working through Stage 1 — still the active unit.
- Share the full D2L course calendar (exam dates, Ch 6+ lecture dates) when available.

## 2026-06-25 — Full Vault Pre-Build (Cruise Preparation)

### Objective
- Build all 18 stage packets in full before a 10-day cruise with no internet access. Scope restriction bypassed per Chris's explicit request.

### Sources touched
- Appendix PDFs (already processed in previous session)
- Textbook knowledge (Serway & Jewett 10th ed., Ch 1–17 and Ch 38) used to author all stage content

### Files created/updated (this session)

**Stage packets (stage overview files):**
- `wiki/stages/stage-5-laws-of-motion.md` ✅ (built directly)
- `wiki/stages/stage-2-motion-in-one-dimension.md` ✅ (built by fork, previous session)
- `wiki/stages/stage-3-vectors.md` ✅ (built by fork)
- `wiki/stages/stage-4-motion-in-two-dimensions.md` ✅ (built by fork)
- `wiki/stages/stage-6-circular-motion.md` ✅ (built by fork)
- `wiki/stages/stage-8-conservation-of-energy.md` ✅ (built by fork)
- `wiki/stages/stage-9-linear-momentum.md` ✅ (built by fork)
- `wiki/stages/stage-10-rotation.md` ✅ (built by fork)
- `wiki/stages/stage-11-angular-momentum.md` ✅ (built by fork)
- `wiki/stages/stage-14-fluid-mechanics.md` ✅ (built by fork)
- `wiki/stages/stage-16-wave-motion.md` ✅ (built by fork)
- Stages 7, 12, 13, 15, 17, 18 — built by background forks (in progress as of this log entry)

**Stage 5 supporting files (all new):**
- `wiki/flashcards/stage-5-laws-of-motion.md`
- `wiki/common-errors/stage-5-laws-of-motion.md`
- `wiki/drills/fbd-drawing-drill.md`, `newtons-second-law-drill.md`, `friction-problems-drill.md`, `inclined-plane-drill.md`
- `wiki/equations/newtons-second-law.md`, `weight.md`, `kinetic-friction.md`, `static-friction.md`
- `wiki/concepts/force.md`, `newtons-first-law.md`, `newtons-second-law.md`, `newtons-third-law.md`, `mass-vs-weight.md`, `normal-force.md`, `friction.md`, `free-body-diagram.md`
- `wiki/problem-types/fbd-single-object.md`, `fbd-connected-objects.md`, `inclined-plane.md`, `atwood-machine.md`, `friction-problems.md`
- `wiki/worked-examples/fbd-block-on-table.md`, `inclined-plane-with-friction.md`, `atwood-machine-worked.md`
- `wiki/glossary/force.md`, `inertia.md`, `net-force.md`, `weight.md`, `normal-force.md`, `friction.md`, `tension.md`, `free-body-diagram.md`

**Appendix section (previous session, fully complete):**
- `wiki/appendix/index.md`, `si-units.md`, `conversion-factors.md`, `quantity-table.md`, `math-algebra.md`, `math-geometry-trig.md`, `math-calculus.md`, `uncertainty.md`

**Map files corrected (previous session):**
- `wiki/concept-map.md` — full 18-stage dependency chain added
- `wiki/calculus-map.md` — all 18 stages mapped
- `wiki/equation-map.md` — updated to 18-stage listing
- `wiki/learning-path.md` — stale note removed

### Concepts/equations/problem types added

**Stage 5:**
- Concepts: force, inertia, Newton's 1st/2nd/3rd laws, mass vs. weight, normal force, friction (static and kinetic), free body diagram
- Equations: F = ma, w = mg, f_k = μ_k n, f_s ≤ μ_s n
- Problem types: FBD single object, FBD connected objects, inclined plane, Atwood machine, friction problems

### Parked material
- None new this session.

### Next action for Chris
- All 18 stage packets are being built for offline cruise use. When complete, begin with Stage 1 and work forward through the sequence.
- Use `wiki/appendix/` as a reference for math, units, and conversions throughout all stages.
- When you return from the cruise, share the full D2L lecture/exam calendar so stage dates can be aligned to deadlines.

## 2026-07-07 — .ROOT System Alignment

### Objective
- Bring PHYSICS's instructional/navigation files into alignment with the July 7, 2026 wiki unification standard (matched against sibling hubs TECHNOLOGY, SYSTEMS, AI_AUTOMATION_SYSTEMS) and confirm North Star routing is current.

### Sources touched
- `00-BRAIN\AI_Agent.md`, `01-NORTH_STAR\NORTH_STAR.md`, `00-BRAIN\vault_map.md`, `00-BRAIN\WHERE_IT_GOES.md` — read for the current governance standard
- Sibling wikis' root structure and frontmatter conventions (TECHNOLOGY, SYSTEMS, BUSINESS, AI_AUTOMATION_SYSTEMS)

### Files created/updated
- Added Tag Standard frontmatter (`type:`/`tags:`) to `CLAUDE.md` and to 10 `wiki/` root files that lacked it: `index.md`, `log.md` (this file), `learning-path.md`, `source-map.md`, `concept-map.md`, `equation-map.md`, `calculus-map.md`, `problem-type-map.md`, `units-and-dimensions.md`, `parking-lot.md`, `current-position.md`

### Files archived (nothing deleted, per WHERE_IT_GOES.md)
- `CREATE_PHYSICS_STRUCTURE.ps1` → `99-ARCHIVE\ARCHIVED_2026-07-07_PHYSICS_CREATE_STRUCTURE_pre_ROOT_migration.ps1` — dead script, targeted the pre-migration `G:\My Drive\.PHYSICS_ED` path; skeleton is frozen so it can never run correctly again.
- `README.md` → `99-ARCHIVE\ARCHIVED_2026-07-07_PHYSICS_README_superseded_by_CLAUDE_and_index.md` — referenced a `FIRST_CLAUDE_PROMPT.md` bootstrap file that no longer exists; its job (orientation, key-file map, academic-integrity note) is now fully covered by `CLAUDE.md`'s Start-of-Session Protocol, `HOW_TO_USE.md`, and `wiki/index.md`. Matches the TECHNOLOGY/SYSTEMS root pattern (`raw/`, `wiki/`, `CLAUDE.md`, `HOW_TO_USE.md` — no root README).

### Concepts/equations/problem types added
- None — this was a governance/structure pass, not a content session.

### Verified, no change needed
- `vault_map.md` and `WHERE_IT_GOES.md` already list PHYSICS correctly under the 7-hub `03-WIKIS` structure (stages 1–18, Realm Check routing line intact).
- `CLAUDE.md` and `HOW_TO_USE.md` content already reflects the current course (PHYS 2211, Fall 2026, Aug 24 start) and North Star Track 1 priority — no factual drift found.

### Parked material
- Individual content pages (`wiki/concepts/`, `equations/`, etc.) carry `type:` frontmatter but are missing the `tags:` line the Tag Standard requires (timeline + topic tags). ~300 pages — out of scope for this pass; flag for a future dedicated cleanup session if Chris wants full Tag Standard compliance at the page level.

### Next action for Chris
- Nothing blocking. Resume the stage-packet build (see prior entry) or continue Stage 1 practice — the alignment pass did not touch stage content.

## 2026-07-07 — Stage 3 (Vectors) Data Review

### Objective
- Chris is currently working on Stage 3 (Vectors). Review the stage against the actual source textbook and process any missing or misfiled data before continuing.

### Sources touched
- `raw/textbook/Physics book-0001-0100.pdf` — extracted full text (pdftotext) and read Chapter 3 (Vectors) directly to verify section structure and content against `wiki/stages/stage-3-vectors.md`.

### Findings
1. **Missing content:** Section 3.1 "Coordinate Systems" (Cartesian vs. polar coordinates, conversion equations) was not covered anywhere in the Stage 3 packet, even though it's real, examinable Ch 3 content that comes before vector components in the textbook's own order.
2. **Wrong citation:** Stage 3's "Textbook Alignment" claimed "sections 3.1–3.6" — the chapter only has four sections (3.1–3.4). Corrected.
3. **Misplaced content:** The dot product was listed as a Stage 3 "Core Concept" and required mastery item. The textbook explicitly states (Preface, "Mathematical Level") that the dot product is not formally introduced until **Chapter 7** (Energy of a System) and the cross product not until **Chapter 11** (Angular Momentum) — this matches Stage 7's own packet, which already lists "dot product" as a prerequisite pulled forward from Stage 3. Reclassified dot product from required-now to Parked for Later (preview) in the stage packet, flashcards, and mastery checklist — the existing concept/equation pages were not deleted, just re-scoped, since the content is accurate and will be needed at Stage 7.
4. **Untracked raw source:** `raw/textbook/Physics book-0001-0100.pdf` exists in `raw/` and was already used to build Stages 1–3, but was never added to `wiki/source-map.md`'s Sources table. Added.
5. **Vault-wide gap (noted, not fixed beyond Stage 3):** `concept-map.md`, `equation-map.md`, and `problem-type-map.md` were never updated after Stages 2–18 were built in the cruise-prep session — they still only documented Stage 1. Added Stage 3 to all three; flagged Stages 2 and 4–18 in `parking-lot.md` for stage-by-stage backfill rather than one large batch session (matches "one stage's frontier at a time").

### Files created/updated
- **New:** `wiki/concepts/coordinate-systems.md`, `wiki/equations/polar-cartesian-conversion.md`, `wiki/problem-types/polar-cartesian-conversion.md`, `wiki/glossary/cartesian-coordinates.md`, `wiki/glossary/polar-coordinates.md`, `wiki/worked-examples/polar-coordinates-conversion-example.md`, `wiki/drills/polar-cartesian-conversion-drill.md`
- **Updated:** `wiki/stages/stage-3-vectors.md` (section citation fix, coordinate systems added, dot product reclassified), `wiki/flashcards/stage-3-vectors.md` (2 new cards, dot-product cards marked preview), `wiki/concept-map.md`, `wiki/equation-map.md`, `wiki/problem-type-map.md` (Stage 3 rows added + gap flagged), `wiki/current-position.md` and `wiki/index.md` (active stage corrected from Stage 1 to Stage 3), `wiki/source-map.md` (missing raw file logged), `wiki/parking-lot.md` (map-backfill item added)

### Concepts/equations/problem types added
- Concept: coordinate systems (Cartesian/polar). Equation: polar↔Cartesian conversion. Problem type: polar-Cartesian conversion. Glossary: Cartesian coordinates, polar coordinates.

### Parked material
- Stages 2, 4–18 backfill into the three master map files — see `parking-lot.md`.

### Next action for Chris
- Start Stage 3 with [[../concepts/coordinate-systems]] (the newly added piece) before vector components — that's the textbook's actual order. Ignore the dot product pages for now; they'll matter at Stage 7.

## 2026-07-07 — Stages 4–5 Data Review (Ahead-Check)

### Objective
- Chris asked to check the next couple of stages after Vectors so he isn't held up, and save the rest (Stages 6–18) for a later pass. Reviewed Stage 4 (Motion in Two Dimensions) and Stage 5 (The Laws of Motion) against the source textbook the same way Stage 3 was checked.

### Sources touched
- `raw/textbook/Physics book-0001-0100.pdf` and `Physics book-0101-0200.pdf` — extracted full text (pdftotext) and read Chapter 4 (all 6 sections) and Chapter 5 (all 8 sections) directly.

### Findings
1. **Stage 4 — real gap found:** Section 4.5 "Tangential and Radial Acceleration" (the non-uniform-circular-motion case: total acceleration = radial + tangential component when speed is also changing) was completely absent from the stage packet. Worse, both `wiki/concepts/uniform-circular-motion.md` and `wiki/equations/centripetal-acceleration.md` explicitly told Chris this topic "becomes important in Stage 10" — wrong. It's Chapter 4 material (right after uniform circular motion, Section 4.5), in scope for the Sep 4/9 lecture window. Stage 10 covers a different, later topic (rotational dynamics: torque, moment of inertia). Built out the missing piece and corrected both misdirecting notes.
2. **Stage 4 — citation fixed:** "Textbook Alignment" previously said only "approx. pp. 78–104" with no section list. Added the full 4.1–4.6 section breakdown for clarity.
3. **Stage 5 — verified clean:** Checked all 8 sections (5.1 Concept of Force through 5.8 Forces of Friction) against the existing concept pages (force, Newton's 1st/2nd/3rd laws, mass-vs-weight, normal-force, friction, free-body-diagram). Full coverage, citation ("sections 5.1–5.8") already correct. No changes made.

### Files created/updated
- **New:** `wiki/concepts/tangential-and-radial-acceleration.md`, `wiki/equations/tangential-and-radial-acceleration.md`, `wiki/problem-types/nonuniform-circular-motion.md`, `wiki/drills/tangential-radial-acceleration-drill.md`
- **Updated:** `wiki/stages/stage-4-motion-in-two-dimensions.md` (section citation, new concept/equation/problem-type/drill links, variables table, diagram, mastery checklist, Parked-for-Later corrected), `wiki/concepts/uniform-circular-motion.md` and `wiki/equations/centripetal-acceleration.md` (removed incorrect "Stage 10" deferral), `wiki/flashcards/stage-4-motion-in-two-dimensions.md` (2 new cards), `wiki/common-errors/stage-4-motion-in-two-dimensions.md` (2 new errors), `wiki/concept-map.md`, `wiki/equation-map.md`, `wiki/problem-type-map.md` (Stage 4 and Stage 5 rows added; gap flag narrowed to Stage 2 and 6–18), `wiki/current-position.md` (Ahead-Check section added), `wiki/parking-lot.md` (backfill flag updated)

### Concepts/equations/problem types added
- Concept + equation + problem type: tangential and radial acceleration (non-uniform circular motion).

### Parked material
- Stage 2 and Stages 6–18 still need the same source-verification pass this session gave Stages 3–5. Per Chris's instruction, not done now — check each one stage-ahead as he progresses, same method: extract the relevant textbook PDF range with `pdftotext`, read the actual section list, compare against the existing stage packet.

### Next action for Chris
- No blockers for Stage 3, 4, or 5 — all three are now verified against the source textbook. Continue with Stage 3 (coordinate systems first), and Stage 4/5 will be ready when reached.

## 2026-07-09 — CLAUDE.md dedup (system-wide, Chris-approved)

### Objective
- Record the operating-file change: duplicated shared blocks (academic integrity,
  chunking) replaced by a pointer to `00-BRAIN\AI_Agent.md § Wiki Shared Layer`;
  this wiki also gains the raw-immutability rule it previously lacked. Expanded
  session protocols stay. No physics content changed.
  Record: `00-BRAIN\Session_Logs\DAILY_2026-07-09.md`.

### Next action for Chris
- Resume Vectors — output reps begin July 10 (cross product ahead; flag 16 anchor
  due when vector products appear).

## 2026-07-09 — Citation/sort audit (Chris-directed, all-wikis sweep)

### Objective
- Sixth hub in the hub-by-hub citation-and-sorting sweep: index vs. live
  tree, frontmatter, raw/ coverage.

### Findings and fixes
- **Index Folders section was badly stale** — still described Stage-1-era
  counts ("concepts/ 6 pages", "common-errors/ 1 page") while the live tree
  holds 58 concepts, 42 equations, 36 problem-types, 35 drills, 46 glossary,
  18 flashcard decks, 18 common-errors pages, and all 18 stage packets from
  the July cruise-prep build. Rewrote the section with live counts, the
  stage-first navigation note, and the generated-vs-studied warning.
- `stages/stage-13-universal-gravitation.md` began with a UTF-8 BOM that
  can break frontmatter parsing — stripped (content untouched).
- raw/ fully accounted for: syllabus + textbook chunks 0001–0600 and
  1201–1370 are all referenced by wiki/log; the 0601–1200 gap is the parked
  Physics-II material, consistent with [[parking-lot]].
- Planned-page wikilinks inside packet pages (~138, e.g. drills and
  problem-types not yet generated) left alone — they resolve as stages
  activate; monthly lint owns the count.

### Next action
- Unchanged: Stage 3 Vectors output rep (Chris's active stage). No system
  work needed here before it.

## 2026-07-11 — CLAUDE.md slim pass (Chris-approved, flag 64)

### Objective
- Slim the always-loaded wiki OS per the Claude-docs review
  (`00-BRAIN\Session_Logs\CLAUDE_DOCS_SYSTEM_REVIEW_2026-07-11.md`).

### Sources touched
- None (system session, no physics content).

### Files created/updated
- CLAUDE.md slimmed 295 → 130 lines; frontmatter timeline tag fixed
  `now` → `reference` (Tag Standard). Old version archived:
  `99-ARCHIVE\ARCHIVED_2026-07-11_PHYSICS_CLAUDE.md`.
- NEW [[authoring-standards]] — core-file specs, four page types,
  stage-packet requirements, writing rules, intake protocol, session
  protocols (all moved from CLAUDE.md, nothing deleted).
- [[index]] — new page registered.

### Concepts/equations/problem types added
- None.

### Parked material
- None new.

### Next action for Chris
- Unchanged: Stage 3 Vectors output rep.

## 2026-07-14 — Stage 3 (Vectors) first live teaching session, paused mid-problem

### Objective
- Run the first live teaching pass on Stage 3 (Vectors) per this wiki's protocol
  (situation → model → quantities → equation → units → problem type → worked
  example → drill), with Chris solving live problems rather than only reading
  the packet.

### Sources touched
- `wiki/stages/stage-3-vectors.md`, `wiki/concepts/coordinate-systems.md`,
  `scalar-vs-vector.md`, `vector-components.md`, `wiki/common-errors/stage-3-vectors.md`
  (read as teaching source; not modified).

### Concepts/equations/problem types added
- None new. This was a teaching rep on existing packet content, not authoring.

### What Chris demonstrated live
- **Coordinate systems:** correctly converted Cartesian (−30, 40) m to polar
  (50 m, 126.87°); self-caught a degree/radian mode mixup on the first pass.
- **Scalar vs. vector:** correctly classified 4 examples; independently
  generalized that adding a direction converts a scalar (distance) into a
  vector (displacement) — one nuance correction given on tension's direction
  being along-the-rope, not assumed-downward.
- **Vector decomposition:** correctly computed Fx = 65.53 N, Fy = 45.89 N from
  80 N at 35°; initially dropped units (newton vs. joule confusion), corrected
  after discussion.
- **Vector reconstruction:** correctly found A = 13 m, θ = 157.38° from
  Ax = −12 m, Ay = 5 m, including the quadrant correction.
- **Vector addition by components:** introduced (40 N at 0° + 30 N at 90°) but
  not completed — Chris had to leave mid-problem.

### Parked material
- None new.

### Next action for Chris
- Resume the paused addition problem (40 N at 0°, 30 N at 90° — explain why
  70 N is wrong before computing the resultant by components).
- After that, one more independent pass over all four skills (conversion,
  scalar/vector ID, decomposition, reconstruction, addition) without notes,
  then check off the Stage 3 mastery checklist in
  `wiki/stages/stage-3-vectors.md` before moving to Stage 4.

## 2026-07-14 — Focused Physics Anki deck reset (Codex + Chris)

### Objective
- Convert the existing broad Physics flashcard stacks into a stage-aligned active
  deck that supports the Stage 3 Vectors frontier without cramming later physics.

### Sources touched
- `wiki/flashcards/stage-1-physics-and-measurement.md`
- `wiki/flashcards/stage-2-motion-in-one-dimension.md`
- `wiki/flashcards/stage-3-vectors.md`
- `wiki/flashcards/stage-4-motion-in-two-dimensions.md` (preview boundary only)

### Files created/updated
- New: `02-LIBRARY\00-SCHOOL\02-Physics I\Flash Cards\Physics_Stages_01-03_Active.tsv`
  (35-card Anki import deck), `README_IMPORT_INSTRUCTIONS.md`, and
  `ADAPTIVE_REVIEW_LOG.md`.
- Updated: `wiki/index.md` and this log.

### Concepts/equations/problem types added
- None. This is a retrieval-layer reset using existing vetted stage cards; dot and
  cross products remain excluded because they are parked beyond the Stage 3 frontier.

### Parked material
- Stage 4 and later decks remain out of the active queue. Stage 4 is the next
  preview only; no later-stage cram deck is authorized.

## 2026-07-16 — Full stage-separated Anki package built (Claude Code, CASTLE hat)

### Objective
- Chris deleted the old Anki decks (they had grown unstructured and too far
  ahead of his actual position) and asked for a complete rebuild: the whole
  thing under one `Physics` deck in Anki, separated by stage, so he can open
  only the subdeck he actually needs instead of facing everything at once.

### What changed
- Wrote `02-LIBRARY\00-SCHOOL\02-Physics I\Flash Cards\Physics_All_Stages.apkg`
  via a one-off `genanki` script (`build_physics_anki.py`, run from the
  scratchpad, not added to the vault). It parses all 18
  `wiki/flashcards/stage-N-*.md` files directly — no content re-authored — and
  emits one Anki package containing 18 subdecks (`Physics::Stage 01 - ...`
  through `Physics::Stage 18 - ...`), 223 cards total. Stage 3's two dot/
  cross-product preview cards carry a `preview` tag.
- Rewrote `README_IMPORT_INSTRUCTIONS.md` to point at the new package (single
  `File → Import`, no manual note-type/separator setup) and marked the July 14
  active TSV and the pre-7/14 mixed decks as superseded-but-preserved.
- Added a superseded note to `ADAPTIVE_REVIEW_LOG.md`'s rotation table.
- Updated this wiki's `index.md` Active Stage block to Stage 4 (Stage 3 closed
  earlier today) and pointed its recall-deck line at the new package.

### Why this shape
- One package instead of 18 separate TSV imports — Chris only performs one
  `File → Import` action, and Anki builds the `Physics::` hierarchy itself from
  the deck names.
- Generated straight from the existing wiki flashcard pages rather than
  rewritten, so the Anki deck and the wiki source cannot drift apart silently —
  regenerating the script after a flashcards/ edit reproduces the package.

### Not done
- Did not delete or archive the July 14 TSV or the pre-7/14 mixed decks;
  AGENT.md file-safety preserves superseded artifacts rather than removing them.
- Did not touch `wiki/flashcards/*.md` content itself — this session only reads
  that source; any card wording fix belongs in those files, then a package
  rebuild.

### Next
- Import `Physics_All_Stages.apkg`, rename/archive any leftover pre-7/14 mixed
  deck in Anki, and study only the `Stage 04` subdeck (plus Stage 01–03 for
  spaced review) going forward.

### Next action for Chris
- Rename the old mixed Physics deck to `Physics::Archive::Pre-2026-07-14`, import
  the focused deck as `Physics::Active::Stages 1-3`, and begin a baseline review.

## 2026-07-14 — Operating contract made model-neutral

- Changed the hub teaching contract from Claude-exclusive wording to “any AI
  teaching physics.” No lesson, stage, mastery, or learner-state content changed.
- Next action remains the paused Stage 3 vector-addition problem already recorded
  above and in the session handoff.

## 2026-07-14 — Learning-path truth reconciled to live Stage 3

- Replaced the stale Stage 1 path status with the live Stage 3 Vectors frontier.
- Marked all 18 packets as generated without calling them mastered; Stages 4–5 are
  source-verified but unstudied, and later stages await sequential re-verification.
- Fixed two broken relative stage links in `current-position.md`.
- Next: resume 40 N at 0° + 30 N at 90°, explain why the resultant is not 70 N,
  then complete a no-notes Stage 3 pass.

## 2026-07-14 — Human guide and prep-plan route verified

- Updated HOW_TO to point to the pre-semester plan and the live learner-state
  authority, including the exact paused Stage 3 action and provisional status of
  generated-but-unmastered packets.
- Cross-reference validation found no active dead link; the next action is unchanged.

## 2026-07-15 — Stage 3 vector-addition problem resumed and solved

### Objective
- Resume the paused 2026-07-14 problem (40 N at 0° + 30 N at 90°) live with Chris,
  per this wiki's teach-then-verify method.

### Sources touched
- `wiki/stages/stage-3-vectors.md`, `wiki/common-errors/stage-3-vectors.md` (read
  as teaching source; not modified).

### What Chris demonstrated live
- Explained why the resultant isn't 40+30=70 N (vector addition depends on
  direction, not just magnitude) after a vocabulary correction.
- Built components from the cos/sin formula: Ax=40, Ay=0, Bx=0, By=30.
- Added components correctly (Rx=40, Ry=30) and computed R=50 N independently.
- Made an angle error (53.13°, the complement of the correct answer) then
  self-corrected to 36.87° from the +x axis, correctly diagnosing that he'd
  measured off the wrong leg of the triangle — without being told.

### Concepts/equations/problem types added
- None new. Teaching rep on existing packet content (vector addition by
  components), the one Stage 3 skill previously flagged as not yet attempted.

### Parked material
- None new.

### Next action for Chris
- This was the easiest case (both vectors axis-aligned, no real decomposition
  needed). Do one more rep with two vectors at non-axis angles, so both actually
  get decomposed, then complete the required no-notes pass over all four Stage 3
  skills (conversion, scalar/vector ID, decomposition, reconstruction, addition)
  before checking off the mastery checklist in `wiki/stages/stage-3-vectors.md`.

## 2026-07-15 — Semester pathway and source-quality unification

### Objective
- Reconcile the full Physics wiki with the updated `.ROOT` context, finish the
  visible Stage 1–18 route, and create a stage-gated trigonometry/calculus refresh
  path grounded in real physical situations.

### Sources touched
- `raw/syllabus/syllabus.pdf` (visual review of the 19-page scan; no raw edits).
- All split Serway textbook PDFs and appendix PDFs (TOC/source screen; no raw edits).
- `02-LIBRARY/REF-META-HOW-TO-WORK/Christopher_Aptitude_Results.pdf` (visual and
  text review used only to choose learning sequence and retrieval supports).
- Official OpenStax, MIT OpenCourseWare, and PhET pages registered in
  `wiki/source-map.md` as optional support for diagnosed gaps.

### Structure completed
- Added `wiki/math-readiness-path.md`: physical sketch → exact math move → guided
  repetition → no-notes transfer → verbal explanation → later cold check.
- Added a complete Stage 1–18 semester control table to `wiki/learning-path.md`
  with math gates, real-life anchors, source status, and packet routes.
- Backfilled Stage 2 and Stages 6–18 into the concept, equation, and problem-type
  maps; fixed their root-map link paths.
- Corrected textbook alignment for Stage 2 (through 2.9), Stage 7 (through 7.9),
  and Stage 17 (17.1–17.7 active; 17.8 parked).
- Updated the hub, current-position, calculus map, source map, parking lot, and
  human guide. No learner mastery checkbox was changed.

### Source-quality findings
- The syllabus PDF is reliable for course identity, outcomes, grading categories,
  and AI policy, but not yet reliable for operations: its calendar ends at Ch 5;
  it includes a January access deadline, an impossible day/date pairing, a recycled
  holiday label, and conflicting exam-drop wording. Live D2L/Owl Express must
  settle those items.
- Textbook screens identified content/scope gates at Stage 6 section 6.3, Stage 9
  sections 9.7–9.9, Stage 11 precession, Stage 14 sections 14.3 and 14.7–14.8,
  and Stage 15 sections 15.6–15.7. These are parked until the live course scope is
  known; later supporting pages remain just-in-time work.
- The Serway appendices already supply the baseline algebra, trigonometry,
  derivatives, and integrals, so a second downloadable math textbook is not needed.

### Next action for Chris
- Resume Stage 3 with two non-axis vectors so both vectors require decomposition,
  then complete the full no-notes Stage 3 pass. Use the Stage 2 calculus bridge
  next: read slope and area from one position/velocity graph before applying a
  kinematic formula.

## 2026-07-15 — Full syllabus and learning-profile closure audit

### Objective
- Confirm that every syllabus page and every named physics outcome has a visible
  destination before closing the Physics folder; review the two additional
  YouScience files supplied by Chris.

### Sources touched
- All 19 pages of `raw/syllabus/syllabus.pdf`, visually inspected.
- `Christopher_Aptitude_Discussion.pdf` (6 pages), visually inspected and text
  checked.
- `Christopher_Aptitude_Results.pdf` (35 pages), previously visually/text reviewed
  during this session and reconfirmed as an input.
- `Christopher_One_Page_Summary.pdf` (1 page), visually inspected and text checked.

### Changes and findings
- Added `wiki/syllabus-coverage-ledger.md`, routing every PDF page to a stage,
  course operations, institutional governance, or student support.
- Applied the syllabus learning outcomes across all stages through a shared mastery
  standard: interpret, represent/model, solve symbolically and numerically, use
  vectors/calculus as needed, check units/reasonableness, and connect to real life.
- Confirmed that every named physics topic in the syllabus is represented in the
  Stage 1-18 sequence. The printed calendar itself still stops at Stage 5/September
  16, so later weeks cannot be assigned official dates without D2L.
- Added the late-homework contradiction to the data-quality gate: page 4 describes
  a 10% daily penalty, while page 7 says work is unavailable after answers release.
- Expanded the math-learning method with strengths from all three profile files:
  numerical pattern finding, spatial/tangible models, thinking aloud, alternate
  approaches followed by a stable process, visible future target, and one next
  action at a time.

### Next action for Chris
- The learning path is closed structurally. Supply the live D2L calendar and current
  grading/exam details when available; until then, treat only the chapter sequence
  as authoritative and all week/date assignments after Chapter 5 as provisional.

## 2026-07-16 — Non-axis vector-addition rep solved; real textbook problem set added

### Objective
- Complete the harder non-axis-angle vector-addition rep flagged 2026-07-15, then
  build a real-textbook problem set (not generated numbers) for Stage 3, per
  Chris's request to work actual Serway end-of-chapter problems going forward and
  flag specific ones for the full reflection/teaching treatment.

### Sources touched
- `raw/textbook/Physics book-0001-0100.pdf` — extracted via `pdftotext -layout`
  to pull the real Chapter 3 "Problems" section (problems 1–32, pp. 63–66) rather
  than generating new numbers.

### What Chris demonstrated live
- A⃗ = 25 N at 40°, B⃗ = 15 N at 120° (both from +x). Correctly computed
  Ax=19.15, Ay=16.07, Bx=−7.5, By=12.99, Rx=11.65, Ry=29.06, R=31.31 N,
  θ=68.15°, and correctly reasoned the quadrant (both Rx, Ry positive → no
  adjustment). This is the first rep where both vectors actually required
  decomposition (no axis-aligned shortcut). The "ladder against a wall"
  physical anchor (Ax = ground reach, Ay = wall height) is what made the
  cos/sin-to-component mapping click.
- Correctly reasoned through tip-to-tail addition geometrically: placing B's
  tail at A's tip (Ax, Ay) and following B out lands at (Rx, Ry) — independently
  connected the graphical and component methods.

### Files created/updated
- `wiki/drills/vector-addition-drill.md` — added Part E with today's problem and
  full worked solution.
- **New:** `wiki/drills/stage-3-textbook-problems.md` — real Serway Ch 3
  end-of-chapter problems (1–32, transcribed from raw PDF via pdftotext, with
  OCR-uncertain figure-dependent ones flagged), organized by section, with a
  blank Reflection? column for Chris to flag live in session.
- `wiki/stages/stage-3-vectors.md` — linked the new textbook problem set under
  Drills.

### Concepts/equations/problem types added
- None new — this closes out the addition skill's harder case and adds a
  retrieval resource; no new concept.

### Parked material
- Problems 15, 16, 20, 22, 23, 28–30, 32 (figure-heavy) not transcribed — pull
  the specific figure from the raw PDF if one is wanted later.

### Next action for Chris
- Full no-notes pass over all four Stage 3 skills (coordinate conversion,
  scalar/vector ID, decomposition, reconstruction, addition) before checking the
  mastery checklist in `wiki/stages/stage-3-vectors.md`. Then start working the
  new textbook problem set, flagging reflection-worthy ones as they come up.

## 2026-07-18 — Full Physics Math Crash Course

### Objective
- Build one complete, stage-mapped review of all math used by the Physics WIKI.

### Sources touched
- Read-only screen of `D:\SCHOOL\Chatt Tech Files\math` (algebra, geometry,
  trig/unit-circle, derivative, integral, calculus-application, Calc II, and
  statistics materials).
- Existing Physics WIKI equation, calculus, units, appendix, learning-path, and
  Stage 4 pages.

### Files created/updated
- Created `wiki/physics-math-crash-course.md`.
- Updated `wiki/index.md`, `wiki/math-readiness-path.md`, and `wiki/source-map.md`.

### Concepts/equations/problem types added
- Unified scientific notation, units, algebra, proportions, graphs, trig,
  vectors, dot/cross products, systems, quadratics, derivatives, integrals,
  rotation, fluids, oscillations, waves, relativity, uncertainty, and lab graphing
  into one physics-first guide with transfer checks.
- Added a Stage 4 projectile bridge and corrected the readiness path from stale
  Stage 3 wording to the active Stage 4 frontier.

### Parked material
- Most Calc II convergence/integration machinery, Laplace and hyperbolic
  functions, complex-number work, and statistics beyond lab uncertainty/graphs.

### Next action for Chris
- Work the crash course's Stage 4 cold projectile transfer rep on paper; review
  only the first module exposed as non-automatic, then retry with changed numbers.

## 2026-07-21 — Cross-Section Syllabus Reconciliation

### Objective
- Reconcile the two newly obtained Fall 2026 PHYS 2211 neighbor syllabi (Section
  51 and Section 55, neither is Chris's registered Section 54) against the
  existing 18-stage path; strengthen and tighten the vault.

### Sources touched
- `raw/syllabus/PHYS 2211 51 (83719) Fall 2026 Syllabus - Reference Only.md`
- `raw/syllabus/PHYS 2211 55 (83723) Fall 2026 Syllabus - Reference Only.md`
- Existing `source-map.md`, `syllabus-coverage-ledger.md`, `learning-path.md`,
  `current-position.md`.

### Files created/updated
- `wiki/source-map.md` — registered both new syllabi in the Sources table;
  identified `syllabus.pdf` as very likely an early truncated capture of the
  same Section 55 syllabus; updated the "later calendar is absent" data-quality
  row to partially resolved.
- `wiki/syllabus-coverage-ledger.md` — added a "Cross-Section Verification,
  2026-07-21" section: confirms Stage 1-12/15 order, flags that neither
  neighbor's calendar schedules Ch 14 or Ch 38 (kept in path per Chris's
  2026-06-25 confirmation), records the grading-structure mismatch, and adds
  soft pacing anchors (Exam 1 ~Sep 25, Exam 2 ~Oct 30, Exam 3 ~Nov 20 per
  Section 55).
- `wiki/learning-path.md` — added the cross-check summary under Path Status;
  flagged Stages 13/14/16/17/18 with the neighbor-calendar gap note; added soft
  pacing-anchor lines to the Stage 5, 10, and 12 detail sections.
- `wiki/current-position.md` — updated First 7-Day Priority item 3 with the new
  pacing evidence.
- `00-BRAIN\SYSTEM_FLAGS.md` flag #57 — logged that the PHYS neighbor syllabi
  are now cross-referenced into the wiki; flag stays OPEN pending real Section
  54 confirmation Aug 24.

### Concepts/equations/problem types added
- None — this was a source-reconciliation and path-integrity pass, not content
  generation.

### Parked material
- None newly parked. Existing Stage 13/14/16/17/18 scope stands unchanged;
  the neighbor-calendar gap is tracked as an open verification item, not a
  parking decision.

### Next action for Chris
- No change to the active Stage 4 study rep. When Section 54 populates in D2L
  (Aug 24+), re-check it against the pacing anchors and the Ch 13/14/16/17/38
  scheduling question logged in `syllabus-coverage-ledger.md`.

## 2026-07-21 — Stage 4-9 Tightening Pass

### Objective
- Chris directed a "chunk format intake" tightening pass on Stages 4-9 tonight,
  following the Source Intake Protocol in `authoring-standards.md`: resolve the
  two known expansion gaps `learning-path.md` had already flagged for this
  range, then check for structural completeness.

### Sources touched
- `raw/textbook/Physics book-0101-0200.pdf` (Ch 6, accelerated frames Sec 6.3;
  Ch 9 section list) — used from prior source-map registration, not re-parsed.
- Existing Stage 4-9 packets, their linked concept/equation/problem-type/
  common-errors/flashcards pages, and `parking-lot.md`.

### Files created/updated
- **New:** `wiki/concepts/accelerated-reference-frames.md` — full concept page
  for noninertial frames and fictitious force (Serway Sec 6.3), the exact gap
  `learning-path.md` had flagged since 2026-07-15.
- **New:** `wiki/glossary/noninertial-reference-frame.md`,
  `wiki/glossary/fictitious-force.md`.
- `wiki/stages/stage-6-circular-motion.md` — added the new concept to Core
  Concepts/Vocabulary/Diagrams, added 3 mastery-checklist items, strengthened
  Do Not Move On Until, fixed frontmatter (added timeline/stage/tags).
- `wiki/common-errors/stage-6-circular-motion.md` — added 2 new error entries
  (fictitious force in the wrong frame; true vs. apparent weight).
- `wiki/flashcards/stage-6-circular-motion.md` — added 3 new cards (13-15).
- `wiki/stages/stage-9-linear-momentum.md` — added the missing "Do Not Move On
  Until" and "Parked for Later" sections (previously absent), added a mastery
  item on p_total = M·v_cm, fixed frontmatter, resolved the Sec 9.7-9.9
  include/park decision using today's neighbor-syllabus evidence.
- `wiki/concepts/center-of-mass.md` — added the explicit p_total = M_total·v_cm
  link between center-of-mass velocity and total system momentum.
- `wiki/stages/stage-5-laws-of-motion.md`, `wiki/stages/stage-8-conservation-of-energy.md`
  — frontmatter-only fix (added timeline/stage/tags) for consistency with
  Stages 4, 6, 7, 9.
- `wiki/parking-lot.md` — marked the Stage 6 §6.3 row resolved; updated the
  Stage 9 §9.7-9.9 row with the park decision and evidence; updated the Stage
  15 §15.6-15.7 row with a lean-toward-include signal from Section 55's real
  calendar (not built tonight — out of the 4-9 scope).
- `wiki/learning-path.md` — flipped Stage 6 and Stage 9 control-table rows and
  detail-section packet-status lines from "needs expansion / needs decision"
  to "ready."
- `wiki/index.md` — updated concepts (58→59) and glossary (46→48) counts and
  the live-counts date.

### Concepts/equations/problem types added
- Concept: motion in accelerated reference frames (fictitious force, apparent
  weight in elevators, centrifugal force as a fictitious force).
- Verified (no gap found, no duplicate created): Stage 5 friction glossary
  already merges static/kinetic; Stage 8 isolated/nonisolated already merged;
  Stage 9 inelastic/perfectly-inelastic already merged; Stage 7/8 power/watt
  already merged. Checked before assuming these needed new stub pages.

### Parked material
- Serway Ch 9 §9.7-9.9 (many-particle systems, deformable systems, rocket
  propulsion) — see `parking-lot.md` for the full decision and unlock
  condition.

### Next action for Chris
- Stages 4-9 are now internally consistent and structurally complete for
  activation. Continue the Stage 4 study rep as planned; when Stage 6 and 9
  come up, both packets are ready with no outstanding expansion debt. Stage 15
  now carries a lean-toward-include signal for damped/forced oscillations —
  revisit when that stage's packet is next expanded.

## 2026-07-21 — Calculus-Link Build-Out for Stages 4-9

### Objective
- Chris asked to pull real content into the calculus material specifically:
  find the actual math connection for each Stage 4-9 topic, and post it with
  practice problems plus a real-world/engineering use-case explanation — not
  just the physics-textbook abstraction.

### Sources touched
- Existing `calculus-links/` pages, `calculus-map.md`, and the Stage 4/6/8/9
  packets' inline "Calculus Connections" sections (previously text-only, not
  linked to a dedicated page for three of the four).

### Files created/updated
- **New:** `wiki/calculus-links/tangential-radial-acceleration-derivative.md`
  — a_t = dv/dt on a curved path (Stage 4 §4.5 / Stage 6), previously only a
  brief inline mention with no dedicated page. 3 practice problems (including
  differentiating a nonlinear v(t)) + engineering use case (highway/conveyor
  curve design, ride/vehicle acceleration limits).
- **New:** `wiki/calculus-links/power-derivative.md` — P = dE/dt and
  ΔE = ∫P dt (Stage 8), previously inline-only. 3 practice problems + use
  case (motor/conveyor sizing, utility demand-charge billing).
- `wiki/calculus-links/kinematics-derivatives.md` (Stage 2, feeds Stage 4) —
  added 3 practice problems + use case (motion-control velocity profiles:
  robotic arms, CNC, elevators).
- `wiki/calculus-links/2d-kinematics-components.md` (Stage 4) — added 3
  practice problems + use case (material-handling conveyor transfer points,
  packaging drop-test trajectories).
- `wiki/calculus-links/stage-7-work-integral.md` (Stage 7) — added 3 practice
  problems + use case (springs/shock absorbers/packaging cushioning sizing).
- `wiki/calculus-links/impulse-integral.md` (Stage 9) — added 3 practice
  problems + use case (crash safety engineering, crumple zones/airbags —
  Δt vs. Δp tradeoff explained numerically).
- `wiki/stages/stage-4-motion-in-two-dimensions.md`, `stage-6-circular-motion.md`,
  `stage-8-conservation-of-energy.md`, `stage-9-linear-momentum.md` — their
  Calculus Connections sections now link out to the full derivation/practice/
  use-case page instead of only describing it inline.
- `wiki/concepts/tangential-and-radial-acceleration.md` — Calculus Connection
  section now links to the new full page.
- `wiki/calculus-map.md` — corrected Stage 6 ("none new" was wrong — a_t
  reused from Stage 4) and Stage 8 ("none new" was wrong — power is a real
  new derivative) roadmap rows; added a table indexing all 9 calculus-link
  pages now built, each tagged with what it covers.
- `wiki/index.md` — calculus-links count 7→9, noted the practice+use-case
  standard now applied to all of them.

### Concepts/equations/problem types added
- No new physics concepts — this was a calculus-depth and cross-linking pass
  on existing Stage 4-9 material, adding worked practice and applied context
  rather than new physical ideas.

### Parked material
- None.

### Next action for Chris
- All Stage 4-9 calculus connections now have a full page with practice
  problems and an engineering use case, not just a one-line mention. Work
  the practice problems cold (cover the Check Yourself section) as part of
  each stage's rep, not just the physics-only drills — the goal is fluency
  differentiating/integrating inside a physical setup, not just algebra with
  given numbers. Stages 10+ calculus-link pages (rotation, angular momentum,
  SHM) already exist from the July build but have not yet had this same
  practice+use-case pass; revisit when those stages activate.

## 2026-07-21 — Pacing Trigger Map Built

### Objective
- Chris asked for a trigger map: a concrete reference for when to read what
  to keep pace for the semester, not just the stage-order path.

### Sources touched
- `02-LIBRARY\00-SCHOOL\View Registration Information.md` — the real,
  confirmed PHYS 2211 Section 54 meeting pattern (MWF 9:10-10:05 AM lecture,
  Friday 11:30 AM-12:25 PM breakout, Aug 24-Dec 14 2026, Marietta Campus) —
  had not previously been pulled into the PHYSICS wiki.
- The two neighbor syllabi and the 2026-07-21 cross-section verification
  already logged in `syllabus-coverage-ledger.md`.

### Files created/updated
- **New:** `wiki/pacing-trigger-map.md` — two trigger types: date triggers
  (a real-Monday-anchored week-by-week table, Aug 24-Dec 14, combining the
  confirmed MWF meeting pattern with the estimated topic/chapter/exam pacing
  from the neighbor syllabi) and state triggers (weekend read-ahead rule,
  exam-approach pre-sweep rule, mastery-moves-the-stage rule overriding the
  calendar, a 7-day stall check, and a hard trigger to re-run the syllabus
  cross-check the day Section 54's real D2L content appears).
- `wiki/index.md` — linked the new page under Core Maps.
- `wiki/current-position.md` — pointed to the new page from the top of the
  file.

### Concepts/equations/problem types added
- None — scheduling/pacing infrastructure, not physics content.

### Parked material
- Fall Break's exact date — neither neighbor syllabus states it clearly;
  left unplaced in the table with an explicit note to confirm via D2L/the
  official academic calendar.

### Next action for Chris
- Use `pacing-trigger-map.md`'s Sunday read-ahead rule starting immediately
  (it doesn't depend on Section 54's dates being final). The moment D2L
  populates real Section 54 content — expected around Aug 24 — re-run the
  cross-check (Trigger Rule 5) and replace the estimated column with real
  dates in the same pass.

## 2026-07-23 — Dead syllabus.pdf path found and fixed (Claude Code)

### Objective
- Chris asked for a second set of eyes on `CLAUDE.md` after the same class of
  issue was found and fixed in the Python wiki: incorrect/stale paths to the
  course syllabi governing this hub.

### Work completed
- Found that `source-map.md`, `syllabus-coverage-ledger.md`,
  `current-position.md`, and `learning-path.md` all cited `raw/syllabus/
  syllabus.pdf` as a live, currently-readable file — course outcomes, grading,
  AI policy, and the full 19-page data-quality gate were all written as if the
  file still lived there. It does not: `raw/syllabus/` currently holds only
  the two real Fall 2026 section syllabi (`PHYS 2211 51` and `PHYS 2211 55`)
  plus `README.md`. The original `syllabus.pdf` was moved on 2026-07-21 to
  `99-ARCHIVE\02-LIBRARY\00-SCHOOL\SYLLABI_REPLACED_2026-07-21\02-Physics I\
  syllabus.pdf` — confirmed by direct filesystem search, not inferred.
- This is a harder break than the Python case (which cited an existing but
  non-canonical duplicate): here the exact cited file is genuinely gone from
  the path four separate pages pointed to.
- `syllabus-coverage-ledger.md`'s own July 21 Cross-Section Verification
  section had already reasoned that `syllabus.pdf` was "very likely an early,
  truncated capture" of the Section 55 syllabus and should be "treated as
  superseded" — but nothing had gone back to update the citing pages once
  that was known, and none of them had discovered the file was actually
  archived, not just superseded-in-place.

### Pages created/updated
- `source-map.md` — the `syllabus.pdf` Sources-table row now states it is
  superseded/archived with its current path; the Syllabus Data-Quality Gate
  section is relabeled historical, sourced from the archived PDF, not a live
  file.
- `syllabus-coverage-ledger.md` — added a Source note dating the archive move
  and pointing to the current file location; the "original spine source" line
  in Cross-Section Verification updated to past tense with the same pointer.
- `current-position.md`, `learning-path.md` — both "Built from `raw/syllabus/
  syllabus.pdf`" lines corrected to note the file is superseded/archived and
  point to the two real section syllabi as the live reference.
- `parking-lot.md` — the two rows sourced to `syllabus.pdf` (remaining
  calendar, operational corrections) updated with the archive pointer; the
  calendar row also notes the 2026-07-21 partial resolution already recorded
  in `source-map.md` (Section 55's real Ch 6-15 calendar) that these two rows
  hadn't been updated to reflect.

### Concepts/equations/problem types added
None — citation/path correction only.

### Progress evidence
n/a — governance session. No physics content changed; all data-quality
findings and course facts extracted from `syllabus.pdf` while it was live
remain accurate and are preserved, just correctly labeled as historical.

### Parked material
None new.

### Next action for Chris
None urgent — this was a citation-path repair, not a content change. The
existing next actions (Section 54 D2L confirmation, Aug 24+) are unchanged.

## 2026-07-24 — Machine-interface architecture conversion (Codex)

### Objective
- Convert the PHYSICS hub to the governed loader/contract/human-router pattern
  without changing learner progress, physics content, or raw evidence.

### Sources touched
- Existing PHYSICS operating files, current position, learning path, index,
  source map, and Fall 2026 semester goal.

### Files created/updated
- New `OPERATIONS.md`: canonical machine contract with authority, durable-spine
  and course-overlay lifespans, INGEST/QUERY/LINT operations, teaching contract,
  mastery proof, academic-integrity boundary, raw boundary, and close rule.
- `CLAUDE.md`: reduced to a thin deterministic AI loader.
- New `README.md`: human entry router.
- `HOW_TO_USE.md`: rewritten as the human study workflow; retired
  `PRE-SEMESTER_PREP_PLAN.md` pointer replaced by `fall_2026_semester.md`.
- `authoring-standards.md`, `source-map.md`, `calculus-map.md`, and
  `syllabus-coverage-ledger.md`: live authority pointers moved from
  `CLAUDE.md` to `OPERATIONS.md`.
- Added a Git-object archive manifest for the exact pre-conversion
  `CLAUDE.md` and `HOW_TO_USE.md` blobs. Historical log references remain
  historical.

### Concepts/equations/problem types added
- None. Stage 4 remains active; no learner proof or stage advancement claimed.

### Parked material
- Existing frontmatter normalization debt remains a separate mechanical pass.

### Next action for Chris
- Begin the Stage 4 projectile-motion rep in `wiki/current-position.md`, while
  using the Stage 3 textbook problems as the recorded durability check.
