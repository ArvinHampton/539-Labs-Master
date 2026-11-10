# Frozen (chmod a-w + sidecar) before the logged run. MR2 2026-11-09. Irrep labels of the low Bolza Laplace levels (OW 8b26c786, Group A).
# Method: every real irrep pi of Isom (order 96) -> vector-valued P1 FEM on the (2,3,8) triangle with BC  u in V+(pi(r_i)) on edge i (essential),
# natural Neumann on the rest; eigenvalue multiplicity = multiplicity of pi in the Laplace eigenspace. Additive; no network.
import numpy as np, hashlib, itertools, time, scipy.sparse as sps, scipy.sparse.linalg as spla
def P(*a): print(*a, flush=True)
def sg(x):
    v=int(round(x)); return f"{v:+d}" if v else "0"
T0=time.time()
R='/workspace/quantum-comp/reports/'
kk=R+'MR2_MN2_KK_TRUNCATION_BOLZA_AUT48_ISOM96_WALL_Z2_2026-11-09.py'
h=hashlib.sha256(open(kk,'rb').read()).hexdigest()
P(f"[0] KK .py sha256 {h} ({'MATCH 88949658' if h.startswith('88949658') else 'MISMATCH'}); exec'ing its group section [G]/[W] and FEM helpers of [T] (mesh/assemble only)")
src=open(kk).read()
exec(src.split('# ---------------- T:')[0])
tsec=src.split('# ---------------- T:')[1].split('BCS=')[0].split('\n',1)[1]
exec(tsec)
def mul(a,b): return (a[0]@b[0], tuple(a[1][b[1][i]] for i in range(6)))
def key(e): return (tuple(np.round(e[0],6).ravel()+0.0), e[1])
G=G96; n=len(G); idx={key(e):i for i,e in enumerate(G)}
E0=[i for i,(D,p) in enumerate(G) if np.allclose(D,np.eye(4)) and p==tuple(range(6))][0]
MT=np.array([[idx[key(mul(G[i],G[j]))] for j in range(n)] for i in range(n)])
INV=[int(np.where(MT[i]==E0)[0][0]) for i in range(n)]
def order(i):
    x=i;k=1
    while x!=E0: x=MT[x][i];k+=1
    return k
Jc_=Jc
anti=[i for i,(D,p) in enumerate(G) if np.allclose(D@Jc_,-Jc_@D)]
inv_anti=[i for i in anti if order(i)==2]
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
trip=None
for a,b,c in itertools.permutations(inv_anti,3):
    if order(MT[a][b])==8 and order(MT[a][c])==2 and order(MT[b][c])==3 and gen_size([a,b,c])==96: trip=(a,b,c); break
rAB,rAC,rBC=trip
P(f"[C] Coxeter triple in Isom: antiholomorphic involutions r_AB,r_AC,r_BC with orders (r_AB r_AC, r_AB r_BC, r_AC r_BC) = ({order(MT[rAB][rAC])},{order(MT[rAB][rBC])},{order(MT[rAC][rBC])}), generating {gen_size(list(trip))} elements")
# hom from generators: BFS words
def rep_from_gens(gm):
    d=gm[rAB].shape[0]; Rm={E0:np.eye(d)}; fr=[E0]; ok=True
    while fr:
        nf=[]
        for a in fr:
            for g_ in (rAB,rAC,rBC):
                b=MT[a][g_]; M=Rm[a]@gm[g_]
                if b in Rm:
                    if not np.allclose(Rm[b],M,atol=1e-9): ok=False
                else: Rm[b]=M; nf.append(b)
        fr=nf
    return [Rm[i] for i in range(n)], ok
# T: B3 mirrors (A: pi/8 -> order 4; B; C)
def refl(v): v=np.array(v,float); v/=np.linalg.norm(v); return np.eye(3)-2*np.outer(v,v)
Tg={rAB:refl([0,0,1]),rAC:refl([0,1,-1]),rBC:refl([1,-1,0])}
Trep,okT=rep_from_gens(Tg)
P(f"[C] Isom -> O_h (B3 mirrors e3, e2-e3, e1-e2) well defined on all 96 elements: {okT}; kernel size {sum(np.allclose(M,np.eye(3)) for M in Trep)} (= <J>, order 2)")
# H^1 rep, orthogonalised
S=sum(D.T@D for D,_ in G); Rc_=np.linalg.cholesky(S).T
H1=[Rc_@D@np.linalg.inv(Rc_) for D,_ in G]
P(f"[C] H^1 rep orthogonal after Gram change of basis: {all(np.allclose(M@M.T,np.eye(4)) for M in H1)}")
# 1-dim characters: (eps_AB, eps_AC=eps_BC)
chars={}
for nm,(e1,e2) in {'NN':(1,1),'DD':(-1,-1),'DN':(-1,1),'ND':(1,-1)}.items():
    cr,okc=rep_from_gens({rAB:np.array([[e1]],float),rAC:np.array([[e2]],float),rBC:np.array([[e2]],float)})
    chars[nm]=cr; assert okc
