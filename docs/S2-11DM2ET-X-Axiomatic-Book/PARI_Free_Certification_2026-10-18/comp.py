# From-scratch Fourier data of the 140 components u_{al,be} (lattice side; no PARI, no reuse of uvec):
#   coefficient at frequency Q:  (1/2) sum_{i in {0,1}} sum_{C in F,-F,T,-T} sum_{nu in C cap (g^-i al + Z^2), Q(nu)=Q} e(B(nu, g^-i be))
# F = [e1, g e1), T = [f, g f), f = (1,-1), g = [[-1,-7],[2,13]].  Every nu is returned with its element beta_nu = (2X+7Y) + Y sqrt35,
# (X,Y) = 70 nu, N(beta_nu) = 19600 Q(nu).
import numpy as np, sys
sys.dont_write_bytecode = True
GI = np.array([[13, 7], [-2, -1]])
def labels():
    sys.path.insert(0, '/workspace/quantum-comp/reports/heavy-daily/2026-10-17-cusp-part')
    from family import LABELS          # label list only (pure definitions, PARI-free)
    return LABELS
def masks(N1, N2):
    F = (2*N1+N2 > 0) & (N2 >= 0)
    T = (11*N1+6*N2 > 0) & (N1+N2 <= 0)
    return [F, (-2*N1-N2 > 0) & (-N2 >= 0), T, (-11*N1-6*N2 > 0) & (-N1-N2 <= 0)]
def points(al70, be70, Qmax):
    """arrays N1, N2 (70 nu), q19600 (=19600 Q signed), phase (complex, includes weight 1/2)"""
    out = []
    al = np.array(al70); be = np.array(be70)
    B = int(14*np.sqrt(Qmax)) + 4
    m = np.arange(-B, B+1)
    for i in range(2):
        M1, M2 = np.meshgrid(m, m, indexing='ij')
        N1 = (al[0] % 70) + 70*M1.ravel(); N2 = (al[1] % 70) + 70*M2.ravel()
        q = 2*(2*N1*N1 + 14*N1*N2 + 7*N2*N2)
        keep = (np.abs(q) <= 19600*Qmax) & (q != 0)
        mk = masks(N1, N2); sel = keep & (mk[0] | mk[1] | mk[2] | mk[3])
        n1, n2, qq = N1[sel], N2[sel], q[sel]
        bb = (n1*(2*be[0]+7*be[1]) + n2*(7*be[0]+7*be[1])) % 4900
        out.append((n1, n2, qq, 0.5*np.exp(2j*np.pi*bb/4900)))
        al = GI @ al; be = GI @ be
    return [np.concatenate([o[k] for o in out]) for k in range(4)]
