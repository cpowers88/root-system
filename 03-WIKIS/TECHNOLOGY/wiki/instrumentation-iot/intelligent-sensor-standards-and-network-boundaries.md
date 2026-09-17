---
domain: technology
type: reference
timeline: reference
status: wiki-only
tags: [subject/instrumentation, subject/standards, subject/interoperability]
source_role: primary
---

# Intelligent Sensor Standards and Network Boundaries

## The Durable IEEE 1451 Separation

The book's 2011 description of IEEE 1451 separates three responsibilities:

| Element | Responsibility |
|---|---|
| STIM | Front-end transducer module: sensors/actuators, conditioning, interface logic, and associated metadata |
| TEDS | Machine-readable transducer identity, characteristics, timing, calibration, and application metadata |
| NCAP | Network-facing processor: interface driver, application functions, conversion, and network communications |

The exact standard family has evolved, but the design lesson remains strong: keep transducer meaning and calibration identity portable, and isolate network-specific complexity behind a gateway boundary.

## Metadata Is Part of the Measurement

TEDS illustrates why a bare numeric stream is insufficient. A consuming system needs identity, units, timing, range, calibration, and operating characteristics to interpret the signal correctly. In a modern build, the equivalent contract should also carry timestamps, quality state, firmware/model version, security identity, and provenance.

## Protocol Selection Gate

The source surveys LonTalk, CEBus, J1850, MI Bus, and an early web-sensor pattern. Treat those details as historical. For a current design, reverify primary standards and vendor documentation, then decide from requirements:

```text
environment and distance
power and bandwidth budget
latency and determinism
node count and topology
interoperability and device lifecycle
security identity, update, and key management
failure behavior and offline operation
gateway/cloud dependency
applicable safety or industry standard
```

Do not select a protocol because it appears in this book, and do not assume IP connectivity makes a sensor interoperable or secure.

## Connection to IoT Architecture

The STIM/TEDS/NCAP separation is a standards-oriented cousin of daCosta's end-device/propagator/integrator model in [[iot-three-tier-publish-subscribe-architecture|IoT Three-Tier Publish/Subscribe Architecture]]. Both move network complexity away from the simplest sensor. IEEE 1451 is a real standards family whose current text must be checked; "Chirp" is the other author's proposed architecture and must not be mislabeled as an adopted standard.

## Source Boundary

Compiled from Chapter 7 of [[intelligent-instrumentation|Intelligent Instrumentation]]. All protocol versions and implementation details require current primary-source verification.

