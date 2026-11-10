# FROZEN before run. MR2 2026-11-09. Additive. No network, no external sends.
# MR2 KK truncation of MN N=2 on Bolza: (A) Aut+ (48) vs (B) Isom (96), each x wall Z2.
# Sections: G group+characters; W Weierstrass/spin/Z2-Wilson; T triangle FEM (1D-rep spectra);
# S spin-2 operator check; L orientation-reversing lift sign bookkeeping; N NL mass carry (sha-checked).
import numpy as np, itertools, hashlib, sys, time
import scipy.sparse as sps, scipy.sparse.linalg as spla
import sympy as sp
np.set_printoptions(linewidth=160, precision=6, suppress=True)
def P(*a): print(*a, flush=True)
T0=time.time()
# ---------------- G: group construction ----------------
f = lambda x: x**5 - x
def mob(M, x):
    a,b,c,d = M[0,0],M[0,1],M[1,0],M[1,1]
    if x is None: return None if abs(c)<1e-12 else a/c
    den = c*x+d
    return None if abs(den)<1e-12 else (a*x+b)/den
def lift_pullback(M):
    a,b,c,d = M[0,0],M[0,1],M[1,0],M[1,1]
    rng = np.random.default_rng(1); xs = rng.normal(size=3)+1j*rng.normal(size=3)
    ks = [f(mob(M,x))*(c*x+d)**6/f(x) for x in xs]
    assert max(abs(k-ks[0]) for k in ks) < 1e-9*abs(ks[0]), "not an automorphism of y^2=x^5-x"
    s = (a*d-b*c)/np.sqrt(ks[0])
    return s*np.array([[d,b],[c,a]]), ks[0]
def realify(Mc): return np.block([[Mc.real,-Mc.imag],[Mc.imag,Mc.real]])
PTS = [0, None, 1, 1j, -1, -1j]; PN = ['0','inf','1','i','-1','-i']
def ptidx(x):
    for k,p in enumerate(PTS):
        if (p is None and x is None) or (p is not None and x is not None and abs(p-x)<1e-9): return k
    raise ValueError(x)
def perm_of(fun): return tuple(ptidx(fun(p)) for p in PTS)
gens = {}
for name, M in [('g1: x->ix', np.array([[1j,0],[0,1]])), ('g2: x->(x+1)/(1-x)', np.array([[1,1],[-1,1]],dtype=complex))]:
    Pm, kap = lift_pullback(M)
    gens[name] = (realify(np.linalg.inv(Pm)), perm_of(lambda x, M=M: mob(M,x)))
    P(f"[G] generator {name}: kappa={kap:.6f}; branch-point perm {[PN[i] for i in gens[name][1]]}")
gens['J: y->-y'] = (-np.eye(4), tuple(range(6)))
gens['K: complex conjugation'] = (np.diag([1.,1,-1,-1]), perm_of(lambda x: None if x is None else np.conj(x)))
def key(D, p): return (tuple(np.round(D,6).ravel()+0.0), p)
def close(gl):
    E = {key(np.eye(4),tuple(range(6))):(np.eye(4),tuple(range(6)))}; frontier=list(E.values())
    while frontier:
        new=[]
        for (D,p) in frontier:
            for (Dg,pg) in gl:
                D2 = D@Dg; p2 = tuple(p[pg[i]] for i in range(6)); k=key(D2,p2)
                if k not in E: E[k]=(D2,p2); new.append((D2,p2))
        frontier=new
    return list(E.values())
Jc = realify(1j*np.eye(2))
G96 = close(list(gens.values()))
G48 = [e for e in G96 if np.allclose(e[0]@Jc, Jc@e[0])]
anti = [e for e in G96 if np.allclose(e[0]@Jc, -Jc@e[0])]
P(f"[G] |closure of <g1,g2,J,K>| = {len(G96)};  holomorphic (Aut+) = {len(G48)};  antiholomorphic = {len(anti)}")
# faithfulness on H^1: distinct matrices
P(f"[G] distinct H^1 matrices: {len(set(tuple(np.round(e[0],6).ravel()+0.0) for e in G96))} (faithful on H^1 iff = |G|)")
def orders(G):
    out=[]
    for D,_ in G:
        k=1; M=D.copy()
        while not np.allclose(M,np.eye(4)): M=M@D; k+=1
        out.append(k)
    return out
