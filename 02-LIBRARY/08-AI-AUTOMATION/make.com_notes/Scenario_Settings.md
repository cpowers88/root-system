---
type: reference
timeline: reference
status: source-capture
title: Scenario settings
slug: scenario-settings
description: Define how your scenario executes and behaves if an error occurs
image: https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/_Of0g4JG3kBZvkOgEFRr0_domino-zoomin-purple-a-1.png
docTags: 
createdAt: 2025-02-03T13:29:15.599Z
---

To access **Scenario settings**, click the gear icon in the Scenario Builder. Here you can set various advanced settings.&#x20;

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/9LE9x1UL499NV1oWem5vb-20260518-112450.png)

## Process data in order

You can choose to processes data in the order it's received, with each run finishing before the next starts. If there's an incomplete execution, no new runs are processed until all incomplete executions are resolved.

- When enabled, Make completes each execution before starting the next. New runs are paused until all incomplete executions are resolved.
- If disabled, the scenario continues to run according to its [schedule](docId\:SCPFttWgFaPf077uJO1jh), regardless of errors.

:::hint{type="info"}
Process data in order also applies to [webhooks](docId:1yhUnJ8jvZyxiP9Cf3Ps1). By default, Make processes webhooks in parallel. When you enable process data in order, Make waits until the previous execution is complete before starting the next one.
:::

## **Keep data confidential**

Make stores the data processed during each run in your execution logs. This lets you inspect and troubleshoot when something goes wrong. If you enable this setting, Make won't retain any of that data. Your logs will still show that a run happened, but without the actual payload.

Enable keep data confidential if your scenarios handle sensitive or personal data that shouldn't be stored after processing.

:::hint{type="warning"}
If enabled, there are very limited options to solve errors that occur in a scenario execution.
:::

## Store incomplete executions

When a scenario run fails, Make saves it as an incomplete execution so the data isn't lost. You can then retry the run manually or let Make handle it automatically - either way, your scenario keeps running.

- If enabled, the scenario is paused and moved to the [incomplete executions](docId:6zZNn7v35hERRCJFccp9Q) folder. This gives you the possibility to fix the issue and continue from where the scenario stopped.
- If disabled, the scenario run stops and starts a [rollback phase](https://help.make.com/scenario-execution-cycles-and-phases#F-KOC).

You can resolve each incomplete execution either manually or automatically.

:::hint{type="info"}
The data in this folder counts towards the storage limits of your [subscription plan](https://www.make.com/en/pricing).
:::

## Discard data if storage is full

If your incomplete executions folder is full when an error occurs, Make discards the failed data and keeps the scenario running. Discarded data can't be recovered, so make sure you have enough space if losing data isn't an option.

## Use updated variable values

When retrying an incomplete execution, you can use either the current variable values or the ones from the original run.&#x20;

- Enable this to use the latest team and organization variable values.
- Disable it to use the values that were active at the time of the original run.

## **Errors before deactivation&#x20;**

You can set how many errors in a row Make accommodates before deactivating the scenario. This setting defines the maximum number of attempts before the scenario deactivates (though there are exceptions listed in the [error handling overview](docId:7-HEHdTuU2XyYs8_qurub).&#x20;

:::hint{type="info"}
If a scenario starts with an instant trigger, the setting is ignored and the scenario is deactivated immediately once the first error has occurred.
:::

## **Commit after each module**

By default, Make commits data only when the entire scenario finishes successfully. Enable this setting to commit data after each module runs instead.

- If enabled, data is committed right away and cannot be restored in the case of an error.
- If disabled, no commit occurs until operations are executed for all modules.

This affects data modules, instant triggers, and webhook responses. Use it when you need to ensure data is saved incrementally - for example, if a later module fails, data processed by earlier modules is still committed rather than rolled back.

## Commit trigger last

This setting defines the module commit order after a successful scenario operation phase. This setting is enabled by default.

- If enabled, the commit phase skips the trigger and processes that module last.
- If disabled, the commit phase occurs in the default order.

## Cycles per run

This setting defines the maximum number of cycles allowed during a scenario execution.

Setting more [cycles](https://help.make.com/scenario-execution-cycles-and-phases#75-3E) can be useful when you want to prevent connection interruption to third-party services. This can also ensure all records are processed within the scenario run.

If you execute the scenario manually by clicking the **Run once** button, the setting is ignored and **only one cycle** will be performed.
