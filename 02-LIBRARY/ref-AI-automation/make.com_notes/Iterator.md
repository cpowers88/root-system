---
type: reference
timeline: reference
status: source-capture
title: Iterator
slug: iterator
description: Split arrays into individual bundles using iterators to process each item separately
image: https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/I0fCfGmmqhy5ewxeDPfA1_domino-zoomin-purple-a-1.png
docTags: 
createdAt: 2025-02-03T13:29:15.599Z
---

Iterator is a special type of module that converts an array into a series of bundles. Each array item will output as a separate bundle.

## Setting up an iterator

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/Z5TzLrnePyBiz8uz4CGc8_uuid-76ebf1a2-e19f-d998-5faa-366411cbe503.png" size="78" width="853" height="497" position="center" showCaption="false"}

Setting up an iterator is done in the same way as [setting any other module](docId\:vNBss-BELMDIN3D4gguxL). The Array field contains the array to be converted/split into separate bundles.

### Examples:

### Save email attachments to Google Drive

The scenario below shows how to retrieve emails with attachments and save the attachments as single files in a selected [Google Drive](docId\:CT1o6eSjM1F0Xm3Wk5nBx) folder.

Emails can contain an array of attachments. The **Iterator** module inserted after the first module enables you to handle each attachment separately. The **Iterator** splits the array of attachments into single bundles, each bundle with one attachment will then save one at a time in a selected Google Drive folder. The **Iterator** module set up is shown above - the Array field should contain the `Attachments[]` array.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/6me7VXLBgnu4YVJzrjewX_uuid-afd56dcf-8ee1-119f-c8cf-9d1b8b93778a.png" size="90" width="1324" height="496" position="center" showCaption="false"}

### Specialized iterators

For your convenience, many Make apps offer specialized iterator modules with a simplified setup. For example, the [Email](docId\:MInmGWOE1-I9v0yVMHkZm) app contains the special iterator **Email > Iterate attachments** that will produce the same results as the general **Iterator** without having to specify the array, just the source module.

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/QhBwYdJiHid8iJz0thwvN_uuid-bd6d2f54-cd86-0526-3eaf-a1ff554dba42.png" size="94" width="1226" height="417" position="center" showCaption="false"}

## Learn when to use an Iterator in your scenarios

The video below is module 1 of the 3 part lesson titled **Iterator and Array Aggregator**. It explains the purpose of the Iterator and the Array Aggregator and with the help of a sample scenario, explains when to use an Iterator and what to do with the output.

::embed[[Youtube Link Here](https://www.youtube.com/embed/mWZBA2xSvB4)]{url="https://www.youtube.com/embed/mWZBA2xSvB4"}

### Troubleshooting: Mapping panel does not display mappable items under the Iterator module

When an **Iterator** does not have information about the structure of the array's items, the mapping panel in the modules following the **Iterator** will display only two items under the **Iterator**: `Total number of bundles` and `Bundle order position`:

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/_4I0SIQ4StH8PY7oH4FzL_uuid-9e8ce4d7-8de0-9a44-0f40-379c04149499.png)

The reason for this is that in Make each module is responsible for providing information about items it outputs so these items can be properly displayed in the mapping panel in the following modules. However, there are several modules that might be unable to provide this information in some cases, e.g. [JSON](docId:2ZexWuohEi0YVSOEq2NAg)**&#x20;> Parse JSON** or [Webhooks](docId:1yhUnJ8jvZyxiP9Cf3Ps1)**&#x20;> Custom Webhook** modules with missing [data structure](docId:1EOkQdVOyEt82um5dJjA8).

The solution is to manually execute the scenario to make the module learn about the items it outputs so it can provide the information to the following modules.

For example, if you have a **JSON > Parse JSON** module without a data structure as below:

::Image[]{src="https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/GBSv9I7uVXF8bQP5TMfxl_uuid-aebaafc2-8fef-c8f5-9c40-c7d125978bd1.png" size="62" width="844" height="677" position="center" showCaption="false"}

And then if you connect an **Iterator** module to it, you will not be able to map the output of the module to the *Array* field in the setup panel of the **Iterator**:

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/lDcwWarEB3Bv0vz0TByn2_uuid-cdb106ba-05ba-4b5a-e0a2-b4999f852db6.png)

To resolve this, just manually start the scenario in the Scenario editor. You can un-link the modules after the **JSON > Parse JSON** module to prevent the flow from proceeding further or right-click th&#x65;**&#x20;JSON > Parse JSON** module and choose "Run this module only" from the context menu to execute only the **JSON > Parse JSON** module.

Once the **JSON > Parse JSON** has been executed, it learns about the items it outputs and provides this information to all the following modules including the **Iterator**. The mapping panel in the **Iterator's** setup will then display the items:

![Flow\_Control\_10.png](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/aDAcDFWeOwq8EBbtvosuL_uuid-52e88ac1-3593-608c-57f3-f93b0a792a7a.png)

Moreover, the mapping panel in the modules connected after the **Iterator** will display the items contained in the array's items:

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/L7AD8qbPhPEC30mVyiMdV_uuid-39c30df4-4f5e-1bff-6c6c-f1449fc1a7da.png)

**In summary:** if you cannot see some items in a module's mapping panel, simply run the scenario once so all the modules can learn about the items they output and provide this information to the following modules.
