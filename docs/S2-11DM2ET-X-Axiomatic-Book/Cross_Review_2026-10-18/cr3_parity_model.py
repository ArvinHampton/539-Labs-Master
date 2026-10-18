# Cross-review check (odd s): local parity model for the lift span.
# (1) EXACT: on L'/Z^2 (cyclic of order n=s(s-2) for odd s) the unit gamma acts on the p-primary part
#     by the scalar s-1 mod p^e, i.e. -1 for p|s and +1 for p|(s-2).  (Checked by direct computation.)
# (2) EXACT: dim Fix(P) from the stored-style P matrix vs 2(n+1).
# (3) MODEL (Cat B): sectors = parity vectors (eps_p) on the prime powers of n, times the 2-adic theta
#     characteristics (A3: 3 even chars, B1: odd char).  P = prod_p Z_p (x) I4 ; gamma = prod_{p|s} Z_p (x) Z2.
#     V = Fix(P) cap Fix(gamma) ; Eis = A3 (x) (all even) ; cusp = the rest.  Compare with Cusp-Onset table.
import math, json, itertools
import numpy as np
from sympy import factorint
from family_s import Family
tabV = {5:20,7:42,9:72,11:110,13:156,15:210,17:272,19:342,21:420,23:506,25:600,41:1640}
tabW = {5:18,7:36,9:60,11:90,13:126,15:126,17:162,19:270,21:240,23:288,25:468,41:882}
def model(s):
    n1, n2 = s, s-2
    pp1 = [p**e for p, e in factorint(n1).items()]; pp2 = [p**e for p, e in factorint(n2).items()]
    def sect(pps):   # dict parity-product -> (dim, dim of all-even part)
        E = O = 0
        for signs in itertools.product((1, -1), repeat=len(pps)):
            d = 1
            for q, sg in zip(pps, signs): d *= (q+1)//2 if sg == 1 else (q-1)//2
            if math.prod(signs) == 1: E += d
            else: O += d
        alleven = math.prod((q+1)//2 for q in pps)
        return E, O, alleven
    E1, O1, ae1 = sect(pp1); E2, O2, ae2 = sect(pp2)
    V = 3*E1*E2 + 1*O1*O2
    W = 3*ae1*ae2
    return dict(V=V, W=W, cusp=V-W, oddodd=O1*O2, A3_mixed=3*(E1*E2-ae1*ae2), FixP=2*(s*(s-2)+1))
out = []
for s in sorted(tabV):
    F = Family(s); n = s*(s-2)
    # (1) gamma action on L'/Z^2: elements are AINV@m / D
    acts = {}
    for p, e in factorint(n).items():
        q = p**e
        # an element of order q: (n/q)*generator; find generator of the cyclic group
        ok = None
        for v in F.LP:
            gv = (F.G @ v) % F.D
            # p-primary component projector: multiply by idempotent c with c = 1 mod q, 0 mod n/q
            c = pow(n//q, -1, q)*(n//q)
            vp = (c*v) % F.D; gvp = (c*gv) % F.D
            if np.any(vp):
                for u in range(q):
                    if np.all((u*vp - gvp) % F.D == 0): ok = u; break
                break
        acts[q] = ok
    sign_rule = all((acts[q] - (s-1)) % q == 0 for q in acts)
    # (2) Fix(P) dimension (exact: P is monomial with root-of-unity phases)
    P = F.Pmatrix(); fixP = int(round(np.real(np.trace((P+np.eye(F.N))/2))))
    m = model(s)
    r = dict(s=s, gamma_scalars=acts, sign_rule_s_minus_1=sign_rule, FixP_numeric=fixP, **m,
             V_table=tabV[s], W_table=tabW[s], cusp_table=tabV[s]-tabW[s],
             match=(m['V'] == tabV[s] and m['W'] == tabW[s] and m['FixP'] == fixP))
    print(r, flush=True); out.append(r)
json.dump(out, open('cr3_parity_model.json', 'w'), indent=1)
