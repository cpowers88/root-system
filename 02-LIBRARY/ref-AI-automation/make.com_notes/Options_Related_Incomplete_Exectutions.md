---
type: reference
timeline: reference
status: source-capture
title: Options related to incomplete executions
slug: options-related-to-incomplete-executions
docTags: 
createdAt: 2025-04-08T11:52:59.627Z
---

The following options in Make scenario settings determine if and how the incomplete executions are stored:&#x20;

- **&#x20;Store incomplete executions**
  This option enables incomplete executions for the scenario. If this option is disabled, Make doesn't store incomplete executions of the scenario.
- **Process data in order******
  Process data in order ensures that the scenario runs in a sequence. If there is an incomplete execution of the scenario, Make pauses further scheduling of the scenario to keep the processing in the chronological sequence. Make activates the scenario again after the scenario has no incomplete executions.

  If the scenario has instant scheduling, Make stores the arriving bundles in the webhook queue.
- **Enable data loss**
  Data loss setting controls what should happen when Make cannot create an incomplete execution of a failed scenario run. This happens in most cases because the incomplete execution storage is full. Incomplete execution storage is limited based on the usage allowance.

  If you keep data loss disabled, Make pauses scheduling of the scenario to avoid losing any more scenario runs, until you clear the incomplete execution storage and enable the scenario again.

  If you enable data loss, Make will continue scheduling the scenario even if it couldn't store the incomplete execution.
