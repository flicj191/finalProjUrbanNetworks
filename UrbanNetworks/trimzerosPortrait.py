'''
takes whole Bmatrix and trims zeros to create new image
'''
from datetime import datetime
import B_matrix 
#use functions generate image and matrix Bagrow code acknowledge..
import numpy as np	

f = open('outputB.txt','r')
B = np.loadtxt(f)
print B.shape, datetime.now()
N = B.shape[1]
# #Btrim = B[:maxval:] #get column index sum is >0
colsum = np.sum(B,axis=0) #array of sums

for i in np.arange(0,N-1,1): #= 1:N-1
    if colsum[i]>0:
        index = i #get index 
print index, 'max'
newB = B[:,0:index+1]

try: # plot the portrait with pylab, but I prefer matlab:
    
    B_matrix.plotMatrix(newB, origin=1, logColors=True, fileName='./../images/subsetB/'+network)
except ImportError:
    print "pylab failed, no plotting"
    
print "writing matrix to file...", outputBmatrix
B_matrix.fileMat(outputBmatrix, newB)

print datetime.now()