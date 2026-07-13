---
title: Subscenarios
slug: subscenarios
description: Build scenario chains to run complex workflows in sequence and transfer data
image: https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/lF-xpvmPXszvfgMC9FdFg_domino-zoomin-purple-a-1.png
docTags: 
createdAt: 2026-03-04T08:34:37.062Z
---

In Make, you can build an automation using a parent scenario and one or more subscenarios.&#x20;

- A parent scenario is the main scenario that triggers one or more subscenarios via the [Scenarios > Call a scenario ](https://apps.make.com/scenario-service#call-a-scenario)module.
- A subscenario is a scenario triggered by a parent scenario or other sources, such as an AI agent, an MCP client, or an API call. &#x20;

A parent scenario can include multipl&#x65;**&#x20;Scenarios >** **Call a scenario** modules to trigger different subscenarios. A subscenario can also act as a parent scenario and trigger other subscenarios through the **Scenarios >** **Call a scenario&#x20;**&#x6D;odule.&#x20;

## Benefits of subscenarios

Subscenarios help you to:

- **Simplify complex workflows**: Break down large scenarios into smaller, manageable components that are easier to build, maintain, and troubleshoot.

:::Paragraph{indent="1"}
For example, instead of building a single scenario with dozens of routes to handle lead creation, checking companies, contacts, campaigns, and affiliates, you can split each task into its own subscenario. The parent scenario stays clean and readable, while each subscenario handles one thing well.
:::

- **Save time by reusing logic:** Use the same subscenario across different parent scenarios instead of recreating modules.

:::Paragraph{indent="1"}
For example, if multiple scenarios need to update your product inventory, new orders, returns, B2B deliveries, you can build one inventory subscenario and call it from all of them. Update the logic once, and all parent scenarios benefit automatically.
:::

- **Extend automation to AI agents and MCP servers**: Use scenarios as callable tools in agent workflows.

:::Paragraph{indent="1"}
For example, you can expose a subscenario as a tool that an AI agent calls when it needs to look up a customer record, send a notification, or trigger an action in an external app, without the agent needing to know how the underlying automation works.
:::

- **Transfer data more easily:** Pass a clearly defined structure of inputs and outputs between scenarios.

:::Paragraph{indent="1"}
For example, you can send a customer’s email as an input to a subscenario. It checks whether they’re already registered, then returns a status as an output that the parent uses to decide whether to send a welcome email. If you call a scenario using the **Webhooks** app, you don't have the in-built capability to define the inputs you want to pass from the parent scenario and the outputs you want to receive from the subscenario
:::

- **Reduce credit usage:&#x20;**&#x53;cenarios run via the **Scenarios** app don't consume credits.

:::Paragraph{indent="1"}
For example, if you call a scenario using the **Webhooks** and **Make** apps, each operation will consume credits. With the Scenarios app, you can call scenarios, pass the inputs, and return outputs free of charge. &#x20;
:::

## Limitations of subscenarios

Although subscenarios offer multiple benefits, they also have certain limitations. You can only call a scenario created in your team. If you want to call a scenario from another team or organization, you have to use one of these modules:

- **Make > Run a scenario**
- **Webhooks > Custom webhook&#x20;**

## Calling modes for subscenarios

Subscenarios can run in two modes that define how the parent scenario and the subscenario interact. They can follow:

- Synchronous execution &#x20;
- Asynchronous execution

The mode depends on whether the parent scenario needs the subscenario´s results to continue the run.

### **Synchronous execution&#x20;**

In synchronous mode:

- The parent scenario calls the subscenario via the **Scenarios >** **Call a scenario&#x20;**&#x6D;odule, passes scenario inputs, and pauses execution until the subscenario completes.&#x20;
- The subscenario starts running with the **Scenarios >** **Start scenario&#x20;**&#x6D;odule, processes the inputs, and returns outputs to the parent scenario via the **Scenarios >** **Return****&#x20;outputs&#x20;**&#x6D;odule.
- Once the parent scenario receives the outputs, it resumes execution.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/E0Rg9YoUtfKIKWMF7lHXm-20260225-102438.png" size="70" width="5856" height="3384" position="center" darkWidth="5856" darkHeight="3384" showCaption="false" indent="2"}

### **Asynchronous execution**

In asynchronous mode:

- The parent scenario calls the subscenario via **Scenarios >** **Call a scenario&#x20;**&#x6D;odule, and continues immediately without waiting for outputs.&#x20;
- The subscenario starts running with **Scenarios >** **Start scenario&#x20;**&#x6D;odule and completes its operations independently.&#x20;

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/WA3LfkRSBjs1qFnxrdMQF-20260225-102507.png" size="70" width="6452" height="3284" position="center" darkWidth="6452" darkHeight="3284" showCaption="false" indent="2"}

A parent scenario can also call multiple subscenarios that run in different modes.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/GU9xcFHGs3NjFP6tiEDts-20260305-110530.png)