def tensor(A,B): return [np.kron(a,b) for a,b in zip(A,B)]
def charvec(rep): return np.array([np.trace(M) for M in rep])
rng=np.random.default_rng(1)
def split(rep):
    d=rep[0].shape[0]; X=rng.standard_normal((d,d)); X=X+X.T
    A=sum(M@X@M.T for M in rep)/n
    w,V=np.linalg.eigh(A); out=[]; i=0
    while i<d:
        j=i
        while j<d and abs(w[j]-w[i])<1e-7*max(1,abs(w[i])): j+=1
        Q=V[:,i:j]; out.append([Q.T@M@Q for M in rep]); i=j
    return out
irreps=[]
def add(rep):
    for r in split(rep):
        cv=charvec(r)
        if abs(cv@cv/n-1)>1e-6: continue   # not absolutely irreducible over R (would need more care)
        if not any(np.allclose(cv,charvec(q),atol=1e-6) for q in irreps): irreps.append(r)
for nm in chars: add(chars[nm])
for nm in chars: add(tensor(Trep,chars[nm]))
add(tensor(Trep,Trep))
for nm in chars: add(tensor(tensor(Trep,Trep),chars[nm]))
for nm in chars: add(tensor(H1,chars[nm]))
for nm in chars: add(tensor(tensor(H1,Trep),chars[nm]))
dims=sorted(r[0].shape[0] for r in irreps)
P(f"[C] real orthogonal irreps found: {len(irreps)}, dims {dims}, sum d^2 = {sum(d*d for d in dims)} (|Isom| = 96 => complete iff 96; all real type iff <chi,chi> = 1 each)")
Jidx=[i for i,(D,p) in enumerate(G) if np.allclose(D,-np.eye(4))][0]
G48i=[i for i in range(n) if i not in anti]
# Aut+ labels: restriction characters on order-8 elements (det = -1 class) etc.
z=MT[rAB][rAC]
def name(r):
    d=r[0].shape[0]; cv=charvec(r)
    e=[int(round(r[g_][0,0])) if d==1 else None for g_ in (rAB,rAC)]
    return d,cv
rows=[]
for k,r in enumerate(irreps):
    d=r[0].shape[0]; cv=charvec(r)
    rows.append(dict(k=k,d=d,J=cv[Jidx],z=cv[z],rAB=cv[rAB],rAC=cv[rAC],rBC=cv[rBC],rep=r))
rows.sort(key=lambda q:(q['d'],-q['J'],-q['z'],-q['rAB'],-q['rAC']))
# Aut+ restriction decomposition by characters: build Aut+ irreps from restrictions
def res(r): return [r[i] for i in G48i]
irr48=[]
for q in rows:
    rr=res(q['rep']); d=rr[0].shape[0]; X=rng.standard_normal((d,d)); X=X+X.T
    A=sum(M@X@M.T for M in rr)/48; w,V=np.linalg.eigh(A); i=0
    while i<d:
        j=i
        while j<d and abs(w[j]-w[i])<1e-7*max(1,abs(w[i])): j+=1
        Q=V[:,i:j]; sub=[Q.T@M@Q for M in rr]; cv=np.array([np.trace(M) for M in sub]); i=j
        if not any(np.allclose(cv,c,atol=1e-6) for c,_ in irr48): irr48.append((cv,Q.shape[1]))
zi=G48i.index(z); Ji=G48i.index(Jidx)
def lab48(cv,d):
    nrm=cv@cv/48
    tag={1:'1' if cv[zi]>0 else 'sgn',3:'3' if cv[zi]>0 else '3(x)sgn',2:'2(J-trivial)',4:'4(J-faithful)'}.get(d,str(d))
    if d==4 and round(nrm)==2: tag="2'+2'' (complex pair, real 4-dim)"
    if d==2 and cv[Ji]<0: tag="2-faithful"
    return tag
P("[C] Aut+ = GL(2,3) real-irreducible pieces (labels: 3 := trace +1 on the order-8 rotation z = r_AB r_AC; 3(x)sgn := 3 tensor det, trace -1 on z):")
for cv,d in sorted(irr48,key=lambda t:t[1]):
    P(f"     dim {d}: <chi,chi> = {cv@cv/48:.0f}, chi(J) = {sg(cv[Ji])}, chi(z) = {sg(cv[zi])} -> {lab48(cv,d)}")
def aut_decomp(q):
    rr=res(q['rep']); cvr=np.array([np.trace(M) for M in rr]); out=[]
    for cv,d in irr48:
        m=round((cvr@cv)/(cv@cv))
        if m: out.append(f"{m if m>1 else ''}{lab48(cv,d)}")
    return ' + '.join(out)
