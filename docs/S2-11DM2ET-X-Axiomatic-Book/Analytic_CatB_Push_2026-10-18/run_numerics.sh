#!/bin/bash
# Cat B support. t grid = F * (1/(mP))^2 * {1,1.5,...,4} (P = 1 at x = 0, P = 2N otherwise); F chosen per case for cost.
run() { s=$1; a=$2; N=$3; mP=$4; F=$5; ts=$(python3 -c "print(','.join(repr($F*f/($mP**2)) for f in (1,1.5,2,2.5,3,3.5,4)))"); python3 numerics_mp.py $s $a $N $ts; }
case $1 in
 A) run 8 0 1 1 0.0005; run 32 0 1 4 0.0005; run 20 0 1 5 0.0005;;
 B) run 56 0 1 7 0.0005;;
 C) run 8 1 2 4 0.0005; run 8 1 3 6 0.0005;;
 D) run 32 1 2 16 0.008;;
 E) run 32 1 3 24 0.016;;
esac
