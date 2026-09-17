---
type: reference
timeline: reference
status: source-capture
title: Scenario execution, cycles, and phases
slug: scenario-execution-cycles-and-phases
description: Explore the cycles and phases of scenario execution to manage data processing
image: https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/t3BB4DcZqEFyzbwDYkxgg_domino-zoomin-purple-a-1.png
docTags: 
createdAt: 2025-02-03T13:29:15.599Z
---

Make is a transactional system, similar to [relational databases](https://en.wikipedia.org/wiki/Database_transaction), where all operations within a scenario are executed as part of the controlled process.

&#x20;Each scenario execution goes through the following phases:&#x20;

- Initialization 
- One or more cycles
- Finalization

# **Initialization phase**

During th&#x65;**&#xA0;initialization phase**, all necessary connections are created and verified. Make   also checks whether each module can perform its intended operation(s).

# Cycles

The initialization phase is followed by at least one cycle, which consists of:

- **O****peration phase** (reading or writing)
- **C****ommit/rollback phases&#x20;**(finalizing or discarding changes).&#x20;

Each cycle represents an indivisible unit of work composed of a series of operations. 

It is possible to set the maximum number of cycles in the [Scenario settings](https://help.make.com/scenario-settings#MsQG). The default number is 1.

## Operation phase

During the **operation phase,** Make performs reading and writing operations.&#x20;

- **R****eading operations** consist of obtaining data from a service that will then be processed by other modules according to a predefined scenario. For example, the **Dropbox > Watch files** module returns new bundles (files) created since the last scenario execution.
- **W****riting operations&#x20;**&#x63;onsist of sending data to a given service for further processing. For example, the **Dropbox > Upload a file** module uploads a file to a Dropbox folder.

## Commit and rollback phases

After the operation phase, Make either commits or rolls back the operations:

- If operations are successful for all modules, the **commit phase** begins. During this phase, all operations performed by the modules are committed. Make sends information to all the services involved in the operation phase about its success.
- If an error occurs during the operation or commit phase for any module, the phase is aborted and the **rollback phase** is started, making all operations during the given cycle void. &#x20;

:::hint{type="warning"}
Not all modules allow for rollback. Modules that support rollback are marked with the `ACID` tag. Modules without this tag do not support rollback and **cannot be reverted&#x20;**&#x62;ack to their initial state in case of an error in other modules.
:::

:::hint{type="info"}
In the context of rollbacks, setting the maximum number of cycles can be particularly useful when processing multiple bundles from a trigger in a single run.

For example, consider a scenario where:

- You use a polling trigger to check for new data.
- You don’t need the scenario to run every minute, so you schedule it to run once per hour.
- There are multiple bundles to process in one execution.

In this case, you have two options:

1. **Increase the trigger limit in the Module settings:&#x20;**&#x52;aise the maximum number of results the trigger retrieves per cycle (e.g., from 2 to 10). The scenario will still use a single cycle, but process more data in one go.&#x20;
2. **Increase the maximum** **number of cycles in the** **Scenario settings:&#x20;**&#x4B;eep the trigger limit low (e.g., 1), but configure the scenario to run in multiple cycles (e.g., from 1 to 10).

If an error occurs while processing the 10th bundle, for example:

- With the first option (one cycle, higher trigger limits), the entire cycle is rolled back. None of the processed bundles are saved, and everything has to be reprocessed in the next run.
- With the second option (multiple cycles, lower trigger limits), only that last cycle (the failed bundle) is rolled back. Since previous cycles are already committed, only that failed bundle has to be reprocessed in the next run. This approach can save time and prevent unnecessary reprocessing of successfully completed work.
:::

# F**inalization phase**

During the **finalization phase**, open connections (e.g., FTP connections, database connections, etc.) are closed and the scenario execution is completed.

# Example

**Transfer of bundles between databases**

The following example shows how to connect three `ACID` modules. The aim of the scenario is to get new rows from a MySQL database, insert (transfer) them into an MSSQL database, and then insert the IDs of the rows from the MSSQL database into a PostgreSQL database.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/yAufeXqD1oGWOPBNi5MAm-QrZSe0uQHs0jTc5lMSP0X-20250214-130728.png" size="90" width="1085" height="368" position="flex-start" alt="Scenario execution example" darkWidth="1085" darkHeight="368" showCaption="false"}

When the scenario starts, the **initialization phase** is performed first. Make verifies connections to the MySQL, MSSQL and PostgreSQL databases one at a time. If everything goes well and the connections are successful, Make moves on to the **operation phase**. If an error occurs, the **finalization phase** starts instead of the **operation phase** and the scenario is terminated.

If there isn't an error, the **operation phase** begins. A preset procedure selects (reads) the table rows (bundles) from MySQL. Those rows are then passed to the next module that writes them to a selected table in the MSSQL database. If everything is in order, the last PostgreSQL procedure is called to insert the row IDs returned by the preceding module into the table.

If the operation phase is completed successfully, the **commit phase** begins. Make calls the SQL COMMIT command for each database, and the write operations are committed.

However, if the operation or commit phase fails due to an error (e.g., connection failure), Make calls for a rollback. During the **rollback phase**, Make goes through all modules and executes the SQL ROLLBACK command for each module to revert each database back to its initial state.

Finally, during the **finalization phase**, each module closes its connection to the database.
