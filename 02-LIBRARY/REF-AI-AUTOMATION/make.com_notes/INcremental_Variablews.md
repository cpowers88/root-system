---
type: reference
timeline: reference
status: source-capture
title: Incremental variables
slug: incremental-variables
docTags: 
createdAt: 2025-05-28T07:33:41.539Z
---

Incremental variables are variables that can be used when you want to keep track of a value when a scenario or a route in a scenario runs.

## Use incremental variables when you need:

- Counters that increment with each scenario run
- Values that can either reset after each run or persist indefinitely

The incremental variable returns a value of `1` after the first run. The subsequent value is based on your choice for the value to never reset, reset after one cycle, or reset after one scenario run.&#x20;

You can add an incremental variable to your scenario by clicking on to the **Tools** icon and selecting the **Increment function** module.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-XsCQyMlfXCyTYY1LwdVTg-20250529-084116.png" size="40" width="446" height="591" position="flex-start" alt="Increment function" showCaption="false"}

:::::ExpandableHeading
## Example: Rotating the assignment of tasks to users in a group

Imagine that you receive a form submission requesting the completion of a task. In the following scenario, an incremental variable is set to count each time a request is submitted and send the task by email to different people, alternating the assignment of the task.

To alternate the tasks, we are using the `mod `function to filter the assignments between two people.

The `mod` function returns the remainder after dividing one number by another.

For example, 12 `mod` 2 = 0, because there is no remainder after dividing 12 by 2. &#x20;

13 `mod` 2 = 1, because after dividing 13 by 2, there is a remainder of 1.

In this scenario, the incremental variable value is divided by 2 using the `mod` function, and the tasks are routed to different people based on the remainder being even (`0`) or odd (`1`).

![Incremental variables](https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-yBtHgNuMdMoYWoOtZV5tk-20250613-092333.png)

::::WorkflowBlock
:::WorkflowBlockItem
Add a **Tool > Increment function** module and configure the value to never reset.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/C2MkrykLq6eO8kjT8AdK6_uuid-805d861a-325c-2420-1bf6-3582ec935f56.png" size="60" width="707" height="346" position="flex-start" alt="Increment function" showCaption="false"}
:::

:::WorkflowBlockItem
Add a router. You will see two default routes added.
:::

:::WorkflowBlockItem
Click the wrench icon for the first route and set the filter:&#x20;

**Label**: Odd&#x20;

**Condition**: Map the incremental variable and use the `mod` math function and add the number `2`

Change the **Equal to** operator from the default **Text operator** to the **Numeric operator&#x20;**&#x61;nd type `1` in the comparison field.&#x20;

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-nfjgUnE27ONDApVF8HPO9-20250613-092458.png" size="68" width="816" height="553" position="flex-start" alt="filter odd" showCaption="false"}
:::

:::WorkflowBlockItem
Click the wrench icon for the second route and set the filter:&#x20;

**Label:** Even

**Condition:** Map the incremental variable and use the mod math function and add the number `2`.&#x20;

Change the **Equal to** operator from the default **Text operator** to the **Numeric** operator and type `0` in the comparison field.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-26Rt5zyvVcRbZbQE1NE2s-20250613-092546.png" size="70" width="819" height="532" position="flex-start" alt="even filter" showCaption="false"}
:::

:::WorkflowBlockItem
Complete your scenario by adding an Email module to the end of each route, notifying the recipient of their assignment.
:::
::::

As information comes in, the task assignment alternates between the two recipients.
:::::
