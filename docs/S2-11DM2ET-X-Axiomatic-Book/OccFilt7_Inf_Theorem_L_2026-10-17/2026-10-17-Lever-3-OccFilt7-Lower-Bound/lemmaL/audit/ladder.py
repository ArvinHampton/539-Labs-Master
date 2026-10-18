"""AUDIT (Cat B): a_n(m) for all n<=N, m<M via the exact ladder A_{n+1}=A_n/(1-(-1)^n x^{n+1}),
in 80-bit long double (numpy.longdouble). Computes E_d, O_d at target d, per-n terms, and the
tilted-model local CLT error at selected n.  Validated against exact g_7 (data/exact_1000000)."""
import numpy as np, sys, json, math
LD = np.longdouble
def step(c, a, eps):
    M = len(c); R = -(-M // a); buf = np.zeros(R*a, dtype=LD); buf[:M] = c
    B = buf.reshape(R, a)
    if eps == 1: B = np.cumsum(B, axis=0)
    else:
        sg = np.where(np.arange(R) % 2 == 0, 1, -1).astype(LD)[:, None]
        B = np.cumsum(B*sg, axis=0)*sg
    return B.reshape(-1)[:M].copy()
def run(ds, M, clt_n=(), clt_u=()):
    N = int(math.isqrt(max(ds)))
    c = np.zeros(M, dtype=LD); c[0] = 1
    E = {d: LD(0) for d in ds}; O = {d: LD(0) for d in ds}; terms = {d: {} for d in ds}; clt = []
    for n in range(0, N+1):
        for d in ds:
            if n*n <= d and (d-n*n) % 7 == 0:
                v = c[(d-n*n)//7]
                terms[d][n] = v
                if n % 2 == 0: E[d] += v
                else: O[d] += v
        if n in clt_n:
            m = np.arange(M, dtype=LD)
            for u in clt_u:
                w = c*np.exp(-LD(u)/n*m); A = w.sum(); P = w/A
                mu = (P*m).sum(); var = (P*(m-mu)**2).sum(); s = np.sqrt(var)
                g = np.exp(-(m-mu)**2/(2*var))
                dev = np.max(np.abs(np.sqrt(2*np.pi)*s*P - g))
                k = int(mu); tailmass = P[-int(M*0.02):].sum()
                clt.append(dict(n=n, u=u, mu_n2=float(mu/n**2), var_n3=float(var/n**3), delta_emp=float(dev), tailmass=float(tailmass)))
                print('CLT', clt[-1], flush=True)
        if n < N or clt_n:
            c = step(c, n+1, 1 if n % 2 == 0 else -1)
    return E, O, terms, clt
