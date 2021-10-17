from qgis.core import*
#creating a variable
path=QgsVectorLayer('D:\Geospatial_Programming\ASSIGNMENT_3\LST\Boundary.shp','Boundary','ogr')
QgsProject.instance().addMapLayer(path)
#First import processing module
import processing   
#set input and output file names
inpath = "D:\Geospatial_Programming\ASSIGNMENT_3\LST\Boundary.shp"
clippath = "D:\Geospatial_Programming\ASSIGNMENT_3\LST\Melbourne.shp"
outpath = "D:\Geospatial_Programming\ASSIGNMENT_3\LST\clip2.shp"
#run the clip tool
processing.run("native:clip", {'INPUT':inpath, \
'OVERLAY':clippath, 'OUTPUT':outpath})
#add output to the qgis interface
iface.addVectorLayer(outpath, '', 'ogr')
