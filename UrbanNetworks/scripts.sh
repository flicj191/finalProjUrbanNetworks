#!/bin/bash

python ./tgrid.py 80 80 6
python ./creategraph.py 'Tgrid_w80_h80_rm6'
python ./tgrid.py 80 80 4
python ./creategraph.py 'Tgrid_w80_h80_rm4'
python ./tgrid.py 80 80 2
python ./creategraph.py 'Tgrid_w80_h80_rm2'
python ./tgrid.py 80 80 8
python ./creategraph.py 'Tgrid_w80_h80_rm8'
python ./tgrid.py 60 100 2
python ./creategraph.py 'Tgrid_w60_h100_rm2'
python ./tgrid.py 60 100 6
python ./creategraph.py 'Tgrid_w60_h100_rm6'

echo "script execution complete"

#CALL 
#batch