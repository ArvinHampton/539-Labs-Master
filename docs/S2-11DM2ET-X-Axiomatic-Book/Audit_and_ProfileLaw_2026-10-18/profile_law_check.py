"""Independent numerical verification of the general radial-profile S/T law (Path 3).
G_{al,be}(x) := mean over nu in al+Z^2 of e(x Q(nu) + B(nu,be)),  Q = 1/2 nu^T A nu,  A=[[2,7],[7,7]].
S-law:  G_{al,be}(-1/x) = e(B(al,be)) / (sqrt(35)|x|) * sum_{p in L'/Z^2} G_{be+p,-al}(x)
T-law:  G_{al,be}(x+1)  = e(-Q(al)-B(al,wc)) G_{al, al+be+wc}(x),  wc = A^{-1}(0,1/2)
Exact integer phase arithmetic; the mean is taken over one full period K^2 (K checked by doubling).
Written from scratch for the 2026-10-18 audit (no code reused)."""
import numpy as np, math, random, itertools, sys
from fractions import Fraction as Fr
A = np.array([[2,7],[7,7]], dtype=object)
Ainv = [[Fr(-1,5),Fr(1,5)],[Fr(1,5),Fr(-2,35)]]
a  = (Fr(7,10), Fr(-1,5))
wc = (Fr(1,10), Fr(-1,35))
def lcm(*xs):
    r=1
    for x in xs: r = r*x//math.gcd(r,x)
    return r
def den(v): return lcm(*[Fr(c).denominator for c in v])
def Bf(u,v): return u[0]*(2*v[0]+7*v[1]) + u[1]*(7*v[0]+7*v[1])
def Qf(u): return Bf(u,u)/2
def ef(r): r = Fr(r)%1; return complex(math.cos(2*math.pi*r), math.sin(2*math.pi*r))
# L'/Z^2 : 35 classes
LP = sorted({((Ainv[0][0]*i+Ainv[0][1]*j)%1, (Ainv[1][0]*i+Ainv[1][1]*j)%1) for i in range(35) for j in range(35)})
assert len(LP)==35
def G(al, be, x, Kmult=1):
    """exact-period mean; x a nonzero Fraction (or 0)."""
    x = Fr(x); h, m = x.numerator, x.denominator
    Da, Db = den(al), den(be)
    D = lcm(Da, Db)
    K = lcm(m*Da, 2*m, Db, Da) * Kmult
    # phase numerator over common denominator M = 2*m*D*D
    M = 2*m*D*D
    al_i = [int(c*D) for c in al]; be_i = [int(c*D) for c in be]
    n = np.arange(K, dtype=np.int64)
    n1 = (al_i[0] + D*n)[:,None]; n2 = (al_i[1] + D*n)[None,:]   # D*nu
    # x Q(nu) = h * (D nu)^T A (D nu) / (2 m D^2)
    qq = (2*n1*n1 + 14*n1*n2 + 7*n2*n2) % (2*m*D*D*1)   # (D nu)^T A (D nu) mod 2 m D^2 (enough since multiplied by h/(2mD^2))
    ph = (h*qq) % M
    # B(nu,be) = (D nu)^T A (D be) / D^2  -> times 2m to put over M
    Abe = (2*be_i[0]+7*be_i[1], 7*be_i[0]+7*be_i[1])
    bb = (n1*Abe[0] + n2*Abe[1]) % (D*D)
    ph = (ph + 2*m*bb) % M
    return np.exp(2j*np.pi*ph/M).mean()
def check_S(al, be, x):
    lhs = G(al, be, -1/Fr(x))
    rhs = ef(Bf(al,be)) / (math.sqrt(35)*abs(float(x))) * sum(G(((be[0]+p[0]), (be[1]+p[1])), (-al[0],-al[1]), x) for p in LP)
    return lhs, rhs
def check_T(al, be, x):
    lhs = G(al, be, Fr(x)+1)
    rhs = ef(-Qf(al)-Bf(al,wc)) * G(al, (al[0]+be[0]+wc[0], al[1]+be[1]+wc[1]), x)
    return lhs, rhs
