# Exact certificates (Fractions / integer cyclotomic arithmetic) for items 1,2,5.
import sys; sys.path.insert(0,'.')
import numpy as np, itertools
from fractions import Fraction as F
from exact import red, D
from family import G, LABELS
out=[]; pr=lambda s:(print(s),out.append(s))
g=np.array([14,6]); a2=np.array([35,0])
lab=[(x,e,d) for x in range(35) for e in (0,1) for d in (0,1)]; idx={l:k for k,l in enumerate(lab)}
J={k:red((x*g+e*a2)%D,-d*a2) for k,(x,e,d) in enumerate(lab)}; inv={j:(k,ph) for k,(j,ph) in J.items()}
def act(f):
    res={}
    for k,(x,e,d) in enumerate(lab):
        al=(x*g+e*a2)%D; be=-d*a2; j2,ph2=red(f(al)%D,f(be)); k2,phk2=inv[j2]; res[k]=(k2,(ph2-phk2)%1)
    return res
Nn=act(lambda v:-v); Gg=act(lambda v:G@v)
def x5x7(x): return x%5,x%7
def xo(a,b): return [x for x in range(35) if x%5==a and x%7==b][0]
# (a) exact form of N and gamma
okN=all(Nn[idx[(x,e,d)]]==(idx[(xo((-x)%5,(-x)%7),e,d)],F(0)) for (x,e,d) in lab)
okG=all(Gg[idx[(x,e,d)]]==(idx[(xo(x%5,(-x)%7),e,d)],F(1,2) if (e,d)==(1,1) else F(0)) for (x,e,d) in lab)
pr(f"(a) negation acts on u' exactly as Z5⊗Z7⊗I4 (u'_k = u'_N(k), phase 0): {okN}")
pr(f"    unit gamma acts exactly as I5⊗Z7⊗diag(1,1,1,-1): {okG}")
# fixed space of the monomial identities u'_k = e(ph) u'_k2  (as linear conditions on value vectors v: v_k = e(ph) v_k2)
par={}; 
def orbit(k):
    # BFS over generators, tracking phase; inconsistent phase => forced zero
    seen={k:F(0)}; st=[k]; bad=False
    while st:
        a=st.pop()
        for A in (Nn,Gg):
            b,ph=A[a]; p=(seen[a]-ph)%1   # v_a = e(ph) v_b -> v_b = e(seen_a - ph) v_k  (v_a = e(seen_a) v_k)
            if b in seen:
                if seen[b]!=p: bad=True
            else: seen[b]=p; st.append(b)
    return seen,bad
orbs={}; 
for k in range(140):
    s,b=orbit(k); key=min(s); orbs[key]=(s,b)
nz=[o for o in orbs.values() if not o[1]]; zz=[o for o in orbs.values() if o[1]]
pr(f"    orbits of <N,gamma> on 140 labels: {len(orbs)}; consistent (free) orbits: {len(nz)} -> dim Fix = {len(nz)}; inconsistent orbits (forced zero): {len(zz)} containing {sum(len(o[0]) for o in zz)} labels")
from collections import Counter
pr(f"    free-orbit sizes: {sorted(Counter(len(o[0]) for o in nz).items())}; proportionality constants within orbits (u' basis): {sorted({str(p) for o in nz for p in o[0][0].values()} if False else {str(p) for o in nz for p in o[0].values()})}")
zl=sorted(lab[k] for o in zz for k in o[0]); pr(f"    zero labels (x5,x7,eps,delta): {[ (x%5,x%7,e,d) for x,e,d in zl]}")
# translate to original labels and phases: u'_k = e(J[k].ph) u_{J[k].j}
zj=sorted(J[idx[l]][0] for l in zl); pr(f"    zero labels in original indexing: {zj}")
# predicted sectors: Fix = even5⊗even7⊗span{00,01,10} + odd5⊗odd7⊗span{11}
pr(f"    predicted dim: 3*4*3 + 2*3*1 = {3*4*3+2*3}")
# proportionality constants in ORIGINAL basis: u_{j_a} = e(-ph_a) u'_a, u'_a = e(p) u'_b -> u_{j_a} = e(-ph_a + p + ph_b) u_{j_b}
consts=set()
for s,b in nz:
    ks=list(s); k0=ks[0]
    for k in ks[1:]:
        c=(-J[k][1]+s[k]-s[k0]+J[k0][1])%1   # rough: relative phase between u_{j_k} and u_{j_k0}
        consts.add(c.denominator)
pr(f"    proportionality constants in the original u basis are roots of unity e(r), r in Q with denominators {sorted(consts)}")
# (c) exact local Weil relations: H=(conj F T)^3 in Z[zeta_p] ; check H = c Z with c^2 = gamma^-2 p^3
def cyc_mul(a,b,p):  # polynomials mod 1+z+...+z^{p-1} represented as length-p int vectors mod (z^p-1), reduce later
    r=[0]*p
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: r[(i+j)%p]+=x*y
    return r
def canon(v,p):  # reduce modulo Phi_p: subtract v[p-1] from all
    c=v[p-1]; return tuple(x-c for x in v[:p-1])
def matmul(A,B,p):
    n=len(A); return [[ [sum(t) for t in zip(*[cyc_mul(A[i][k],B[k][j],p) for k in range(n)])] for j in range(n)] for i in range(n)]
for p,gk in ((5,4),(7,6)):
    def mono(k): v=[0]*p; v[k%p]=1; return v
    Fb=[[mono(-4*x*y) for y in range(p)] for x in range(p)]
    Tm=[[mono(2*x*x) if x==y else [0]*p for y in range(p)] for x in range(p)]
    FT=matmul(Fb,Tm,p); H=matmul(matmul(FT,FT,p),FT,p)
    H2=matmul(H,H,p)
    # H = c * Z ?  check off-pattern entries vanish and pattern entries equal
    pat=all(canon(H[x][y],p)==tuple([0]*(p-1)) for x in range(p) for y in range(p) if (x+y)%p!=0)
    cvals={canon(H[x][(-x)%p],p) for x in range(p)}
    sq=all(canon(H2[x][y],p)==(tuple([0]*(p-1)) if x!=y else None) or (x==y) for x in range(p) for y in range(p))
    diag={canon(H2[x][x],p) for x in range(p)}
    pr(f"(c) p={p}: (conj(F)T)^3 = c·Z exactly: {pat and len(cvals)==1}; (..)^2 off-diagonal zero: {sq}; diagonal = {diag} (as poly in zeta_{p}; constant {'-' if False else ''}p^3={p**3} means c^2 = p^3 up to the gamma^-2 sign)")
open("closure_exact.txt","w").write("\n".join(out)+"\n")
