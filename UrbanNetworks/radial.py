'''
For creating a radial network for final project

Felicity Chun
2018
'''
#radial 
from shapely.geometry import Point, LineString, MultiPoint, mapping
from shapely.ops import nearest_points, split
import fiona, sys

##parameters
depth = 5 #sys.argv[1]
initBranches = 4 #sys.argv[2]

## save file create
folder = 'outputs/'
NetType ='Radial'
savefile = folder + NetType +'_d'+str(depth)+'_b'+str(initBranches)

#draw lines function for ring
def ringlines(line,ls):
    i=0
    while i < len(ls)-1:
        line = line.union(LineString([(Point(ls[i]).x, Point(ls[i]).y),(ls[i+1])]))
        i+=1
    line = line.union(LineString([ls[len(ls)-1],ls[0]]))
    return line

# function for adding another ring and drawing intersecting lines
def intersectLines(ring1,ls,line):
    ring2 = ring1.buffer(10)
    nextls = []
    k=0
    for co in ls:
        pt = nearest_points(Point(co),ring2.boundary)[1]#
        line = line.union(LineString([(co),(pt.x,pt.y)]))
        nextls.append((pt.x,pt.y)) #list of tuples of coordinates
        if k == 0:
            ptstart = pt
        k+=1
    #append first point again
    nextls.append((ptstart.x,ptstart.y))
    #create new point list with points in between, doubling number of points
    newls = []
    i=0
    while i < len(nextls)-1:
        newls.append(nextls[i])
        midcoords = ((nextls[i][0]+nextls[i+1][0])/2,(nextls[i][1]+nextls[i+1][1])/2)
        midpoint = Point(midcoords)
        pt = nearest_points(midpoint,ring2.boundary)[1]
        newls.append((pt.x,pt.y))
        i+=1

    return (ring2,newls,line)

#initialize center and initial list of points
center = Point(100,100)
ring1 = center.buffer(5)
ls = []
i=0
incr = 1/float(initBranches)
while i < 1:
    ptOnRing = ring1.boundary.interpolate(i, normalized=True)
    ls.append((ptOnRing.x,ptOnRing.y)) #ls points
    i += incr #parameter
    
line = LineString()
#connect points by lines
line = ringlines(line,ls)
res = intersectLines(ring1,ls,line)
line = res[2]
newls = res[1]
ring2 = res[0]

while depth > 0:
    line = ringlines(line,newls)
    res = intersectLines(ring2,newls,line)
    line = res[2]
    newls = res[1]
    ring2 = res[0]
    depth -= 1
    print 'depth: '+str(depth)


# schema of the shapefile ##create in top cell
schema = {'geometry': 'MultiLineString','properties': {'test': 'int'}}
with fiona.open(savefile,'w','ESRI Shapefile', schema) as c:
       record = {'geometry':mapping(line), 'properties':{'test':1}}
       c.write(record)