P("[C] Isom irreps (tag; dim; chi(J); chi(z); chi(r_AB); chi(r_AC); chi(r_BC); restriction to Aut+):")
for t,q in enumerate(rows):
    q['tag']=f"I{t+1}"
    P(f"     {q['tag']}: dim {q['d']}, chi(J) {sg(q['J'])}, chi(z) {sg(q['z'])}, chi(r_AB) {sg(q['rAB'])}, chi(r_AC) {sg(q['rAC'])}, chi(r_BC) {sg(q['rBC'])} | Aut+: {aut_decomp(q)}")
# ---------------- F: vector FEM ----------------
def solve_vec(nm, rep, k=8):
    d=rep[0].shape[0]
    X,tris,AB,AC,BC=mesh(nm); K,M,area=assemble(X,tris,True)
    def plus(g_):
        w,V=np.linalg.eigh((rep[g_]+rep[g_].T)/2); return V[:,w>0]
    Vp={'AB':plus(rAB),'AC':plus(rAC),'BC':plus(rBC)}
    on={i:[] for i in range(len(X))}
    for nm2,side in (('AB',AB),('AC',AC),('BC',BC)):
        for i in side: on[i].append(nm2)
    rows_,cols_,vals_=[],[],[]; col=0
    for i in range(len(X)):
        if not on[i]: B=np.eye(d)
        else:
            Pr=np.eye(d)
            for s_ in set(on[i]): Pr=Pr@ (Vp[s_]@Vp[s_].T)
            # intersection of the + eigenspaces
            Ms=[np.eye(d)-Vp[s_]@Vp[s_].T for s_ in set(on[i])]
            Cm=np.vstack(Ms); u,sv,vt=np.linalg.svd(Cm); null=vt[(sv>1e-9).sum():].T if Cm.shape[0]>=d else None
            if Cm.shape[0]<d: 
                u,sv,vt=np.linalg.svd(Cm,full_matrices=True); null=vt[(sv>1e-9).sum():].T
            B=null
        for a in range(B.shape[1]):
            for r_ in range(d):
                if abs(B[r_,a])>1e-14: rows_.append(i*d+r_); cols_.append(col); vals_.append(B[r_,a])
            col+=1
    Pm=sps.csr_matrix((vals_,(rows_,cols_)),shape=(len(X)*d,col))
    Kd=sps.kron(K,sps.eye(d)); Md=sps.kron(M,sps.eye(d))
    Kf=(Pm.T@Kd@Pm).tocsc(); Mf=(Pm.T@Md@Pm).tocsc()
    w=spla.eigsh(Kf,k=k,M=Mf,sigma=-1.0,which='LM',return_eigenvectors=False)
    return np.sort(w)
LEV=[60,120]
LMAX=25.5
SUref=[(3.8388872588421995,3),(5.3536013411890504,4),(8.2495548152006581,2),(14.726216787788832,4),(15.048916133267049,3),(18.658819627260194,3),(20.519859734142002,4),(23.078558481381635,1)]
levels=[]
for q in rows:
    kq=6 if q['d']<=2 else 8
    vals=[solve_vec(nm_,q['rep'],k=kq) for nm_ in LEV]
    ext=(4*vals[1]-vals[0])/3
    low=[(x,abs(vals[1][i]-x)) for i,x in enumerate(ext) if x<LMAX]
    for x,e in low:
        if x>1e-6: levels.append((x,q['tag'],q['d'],e))
    P(f"[F] {q['tag']} (dim {q['d']}): Richardson(60,120) eigenvalues < {LMAX}: {[f'{x:.5f}' for x,_ in low]}  (largest computed {ext[-1]:.3f}; Richardson correction sizes {[f'{e:.1e}' for _,e in low]})")
P("[F] control: the 1-dim sectors I1-I4 must match the scalar NN/DD/DN/ND FEM of ecee2668 (NN 0, 23.078559; DN 32.673650; ND 91.464863; DD 222.371127): only I1 has eigenvalues below 25.5 (0 and 23.0786)")
P(f"[F] Weyl check: number of nonzero eigenvalues below 25.5 counted with multiplicity = {sum(d for x,t,d,e in levels)}; Weyl leading term area*lambda/(4 pi) = 4 pi (g-1) * 25.5/(4 pi) = 25.5")
levels.sort()
P("[L] assembled spectrum (lambda < 25.5): eigenvalue, Isom irrep, dim; grouped by level (tolerance 2e-3):")
grp=[]
for x,t,d,e in levels:
    if grp and abs(grp[-1][0]-x)<2e-3: grp[-1][1].append((t,d,x))
    else: grp.append([x,[(t,d,x)]])
tagq={q['tag']:q for q in rows}
for x,lst in grp:
    mult=sum(d for _,d,_ in lst); best=min(SUref,key=lambda s:abs(s[0]-x))
    aut=' + '.join(aut_decomp(tagq[t]) for t,_,_ in lst)
    P(f"     lambda = {x:.5f}: Isom {' + '.join(t for t,_,_ in lst)} | dim {mult} | Aut+: {aut} | SU nearest {best[0]:.6f} (mult {best[1]}), rel diff {abs(best[0]-x)/best[0]:.1e}")
P(f"[done] runtime {time.time()-T0:.1f} s")
