'''
For creating a branching tree in final project
Felicity Chun
2018

adjustments on radial script to create tree growing in circular rings
using written functions: 
- createListOuter
- growtree

'''

from datetime import datetime
from shapely.geometry import Point, LineString, MultiPoint, mapping

import fiona, sys

# parameters ##
factor = int(sys.argv[1]) #5 depth the tree grows to
intbranch = int(sys.argv[2]) #2
branchamt = float(intbranch) #amount of branches for each node

folder = 'outputs/'
NetType ='Tree'
savefile = folder + NetType +'_d'+str(factor)+'_b'+str(intbranch)

# create point (100,100) and buffer a distance

center = Point(100,100)
ring1 = center.buffer(10)
ls = []
i=0
line = LineString()
while i < 1: 
    ptOnRing = ring1.boundary.interpolate(i, normalized=True)
    ls.append((ptOnRing.x,ptOnRing.y)) #ls point objects
    i += 1/branchamt #parameter
    line = line.union(LineString([(center.x,center.y),(ptOnRing.x,ptOnRing.y)]))

#create list on outer ring
def createListOuter(ring1,branchamt):
    outer = []
    i = 0
    ringO = ring1.buffer(10)
    branchnumber = branchamt * intbranch
    while i < 1:
        ringPt = ringO.boundary.interpolate(i, normalized=True)
        outer.append((ringPt.x,ringPt.y))
        i = i + 1/branchnumber
    return (outer,ringO,branchnumber)

#iterate with two lists
def growtree(ls,outer,tree):
    i=0
    for coord in ls:
        if i < (len(outer)-intbranch+1):
            for j in range(i,i+intbranch):
                tree = tree.union(LineString([coord,outer[j]]))
        
        i = i + intbranch

    return tree

#grow tree
while factor > 0:
    res = createListOuter(ring1,branchamt)
    outer = res[0]
    tree = growtree(ls,outer,line)

    ring1 = res[1]
    branchamt = res[2]
    ls = outer
    line = tree
    factor -= 1
    print 'factor: ',str(factor), datetime.now()

print len(res[0])

# schema of the shapefile
schema = {'geometry': 'MultiLineString','properties': {'test': 'int'}}
with fiona.open(savefile,'w','ESRI Shapefile', schema) as c:
       record = {'geometry':mapping(line), 'properties':{'test':1}}
       c.write(record)