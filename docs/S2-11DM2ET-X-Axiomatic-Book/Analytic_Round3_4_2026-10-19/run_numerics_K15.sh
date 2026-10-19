#!/bin/bash
run() { s=$1; mP=$2; F=$3; ts=$(python3 -c "print(','.join(repr($F*f/($mP**2)) for f in (1,1.5,2,2.5,3,3.5,4)))"); python3 numerics_mp_K15.py $s 0 1 $ts; }
case $1 in I) run 20 5 0.0005;; J) run 32 4 0.0005;; K) run 8 1 0.0005;; esac
