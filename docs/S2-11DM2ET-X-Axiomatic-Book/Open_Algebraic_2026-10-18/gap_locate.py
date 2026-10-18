import sys, json, numpy as np, cmath, math, sympy
from fractions import Fraction as Fr
import n9h
from even_exact import run as erun, red
out=[]
for s in [int(z) for z in sys.argv[1].split(',')]:
    info=n9h.run(s); reps=n9h.run.reps; M=n9h.run.M
    r,F,O,Tw,key,Sx,Tx=erun(s); D=F.D
    # left kernel of incidence (exact)
    import flint
    X,nul=M.transpose().nullspace()
    K=[[X[i,j] for i in range(X.nrows())] for j in range(nul)]
    idx={}
    for i,(al,be) in enumerate(F.LABELS): idx.setdefault((al[0]%D,al[1]%D),[]).append((i,be))
    print("s",s,"BES",F.BES,"kernel dim",len(K),flush=True)
    # orbit vectors: labels (x, beta=BES[0])
    b0=F.BES[0]
    def ovec(Orb):
        v=np.zeros(F.N,complex)
        for x in Orb:
            for i,be in idx[x]:
                if tuple(be)==tuple(b0): v[i]+=1
        return v
    V=np.array([ovec(Orb) for Orb in reps]).T
    oi={o:i for i,o in enumerate(O)}; ti={t:i for i,t in enumerate(Tw)}
    def to_tensor(v):
        Tm=np.zeros((len(O),len(Tw)),complex)
        for i in range(F.N): Tm[oi[key[i][0]],ti[key[i][1]]]+=v[i]
        return Tm
    odd_span=[];two_span=[]
    for k in K:
        v=V@np.array([float(int(z)) for z in k]); Tm=to_tensor(v)
        U,sv,Wh=np.linalg.svd(Tm); r_=int((sv>1e-8*sv[0]).sum())
        odd_span+= [U[:,j] for j in range(r_)]; two_span+=[Wh[j] for j in range(r_)]
    Ao=np.array(odd_span).T; A2=np.array(two_span).T
    ro=np.linalg.matrix_rank(Ao,tol=1e-8); r2=np.linalg.matrix_rank(A2,tol=1e-8)
    # test: odd side invariant under translation by isotropic subgroup of order m_odd? measure
    m=info['m']; mo=m
    while mo%2==0: mo//=2
    res={"s":s,"m":m,"gap":info['gap'],"kernel_dim":len(K),"rank_odd_side":int(ro),"rank_2adic_side":int(r2),"|odd|":len(O),"|2adic|":len(Tw)}
    if mo>1:
        # translation by an element of order mo in L'_odd: find x with mo*x=0 nonzero, Q(x) in Z (isotropic)
        Oa=[np.array(o) for o in O]
        iso=[o for o in Oa if np.all((mo*o)%D==0) and np.any(o%D) and F.Q(o)%1==0]
        res["isotropic_elems"]=len(iso)
        if iso:
            t=iso[0]; Pm=np.zeros((len(O),len(O)))
            for i,o in enumerate(Oa): Pm[oi[tuple((o+t)%D)],i]=1
            res["odd_side_translation_invariant"]=bool(np.allclose(Pm@Ao,Ao) or np.linalg.matrix_rank(np.hstack([Ao,Pm@Ao]),tol=1e-8)==ro)
            # characters: is odd side supported on iso-orthogonal labels (B(x,t)=0)?
            sup=[i for i,o in enumerate(Oa) if F.B(o,t)%1!=0]
            res["odd_side_supported_on_t_perp"]=bool(np.allclose(Ao[sup],0,atol=1e-8))
    print(json.dumps(res),flush=True); out.append(res)
json.dump(out,open("gap_locate.json","w"),indent=1)
