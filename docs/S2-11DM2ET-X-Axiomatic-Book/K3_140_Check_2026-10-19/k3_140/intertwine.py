# Hom_{SL2(Z)}(rho_W, rho_rev) over F_ell, rho_W = Weil rep of the even lattice N2=[[2,14],[14,28]] (or variants), rho_rev = rev6 s=7 label rep.
# Unknown X (140x140) with X rho_W(g) = rho_rev(g) X for g=S,T. Exactness: random row-compression can only enlarge the solution space;
# every basis vector found is then verified against the FULL S- and T-equations, so the computed space is exactly Hom over F_ell.
import pickle, json, sys, itertools, random
import numpy as np, sympy as sp
from fractions import Fraction as Fr
from collections import Counter, defaultdict
R=pickle.load(open('rev_s7_exact.pkl','rb')); N=140
# prime ell = 1 mod 280, ell < 2^20
ell=next(p for p in range(280*3000+1,2**20,280) if sp.isprime(p)); p=ell
g=sp.primitive_root(p); z280=pow(int(g),(p-1)//280,p)
def E(r):  # e(r) for r in (1/280)Z
    r=Fr(r)%1; assert (280*r).denominator==1; return pow(z280,int(280*r),p)
inv=lambda a: pow(int(a)%p,p-2,p)
I4=E(Fr(1,4))
s5=sum(E(Fr(2*x*x,5)) if False else E(Fr(x*x,5)) for x in range(5))%p     # Gauss sum, = sqrt5 (5=1 mod 4)
s7=(-I4*sum(E(Fr(x*x,7)) for x in range(7)))%p                             # sqrt7 = -i*g7
assert s5*s5%p==5 and s7*s7%p==7
r35=s5*s7%p; ir35=inv(r35)
def mat_from(d,scale=1):
    M=np.zeros((N,N),dtype=np.int64)
    for (i,j),r in d.items(): M[i,j]=E(r)*scale%p
    return M
S_lab=mat_from(R['S'],ir35); T_rev=mat_from(R['T'])
S_lab_inv=np.zeros((N,N),dtype=np.int64)
for (i,j),r in R['S'].items(): S_lab_inv[j,i]=E(-r)*ir35%p
def mm(A,B):  # mod-p product, entries < 2^20
    return (A@B)%p
Id=np.eye(N,dtype=np.int64)
assert np.array_equal(mm(S_lab,S_lab_inv),Id)
# Weil rep of N2 (Borcherds convention, sig=0): rho(T)e_y=e(q(y))e_y, rho(S)e_y = |A|^{-1/2} sum_d e(-b(y,d)) e_d
def weil(G,dual=False):
    G=sp.Matrix(G); Gi=G.inv(); d=abs(G.det())
    reps={}
    for m1 in range(d):
        for m2 in range(d):
            y=Gi*sp.Matrix([m1,m2]); key=tuple(Fr(str(v))%1 for v in y)
            reps.setdefault(key,y)
    els=list(reps.values()); assert len(els)==d
    q=[Fr(str((y.T*G*y)[0]/2))%1 for y in els]
    b=[[Fr(str((y.T*G*w)[0]))%1 for w in els] for y in els]
    sg=-1 if dual else 1
    TW=np.zeros((d,d),dtype=np.int64); SW=np.zeros((d,d),dtype=np.int64)
    ir140=inv(2*r35)
    for k in range(d): TW[k,k]=E(sg*q[k])
    for k in range(d):
        for l in range(d): SW[l,k]=E(-sg*b[k][l])*ir140%p   # column k = image of e_k
    return els,q,TW,SW
def check_rel(S,T):
    S2=mm(S,S); return {'S^4=I':bool(np.array_equal(mm(S2,S2),Id)),'(ST)^3=S^2':bool(np.array_equal(mm(mm(mm(S,T),mm(S,T)),mm(S,T)),S2))}
def hom(SW,TW,SR,TR,seed=1):
    # eigen-decompose TR (monomial: fixed points and 2-cycles) exactly over F_p
    nxt={i:int(np.nonzero(TR[:,i])[0][0]) for i in range(N)}   # T e_i = TR[k,i] e_k
    V=np.zeros((N,N),dtype=np.int64); lam=[]; col=0; done=set()
    for i in range(N):
        if i in done: continue
        j=nxt[i]
        if j==i: V[i,col]=1; lam.append(TR[i,i]); col+=1; done.add(i)
        else:
            assert nxt[j]==i; done|={i,j}
            a=TR[j,i]; bb=TR[i,j]   # T e_i = a e_j, T e_j = bb e_i
            ab=a*bb%p
            rts=[x for x in sp.ntheory.residue_ntheory.sqrt_mod(int(ab),p,all_roots=True)]
            for lm in rts:   # v = e_i + c e_j with T v = lm v: T v = a e_j + c bb e_i => c*bb=lm, a=lm*c
                c=lm*inv(bb)%p; assert a%p==lm*c%p
                V[i,col]=1; V[j,col]=c; lam.append(lm); col+=1
    assert col==N
    Vi=np.array(sp.Matrix(V.tolist()).inv_mod(p).tolist(),dtype=np.int64)
    assert np.array_equal(mm(Vi,V),Id) and np.array_equal(mm(mm(Vi,TR),V),np.diag(np.array(lam,dtype=np.int64)%p))
    lamW=[int(TW[k,k]) for k in range(N)]
    if Counter(lam)!=Counter(lamW): return {'T_spectra_equal':False}
    Sp=mm(mm(Vi,SR),V)
    # unknowns Y[i,k] with lam[i]==lamW[k]
    unk=[(i,k) for i in range(N) for k in range(N) if lam[i]==lamW[k]]
    U=len(unk); idx={u:n for n,u in enumerate(unk)}
    byrow=defaultdict(list); bycol=defaultdict(list)
    for n,(i,k) in enumerate(unk): byrow[i].append((k,n)); bycol[k].append((i,n))
    # equation (i,k): sum_j Sp[i,j] Y[j,k] - sum_j Y[i,j] SW[j,k] = 0  -> row vector over unknowns
    rng=np.random.default_rng(seed); m=U+40
    C=np.zeros((m,U),dtype=np.int64)
    # accumulate random combinations without materialising all 19600 rows at once: process by k
    for k in range(N):
        rows=np.zeros((N,U),dtype=np.int64)
        for (j,n) in bycol[k]:          # Y[j,k]
            rows[:,n]=(rows[:,n]+Sp[:,j])%p
        for i in range(N):
            for (jj,n) in byrow[i]:     # Y[i,jj]*SW[jj,k]
                rows[i,n]=(rows[i,n]-SW[jj,k])%p
        Rk=rng.integers(0,p,size=(m,N),dtype=np.int64)
        C=(C+(Rk@rows)%p)%p
    ns=nullspace_mod(C,p)
    # verify each basis vector against full equations
    sols=[]
    for v in ns:
        Y=np.zeros((N,N),dtype=np.int64)
        for n,(i,k) in enumerate(unk): Y[i,k]=v[n]
        X=mm(V,Y)
        okS=np.array_equal(mm(X,SW),mm(SR,X)); okT=np.array_equal(mm(X,TW),mm(TR,X))
        assert okS and okT, "compressed solution fails full system"
        sols.append(X)
    res={'T_spectra_equal':True,'unknowns':U,'dim_Hom':len(sols)}
    if sols:
        rnd=np.random.default_rng(seed+7); X=np.zeros((N,N),dtype=np.int64)
        for Xs in sols: X=(X+int(rnd.integers(1,p))*Xs)%p
        rk=int(sp.Matrix(X.tolist()).rank(iszerofunc=lambda x: x%p==0)) if False else rank_mod(X,p)
        res['rank_of_random_combination']=rk
        res['_X']=X
    return res
def rank_mod(A,p):
    A=A.copy()%p; r=0; rows,cols=A.shape
    for c in range(cols):
        piv=next((i for i in range(r,rows) if A[i,c]),None)
        if piv is None: continue
        A[[r,piv]]=A[[piv,r]]; A[r]=A[r]*inv(A[r,c])%p
        nz=np.nonzero(A[:,c])[0]
        for i in nz:
            if i!=r: A[i]=(A[i]-A[i,c]*A[r])%p
        r+=1
        if r==rows: break
    return r
def nullspace_mod(A,p):
    A=A.copy()%p; rows,cols=A.shape; r=0; pivs=[]
    for c in range(cols):
        piv=next((i for i in range(r,rows) if A[i,c]),None)
        if piv is None: continue
        A[[r,piv]]=A[[piv,r]]; A[r]=A[r]*inv(A[r,c])%p
        col=A[:,c].copy(); col[r]=0
        A=(A-np.outer(col,A[r]))%p
        pivs.append(c); r+=1
        if r==rows: break
    free=[c for c in range(cols) if c not in set(pivs)]
    basis=[]
    for f in free:
        v=np.zeros(cols,dtype=np.int64); v[f]=1
        for i,c in enumerate(pivs): v[c]=(-A[i,f])%p
        basis.append(v)
    return basis
if __name__=="__main__":
    out={'ell':ell}
    out['rev_relations']={'(S_lab,T)':check_rel(S_lab,T_rev),'(S_lab^-1,T)':check_rel(S_lab_inv,T_rev)}
    lat={'N2=[[2,14],[14,28]]':[[2,14],[14,28]],'N1=[[4,14],[14,14]]':[[4,14],[14,14]]}
    Xkeep=None
    for ln,G in lat.items():
        for dual in (False,True):
            els,q,TW,SW=weil(G,dual)
            key=f"{ln}{' dual' if dual else ''}"
            out[key+' Weil relations']=check_rel(SW,TW)
            for rn,(SR,TR) in {'(S_lab^-1,T)':(S_lab_inv,T_rev),'(S_lab,T)':(S_lab,T_rev)}.items():
                r=hom(SW,TW,SR,TR)
                X=r.pop('_X',None)
                out[f'Hom(rho_W[{key}], rho_rev{rn})']=r; print(key,rn,r,flush=True)
                if X is not None and r.get('rank_of_random_combination')==N and Xkeep is None:
                    Xkeep=(key,rn,X,els,q)
    json.dump(out,open('intertwine.json','w'),indent=1,default=str)
    if Xkeep: pickle.dump({'lattice':Xkeep[0],'rev':Xkeep[1],'X':Xkeep[2],'ell':ell,'els':[tuple(str(v) for v in y) for y in Xkeep[3]],'q':[str(x) for x in Xkeep[4]]},open('X_modl.pkl','wb'))