if __name__ == "__main__":
    out = []
    pr = lambda *s: (print(*s), out.append(" ".join(map(str,s))))
    # period sanity: doubling K changes nothing
    for (al,be,x) in [(a,(0,0),Fr(1,3)), ((Fr(1,2),Fr(1,3)),(Fr(1,3),Fr(0)),Fr(-2,3)), (LP[5],(-a[0],-a[1]),Fr(3,7))]:
        d = abs(G(al,be,x)-G(al,be,x,Kmult=2)); pr("period check", al, be, x, "diff", f"{d:.2e}")
    labels_al = [p for p in LP] + [((p[0]+a[0])%1, (p[1]+a[1])%1) for p in LP]
    labels_be = [(Fr(0),Fr(0)), (-a[0],-a[1])]
    labels = [(al,be) for al in labels_al for be in labels_be]
    assert len(labels)==140
    xs = [Fr(1),Fr(-1),Fr(1,3),Fr(-1,3),Fr(2,3),Fr(-2,3),Fr(1,7),Fr(-3,7),Fr(2),Fr(-3,2),Fr(3,5),Fr(-7,4)]
    # (1) all 140 labels at 4 x-values (both signs), S-law
    worst=0; nz=0; n=0
    for (al,be) in labels:
        for x in [Fr(1),Fr(-1),Fr(1,3),Fr(-2,3)]:
            l,r = check_S(al,be,x); worst=max(worst,abs(l-r)); n+=1; nz += abs(l)>1e-9
    pr(f"S-law, all 140 labels x in {{1,-1,1/3,-2/3}}: {n} tests, {nz} with LHS nonzero, max |LHS-RHS| = {worst:.2e}")
    # (2) selected labels, many x
    worst=0; n=0; nz=0
    random.seed(20261018)
    sel = random.sample(labels, 12) + [(a,(Fr(0),Fr(0)))]
    for (al,be) in sel:
        for x in xs:
            l,r = check_S(al,be,x); worst=max(worst,abs(l-r)); n+=1; nz += abs(l)>1e-9
    pr(f"S-law, 13 labels x 12 x-values: {n} tests, {nz} nonzero, max dev {worst:.2e}")
    # (3) random rational al, be NOT in the family (denominators 2,3,4,6)
    worst=0; n=0; nz=0
    dens=[1,2,3,4,6]
    for trial in range(40):
        al = (Fr(random.randrange(12),random.choice(dens)), Fr(random.randrange(12),random.choice(dens)))
        be = (Fr(random.randrange(12),random.choice(dens)), Fr(random.randrange(12),random.choice(dens)))
        x = random.choice([Fr(1),Fr(-1),Fr(1,2),Fr(-1,2),Fr(2,3),Fr(-1,3),Fr(3,2),Fr(-2)])
        l,r = check_S(al,be,x); worst=max(worst,abs(l-r)); n+=1; nz += abs(l)>1e-9
    pr(f"S-law, 40 random (al,be) with denominators in {{1,2,3,4,6}}: {n} tests, {nz} nonzero, max dev {worst:.2e}")
    # (4) the signed factor fails at x<0: ratio LHS/RHS_signed = -1
    rat=[]
    for x in [Fr(-1),Fr(-1,3),Fr(-3,7)]:
        l,r = check_S(a,(Fr(0),Fr(0)),x)
        if abs(l)>1e-9: rat.append(l/(r*abs(float(x))/float(x)))
    pr("with signed factor x instead of |x| at x<0, LHS/RHS =", [f"{z.real:+.12f}{z.imag:+.1e}i" for z in rat])
    # (5) T-law on all labels and random
    worst=0; n=0
    for (al,be) in labels:
        for x in [Fr(1,3),Fr(-2,5)]:
            l,r = check_T(al,be,x); worst=max(worst,abs(l-r)); n+=1
    pr(f"T-law, all 140 labels, x in {{1/3,-2/5}}: {n} tests, max dev {worst:.2e}")
    open("profile_law_check.txt","w").write("\n".join(out)+"\n")
