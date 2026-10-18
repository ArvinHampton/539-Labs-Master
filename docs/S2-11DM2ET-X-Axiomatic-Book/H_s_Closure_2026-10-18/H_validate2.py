# Validation of H_{3/2}, H_{5/2}: (i) generic Bernoulli sums Sx_p = Sy_p = m^{1-p} B_p for p<=6 vs exact per-s sums;
# (ii) direct numerics: R(t) = (H - h_{-1/2} t^{-1/2} - h_{1/2} t^{1/2}) / t^{3/2} -> h_{3/2} (integer orders t^0, t^1 vanish; t^2 unknown => O(t^{1/2}) drift).
import numpy as np, math, pickle, sympy as sp, mpmath as mp
s_, g_ = sp.symbols('s g', positive=True)
res = pickle.load(open('H_closed2.pkl', 'rb'))
def hval(k, s):
    g = math.gcd(24, s-8); A, B = res[k]
    return float(sp.sqrt(2*sp.pi*s)*(A + B*sp.sqrt((s-2)*(7*s-32))).subs({s_: s, g_: g}))
def bern_ok(sv, Pm=6):
    gv = math.gcd(24, sv-8); mv = 3*sv//gv; bv = (sv-8)//gv
    Bt = lambda p, x: (sp.bernoulli(p, 0) + sp.bernoulli(p, 1))/2 if x == 0 else sp.bernoulli(p, x)
    xs = [sp.Rational((-bv*j) % mv, mv) for j in range(mv)]; ys = [sp.Rational(j, mv) for j in range(mv)]
    for p in range(1, Pm+1):
        gen = 0 if p == 1 else sp.Rational(mv)**(1-p)*sp.bernoulli(p)
        if sum(Bt(p, x) for x in xs) != gen or sum(Bt(p, y) for y in ys) != gen: return False
    return True
def Hdirect(s, t, Qmax=None):
    Qmax = Qmax or 60/t; tot = mp.mpf(0)
    cmin = min(1.0, (7*s*s-46*s+64)/(18*s)); nmax = int(math.sqrt(Qmax/cmin)) + 2
    acc = 0.0; comp = 0.0
    for n in range(0, nmax+1):
        k0 = 1 if n == 0 else -(-((s-8)*n)//(3*s))
        kmax = int(math.sqrt(2*Qmax/s)) + abs(k0) + nmax + 5
        k = np.arange(k0, kmax+1, dtype=np.float64)
        wt = np.where(n == 0, 0.5, np.where(3*s*k == (s-8)*n, 0.5, 1.0))
        Q2 = n*n + s*n*k + s/2*k*k
        m = Q2 <= Qmax
        if not m.any() and n > 0: continue
        v = np.sum(wt[m]*(np.exp(-t*(Q2[m] + s/2*k[m])) - np.exp(-t*(Q2[m] - s/2*k[m]))))
        y = v - comp; tt = acc + y; comp = (tt - acc) - y; acc = tt
    return acc
if __name__ == "__main__":
    out = []
    bad = [sv for sv in list(range(5, 81)) + [99, 100, 151, 223, 300] if not bern_ok(sv)]
    out.append(f"[{'PASS' if not bad else 'FAIL'}] generic Bernoulli sums p<=6 for s=5..80,99,100,151,223,300: mismatches {bad}")
    print(out[-1], flush=True)
    for s in (6, 7, 9, 11, 13, 20):
        hm, hp, h3, h5 = (hval(k, s) for k in (-1, 1, 3, 5))
        ts = [0.04, 0.02, 0.01, 0.005]
        R = [(Hdirect(s, t) - hm*t**-0.5 - hp*t**0.5)/t**1.5 for t in ts]
        R2 = [(Hdirect(s, t) - hm*t**-0.5 - hp*t**0.5 - h3*t**1.5)/t**2.5 for t in ts]
        out.append(f"s={s}: h_3/2={h3:.10f}; R(t) at t={ts}: " + ", ".join(f"{r:.7f}" for r in R) + f" | h_5/2={h5:.8f}; R2(t): " + ", ".join(f"{r:.5f}" for r in R2))
        print(out[-1], flush=True)
    open('H_validate2.txt', 'w').write("\n".join(out) + "\n")
