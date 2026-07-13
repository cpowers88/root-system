---
title: Scenario variables
slug: scenario-variables
docTags: 
createdAt: 2025-05-28T07:29:41.740Z
---

**Scenario variables are useful when you need to reuse the same information multiple times. They make scenarios easier to manage and maintain.&#x20;

## Use scenario variables when you need:

- Temporary data that only exists during one scenario run
- To pass information between modules in the same scenario&#x20;
- Data that doesn't need to persist after the scenario completes
- Simple counters or flags within a single scenario run

To use scenario variables, use the **Set variable** or **Set multiple variable** tools in your scenario.

If you need to access the defined variable(s) in a different route than where they were set, use the **Get Variable** or **Get Multiple Variable** tools.

## Create a scenario variable

You can create scenario variables in your scenario.

:::::WorkflowBlock
::::WorkflowBlockItem
Click the **Tool** icon on the Scenario Builder toolbar to select the **Set variable** tool.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-rkQcxfJghBuZXk7lIFP9n-20250610-113901.png" size="52" width="448" height="593" position="flex-start" alt="Set variable" showCaption="false"}

You can also click the giant plus in your canvas to select **Tools \< Set variable**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-WmPOOrQlVP_n4Dp8QFjjf-20250610-114136.png" size="68" width="706" height="554" position="flex-start" alt="Set variable" showCaption="false"}

:::hint{type="info"}
To set multiple variables at once, select the **Set multiple variables** tool.
:::
::::

:::WorkflowBlockItem
Fill in the following information:

| **Field**             | **Description**                                                                                     |
| --------------------- | --------------------------------------------------------------------------------------------------- |
| **Variable name**     | - This field is mandatory.
- The name is the identifier of the variable.                            |
| **Variable value**    | * Enter the value for your variable.
* You can use letters, digits, spaces, and special characters. |
| **Variable lifetime** | Select the lifetime of your variable:<br />* One cycle
* One execution                              |

If you are using the **Set multiple variables** tool, repeat this for each variable.
:::

:::WorkflowBlockItem
Click **Save** to save your variable.
:::
:::::

::::::ExpandableHeading
## Example: Send an email with weather conditions for a selected city

In this example, we use the **Set variable** module to select a city, retrieve weather information for the city, and use the **Set multiple variables** and **Get multiple variables** modules to send the information in an email to a team member.

![Scenario variables example](https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-LAN_DOvHPVRRkaOmnzyyq-20250613-100249.png)

:::::WorkflowBlock
:::WorkflowBlockItem
In your scenario, click the **Tool** icon on the Scenario Builder toolbar to select the **Set variable** tool.

You can also click the giant plus in your canvas to select **Tools \< Set variable**.
:::

:::WorkflowBlockItem
In the **Variable name** field, enter `City`.

For this example, we have set the **Variable value** to `Paris`.

Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-xwltSHLrnuTKh1mSWO0cH-20250613-122950.png" size="60" width="448" height="283" position="flex-start" alt="Set variable - City" showCaption="false"}
:::

:::WorkflowBlockItem
Add a **Router**.
:::

:::WorkflowBlockItem
In the first route at the top, add a **Weather** module.

In the **I want to enter a location by** field, select `cities`.

In the **City** field, map the value to the `City variable` that you set in step 1.

Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-rLGQ50RzDZKUs_R_HHdeg-20250613-123355.png" size="78" width="805" height="309" position="flex-start" alt="Weather module" showCaption="false"}
:::

:::WorkflowBlockItem
After the **Weather** module in the first route, add a **Set multiple variables** module.

Add two variables:

- `status` - mapped to the `Status` value from the Weather module.
- `description` - mapped ot the `Description` value from the Weather module.

Click **Save.**

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-fZOk8tNxXpXhE5WjqBWeK-20250613-123755.png" size="60" width="448" height="609" position="flex-start" alt="Set multiple variables" showCaption="false"}
:::

::::WorkflowBlockItem
In the second route at the bottom, add a **Get multiple variables** module to retrieve the information from the previously set variables.

For **Variable name 1**, enter `status`.

For **Variable name 2**, enter `description`.

Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-6zwZDS5jq-PFKEaqeNi3P-20250613-124104.png" size="70" width="789" height="387" position="flex-start" alt="Get multiple variables" showCaption="false"}

:::hint{type="info"}
Note that this step is not necessary if you are not using a router.&#x20;

In this example, we've chosen to split the scenario into two routes to demonstrate both the **Set mutliple variables** and **Get multiple variables** modules.
:::
::::

:::WorkflowBlockItem
After the **Get multiple variables** module in the second route, add an **Email > Send an Email to a Team Member&#x20;**&#x6D;odule and **Create a connection**.

In the **To** field, select the member of your team you want to send the email to.

In the **Subject** field, enter a relevant subject.

In the **Content** field, enter the text of your email, mapping the `City`, `status`, and `description` variables. You can use HTML tags.

Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-zLjNKS7k8U5HrNLV-5d8K-20250613-124852.png" size="74" width="743" height="539" position="flex-start" alt="Send email" showCaption="false"}
:::

:::WorkflowBlockItem
Click **Run once** to test your scenario.
:::
:::::

The person you selected in the Email module receives an email like this:

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-8mnNqCgk2VyW-DiQiQThV-20250613-125224.png" size="70" width="714" height="524" position="flex-start" alt="Weather scenario email" showCaption="false"}
::::::
