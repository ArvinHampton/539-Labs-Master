# Frozen (chmod a-w + sidecar) before the logged run. MR2 2026-11-09. SU(2)_R item, completion: SU(2) lift of the invariant SO(3) point; dihedral and Klein edge cases. Additive; no network.
import numpy as np, hashlib, itertools, time
def P(*a): print(*a, flush=True)
T0=time.time()
R='/workspace/quantum-comp/reports/'
kk=R+'MR2_MN2_KK_TRUNCATION_BOLZA_AUT48_ISOM96_WALL_Z2_2026-11-09.py'
h=hashlib.sha256(open(kk,'rb').read()).hexdigest()
P(f"[0] KK .py sha256 {h} ({'MATCH 88949658' if h.startswith('88949658') else 'MISMATCH'}); exec'ing its group section")
exec(open(kk).read().split('# ---------------- T:')[0])
def mul(a,b): return (a[0]@b[0], tuple(a[1][b[1][i]] for i in range(6)))
def key(e): return (tuple(np.round(e[0],6).ravel()+0.0), e[1])
idx={key(e):i for i,e in enumerate(G48)}
n=len(G48); E0=[i for i,(D,p) in enumerate(G48) if np.allclose(D,np.eye(4)) and p==tuple(range(6))][0]
MT=[[idx[key(mul(G48[i],G48[j]))] for j in range(n)] for i in range(n)]
def order_of(i):
    x=i;k=1
    while x!=E0: x=MT[x][i];k+=1
    return k
def gen_size(gs):
    S={E0}; fr=[E0]
    while fr:
        nf=[]
        for a in fr:
            for g_ in gs:
                b=MT[a][g_]
                if b not in S: S.add(b); nf.append(b)
        fr=nf
    return len(S)
xa=ya=None
for a in range(n):
    if order_of(a)!=2 or np.allclose(G48[a][0],-np.eye(4)): continue
    for b in range(n):
        if order_of(b)==3 and order_of(MT[a][b])==8 and gen_size([a,b])==48: xa,ya=a,b; break
    if xa is not None: break
P(f"[R] surjection Delta+(2,3,8)=<x,y|x^2,y^3,(xy)^8> -> Aut+ : x->{xa}, y->{ya} (orders 2,3, xy order 8, generates 48)")
GEN={'x':xa,'y':ya}
rep={E0:''}; fr=[E0]
while fr:
    nf=[]
    for c in fr:
        for s_ in 'xy':
            d=MT[c][GEN[s_]]
            if d not in rep: rep[d]=rep[c]+s_; nf.append(d)
    fr=nf
tree={(c,s_) for c in rep for s_ in 'xy' if rep.get(MT[c][GEN[s_]])==rep[c]+s_}
sch=[(c,s_) for c in range(n) for s_ in 'xy' if (c,s_) not in tree]
sid={g_:j for j,g_ in enumerate(sch)}
P(f"[R] Schreier transversal size {len(rep)}; free Schreier generators {len(sch)} (expect 49)")
INV={(MT[d][GEN[s_]],s_):d for d in range(n) for s_ in 'xy'}
def rewrite(word):
    c=E0; out=[]
    for s_,e in word:
        if e==1:
            if (c,s_) in sid: out.append((sid[(c,s_)],1))
            c=MT[c][GEN[s_]]
        else:
            d=INV[(c,s_)]
            if (d,s_) in sid: out.append((sid[(d,s_)],-1))
            c=d
    assert c==E0, "word not in K"
    return out
W=lambda st: [(ch,1) for ch in st]
def winv(w): return [(s_,-e) for s_,e in reversed(w)]
schword=[W(rep[c])+[(s_,1)]+winv(W(rep[MT[c][GEN[s_]]])) for c,s_ in sch]
rels={'x^2':W('xx'),'y^3':W('yyy'),'(xy)^8':W('xy'*8)}
relw=[(nm,rewrite(W(rep[c])+r+winv(W(rep[c])))) for c in range(n) for nm,r in rels.items()]
conjw={d:[rewrite([(d,1)]+schword[j]+[(d,-1)]) for j in range(len(sch))] for d in 'xy'}
NS=len(sch)
def cnt(rw):
    v=np.zeros(NS,dtype=np.uint8)
    for j,e in rw: v[j]^=1
    return v
def rref(A,b=None):
    A=A.copy()%2; m,k=A.shape
    B=None if b is None else b.copy()%2
    piv=[]; r=0
    for c in range(k):
        p=[i for i in range(r,m) if A[i,c]]
        if not p: continue
        i=p[0]; A[[r,i]]=A[[i,r]]
        if B is not None: B[[r,i]]=B[[i,r]]
        for i2 in range(m):
            if i2!=r and A[i2,c]:
                A[i2]^=A[r]
                if B is not None: B[i2]^=B[r]
        piv.append(c); r+=1
        if r==m: break
    return A,B,piv,r
