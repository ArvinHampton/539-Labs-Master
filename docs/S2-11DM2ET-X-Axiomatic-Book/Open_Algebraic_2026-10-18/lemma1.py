# (1) Orbit lemma.  2*Qi(X) = y^2 - d x2^2 with y = 2x1 + s x2, d = s(s-2) = (s-1)^2-1, eps = (s-1)+sqrt d <-> gamma.
# Norm -4d.  Nagell: every class of solutions of y^2 - d x2^2 = -4d has a representative with 0 < x2 <= sqrt(4d)/sqrt(2(s-2)) = sqrt(2s).
# x2 = 2 gives y = 0 (nu0, self-conjugate class).  Lemma <=> no c in [3, sqrt(2s)] with (c^2-4) d a square (c=1 impossible: negative).
#   c = 3: 5((s-1)^2-1) = y^2 forces (s-1)^2 - 5z^2 = 1 with s-1 = u; all solutions (9+4 sqrt5)^k have u odd => s even.  Never for odd s.
# Part B: orbit of u_S nu0 vs nu0 in Delta, exact, odd s up to SMAX.
import sys, math, json, itertools, sympy
from sympy.ntheory.modular import crt
SMAX=int(sys.argv[1]); SB=int(sys.argv[2])
exc=[]
for s in range(5,SMAX+1,2):
    d=s*(s-2)
    for c in range(3,math.isqrt(2*s)+1):
        v=(c*c-4)*d; r=math.isqrt(v)
        if r*r==v and (r - s*c)%2==0: exc.append((s,c))
print("exceptions (s,c) with extra reduced classes, odd s <=",SMAX,":",exc[:50],len(exc))
# Pell parity check for c=3 (first few solutions)
u,z=9,4; par=[]
for _ in range(8): par.append(u%2); u,z=9*u+20*z,4*u+9*z
print("c=3 Pell u parities:",par)
# Part B
res=[]
for s in range(5,SB+1,2):
    D=2*s*(s-2)  # vrank odd: mod=(D,2D) with D=F.D; recompute D as in family? use F
    from family_s import Family
    F=Family(s); D=F.D; mod=(D,2*D)
    G=[[-1,-s],[2,2*s-1]]
    act=lambda g,x:((g[0][0]*x[0]+g[0][1]*x[1])%mod[0],(g[1][0]*x[0]+g[1][1]*x[1])%mod[1])
    x0=(s%mod[0],(-2)%mod[1])
    orb=set(); y=x0
    while True:
        for sg in (1,-1): orb.add(((sg*y[0])%mod[0],(sg*y[1])%mod[1]))
        y=act(G,y)
        if y==x0: break
    ps=[p for p in sympy.factorint(s*(s-2))]
    M=2*D
    fixers=[]
    for S in itertools.product((0,1),repeat=len(ps)):
        u=1
        for b,p in zip(S,ps):
            if b:
                pe=p**sympy.multiplicity(p,M); u=u*int(crt([pe,M//pe],[pe-1,1])[0])%M
        if (u*x0[0]%mod[0],u*x0[1]%mod[1]) in orb: fixers.append([p for b,p in zip(S,ps) if b])
    res.append((s,ps,fixers))
bad=[r for r in res if len(r[2])!=1]
print("odd s<=%d: subsets S with Z_S O0 = O0 other than empty:"%SB, bad[:20], "count",len(bad))
json.dump({"exceptions":exc,"partB_bad":bad,"partB_all":res},open("lemma1.json","w"),indent=0,default=str)
