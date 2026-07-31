---
type: reference
timeline: reference
status: source-capture
title: Create the structure of scenario inputs or outputs
slug: create-the-structure-of-scenario-inputs-or-outputs
docTags: 
createdAt: 2025-04-08T07:50:05.518Z
---

Before using scenario inputs or scenario outputs, you need to define their structure. When creating the scenario input structure, you can set any parameter as required, which allows you to validate the structure of the input data.

You can also add a description to each input parameter to document the data the parameter contains.

You can add scenario inputs and outputs anytime. To do that:

:::::WorkflowBlock
:::WorkflowBlockItem
In the Scenario Builder, click the scenario inputs and outputs icon.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/hyWBQlny5zwsCdVR280TI-20260513-070958.png)
:::

:::WorkflowBlockItem
Select the **Scenario inputs** or **Scenario outputs** tab and click **Add item**.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/CzXDATvPiBvFH4yyYJ2Qz-20260513-072442.png)
:::

::::WorkflowBlockItem
In the **Name** field, enter the name of the input or output item. This field is mandatory.

:::hint{type="warning"}
You can't use spaces or special characters in the name. You can use letters, numbers, and the underscore symbol. You can not start with a number or an underscore followed by a number.
:::
::::

:::WorkflowBlockItem
Optional: In the **Description** field, add information about the input or output item. For example, how it is used in the scenario or what information it contains.
:::

:::WorkflowBlockItem
In the **Type** field, select the [type of scenario input or output](https://help.make.com/scenario-inputs-and-outputs#scenario-input-and-output-types) from the dropdown menu. This field is also mandatory.

- If you use the type **Array**, set the type of the array items in the nested **Type** field.
- If you use the type **Collection**, you can set the structure of the collection in the **Specification** field. Make validates the input data against the specification. If you keep the **Specification** empty, Make will accept any collection for the input data.
- If you use the type **Select**, add options for the dropdown selection in the **Options** field.
- If you use the type **Dynamic collection**, you can map a collection or a JSON string to the output field. The **Return output** module parses the JSON and returns it as output bundles. You can use the **Create JSON** module to create a custom data output.
:::

:::WorkflowBlockItem
Optional: In the **Default** field, enter the default value that is used if the value is missing in the original input.
:::

:::WorkflowBlockItem
Under **Required**, select whether this input is required or not to start your scenario.
:::

:::WorkflowBlockItem
Under **Multi-line**, select how you want your text to be displayed if you selected **Text**, **Array**, **Collection** or **JSON** as the item data typ&#x65;**.**

Selecting **Yes** shows multiple lines of text. Selecting **No** shows only one line of text.
:::

:::WorkflowBlockItem
Repeat the process if you need to add more items.
:::

:::WorkflowBlockItem
Click **Save&#x20;**&#x69;n th&#x65;**&#x20;Scenario inputs&#x20;**&#x62;ox and save your scenario.&#x20;
:::
:::::

To work with scenario inputs, you should use the **Scenarios** > **Start scenario&#x20;**&#x6D;odule. To work with scenario outputs, you should use the **Scenarios** > **Return output** module.&#x20;