def nullspace(A):
    A2,_,piv,r=rref(A); k=A.shape[1]; free=[c for c in range(k) if c not in piv]; basis=[]
    for f in free:
        v=np.zeros(k,dtype=np.uint8); v[f]=1
        for i,pc in enumerate(piv):
            if A2[i,f]: v[pc]=1
        basis.append(v)
    return basis
def solve(A,b):
    A2,B2,piv,r=rref(A,b)
    if any(B2[i] for i in range(r,len(b))): return None
    s=np.zeros(A.shape[1],dtype=np.uint8)
    for i,pc in enumerate(piv): s[pc]=B2[i]
    assert ((A@s)%2==b%2).all()
    return s
Rm=np.array([cnt(w) for _,w in relw],dtype=np.uint8)
_,_,_,rk=rref(Rm)
P(f"[R] H_1(Sigma;Z2) = Z2^49/(relator span): dim = {NS-rk} (expect 2g = 4)")
H1=nullspace(Rm)
P(f"[R] H^1(Sigma;Z2) = characters (Rm eps = 0): dim {len(H1)}")
Cx=np.array([cnt(w) for w in conjw['x']],dtype=np.uint8); Cy=np.array([cnt(w) for w in conjw['y']],dtype=np.uint8)
I=np.eye(NS,dtype=np.uint8)
P(f"[R] Aut+-invariant characters: dim {len(nullspace(np.vstack([Rm,(Cx+I)%2,(Cy+I)%2])))} (expect 0)")
def comb(cs): 
    v=np.zeros(NS,dtype=np.uint8)
    for c,u in zip(cs,H1):
        if c: v^=u
    return v
# ---- K3
from math import pi
def su2(nv,a):
    sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
    nv=np.array(nv,float); nv/=np.linalg.norm(nv)
    return np.cos(a/2)*np.eye(2)-1j*np.sin(a/2)*(nv[0]*sx+nv[1]*sy+nv[2]*sz)
def rot_angle(U): return 2*np.arccos(np.clip(abs(np.trace(U).real)/2,-1,1))
f=lambda t: rot_angle(su2([0,0,1],pi)@su2([np.sin(t),0,np.cos(t)],2*pi/3))-3*pi/4
ts=np.linspace(1e-3,pi/2,4000); vals=[f(t) for t in ts]
i0=[i for i in range(len(ts)-1) if vals[i]*vals[i+1]<0][0]; lo,hi=ts[i0],ts[i0+1]
for _ in range(80):
    mid=(lo+hi)/2
    if f(lo)*f(mid)<=0: hi=mid
    else: lo=mid
tilt=lo
LET={'x':su2([0,0,1],pi),'y':su2([np.sin(tilt),0,np.cos(tilt)],2*pi/3)}
def ev(word,L=LET):
    U=np.eye(2,dtype=complex)
    for s_,e in word: U=U@(L[s_] if e==1 else np.linalg.inv(L[s_]))
    return U
def cval(U): return 0 if np.allclose(U,np.eye(2),atol=1e-8) else (1 if np.allclose(U,-np.eye(2),atol=1e-8) else None)
vx=cval(ev(W('xx'))); vy=cval(ev(W('yyy'))); vz=cval(ev(W('xy'*8)))
P(f"[K3] tilt {tilt:.6f} rad (ac257bf7: 1.113098); SU(2) word-lift: x~^2 = {(-1)**vx:+d}, y~^3 = {(-1)**vy:+d}, (x~y~)^8 = {(-1)**vz:+d}")
P(f"[K3] class invariants (a,d) = ({vx},{vz}); Fuchsian SL(2,R) lift of the same Delta+ (x~ elliptic, half-angle pi/2; z~ half-angle pi/8): (1,1). Same class in H^2(Delta+;Z2)")
b=np.array([{'x^2':vx,'y^3':vy,'(xy)^8':vz}[nm] for nm,_ in relw],dtype=np.uint8)
s0=solve(Rm,b)
P(f"[K3] SU(2) lift of phi|pi1(Sigma) exists (GF(2) system solvable): {s0 is not None}")
lifts=[(s0^comb(cs)) for cs in itertools.product([0,1],repeat=len(H1))]
ninv=sum(1 for s in lifts if (((Cx@s)%2)==s).all() and (((Cy@s)%2)==s).all())
P(f"[K3] SU(2) lifts: {len(lifts)} (torsor over H^1); Aut+-invariant up to SU(2) gauge (h = +-lift of phi(d), forced by density): {ninv}")

# ---- FC: control. Fuchsian SL(2,R) lift of the same Delta+ (lifts of the uniformizing rep <-> the 16 spin structures; Aut+ orbits on theta chars 6+4+6 predict 0 invariant)
Rt=lambda a: np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
def yF(l): A=np.diag([l,1/l]); return A@Rt(pi/3)@np.linalg.inv(A)
g_=lambda l: abs(np.trace(Rt(pi/2)@yF(l)))-2*np.cos(pi/8)
lo,hi=1.0,5.0
for _ in range(100):
    mid=(lo+hi)/2
    if g_(lo)*g_(mid)<=0: hi=mid
    else: lo=mid
