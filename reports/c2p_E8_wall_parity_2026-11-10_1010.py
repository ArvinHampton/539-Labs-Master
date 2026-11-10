# FROZEN before run (MR2, 2026-11-10). B1-c2' E8 wall bundle under 1a: geometric inputs for the lift check.
# Metric: MN2 11D uplift exactly as in /workspace/mr2-branch-2134/L1_everywhere_symbolic_2026-11-09_2204.py (sha 2f2b9d4f..., PP-audited
# in 60293840), chart (mu1, mu2), mu0^2 = 1 - mu1^2 - mu2^2, twist A = dx/y on phi1, plus the phi2 row g_{phi2 phi2} = (1/4) D^{-2/3} mu2^2/X2
# (a2 = 0: no phi2 cross terms). Wall = constant-r face (1a); we use the smooth-side 11D curvature at the face.
# Checks: [M] exact invariance of the metric under r~ = {x, phi1}, P = {phi2}, f = P o r~ = {x, phi1, phi2}, c2' = f o Pi_x3.
#         [D] fibre (S^4) orientation degree of each map from the Jacobian on (mu1, mu2, phi1, phi2).
#         [Q] tr R^R: all 15 components with 4 internal-Y6 indices {x,y,mu1,mu2,phi1,phi2} at one generic point (mp dps 30);
#             parity (-1)^{|S cap I|} of every nonzero component, versus the G4 index-set parity from bd47ff5e.
import sympy as sp, mpmath as mp, itertools, time
mp.mp.dps = 30
t0 = time.time()
t,x1,x2,x3,r,x,y,u,v,p1,p2 = sp.symbols('t x1 x2 x3 r x y mu1 mu2 phi1 phi2', real=True)
X = [t,x1,x2,x3,r,x,y,u,v,p1,p2]; names = ['t','x1','x2','x3','r','x','y','mu1','mu2','phi1','phi2']
X1 = 2**sp.Rational(-3,5); X2 = 2**sp.Rational(2,5); F = 2**sp.Rational(-4,5); Gs = 2**sp.Rational(1,5)/4; a1 = 1
X0 = 1/(X1*X2)**2
m0sq = 1-u**2-v**2
D = X0*m0sq + X1*u**2 + X2*v**2
n = 11; g = sp.zeros(n)
w = D**sp.Rational(1,3)
for i in range(5): g[i,i] = w*F/r**2*(-1 if i==0 else 1)
g[5,5] += w*Gs/y**2; g[6,6] += w*Gs/y**2
vv = sp.Rational(1,4)*D**sp.Rational(-2,3)
g[7,7] += vv*(1/X1 + u*u/(X0*m0sq)); g[8,8] += vv*(1/X2 + v*v/(X0*m0sq))
g[7,8] += vv*(u*v/(X0*m0sq)); g[8,7] += vv*(u*v/(X0*m0sq))
c1 = vv*u**2/X1
g[9,9] += c1; g[9,5] += c1*a1/y; g[5,9] += c1*a1/y; g[5,5] += c1*a1**2/y**2
g[10,10] += vv*v**2/X2
maps = {"r~ = {x,phi1}": {x,p1}, "P = {phi2}": {p2}, "f = P o r~ = {x,phi1,phi2}": {x,p1,p2}, "c2' = f o Pi_x3": {x,p1,p2,x3}}
print("[M] metric invariance (pullback g -> J^T g(f(p)) J, exact):")
for lab, S in maps.items():
    J = sp.diag(*[(-1 if X[i] in S else 1) for i in range(n)])
    sub = {s_: -s_ for s_ in S}
    gp = (J.T*g.subs(sub, simultaneous=True)*J - g).applyfunc(sp.simplify)
    print(f"  {lab:28s} invariant: {gp == sp.zeros(n)}")
print("[D] S^4-fibre orientation degree (det of Jacobian on (mu1,mu2,phi1,phi2)):")
fib = [7,8,9,10]
for lab, S in maps.items():
    print(f"  {lab:28s} deg = {sp.prod([(-1 if X[i] in S else 1) for i in fib])}")
