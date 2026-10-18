# Where does C_third have a finite radial limit?  Need s_C(x) = 0 (no 1/t) and h_C(x) = 0 (no t^{-1/2}).
import math, sys
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
from radial import Cthird_exp, G
out = []; both = []; cnt = {'s=0': 0, 'h=0': 0, 'tot': 0}
for m in range(1, 41):
    for h in range(0, m):
        if math.gcd(h, m) != 1: continue
        x = Fr(h, m); s, hh, c = Cthird_exp(x); cnt['tot'] += 1
        zs = abs(s) < 1e-12; zh = abs(hh) < 1e-12
        cnt['s=0'] += zs; cnt['h=0'] += zh
        if zs and zh: both.append(str(x))
        if zh and not zs: out.append(f"h=0 but s!=0 at {x}")
txt = [f"rationals h/m in [0,1), m <= 40: {cnt['tot']}; with s_C = 0: {cnt['s=0']} (exactly 2|m or 5|m, Theorem G); with h_C = 0: {cnt['h=0']}; with both (finite radial limit): {len(both)} {both[:20]}"] + out[:20]
print("\n".join(txt)); open('scan.txt', 'w').write("\n".join(txt)+"\n")
