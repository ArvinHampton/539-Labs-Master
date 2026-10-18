# Compare the symbolic H_{7/2} (H_closed3.pkl) with the exact-term engine values at several s.
import pickle, sympy as sp, math, mpmath as mp
from asym_engine import expansion
res = pickle.load(open('H_closed3.pkl', 'rb')); s_, g_ = sp.symbols('s g', positive=True)
out = []
for s in (6, 7, 8, 9, 10, 11, 13, 20, 25):
    g = math.gcd(24, s-8); A, B = res[7]
    v = float(sp.sqrt(2*sp.pi*s)*(A + B*sp.sqrt((s_-2)*(7*s_-32))).subs({s_: s, g_: g}).evalf(30))
    e = float(expansion(s, 0, 1, 7)[7].real)
    out.append(f"s={s}: H_7/2 closed = {v:.15g}   engine = {e:.15g}   diff = {abs(v-e):.1e}"); print(out[-1], flush=True)
A, B = res[7]; out.append(f"H_{{7/2}} = sqrt(2 pi s) * [ {A}  +  ({B}) * sqrt((s-2)(7s-32)) ]")
open('check_t72.txt', 'w').write("\n".join(out) + "\n")
