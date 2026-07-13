---
title: Incomplete executions
slug: incomplete-executions
description: Store failed scenario runs and resolve them automatically or manually to prevent data loss
image: https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/15xODkWQr6NBmCuxu-Iuj_domino-zoomin-purple-a-1.png
docTags: 
createdAt: 2025-02-03T13:29:15.599Z
---

Incomplete executions are a safety feature that protects your scenarios from stopping due to errors and from data loss that could happen. When a scenario encounters an error with incomplete executions enabled, Make stores the unfinished scenario run in the **Incomplete executions** tab.

:::hint{type="info"}
Incomplete executions are disabled by default. To store incomplete executions, enable the **Store** **incomplete executions** option in the **Scenario** **settings**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/JITv5bFhH08k053Dq2pdC-20260204-150539.png" size="40" width="720" height="1392" position="center" showCaption="false"}
:::

You can handle incomplete executions in the following ways:

- let Make retry the incomplete executions automatically for the [supported error types](docId:05poZkkKtmKaJW14PAdu-) or use the **Break** error handler
- [resolve](docId\:sFa-8JvNu5DmVRabNRseR) the incomplete executions manually
- [delete](docId\:sFa-8JvNu5DmVRabNRseR) the incomplete executions

:::hint{type="info"}
The maximum number of incomplete executions from all scenarios in all teams in an organization depends on your usage allowance. If the limit is exceeded, you will receive an error message.&#x20;
:::
