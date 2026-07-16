---
domain: technology
type: reference
timeline: reference
status: wiki-only
tags: [domain/technology, source-role/primary, subject/instrumentation, subject/measurement, subject/sensors]
---

# Measurement Quality and Sensor Dynamics

## A Reading Is Not Yet Evidence

A measurement chain includes the sensing element, signal conditioning, conversion, processing, and the environment in which all of them operate. Quality therefore cannot be inferred from a displayed number or its decimal places.

| Property | Decision meaning |
|---|---|
| Accuracy | Closeness to a reference or accepted true value |
| Precision | Closeness among repeated readings; precision can be high while accuracy is poor |
| Repeatability | Agreement under the same method, operator, instrument, place, and short interval |
| Reproducibility | Agreement after relevant conditions change |
| Sensitivity | Output change produced by an input change |
| Resolution | Smallest input change that produces a detectable output |
| Linearity | Closeness of the input-output response to the chosen straight-line reference |
| Hysteresis | Different output for the same input depending on the direction/history of approach |
| Uncertainty | Bounded doubt attached to the result, not a defect that can always be eliminated |

The practical audit question is not "does the sensor work?" It is "is its measurement performance sufficient for the decision, alarm, or control action being made?"

## Static and Dynamic Fitness Are Different

Static characteristics describe response when the measurand is constant or changes slowly. Time-varying inputs expose energy storage, delay, damping, bandwidth, and transient response. A sensor that is accurate at equilibrium can still report a rapidly changing process too late or with unacceptable distortion.

Before using a signal, name:

1. the expected input range and rate of change;
2. the response time and sampling rate required by the decision;
3. environmental and cross-sensitive inputs;
4. acceptable error and uncertainty;
5. what happens when the signal is missing, stale, saturated, or implausible.

## Correct Interference at the Earliest Layer

The source presents three broad compensation paths: make the sensor physically insensitive to the interference, use feedback, or generate an opposing input in the conditioning circuit. The ordering matters. Interference removed at the sensing layer cannot be amplified downstream; software correction is useful only when the disturbing variable is observable and the correction model remains valid.

## Audit Pattern

```text
Decision or control action:
Measurand and operating range:
Required accuracy, resolution, and response time:
Reference/calibration source:
Known interference and environmental variables:
Missing/stale/implausible-data behavior:
Recalibration and drift trigger:
```

This is directly useful when a business wants alerts, predictive maintenance, energy monitoring, quality control, or automated field capture. Validate the measurement chain before recommending a dashboard or AI layer.

## Source Boundary

Compiled from Chapters 2-3 of [[intelligent-instrumentation|Intelligent Instrumentation]]. The equations and device-specific designs remain in the source PDF.

