# u_L = u_(a,0) cusp test via prime periodicity (function-level, Hecke/Chebotarev criterion).
# Coefficient of u_L at mode q (q = Q2(nu), nu in a+Z^2) counts nu in (F u -F) (F=[e1,gamma e1)) for q>0, and nu in
# (G u -G) (G=[f,gamma f), f=(1,-1)) for q<0.  Normalised integer norm N = (4(s-2)Q_s - s)/g0 with Q_s = Q2+c0.
# Eisenstein (genus) part => count at prime |N|=p depends only on (sign, p mod L) (genus characters are psi o Norm with
# psi of modulus dividing L).  Any cusp (non-genus ray-class) content => variation inside a residue class (Chebotarev).
# Robustness: test at L and multiples kL; persisting violations at all k = cusp content.
import numpy as np, math, sys, json, sympy
from math import gcd
def sqfree_part(n):
    f = sympy.factorint(n); c = 1; d = 1
    for p, e in f.items():
        d *= p**(e % 2); c *= p**(e//2)
    return d, c
def run(s, Pmax, ks=(1, 2, 3, 5)):
    d = 2*(s-2); g0 = gcd(4*(s-2), s)
    kappa = 4*(s-2)//g0
    lam = s-1+math.sqrt(s*s-2*s)
    G = np.array([[-1, -s], [2, 2*s-1]])
    Dfull = s*s-2*s; D0, c = sqfree_part(Dfull)
    dK = D0 if D0 % 4 == 1 else 4*D0
    L = 2*(4*d*c*dK)//gcd(4*d*c, dK)
    Xmax = Pmax/kappa
    # nu = a + (n,k); a = (s/(2(s-2)), -1/(s-2)); work with X = d*nu integer: X = (s + d n, -2 + d k)
    def Q2(x, y): return x*x + s*x*y + 0.5*s*y*y
    counts = {}
    for sign_cone, base in ((1, (1, 0)), (-1, (1, -1))):
        b1 = np.array(base, float); b2 = G @ b1
        # bounding radius: min |Q2| on cone directions
        th = np.linspace(0, 1, 20001)
        dirs = np.outer(1-th, b1) + np.outer(th, b2); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
        qmin = np.min(np.abs(Q2(dirs[:, 0], dirs[:, 1])))
        R = math.sqrt(Xmax/qmin) + 2
        det = b1[0]*b2[1]-b1[1]*b2[0]
        for sgn in (1, -1):
            for x0 in (s, ):
                pass
            n = np.arange(-int(R)-2, int(R)+3)
            for kk in range(-int(R)-2, int(R)+3):
                X = (s + d*n)/d; Y = np.full_like(X, (-2 + d*kk)/d)
                vx, vy = sgn*X, sgn*Y   # nu in sgn*cone  <=>  sgn*nu in cone
                # coordinates of (vx,vy) in basis b1,b2: nu = u b1 + w b2
                u = (vx*b2[1]-vy*b2[0])/det; w = (b1[0]*vy-b1[1]*vx)/det
                m = (u > 1e-12) & (w > -1e-12)
                if not m.any(): continue
                q = Q2(X[m], Y[m])
                q = q[np.abs(q) <= Xmax]
                # integer norm: N = kappa*Q2 exactly; compute exactly in integers via d*nu
                for qq in q:
                    Nn = int(round(kappa*qq))
                    counts[Nn] = counts.get(Nn, 0) + 1
    primes = list(sympy.primerange(3, Pmax))
    out = {"s": s, "kappa": kappa, "D0": D0, "c": c, "dK": dK, "L": L, "Pmax": Pmax}
    for k in ks:
        Lk = L*k
        by = {}
        for sg in (1, -1):
            for p in primes:
                if Lk % p == 0: continue
                by.setdefault((sg, p % Lk), set()).add(counts.get(sg*p, 0))
        hit = [r for r, v in by.items() if max(v) > 0]
        mixed = [r for r, v in by.items() if len(v) > 1]
        out[f"k={k}"] = {"classes_hit": len(hit), "classes_mixed": len(mixed),
                         "frac_mixed_of_hit": round(len(mixed)/max(1, len(hit)), 3),
                         "example": [(r, sorted(by[r])) for r in mixed[:3]]}
    # density of represented primes (Eis-pure genus theta: represented primes = whole residue classes)
    return out
if __name__ == "__main__":
    s = int(sys.argv[1]); P = int(float(sys.argv[2]))
    r = run(s, P); print(json.dumps(r), flush=True)
