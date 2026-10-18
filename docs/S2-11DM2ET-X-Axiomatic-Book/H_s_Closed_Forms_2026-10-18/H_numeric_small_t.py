# Deeper-t check for s with g=1 (m=3s cosets => asymptotic regime needs t*m^2 small).
import math, pickle, sympy as sp
from H_numeric import Hdirect, H, s_, g_
out = []
for s, ts in ((7, [4e-4, 2e-4, 1e-4]), (9, [2e-4, 1e-4, 5e-5]), (13, [1e-4, 5e-5, 2.5e-5]), (25, [2e-5, 1e-5, 5e-6]), (41, [1e-5, 5e-6, 2.5e-6])):
    g = math.gcd(24, s-8); hm = float(H[-1].subs({s_: s, g_: g})); hp = float(H[1].subs({s_: s, g_: g}))
    r = [(t, (Hdirect(s, t, 40/t) - hm*t**-0.5 - hp*t**0.5)/t**1.5) for t in ts]
    out.append(f"s={s} g={g} m={3*s//g}: (H - pred)/t^(3/2): " + ", ".join(f"t={t:g}: {v:.4f}" for t, v in r)); print(out[-1], flush=True)
open('H_numeric_small_t.txt', 'w').write("\n".join(out) + "\n")
