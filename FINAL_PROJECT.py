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
clip_extent = arcpy.GetParameterAsText(2)
xy_tolerance = ("")

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
arcpy.CompositeBands_management(bands,
                                os.path.join(output_folder, "compbands.tif"))

arcpy.Clip_analysis(os.path.join(output_folder, "compbands.tif"), clip_extent, os.path.join(output_folder, "clip_composit.tif"), xy_tolerance)

#arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)

""" File "L:\TDAVI4633\4 Fall 2018\GISC 3200K - Python\LandSat_Imagery_Processor\FINAL_PROJECT.py", line 42
    arcpy.Clip_analysis(os.path.join(output_folder, "compbands.tif")), clip_extent, output_folder, xy_tolerance)
                                                                                                               ^
SyntaxError: invalid syntax
 Failed to execute (Unzip).
"""
