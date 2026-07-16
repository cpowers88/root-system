---
domain: systems
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, system-dynamics, diffusion, epidemics, product-growth, audit]
---

# Epidemics, Innovation Diffusion, and Product Growth

**Summary**: S-shaped growth is a shift in loop dominance: reinforcing growth
drives early expansion, then balancing feedback from depletion, saturation,
recovery, abandonment, or replacement limits it. Epidemics and product adoption
share this structure, but useful models must represent their causal mechanisms
rather than merely fit an S-curve to historical data.

**Source**: BusinessDynamics.pdf (Sterman, Business Dynamics, 2000), Chapter 9,
"S-Shaped Growth: Epidemics, Innovation Diffusion, and the Growth of New
Products" (printed pp. 295-347; physical PDF pp. 320-372), reviewed as one
complete chapter chunk.

**Last updated**: 2026-07-15

## Chapter Coverage

| Source section | Disposition |
|---|---|
| 9.1 Modeling S-Shaped Growth | Logistic, Richards, Gompertz, and Weibull growth models; assumptions and fit limits captured below |
| 9.2 Dynamics of Disease | SI and SIR structures, tipping point, reproduction rate, immunization, herd immunity, structural change, incubation, and HIV extensions captured |
| 9.3 Innovation Diffusion | Word of mouth, Bass diffusion, historical-fit warning, abandonment, fads, and durable-product replacement captured |
| 9.4 Summary | Causal-modeling and anti-black-box conclusions incorporated throughout |

## S-Shaped Growth Is a Change in Loop Dominance

Early in a growth process, reinforcing feedback dominates: more infected people
create more exposures; more adopters create more word of mouth; a larger installed
base increases visibility and complementary support. Growth cannot continue
forever. As the susceptible or potential-adopter pool is depleted, balancing feedback
strengthens and net growth falls.

Smooth S-shaped growth requires the limiting feedback to operate without a major
delay. Delayed limits can create overshoot and oscillation; growth that erodes its
own carrying capacity can create overshoot and collapse.

## Common Growth Curves and Their Limits

| Model | Useful feature | Restrictive assumption |
|---|---|---|
| Logistic | Simple, analytically tractable, and often a reasonable first approximation | Fractional growth declines linearly; maximum net growth occurs exactly at half the carrying capacity |
| Richards | Adds a shape parameter and permits asymmetric S-curves | Still imposes a preselected analytic family |
| Gompertz | Common asymmetric special case; peak growth occurs before the midpoint | Shape remains fixed by the functional form |
| Weibull | Flexible shape and scale for growth or adoption timing | A statistical fit does not identify the causal feedback structure |

These curves can describe a pattern but do not explain why it occurs. Different
causal structures can fit the same history and then respond differently to policy.
Use curve families as diagnostics or compact approximations, not as black-box
forecasts.

## Epidemic Structure: SI, SIR, and the Tipping Point

The simple SI model divides a fixed population into susceptible and infectious
stocks. Infection depends on contact between the two groups, so early infections
reinforce further infection while depletion of susceptibles eventually limits growth.

The SIR model adds a recovered stock and a recovery outflow. Whether an epidemic
grows depends on the number of new infections created by each infectious person
before recovery:

Reproduction rate = contact rate x infectivity x infectious duration x susceptible fraction

- Below 1, recovery dominates and introductions die out.
- At 1, the system is at the tipping threshold.
- Above 1, contagion dominates until depletion or intervention lowers the rate.

This formulation identifies four distinct levers: reduce contact, reduce infectivity,
shorten the infectious period, or reduce the susceptible fraction. Universal or
perfect immunization is not required for eradication; the intervention must keep
the reproduction rate below one.

## Herd Immunity and Recurrent Waves

Herd immunity is a system state, not simply a vaccination percentage. A population
is protected when its reproduction rate is below one under current contact,
infectivity, duration, and susceptibility conditions. Urbanization, new practices,
technical changes, waning immunity, births, or a changed pathogen can move the
same population across the tipping point.

Repeated waves can arise when an epidemic depletes susceptibility enough to restore
stability, then births or other changes rebuild the susceptible pool until the threshold
is crossed again. Incubation and asymptomatic transmission weaken reactive controls
because people continue normal contact before detection.

The deterministic SIR model is an average-process assumption. Small populations,
heterogeneous contact networks, highly variable infectious periods, or superspreading
may require stochastic or agent-based extensions.

## Innovation Diffusion as Contagion

Innovation adoption can be modeled with potential adopters and adopters:

- contact with adopters creates awareness and imitation;
- adoption reduces the remaining potential market;
- product attractiveness, availability, price, competition, and technical change
  affect conversion;
- advertising or other external influence can create adoption without contact.

The Bass model combines external influence with imitation. It often fits historical
sales well, but the coefficients do not automatically explain the underlying
mechanisms. A causal model should distinguish paid awareness, word of mouth,
availability, network effects, product quality, competitive response, and the
changing criteria customers use as a market matures.

## Abandonment, Fads, and Replacement

A cumulative-adoption curve is insufficient when people can abandon an innovation.
Adding an abandonment flow can produce a fad: reinforcing adoption creates rapid
growth, but changing attractiveness or social signals reverse the flow.

Durable-product sales combine first purchases with replacements. The installed base
is a stock; retirements depend on product age and lifetime; replacement sales can
remain high after first-time adoption saturates. Confusing shipments with installed
base or first purchases with total demand produces poor capacity forecasts.

## Audit Translation

For a new service, process rollout, technology adoption, or customer program, map:

1. potential population and current adopters;
2. contact, awareness, and conversion mechanisms;
3. external promotion versus endogenous word of mouth;
4. capacity, availability, and attractiveness constraints;
5. abandonment, churn, retirement, and replacement;
6. threshold conditions and the variables capable of moving the system across them;
7. heterogeneity hidden by an aggregate average.

Do not report an adoption forecast from a fitted S-curve without identifying the
feedbacks that make the forecast policy-responsive.

## Connects to

[[s-shaped-growth-overshoot-collapse-and-chaos]],
[[multiple-loop-systems-and-loop-dominance]],
[[path-dependence-positive-feedback-and-standards]],
[[coflows-aging-chains-and-attribute-dynamics]],
[[model-validation-and-testing-practice]], and
[[forecasting-expectations-and-fudge-factors]].

## Use / Retrieval Notes

**Use when**: Diagnosing adoption, contagion, churn, replacement demand, or a
forecast that assumes smooth market saturation.

**Proof**: The model names the stocks, contact/conversion flows, limiting feedback,
threshold, abandonment/replacement processes, and evidence that would distinguish
its causal structure from another curve that fits the same history.

