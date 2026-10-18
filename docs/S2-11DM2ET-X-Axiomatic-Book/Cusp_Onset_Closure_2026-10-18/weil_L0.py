# A(2): identify the odd-s family rep with the Weil rep of the EVEN lattice L0 = {n in Z^2 : n2 even} = (L'')^*.
#   theta_{al,be} = sum_{eps in {0,1}} e(B(al+eps e2, be)) theta^{L0}_{al+eps e2}  =>  rho_fam M = M rho_L0 (checked here),
#   and M^{-1} c = delta_0.
import numpy as np, sys, math, json
from family_s import Family
def build(s):
    F = Family(s); D = F.D; n = s*(s-2)
    gam = []; 
    for al in F.ALS:
        for eps in (0, 1):
            g = (al[0] % D, (al[1] + eps*D) % (2*D)); gam.append(g)
    gam = sorted(set(gam)); gi = {g: i for i, g in enumerate(gam)}; assert len(gam) == 4*n == F.N
    M = np.zeros((F.N, F.N), complex)
    for (al, be), i in F.IDX.items():
        for eps in (0, 1):
            g = (al[0] % D, (al[1] + eps*D) % (2*D)); gv = np.array([al[0], al[1] + eps*D])
            M[i, gi[g]] += F.e(F.B(gv, np.array(be)))
    G = [np.array(g) for g in gam]
    Bm = np.array([[float(F.B(x, y) % 1) for y in G] for x in G]); Qv = np.array([float(F.Q(x) % 1) for x in G])
    return F, M, Bm, Qv, gam, gi
def test(s):
    F, M, Bm, Qv, gam, gi = build(s); S = F.Smatrix(); T = F.Tmatrix(); n = s*(s-2)
    best = None
    for sg in (1, -1):
        SL = np.exp(2j*np.pi*sg*Bm)/math.sqrt(4*n); TL = np.diag(np.exp(2j*np.pi*sg*Qv))
        A = S@M; B = M@SL; k = np.vdot(B.ravel(), A.ravel())/np.vdot(B.ravel(), B.ravel())
        eS = np.abs(A - k*B).max(); eT = np.abs(T@M - M@TL).max()
        if best is None or eS + eT < best[0]: best = (eS + eT, sg, complex(k), eS, eT)
    c = np.zeros(F.N); c[[F.IDX[((0, 0), b)] for b in F.BES]] = 1
    x = np.linalg.solve(M, c); d0 = np.zeros(F.N); d0[gi[(0, 0)]] = 1
    return dict(s=s, sign=best[1], scalar=str(np.round(best[2], 12)), err_S=best[3], err_T=best[4], Minv_c_is_delta0=bool(np.abs(x - d0).max() < 1e-12),
                cond_M=float(np.linalg.cond(M)))
if __name__ == "__main__":
    for s in [int(z) for z in sys.argv[1].split(',')]: print(json.dumps(test(s)), flush=True)
