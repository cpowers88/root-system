---
domain: technology
type: reference
timeline: reference
status: wiki-only
tags: [domain/technology, source-role/primary, subject/instrumentation, subject/calibration, subject/data-quality]
---

# Sensor Linearization, Calibration, and Compensation

## Four Corrections Solve Different Problems

| Operation | Problem addressed | Evidence required |
|---|---|---|
| Linearization | Nonlinear relationship between input and output | Characterization data over the operating range |
| Calibration | Relationship between indication and a traceable reference, including uncertainty | Reference, conditions, date, procedure, and result |
| Compensation | Predictable influence from temperature, interference, lead wires, or another variable | Measured disturbing variable and validated correction relationship |
| Validation | Fault, inconsistency, or operation outside the trusted domain | Health checks, redundancy/model residuals, and explicit quality state |

These are not interchangeable. A well-linearized signal can remain biased; a calibrated sensor can drift; compensation can hide failure if the compensating input is bad.

## Choose the Simplest Correction That Meets the Requirement

The source spans analog circuits, nonlinear conversion, interpolation, piecewise fits, lookup tables, polynomial computation, adaptive filters, and neural networks. A durable selection order is:

1. narrow the operating range if that makes the raw response sufficiently linear;
2. remove or reduce interference physically;
3. use simple analog or digital correction where behavior is stable;
4. use piecewise or lookup-table correction when empirical characterization is reliable;
5. use a fitted model only when its added complexity earns measurable error reduction;
6. use adaptive or learned correction only with validation data, drift monitoring, versioning, and fallback.

More sophisticated correction is not automatically more accurate. It can trade transparent, bounded error for opaque model error.

## Calibration Is a Lifecycle

Calibration does not make uncertainty disappear. It estimates the relationship to a reference under stated conditions. The source identifies environmental change, limited resolution, poor repeatability, defects, contamination, and aging as contributors to uncertainty or drift.

A usable record includes:

```text
sensor and channel identity
reference standard and traceability
as-found result
adjustment/correction applied
as-left result
environmental conditions
uncertainty and acceptance limit
date, operator/procedure, next trigger
```

Trigger recalibration by risk and evidence—elapsed time, drift trend, shock/repair, environmental excursion, failed validation—not merely by habit.

## Source Boundary

Compiled from Chapters 3-5 of [[intelligent-instrumentation|Intelligent Instrumentation]]. Circuit designs and equations are retained in the PDF for a triggered engineering lookup.

