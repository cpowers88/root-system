---
type: method
timeline: reference
status: active
tags: [physics, method, evidence]
created: 2026-07-26
---

# Handwritten Physics on the iPad — Method

Adopted 2026-07-26. All physics work is handwritten because the work itself is
spatial: a free-body diagram, a vector decomposition, an axis choice, and a sign
convention cannot be typed. Typing physics turns a spatial problem into
transcription and deletes the step being trained.

This page is the method. It is short on purpose — the tool gets learned by doing
physics on it, not by practicing the tool.

---

## 1. The page skeleton — the actual lesson

Every problem page uses the same spatial layout, because physics problem-solving
has a fixed order and the page should make that order visible.

```
┌──────────────────────────┬─────────────────────┐
│  SKETCH                  │  KNOWNS             │
│  the physical situation  │  v₀ = 20 m/s        │
│  + axes drawn ON it      │  θ  = 35°           │
│  + sign convention       │  h  = 12 m          │
│                          │  ─────────          │
│      ↗ v₀                │  UNKNOWN            │
│     /                    │  range = ?          │
│  ──/────────→ +x         │                     │
│   │ +y up                │                     │
└──────────────────────────┴─────────────────────┘
│  MODEL — which equations, and why these         │
│  x: constant velocity → x = v₀ₓt                │
│  y: constant accel   → y = v₀ᵧt − ½gt²          │
├─────────────────────────────────────────────────┤
│  SYMBOLIC — solve for the unknown in symbols    │
│  BEFORE any number goes on the page             │
├─────────────────────────────────────────────────┤
│  NUMBERS — substitute last, units on every line │
├─────────────────────────────────────────────────┤
│  CHECK — is this physically reasonable? why?    │
└─────────────────────────────────────────────────┘
```

**Why this exact layout.** It maps one-to-one onto the syllabus-wide mastery
standard — physical interpretation, a pictorial representation, a symbolic setup,
a numerical solution with units, and a reasonableness check — and onto the eight
evidence components the Stage 4 gate asks for. When a problem is missed, the
layout shows *which box* failed. "I got it wrong" is an aggregate score and
cannot be acted on; "my sign convention was inconsistent between the sketch and
the y-equation" is a retest item.

**The one rule people skip:** solve symbolically before substituting numbers.
Numbers early hide algebra errors and make the result impossible to sanity-check.

---

## 2. Five iPad techniques that matter for physics

Ignore everything else the app can do until these are automatic.

1. **Duplicate a template page.** Draw axes, a horizon line, and the box layout
   once. Duplicate it for every new problem. Never redraw a coordinate system —
   that is wasted motion, not practice.
2. **Lasso, select, move.** Physics work grows sideways and runs out of room.
   Being able to grab a diagram and slide it is the single biggest advantage the
   iPad has over paper. Learn this one first.
3. **Shape snap.** Hold the pen at the end of a stroke and the line straightens
   into a clean vector or axis. Essential — crooked axes make sign errors.
4. **Zoom / write box.** Write at a comfortable hand size and it lands small and
   neat on the page. Do not shrink your handwriting; shrink the page.
5. **Undo is free.** This matters more than it sounds. A cold attempt is only
   honest if attempting is cheap, and infinite undo makes it cheap.

---

## 3. Color as convention, not decoration

Four colors, fixed meanings, never decorative:

| Color | Means |
|---|---|
| **Black** | given information, the problem as stated |
| **Blue** | your work |
| **Red** | the final answer, with units |
| **Green** | the correction, added *after* checking |

Green is the one that earns its place. Correcting in a distinct color means one
photo of the page shows **both the first attempt and the fix** — which is exactly
the evidence the teaching loop needs. Do not erase a wrong first attempt. The
wrong attempt is the data.

---

## 4. Where the file goes

Export the page as PDF (or PNG for a single diagram) into:

```
03-WIKIS\PHYSICS\wiki\handwritten\
```

Name it so it sorts by date and points at what it proves:

```
2026-07-27_stage-04_launch-diagram.pdf
2026-07-27_stage-04_projectile-drill-p1-p2.pdf
2026-07-31_stage-04_cold-gate.pdf
```

That is the whole pipeline. No tagging system, no index to maintain — the folder
sorts chronologically and the filename carries the stage and the drill.

**Added 2026-07-30:** a Markdown problem page may sit alongside a handwritten
artifact as the shared derivation/reasoning surface (`OPERATIONS.md` §
Calculus-Reconstruction Lens) — it links to the exported PNG/PDF, it never
replaces it. The sketch, axes, and first attempt stay handwritten; the
calculus derivation and explanation can happen in Markdown where symbolic
back-and-forth is faster than re-drawing.

---

## 5. What not to do

- **Do not build a note-taking system before taking notes.** Run two weeks, keep
  whatever you actually did twice, then write it down. Optimizing the setup first
  is the same trap as generating wiki pages five stages ahead of need.
- **Do not tidy the page afterward.** A clean rewrite is transcription and proves
  nothing. The messy first attempt with a green correction is worth more than a
  neat final copy.
- **Do not type it up later.** Zero learning value, real time cost.
- **Do not chase the perfect app.** Whatever is already installed is fine. All
  five techniques above exist in every major option.

---

## First rep — Monday, July 27, 11:00

Low stakes on purpose: **one launch diagram.** Sketch the situation from Ch 4
§4.1–4.2, draw the axes on it, mark the sign convention, and label v₀ₓ and v₀ᵧ.
That is the whole artifact. Photograph or export it.

Building the full page template can wait until the 1:00 block, when there is an
actual problem to solve on it.

---
*Related: [[stages/stage-4-motion-in-two-dimensions]] mastery checklist;
[[common-errors/stage-4-motion-in-two-dimensions]] for the miss classifications
this layout is designed to expose.*
