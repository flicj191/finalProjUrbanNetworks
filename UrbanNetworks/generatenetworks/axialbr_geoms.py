'''
For creating a axial network for final project
Felicity Chun 
2018

axial graph 
*adjusted to create each line as separate object
    '''

from shapely.geometry import LineString, Point, mapping
from shapely.ops import unary_union
from datetime import datetime
import fiona, sys, math

## parameters
factor = 4 #sys.argv[1]
length = 500

#savefile
folder = 'outputs/'
NetType ='Axial_geoms'
savefile = folder + NetType +'_d'+str(factor)

startPt = Point(100,100)
direction = 0
alongx = True
network = LineString()
pnum = math.factorial(factor)
print math.factorial(factor), datetime.now() 
def drawBranches(factor,length,startPt,direction,alongx,network):
    #print 'running: '+str(length)
    if factor == 0:
        return network
    
    else:
        if direction%2 ==0:
            ptx = startPt.x + (length)
            pty = startPt.y + (length)  
        else:
            ptx = startPt.x - (length)
            pty = startPt.y - (length)
        
        if alongx: ##alternate up and down
            line = LineString([(startPt), (ptx,startPt.y)]) 
            alongx = False
        else:
            line = LineString([(startPt), (startPt.x, pty)])
            alongx = True
        #print line
        #network = LineString()
        record = {'geometry':mapping(line), 'properties':{'test':length}}
        c.write(record)
        
        ptls = [] #list of point objects interpolated along line by factor
        i = 1.0/(factor+1)
        while i < 0.99:
            pt = line.interpolate(i, normalized=True)
            ptls.append(pt)
            i = i+ (1.0/(factor+1)) 
            
        #print ptls
        
        if factor%2 == 0:
            length = length/(factor+2)
        else:
            length = length*0.8
        #print length
        factor -= 1
        
        for pt in ptls:
            #draw lines for each point
            direction+=1
            network = network.union(drawBranches(factor, length, pt, direction, alongx, network)) 

            
        return network


# schema of the shapefile 
schema = {'geometry': 'MultiLineString','properties': {'test': 'int'}}
c = fiona.open(savefile,'w','ESRI Shapefile', schema)

line = drawBranches(factor, length, startPt, direction, alongx, network)

print datetime.now()