from collections import Counter
P(f"[G] Aut+ element orders: {sorted(Counter(orders(G48)).items())}")
P(f"[G] Isom element orders: {sorted(Counter(orders(G96)).items())}")
# check GL(2,3) identification: order stats of GL(2,3) computed directly
GL23=[np.array(m).reshape(2,2) for m in itertools.product(range(3),repeat=4) if (m[0]*m[3]-m[1]*m[2])%3!=0]
def ordmod3(A):
    k=1; M=A.copy()%3
    while not np.array_equal(M,np.eye(2,dtype=int)): M=(M@A)%3; k+=1
    return k
P(f"[G] GL(2,3) by enumeration: |GL(2,3)|={len(GL23)}, element orders {sorted(Counter(ordmod3(A) for A in GL23).items())}")
# J central in both, acts as -1 on H^1
J = [e for e in G48 if np.allclose(e[0],-np.eye(4))]
P(f"[G] elements acting as -1 on H^1: {len(J)} (the hyperelliptic involution); central in Isom: {all(np.allclose(J[0][0]@e[0], e[0]@J[0][0]) for e in G96)}")
def char_table(G, label):
    n=len(G); keys=[key(*e) for e in G]; idx={k:i for i,k in enumerate(keys)}
    mul=np.zeros((n,n),dtype=int)
    for i,(Di,pi) in enumerate(G):
        for j,(Dj,pj) in enumerate(G):
            mul[i,j]=idx[key(Di@Dj, tuple(pi[pj[t]] for t in range(6)))]
    e=idx[key(np.eye(4),tuple(range(6)))]
    inv=np.array([int(np.where(mul[i]==e)[0][0]) for i in range(n)])
    cls=[]; seen=set()
    for i in range(n):
        if i in seen: continue
        c=sorted(set(mul[mul[g,i],inv[g]] for g in range(n))); cls.append(c); seen|=set(c)
    cls.sort(key=lambda c:(len(c),c[0]!=e))
    r=len(cls); cof=np.zeros(n,dtype=int)
    for k,c in enumerate(cls):
        for i in c: cof[i]=k
    C=np.zeros((r,r,r))
    for j in range(r):
        for l in range(r):
            z=cls[l][0]
            for x in cls[j]:
                C[j,cof[mul[inv[x],z]],l]+=1
    # M_j[k,l] = c_{jkl}; class-sum algebra: common eigenvectors of M_j^T
    rng=np.random.default_rng(7); A=sum(rng.normal()*C[j] for j in range(r))
    w,V=np.linalg.eig(A)
    chars=[]; sizes=np.array([len(c) for c in cls])
    i0=[k for k,c in enumerate(cls) if c==[e]][0]
    for t in range(r):
        v=V[:,t]/V[i0,t]
        d2=n/np.sum(np.abs(v)**2/sizes); d=np.sqrt(d2)
        chars.append(d*v/sizes)
    chars=np.array(chars); chars=chars[np.lexsort(([-np.sum(c.real) for c in chars],[round(c[i0].real) for c in chars]))]
    # orthogonality check
    O=(chars*sizes)@chars.conj().T/n
    reps=[cls[k][0] for k in range(r)]
    P(f"[G] {label}: {r} classes, sizes {list(sizes)}, irrep dims {[int(round(c[i0].real)) for c in chars]}, sum d^2 = {int(round(sum(c[i0].real**2 for c in chars)))}, orthogonality err {np.abs(O-np.eye(r)).max():.1e}")
    ords=orders([G[i] for i in reps]) if True else None; orient=[1 if np.allclose(G[i][0]@Jc,Jc@G[i][0]) else -1 for i in reps]
    P(f"[G] {label} class rep orders {ords}; orientation {orient}")
    for k,c in enumerate(chars):
        P(f"   chi_{k}: "+"  ".join(f"{x.real:+.3f}"+(f"{x.imag:+.3f}i" if abs(x.imag)>1e-9 else "") for x in c))
    return dict(cls=cls,chars=chars,sizes=sizes,reps=reps,n=n,orient=orient,ords=ords)
