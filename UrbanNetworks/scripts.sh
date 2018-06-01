#!/bin/bash

python ./generatenetworks/gridx.py 80 100
python ./../createportrait.py Tree_d10_b2
python ./../createportrait.py Tree_d12_b2

# i=1;
# for d in * ; do
#     echo "$d"
#     python ./../createportrait.py "$d"
#     echo $i
#     i=$((i+1))
# done


echo "script execution complete"

#CALL 
#batch