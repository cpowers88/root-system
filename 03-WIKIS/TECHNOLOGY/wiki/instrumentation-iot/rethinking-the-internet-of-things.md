---
domain: technology
type: source-summary
timeline: reference
status: wiki-only
tags: [domain/technology, source-role/primary, subject/iot, subject/edge-computing, subject/distributed-systems]
---

# Rethinking the Internet of Things - Source Summary and Navigation Hub

**Source:** `raw/Rethinking the Internet of Things - Francis daCosta.pdf`, Francis daCosta, *Rethinking the Internet of Things: A Scalable Approach to Connecting Everything* (ApressOpen, 2013; 185 PDF pages).

## Why It Matters

The book challenges a cloud-first assumption: not every sensor should be a fully managed peer, not every reading needs reliable end-to-end delivery, and not every control loop should cross a wide-area network. Its useful contribution is an architecture thought experiment about placing cost, intelligence, filtering, and control at the right layer.

Its proposed "Chirp" protocol did not become the universal IoT foundation asserted by the text. Use the principles as design questions, not the protocol, forecasts, cost figures, or standards claims as current facts.

## Retrieval Map

- [[iot-edge-autonomy-local-control-and-trust|IoT Edge Autonomy, Local Control, and Trust]] - constrained endpoints, intermittent links, local response, graceful degradation, and the limits of simplicity-as-security.
- [[iot-three-tier-publish-subscribe-architecture|IoT Three-Tier Publish/Subscribe Architecture]] - end devices, propagator nodes, integrator functions, filtering, translation, and topic-like classification.
- [[iot-data-reduction-adoption-and-current-use-filter|IoT Data Reduction, Adoption, and Current-Use Filter]] - small-data aggregation, discovery, use cases, transition paths, and historical claims.

## Complete Chunk Ledger

The publisher placed conventional front matter after the index. Physical pages are used so the ledger matches the file as rendered.

| PDF range | Book content | Disposition |
|---|---|---|
| 1-5 | Contents at a glance and introduction | Thesis and caveats summarized here |
| 6-27 | Chapter 1: frontier constraints, economics, nature analogy, three functional levels | Compiled into edge and architecture pages |
| 28-45 | Chapter 2: guiding principles and terse "Chirp" messaging | Principles compiled; proposed packet/protocol retained as historical |
| 46-63 | Chapter 3: edge devices, classification, redundancy, local control | Compiled into edge page |
| 64-81 | Chapter 4: propagator nodes and publishing agents | Compiled into architecture page |
| 82-99 | Chapter 5: integrator functions, filtering, cluster/avoid scheduling | Compiled into architecture and data pages |
| 100-127 | Chapter 6: detailed packet/tree architecture | High-level separation compiled; packet and routing specification remains historical lookup |
| 128-147 | Chapter 7: applications and data-flow examples | Durable use-case logic compiled; forecasts omitted |
| 148-165 | Chapter 8: deployment paths, standards, ecosystem constituencies | Compiled into adoption/current-use page |
| 166-170 | Index | Reviewed for closure; lookup-only |
| 171-185 | Delayed title, copyright/ApressOpen license, author/reviewer material | License and provenance verified; biography omitted |

## Current-Use Gate

Treat every statement about IPv6 suitability, protocol overhead, device counts, component cost, attack risk, standards, and market adoption as a 2013 claim requiring current primary-source verification. The embedded ApressOpen license permits complete, unmodified electronic distribution for noncommercial purposes.

## Related Pages

- [[intelligent-instrumentation|Intelligent Instrumentation]]
- [[../distributed-systems/asynchronous-messaging|Asynchronous Messaging]]
- [[../distributed-systems/serverless-processing|Serverless Processing Systems]]