CT48=char_table(G48,"Aut+ (order 48)")
CT96=char_table(G96,"Isom (order 96)")
def decompose(CT, chi, label):
    m=(CT['chars'].conj()*CT['sizes'])@chi/CT['n']
    P(f"[G] {label}: multiplicities {np.round(m.real,6).tolist()}  trivial-rep multiplicity = {m[0].real:.6f}")
    return m
for CT,G,lab in [(CT48,G48,'A'),(CT96,G96,'B')]:
    chi=np.array([np.trace(G[i][0]) for i in CT['reps']])
    decompose(CT,chi,f"({lab}) H^1(Sigma,R) (harmonic 1-forms, dim 4)")
# holomorphic sections, Aut+ only
def cplx(D): return D[:2,:2]+1j*D[2:,:2]
chi1=np.array([np.trace(cplx(G48[i][0])) for i in CT48['reps']])
chi1sq=np.array([np.trace(cplx(G48[i][0])@cplx(G48[i][0])) for i in CT48['reps']])
decompose(CT48,chi1,"(A) H^0(K) = holomorphic 1-forms (dim 2; q=1 lowest Landau level)")
decompose(CT48,(chi1**2+chi1sq)/2,"(A) H^0(K^2) = Sym^2 H^0(K) (dim 3; q=2 lowest Landau level)")
# 1D characters
for CT,lab in [(CT48,'Aut+'),(CT96,'Isom')]:
    d1=[k for k,c in enumerate(CT['chars']) if abs(c[0]-1)<1e-9]
    P(f"[G] {lab}: number of 1-dim characters = {len(d1)}")
# ---------------- W: Weierstrass points, spin structures, Z2 Wilson lines ----------------
def orbit_report(G, objs, act, label):
    objs=list(objs); fixed=[o for o in objs if all(act(p,o)==o for _,p in G)]
    seen=set(); orbs=[]
    for o in objs:
        if o in seen: continue
        orb={act(p,o) for _,p in G}; orbs.append(len(orb)); seen|=orb
    P(f"[W] {label}: {len(objs)} objects, orbit sizes {sorted(orbs)}, invariant = {len(fixed)}")
pt_act=lambda p,o: p[o]
set_act=lambda p,o: frozenset(p[i] for i in o)
part_act=lambda p,o: frozenset(frozenset(p[i] for i in T) for T in o)
odd=range(6)
even={frozenset([frozenset(T),frozenset(set(range(6))-set(T))]) for T in itertools.combinations(range(6),3)}
pairs=[frozenset(s) for s in itertools.combinations(range(6),2)]
for G,lab in [(G48,'(A) Aut+'),(G96,'(B) Isom')]:
    orbit_report(G,odd,pt_act,f"{lab} odd spin structures (theta chars O(P_i))")
    orbit_report(G,even,part_act,f"{lab} even spin structures (3+3 partitions)")
    orbit_report(G,pairs,set_act,f"{lab} nonzero H^1(Sigma,Z2) classes (P_i-P_j): discrete Z2 Wilson lines")
