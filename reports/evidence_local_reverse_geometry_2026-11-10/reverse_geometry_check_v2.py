# Local-derived evidence, 2026-11-10 (America/Chicago). Pure arithmetic; no physics input.
# G1: AL / local signs of Xi; G2: Weil rho(-I) on e0 for N2 (parity lock); G3: Bolza Jacobian CM field;
# G4: split-form chi_23 test for chi_140 vs chi_-20; G5: charge-relation lattice illustration.
import cypari2, itertools, cmath
from fractions import Fraction as Fr
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
print("== G1: Atkin-Lehner signs of f_Xi (w_p = eps_p for p | N, weight 2) ==")
E49 = pari('ellinit([1,-1,0,-2,-1])')
X = pari('ellinit(elltwist(ellinit([1,-1,0,-2,-1]),140))')
print("cond(Xi) =", pari.ellglobalred(X)[0], " eps(Xi) =", pari.ellrootno(X), " Fricke w = -eps =", -pari.ellrootno(X))
loc = {}
for p in [2,5,7]:
    loc[p] = int(pari.ellrootno(X,p)); print(" p=%d  eps_p = w_p = %+d" % (p, loc[p]))
print(" check: -prod(eps_p) * eps_inf(=-1) ... global eps = eps_inf*prod =", -1*loc[2]*loc[5]*loc[7])
for r in range(1,4):
    for S in itertools.combinations([2,5,7], r):
        w = 1
        for p in S: w *= loc[p]
        Q = 1
        for p in S: Q *= {2:16,5:25,7:49}[p]
        print("  W_%-5d (p in %s): eigenvalue %+d" % (Q, S, w))
for p in [3,5,11,13,17,19,23,29,31,37,41,43]:
    print("  a_%d(Xi) = %s   a_%d(49a1) = %s" % (p, pari.ellap(X,p), p, pari.ellap(E49,p)))
print("== G2: Weil rep rho(-I) on C[D(N2)], N2=[[2,14],[14,28]] ==")
G = pari('[2,14;14,28]'); print("det =", pari.matdet(G), " signature (b+,b-) = (1,1) since det<0")
Gi = [[Fr(28,-140),Fr(-14,-140)],[Fr(-14,-140),Fr(2,-140)]]
pts=set()
for v1 in range(140):
    for v2 in range(140):
        x=(Gi[0][0]*v1+Gi[0][1]*v2, Gi[1][0]*v1+Gi[1][1]*v2)
        pts.add(tuple(c%1 for c in x))
q = lambda g: (Fr(1,2)*(g[0]*(2*g[0]+14*g[1])+g[1]*(14*g[0]+28*g[1])))%1
assert all(((Fr(2)*q(g))%1)==((Fr(2)*q(tuple(-c%1 for c in g)))%1) for g in pts)
print("|D| =", len(pts))
neg = lambda g: tuple((-c)%1 for c in g)
fixed = [g for g in pts if neg(g)==g]
print("#{g : g = -g} (2-torsion) =", len(fixed))
sig = 0
print("rho(Z) e_g = e(-sig/4) e_{-g}, sig = 0  =>  e0 -> e0; +1 eigenspace dim =", (len(pts)+len(fixed))//2, " -1 eigenspace dim =", (len(pts)-len(fixed))//2)
print("chi_140(-1) =", pari.kronecker(140,-1), " (must equal e(-sig/4)=+1: parity lock holds)")
for s in [0,1,2,3]:
    print("  parity lock: sig = %d mod 4 -> forced chi(-1) on e0 = %s" % (s, {0:'+1',2:'-1',1:'impossible (i^-1 not real)',3:'impossible'}[s]))
print("== G3: Bolza Jacobian y^2 = x^5 - x : Frobenius char polys ==")
inert7 = lambda p: pari.kronecker(-7,p)==-1
bad = []
for p in pari.primes(60)[2:]:
    p=int(p)
    cp = pari.hyperellcharpoly(pari('Mod(1,%d)*(x^5-x)'%p))
    fac = pari.factor(cp)
    print(" p=%3d  (-2/p)=%+d (-7/p)=%+d  charpoly factors: %s" % (p, pari.kronecker(-2,p), pari.kronecker(-7,p), [str(f) for f in fac[0]]))
    # elliptic-factor traces
    if pari.kronecker(-2,p)==1 and inert7(p):
        bad.append(p)
print(" primes split in Q(sqrt-2), inert in Q(sqrt-7) (Xi has a_p=0 there):", bad)
print(" discriminants a^2-4p of quadratic factors at split primes (squarefree part):")
for p in pari.primes(60)[2:]:
    p=int(p)
    cp = pari.hyperellcharpoly(pari('Mod(1,%d)*(x^5-x)'%p)); fac=pari.factor(cp)[0]
    out=[]
    for f in fac:
        if pari.poldegree(f)==2:
            a = -pari.polcoef(f,1); d = a*a-4*pari.polcoef(f,0)
            out.append((int(a), str(pari.core(d)) if d!=0 else '0'))
    print("  p=%d: %s" % (p,out))
print("== G4: split SO(24,24) form: chi_23 trivial test, (D/23) ==")
for D in [140, -20, -7, 5, 28, -35, 35, -4, 8, -8]:
    print("  D=%4d  (D/23)=%+d" % (D, pari.kronecker(D,23)))
print("== G5 (illustration only): kernel lattice of (1,1,-2) in Z^3, standard form ==")
K = pari.matkerint(pari('[1,1,-2]')); print(" basis =", K); Gr = K.mattranspose()*K; print(" Gram =", Gr, " det =", pari.matdet(Gr))
