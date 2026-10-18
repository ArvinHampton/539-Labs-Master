# Direct numerical check of the H_s radial expansion and exact q-series facts (H_5 == 0).
import numpy as np, math, pickle, sympy as sp
from fractions import Fraction as Fr
d = pickle.load(open('H_closed.pkl', 'rb')); H = d['H']; s_, g_ = sp.symbols('s g', positive=True)
def Hdirect(s, t, Qmax=None):
    Qmax = Qmax or 45/t; tot = 0.0
    cmin = min(1.0, (7*s*s-46*s+64)/(18*s)); nmax = int(math.sqrt(Qmax/cmin)) + 2
    for n in range(0, nmax+1):
        k0 = 1 if n == 0 else -(-((s-8)*n)//(3*s))       # ceil((s-8)n/(3s))
        kmax = int(math.sqrt(2*Qmax/s)) + abs(k0) + nmax + 5
        k = np.arange(k0, kmax+1)
        wt = np.where(n == 0, 0.5, np.where(3*s*k == (s-8)*n, 0.5, 1.0))
        Q2 = n*n + s*n*k + s/2*k*k
        m = Q2 <= Qmax
        if not m.any() and n > 0: continue
        tot += float(np.sum(wt[m]*(np.exp(-t*(Q2[m] + s/2*k[m])) - np.exp(-t*(Q2[m] - s/2*k[m])))))
    return tot
out = []
if __name__ == "__main__":
  pass
for s in ((5, 6, 7, 8, 9, 11, 13, 20, 25) if __name__ == "__main__" else ()):
    g = math.gcd(24, s-8); hm = float(H[-1].subs({s_: s, g_: g})); hp = float(H[1].subs({s_: s, g_: g}))
    ts = [0.02, 0.01, 0.005, 0.0025, 0.00125]
    res = [(t, (Hdirect(s, t) - hm*t**-0.5 - hp*t**0.5)/t**1.5) for t in ts]
    out.append(f"s={s} g={g}: predicted h(-1/2)={hm:.12f}, h(1/2)={hp:.12f}; (H - pred)/t^(3/2) at t={ts}: " + ", ".join(f"{r:.4f}" for _, r in res))
    print(out[-1], flush=True)
if __name__ == '__main__':
    # exact q-series: H_5 == 0 ?  (coefficients through q^2000)
    def Hseries(s, N):
        c = {}
        for n in range(-200, 201):
            for k in range(-400, 401):
                B1 = (s-2)*n; B2 = (s-8)*n - 3*s*k
                w = Fr((B1 > 0) - (B1 < 0) - ((B2 > 0) - (B2 < 0)), 2)
                if w == 0: continue
                e = Fr(2*n*n + 2*s*n*k + s*k*(k+1), 2)
                if e < N: c[e] = c.get(e, 0) + w
        return {e: v for e, v in c.items() if v != 0}
    h5 = Hseries(5, 2000); out.append(f"H_5 as a q-series through q^2000: number of nonzero coefficients = {len(h5)}  (=> H_5 == 0 exactly on this range)")
    h7 = Hseries(7, 300); out.append(f"H_7 first terms: {sorted(h7.items())[:8]}")
    print("\n".join(out[-2:])); open('H_numeric.txt', 'w').write("\n".join(out) + "\n")