P(f"[W] check: 6 odd + {len(even)} even = {6+len(even)} spin structures; {len(pairs)} nonzero Z2 classes = 2^4-1")
# ---------------- T: (2,3,8) triangle FEM with the four 1-dim-character boundary conditions ----------------
al,be,ga=np.pi/8,np.pi/2,np.pi/3
dAB=np.arccosh(np.cos(ga)/np.sin(al)); dAC=np.arccosh(1/(np.tan(al)*np.tan(ga)))
rB,rC=np.tanh(dAB/2),np.tanh(dAC/2); c0=(rB**2+1)/(2*rB); Rc=np.sqrt(c0**2-1)
Cpt=rC*np.exp(1j*al)
P(f"[T] (2,3,8) triangle: r_B={rB:.12f}, r_C={rC:.12f}; arc centre c0={c0:.12f} (real => right angle at B); |C-c0|-R = {abs(Cpt-c0)-Rc:.2e} (law-of-cosines consistency)")
# angle at C check
tC=1j*(Cpt-c0); tC/=abs(tC); ang=np.arccos(abs((tC*np.conj(np.exp(1j*al))).real))
P(f"[T] angle at C between ray and arc = {ang:.12f} vs pi/3 = {np.pi/3:.12f}")
def Rb(th): return c0*np.cos(th)-np.sqrt((c0*np.cos(th))**2-1)
def mesh(n):
    idx={}; X=[]
    for i in range(n+1):
        for j in range(i+1):
            if i==0: z=0j
            else:
                th=(j/i)*al; z=(i/n)*Rb(th)*np.exp(1j*th)
            idx[(i,j)]=len(X); X.append(z)
    tris=[]
    for i in range(n):
        for j in range(i+1):
            tris.append((idx[(i,j)],idx[(i+1,j)],idx[(i+1,j+1)]))
            if j<i: tris.append((idx[(i,j)],idx[(i+1,j+1)],idx[(i,j+1)]))
    X=np.array(X)
    sideAB=[idx[(i,0)] for i in range(n+1)]; sideAC=[idx[(i,i)] for i in range(n+1)]; sideBC=[idx[(n,j)] for j in range(n+1)]
    return X,np.array(tris),sideAB,sideAC,sideBC
def assemble(X,tris,weight=True):
    N=len(X); I=[];Jj=[];Kv=[];Mv=[]; area_h=0
    for t in tris:
        p=np.array([[X[k].real,X[k].imag] for k in t])
        Bm=np.array([p[1]-p[0],p[2]-p[0]]).T; A=abs(np.linalg.det(Bm))/2
        G=np.linalg.inv(Bm).T@np.array([[-1,1,0],[-1,0,1]])
        Ke=A*G.T@G
        mids=[(p[0]+p[1])/2,(p[1]+p[2])/2,(p[0]+p[2])/2]; phis=[[.5,.5,0],[0,.5,.5],[.5,0,.5]]
        Me=np.zeros((3,3))
        for m,ph in zip(mids,phis):
            w=4/(1-m@m)**2 if weight else 1.0
            Me+=A/3*w*np.outer(ph,ph); area_h+=A/3*w
        for a in range(3):
            for b in range(3):
                I.append(t[a]);Jj.append(t[b]);Kv.append(Ke[a,b]);Mv.append(Me[a,b])
    K=sps.csr_matrix((Kv,(I,Jj)),shape=(N,N)); M=sps.csr_matrix((Mv,(I,Jj)),shape=(N,N))
    return K,M,area_h
BCS={'NN':('N','N'),'DD':('D','D'),'DN':('D','N'),'ND':('N','D')}  # (side AB, sides AC=BC)
def solve(n,bc,k=10,weight=True):
    X,tris,AB,AC,BC=mesh(n); K,M,area=assemble(X,tris,weight)
    dir=set()
    if BCS[bc][0]=='D': dir|=set(AB)
    if BCS[bc][1]=='D': dir|=set(AC)|set(BC)
    free=np.array(sorted(set(range(len(X)))-dir))
    Kf=K[free][:,free]; Mf=M[free][:,free]
    w=spla.eigsh(Kf,k=k,M=Mf,sigma=-1.0,which='LM',return_eigenvectors=False)
    return np.sort(w),area
SU=[(3.8388872588421995,3),(5.3536013411890504,4),(8.2495548152006581,2),(14.726216787788832,4),(15.048916133267049,3),
    (18.658819627260194,3),(20.519859734142002,4),(23.078558481381635,1),(28.079605737677729,3)]
