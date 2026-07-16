---
domain: systems
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, system-dynamics, forecasting, expectations, cognitive-bias, audit]
---

# Forecasting, Expectations, and Fudge Factors

**Summary**: Forecasts often adapt to recent history through smoothing and trend
extrapolation. That learning is useful but delayed: forecasters miss turning points,
continue obsolete trends, attenuate volatility, and adjust formal model outputs
toward intuition or political expectations.

**Source**: BusinessDynamics.pdf (Sterman, Business Dynamics, 2000), Chapter 16,
"Forecasts and Fudge Factors: Modeling Expectation Formation" (printed
pp. 631-660; physical PDF pp. 656-685), reviewed as one complete chapter chunk.

**Last updated**: 2026-07-15

## Chapter Coverage

| Source section | Disposition |
|---|---|
| 16.1 Expectation formation | TREND structure, time constants, steady-state behavior, and transient error captured |
| 16.2-16.4 Cases | Energy consumption, commodity prices, and inflation evidence captured |
| 16.5 Forecast consumers | Adaptive expectations, anchoring, add factors, and consumer tests captured |
| 16.6 Initialization | Steady-state response and initialization requirements retained conceptually |
| 16.7 Summary | Slow adaptation, turning-point failure, trend dominance, and political adjustment incorporated |

## Expectations Are Decision-System States

Capacity, hiring, inventory, pricing, investment, and policy decisions depend on
beliefs about the future. Those beliefs are not direct observations. They are states
formed from past information, filtered through delays, heuristics, models, incentives,
and social pressure.

Treat an expectation as an explicit stock with an update process. Do not insert a
perfect forecast or assume errors cancel automatically.

## The TREND Structure

The boundedly rational TREND formulation estimates the fractional growth rate of
an input from its own history:

1. Smooth the input to form a perceived present condition.
2. Smooth that perceived condition again to form a reference condition.
3. Compare present with reference to estimate the indicated trend.
4. Smooth the indicated trend to form the perceived trend.

Three time constants control how quickly the present condition, reference condition,
and perceived trend adjust.

If an input grows exponentially at a constant rate, the TREND function eventually
estimates that rate without steady-state bias. During changes and turning points,
the internal smoothing creates lag and transient error.

Initialization matters. The perceived present, reference condition, and trend must be
consistent with the assumed initial growth state or the model creates artificial
transients unrelated to the real system.

## Recurring Forecast-Error Signatures

| Signature | Structural cause |
|---|---|
| Missed turning point | Smoothed history still reports the old direction after reality changes |
| Overshoot after a trend | The estimated trend adjusts slowly and continues extrapolating after the driver reverses |
| Phase lag | Peaks and troughs in expectations occur after actual peaks and troughs |
| Attenuation | Smoothing suppresses the amplitude of real variation |
| Persistent bias | Forecasts anchor on a reference value or revise too little |
| Capacity boom/bust | Growth is extrapolated during expansion and saturation is recognized only after delayed capacity arrives |

## Evidence from Energy, Commodities, and Inflation

The chapter tests the adaptive formulation against professional forecasts in several
domains. In each, simple smoothing and trend extrapolation reproduce much of the
observed forecast behavior despite forecasters' claims to consider many variables.

- Energy forecasts remained strongly constrained by recent consumption trends.
- Commodity-price forecasts missed reversals and overshot after sustained movements.
- Inflation forecasts lagged turning points, muted cyclical variation, and showed
  anchoring bias.

The lesson is not that other information is never considered. When causal
relationships are noisy, unstable, obscure, or disputed, the target variable's own
history becomes a powerful anchor and dominates judgment.

## Anchoring and Adjustment

Forecasters revise from a reference point rather than recomputing beliefs from
scratch. The anchor may be:

- the latest observed value;
- the recent smoothed trend;
- zero change or a policy target;
- a long-term historical average;
- a consensus forecast;
- the prior published forecast.

Adjustment is commonly insufficient. Anchors can improve stability in noise but
also preserve obsolete assumptions.

## Fudge Factors and Add Factors

An add factor is an unexplained adjustment applied until a formal model's output
matches intuition, conventional wisdom, or political acceptability. It may be
defended as incorporating fresh information or model limitations, but without a
named causal variable, source, and test it prevents replication and hides bias.

A legitimate override should be recorded as an explicit hypothesis:

- what new information is missing from the model;
- how it affects the forecast;
- who supplied the judgment;
- its units and duration;
- what evidence will confirm or retire it.

If the adjustment cannot be represented and tested this way, report the model result
and judgmental override separately.

## Questions for Forecast Consumers

1. What exact history, variables, and time window anchor the forecast?
2. How are recent observations smoothed, weighted, and revised?
3. What are the effective perception and adjustment delays?
4. How did the method perform at prior turning points?
5. Does the interval include structural uncertainty or only parameter noise?
6. Which manual overrides or add factors were applied?
7. Can the published forecast be reproduced without private intuition?
8. What event would cause the trend assumption to be retired?
9. Is the forecast being used beyond the horizon over which its feedback structure
   was tested?

## Audit Translation

Maintain a forecast lineage table:

| Field | Required record |
|---|---|
| Target and horizon | What is predicted and when |
| Data cutoff | Information actually available when issued |
| Base method | Smoothing, trend, causal model, judgment, or combination |
| Parameters | Windows, weights, and adjustment times |
| Overrides | Amount, author, rationale, evidence, and expiration |
| Prior-version comparison | What changed and why |
| Turning-point test | Performance before and after known reversals |
| Decision consequence | Capacity, staffing, cash, inventory, or policy exposure |

## Connects to

[[forecasting-time-series-and-exponential-smoothing]],
[[material-information-and-pipeline-delays]],
[[bounded-rationality-intended-rationality-and-local-policy]],
[[commodity-cycles-and-the-generic-market-model]],
[[pulp-paper-cycles-and-sensitivity-analysis]],
[[model-validation-and-testing-practice]], and
[[epidemics-innovation-diffusion-and-product-growth]].

## Use / Retrieval Notes

**Use when**: Reviewing a professional forecast, capacity plan, budget, consensus
estimate, or model output that has been manually adjusted.

**Proof**: The forecast can be reproduced from information available at issue time,
its smoothing/adjustment delays and overrides are explicit, and it has been tested
against turning points rather than only periods of stable trend.

