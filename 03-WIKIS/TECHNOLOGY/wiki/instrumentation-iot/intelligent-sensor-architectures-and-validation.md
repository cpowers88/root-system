---
domain: technology
type: reference
timeline: reference
status: wiki-only
tags: [subject/instrumentation, subject/sensors, subject/validation]
source_role: primary
---

# Intelligent Sensor Architectures and Validation

## Intelligence Is a Stack of Capabilities

The book's terminology is more useful as a capability ladder than as rigid product labels:

| Sensor form | Added capability | Important boundary |
|---|---|---|
| Classical sensor | Converts a physical quantity to a usable signal | Raw response still needs conditioning and interpretation |
| Smart sensor | Adds onboard storage or signal processing | Processing alone does not imply judgment |
| Cogent sensor | Converts processed data into application-specific classification, inference, or decision information | Decision logic and failure modes must be exposed |
| Soft/virtual sensor | Estimates a temporarily unavailable measurement from a process model and secondary variables | Must be reconciled when the physical sensor returns |
| Self-adaptive sensor | Changes its procedure or parameters as signal/environment conditions change | Adaptation needs bounds and observable state |
| Self-validating sensor | Reports confidence/qualification and detects inconsistent or faulty behavior | A value without validity state is incomplete |
| Indirect sensor | Permanently estimates a hard-to-measure variable from other measurable variables | It is a model-derived estimate, not a direct observation |

This ladder prevents a common category error: putting a processor beside a transducer and calling the result intelligent without specifying what higher-level function it actually performs.

## Soft and Indirect Sensing Need Different Contracts

A soft sensor substitutes temporarily when a physical measurement is unavailable because of failure, maintenance, cost, time sharing, or inadequate sampling. It learns or updates its process relationship while the direct measurement is available.

Indirect sensing is the standing design when a direct sensor does not exist or is impractical. It estimates the target from correlated measurable variables using parameter estimation, spectral analysis, fuzzy logic, neural networks, or another model.

Both must expose:

- whether the value is observed or estimated;
- model/version and input provenance;
- freshness and confidence;
- the domain over which the estimate was validated;
- drift or inconsistency checks;
- fallback behavior when required inputs fail.

## Validation Must Travel With the Value

The source divides self-validation into functional and technological validation. Its durable point is that a measurement should include qualification information, not only a scalar reading. Fault detection should identify inconsistency and, where possible, isolate the fault source.

For operational systems, carry at least:

```text
value | unit | timestamp | source_id | observed_or_estimated
quality_state | confidence_or_uncertainty | calibration_state
model_version_if_estimated | fault_code_if_any
```

## Current Operating Guard

Never allow a model-derived value to silently replace a calibrated physical measurement in a safety-, compliance-, or money-critical workflow. Make substitution visible, bound the acceptable duration and confidence, and define a fail-safe state. This guard is a current operational synthesis of the source's validation logic, not a claim that the 2011 implementations satisfy modern safety requirements.

## Source Boundary

Compiled from Chapter 4 of [[intelligent-instrumentation|Intelligent Instrumentation]]. VLSI implementations, detailed temperature circuits, numerical examples, and device equations remain lookup-only.

