# scalar label maps U_k: (al,be) -> (k al, k be) reduced, k up to 2D^2; which commute with S,T and fix c; resulting fixed-space dims
import numpy as np, math, sys, json
from cert_rank import XF, numeric_U, closure
from affine_sym import U_aff
def run(s):
    F = XF(s); S = F.Smatrix(); T = F.Tmatrix(); D = F.D
    cvec = np.zeros(F.N); cvec[[F.IDX[((0, 0), b)] for b in F.BES]] = 1
    res = {}; mats = {}
    for k in range(1, 2*D*D):
        if math.gcd(k, D) != 1 or (k*k) % D != 1: continue
        r = U_aff(F, k, (0, 0), (0, 0))
        if r is None: continue
        key = (tuple(r[0]), tuple(r[1]))
        if key in mats: continue
        U = numeric_U(F, *r)
        if np.abs(U@T - T@U).max() < 1e-9 and np.abs(U@S - S@U).max() < 1e-9:
            mats[key] = (k, U, bool(np.abs(U@cvec - cvec).max() < 1e-9))
    good = [U for (k, U, fc) in mats.values() if fc]
    P = F.Pmatrix(); assert np.abs(P@S-S@P).max()<1e-9 and np.abs(P@T-T@P).max()<1e-9 and np.abs(P@cvec-cvec).max()<1e-9
    good.append(P)
    G = closure(good)
    dimFix = int(round(np.trace(sum(G)/len(G)).real))
    return dict(s=s, N=F.N, ks=sorted(k for (k, U, fc) in mats.values()), ks_fix_c=sorted(k for (k, U, fc) in mats.values() if fc), group=len(G), dimFix=dimFix)
if __name__ == "__main__":
    for s in [int(z) for z in sys.argv[1].split(',')]:
        print(json.dumps(run(s)), flush=True)
