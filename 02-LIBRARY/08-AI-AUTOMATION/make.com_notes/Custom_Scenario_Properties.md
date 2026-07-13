---
title: Custom scenario properties
slug: custom-scenario-properties
description: Add custom properties to organize, sort, and filter your scenarios in a table view
image: https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/G4hKz2K12PqwWjnoUlmms_domino-zoomin-purple-a-1.png
docTags: 
createdAt: 2025-02-03T13:29:15.599Z
---

:::hint{type="info"}
This feature is available to Enterprise customers.
:::

To help organize and sort scenarios, you can use custom scenario properties to add customizable metadata. The properties you create appear on the scenario detail page and also in sortable columns in a table view of your scenario. You can add as many custom properties as you like and edit which properties appear in your table view.

All organization members can view and use custom scenario properties. This includes using custom properties to filter the table view of scenarios.

For all properties, you can define the following:

- **Name** - a descriptive name used as a unique identifier that only appears when you manage your custom properties.
- **Label** - the name visible on the table view and detail page.
- **Hint text** - a short message you add to help your organization members use your custom property.
- **Field type** - the property type. For example, dropdown or boolean.
- **Required** - select **Yes** to make a property mandatory to include when applying custom properties to a scenario.

Custom scenario properties support the following field types:

- **Short text** - up to 200 characters; useful for email addresses and URLs.
- **Long text** - up to 1,000 characters; supports multiple lines.
- **Number** - supports integers.
- **Boolean** - a yes/no value that appears as radio buttons.
- **Date** - date and time according to [ISO 8601.](https://en.wikipedia.org/wiki/ISO_8601)
- **Dropdown** - a list of items where users can select only one.
- **Multichoice** - a list of items where users can select multiple values.

## Create custom properties

Your organization dashboard has a **Scenario properties** tab where you can create and manage your custom properties.

::::WorkflowBlock
:::WorkflowBlockItem
In the left sidebar, click **Org**.
:::

:::WorkflowBlockItem
Switch to the **Scenario properties** tab.
:::

:::WorkflowBlockItem
Click **+Add property**.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/zbnyDTSnaU_G6W33WIvvq-20251006-121758.png)
:::

:::WorkflowBlockItem
In the **Add custom property** dialog box, enter and select your information for each field. Click **Save** to create your custom property.

::Image[]{src="https://app.archbee.com/api/optimize/oAyFj2GHlBeBVWF5OAir2/8cQHVIWkk7pK-Q8yAfnUg-20251006-121833.png" size="50" width="878" height="1284" position="center" showCaption="false"}
:::
::::

Your custom property appears on the list on the **Scenario properties** tab.

:::hint{type="info"}
Only organization owners and admins can create and manage custom properties.
:::

## Use custom Make properties

All organization members can:

- Apply and edit custom properties to Make.
- Use custom properties to filter and sort the Make list.

### Apply and edit custom scenario properties

::::WorkflowBlock
:::WorkflowBlockItem
In the left sidebar, click **Scenarios**.
:::

:::WorkflowBlockItem
Click the three dots next to the scenario whose custom properties you want to edit.
:::

:::WorkflowBlockItem
Select **Edit custom properties**.

::Image[]{src="https://app.archbee.com/api/optimize/oAyFj2GHlBeBVWF5OAir2/QaRvPuVmVBEnuVk7EjJQ4-20251006-122355.png" size="80" width="2650" height="828" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
In the dialog box, edit your scenario properties
:::

:::WorkflowBlockItem
Click **Save**.
:::
::::

:::hint{type="info"}
You can also apply and edit custom properties from the scenario detail page.
:::

### Filter the scenario list&#x20;

::::WorkflowBlock
:::WorkflowBlockItem
In the left sidebar, click **Scenarios**.
:::

:::WorkflowBlockItem
Click **Table** to switch to the table view.

::Image[]{src="https://app.archbee.com/api/optimize/oAyFj2GHlBeBVWF5OAir2/njp2_c-6jqhDyNFx2VBq7-20251006-122713.png" size="78" width="2068" height="252" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
Click the icon next to the **Filter**, and select the properties you want to see in the table.

::Image[]{src="https://app.archbee.com/api/optimize/oAyFj2GHlBeBVWF5OAir2/cZWBZykhM9Rxw0WcVRVWC-20251006-123003.png" size="30" width="556" height="846" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
Click **Apply**.
:::
::::

### Sort the scenario list

By default, scenarios are sorted by their names in alphabetical order, with active scenarios at the top of the list. However, it is possible to change the sorting in both the List and Table views.

From the List view:

::::WorkflowBlock
:::WorkflowBlockItem
In the left sidebar, click **Scenarios**.
:::

:::WorkflowBlockItem
Click the **Sort by** button.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/sg7zl4smCS_geEdqWxG4I-20251006-123926.png)
:::

:::WorkflowBlockItem
Select a sorting option. You can sort scenarios by their name or creation date.
:::
::::

From the Table view:

::::WorkflowBlock
:::WorkflowBlockItem
In the left sidebar, click **Scenarios**.
:::

:::WorkflowBlockItem
Click **Table** to switch to the table view.
:::

:::WorkflowBlockItem
Click the title header of a column to sort the list by that property. Click again to see a descending order list.
:::
::::

## Manage custom properties

You can edit or delete your custom scenario properties from the **Scenario properties** tab of your organization dashboard.

### Edit custom properties

::::WorkflowBlock
:::WorkflowBlockItem
In the left sidebar, click **Org**.
:::

:::WorkflowBlockItem
Switch to the **Scenario properties** tab.
:::

:::WorkflowBlockItem
Find the custom property you want to edit and click **Edit.**
:::

:::WorkflowBlockItem
In the dialog box, change the information as needed.
:::

:::WorkflowBlockItem
Click **Save**.
:::
::::

A confirmation message appears at the bottom of the screen and your changes appear in the table.

### Delete a custom property

::::WorkflowBlock
:::WorkflowBlockItem
In the left sidebar, click **Org**.
:::

:::WorkflowBlockItem
Switch to the **Scenario properties** tab.
:::

:::WorkflowBlockItem
Find the custom property you want to delete and click the down arrow icon.
:::

:::WorkflowBlockItem
Click **Delete**.
:::
::::

The property disappears from the table.