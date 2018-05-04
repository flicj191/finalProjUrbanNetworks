'''
for final project 2018
read shapefiles of created networks and get line graph

create portraits by creating the edgelist file for input into bagrow code

'''
import networkx as nx

#import matplotlib.pyplot as plt
from datetime import datetime
##parameters
network = 'Axial_d5'
shp = 'outputs/'+network+ '/' +network+ '.shp'
#files =
outputBmatrix = 'Bmatrices/'+network+'outB.txt'

#read shapefile
G=nx.read_shp(shp) 
#G = nx.Graph(day="Friday") #G.graph['day']='Monday'
G.name = network
#creates graph
Gg = nx.Graph(G)
print nx.number_of_nodes(Gg)


#function to convert to representative graph
H = nx.line_graph(Gg)
Hlabeled = nx.convert_node_labels_to_integers(H)
print nx.number_of_edges(H), 'edges'
H.remove_edges_from(H.selfloop_edges())
print nx.number_of_edges(H), 'edges'
print nx.is_connected(H)
exit()
print nx.number_of_nodes(H), 'nodes'
print nx.number_of_edges(H), 'edges'

#edgelist for portraits - bagrow -command line function
# fout =open('edgelist.txt','wb')
# nx.write_edgelist(Hlabeled,fout, data=False)
# fout.close()

# fin = open('edgelist.txt','rb') #use bagrow code
# Gread = nx.read_edgelist(fin)
# fin.close()

print datetime.now()
import B_matrix 
#use functions generate image and matrix Bagrow code acknowledge..
	
B = B_matrix.portrait(Hlabeled)

try: # plot the portrait with pylab, but I prefer matlab:
    
    B_matrix.plotMatrix(B, origin=1, logColors=True, fileName='images/'+network+'test')
except ImportError:
    print "pylab failed, no plotting"
    
print "writing matrix to file...", outputBmatrix
B_matrix.fileMat(outputBmatrix, B)
#except:
    #print "error writing"

print datetime.now()

