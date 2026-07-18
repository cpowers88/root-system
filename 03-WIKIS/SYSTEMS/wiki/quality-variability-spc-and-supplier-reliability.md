---
type: framework
timeline: reference
status: active
reference_priority: core
tags: [systems, factory-physics, quality, spc, six-sigma, rework, suppliers, audit]
---

# Quality, Variability, SPC, and Supplier Reliability

**Summary**: Quality and operations are one coupled system. Defects consume
capacity, create rework/scrap loops, inflate cycle-time mean and spread, and make
supplier delivery unreliable. Good flow also improves quality by shortening the
distance between defect creation and detection. SPC distinguishes natural from
assignable variation; Six Sigma supplies a structured variability-reduction
organization; Factory Physics identifies where that power has the greatest system
leverage.

**Source**: `factoryPhysics.pdf` (Hopp and Spearman, *Factory Physics*, 3rd ed.),
Chapter 12, "Total Quality Manufacturing" (printed pp. 399-428; physical PDF pp.
1210-1281), reviewed as one complete chapter-content chunk. Study questions and
problems (printed pp. 428-431; physical pp. 1282-1290) were identified and excluded.

**Last updated**: 2026-07-16

## Chapter Coverage

| Section | Disposition |
|---|---|
| 12.1-12.2 | Five quality views and internal/external-quality bridge captured |
| 12.3 | Acceptance sampling, SPC, DOE, control/capability distinction, and chart extensions captured |
| 12.4 | Six Sigma statistical caveat, DMAIC/DMADV, organization, and Factory Physics relationship captured |
| 12.5 | Cost-quality tradeoff, rework law, scrap/detection delay, and mutual support captured |
| 12.6 | Supplier lead-time variability, assembly multiplication, and vendor policy captured |
| 12.7 | Three-point conclusion incorporated |

## Quality Has Multiple Meanings

Quality can mean innate excellence, superior product attributes, user preference,
conformance to specification, or value for price. Operations must connect:

- **external quality**: what customers value and experience; to
- **internal quality**: product/process measures that production can observe and
  control.

That connection requires error prevention, rapid detection, and a field-feedback
loop that routes customer failures back to the responsible design/process team.

## Three Statistical Quality Roles

1. **Acceptance sampling** detects nonconforming output after it exists.
2. **Statistical process control (SPC)** monitors process mean and variation in
   real time, distinguishing stable natural variation from assignable causes.
3. **Design of experiments (DOE)** deliberately varies controllable inputs to find
   causal drivers and improve the process.

Do not adjust a process in response to ordinary noise; doing so increases
variability. Control limits describe statistically unusual process behavior.
Specification limits describe external performance requirements. A process can be
stable but incapable: "in control" does not mean "meets customer requirements."

Use mean charts with variation charts, attribute charts when output is classified
good/bad, and the same control logic for throughput or delivery performance when
the measure is not a physical dimension.

## Six Sigma: Useful but Not a Manufacturing Theory

DMAIC structures improvement of an existing process: define, measure, analyze,
improve, control. DMADV applies when a process requires redesign: define, measure,
analyze, design, verify. The belt/champion structure gives trained people sustained
ownership rather than ending with a short course.

The familiar 3.4-defects-per-million claim assumes a 1.5-sigma mean shift and is
sensitive to how "opportunities" are counted. It supports within-process progress
only when the denominator remains honest and stable; it is not a universal quality
comparison.

Six Sigma measures and attacks variability well. Factory Physics supplies the
system model needed to decide which variability source constrains throughput,
cycle time, WIP, or service. They are complements.

## Quality and Operating Performance

Quality cost can rise or fall with quality. Premium materials may cost more;
preventing rework may save more than it costs. Evaluate the specific prevention,
failure, customer, capacity, and market consequences rather than asserting either
"quality is free" or "quality is costly" universally.

### Rework law

For a fixed throughput, rework increases both the mean and standard deviation of
cycle time. It:

- consumes capacity and can create or move the bottleneck;
- increases effective processing-time variance;
- requires more WIP to protect throughput;
- lengthens quoted lead time or lowers on-time service; and
- becomes more disruptive as the rework loop grows longer.

Separate rework lines can protect main-line capacity but hide ownership and do not
remove total cycle-time inflation. Scrap is effectively rework from the start of
the routing and can be even more costly.

### Flow supports quality

High WIP increases the number of units produced between defect creation and
detection. With delayed end-of-line inspection, throughput can actually rise and
then fall as WIP grows because additional output is overwhelmed by scrap. WIP
control, early detection, and quality at source create a reinforcing improvement
cycle: less delay -> less loss -> clearer cause -> faster correction.

## Supplier Reliability and Assembly

Purchased-part quality problems remain operational problems even when receiving
inspection catches them: returns and supplier rework make effective delivery time
variable. Higher delivery variance requires more safety lead time and raw-material
inventory for the same on-time probability.

Assembly multiplies the reliability requirement. If ten independent components are
each 95% likely to arrive on time, the chance all ten are present is only
`0.95^10`, about 60%. To make the assembly 95% ready, every component must be about
99.49% reliable. The tails of supplier lead-time distributions therefore matter
more as component and supplier counts grow.

Supplier choice must include delivery variance, defect effects, schedule risk, and
inventory cost - not price alone. Fewer capable suppliers may improve coordination
and priority, but inexpensive/common items and expensive/rare components warrant
different service targets.

## Audit Sequence

1. Translate customer complaints/returns into controllable internal measures.
2. Separate natural variation from assignable causes before changing settings.
3. Check stability and capability independently.
4. Map every scrap/rework loop and its consumed station capacity.
5. Measure time from defect creation to detection and count exposed WIP.
6. Validate Six Sigma denominators and select projects by system leverage.
7. Compare suppliers on acceptable-part delivery distributions, not quoted mean
   lead time or unit price alone.
8. For assemblies, compute joint availability rather than reviewing each component
   service level in isolation.

## Overlap Decisions

[[jit-implementation-tactics-and-quality-revolution]] retains Chapter 4's JIT/TQM
history, setup/quality practices, and ISO critique. [[causes-of-variability-breakdowns-setups-rework]]
retains Chapter 8 effective-process-time formulas. This page adds Chapter 12's
SPC/capability distinction, Six Sigma boundary, rework law at line level, defect
detection delay, and supplier/assembly reliability consequences.

## Connects to

[[variability-buffering-batching-and-diagnostic-laws]],
[[push-pull-conwip-and-postponement]],
[[qr-model-and-lead-time-variability]], and
[[designing-for-human-error-and-recovery]].

## Use / Retrieval Notes

**Use when**: Defects, rework, scrap, late suppliers, inspection delay, or a Six
Sigma initiative must be translated into throughput, WIP, lead-time, and service
consequences.

**Proof**: A quality intervention reduces the relevant defect/rework distribution
and demonstrates the resulting capacity, flow, inventory, and service movement.
