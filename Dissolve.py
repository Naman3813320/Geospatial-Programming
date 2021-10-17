import processing

infn = 'D:\\Geospatial_Programming\\ASSIGNMENT_3\\LST\\place1_buffer.shp'

outfn = 'D:\\Geospatial_Programming\\ASSIGNMENT_3\\LST\\place1_buffer_dissolved.shp'

processing.run("native:dissolve", {'INPUT':infn, 'OUTPUT': outfn})
iface.addVectorLayer(outfn, '', 'ogr')
