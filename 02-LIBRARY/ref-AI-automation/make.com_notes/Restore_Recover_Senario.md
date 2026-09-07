---
type: reference
timeline: reference
status: source-capture
title: Restore and recover scenario
slug: restore-and-recover-scenario
description: Restore previous versions of your scenarios and recover unsaved changes when needed
image: https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/s6sx-z3eC6pkf8y3MKKwJ_domino-zoomin-purple-a-1.png
docTags: 
createdAt: 2025-02-03T13:29:15.599Z
---

When working on scenarios, changes don't always go as planned. You may need to undo edits, restore previous versions, or troubleshoot after updates. Make allows you to restore a manually saved scenario and retrieve unsaved changes. You can use: 

- **Version history** for restoring previously manually saved versions
- **Scenario recovery** for retrieving unsaved changes in case of unexpected session interruptions&#x20;

These features will help you safely build, edit, and maintain your scenarios.

## Version history

Version history lets you access and restore previously saved scenario versions for up to 60 days. It helps you revert unwanted changes, troubleshoot errors, and safely experiment with new configurations.&#x20;

### When to use Version history

Saving scenario versions manually can help you in many cases:

- **Building or expanding a scenario**

:::Paragraph{indent="1"}
When creating or modifying a scenario, you may experiment with different routing logic, modules, filters, or mappings. Saving a baseline version before experimenting lets you safely test changes and easily revert if something doesn't work. 
:::

- **Fixing a broken automation after changes**

:::Paragraph{indent="1"}
Updates to modules, filters, or mappings can sometimes cause a scenario to stop working or produce incorrect results. This is particularly important if the automation supports critical business processes. Restoring a previous version from when the scenario was working correctly helps you quickly fix the problem and investigate later what caused the issue.  
:::

- **Rolling back unwanted changes**

:::Paragraph{indent="1"}
There’s no undo button for scenarios in Make. By saving your scenario regularly, you can restore a previous state in case you accidentally delete a module, filter, or tool, or change module settings or mappings.
:::

- **Working in a team**

:::Paragraph{indent="1"}
When multiple team members work on the same scenario, changes can be saved by different users. Version history allows you to track who made updates and restore previous versions if needed.
:::

### Restore scenario from Version history

To restore a manually saved scenario from the **Version history**:

::::WorkflowBlock
:::WorkflowBlockItem
Open your scenario.
:::

:::WorkflowBlockItem
Click the **V****ersion history** icon in the Scenario toolbar.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/PF7R6KogXMf62CpDtvdri-20260316-105452.png" size="80" width="1324" height="174" position="center" darkWidth="1324" darkHeight="174" showCaption="false"}
:::

:::WorkflowBlockItem
In the **Versions** field, select a previous version you want to restore.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/rfJI3E7tcKn--uWJLtf1--20260316-110938.png" size="50" width="1098" height="798" position="center" darkWidth="1098" darkHeight="798" showCaption="false"}
:::

:::WorkflowBlockItem
Click **Restore version**.
:::

:::WorkflowBlockItem
Click the **Save** icon to save the scenario with the restored version.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/njXrvWe2Z4NSELrXfPfOf-20260316-111253.png" size="60" width="966" height="174" position="center" darkWidth="966" darkHeight="174" showCaption="false"}
:::
::::

:::hint{type="warning"}
The restored version of the scenario is not automatically saved. If you wish to save the restored version of the scenario, you have to do so manually, as described in step 5.
:::

## Scenario recovery

Scenario recovery allows you to retrieve unsaved changes to a scenario from a blueprint that is automatically saved in the background while you work in Scenario Builder.

### When to use Scenario recovery

Scenario recovery helps you retrieve the changes you haven't saved manually in case of unexpected user session interruptions, such as a browser crash, an internet disconnect, a power outage, or when you accidentally closed the tab.

When you reopen a scenario, Make compares the latest automatically saved blueprint and the latest manually saved version. If they differ, you will be prompted to recover the most recent changes.  &#x20;

:::hint{type="warning"}
Scenario recovery is not an autosave feature. It only helps retrieve unsaved changes after a session interruption. After recovering the changes, you still need to **manually** save the scenario.&#x20;
:::

### Retrieve unsaved changes from blueprint

To retrieve unsaved changes from an automatically saved blueprint:

:::::WorkflowBlock
::::WorkflowBlockItem
Open the scenario.

:::hint{type="info"}
If it's a new scenario that has never been saved, click **+Create scenario.**
:::
::::

:::WorkflowBlockItem
If unsaved changes are detected, a dialog window will appear displaying: &#x20;

- A list of changes
- A scenario preview
- The date of the latest blueprint version&#x20;
:::

:::WorkflowBlockItem
Click **Recover**.&#x20;

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/-m6aBSS0rtdls_wmzaRoK-20260313-160421.png)
:::

:::WorkflowBlockItem
A confirmation message will appear in the bottom-right corner.
:::

:::WorkflowBlockItem
Click **Save** in the Scenario toolbar to keep the recovered changes.
:::
:::::

Your recovered scenario will be saved. You can access it in the **Version** **history**.&#x20;

### Restore a recovered scenario from Version history

:::hint{type="warning"}
If you close the scenario recovery dialog or click **Not** **now:**

- The recovered blueprint remains temporarily available in the Version history.&#x20;
- It will be permanently deleted once you manually save a new scenario version.

If you continue editing without saving the recovered scenario and another interruption occurs, a new blueprint will overwrite the previous one.

To avoid losing your changes, recover and save the scenario as soon as you reopen it.
:::

To restore a recovered version from the Version history:

::::WorkflowBlock
:::WorkflowBlockItem
Click the **V****ersion history** icon in the Scenario toolbar.
:::

:::WorkflowBlockItem
In the **Versions** field, select the latest version marked as `Recovered`.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/EYssizqfhOfsLXv7OUzao-20260316-154234.png" size="50" width="1059" height="771" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
Click **Restore version**.
:::

:::WorkflowBlockItem
Click the **Save** icon to save the scenario from the recovered version.
:::
::::

Your recovered scenario will be saved. You can access it in the **Version** **history**.&#x20;

:::hint{type="warning"}
Always save the scenario after restoring a recovered version. Otherwise, you can lose all the recovered changes.&#x20;
:::
