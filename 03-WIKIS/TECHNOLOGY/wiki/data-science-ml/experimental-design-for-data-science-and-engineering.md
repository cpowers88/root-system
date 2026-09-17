---
domain: technology
type: reference
timeline: reference
status: wiki-only
tags: [subject/experimental-design, subject/data-science, subject/statistics]
source_role: primary
stack: [r]
---

# Experimental Design for Data Science and Engineering — Source Summary and Navigation Hub

**Summary**: Full-source summary for *Experimental Design for Data Science and
Engineering* (V. Roshan Joseph, CRC Press, first edition 2026, 246 pp.,
chapters released CC BY-NC-ND 4.0). A modern, Gaussian-process-first treatment
of design of experiments (DOE) that runs from classical physical experiments
through computer experiments to direct data-science applications (subsampling,
train/test splitting, factor selection). Selectively ingested 2026-07-17 into
two applied pages; the heavy mathematical machinery is retained in raw/ for
triggered lookup.

## Why this source matters here

- **ISYE bridge**: DOE is core Industrial & Systems Engineering curriculum;
  this book connects the classical material (fractional factorials, aliasing,
  resolution) Chris will meet at KSU to the modern computer-experiment and
  ML-era methods that replaced much of it in practice.
- **The author is the method-builder**: Joseph (Georgia Tech ISyE) is the
  originator or co-author of several methods the book teaches — MaxPro
  designs, SPlit, twinning, supercompress, FIRST, TwinGP — each with a
  maintained R package. The book doubles as documentation for that toolchain.
- **Direct data-science payoff now**: Part IV needs no experiment at all —
  it applies design thinking to datasets you already have (better train/test
  splits, principled subsampling, model-free variable selection). That is
  immediately usable against the scanner SQLite data and the tracker.

## The book's central argument

Optimal experimental design depends on the objective (approximate the surface,
optimize it, propagate uncertainty, screen factors) **and** on the unknown
response surface — so classical designs built on an assumed linear-regression
model quietly bet everything on that model being right. Linear regression puts
its highest confidence exactly where it has no data (uncertainty smallest in
the middle, largest at the extremes); a Gaussian process does the opposite —
zero uncertainty where you observed, maximum where you haven't. Building the
design theory on GP uncertainty produces designs that are robust to model
misspecification, and space-filling designs emerge as the practical,
parameter-free limiting case. Sequential (active-learning) designs then adapt
to the specific function as data arrives.

## Coverage map (what was read vs. parked)

| Part / chapter | Status | Where it lives |
|---|---|---|
| Ch 1 Experiments (framing, objectives, role of uncertainty) | Compiled | this page + [[space-filling-screening-and-sequential-designs]] |
| Ch 2 Modeling (interpolation, kriging, GP regression math) | Lookup | raw/ — prerequisite math, retrieve behind an active GP need |
| Ch 3 Model-based designs (IMSE/MMSE/entropy) | Compiled (concept level) | [[space-filling-screening-and-sequential-designs]] |
| Ch 4 Space-filling (clustering, minimax, maximin, LHD, MaxPro) | Compiled (4.1–4.5 core) | [[space-filling-screening-and-sequential-designs]] |
| Ch 4.6 Minimum energy designs, Ch 5 Representative points | Lookup | raw/ — Bayesian computation and QMC depth beyond current need |
| Ch 6 Screening (Sobol indices, Morris, MOFAT) | Compiled | [[space-filling-screening-and-sequential-designs]] |
| Ch 7 Sequential designs (ALC/ALM, Bayesian optimization/EI, inverse design) | Compiled | [[space-filling-screening-and-sequential-designs]] |
| Ch 8 Fractional factorials (aliasing, resolution, minimum aberration, Bayesian-inspired) | Compiled (8.1–8.2 essentials) | [[space-filling-screening-and-sequential-designs]] |
| Ch 8.3–8.4 Multi-level and mixture designs | Lookup | raw/ — retrieve when a real mixture/multi-level experiment exists |
| Ch 9 Model calibration (computer + physical data) | Lookup | raw/ — advanced; behind a real calibration problem |
| Ch 10 Data subsampling (support points, SPlit, twinning, supercompress) | Compiled | [[data-splitting-twinning-and-subsampling]] |
| Ch 11 Data analysis (FIRST factor selection, TwinGP) | Compiled | [[data-splitting-twinning-and-subsampling]] |

## Physical anchor for the whole subject

An experimental design is a **drilling plan**: you own a piece of land (the
input space), holes are expensive, and you must decide where to drill before
knowing what's underground. Classical DOE drills on a rigid grid an engineer
drew in advance assuming flat geology (a linear model). This book's approach
drills a well-spread first pass (space-filling), maps the uncertainty after
each hole (GP), and sends the rig where the map is blurriest or the ore looks
richest (sequential design / expected improvement).

## Verification notes

- First edition 2026; the R ecosystem it documents (`SFDesign`, `rkriging`,
  `SPlit`, `twinning`, `supercompress`, `first`, `twingp`, plus a Python
  `pyfirst`) is 2021–2025 vintage and volatile — verify package names, current
  APIs, and maintenance status before recommending or building on them.
- Text was extracted programmatically (pypdf); figures and some equation
  typography were not rendered. Equation-level claims should be re-checked
  against the PDF page before any derivation-dependent use.

## Related pages

- [[space-filling-screening-and-sequential-designs]] — design families and the decision map
- [[data-splitting-twinning-and-subsampling]] — Part IV applied to everyday ML work
- [[ab-testing-hypothesis-tests-and-p-values]] — the classical two-option experiment this book generalizes
- [[holdout-cross-validation-and-learning-curves]] — the validation problem SPlit/twinning improve on
- [[business-experimentation-and-project-unicorn]] — why businesses experiment at all
