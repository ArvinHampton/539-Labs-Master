# refined parity fit: sqrt(t)*q^8f(e(x)e^{-t}) vs powers of sqrt(t); odd powers (-> integer powers of t in q^8 f) should vanish
import numpy as np, math, sys
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
from parity_check import series_vals
from radial import Cthird_exp
out = []
for x in (Fr(0), Fr(1, 3), Fr(1, 2), Fr(1, 7)):
    ts = np.geomspace(4e-4, 1.2e-2, 18)
    v = np.array([math.sqrt(t)*series_vals(x, t, 'F') for t in ts])
    for deg in (6, 8):
        A = np.stack([ts**(j/2) for j in range(deg)], axis=1).astype(complex)
        c, *_ = np.linalg.lstsq(A, v, rcond=None)
        out.append(f"x={x} deg {deg}: coeffs of t^(j/2), j=0..{deg-1} in sqrt(t)*q8f: " + ", ".join(f"{abs(cc):.1e}" for cc in c))
    out.append(f"   exact t^-1/2 coefficient of q8f = 2 h_C: {abs(2*Cthird_exp(x)[1]):.10f}")
print("\n".join(out)); open('parity_fit2.txt', 'w').write("\n".join(out)+"\n")
