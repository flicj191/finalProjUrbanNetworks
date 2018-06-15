### Final semester Project 
# Generate Urban Networks
Felicity Chun 2018

scripts are run with conda installation and python2.7 environment

## UrbanNetworks/generatenetworks

Scripts in this folder are used to generate networks
- `axialbr_geoms.py` was not used in the project, it generates each line as a separate object

## UrbanNetworks/functions
The following scripts are the function scripts and are usually run in the main folder

- `function-cut.py`
- `function-join.py`

##  UrbanNetworks
Other scripts are for graph statistics, B-matrix and portrait generation and clustering.

- `B_matrix.py`
From Bagrow(2008) <https://github.com/bagrow/portraits>
- `creategraph.py`
takes shapefile as input and generates B-matrix, portrait and graph statistics
- `createportrait.py`
takes shapefile to generate B-matrix and trims to output trimmed portrait
- `dendrogram.py`
takes an adjacency list and creates dendrogram with numbers and network names in text file
- `scripts.sh`
used to run program multiple times in succession

## UrbanNetworks/distance-matlab
Matlab files used to create adjacency list file.
- `createdistList.m`
Other files from [Bagrow(2008)](https://github.com/bagrow/portraits)

