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
shp = 'outputs/'+network+ '/' +network+ '.shp'
#files =
outputBmatrix = 'Bmatrices/'+network+'outB.txt'

#read shapefile
G=nx.read_shp(shp) 

#creates graph
Gg = nx.Graph(G)
print nx.number_of_nodes(Gg)

### G.remove_edges_from(G.selfloop_edges()) ###
### print(nx.is_connected(G)) ###

#function to convert to representative graph
H = nx.line_graph(Gg)
H.name = network
Hlabeled = nx.convert_node_labels_to_integers(H)
#nx.write_pajek(H,'dump/pajekfiles/'+network+'.net') #pajek file to bring into SNAP
print nx.number_of_nodes(H), 'nodes'
print nx.number_of_edges(H), 'edges'
#Graph = snap.LoadPajek(snap.PUNGraph, 'example.paj')
#

#edgelist for portraits - bagrow -command line function
fout =open('edgelist.txt','wb')
nx.write_edgelist(Hlabeled,fout, data=False)
fout.close()

LoadedGraph = snap.LoadEdgeList(snap.PUNGraph, "edgelist.txt", 0, 1, ' ') #'\t'
Triads = snap.GetTriads(LoadedGraph, -1)
ClustCf = snap.GetClustCf (LoadedGraph, -1)

print Triads, ClustCf
print nx.transitivity(H), 'transivity'
print nx.average_clustering(H), 'clustering'

# fin = open('edgelist.txt','rb') #use bagrow code
# Gread = nx.read_edgelist(fin)
# fin.close()
print datetime.now()

import B_matrix 
#use functions generate image and matrix Bagrow code acknowledge..
	
B = B_matrix.portrait(Hlabeled)

try: # plot the portrait with pylab, but I prefer matlab:
    
    B_matrix.plotMatrix(B, origin=1, logColors=True, fileName='nx')
except ImportError:
    print "pylab failed, no plotting"
    
print "writing matrix to file...", outputBmatrix
B_matrix.fileMat(outputBmatrix, B)
#except:
    #print "error writing"


print datetime.now()
#networkx statistics:
fs = open('statsAxial.csv','ab')
fstat = csv.writer(fs)
#degreeHist = nx.degree_histogram(H)
density = nx.density(H)
dia = nx.diameter(H)
info = nx.info(H) #Name?
avepath = nx.average_shortest_path_length(H)

# nx.number_of_nodes(H) nx.number_of_edges(H)
fstat.writerow([info])
fstat.writerow([avepath,dia,Triads,density,ClustCf])

fs.close()
print datetime.now()