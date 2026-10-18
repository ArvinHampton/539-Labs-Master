# Further checks: (a) H_5 == 0 identically => all coefficients vanish at s=5; (b) compare h_{3/2} with the earlier small-t numerics
# (2026-10-18-H_s-Closed-Forms/H_numeric_small_t.txt); (c) s=8 (g=24, m=1) direct numerics for h_{5/2}.
import math, sympy as sp
from H_validate2 import hval, Hdirect
out = []
for k in (-1, 1, 3, 5): out.append(f"s=5: h_{k}/2 = {hval(k, 5):.3e}")
prev = {7: -0.2065, 9: -0.2927, 13: -0.4928, 25: -1.2701, 41: -2.6280, 11: -0.3886, 20: -0.9165, 6: -0.1664}
for s, v in prev.items(): out.append(f"s={s}: h_3/2 closed form = {hval(3, s):.6f}; earlier small-t numerics (H-pred)/t^1.5 = {v}")
s = 8; hm, hp, h3, h5 = (hval(k, s) for k in (-1, 1, 3, 5))
for t in (0.02, 0.01, 0.005, 0.0025, 0.00125):
    H = Hdirect(s, t); out.append(f"s=8 t={t}: R={(H-hm*t**-0.5-hp*t**0.5)/t**1.5:.6f} (h3/2={h3:.6f}); R2={(H-hm*t**-0.5-hp*t**0.5-h3*t**1.5)/t**2.5:.5f} (h5/2={h5:.5f})")
print("\n".join(out)); open('H_validate3.txt', 'w').write("\n".join(out) + "\n")