P(f"[T] exact hyperbolic area pi/24 = {np.pi/24:.10f}")
LEV=[60,120,240]; res={}
for bc in BCS:
    vals=[]
    for n in LEV:
        w,area=solve(n,bc); vals.append(w)
    ext=(4*vals[2]-vals[1])/3; ext2=(4*vals[1]-vals[0])/3
    res[bc]=ext
    P(f"[T] {bc}: FEM area(n=240)={area:.10f}")
    for q in range(len(ext)):
        P(f"    {bc} #{q}: n=60 {vals[0][q]:12.6f}  n=120 {vals[1][q]:12.6f}  n=240 {vals[2][q]:12.6f}  Richardson {ext[q]:12.6f}  (Richardson spread {abs(ext[q]-ext2[q]):.1e})")
P("[T] cross-check against Strohmaier-Uski Bolza eigenvalues (lambda<=28.08):")
for bc in BCS:
    for x in res[bc]:
        if x<1e-6 or x>28.5: continue
        best=min(SU,key=lambda s:abs(s[0]-x))
        P(f"    {bc} lambda={x:.6f} -> SU {best[0]:.10f} (mult {best[1]}), rel diff {abs(best[0]-x)/best[0]:.1e}")
lo=[(x,bc) for bc in BCS for x in res[bc] if 1e-6<x<28.5]
P(f"[T] 1-dim-character eigenvalues below 28.5: {[(round(x,5),bc) for x,bc in sorted(lo)]}")
# control: flat (unweighted) metric must NOT reproduce the hyperbolic values
wc,ac=solve(120,'NN',k=4,weight=False)
P(f"[T] CONTROL flat-metric NN (n=120): {wc}; area {ac:.5f} (must not match the SU list)")
# control: lambda_1 = 3.83889 (3-dim irrep) must be absent from all four 1-dim spectra
P(f"[T] CONTROL lambda_1 absent from 1-dim spectra: min |x-3.83889| over all = {min(abs(x-3.8388872588) for bc in BCS for x in res[bc]):.3f}")
# ---------------- S: spin-2 (Bachas-Estes) operator on Sigma-only modes for the MN2 uplift ----------------
# metric copied verbatim in form from MR2 V2 .py cand_metric (sha ad134752..., checked below): CLP uplift, upper-half-plane Sigma
t_,x1_,x2_,x3_,r_,u_,v_,al_,be_,p1_,p2_ = sp.symbols('t x1 x2 x3 r u v alpha beta phi1 phi2', real=True)
X1s,X2s,F0s,G0s,a1s,a2s = sp.symbols('X1 X2 F0 G0 a1 a2', positive=True)
m0,m1,m2 = sp.cos(al_), sp.sin(al_)*sp.cos(be_), sp.sin(al_)*sp.sin(be_)
def cand_metric():
    X1,X2 = X1s,X2s; X0 = 1/(X1*X2)**2
    D = X0*m0**2+X1*m1**2+X2*m2**2
    Gm = sp.zeros(11); w7 = D**sp.Rational(1,3)
    for i,s_ in enumerate([-1,1,1,1,1]): Gm[i,i] = w7*F0s*s_/r_**2
    Gm[5,5] = w7*G0s/v_**2; Gm[6,6] = w7*G0s/v_**2
    c = D**sp.Rational(-2,3)/4
    dm = [[sp.diff(m,al_), sp.diff(m,be_)] for m in (m0,m1,m2)]; Xs=[X0,X1,X2]
    for i in range(2):
        for j in range(2):
            Gm[7+i,7+j] += c*sum(dm[k][i]*dm[k][j]/Xs[k] for k in range(3))
    for k,(ph,ai,mu) in enumerate([(9,a1s,m1),(10,a2s,m2)]):
        fac = c*mu**2/Xs[k+1]
        Gm[ph,ph] += fac; Gm[ph,5] += fac*ai/v_; Gm[5,ph] += fac*ai/v_; Gm[5,5] += fac*ai**2/v_**2
    return Gm, w7