G4sets = [{'x','y','mu?','phi2'}]  # placeholder not used; bd47ff5e sets in (u,v,alpha,beta,phi1,phi2) labels below
bd = [{'u','v','alpha','phi2'},{'u','v','beta','phi2'},{'u','alpha','beta','phi2'},{'alpha','beta','phi1','phi2'}]
tr = {'x':'u','phi1':'phi1','phi2':'phi2','x3':'x3'}
print("[G] G4 pullback sign from bd47ff5e index sets (u = Sigma coordinate x):")
for lab, S in maps.items():
    Sb = {tr[names[X.index(s_)]] for s_ in S}
    signs = {(-1)**len(Sb & I) for I in bd}
    print(f"  {lab:28s} f*G = {signs}")
# --- Riemann numerically at a generic point
gi = g.inv(method='LU')
dep = [4,6,7,8]
dg = {c: g.diff(X[c]) for c in dep}
Gam = {}
for l in range(n):
    for a in range(n):
        for b in range(a,n):
            s = 0
            for m_ in range(n):
                if gi[l,m_] == 0: continue
                term = (dg[b][m_,a] if b in dep else 0) + (dg[a][m_,b] if a in dep else 0) - (dg[m_][a,b] if m_ in dep else 0)
                if term != 0: s += gi[l,m_]*term/2
            if s != 0: Gam[(l,a,b)] = s; Gam[(l,b,a)] = s
pt = {t:0, x1:0, x2:0, x3:0, r:1, x:sp.Rational(1,5), y:sp.Rational(13,10), u:sp.Rational(1,2), v:sp.Rational(2,5), p1:sp.Rational(3,10), p2:sp.Rational(7,10)}
def N(e): return mp.mpf(str(sp.N(e.subs(pt), 40))) if e != 0 else mp.mpf(0)
GamN = {k_: N(e) for k_, e in Gam.items()}
dGamN = {}
for k_, e in Gam.items():
    for c in dep:
        de = sp.diff(e, X[c])
        if de != 0: dGamN[(k_, c)] = N(de)
GN = lambda l,a,b: GamN.get((l,a,b), mp.mpf(0))
def Rm(a,b,c,d_):  # R^a_{b c d}
    val = dGamN.get(((a,d_,b),c), 0) - dGamN.get(((a,c,b),d_), 0)
    for e in range(n): val += GN(a,c,e)*GN(e,d_,b) - GN(a,d_,e)*GN(e,c,b)
    return val
internal = [5,6,7,8,9,10]
pairs = list(itertools.combinations(internal, 2))
Rc = {(a,b,c,d_): Rm(a,b,c,d_) for a in range(n) for b in range(n) for (c,d_) in pairs}
def R2(a,b,c,d_):
    if c < d_: return Rc[(a,b,c,d_)]
    return -Rc[(a,b,d_,c)]
print(f"[Q] tr R^R components on Y6 at point mu1=1/2, mu2=2/5, y=13/10 (dps 30); elapsed {time.time()-t0:.1f}s")
rows = []
for (c,d_,e,f_) in itertools.combinations(internal, 4):
    s = 0
    for a in range(n):
        for b in range(n):
            s += R2(a,b,c,d_)*R2(b,a,e,f_) - R2(a,b,c,e)*R2(b,a,d_,f_) + R2(a,b,c,f_)*R2(b,a,d_,e)
    I = {names[c],names[d_],names[e],names[f_]}
    rows.append((I, s))
thr = mp.mpf('1e-20')
for I, s in rows:
    nz = abs(s) > thr
    par = {lab: (-1)**len({names[X.index(q)] for q in S} & I) for lab, S in maps.items()}
    print(f"  {sorted(I)}: {mp.nstr(s, 15)}  {'NONZERO' if nz else 'zero'}  parity r~,P,f,c2' = {list(par.values()) if nz else '-'}")
bad = {lab: [sorted(I) for I, s in rows if abs(s) > thr and (-1)**len({names[X.index(q)] for q in S} & I) == -1] for lab, S in maps.items()}
print("[Q] nonzero tr R^R components with odd parity (would contradict naturality):", bad)
print(f"done {time.time()-t0:.1f}s")
