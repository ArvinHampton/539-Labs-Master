#!/bin/bash
# N2: exact rational rank of the orbit-theta coefficient matrix, s = 35..50 (Qmax 45); s = 50 also at Qmax 60 for stability.
for s in 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49; do timeout 3000 python3 vrank.py $s 45 > vrank_${s}_q45.log 2>&1; done
timeout 3000 python3 vrank.py 50 60 > vrank_50_q60.log 2>&1
