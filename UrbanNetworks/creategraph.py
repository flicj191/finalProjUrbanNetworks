'''
for final project 2018
read shapefiles of created networks and get line graph
print statistics and save to file

create portraits by creating the edgelist file for input into bagrow code

'''
import networkx as nx
import snap, csv,sys
import matplotlib.pyplot as plt
from datetime import datetime

##parameters
network = sys.argv[1]#'Tree_d15_b2'
shp = 'dump/'+network+ '/' +network+ '.shp'
lineG = True
#files =
outputBmatrix = 'Bmatrices/linegraphB/'+network+'outB.txt'

#read shapefile
G=nx.read_shp(shp) 

#creates graph
Gg = nx.Graph(G)
print nx.number_of_nodes(Gg)

#function to convert to representative graph
if lineG == True:
    H = nx.line_graph(Gg)
    print 'line'
else:
    H = Gg
H.name = network
Hlabeled = nx.convert_node_labels_to_integers(H)

if nx.is_connected(H) == False:
    print 'not connected! ...exit'
    exit()

# alldegs = dict(H.degree()).values() 
# nodes = nx.number_of_nodes(H) 
# avedeg = sum(alldegs)/float(nodes)
# print avedeg, 'avedeg'
# #exit()

#edgelist for snap
fout =open('dump/edgelist.txt','wb')
nx.write_edgelist(Hlabeled,fout, data=False)
#nx.write_adjlist(Hlabeled,fout)
fout.close()

LoadedGraph = snap.LoadEdgeList(snap.PUNGraph, "dump/edgelist.txt", 0, 1, ' ') #'\t'
Triads = snap.GetTriads(LoadedGraph, -1)
ClustCf = snap.GetClustCf (LoadedGraph, -1)

print Triads, ClustCf
transi = nx.transitivity(H)
print transi, 'transivity'
aveclust = nx.average_clustering(H)
print aveclust, 'clustering'

print datetime.now()

import B_matrix 
	
B = B_matrix.portrait(Hlabeled)

try:
    
    B_matrix.plotMatrix(B, origin=1, logColors=True, fileName='images/line/'+network)
except ImportError:
    print "pylab failed, no plotting"
    
print "writing matrix to file...", outputBmatrix
B_matrix.fileMat(outputBmatrix, B)

print datetime.now()
#networkx statistics:
fs = open('stats.csv','ab')
fstat = csv.writer(fs)
#degreeHist = nx.degree_histogram(H)
density = nx.density(H)
dia = nx.diameter(H)
#info = nx.info(H) #Name
avepath = nx.average_shortest_path_length(H)
alldegs = dict(H.degree()).values() 
nodes = nx.number_of_nodes(H) 
edges = nx.number_of_edges(H)
avedeg = sum(alldegs)/float(nodes)
#fstat.writerow([info])
print datetime.now(),"writing statistics"
fstat.writerow([network,nodes,edges,avedeg,dia,Triads,density,ClustCf,transi,avepath])

fs.close()
print datetime.now()