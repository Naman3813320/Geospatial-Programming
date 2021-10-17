import gdal

gdal.UseExceptions()

rasin = "D:\Geospatial_Programming\ASSIGNMENT_3\LST\LST_Summer_20201.tif"
shpin = "D:\Geospatial_Programming\ASSIGNMENT_3\LST\Melbourne.shp"
rasout = "D:\Geospatial_Programming\ASSIGNMENT_3\LST\LST_CLIP_2020.tif"

result = gdal.Warp(rasout, rasin, cutlineDSName=shpin)

iface.addRasterLayer(rasout)

   
