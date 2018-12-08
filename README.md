# LandSat_Imagery_Processor
This is a tool that takes LandSat Images that are in the tar file format and unzips, and composites all the numbered bands.
## Lots of LandSat Images to Process 
In the pasted this job involved a lot of time, pain, and suffering. Keeping all the files in order and making sure that you didn’t unzip the same file twice was all part of the fun.
## Summary
This python script is design to unzip the LandSat tar.gz flies from USGS website [Earth Explorer](https://earthexplorer.usgs.gov/). Obtaining imagery form USGS website allows you to get global imagery collected every sixteen days. These files are usually very large and that is why they are zipped with the tar.gz file zip. These files can range from 200 to over 400 MB each in the tar.gz file format, and after they are unzipped, they range anywhere from 1 to 2 GB. After the unzip is done the result is a list of flies and single band images. Then the script separates out from the list of images files that are bands 1 through however many bands there are and arranges them in numerical order, then it calls the composite tool in Arc Pro and runs it to composite the bands to form the multi spectral LandSat image. Last of all it calls the clip tool and clips the image to the study area. All of this is done in automated sequence, and the results are great!  
## What
With this tool in Arc Pro you can unzip the tar.gz LandSat file and composite the bands and last of all it Clips the LandSat image tile to a provided study area. 
## Why
Because this job can be tedious and very time consuming.
## How
In this script we first import the arcpy library along with the os, sys, glob, tarfile, zipfile and we also called at second script that did the converting the file end to a integer so that we could sort them in numerical order. Then we did some [arcpy](http://pro.arcgis.com/en/pro-app/arcpy/functions/getparameterastext.htm) setup with the . GetParameterAsText(0). Then we open the file and called the .extractall() this is from [Stackoverflow](https://stackoverflow.com/questions/30887979/i-want-to-create-a-script-for-unzip-tar-gz-file-via-python)after that we sorted the images then we called the arcpy.CompositeBands_management()  then last of all we call the arcpy.Clip_management() to clip the image to the study area.
## Usage/Example
I used it to unzip, composite and clip LandSat images of Hawaii for a Remote Sensing Project.
