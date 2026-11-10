# Frozen (chmod a-w + sidecar) before the logged run. MR2 2026-11-09. Checks for erratum per PP ef599f76: lift-orbit decomposition (fix 2), closed-form tilt (fix 4), Lagrangian W (fix 1). Additive; no network.
import numpy as np, hashlib
from math import pi, cos, sin, acos
R='/workspace/quantum-comp/reports/'
src=R+'MR2_MN2_KK_A_SU2R_FLAT_CONNECTIONS_LIFT_AND_EDGE_CASES_AUT48_2026-11-09.py'
h=hashlib.sha256(open(src,'rb').read()).hexdigest()
print(f"[0] b0c6e848's .py sha256 {h} ({'MATCH 02b94500' if h.startswith('02b94500') else 'MISMATCH'}); exec'ing it verbatim (its own lines follow)", flush=True)
exec(open(src).read())
P("---- new checks (this erratum) ----")
def orbits(vecs, mats):
    keyv=lambda v: tuple(int(a) for a in v)
    left={keyv(v):v for v in vecs}; out=[]
    while left:
        k0,v0=next(iter(left.items())); o={k0:v0}; fr=[v0]
        while fr:
            nf=[]
            for u in fr:
                for M in mats:
                    w=(M@u)%2; kw=keyv(w)
                    if kw not in o: o[kw]=w; nf.append(w)
            fr=nf
        for k in o: left.pop(k,None)
        out.append(len(o))
    return sorted(out)
valid=all(((Rm@((Cx@s)%2))%2==b).all() and ((Rm@((Cy@s)%2))%2==b).all() for s in lifts)
P(f"[F2] Aut+ maps K3 lifts to K3 lifts: {valid}; orbit sizes of Aut+ on the 16 K3 lifts: {orbits(lifts,[Cx,Cy])} (theta characteristics 88949658 [W]: odd 6, even 4+6 => 4+6+6)")
P(f"[F2] orbit sizes of Aut+ on the 16 characters (linear, H^1): {orbits([comb(cs) for cs in itertools.product([0,1],repeat=4)],[Cx,Cy])} (J[2]: 1+3+12)")
# cup product on H^1(Sigma;Z2) via Weierstrass model: e(S,T) = |S cap T| mod 2 for even subsets mod complement; W = antipodal pairs
pairs=[{0,1},{2,4},{3,5}]  # (0,inf),(1,-1),(i,-i) in PTS order [0,inf,1,i,-1,-i]
P(f"[F1] Weierstrass check: antipodal-pair classes pairwise intersection |S cap T| mod 2 = {[len(a&b_)%2 for a in pairs for b_ in pairs if a!=b_]} (0 => W isotropic, dim 2 = half of 4 => Lagrangian)")
P("[F4] closed form: for x = pi-rotation about e3, y = 2pi/3-rotation about n(psi): Re tr/2 of x~y~ = -sin(pi/3) cos(psi); z of order 8 with angle 2pi k/8 needs |sin(pi/3) cos psi| = |cos(pi k/8)|:")
for k in range(1,8):
    c=cos(pi*k/8)/sin(pi/3)
    P(f"     k={k}: cos psi = +-{c:.6f} -> {'psi = %.6f rad (real)'%acos(abs(c)) if abs(c)<=1 else 'no real psi (|cos psi|>1 would need a complex angle): no SO(3) rep'}")
P(f"[F4] k=3 closed form psi = {acos(cos(3*pi/8)/sin(pi/3)):.9f} vs bisection {tilt:.9f}: diff {abs(acos(cos(3*pi/8)/sin(pi/3))-tilt):.1e}")
P("[F4] lift signs forced by orders: any lift of a pi-rotation has x~^2 = -1; z of order 8 with angle 3pi/4 has z~^8 = exp(3 pi i n.sigma) = -1 for either sign; y~^3 = +-1 is a free normalisation (y~ -> -y~). So b = (1, c, 1) on the three relator types, independent of the numerical root.")
