# search affine monomial label maps (al,be) -> (k al + t, k be + t2), reduced with phase, commuting with S and T
import numpy as np, math, sys
from cert_rank import XF, numeric_U
def U_aff(F, k, t, t2):
    perm = np.zeros(F.N, int); ph = []
    for i, (al, be) in enumerate(F.LABELS):
        a2 = (k*np.array(al) + np.array(t)) % F.D
        try: j, f = F.reduce_fr(a2, k*np.array(be) + np.array(t2))
        except (ValueError, KeyError): return None
        perm[i] = j; ph.append(f % 1)
    if len(set(perm)) != F.N: return None
    return perm, ph
def search(s, extra_phase=True):
    F = XF(s); S = F.Smatrix(); T = F.Tmatrix(); D = F.D
    cvec = np.zeros(F.N); cvec[[F.IDX[((0, 0), b)] for b in F.BES]] = 1
    found = []
    ks = [k for k in range(1, 2*D) if math.gcd(k, D) == 1 and (k*k) % (D) == 1]
    for k in ks:
        for t in F.ALS:
            for t2 in F.BES:
                r = U_aff(F, k, t, t2)
                if r is None: continue
                U = numeric_U(F, *r)
                # allow an overall diagonal character correction: test commutation up to a diagonal gauge is hard; test exact
                if np.abs(U@T - T@U).max() < 1e-9 and np.abs(U@S - S@U).max() < 1e-9:
                    found.append((k, t, t2, bool(np.abs(U@cvec - cvec).max() < 1e-9)))
    return found
if __name__ == "__main__":
    for s in [int(z) for z in sys.argv[1].split(',')]:
        f = search(s); print(s, len(f), f[:12], flush=True)
