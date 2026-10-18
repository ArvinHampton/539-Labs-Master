# contrast: with the holomorphic factor (cx+d)^{-1} instead of |cx+d|^{-1}, rows with cx+d < 0 miss the period formula by 2|kappa_L(gamma'x)|/|cx+d|
import json, math
from fractions import Fraction as Fr
from cocycle_gamma import kL
rows = json.load(open('cocycle_gamma.json')); out = []
for r in rows:
    if r['cx_d'] < 0:
        L = complex(*r['lhs']); k = kL(Fr(r['x'])); miss = 2*abs(k - L)
        out.append(f"j={r['j']} k={r['k']} x={r['x']} cx+d={r['cx_d']:.3f}: |x| factor diff={r['diff']:.1e}; holomorphic factor diff={miss:.3e}")
        print(out[-1], flush=True)
open('cocycle_holfactor.txt', 'w').write('\n'.join(out) + '\n')
