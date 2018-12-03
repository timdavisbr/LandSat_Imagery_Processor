"""
Final Project - LandSat Image Processor
Timothy Davis
tdavi4633@ung.edu

"""
### -Improts- ###

import arcpy
import os
import sys
import glob
import tarfile
import zipfile
from tool_utils import banded

### -Main Block- ###


zipfile = arcpy.GetParameterAsText(0)
output_folder = arcpy.GetParameterAsText(1)

tf = tarfile.open(zipfile, 'r:gz')
tf.extractall()


images = glob.glob('*.tif')

results = []
for f in images:
    if 'band' in f:
        results.append(f)
        results = sorted(results, key=banded)
bands = ";".join(results)

arcpy.AddMessage(images)
arcpy.CompositeBands_management(bands, "compbands.tif")


""" This tool didn't work
ERROR 999999: Error executing function.
The table name is invalid.
No spatial reference exists.
The table was not found. [compbands.tif]
Failed to execute (CompositeBands).
 Failed to execute (Unzip).

"""
