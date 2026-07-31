---
type: reference
timeline: reference
status: source-capture
title: Router
slug: router
description: Branch a scenario into multiple routes to process data differently based on specific conditions
image: https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/RhNRn8RZpC590p7fu9VMg_domino-zoomin-purple-a-1.png
docTags: 
createdAt: 2025-02-03T13:29:15.599Z
---

A router allows you to branch the scenario flow into several chains of modules. Each route processes the data differently according to the condition you set. Filters help you to determine conditions via different operators such as `less than`, `greater than`, and so on.

Order routes in the sequence you want and set up a fallback route that will process data that doesn't fit other routes.

:::hint{type="success"}
See our scenario template for the [Controlled distribution of data flow](https://www.make.com/en/templates/2952-controlled-distribution-of-data-flow).
:::

## Adding a router to a scenario&#x20;

You can add a router in two different ways:

- Connect a router to a module:

::::WorkflowBlock
:::WorkflowBlockItem
Click **Add another module**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/4CkrlJIBl1di_p1x71ery-7A9Xm0SEYKNR5hyiYiNtj-20250214-104816.png" size="62" width="677" height="420" position="center" darkWidth="677" darkHeight="420" showCaption="false"}
:::

:::WorkflowBlockItem
In the search box, type **Flow controls** and click it.

![](https://archbee-image-uploads.s3.amazonaws.com/4CkrlJIBl1di_p1x71ery-u0Ejrv2fkBo4bRM2LrUiS-20250214-104853.png)
:::

:::WorkflowBlockItem
Select **Router**.
:::
::::

- Insert a router between two modules:

::::WorkflowBlock
:::WorkflowBlockItem
Right-click the bridge between two modules, and select **Add a router**.

![](https://archbee-image-uploads.s3.amazonaws.com/4CkrlJIBl1di_p1x71ery-AFT6IYmtIq9Qk8Hh71cyt-20250214-105016.png)
:::
::::

## Order routes

You can set the order of routes in which Make processes them in the scenario.

This example shows the router that determines which hint to send you on Slack according to tomorrow's weather.

::::WorkflowBlock
:::WorkflowBlockItem
Click the router that contains the routes you want to order.
:::

:::WorkflowBlockItem
Right-click and select **Order routes**. A window appears.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/4CkrlJIBl1di_p1x71ery-7NMjzMmIo7MABvZ3xT1oD-20250214-104142.png" size="60" width="441" height="362" position="center" darkWidth="441" darkHeight="362" showCaption="false"}
:::

:::WorkflowBlockItem
Click arrows and move routes according to your needs.
:::

:::WorkflowBlockItem
*Optional*. Select **Auto-align arranges with set order** to visually arrange modules on the scenario canvas according to the set order.
:::

:::WorkflowBlockItem
Click **Apply**.
:::
::::

:::hint{type="success"}
Routes are processed sequentially, not in parallel. Make won't process the second route unless it finishes processing the first one.
:::

## The fallback route

A fallback route processes data that doesn't fit the condition of all other routes. You can mark a route as a fallback if you want it to be executed last.

:::hint{type="info"}
You can set up a filter for a fallback route same as for other routes.
:::

To set up a fallback route, follow the steps:

::::WorkflowBlock
:::WorkflowBlockItem
Click the route you want to mark as a fallback. A filter window appears.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/4CkrlJIBl1di_p1x71ery-SWpPW5k0ghLuACwq_5Mki-20250214-104238.png" size="60" width="664" height="754" position="center" darkWidth="664" darkHeight="754" showCaption="false"}
:::

:::WorkflowBlockItem
Select **Yes**.
:::

:::WorkflowBlockItem
Click **Save**.
:::
::::

You can recognize the fallback route by the special arrow icon on the router module:

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/bKOATYxUqQHyoHAhGGKn7_uuid-036cc5df-914c-058d-d73f-7e0774a9e6c1.png" size="40" width="298" height="317" position="center" darkWidth="298" darkHeight="317" showCaption="false"}

## Select a whole branch

You can manage all modules in the branch at once.

Click the route menu, then click **Select whole branch**. It selects all the following modules.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/IrpZRCGHih_oujYeT9637_uuid-e3def79c-e047-8485-8c6e-d563eb9323a2.png)

You can copy or delete all selected modules at once.

**Example of a router with a fallback route**

You need to receive a message on Slack depending on tomorrow's weather:

- if the weather is hot, the message is `wear shorts`.
- if the weather is cold, the message is `wear a jacket`.
- if the weather is neither hot nor cold, the message is `better stay at home`.

The scenario looks like that:

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/chJne3fCQxUYdpDVbPlVV_uuid-1159cae7-cd6f-80a5-2280-f28de8aa5927.png" size="76" width="1007" height="1038" position="center" darkWidth="1007" darkHeight="1038" showCaption="false"}

The scenario flow is:

::::WorkflowBlock
:::WorkflowBlockItem
The Weather module gets data about tomorrow's weather.
:::

:::WorkflowBlockItem
Data goes to the router that processes routes in the determined order:

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/4CkrlJIBl1di_p1x71ery-BQG-iuSswyxPS-O03UXy_-20250214-103759.png" size="60" width="443" height="300" position="center" darkWidth="443" darkHeight="300" showCaption="false"}

a. The **Hot weather** route sends the message to Slack, if data fits the filter condition:

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/4CkrlJIBl1di_p1x71ery-pqtiJwBALe7xyVNGecyFL-20250214-103850.png" size="60" width="661" height="686" position="center" darkWidth="661" darkHeight="686" showCaption="false"}

b. The **Cold weather** route sends the message to Slack, if data fits the filter condition:

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/4CkrlJIBl1di_p1x71ery-1C8OePr9a8L6pnpZSb4Fm-20250214-103925.png" size="60" width="661" height="685" position="center" darkWidth="661" darkHeight="685" showCaption="false"}

c. The **Fallback** route sends the message to Slack, if data doesn't fit previous routes.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/4CkrlJIBl1di_p1x71ery-w0NqmS-n5v_864VysGVU8-20250214-103953.png" size="60" width="644" height="681" position="center" darkWidth="644" darkHeight="681" showCaption="false"}
:::
::::
