from qgis.core import*
#creating a variable
path=QgsVectorLayer('D:\Geospatial_Programming\ASSIGNMENT_3\LST\Boundary.shp','Boundary','ogr')
QgsProject.instance().addMapLayer(path)
#creating a variable2
path2=QgsVectorLayer('D:\Geospatial_Programming\ASSIGNMENT_3\LST\Places.shp','Places','ogr')
QgsProject.instance().addMapLayer(path2)
#First import processing module
import processing

#defining the in and out function
infn = 'D:\\Geospatial_Programming\\ASSIGNMENT_3\\LST\\place.shp'
outfn = 'D:\\Geospatial_Programming\\ASSIGNMENT_3\\LST\\place2_buffer.shp'  

#putting the rest of information related to buffer
processing.run("native:buffer", \
{'INPUT':infn, \
'DISTANCE':5000,'SEGMENTS':5, \
'END_CAP_STYLE':0,'JOIN_STYLE':0, \
'MITER_LIMIT':2,'DISSOLVE':False, \
'OUTPUT':outfn})
#add layer to map using iface
iface.addVectorLayer(outfn,'','ogr')