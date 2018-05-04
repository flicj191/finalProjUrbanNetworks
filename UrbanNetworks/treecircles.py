'''
For creating a branching tree in final project
Felicity Chun
2018
'''
#radial 
#import math
from shapely.geometry import Point, LineString, MultiPoint, mapping
from shapely.ops import unary_union
import fiona, sys

# parameters ##
factor = sys.argv[1] #5

branchamt = float(2) #sys.argv[2] #limit 2 branches for each node *float

folder = 'outputs/'
NetType ='Tree'
savefile = folder + NetType +'_d'+str(factor)+'_b'+str(int(branchamt))

# create point (100,100) and buffer a distance - number of points on circle?

center = Point(100,100)
ring1 = center.buffer(10)
ls = []
i=0
line = []#LineString()
while i < 1: 
    ptOnRing = ring1.boundary.interpolate(i, normalized=True)
    ls.append((ptOnRing.x,ptOnRing.y)) #ls point objects?
    i += 1/branchamt #parameter
    line.append(LineString([(center.x,center.y),(ptOnRing.x,ptOnRing.y)]))

#print ls
#create list on outer ring
def createListOuter(ring1,branchamt):
    outer = []
    i = 0
    ringO = ring1.buffer(10)
    branchnumber = branchamt * 2
    while i < 1:
        ringPt = ringO.boundary.interpolate(i, normalized=True)
        outer.append((ringPt.x,ringPt.y))
        i = i + 1/branchnumber
    return (outer,ringO,branchnumber)

#iterate with two lists
def growtree(ls,outer,tree):
    i=0
    for coord in ls:
        tree.append(LineString([coord,outer[i]]))
        tree.append(LineString([coord,outer[i+1]]))
        #line is the 2 branches from 1 point
        i = i + 2
        #tree = tree.union(line) #union line to tree each time

    return tree

#grow
while factor > 0:
    res = createListOuter(ring1,branchamt)
    outer = res[0]
    tree = growtree(ls,outer,line)

    ring1 = res[1]
    branchamt = res[2]
    ls = outer
    line = tree
    factor -= 1
    print 'factor: '+str(factor)

print len(res[0])
lines = unary_union(line)

# schema of the shapefile ##create in top cell
schema = {'geometry': 'MultiLineString','properties': {'test': 'int'}}
with fiona.open(savefile,'w','ESRI Shapefile', schema) as c:
       record = {'geometry':mapping(lines), 'properties':{'test':1}}
       c.write(record)