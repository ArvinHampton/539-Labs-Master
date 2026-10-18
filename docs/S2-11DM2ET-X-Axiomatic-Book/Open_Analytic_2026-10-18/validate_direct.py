# Validate asym_engine against direct summation at small t (double precision, vectorised), x = a/N.
import numpy as np, math, sys, json, mpmath as mp
from asym_engine import expansion
def Hdirect(s, t, a, N, Qmax=None):
    Qmax = Qmax or 50/t; acc = 0j
    g = math.gcd(24, s-8); m = 3*s//g; b = (s-8)//g
    cmin = min(1.0, (7*s*s-46*s+64)/(18*s)); nmax = int(math.sqrt(Qmax/cmin)) + 2
    for n in range(0, nmax+1):
        k0 = 1 if n == 0 else -(-((s-8)*n)//(3*s))
        kmax = int(math.sqrt(2*Qmax/s)) + abs(k0) + nmax + 5
        k = np.arange(k0, kmax+1, dtype=np.int64)
        wt = np.where(n == 0, 0.5, np.where(3*s*k == (s-8)*n, 0.5, 1.0))
        Qp = n*n + s*n*k + (s*k*(k+1))//2; Qm = n*n + s*n*k + (s*k*(k-1))//2
        msk = (n*n + s*n*k + s/2*k*k) <= Qmax
        if not msk.any():
            if n > 0: continue
        php = np.exp(2j*np.pi*a*(Qp[msk] % N)/N); phm = np.exp(2j*np.pi*a*(Qm[msk] % N)/N)
        acc += np.sum(wt[msk]*(php*np.exp(-t*Qp[msk]) - phm*np.exp(-t*Qm[msk])))
    return acc
if __name__ == "__main__":
    s = int(sys.argv[1]); a, N = (int(z) for z in sys.argv[2].split('/')); K = int(sys.argv[3])
    g = math.gcd(24, s-8); m = 3*s//g; P = 1 if a % N == 0 else 2*N
    c = expansion(s, a, N, K)
    out = dict(s=s, x=f"{a}/{N}", K=K, coeffs={str(e): [float(c[e].real), float(c[e].imag)] for e in c}, checks=[])
    t0 = (0.25/(m*P))**2
    for t in (16*t0, 8*t0, 4*t0, 2*t0, t0, t0/2):
        Hd = Hdirect(s, t, a, N); Ha = complex(sum(c[e]*mp.mpf(t)**(mp.mpf(e)/2) for e in c))
        res = abs(Hd - Ha); out['checks'].append(dict(t=t, H=[Hd.real, Hd.imag], resid=res, resid_over_t_pow=res/t**((K+1)/2)))
        # leading-order recovery of the top two half-integer coefficients
        rec = {}
        for etop in (K-2, K):
            low = complex(sum(c[e]*mp.mpf(t)**(mp.mpf(e)/2) for e in c if e < etop))
            rec[etop] = (Hd - low)/t**(etop/2)
        out['checks'][-1]['recovered'] = {str(k): [v.real, v.imag] for k, v in rec.items()}
        print(f"s={s} x={a}/{N} t={t:.3e}: |H - asym_K{K}| = {res:.3e} (/t^{(K+1)/2} = {res/t**((K+1)/2):.2e}); " +
              "; ".join(f"recovered t^{k}/2 = {v.real:+.6f}{v.imag:+.6f}i (engine {float(c[k].real):+.6f}{float(c[k].imag):+.6f}i)" for k, v in rec.items()), flush=True)
    json.dump(out, open(f"val_s{s}_x{a}-{N}_K{K}.json", "w"), indent=1)
