---
title: Working with files
slug: working-with-files
description: Learn how Make handles files and how to map file names and actual content
image: https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/OoiUJgdjCTv3dEFFtQKFV_domino-zoomin-purple-a-1.png
docTags: 
createdAt: 2025-02-03T13:29:15.599Z
---

Some modules in Make work with files, allowing you to download, upload, transform, or move files between apps. For example, you can download email attachments or transcribe audio files using AI.

To use a file in your scenario, you first need a module that retrieves the file data. Once the file is available, you can map it to subsequent modules for further processing.

## How to work with file handling modules

**Input for file handling modules**

To use the file handling modules, you will require two inputs:

1. File Name
2. Data

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/H74qf4vwTCOSQVgL2_Ffu_image.png)

**Step 1**: To get the **File name** and **Data**, use any module that can download or return the content of a file you wish to process. For example: **Google Drive** > **Download a File**, **Dropbox** > **Watch Files**, **Facebook Pages** > **Watch Posts**, or **Gmail** > **List attachments and media**, etc.

**Step 2**: Use the output from step 1 as the input for the file handling module. The file name and file content are then mapped automatically or you can map them manually as shown below.&#x20;

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/dsmDgCu4oZa3cvrqrrf40-20260126-123320.png)

:::hint{type="success"}
To process a file from a URL, use the **HTTP > Download a file** module to download the file. You can then map the downloaded file from the **HTTP > Download a file** module to the appropriate field in your scenario.
:::

## Example 1: Upload images to cloud storage

The example below shows how to upload images from Gmail to Google Drive. The **Gmail&#x20;**> **List email attachments and media** module returns the image and other data based on the filters set. To upload the image to Google Drive, select the **Gmail&#x20;**>**&#x20;List email attachments and media** as the source file in the **Google Drive** >**&#x20;Upload a file** module. Make automatically maps the file name and content, and uploads it to the specified Google Drive folder.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/NhU4qZuQaJ0LHLhiT3egd-20260126-085726.png)

In some cases, you may want to rename a file while keeping its content unchanged. To do this, use the **Map** option to map the file name and file content separately.

When specifying the file name, include the full name and extension (for example, invoice.xml). Both binary files (such as photos, videos, and PDFs) and text formats are supported.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/-VDXYn0YfSGPVzqDpF-Sb-20260126-090931.png)

## Example 2: Download photos to Dropbox using the HTTP module

The following example demonstrates how to map photos from Facebook Pages to Dropbox using an HTTP module. The **Facebook Pages&#x20;**>**&#x20;Watch Posts (public page)** trigger returns the image’s URL and other details. The  **HTTP&#x20;**>**&#x20;Download a file** module is added to download the file from the URL. To upload the image to Dropbox, select the **HTTP > Download a file** as the source file in the **Dropbox&#x20;**>**&#x20;Upload a file** module. Make automatically maps the file name and content, and the images will be uploaded to the specified Dropbox folder.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/h2_WfQxcJk4jfgEME2gdj-20260126-093624.png)

As shown in Example 1, you may want to rename a file without changing its content. To achieve this, use the **Map** option to map the file name and file content separately.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/ryMqiY08bYAH1phU_-z4b-20260126-093450.png)

## Example 3: Extract and analyze content from a PDF file

In the example below, a PDF file containg a Wikipedia page with holidays in the Czech Republic is stored in Google Drive. It is then downloaded, and its content is extracted and analyzed for further processing. The **Google Drive&#x20;**>**&#x20;Download a File** module is used to download the PDF file. The file’s contents are then extracted using the **Make AI Content Extractor&#x20;**>**&#x20;Extract text from a document** module by mapping the output from **Google Drive&#x20;**>**&#x20;Download a File**.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/X2gTNH20VwL23dhDg4Tl7-20260126-103331.png)

When this module runs, an output bundle of the text from the PDF file is generated.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/JPwzHSURbzAo2AqZbbp8I-20260126-105403.png)

The output of this module can be further analyzed to achieve the desired results as shown below. In this example, **Make AI Toolkit** >**&#x20;Simple Text Prompt** is instructed to list all the holidays in chronological order with one entry per line.

![](https://archbee-image-uploads.s3.amazonaws.com/oAyFj2GHlBeBVWF5OAir2/4PN2zd4TjflyTsgc3upIa-20260126-110619.png)

## Maximum file size

The maximum file size allowed depends on the plan you are subscribed to (FREE - 5 MB, CORE - 100 MB, PRO - 250 MB, TEAMS - 500 MB, ENTERPRISE - 1,000 MB). If it is exceeded, Make proceeds in accordance with the settings of the [Enable data loss](https://app.archbee.com/docs/TDD_JYughqVhdcQ3sZF9_/7-HEHdTuU2XyYs8_qurub#pSdXT) option.