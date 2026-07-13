---
title: Edit the structure of a scenario input or output
slug: edit-the-structure-of-a-scenario-input-or-output
docTags: 
createdAt: 2025-04-08T07:51:47.754Z
---

To edit the structure of the scenario input or output:

:::::WorkflowBlock
:::WorkflowBlockItem
In the Scenario Builder, click the scenario inputs and outputs icon.
:::

::::WorkflowBlockItem
Click on the item you want to edit, and make the changes.

:::hint{type="warning"}
Changing the scenario input **name** will cause the scenario to fail. If you need to change the input name, we recommend deleting the old item and adding a new one with the new name.

If you change the inputs from not required to required, you need to change your scheduling to **On-demand**.
:::
::::

:::WorkflowBlockItem
Click **Save**.
:::
:::::

Once you save your changes, the scenario input or output updates automatically everywhere you use it.

:::hint{type="warning"}
Editing the input or output structure item(s) in an active scenario might lead to data inconsistencies and scenario failure.

If you are connecting the scenarios through the **Call a scenario** and **Return output** modules, check the **Relation tree** tab to find related scenarios  quickly. [Find out more about the Relation tree tab](docId:9cmtJAPTuG8sQnm3uq-ay).
:::
