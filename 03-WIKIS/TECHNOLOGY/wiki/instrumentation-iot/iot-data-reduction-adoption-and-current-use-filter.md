---
domain: technology
type: reference
timeline: reference
status: wiki-only
tags: [subject/iot, subject/data-architecture, subject/adoption]
source_role: primary
---

# IoT Data Reduction, Adoption, and Current-Use Filter

## Send Decisions Upstream, Not Noise

The book distinguishes terse device readings from the "small data" produced after local abstraction and the larger analytical context used centrally. Its durable point is that raw telemetry should not automatically cross every network boundary forever.

At the nearest sensible layer:

- remove duplicates and impossible values;
- attach units, identity, time, and quality;
- aggregate at a cadence appropriate to the decision;
- preserve exceptions and state changes;
- retain enough raw evidence for diagnosis, calibration, and model review;
- document what was filtered so silence is not mistaken for normal operation.

Reduction policy is a risk decision. A temperature trend may tolerate sampling and batching; a shutdown event may require durable delivery and acknowledgment.

## Discovery Creates Secondary Uses—and Governance Risk

Publish/subscribe allows a later consumer to discover a useful stream that the original device owner did not anticipate. That can create cross-system value, but classification is not permission. Secondary use needs ownership, purpose, privacy, retention, quality, and access rules. The book's open discovery vision should therefore be paired with modern data governance.

## Adoption Path: Bridge Before Replacement

The proposed transition uses gateways that support constrained endpoint messaging while bridging to existing IP infrastructure. The reusable adoption lesson is incremental coexistence:

1. prove a narrow endpoint/gateway/application use case;
2. keep legacy paths working;
3. standardize the data contract at the boundary;
4. measure power, traffic, latency, reliability, and maintenance burden;
5. expand only when the architecture beats a simpler existing option.

This aligns with the Technology Recommendation Ladder: do not invent a new protocol if an existing device, form, gateway, or managed platform solves the actual business problem cheaply.

## Historical Claim Filter

| Keep as a design question | Reverify or reject as current evidence |
|---|---|
| Where should complexity live? | Exact device-count and cost forecasts |
| Which control loops must be local? | Claim that IPv6 cannot serve IoT generally |
| Can endpoints be simpler and longer-lived? | Chirp as an established or inevitable standard |
| Where should data be filtered and translated? | 2013 protocol, radio, router, and market assumptions |
| Can new subscribers reuse a stream? | Simplicity alone as a security control |
| Can gateways bridge old and new systems? | Named ecosystem and vendor adoption pathways |

## Source Boundary

Compiled from Chapters 5, 7, and 8 of [[rethinking-the-internet-of-things|Rethinking the Internet of Things]].