## Create a parent scenario with subscenarios

To build an automation with subscenarios, you need to:

- Create a parent scenario
- Create one or more subscenarios that this parent scenario will call
- Link them with th&#x65;**&#x20;Scenarios >** **Call a scenario**/**Scenarios >** **Start scenario** modules

&#x20;Let's look at this basic workflow as an example and walk through each step afterward.&#x20;

:::hint{type="info"}
**A parent scenario:**

- The parent scenario receives the data from the **Jotform > Watch for Submissions.**

**A&#x20;****subscenario with s****ynchronous execution:**

- The parent scenario sends the data to the subscenario and waits for the output.
- The subscenario checks if the email from the event registration form already exists in the database using the **Google Sheets > Search Rows&#x20;**&#x6D;odule.
- A **Router** handles two possible outcomes:&#x20;
  - **Email doesn't exist**: The participant is added to the database via the **Google Sheets > Add Rows&#x20;**&#x6D;odule. The subscenario sends a confirmation and the data back to the parent scenario via **Scenarios > Return output&#x20;**&#x6D;odule.&#x20;
  - **Email already exists**: The subscenario sends a notification back to the parent scenario via the **Scenarios > Return output&#x20;**&#x6D;odule. &#x20;
- After the parent scenario receives confirmation that the email has been added, it sends a welcome email to the participant via the **Gmail > Send an email module**.&#x20;

**A****&#x20;subscenario with as****ynchronous execution:**

- The parent scenario sends the data to the subscenario and immediately proceeds to send a welcome email to the participant without waiting for the outputs.
- The subscenario stores the participant's data in the database and completes.&#x20;
:::

### Create a parent scenario&#x20;

To create a parent scenario:

:::::WorkflowBlock
:::WorkflowBlockItem
In Make, click **+Create a new scenario**.
:::

:::WorkflowBlockItem
In the Scenario Builder, click the big plus icon and add the **Jotform > Watch for Submissions** module.
:::

:::WorkflowBlockItem
In the **Webhook** field, click **Add** to create a webhook.
:::

:::WorkflowBlockItem
In the **Create a webhook** window:

- In the **Webhook** **name** field, enter the webhook's name.
- In the **Connection** field, select a connection or create a new one.
- In the **Team** field, select the Jotform team.
- In the **Form** field, select the form that collects event registrations.&#x20;
- Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/DVyl0g4YEKYP_ohDvETXn-20260219-105913.png" size="70" width="1846" height="884" position="center" darkWidth="1846" darkHeight="884" showCaption="false" indent="2"}
:::

:::WorkflowBlockItem
Click **Save** to save the module settings.&#x20;
:::

:::WorkflowBlockItem
Click the plus icon next to the **Jotform > Watch for Submissions** module and add the **Scenarios >** **Call a scenario&#x20;**&#x6D;odule.
:::

::::WorkflowBlockItem
In the **Scenario** field, click **+Create scenario**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/leLwUOvtTJ9sMEnJSJlAf-20260206-152304.png" size="50" width="1160" height="940" position="center" darkWidth="1160" darkHeight="940" showCaption="false"}

:::hint{type="info"}
You can also select an existing scenario from the list. In this case, make sure that the scenario you select as a subscenario is **active** and scheduled to run **on demand**.&#x20;

Additionally:

- Use th&#x65;**&#x20;Scenarios > Start a scenario** module to start a subscenario
- Define scenario inputs
- Define scenario outputs if the parent scenario expects them
- Use **Scenarios > Return output** module if the parent scenario expects outputs
:::
::::
:::::

After this, you'll be redirected to the Scenario Builder. There, you can create and configure your subscenario based on whether you want synchronous or asynchronous execution.&#x20;

### Create a subscenario with s**ynchronous execution&#x20;**

After clicking **Create a scenario** in the **Scenarios >** **Call a scenario** module, you can configure your subscenario. To do that:

:::::WorkflowBlock
::::WorkflowBlockItem
In the **Create a scenario** window:

- In the **Name** field, enter the subscenario name.
- Optionally, in the **Description name** field, add a description.
- Define the input and output structure.

In our example, the parent scenario receives the **Name** and the **Email** from the **Jotform > Watch for Submissions&#x20;**&#x6D;odule and passes this data to the subscenario. Therefore, we create two scenario inputs: `name` and `email`.

