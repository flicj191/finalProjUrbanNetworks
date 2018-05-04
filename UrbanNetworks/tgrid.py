'''
For tgrid network creation in final project

reference stackoverflow sorting tuples

Felicity Chun
2018
'''
import numpy as np
import fiona, itertools, sys
from shapely.geometry import Point, LineString, mapping
from shapely.ops import unary_union
#parameters:
width = int(sys.argv[1]) #10
height = int(sys.argv[2])#10
freqremoved = int(sys.argv[3])#2

folder = 'outputs/'
NetType ='Tgrid'
savefile = folder + NetType +'_w'+str(width)+'_h'+str(height)+'_rm'+str(freqremoved)

x = np.linspace(10,width*10,width)
y =np.linspace(10,height*10,height)
X,Y = np.meshgrid(x,y)
X = X.reshape((np.prod(X.shape),))
Y = Y.reshape((np.prod(Y.shape),))#reshape to size of the product of shape - 9*9

coords = zip(X,Y) #list of coords
print len(coords)
#create t-junctions

verticals =[]
line = LineString()
kk=0
for i in  itertools.combinations(coords, 2): #combinations of 2 for each point
     # if distance < 14m union the line ptx-pty to line *14m or grid distance
    if Point(i[0]).distance(Point(i[1])) == 10:
#create t junctions - check y coord is same then.. i is combo- [pt1,pt2] pt is(x,y) so compare i[0][1]
        if i[0][1] == i[1][1]:
           verticals.append(i) #i is list?
        else:
            line = line.union(LineString([i[0],i[1]]))
            #line.append(LineString([i[0],i[1]]))
            #join all horizontal lines
    kk+=1
    if kk%((len(coords)**2)/10)==0:
        print kk
  
    #sort list
    #function to draw verticals
k =0
cnt = 0
for j in sorted(verticals, key=lambda tup: (tup[1][1]) ): #tuple priority?
    if k%freqremoved==0 and j[0][1]%freqremoved*10 == 0: #2 is a factor of what is joined
        cnt+=1
    elif k%freqremoved==0:
        cnt+1
    else: #join other ones
        line = line.union(LineString([j[0],j[1]])) #linestring code
        #line.append(LineString([j[0],j[1]]))
        #write with properties..
    k+=1

#lines = unary_union(line)
# schema of the shapefile ##create in top cell
schema = {'geometry': 'MultiLineString','properties': {'test': 'int'}}
with fiona.open(savefile,'w','ESRI Shapefile', schema) as c:
       record = {'geometry':mapping(line), 'properties':{'test':1}}
       c.write(record)