src_v2='/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
h=hashlib.sha256(open(src_v2,'rb').read()).hexdigest()
P(f"[S] V2 metric source sha256 {h} (expected ad134752...: {'MATCH' if h.startswith('ad134752') else 'MISMATCH'}); verbatim block present: {'G[5,5] += fac*ai**2/v**2' in open(src_v2).read()}")
Gm,w7 = cand_metric()
Gm = Gm.subs(a2s,0)
# exact MN2 point (z=1): X1 = 2^(-3/5), X2 = X0 ; G0 = X1*X2/8*((1-z)X1+(1+z)X2) ; F0 = X0^-2  (as in V2 fpar/sub)
X1v = 2**sp.Rational(-3,5); X2v = sp.symbols('X2v',positive=True)
X2v = sp.solve(sp.Eq(X2v, 1/(X1v*X2v)**2), X2v)[0]
X0v = 1/(X1v*X2v)**2
F0v = X0v**-2; G0v = X1v*X2v/8*(2*X2v)
P(f"[S] MN2 point: X1={sp.N(X1v,10)}, X2=X0={sp.N(X2v,10)}, e^2f0=F0={sp.N(F0v,10)}, e^2g0=G0={sp.N(G0v,10)}, F0/G0 = {sp.nsimplify(sp.N(F0v/G0v,30))} ({sp.N(F0v/G0v,15)})")
fu = sp.Function('f')(u_,v_)
# block inverse for the (u,v,phi1,phi2) and (alpha,beta) blocks; Sigma-only psi, phi-independent background
idx = [5,6,9,10]
B = Gm.extract(idx,idx); Binv = sp.simplify(B.inv())
sqrtg = sp.sqrt(-Gm.det())
P(f"[S] inverse-metric Sigma block: g^uu = {sp.simplify(Binv[0,0])}, g^vv = {sp.simplify(Binv[1,1])}, g^uv = {sp.simplify(Binv[0,1])}")
coordsUV=[u_,v_]
div = sum(sp.diff(sqrtg*Binv[a,b]*sp.diff(fu,coordsUV[b]), coordsUV[a]) for a in range(2) for b in range(2))
e2A = w7*F0s  # g_mu nu = e^{2A} * (unit-radius AdS5 Poincare metric)
op = -e2A*div/sqrtg
target = (F0s/G0s)*v_**2*(sp.diff(fu,u_,2)+sp.diff(fu,v_,2))*(-1)
diff_ = sp.simplify(sp.expand(op - target))
P(f"[S] spin-2 operator on psi=f(u,v): op - (F0/G0)*(-Delta_H2 f) simplifies to: {diff_}")
# numeric spot check with generic X1,X2 too (identity holds for any z since only the common D^(1/3) warp enters)
P(f"[S] => m^2 L5^2 = (F0/G0) * lambda_hyp = {sp.N(F0v/G0v,12)} * lambda for every Sigma-eigenfunction (exact, all X); (D) analogue (L5/rho)^2 = 4")
# identify which Isom 1-dim character each triangle BC realises
orient=np.array(CT96['orient'])
o_idx=[k for k,c in enumerate(CT96['chars']) if np.allclose(c.real,orient)]
P(f"[T] orientation character of Isom = chi_{o_idx} (trivial on Aut+): NN <-> chi_0 (Isom-trivial), DD <-> orientation char; DN, ND restrict to the det character of Aut+ = GL(2,3)")
# ---------------- L: can an orientation-reversing Bolza isometry act as an INTERNAL symmetry of MN2? ----------------
# local model: gamma: u -> -u on the upper half plane (orientation-reversing isometry of H^2); twist bundle forces phi1 -> -phi1
Gm1,_ = cand_metric(); Gm1 = Gm1.subs(a2s,0)
def pull(Gmat, flips):
    S = sp.diag(*[(-1 if i in flips else 1) for i in range(11)])
    sub = {u_: -u_} if 5 in flips else {}
    return sp.simplify(S*Gmat.subs(sub, simultaneous=True)*S - Gmat)
