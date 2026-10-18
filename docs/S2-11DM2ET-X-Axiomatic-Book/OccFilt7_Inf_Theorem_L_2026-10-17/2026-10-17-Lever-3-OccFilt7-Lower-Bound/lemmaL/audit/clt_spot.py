"""AUDIT (Cat B): empirical local-CLT error delta_emp = max_m |sqrt(2pi) sigma P(S=m) - exp(-(m-mu)^2/2sigma^2)|
for the tilted model at r=e^{-u/n}, from a_n(m) built with positive operations only (long double),
compared with the rigorous cell delta (verify_blocks cells) and the Lemma S enclosures of mu/n^2, sigma^2/n^3."""
import numpy as np, json, sys
sys.path.insert(0, 'rerun')
from clt import constants
LD = np.longdouble
def div1m(c, a):
    M = len(c); R = -(-M//a); b = np.zeros(R*a, dtype=LD); b[:M] = c
    return np.cumsum(b.reshape(R, a), axis=0).reshape(-1)[:M].copy()
def A_coeffs(n, M):
    c = np.zeros(M, dtype=LD); c[0] = 1
    for j in range(1, n+1, 2): c[j:] += c[:-j].copy()
    for k in range(n//2+1, n+1): c = div1m(c, 2*k)
    return c
cells = json.load(open('../route3/blocks_N900_0.3_1.6.json'))['cells'] if len(sys.argv) < 2 else None
M = 2_000_000; res = []
for n, us in [(893, [0.3, 0.6, 0.975, 1.6]), (900, [0.3, 0.6, 0.975, 1.6]), (1306, [0.6, 0.975, 1.6])]:
    c = A_coeffs(n, M); m = np.arange(M, dtype=LD)
    for u in us:
        w = c*np.exp(-LD(u)/n*m); A = w.sum(); P = w/A
        mu = (P*m).sum(); var = (P*(m-mu)**2).sum(); s = np.sqrt(var)
        dev = float(np.max(np.abs(np.sqrt(2*np.pi)*s*P - np.exp(-(m-mu)**2/(2*var)))))
        cell = [x for x in cells if x[0] <= u < x[1] or abs(x[1]-u) < 1e-12][0] if cells else None
        C = constants(u, u, 893, 0.5)
        r = dict(n=n, u=u, delta_emp=dev, delta_rig_cell=cell[3] if cell else None, mu_n2=float(mu/n**2),
                 M_enc=[float(C['M_lo']), float(C['M_hi'])], var_n3=float(var/n**3), S_enc=[float(C['S_lo']), float(C['S_hi'])],
                 tail_mass_last_5pct=float(P[-M//20:].sum()))
        r['mu_in'] = r['M_enc'][0] <= r['mu_n2'] <= r['M_enc'][1]; r['var_in'] = r['S_enc'][0] <= r['var_n3'] <= r['S_enc'][1]
        print(r, flush=True); res.append(r)
json.dump(res, open('clt_spot.json', 'w'), indent=1)
