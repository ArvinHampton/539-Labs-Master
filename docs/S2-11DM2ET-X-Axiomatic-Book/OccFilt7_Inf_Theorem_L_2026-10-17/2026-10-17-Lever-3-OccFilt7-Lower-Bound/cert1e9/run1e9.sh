#!/bin/bash
# sequential two-pass certification at D=1e9 (classes {0,1} then {2,4}), 4 threads
cd "$(dirname "$0")"
D=1000000000
date; free -m | head -2
for m in 3 12; do
  echo "pass mask=$m start $(date)"; free -m | sed -n 2p
  { time ./g7cert2 $D D1e9_m$m 4 16 0 $m ; } 2>&1
  echo "pass mask=$m end $(date)"
done
python3 merge.py $D D1e9_m3 D1e9_m12 D1e9.zeros
date