P(f"[L] metric invariant under (u->-u, phi1->-phi1): {pull(Gm1,{5,9}) == sp.zeros(11)}")
P(f"[L] metric invariant under (u->-u) alone: {pull(Gm1,{5}) == sp.zeros(11)}  (False expected: twist cross-term g_u,phi1 ~ a1/v)")
# G4 nonzero components (MR2 wall file bd47ff5e C2, all u-independent): index sets
names={0:'t',1:'x1',2:'x2',3:'x3',4:'r',5:'u',6:'v',7:'alpha',8:'beta',9:'phi1',10:'phi2'}
G4sets=[{5,6,7,10},{5,6,8,10},{5,7,8,10},{7,8,9,10}]
extras={'none':set(),'phi2->-phi2 (O(3) det -1)':{10},'x3->-x3 (5D parity P)':{3},'t->-t (time reversal T)':{0},
        'wall Z2 rho->-rho (G4 sgn(rho))':'wall','phi2 & x3':{10,3}}
for lab,ex in extras.items():
    flips={5,9}; wall=False
    if ex=='wall': wall=True
    else: flips|=ex
    sG=set(); 
    for s_ in G4sets:
        sg=(-1)**len(s_&flips)
        if wall: sg*=-1
        sG.add(sg)
    chiG = sG.pop() if len(sG)==1 else None
    chio = (-1)**len(flips)*(-1 if wall else 1)
    ok = (chiG==chio)
    P(f"[L] Bolza reflection (u,phi1) + {lab:32s}: G4 -> {chiG:+d} G4, orientation {chio:+d} -> M-theory symmetry (needs G4 sign = orientation sign): {ok}")
# ---------------- N: carry NL MN2 Sigma-constant masses (sha-checked log) ----------------
nlp='/workspace/nl-twist-1609/nl_twist_main.log'
hh=hashlib.sha256(open(nlp,'rb').read()).hexdigest()
P(f"[N] NL log sha256 {hh} (NL 418e4e50 lists 30b89fb5...: {'MATCH' if hh.startswith('30b89fb5') else 'MISMATCH'})")
for line in open(nlp):
    if line.startswith('[MN N=2 (z=1)] allowed arc'): P('[N] '+line.strip())
# ---------------- M: mass tables ----------------
def Delta(m2): return 2+np.sqrt(4+m2)
lamA=sorted([(x,'NN') for x in res['NN'] if x>1e-6]+[(x,'DD') for x in res['DD']])
lamB=sorted([(x,'NN') for x in res['NN'] if x>1e-6])
P("[M] Sigma-constant scalars (both A and B; invariant trivially): m2L2 -4 (Delta 2, SU(2)_R singlet), 0 (Delta 4, SU(2)_R 5-plet), 12 (Delta 6, singlet)")
P("[M] spin-2 tower m2L5^2 = 2*lambda (exact operator identity [S]); lambda=0: massless graviton (Delta 4)")
for lab,L in [('(A) Aut+ x wall',lamA),('(B) Isom x wall [internal reading]',lamB)]:
    P(f"[M] {lab}: first invariant nonzero levels")
    for x,bc in L[:6]:
        P(f"     lambda={x:11.5f} [{bc}]  m2L5^2={2*x:11.4f}  Delta={Delta(2*x):9.5f}")
P(f"[M] for reference (not invariant, 3-dim irrep): Bolza lambda_1 = 3.8388872588 -> m2L5^2 = {2*3.8388872588:.6f}, Delta = {Delta(2*3.8388872588):.6f}")
P(f"[M] KMP bound 3.8388976481 (all genus 2) is NOT the Bolza value; difference {3.8388976481-3.8388872588:.3e}")
P(f"[done] runtime {time.time()-T0:.1f} s")
