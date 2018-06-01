'''
to create a grid network for final project

reference stackoverflow sorting tuples(jupyter)

Felicity Chun
2018
'''

import numpy as np
import itertools, fiona, sys
from shapely.geometry import Point, LineString, mapping
from datetime import datetime

#parameters:
width = int(sys.argv[1])
height = int(sys.argv[2])
#savefile name create
folder = 'outputs/'
NetType ='grid'
savefile = folder + NetType +'_w'+str(width)+'_h'+str(height)

x = np.linspace(10,width*10,width)
y = np.linspace(10,height*10,height)
X,Y = np.meshgrid(x,y)
X = X.reshape((np.prod(X.shape),))
Y = Y.reshape((np.prod(Y.shape),))

coords = zip(X,Y) #list of coords
print len(coords)

line = LineString()
progress = (len(coords)**2)/10
k=0
print datetime.now()
for i in  itertools.combinations(coords, 2): #combinations of 2 for each point
     # if distance < the spacing union the line ptx-pty to line 
    if Point(i[0]).distance(Point(i[1])) < 11:
        line = line.union(LineString([(i[0]), (Point(i[1]).x, Point(i[1]).y)]))
    
    k+=1
    if k%progress == 0:
        print k, datetime.now()
            
     
print datetime.now()
# schema of the shapefile ##create in top cell
schema = {'geometry': 'MultiLineString','properties': {'test': 'int'}}
with fiona.open(savefile,'w','ESRI Shapefile', schema) as c:
       record = {'geometry':mapping(line), 'properties':{'test':1}}
       c.write(record)