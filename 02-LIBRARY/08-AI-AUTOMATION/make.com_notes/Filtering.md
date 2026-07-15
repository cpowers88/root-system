---
type: reference
timeline: reference
status: source-capture
title: Filtering
slug: filtering
description: Manage data flow between modules with filters and operators, and copy them
image: https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/5UT0rCZ7w7L0Vo7Q9DPZ9_domino-zoomin-purple-a-1.png
docTags: 
createdAt: 2025-02-03T13:29:15.599Z
---

In some scenarios, you may need to only work with bundles that fit specific criteria. Filters will help you to select those bundles.

You can add a filter between two modules and check whether bundles received from the preceding modules fulfill specific filter conditions or not. If yes, the bundles will be passed on to the next module in the scenario. If not, their processing will be terminated.

For example, if you want to create a scenario with the [Facebook](docId\:xrAgCGHcpYJ0o9GcXgYu8) trigger *Watch posts* and you want to work only with posts containing a specific word or posts written by a specific author, a filter would make sure you receive only these posts and nothing else.

## Adding a filter

To add a filter between two modules, click on the connecting line between them.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/vfcJ7M8gpBi-dE4rqZWQs_uuid-1c880eae-ed8e-cb8c-b69a-33b4996368f8.png)

This brings up a panel where you can enter the name for the filter that is to be created and define one or more filter conditions.

![screen-shot-2021-12-10-at-16\_16\_11.png](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/TbSIURX6BoQ0WpVdiMM9K_uuid-3d5735ef-a72c-04e2-86fc-50e9b0529622.png)

For each condition, you can enter one or two operands and an operator that will determine the relation between them. In the operand field, you can enter values in the same way as you would [map](docId\:upfwoZsCC5SoIXR2954z2) them.

In the example above, you can see how to connect the [Gmail](docId\:v6l8KMmwflB2wxhoi3TRp) trigger *Watch emails* and the [Google Drive](docId\:CT1o6eSjM1F0Xm3Wk5nBx) action *Upload a file*. The filter automatically applies the condition to incoming bundles from the first module and only bundles containing attachments are allowed to pass on to the next module.

## Operators

For each condition, you can use one of several different operators.

### Basic operators

- **Exists** - checks whether a specific bundle item is filled in. Using this operator, you can create a filter that permits, for example, only Facebook posts that contain a photo to go through to the next module in a scenario.
- **Not exists** - the opposite of *exists*. It permits only those bundles where a specific item is not filled in.

### Other operators

There are a number of other operators you can use: text comparison operators, numerical operators, time and date operators, and operators for working with [arrays](docId\:K8NyMRgqbg3l_8LnPX7Wm).

## Copying a filter

Copying filters is currently not natively supported by the [Scenario editor](docId:7euvHnup3GLX7SO-Jdcng), though if you use the Google Chrome web browser, the following workaround can be employed:

::::WorkflowBlock
:::WorkflowBlockItem
Install [Make DevTool](docId\:bChJZZdDEM-1PyFEx4NPC) Chrome extension.
:::

:::WorkflowBlockItem
In Make, open your scenario.
:::

:::WorkflowBlockItem
In Chrome, open the **Developer tools**. You can do so either by choosing the **Developer tools** command from the the Chrome main menu or just press Ctrl+Shift+I or F12:

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/5P34QWcnnARKeSEitdHww-20260115-132649.png" size="60" width="1132" height="1590" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
In the **Developer tools**, click on the Make tab.
:::

:::WorkflowBlockItem
Click on the **Tools** icon in the left side bar.
:::

:::WorkflowBlockItem
.Click on the **Copy filter** tool and configure it in the right side panel.
:::

:::WorkflowBlockItem
Set the **Source Module** field - the module that's right after the filter you wish to copy.
:::

:::WorkflowBlockItem
Set the **Target Module** field - the module before which you wish to copy the filter.
:::

:::WorkflowBlockItem
Click on the **Run** button.
:::
::::
