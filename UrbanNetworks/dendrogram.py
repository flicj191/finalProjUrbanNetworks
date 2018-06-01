'''
'''

import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
# https://stackoverflow.com/questions/11917779/how-to-plot-and-annotate-hierarchical-clustering-dendrograms-in-scipy-matplotlib
# https://stackoverflow.com/questions/41416498/dendrogram-or-other-plot-from-distance-matrix

from scipy.spatial.distance import squareform

import networkx as nx
import scipy 

fe = open('Bmatrices/sample30distance.txt','rb')
Gdist = nx.read_weighted_edgelist(fe)
nodes = Gdist.nodes()
lnodes = list(nodes)
D = nx.adjacency_matrix(Gdist,weight='weight')
ND = nx.to_numpy_matrix(Gdist, weight='weight')
print lnodes
print ND.shape
# fn = open('allnodes.txt','wb')
# i=0
# for n in nodes:
#     fn.write(str(i)+' ' +n+'\n')
#     i+=1
# fn.close()
# exit()

f = open('my_data.txt','r')
mat = np.loadtxt(f)
print mat.shape
#print mat

# https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.loadtxt.html
# scipy.io.loadmat()
#mat = np.array([[0.0, 2.0, 0.1], [2.0, 0.0, 2.0], [0.1, 2.0, 0.0]])
dists = squareform(ND)


linkage_matrix = linkage(dists, "single")
#ls = ["0", "1", "2"]
ls = ['grid_w40_h40',
    'grid_w60_h60',
    'grid_w100_h80',
    'Tgrid_w40_h40_rm2',
    'Tgrid_w60_h100_rm2',
    'Tgrid_w100_h80_rm2',
    'Tree_d6_b3',
    'Tree_d7_b3',
    'Tree_d8_b3',
    'Radial_d6_b5',
    'Radial_d8_b5',
    'Radial_d10_b5',
    'Axial_d6',
    'Axial_d6Axial_d6',
    'Axial_d7']
dendrogram(linkage_matrix, labels=lnodes,leaf_rotation=90)
plt.title("")
plt.savefig('dendro')
plt.show()
