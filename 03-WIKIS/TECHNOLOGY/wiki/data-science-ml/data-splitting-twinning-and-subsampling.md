---
domain: technology
type: concept
timeline: reference
status: wiki-only
tags: [domain/technology, source-role/primary, subject/experimental-design, subject/data-science, subject/machine-learning, stack/r, stack/python]
---

# Data Splitting, Twinning, and Subsampling — DOE Applied to Data You Already Have

**Summary**: Part IV of *Experimental Design for Data Science and Engineering*
(Joseph, 2026) turns experimental-design thinking onto ordinary ML workflow
steps — train/test splitting, subsampling big data, compressing datasets for
expensive models, and selecting variables — replacing "sample rows at random"
with principled, distribution-matching methods. This is the most directly
applicable chapter set for everyday data work: no experiment required.

## The core idea

Subsampling **is** experimental design in a discrete space: instead of asking
"where should I collect data?" you ask "which of the rows I already have carry
the information?" A random subsample is like a random design — sometimes fine,
sometimes terrible, always high-variance. The fix is the same as in design:
choose the subset that **matches the distribution** of the full data, measured
by **energy distance** between the empirical distributions.

## Support-points subsampling (Ch 10.1)

- Find n *support points* minimizing energy distance to the dataset
  (continuous optimization), then snap each to its nearest unclaimed data row
  (sequential nearest-neighbor, kd-tree). Model-free: unlike a D-optimal
  subsample (optimal only for the linear model that defined it), a
  distribution-matched subsample serves whatever model you fit next.
- Wind-turbine example: 39,195 rows → 392-point subsample (1%) → GP fit in
  under 3 seconds total, versus an estimated **3.5 days** to fit the full set
  (GP cost scales O(N³)).
- Same machinery does scenario reduction in stochastic optimization (power
  grids), and uncertainty propagation.
- Caveat observed in the example: a stationary GP "mean-reverts" in
  data-sparse regions — subsampling can't fix a model-class limitation.

## Data splitting done right (Ch 10.2)

Random 80:20 splits make test results noisy enough to misrank models. The
**SPlit** method selects a testing set that is distribution-matched to the
whole dataset (support points on the joint (X, y) distribution) — older
alternatives (Kennard-Stone/CADEX, DUPLEX) push test points to the boundary
and distort the test distribution. Assumption to keep visible: no covariate
shift between the dataset and deployment.

## Twinning (Ch 10.3) — the fast general tool

Minimizing energy distance between the subset S and its complement makes the
two sets statistical **twins** — provably identical optimum to matching S
against the full data, but computable greedily with a kd-tree in
O(pN log N): the 39,195-row split that took SPlit ~2s took **twinning
~0.02s**. Because it's cheap, twinning generalizes to *multiplets* —
partitioning data into k statistically-equivalent folds for cross-validation
or divide-and-conquer. R: `twinning`; also `SPlit`.

## Supervised compression (Ch 10.4)

When the subsample exists to feed a predictive model, use the response too:
**supercompress** (Joseph & Mak 2021) greedily splits the input-space cluster
with the largest response sum-of-squares, concentrating points where the
response surface changes fast and spending few where it's flat (36% nearest-
neighbor RMSE improvement over k-means selection in the book's example).
Slower than twinning — use when prediction accuracy, not speed, drives the
compression. R: `supercompress`.

## FIRST — model-free factor selection from raw data (Ch 11.1)

Total Sobol indices normally need a computer model you can query. **FIRST**
(Huang & Joseph 2025) estimates them straight from a dataset using
nearest-neighbor approximations (double Monte Carlo over kd-tree neighbors),
with a noise-variance correction — no model fitting, no density estimation.

- **Dependent-inputs caveat** (important): with correlated inputs the
  functional-ANOVA decomposition behind Sobol indices breaks; as correlation
  → 1 the indices of two useful-but-correlated variables both → 0. The rescue:
  T_i = 0 **iff** y ⊥ x_i given the rest — so the index is still a valid
  *selection* signal even when its magnitude stops meaning "importance."
  Rank by iterative backward removal instead of raw index size.
- Concrete-strength case study: FIRST picked ~4 of 8 predictors; both random
  forest and GP predicted **better with the selected subset than with all
  eight** — variable selection as accuracy tool, not just parsimony.
  R: `first`; Python: `pyfirst`.

## TwinGP (Ch 11.2) — GP on big data

Fit a global GP on a twinning subsample (n_g ≈ √N) plus a local GP on the ~25
nearest neighbors of each prediction point, blended with a compactly-supported
local kernel: O(N^1.5) total, 0.2s on the wind dataset, and better accuracy
than the global-subsample fit. R: `twingp`.

## Where this bites in current work

- **Scanner/tracker SQL evidence**: when a model or dashboard rep needs a
  train/test split or a manageable sample of a big query result, twinning-
  style distribution-matched selection is the defensible default; random
  splits are the thing it replaces.
- **Revenue Lab bounded tests**: SPlit logic = "make the comparison sets
  statistically equivalent before comparing" — same discipline as A/B design
  ([[ab-testing-hypothesis-tests-and-p-values]]).
- **Client data-reconciliation work** (reconciliation-engine lineage): FIRST
  gives a model-free first answer to "which fields actually drive this
  outcome" before anyone builds a model.

## Verification notes

Package facts (names, APIs, speeds) are 2021–2025 vintage from a 2026 first
edition — verify current state before use. Timing claims are the author's
single-machine benchmarks; treat as orders of magnitude, not guarantees.

Source: [[experimental-design-for-data-science-and-engineering]]. Related:
[[space-filling-screening-and-sequential-designs]],
[[holdout-cross-validation-and-learning-curves]],
[[estimates-of-location-and-variability]].
