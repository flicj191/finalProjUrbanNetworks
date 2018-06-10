'''
for final project 2018
read shapefiles of created networks and get line graph

create portraits 
and trimming zeros to get subset of graph

using code from Bagrow

'''
import networkx as nx
import sys
#import matplotlib.pyplot as plt
from datetime import datetime
##parameters
network = sys.argv[1] #'Axial_d6Radial_d6_b5'
shp = network+ '/' +network+ '.shp'
#in folder with shapefile
outputBmatrix = './../Bmatrices/subsetB/'+network+'outB.txt'

#read shapefile
G=nx.read_shp(shp) 
G.name = network
#creates graph
Gg = nx.Graph(G)

#function to convert to representative graph
H = nx.line_graph(Gg)
Hlabeled = nx.convert_node_labels_to_integers(H)

print datetime.now()
import B_matrix 
	
B = B_matrix.portrait(Hlabeled)
import numpy as np
print B.shape, datetime.now()
N = B.shape[1]
# #Btrim = B[:maxval:] #get column index sum is >0
colsum = np.sum(B,axis=0) #array of sums

for i in np.arange(0,N-1,1): #= 1:N-1
    if colsum[i]>0:
        index = i #get index 
print index, 'max'
newB = B[:,0:index+1]
print newB.shape
try: # plot the portrait with pylab, but I prefer matlab:
    
    B_matrix.plotMatrix(newB, origin=1, logColors=True, fileName='./../images/subsetB/'+network)
except ImportError:
    print "pylab failed, no plotting"
    
print "writing matrix to file...", outputBmatrix
B_matrix.fileMat(outputBmatrix, newB)

print datetime.now()

