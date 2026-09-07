---
domain: technology
type: reference
timeline: reference
status: wiki-only
tags: [subject/iot, subject/publish-subscribe, subject/distributed-systems]
source_role: primary
---

# IoT Three-Tier Publish/Subscribe Architecture

## Separate Sensing, Transport, and Meaning

DaCosta proposes three functional levels:

| Level | Book term | Durable responsibility |
|---|---|---|
| I | End device | Sense or actuate; emit/receive a minimal, typed message; remain locally autonomous where required |
| II | Propagator node | Discover endpoints, aggregate/prune traffic, translate protocols, route, and bridge to conventional networks |
| III | Integrator function | Subscribe to relevant streams, combine context, analyze, control policy, and present exceptions or decisions to humans |

The names are historical, but the separation resembles modern endpoint/edge-platform/application boundaries. It keeps device-specific and network-specific complexity from leaking into every consumer.

## Publish/Subscribe Changes the Relationship

Instead of a fixed point-to-point conversation, publishers label what a message represents and subscribers express interest. The book calls those logical groupings neighborhoods and affinities. Modern implementations may use topics, schemas, metadata, routing keys, registries, or stream-processing rules.

The important design questions are:

- Can a consumer discover meaning without knowing the device vendor?
- Is identity separate from classification and location?
- Who owns the schema and compatibility policy?
- Where are filtering, deduplication, aggregation, and retention performed?
- What delivery guarantee does each event class require?
- Can a subscriber be added without reflashing every endpoint?

## Gateways Are Policy Boundaries

The book's propagator node is more than a dumb relay. It can translate, suppress repetition, aggregate readings, enforce timing, and apply locally installed publishing agents. In a current architecture that power makes the gateway a trust and failure boundary. Version its rules, authenticate its management plane, observe dropped/transformed data, and define behavior when disconnected from central policy.

## Do Not Confuse Classification With Truth

Self-described type markers make routing possible, but they do not prove identity, calibration, accuracy, or authorization. Pair message classification with the measurement metadata and validity state described in [[intelligent-sensor-architectures-and-validation|Intelligent Sensor Architectures and Validation]].

## Source Boundary

Compiled from Chapters 1, 2, 4, 5, and 6 of [[rethinking-the-internet-of-things|Rethinking the Internet of Things]]. The detailed Chirp packet and routing tree are retained only as historical design material.

