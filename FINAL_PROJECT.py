"""
Final Project - LandSat Image Processor
Timothy Davis
tdavi4633@ung.edu

"""
### -Imports- ###

import arcpy
import os
import sys
import glob
import tarfile
import zipfile
import shutil
import time
from tool_utils import banded

### -Main Block- ###


zipfile = arcpy.GetParameterAsText(0)
output_folder = arcpy.GetParameterAsText(1)
clip_extent = arcpy.GetParameterAsText(2)


tf = tarfile.open(zipfile, 'r:gz')
TEMP = os.path.join(output_folder, 'temp')
if not os.path.isdir(TEMP):
    os.mkdir(TEMP)
else:
    shutil.rmtree(TEMP)
    time.sleep(1)
    os.mkdir(TEMP)

tf.extractall(TEMP)

images = glob.glob(os.path.join(TEMP, '*.tif'))
arcpy.AddMessage(images)

results = []
for f in images:
    if 'band' in f:
        results.append(f)
        results = sorted(results, key=banded)
bands = ";".join(results)

 

arcpy.CompositeBands_management(bands,
                                os.path.join(output_folder, "compbands.tif"))

arcpy.Clip_management(os.path.join(output_folder, "compbands.tif"),
                      "#", 
                      os.path.join(output_folder, "clip_composit.tif"),
                      clip_extent,
                      "#", "ClippingGeometry", "NO_MAINTAIN_EXTENT")

# Clip_management (in_raster, rectangle, out_raster,
# {in_template_dataset}, {nodata_value}, {clipping_geometry}, {maintain_clipping_extent})



shutil.rmtree(TEMP)











