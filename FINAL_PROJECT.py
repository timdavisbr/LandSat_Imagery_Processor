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

""" Traceback (most recent call last):
  File "L:\TDAVI4633\4 Fall 2018\GISC 3200K - Python\LandSat_Imagery_Processor\FINAL_PROJECT.py", line 42, in <module>
    arcpy.Clip_analysis(os.path.join(output_folder, "compbands.tif"), clip_extent, os.path.join(output_folder, "clip_composit.tif"), xy_tolerance)
  File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\analysis.py", line 63, in Clip
    raise e
  File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\analysis.py", line 60, in Clip
    retval = convertArcObjectToPythonObject(gp.Clip_analysis(*gp_fixargs((in_features, clip_features, out_feature_class, cluster_tolerance), True)))
  File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\geoprocessing\_base.py", line 506, in <lambda>
    return lambda *args: val(*gp_fixargs(args, True))
arcgisscripting.ExecuteError: Failed to execute. Parameters are not valid.
 ERROR 000732: Input Features: Dataset L:\TDAVI4633\4 Fall 2018\GISC 3200K - Python\Python\compbands.tif does not exist or is not supported
Failed to execute (Clip).s
 Failed to execute (Unzip).
"""
