#importing QtGui and Qcolor library
from qgis.core import*
from PyQt5.QtGui import QColor
#creating a variable2
path=QgsVectorLayer('D:\Geospatial_Programming\ASSIGNMENT_3\LST\Boundary.shp','Boundary','ogr')
QgsProject.instance().addMapLayer(path)
# create a new symbol
symbol = QgsFillSymbol.createSimple({'line_style': 'dash', 'color': 'red'})
# apply symbol to layer renderer
path.renderer().setSymbol(symbol)
# repaint the layer
path.triggerRepaint()
print(path.renderer().symbol().symbolLayers()[0].properties())
#creating a variable2
path2=QgsRasterLayer('D:\Geospatial_Programming\ASSIGNMENT_3\LST\LST_Summer_20201.tif','Land_Surface_Temperature')
QgsProject.instance().addMapLayer(path2)
#statistics for raster band
stats=path2.dataProvider().bandStatistics(1, QgsRasterBandStats.All)
#get minimum and maximum value
min = stats.minimumValue
max = stats.maximumValue
#Create a color ramp shader
function= QgsColorRampShader()
function.setColorRampType(QgsColorRampShader.Interpolated)
#Define the colors
LST = [QgsColorRampShader.ColorRampItem(min, Qcolor(0, 255, 0)), 
QgsColorRampShader.ColorRampItem(max, Qcolor(255, 255, 0))]
function.setColorRamp(LST)
#Assign the color ramp 
shader=QgsRasterShader()
shader.setRasterShaderFunction(function)
#Apply symbology to raster
renderer = QgsSingleBandPseudoColorRenderer(path2.dataProvider(), 1, shader)
path2.setRenderer(renderer)