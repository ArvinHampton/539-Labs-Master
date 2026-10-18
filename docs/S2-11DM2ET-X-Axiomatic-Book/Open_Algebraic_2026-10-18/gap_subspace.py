# (2b) Subspace check: half-cone relation kernel K == delta_iso(Z/m^2) ⊗ X, X = {N=1, g=-1} on the complement.
import sys, json, numpy as np, cmath, math, flint
import n9h
from even_exact import red
src=open('gap_g.py').read(); exec(src.split("out=[]")[0])
res=[]
for m in map(int,sys.argv[1].split(',')):
    s=2*m*m; info=n9h.run(s); reps=n9h.run.reps; M=n9h.run.M; F=n9h.run.F; D=F.D
    X_,nul=M.transpose().nullspace(); K=[[int(X_[i,j]) for i in range(X_.nrows())] for j in range(nul)]
    dm=mpart(D,m); dc=D//dm; ec=(pow(dm,-1,dc)*dm)%D; em=(1-ec)%D
    key=[(tuple((em*np.array(al))%D),(tuple((ec*np.array(al))%D),tuple((ec*np.array(be))%D))) for al,be in F.LABELS]
    Ms=sorted({k[0] for k in key}); Cs=sorted({k[1] for k in key}); assert len(Ms)*len(Cs)==F.N
    mi={x:i for i,x in enumerate(Ms)}; ci={x:i for i,x in enumerate(Cs)}
    idx={}
    for i,(al,be) in enumerate(F.LABELS): idx.setdefault((al[0]%D,al[1]%D),[]).append((i,be))
    b0=F.BES[0]
    def ovec(O):
        v=np.zeros(F.N)
        for x in O:
            for i,be in idx[x]:
                if tuple(be)==tuple(b0): v[i]+=1
        return v
    Vo=np.array([ovec(O) for O in reps]).T
    # complement operators on Cs coordinates (labels with zero m-part)
    minv=pow(m,-1,dc)
    def lift(Mc): return np.array([[ (Mc[i][j]*ec + (1 if i==j else 0)*(1-ec))%D for j in range(2)] for i in range(2)],dtype=object)
    def mat(A):
        X=np.zeros((len(Cs),len(Cs)),complex)
        for i,(al,be) in enumerate(F.LABELS):
            if key[i][0]!=Ms[mi[tuple([0,0])]] if (0,0) in mi else True: continue
            al=np.array(al,dtype=object); be=np.array(be,dtype=object)
            j,ph=red(F,np.array([int(v) for v in A.dot(al)%D]),np.array([int(v) for v in A.dot(be)]))
            X[ci[key[j][1]],ci[key[i][1]]]=cmath.exp(2j*math.pi*float(ph))
        return X
    Xg=mat(lift([[0,-m],[minv,2*m]])); Xn=mat(lift([[-1,0],[0,-1]]))
    A=np.vstack([Xn-np.eye(len(Cs)),Xg+np.eye(len(Cs))]); _,sv,vh=np.linalg.svd(A); Xb=vh[np.sum(sv>1e-8):].conj().T
    # isotropic delta on the m-part: indicator of t^perp/t-invariant line: delta = sum over m*Z/m^2-multiples? compute from K itself and compare
    T=[]
    for k in K:
        v=Vo@np.array(k,float); Tm=np.zeros((len(Ms),len(Cs)))
        for i in range(F.N): Tm[mi[key[i][0]],ci[key[i][1]]]+=v[i]
        T.append(Tm)
    U,sv,_=np.linalg.svd(np.hstack(T)); rm=int((sv>1e-8*sv[0]).sum())
    dl=U[:,0]
    # predicted delta_iso: indicator of {x in m-part : x in (m)Z/m^2 component}, i.e. x with m*x ≡ 0
    pred=np.array([1.0 if all((m*np.array(x))%D==0) else 0.0 for x in Ms]); pred/=np.linalg.norm(pred)
    line_match=abs(abs(dl@pred)-1)<1e-9
    # complement sides: C_k = dl^T Tm ; span vs Xb
    Cside=np.array([dl@Tm for Tm in T]).T
    resid=np.linalg.norm(Cside-Xb@(Xb.conj().T@Cside))/np.linalg.norm(Cside)
    r=dict(m=m,s=s,kernel_dim=len(K),m_side_rank=rm,m_side_equals_delta_iso=bool(line_match),dimX=Xb.shape[1],
           rank_complement_side=int(np.linalg.matrix_rank(Cside,tol=1e-8)),residual_C_in_X=float(resid))
    r["subspace_equal"]=bool(rm==1 and line_match and r["rank_complement_side"]==Xb.shape[1] and resid<1e-9)
    print(json.dumps(r),flush=True); res.append(r)
json.dump(res,open("gap_subspace.json","w"),indent=1)
