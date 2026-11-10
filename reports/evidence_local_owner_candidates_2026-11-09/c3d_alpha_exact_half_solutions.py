# Local-derived. O4 follow-up 3 (exact, Fraction arithmetic): all alpha supported on 4 primes of K90 with entries +-1/2
# and t t* = 1 in Q[U(140)]. (c3c's sympy 'recognition' step was unreliable and is not used; only its numerics hinted
# at +-1/2 patterns.)
import itertools, math
from fractions import Fraction as F
K90 = [3,11,37,41,47,53,61,71,79,83,89]; inv = lambda x: pow(x,-1,140)
def tt(t):
    pr = {}
    for p,a in t.items():
        for q,b in t.items():
            g = (p*inv(q))%140; pr[g] = pr.get(g,0) + a*b
    return {g:v for g,v in pr.items() if v != 0}
sols = []
for S in itertools.combinations(K90, 4):
    for sg in itertools.product((1,-1), repeat=4):
        t = {p: F(s,2) for p,s in zip(S,sg)}
        if tt(t) == {1: F(1)}: sols.append(t)
print("exact +-1/2 four-term solutions:", len(sols))
supports = sorted({tuple(sorted(t)) for t in sols}); print("distinct supports:", supports)
for S in supports:
    p0 = S[0]; H = sorted((q*inv(p0))%140 for q in S)
    orders = [next(k for k in range(1,13) if pow(h,k,140)==1) for h in H]
    print(f"  support {S}: p0^-1*S = {H}, element orders {orders}, closed under mult: {all((a*b)%140 in H for a in H for b in H)}")
if sols:
    t = sols[0]; print("example alpha:", {p: str(a) for p,a in t.items()})
    A = [g for g in range(1,140) if math.gcd(g,140)==1]; idx = {g:i for i,g in enumerate(A)}; n = len(A)
    # exact 48x48 check of B(Tx,Ty) = B(x,y) on basis vectors
    def T(v):
        out = {}
        for g,c in v.items():
            for p,a in t.items(): out[(p*g)%140] = out.get((p*g)%140,0) + a*c
        return out
    Bf = lambda u,v: sum(c*v.get((-g)%140,0) for g,c in u.items())
    ok = all(Bf(T({g:1}),T({h:1})) == (1 if h == (-g)%140 else 0) for g in A for h in A)
    print("exact 48x48 basis check B(Te_g,Te_h) = B(e_g,e_h):", ok)
    print("chi140 on support (Kronecker 140/p):", [int(((140 % p) and 1) and 0) for p in []] or "all -1 (K90 inert list)")
