'''
for final project 2018
felicity chun

cut function


https://shapely.readthedocs.io/en/latest/manual.html#shapely.ops.split
'''
#get bounding box creates from values counterclockwise
from shapely.geometry import LineString, box, shape, mapping
import fiona
from shapely.ops import split
from datetime import datetime

#parameters##
shpfile = "grid_w40_h80" #input
inpath ='outputs/'
 
frac1 = 0.2 # fraction between 0 and 1
frac2 = 0.4
outshp = 'dump/'+shpfile+'c'+ str(frac1).replace('.','') + str(frac2).replace('.','') #out


#read in shapefile ***
with fiona.collection(inpath+shpfile+'/'+shpfile+'.shp', "r") as input:
    for feature in input:
        network = shape(feature['geometry'])
    

#fraction along top line, fraction along side line, draw line between points
bboxTuple = network.bounds
bbox = box(bboxTuple[0],bboxTuple[1],bboxTuple[2],bboxTuple[3],ccw=False)#.buffer(10)

## get distance between tuple 1 and tuple 2 - or create lines
## input fraction of first dist and second dist(vertical) and interpolate-* by dist, second add first dist
disty = bboxTuple[3] - bboxTuple[1]
distx = bboxTuple[2] - bboxTuple[0]
in1 = frac1 * disty
in2 = (frac2 * distx) + disty


firstPt = bbox.boundary.interpolate(in1)
secondPt = bbox.boundary.interpolate(in2)
cutline = LineString([(firstPt.x,firstPt.y),(secondPt.x,secondPt.y)])

print shpfile, datetime.now()
print bbox.wkt
print cutline.wkt
#polygon of bounds and cutline

poly = split(bbox,cutline)[0]
print poly.wkt


new = split(network,cutline) #split lines by line to get geometry collection
res = new[0]
print len(network)
result = LineString()
for l in new:
    if l.within(poly.buffer(0.5)):
        result = result.union(l)

#union splitline
result = result.union(cutline)

#write new shapefile
print datetime.now(), 'outputting shapefile..'
# schema of the shapefile 
schema = {'geometry': 'MultiLineString','properties': {'test': 'int'}}
with fiona.open(outshp,'w','ESRI Shapefile', schema) as c:
       record = {'geometry':mapping(result), 'properties':{'test':1}}
       c.write(record)