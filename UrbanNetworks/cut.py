##cut..

#get bounding box creates from values counterclockwise
from shapely.geometry import LineString, box, shape, mapping
import fiona
from shapely.ops import split

#parameters##
shpfile = "dump/myTgrid.shp" #input
outshp = 'dump/cut.shp' #out 
in1 = 0.15 #? fraction?
in2 = 0.4

#read in shapefile ***
with fiona.collection(shpfile, "r") as input:
    for feature in input:
        network = shape(feature['geometry'])
    #network = #union all lines

#fraction along top line, fraction along side line, draw line between points
bboxTuple = network.bounds
bbox = box(bboxTuple[0],bboxTuple[1],bboxTuple[2],bboxTuple[3],ccw=False)#.buffer(10)

## get distance between tuple 1 and tuple 2 - or create lines
## input fraction of first dist and second dist(vertical) and interpolate-* by dist, second add first dist
## difx = bboxTuple2[2] - bboxTuple[0]
#i is between 0-0.5 (diagonal) or 0-0.75? first(0-0.25) second(0.25-0.5)
firstPt = bbox.boundary.interpolate(in1, normalized=True)
secondPt = bbox.boundary.interpolate(in2, normalized=True)
cutline = LineString([(firstPt.x,firstPt.y),(secondPt.x,secondPt.y)])
print bbox.wkt
print cutline.wkt
#polygon of bounds and cutline
#replace 2nd point not bufferd with cutline ..then buffer
poly = split(bbox,cutline)[0]
print poly.wkt

#networkcutpts = network.intersection(cutline)##polygons
#https://shapely.readthedocs.io/en/latest/manual.html#shapely.ops.split
new = split(network,cutline) #split lines by line to get geometry collection
res = new[0]
print len(network)
result = LineString()
for l in new:
    if l.within(poly.buffer(0.5)):
        result = result.union(l)

#write new shapefile

# schema of the shapefile 
schema = {'geometry': 'MultiLineString','properties': {'test': 'int'}}
with fiona.open(outshp,'w','ESRI Shapefile', schema) as c:
       record = {'geometry':mapping(result), 'properties':{'test':1}}
       c.write(record)