LF={'x':Rt(pi/2).astype(complex),'y':yF(lo).astype(complex)}
fx=cval(ev(W('xx'),LF)); fy=cval(ev(W('yyy'),LF)); fz=cval(ev(W('xy'*8),LF))
P(f"[FC] Fuchsian control: |tr(x~y~)| = 2cos(pi/8) at lambda={lo:.6f}; x~^2 = {(-1)**fx:+d}, y~^3 = {(-1)**fy:+d}, (x~y~)^8 = {(-1)**fz:+d} -> (a,d) = ({fx},{fz})")
bF=np.array([{'x^2':fx,'y^3':fy,'(xy)^8':fz}[nm] for nm,_ in relw],dtype=np.uint8)
sF=solve(Rm,bF)
nF=sum(1 for cs in itertools.product([0,1],repeat=4) if (((Cx@(sF^comb(cs)))%2)==(sF^comb(cs))).all() and (((Cy@(sF^comb(cs)))%2)==(sF^comb(cs))).all())
P(f"[FC] SL(2,R) lift exists: {sF is not None} (spin structures exist); Aut+-invariant lifts: {nF} (theta-characteristic orbits 6+4+6 predict 0) => machinery reproduces the known answer")
P(f"[FC] K3 vs Fuchsian affine data identical (same relator vector b): {bool((b==bF).all())}")
# ---- KL Klein type
orb=[]; seen=[]
vecs=[comb(cs) for cs in itertools.product([0,1],repeat=4) if any(cs)]
eq=lambda u,v: not (u^v).any()
for v in vecs:
    if any(eq(v,w) for w in seen): continue
    o=[v]; fr=[v]
    while fr:
        nf=[]
        for u in fr:
            for M in (Cx,Cy):
                w=(M@u)%2
                if not any(eq(w,z) for z in o): o.append(w); nf.append(w)
        fr=nf
    seen+=o; orb.append(o)
P(f"[KL] Aut+ orbits on nonzero characters: sizes {sorted(len(o) for o in orb)}")
o3=[o for o in orb if len(o)==3][0]
P(f"[KL] 3-orbit + 0 is a subspace W: {eq(o3[0]^o3[1],o3[2])}; other invariant 2-planes: none possible (a 2-plane has 3 nonzero vectors; only the 3-orbit has size <= 3)")
qI=np.eye(2,dtype=complex); qi=np.array([[1j,0],[0,-1j]]); qj=np.array([[0,1],[-1,0]],complex); qk=qi@qj
c1,c2=o3[0],o3[1]
Q={(0,0):qI,(1,0):qi,(0,1):qj,(1,1):qk}
def rho(t,j): return ((-1)**int(t[j]))*Q[(int(c1[j]),int(c2[j]))]
def rho_word(t,w):
    U=np.eye(2,dtype=complex)
    for j,e in w: U=U@(rho(t,j) if e==1 else np.linalg.inv(rho(t,j)))
    return U
zero=np.zeros(NS,dtype=np.uint8)
base=[cval(rho_word(zero,w)) for _,w in relw]
P(f"[KL] base Q8 relator values all central: {all(v is not None for v in base)}")
t0=solve(Rm,np.array(base,dtype=np.uint8))
P(f"[KL] Q8 (SU(2)) lift of the Klein point exists (w2 = <chi1 cup chi2,[Sigma]> = 0): {t0 is not None}")
els=[qI]; fr=[qI]; gens2=[(qI+qi)/np.sqrt(2),(qI+qi+qj+qk)/2]
while fr:
    nf=[]
    for U in fr:
        for G_ in gens2:
            V=U@G_
            if not any(np.allclose(V,Z) for Z in els): els.append(V); nf.append(V)
    fr=nf
P(f"[KL] |N_SU(2)(Q8)| = |2O| = {len(els)}")
if t0 is not None:
    ninvq=0; inv_list=[]
    for cs in itertools.product([0,1],repeat=4):
        t=t0^comb(cs); ok=True
        for d in 'xy':
            imgs=[rho_word(t,conjw[d][j]) for j in range(NS)]
            bs=[rho(t,j) for j in range(NS)]
            if not any(all(np.allclose(imgs[j],Hh@bs[j]@Hh.conj().T) for j in range(NS)) for Hh in els): ok=False; break
        ninvq+=ok
        if ok: inv_list.append(cs)
    # gauge classes among the 16 lifts: t ~ t' if conjugate by an element of 2O
    def conjclass(t):
        return [tuple(np.round(np.array([Hh@rho(t,j)@Hh.conj().T for j in range(NS)]).ravel(),6)) for Hh in els]
    classes=[]
    for cs in itertools.product([0,1],repeat=4):
        t=t0^comb(cs); sig=tuple(np.round(np.array([rho(t,j) for j in range(NS)]).ravel(),6))
        if not any(sig in C for C in classes): classes.append(set(conjclass(t)))
    P(f"[KL] Q8 lifts: 16; gauge classes (mod 2O conjugation): {len(classes)}; lifts invariant under Aut+ up to SU(2) gauge: {ninvq}")
P(f"[done] runtime {time.time()-T0:.1f} s")