For outputs, we want to return the participant's registration status together with the name and email, so we create three outputs: `status`, `name`, and `email`.

- Click **Create** **scenario**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/ejf0xxT9HNoNX90YD53vG-20260206-152332.png" size="30" width="714" height="1382" position="center" showCaption="false"}

:::hint{type="warning"}
You can see scenario inputs and outputs in the subscenario.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/KDhUGaIYIPjOCbX72rjkT-20260305-141055.png" size="40" width="662" height="610" position="center" showCaption="false"}

It is important to define the [structure of scenario inputs and outputs ](https://help.make.com/create-the-structure-of-scenario-inputs-or-outputs)accurately to ensure data passes without errors.&#x20;
:::
::::

:::WorkflowBlockItem
You will see a scenario diagram with two automatically added modules: **Scenarios >** **Start scenario&#x20;**&#x61;nd **Scenarios >** **Return****&#x20;outputs**. To add modules to your subscenario, click the big + icon between the modules.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/aY8RsLv5f8L2ikYj1f4Yg-20260305-130333.png" size="70" width="1770" height="868" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
Add the **Google Sheets > Search Rows&#x20;**&#x6D;odule to check whether the email already exists in your database. In the module settings:

- Select the spreadsheet and sheet where registrations are stored.
- In the **Filter** field:
  - Select the Google Sheet's column that contains emails.
  - Set the **Text operators:** **Equal to**.&#x20;
  - Map the `email` from **Scenarios > Start scenario** module.
- Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/qQ_rgXGLuy-zaOCaYP06K-20260219-114544.png" size="52" width="1590" height="1388" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
Add a **Router&#x20;**&#x74;hat will handle two possible routes.
:::

:::WorkflowBlockItem
The first route will run if the email from the registration form **doesn't exist** in the database. To configure the filter, right-click the dots between the modules and select **Set up a filter**.&#x20;

Set the **Condition** as follows: &#x20;

- Map `Total number of bundles` from the **Google Sheets > Search Rows** module.
- Select **Numeric operators: Equal to**
- Enter **0**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/8kmsml9OhcvEFmkBxfkcV-20260223-103542.png" size="50" width="1258" height="956" position="center" showCaption="false" indent="2"}
:::

:::WorkflowBlockItem
Add the **Google Sheets > Add a Row&#x20;**&#x6D;odule to store the email and the name from the registration form. In the module settings:

- Select the spreadsheet and sheet where registrations are stored.
- Map `name` and `email` values from the **Scenarios > Start scenario** module.
- Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/qQEYAPR0Nq_JlYkGHbcjw-20260219-125954.png" size="50" width="1028" height="1394" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
Click the **Scenarios > Return output** module after the **Google Sheets > Add a Row&#x20;**&#x6D;odule. You will see the output fields you defined when creating a subscenario:

- In the **Status** field, enter a message indicating the participant has been added: e.g., `Participant added`.&#x20;
- In the **Name** and **Email** fields, map the name and email passed from the parent scenario so that you can identify the participant.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/g3HTq5htfclZG8KFU9e1P-20260223-093555.png" size="50" width="1084" height="638" position="center" showCaption="false" indent="2"}
:::

:::WorkflowBlockItem
Return to the **Router** and add a second route.&#x20;

This route will run if the email from the registration form **already exists** in the database. To configure the filter, right-click the dots and select **Set up a filter**.&#x20;

Set the **Condition** as follows: &#x20;

- Map `Total number of bundles` from the **Google Sheets > Search Rows** module.
- Select **Numeric operators: Greater than**
- Enter **0**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/H1eL5iXrs-dfJkaByFeEr-20260223-102239.png" size="50" width="1146" height="928" position="center" showCaption="false" indent="2"}
:::

:::WorkflowBlockItem
Add another **Scenarios > Return output** module to this route. You will see the output fields you defined when creating a subscenario:

- In the **Status** field, add a message indicating the participant is already registered: e.g., `Participant already exists`.&#x20;
- In the **Name** and **Email** fields, map the name and email passed from the parent scenario.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/yQOt3lBC-dS71RydPe1Zv-20260223-110917.png" size="60" width="1310" height="642" position="center" showCaption="false" indent="2"}
:::

:::WorkflowBlockItem
Your subscenario should now look like this:

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/xoo-2aTEmKEcaZt2jpqLc-20260223-112414.png" size="70" width="2236" height="1172" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
All subscenarios should be **active** and scheduled **on demand**.&#x20;

If you create a subscenario from the **Scenarios > Call a scenario** module, it's automatically scheduled on demand. In this case, you only need to enable the toggle to activate the subscenario and save it.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/OvspdJawZNlzG6qydsJQD-20260224-130950.png" size="40" width="1298" height="104" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
Return to the parent scenario to complete the configuration.&#x20;
:::

:::WorkflowBlockItem
Open the **Scenarios > Call a scenario** module and verify that:

- The correct subscenario is selected
- The subscenario is active (has a green **Active** label)

In the Scenario inputs field, map the data you pass from the parent scenario to the subscenario. In this example, it will be Name and Email from the **Jotform > Watch for Submissions** module. &#x20;

Se&#x74;**&#x20;Wait for the scenario** **to** **finish** to **Yes**. In a synchronous execution, it indicates that a parent scenario will wait for a subscenario's outputs before continuing execution.

Once verified, click **Save**.&#x20;

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/JbKdAaue5D83PkZCkOfBx-20260224-150614.png" size="50" width="1020" height="1298" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
Add the **Gmail > Send an email** module to send a welcome email to the registered participant. Here, you can map `email` returned from the **Scenarios > Call a scenario** module to the **Recipient email address** field.&#x20;

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/xSpopoGgSncg0Or6H8tee-20260223-172334.png" size="50" width="1130" height="1208" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
Th&#x65;**&#x20;Scenarios > Call a scenario** module will return outputs from your subscenario. Since we only need to send the email to the newly registered participants, set up a corresponding filter.&#x20;

Right-click the dots between the **Gmail > Send an email** and **Scenarios > Call a scenario&#x20;**&#x6D;odules, and click **Set up a filter.&#x20;**

Set the **Condition** as follows: &#x20;

- Map `status` from the **Scenarios > Call a scenario&#x20;**&#x6D;odule.
- Select **Text operators: Equal to**
- Enter `Participant added` (the status defined in step 8).
- Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/84hVWWZI3wyGm8F7ArT1Q-20260223-174312.png" size="70" width="1390" height="778" position="center" showCaption="false"}
:::
:::::

Your parent scenario should look like this:

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/AjB07AK736C5BCIRvW4Ty-20260305-142648.png" size="60" width="1748" height="1374" position="center" showCaption="false"}

Save it and submit a form in Jotform to test the workflow.

### Create a subscenario with as**ynchronous execution&#x20;**

After clicking **Create a scenario** in the **Scenarios >** **Call a scenario** module, you can create your subscenario. To do that:

:::::WorkflowBlock
:::WorkflowBlockItem
In the **Create a scenario** window:

- In the **Name** field, enter the subscenario name.
- Optionally, in the **Description name** field, add a description.
- Define the input structure.

In our example, the parent scenario receives the **Name** and the **Email** from the **Jotform > Watch for Submissions&#x20;**&#x6D;odule and passes this data to the subscenario. Therefore, we create two inputs: `name` and `email`.

Since this is asynchronous execution, the parent scenario doesn't expect any outputs. Therefore, you don't need to define any output fields.

- Click **Create** **scenario**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/ejf0xxT9HNoNX90YD53vG-20260206-152332.png" size="30" width="714" height="1382" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
You will see a scenario diagram with the **Scenarios >** **Start scenario&#x20;**&#x61;nd the **Scenarios >** **Return****&#x20;outputs&#x20;**&#x6D;odules.&#x20;
:::

:::WorkflowBlockItem
To add modules to your subscenario, click the big + icon between the modules
:::

:::WorkflowBlockItem
Add the **Google Sheets > Add a Row** module to store the participant's information. In the module settings:

- Select the spreadsheet and sheet where registrations are stored.
- Map `name` and `email` values from the **Scenarios > Start scenario** module.
- Click **Save**.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/qQEYAPR0Nq_JlYkGHbcjw-20260219-125954.png" size="50" width="1028" height="1394" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
If you create a subscenario from the **Scenarios > Call a scenario** module, the  **Scenarios > Return output** module is added automatically.&#x20;

Since in asynchronous execution, your subscenario will not return any output, you can right-click this module and delete it.
:::

:::WorkflowBlockItem
Your subscenario should now look like this:

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/2DBj82pK7r43FeMM7zpQ7-20260224-135914.png" size="60" width="1544" height="844" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
All subscenarios should be active and scheduled on demand.&#x20;

If you create a subscenario from the **Scenarios > Call a scenario** module, it's automatically scheduled on demand. In this case, you only need to enable the toggle to activate the subscenario and save it.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/OvspdJawZNlzG6qydsJQD-20260224-130950.png" size="40" width="1298" height="104" position="center" showCaption="false"}
:::

:::WorkflowBlockItem
Return to the parent scenario to complete the configuration.
:::

::::WorkflowBlockItem
Open the **Scenarios > Call a scenario** module and verify whether:

- The correct subscenario is selected
- The subscenario is active (has a green **Active** label)

In the Scenario inputs field, map the data you pass from the parent scenario to the subscenario. In this example, it will be Name and Email from the **Jotform > Watch for Submissions** module. &#x20;

Se&#x74;**&#x20;Wait for the scenario** **to** **finish** to **No**. In asynchronous execution, it indicates that a parent scenario will not wait for a subscenario's outputs and will continue execution after calling it.

Once verified, click **Save**.&#x20;

:::hint{type="info"}
If the subscenario has a grey **Inactive** label, click **Preview**. This will open a subscenario in a new window, where you can activate and save it.  &#x20;

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/w6S1RefF0P6ClcfWoTNI8-20260225-090939.png" size="50" width="1002" height="1286" position="center" showCaption="false" indent="2"}
:::
::::

:::WorkflowBlockItem
Add the **Gmail > Send an email** module to send a welcome email to the registered participants. Here, you can map `email` returned from the **Scenarios > Call a scenario** module to the **Recipient email address** field.&#x20;

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/xSpopoGgSncg0Or6H8tee-20260223-172334.png" size="50" width="1130" height="1208" position="center" showCaption="false"}
:::
:::::

Finally, save the parent scenario and submit a form in Jotform to test the workflow.

## When to use subscenarios

### Reduce the complexity and simplify the maintenance of scenarios

Subscenarios are useful when you're building a complex workflow with multiple conditions and branching logic. They help reduce overall complexity and make scenarios easier to read, debug, and maintain.

Let's suppose you are creating a "B2B Leads Creation" scenario that receives new contact information, which includes:&#x20;

- The contact's identity
- The company they work for&#x20;
- Optionally, the affiliate who introduced them
- Optionally, the campaign or event they are interested in

Creating a contact may seem simple, but the process can quickly become complex, as you need to:

- Check whether the company already exists in the CRM (and create it, if it doesn't)
- Check whether the contact already exists (and create or update it, if necessary)&#x20;
- Optionally, add the contact to campaigns or events
- Optionally, link the contact to an affiliate partner

If you process such a complex workflow in a single scenario, you may end up with multiple routes and nested filters leading to more routes. As the workflow grows, it becomes harder to read, more difficult to debug, and increasingly complex to maintain.

A better approach is to divide the workflow into dedicated subscenarios for each task:

- Create or update a company
- Create or update a contact
- Add a contact to a campaign or event
- Attach a contact to an affiliate

With this structure, the parent scenario stays simple. It can have a few routes, evaluate high-level conditions, and call the appropriate subscenario when needed. The subscenarios will focus on a single task each and have their own routes and conditions. Even if a subscenario becomes complex internally, it remains easier to maintain and troubleshoot.

### R**euse instead of duplicating**

Subscenarios are also useful for avoiding duplicated logic across multiple workflows. Let's suppose you're managing product inventory and need to create or update products in several different business cases:

- When a new order is placed in your online store, you decrease the stock
- When a B2B partner places a direct order, you also decrease the stock
- When new products are delivered, you update the product in the inventory
- When a customer returns a product, you increase its stock

You can build separate scenarios for each of these cases. For example, when a new order is placed in Shopify, the scenario would:

- Check whether the product still exists in the inventory in your ERP&#x20;
- Verify that stock is available
- Return an error if the stock is 0
- Decrease the stock by the ordered quantity

Similarly, when adding a new product to the inventory via a form, the scenario would:

- Verify whether the SKU already exists
- Create the product if it doesn't exist
- Update the stock level accordingly&#x20;

If you look closely, each use case follows the same pattern:

- Verify whether the product exists
- Check stock levels
- Increase or decrease stock&#x20;
- Update product information&#x20;
- Handle errors (e.g., when stock equals 0)

By having a workflow for each case, you're duplicating actions across multiple scenarios and spending more time on updating each of them. Additionally, if you want to add another step to the workflow (e.g., add a new POS with access to update inventory), you have to duplicate the stock inventory logic again.

A better approach is to create a dedicated subscenario that will handle inventory and:

- Create products
- Update products
- Verify stock levels
- Increase or decrease stock&#x20;
- Manage stock-related errors

All parent scenarios can simply call this subscenario whenever inventory needs to be checked or modified. You will no longer need to duplicate the stock management operations as they are centralized in one subscenario that reuses the same logic. You can also link any new parent scenario at any time, and if you change ERP or handle more data, you just need to change one single scenario.