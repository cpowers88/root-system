---
type: reference
timeline: reference
status: source-capture
title: Use scenario inputs
slug: use-scenario-inputs
docTags: 
createdAt: 2025-04-08T07:50:45.540Z
---

You can use scenario inputs in the following ways:

- You can provide the inputs manually when you want to run the scenario. This is great for processes that you need to run on demand and that need human input and verification.
- You can send the inputs from another scenario. In this case, you need to use the **Scenarios >** **Call a scenario** module to trigger the scenario.
- You can add the inputs to the request body when triggering the scenario with the [Make API](https://developers.make.com/api-documentation/api-reference/scenarios/post--scenarios--scenarioid--run).
- You can define scenario inputs and outputs to help Make AI Agents and MCP server tools understand what data to provide and return.

:::hint{type="info"}
For combining subscenarios and scenario inputs, use the **Scenarios >** **Start scenario** module as the trigger for the subscenario.
:::

With defined scenario inputs, every time you trigger a scenario manually with the **Run once&#x20;**&#x62;utton, the scenario inputs window pops up. The scenario can run only if you fill in all the required fields with the correct data types.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/LlW-YSNRoiV4a6dkDmWLg-20260121-134033.png)
