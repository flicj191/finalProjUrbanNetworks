'''
for final project 2018
generate clustering with dendrogram
reads an adjacency list and uses networkx to create a distance matrix

ref:
# https://stackoverflow.com/questions/11917779/how-to-plot-and-annotate-hierarchical-clustering-dendrograms-in-scipy-matplotlib
# https://stackoverflow.com/questions/41416498/dendrogram-or-other-plot-from-distance-matrix
# https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.cluster.hierarchy.dendrogram.html
'''

import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

from scipy.spatial.distance import squareform

import networkx as nx
import scipy 

fe = open('Bmatrices/clustering/sample30distance.txt','rb')
Gdist = nx.read_weighted_edgelist(fe)
nodes = Gdist.nodes()
lnodes = list(nodes)
D = nx.adjacency_matrix(Gdist,weight='weight')
ND = nx.to_numpy_matrix(Gdist, weight='weight')
#print lnodes
print ND.shape

#print numbers and their respective networks
fn = open('label30nodes.txt','wb')
i=0
for n in nodes:
    fn.write(str(i)+' ' +n+'\n')
    i+=1
fn.close()
# exit()

f = open('my_data.txt','r') #load a distance matrix
mat = np.loadtxt(f)
print mat.shape
#print mat

dists = squareform(ND)


linkage_matrix = linkage(dists, "single")

dendrogram(linkage_matrix ,leaf_rotation=90)  #labels=lnodes #option to label nodes
plt.title("")
plt.savefig('dendro30')
plt.show()
