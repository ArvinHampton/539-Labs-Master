#!/bin/bash
# runs exact u_L test with criterion data, one process per s
for s in "$@"; do
  timeout 3000 python3 uL_rayclass_exact.py $s 1 20000 > logs/run_$s.log 2>&1 &
done
wait
