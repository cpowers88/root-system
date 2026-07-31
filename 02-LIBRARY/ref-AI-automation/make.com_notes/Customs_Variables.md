---
type: reference
timeline: reference
status: source-capture
title: Custom variables
slug: custom-variables
docTags: 
createdAt: 2025-05-28T07:31:15.342Z
---

::embed[]{url="https://youtu.be/YF4qYcMfLQc"}

Custom variables are similar to [scenario variables](docId\:xheAxlxyiFE-v0oSUxxpE), but they are defined at the organization or team level.

## Use custom variables when you need:

- Data shared across multiple scenarios&#x20;
- Settings that control how scenarios behave (for example, TestMode = true/false)
- Values that persist between scenario runs
- Team or organization-wide configuration values

:::hint{type="info"}
Custom variables are available only on Pro, Teams, and Enterprise pricing plans. See [Make pricing](https://www.make.com/en/pricing) for more information.
:::



For each variable, you need to identify the:

- **Name** (permanent variable name)
- **Data type** (text, number, Boolean, or date)
- **Value** (the actual value of the variable)

Here are some situations for which you might use custom variables:

- Keep track of a value between multiple scenario executions
- Share a value between different scenarios&#x20;
- Set a global variable that various scenarios leverage. For example `TestMode = true/false` so the scenario routes differently according to the value.
- Change the behavior of a scenario without modifying the scenario blueprint. For example, `myLimit=20` set as a custom variable in the Limit field of a module.

:::hint{type="warning"}
Variables are not meant to store secrets. Don’t use them for anything sensitive!

Variable values are not encrypted as they are stored in plain text. Don’t use variables to store passwords or any other sensitive data. Be aware that other team members and organization admins can access all custom variables.
:::

:::::ExpandableHeading
## Create a custom variable

You can create custom variables at the organization level and at the team level.

::::WorkflowBlock
:::WorkflowBlockItem
Decide if you want to create an organization variable or a team variable. 

- For organization variables, go to the organization dashboard and click **Org Variables > Add organization variable**.
- For team variables, go to the team dashboard and click **Team Variables > Add team variable**.
:::

:::WorkflowBlockItem
Fill in the following information:

| **Field**     | **Description**                                                                                                                                                                                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**      | - This field is mandatory and you cannot change it after you save it.
- The name is the identifier of the variable.
- The name must contain only letters, digits, or the symbols $ and \_.
- The name cannot start with a digit.
- The name must contain a maximum of 128 characters. |
| **Data type** | Choose the variable data type from the dropdown menu<br />- Number
- Text
- Boolean
- Date                                                                                                                                                                                            |
| **Value**     | * Enter the value for your variable.
* You can use letters, digits, spaces, and special characters.
* Value cannot be empty.                                                                                                                                                          |
:::

:::WorkflowBlockItem
Click **Save** to save your custom variable.
:::
::::

Your new variable will appear in the list of variables. Click the scenarios icon to see a list of scenarios using the custom variable.

![Usage of a custom variable in a scenario](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/XFzTBc-zqZfSAgR6OdyqW-20260316-113448.png)

To preview the variable value, hover over the individual value field.

![Preview variable value](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/sSplZad7fcVAGvcJwJlGt_uuid-be2168f3-43b9-8e67-f571-98acc55cb92d.png)
:::::

:::::ExpandableHeading
## Edit a custom variable

:::hint{type="warning"}
If your other team members or organization admins use the same variable in their scenarios, the changes will affect them too.
:::

::::WorkflowBlock
:::WorkflowBlockItem
Go to the variable you want to edit.

- For organization variables, go to the organization dashboard and click **Variables**.
- For team variables, go to the team dashboard and click **Variables**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/Sw7hlnJFiOAmA_SNthxsF_uuid-9aa620f5-93e1-2e75-f40f-d40d8d3f367c.png" size="80" width="2792" height="866" position="flex-start" alt="Organization variables" showCaption="false"}
:::

:::WorkflowBlockItem
In the list of your custom variables, find the one you want to edit and click **Edit** next to it.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/_LxOWDd6e0-n0leVNvRZF_uuid-649fa07f-5cc6-a3ca-2965-1a037be80585.png" size="80" width="2248" height="754" position="flex-start" alt="Edit a custom variable" showCaption="false"}
:::

:::WorkflowBlockItem
Edit the variable as needed. You can edit the variable data type and value. You can't edit the name.
:::

:::WorkflowBlockItem
Click **Save** to save your changes.
:::
::::

Your changes are saved and your updated variable will appear on the list of variables. Hover over the individual value field to preview the variable value.

The changes automatically update in the scenarios that already use the variable.

:::hint{type="info"}
The value of a custom variable can be changed within a scenarioas well. The value changes only **after** the scenario finishes running. The new value is available for the next run of the scenario for everyone in the organization or team.
:::
:::::

::::::ExpandableHeading
## Delete a custom variable

:::hint{type="warning"}
Deleting a variable that you already use in one or more scenarios can affect other users who use the same variable in their scenarios. After you delete a variable, the variable becomes inactive in all scenarios where it is used and it stops returning expected values.
:::

:::::WorkflowBlock
:::WorkflowBlockItem
Decide if you want to delete an organization variable or a team variable.

- For organization variables, go to the organization dashboard and click **Variables**.
- For team variables, go to the team dashboard and click **Variables**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/Sw7hlnJFiOAmA_SNthxsF_uuid-9aa620f5-93e1-2e75-f40f-d40d8d3f367c.png" size="80" width="2792" height="866" position="flex-start" alt="Organization variables" showCaption="false"}
:::

:::WorkflowBlockItem
In the list of your custom variables find the one you want to delete and click **Delete&#x20;**&#x6E;ext to it.

![Delete a custom variable](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/a9rv3DYO_7AZZ9KyBcQf2_uuid-937365c7-46ad-aaa5-a44d-bf6e8f36eb13.png "Delete_a_custom_variable_.png")
:::

::::WorkflowBlockItem
Clic&#x6B;**&#x20;OK** to confirm that you want to delete the variable.&#x20;

:::hint{type="warning"}
If the custom variable you are deleting is already used, you will see a pop-up that lists all scenarios that will be impacted. If you still want to delete it, click **OK**.
:::
::::
:::::

The variable is deleted and disappears from your list of custom variables.
::::::

:::::ExpandableHeading
## Check custom variable history

You can see who changed the custom variable, when, and what the changes are.

::::WorkflowBlock
:::WorkflowBlockItem
Go to the custom variable whose history you want to check.

- For organization variables, go to the organization dashboard and click **Variables**.
- For team variables, go to the team dashboard and click **Variables**.
:::

:::WorkflowBlockItem
Click the dropdown menu next to **Edit**. Select **Show history**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/QqjNTbNk_9BJuuBmhxDwy_uuid-3a08debe-c15d-3c76-aace-5baa64271b62.png" size="80" width="1262" height="625" position="flex-start" alt="Variable history" showCaption="false"}
:::
::::

A new window opens where you can see the variable history. The last change appears on the top.
:::::

:::ExpandableHeading
## User permissions for custom variables

**Organization variables**

|                                                   | **Owner** | **Admin** | **Member** | **Accountant** | **App Developer** |
| ------------------------------------------------- | --------- | --------- | ---------- | -------------- | ----------------- |
| **Can access organization variables**             | X         | X         | X          |                | X                 |
| **Can edit&#x20;**&#xA;**organization variables** | X         | X         |            |                |                   |
| **Can add&#x20;**&#xA;**organization variables**  | X         | X         |            |                |                   |
| **Can delete organization variables**             | X         | X         |            |                |                   |

**Team variables**

|                               | **Team Admin** | **Team Member** | **Team Monitoring** | **Team Operator** | **Team Restricted Member** |
| ----------------------------- | -------------- | --------------- | ------------------- | ----------------- | -------------------------- |
| **Can access team variables** | X              | X               |                     | X                 | X                          |
| **Can add team variables**    | X              | X               |                     |                   | X                          |
| **Can edit team variables**   | X              | X               |                     |                   | X                          |
| **Can delete team variables** | X              | X               |                     |                   | X                          |
:::

:::::ExpandableHeading
## Example: Use a custom variable to control a scenario

You can use a custom variable at the organization or team level to easily switch the value and control how a scenarioworks. Here, a custom variable called `debugMode` is boolean, and if the value is `true` an email will be sent to a team member. If you change the value to `false` at the team level, the scenario will end after adding a row to the Google Sheets document.&#x20;

![Custom variable scenario example](https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-0RMLHlJimsf2Wky8UYh1r-20250617-084713.png)

::::WorkflowBlock
:::WorkflowBlockItem
Decide if you want to create an organization variable or a team variable.

- For organization variables, go to the organization dashboard and click **Variables > Add organization variable**.
- For team variables, go to the team dashboard and click **Variables > Add team variable**.

In this example, we are using a team variable.
:::

:::WorkflowBlockItem
Enter your variable **Name**, **Data type**, and **Value**.

**Name:** debugMode

**Data type:** boolean

**Value:** Yes

Click **Save** to save your custom variable.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-HazvNPMejaof-Z8-BnLJw-20250617-084350.png" size="64" width="497" height="481" position="flex-start" alt="custom variable" showCaption="false"}
:::

:::WorkflowBlockItem
In your scenario, add a **Tools > Set variable** module.&#x20;

Set the **Variable name** to `city` and the **Variable value** to `Madrid`.

Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-DqxgjWG2V5IGQMKHJiVET-20250617-085014.png" size="72" width="698" height="364" position="flex-start" alt="Set city variable" showCaption="false"}
:::

:::WorkflowBlockItem
Add a **Weather > Get current weather&#x20;**&#x6D;odule.

In the **I want to enter a location by** field, select `cities`.

In the **City** field, map the value to the `city` variable that you set in step 3.

Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-IX7qNS0yDENePw7GKuSCS-20250617-085651.png" size="80" width="807" height="337" position="flex-start" alt="Weather, set location" showCaption="false"}
:::

:::WorkflowBlockItem
Add a **Google Sheets > Add a row** module and create a connection.

In this example, we have a Google Sheets document called **Weather report** saved in **My Drive**. This file has headers for the **date**, **city**, **average temp**, **status**, and **description**.

Connect to this file and map values as shown:

| **Field**    | **Mapped value**                |
| ------------ | ------------------------------- |
| date         | formatDate(now; "DD-MM-YYYY")   |
| city         | Scenario variable `city`        |
| average temp | Weather app value `Temperature` |
| status       | Weather app value `Status`      |
| description  | Weather app value `Description` |

Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-VoQ6hXm33LbPO9xO0-njy-20250617-085949.png" size="78" width="716" height="1115" position="flex-start" alt="Map values to the Google Sheet document" showCaption="false"}
:::

:::WorkflowBlockItem
Add an **Email > Send an Email to a Team Member** module and create a connection.

In the **To** field, select the member of your team you want to send the email to.

In the **Subject** field, enter a relevant subject.

In the **Content&#x20;**&#x66;ield, enter the text of your email, mapping the information you want to share with your team member. You can use HTML tags.

Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-kl0TKIbuE8qBAC6U93HFV-20250617-090231.png" size="70" width="448" height="844" position="flex-start" alt="Send email if filter is true" showCaption="false"}
:::

:::WorkflowBlockItem
In your scenario, between the **Google Sheets** and **Email** modules, click the **wrench icon** to set up a filter.

**Label:** Debug mode?

**Condition:&#x20;**&#x4D;ap the condition to the `debugMode` custom variable.

Change the operator to **Boolean operators: Equal to** and enter `true` in the field.

Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-1vdyNQYWQEYxTHdO1uqtt-20250617-090525.png" size="68" width="450" height="405" position="flex-start" alt="Debug filter" showCaption="false"}
:::

:::WorkflowBlockItem
Click the save icon to save your scenario and click **Run once** to test.
:::
::::

If your custom variable value is `yes`, an email is sent to your team member.

![Custom variable email example](https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-j_yvnMTfJp1abCZoZs2_u-20250617-094226.png)

If the custom variable value is `no`, the email is not sent after the weather information is stored in the Google Sheets document.
:::::
