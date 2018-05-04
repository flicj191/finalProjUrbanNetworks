##join ..
'''read shapefile 
https://macwright.org/2012/10/31/gis-with-python-shapely-fiona.html'''

from shapely.geometry import LineString, box, shape, mapping
from shapely.affinity import translate
from shapely.ops import nearest_points
import fiona

#parameters## 
yoff = 0 #translate up or down -will change which points are joined
network = "dump/cut.shp"
network2 = "dump/myshp3.shp"

outshp = 'dump/join.shp' #output

with fiona.collection(network, "r") as input:
    for feature in input:
        network = shape(feature['geometry'])
        #print shape(feature['geometry'])

with fiona.collection(network2, "r") as input:
    for feature in input:
        network2 = shape(feature['geometry'])
        #print shape(feature['geometry'])

bboxTuple = network.bounds
bbox = box(bboxTuple[0],bboxTuple[1],bboxTuple[2],bboxTuple[3],ccw=False)
#minx, miny, maxx, maxy
bboxTuple2 = network2.bounds
bbox2 = box(bboxTuple2[0],bboxTuple2[1],bboxTuple2[2],bboxTuple2[3],ccw=False)

#translate left (minx) is greater than maxx of other
#shapely.affinity.translate(geom, xoff=0.0, yoff=0.0, zoff=0.0)
difx = bboxTuple2[2] - bboxTuple[0]

network1 = translate(network, xoff=difx+1, yoff=yoff)
Pts = nearest_points(network2,network1) #returns tuple
result = network2.union(LineString([(Pts[0].x,Pts[0].y),(Pts[1].x,Pts[1].y)]))

#union
result = result.union(network1)


#write new shapefile?
# schema of the shapefile 
schema = {'geometry': 'MultiLineString','properties': {'test': 'int'}}
with fiona.open(outshp,'w','ESRI Shapefile', schema) as c:
       record = {'geometry':mapping(result), 'properties':{'test':1}}
       c.write(record)