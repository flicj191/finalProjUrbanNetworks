'''
for final project 2018
read shapefiles of created networks and get line graph
print statistics and save to file

'''
import networkx as nx
import snap, csv
import matplotlib.pyplot as plt
from datetime import datetime
##parameters
network = 'Axial_d6c0204'
shp = 'dump/cuts/'+network+ '/' +network+ '.shp'
#files =
# outputBmatrix = 'dump/'network+'outB.txt'

#read shapefile
G=nx.read_shp(shp) 
#G = nx.Graph(day="Friday") #G.graph['day']='Monday'
#G.Name = network
#creates graph
Gg = nx.Graph(G)
print nx.number_of_nodes(Gg)


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
fout =open('dump/edgelist.txt','wb')
nx.write_edgelist(Hlabeled,fout, data=False)
fout.close()

LoadedGraph = snap.LoadEdgeList(snap.PUNGraph, "dump/edgelist.txt", 0, 1, ' ') #'\t'
Triads = snap.GetTriads(LoadedGraph, -1)
ClustCf = snap.GetClustCf (LoadedGraph, -1)
print Triads, ClustCf
	
print datetime.now()
#networkx statistics:
fs = open('statsAxial.csv','ab')
fstat = csv.writer(fs)
#degreeHist = nx.degree_histogram(H)
density = nx.density(H)
print density, datetime.now() 
dia = nx.diameter(H)
print dia, datetime.now()
info = nx.info(H) #Name?
print info, datetime.now()
transi = nx.transitivity(H)
avepath = nx.average_shortest_path_length(H)

fstat.writerow([info])
fstat.writerow([dia,Triads,density,ClustCf,transi,avepath])
#record snap statistics --in csv?
fs.close()
print datetime.now()