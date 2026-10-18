# Path B closure, x != 0 (Cat B numerics): radial expansion of H_s(e(x) e^{-t}) at x = 1/2, 1/3 by least-squares fits in powers t^{k/2}.
# H_s(q) = sum_{K} w(v) (q^{Q2+lam k} - q^{Q2-lam k}),  Q2 +- lam k integers; q = e(x) e^{-t}.
import numpy as np, math, json, sys
def Hx(s, t, x, Qmax=None):
    Qmax = Qmax or 60/t; acc = 0j
    cmin = min(1.0, (7*s*s-46*s+64)/(18*s)); nmax = int(math.sqrt(Qmax/cmin)) + 2
    for n in range(0, nmax+1):
        k0 = 1 if n == 0 else -(-((s-8)*n)//(3*s))
        kmax = int(math.sqrt(2*Qmax/s)) + abs(k0) + nmax + 5
        k = np.arange(k0, kmax+1, dtype=np.int64)
        wt = np.where(n == 0, 0.5, np.where(3*s*k == (s-8)*n, 0.5, 1.0))
        Q2 = n*n + s*n*k + (s*k*k)//2 if s % 2 == 0 else None
        Qp = n*n + s*n*k + (s*k*(k+1))//2; Qm = n*n + s*n*k + (s*k*(k-1))//2
        Q2f = n*n + s*n*k + s/2*k*k
        m = Q2f <= Qmax
        if not m.any() and n > 0: continue
        ph_p = np.exp(2j*np.pi*((x[0]*(Qp[m] % x[1])) % x[1])/x[1]); ph_m = np.exp(2j*np.pi*((x[0]*(Qm[m] % x[1])) % x[1])/x[1])
        acc += np.sum(wt[m]*(ph_p*np.exp(-t*Qp[m]) - ph_m*np.exp(-t*Qm[m])))
    return acc
def fit(s, x, ts, powers):
    H = np.array([Hx(s, t, x) for t in ts]); A = np.array([[t**p for p in powers] for t in ts])
    c, *_ = np.linalg.lstsq(A, H, rcond=None); return c
if __name__ == "__main__":
    out = []
    powers = [-1, -0.5, 0, 0.5, 1, 1.5, 2]
    for x in ((1, 2), (1, 3)):
        for s in (5, 6, 7, 8, 9, 10, 12):
            g = math.gcd(24, s-8); m = 3*s//g
            tmax = min(0.02, 0.3/m**2); ts = np.geomspace(tmax/40, tmax, 24)
            c1 = fit(s, x, ts, powers); c2 = fit(s, x, ts[4:], powers[:-1])
            line = f"x={x[0]}/{x[1]} s={s} (m={m}): " + "; ".join(f"t^{p}: {c1[i].real:+.6f}{c1[i].imag:+.6f}i" for i, p in enumerate(powers[:4])) + \
                   " | stability (drop t^2, fewer pts): " + "; ".join(f"{abs(c1[i]-c2[i]):.1e}" for i in range(4))
            out.append(line); print(line, flush=True)
    open('H_x.txt', 'w').write("\n".join(out) + "\n")
