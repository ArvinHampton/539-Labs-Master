#!/bin/bash
run() { s=$1; a=$2; N=$3; mP=$4; F=$5; ts=$(python3 -c "print(','.join(repr($F*f/($mP**2)) for f in (1,1.5,2,2.5,3,3.5,4)))"); python3 numerics_mp.py $s $a $N $ts; }
case $1 in
 F) run 8 1 4 8 0.002;;
 G) run 8 1 6 12 0.004;;
 H) run 8 3 4 8 0.002;;
esac
