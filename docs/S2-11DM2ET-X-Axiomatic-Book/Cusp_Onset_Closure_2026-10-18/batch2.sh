#!/bin/bash
# re-run incomplete cases with larger Nmax (output files get suffix via separate dir)
mkdir -p big; cd big; cp ../uL_rayclass_exact.py .
for s in "$@"; do timeout 6000 python3 uL_rayclass_exact.py $s 1 80000 > run_$s.log 2>&1 & done; wait
