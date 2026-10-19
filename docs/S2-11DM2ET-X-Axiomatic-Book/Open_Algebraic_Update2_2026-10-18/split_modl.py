# Item 1 exact: irreducibility of eps-sectors via mod-ell Krylov from simple T-eigenvectors.
# Argument: rho finite-order, ell ≡ 1 mod Kbig (all eigenvalues in F_ell, distinct reductions), so mod-ell eigenspace dims
# equal char-0 ones; a mod-ell 1-dim eigenspace is the reduction of the char-0 eigenline; Krylov rank mod ell <= char-0 rank.
# If an eigenvector of a SIMPLE T-eigenvalue generates all of E mod ell, E is irreducible over C (unitary => semisimple).
import sys, json, math, itertools, numpy as np, flint, sympy
from vecfam import VF, to_complex
def nm(E,zeta_pow,ell):  # exponent matrix -> nmod_mat
    n,m=E.shape; L=[[0 if E[i,j]<0 else zeta_pow[E[i,j]] for j in range(m)] for i in range(n)]
    return flint.nmod_mat(L,ell)
for s in map(int,sys.argv[1].split(',')):
    v=VF(s); K=v.K; SE_=v.S_exp(); TE_=v.T_exp(); MP=v.maps(); N=v.N
    # T cycle lengths
    perm=[int(np.nonzero(TE_[i]>=0)[0][0]) for i in range(N)]
    seen=set(); lens=set()
    for i in range(N):
        if i in seen: continue
        c=0; j=i
        while j not in seen: seen.add(j); j=perm[j]; c+=1
        lens.add(c)
    Kbig=K*math.lcm(*lens)
    k=1
    while True:
        ell=k*Kbig+1
        if ell<2**62 and sympy.isprime(ell): break
        k+=1
    gen=sympy.primitive_root(ell); zeta=pow(gen,(ell-1)//Kbig,ell)
    zp=[pow(zeta,a*(Kbig//K),ell) for a in range(K)]
    S=nm(SE_,zp,ell); T=nm(TE_,zp,ell); Ms={k_:nm(E,zp,ell) for k_,E in MP.items()}
    ps=[k_ for k_ in MP if isinstance(k_,int)]
    I=flint.nmod_mat([[int(i==j) for j in range(N)] for i in range(N)],ell)
    Tc=to_complex(TE_,K); Sc=to_complex(SE_,K)
    res={"s":s,"ell":int(ell),"Kbig":int(Kbig),"sectors":[]}
    for eps in [tuple(1 for _ in ps)]:
        blocks=[Ms['neg']-I,Ms['gamma']-I]+[Ms[p]-(I if e==1 else I*(ell-1)) for p,e in zip(ps,eps)]
        St=flint.nmod_mat([[int(b[i,j]) for j in range(N)] for b in blocks for i in range(N)],ell)
        X,nul=St.nullspace()
        d=nul
        if d==0: continue
        Eb=flint.nmod_mat([[int(X[i,j]) for j in range(d)] for i in range(N)],ell)   # N x d
        # pivot rows
        R,rk=Eb.transpose().rref()
        piv=[]; r=0
        for j in range(N):
            if r<rk and int(R[r,j])!=0: piv.append(j); r+=1
        Ep=flint.nmod_mat([[int(Eb[i,j]) for j in range(d)] for i in piv],ell); Epi=Ep.inv()
        def restrict(M):
            ME=M*Eb; MEp=flint.nmod_mat([[int(ME[i,j]) for j in range(d)] for i in piv],ell); return Epi*MEp
        Sd=restrict(S); Td=restrict(T)
        cp=Td.charpoly(); fac=cp.factor()[1]
        simple_l=[int(-f[0])%ell for f,e in fac if f.degree()==1 and e==1]
        simple=simple_l
        import random
        random.seed(1)
        def krylov(vec):
            B=flint.nmod_mat([vec],ell); r0=1
            while True:
                rows=[[int(M_[i,j]) for j in range(d)] for M_ in (B,B*Sd.transpose(),B*Td.transpose()) for i in range(M_.nrows())]
                Rm,rr=flint.nmod_mat(rows,ell).rref()
                B=flint.nmod_mat([[int(Rm[i,j]) for j in range(d)] for i in range(rr)],ell)
                if rr==r0: return B,rr
                r0=rr
        def rank(rows):
            return flint.nmod_mat(rows,ell).rref()[1] if rows else 0
        # eigen-decomposition of Td mod ell
        roots=[(int(-f[0])%ell,e) for f,e in fac]; assert all(f.degree()==1 for f,e in fac)
        cols=[]; blocks=[]
        for lam,e in roots:
            Y,ny=(Td-flint.nmod_mat([[lam*int(i==j) for j in range(d)] for i in range(d)],ell)).nullspace()
            assert ny==e   # T semisimple mod ell
            idx=list(range(len(cols),len(cols)+ny)); blocks.append((lam,idx))
            cols+= [[int(Y[i,j]) for i in range(d)] for j in range(ny)]
        P=flint.nmod_mat(cols,ell).transpose(); Sp=P.inv()*Sd*P
        unk=[(i,j) for lam,idx in blocks for i in idx for j in idx]
        nU=len(unk); rows=[]
        for t in range(nU+40):
            u=flint.nmod_mat([[random.randrange(ell) for _ in range(d)]],ell)
            w=flint.nmod_mat([[random.randrange(ell)] for _ in range(d)],ell)
            aa=u*Sp; bb=Sp*w
            av=[int(aa[0,i]) for i in range(d)]; uv=[int(u[0,i]) for i in range(d)]
            bv=[int(bb[i,0]) for i in range(d)]; wv=[int(w[i,0]) for i in range(d)]
            rows.append([(av[i]*wv[j]-uv[i]*bv[j])%ell for i,j in unk])
        NS,comm_ub=flint.nmod_mat(rows,ell).nullspace()
        Xs=[]
        for c in range(comm_ub):
            X=[[0]*d for _ in range(d)]
            for k_,(i,j) in enumerate(unk): X[i][j]=int(NS[k_,c])
            X=flint.nmod_mat(X,ell); Xs.append(X)
            assert Sp*X==X*Sp, "spurious"
        print(s,"commutant basis verified exactly:",comm_ub,flush=True)
        # pick non-scalar X; its eigenvalues; kernels in original sector coords
        Id_=flint.nmod_mat([[int(i==j) for j in range(d)] for i in range(d)],ell)
        comps=[]
        for X in Xs:
            if X==Id_*int(X[0,0]): continue
            cpX=X.charpoly().factor()[1]
            for f,e in cpX:
                assert f.degree()==1
                mu=int(-f[0])%ell
                Kx,nk=(X-Id_*mu).nullspace()
                Wc=P*flint.nmod_mat([[int(Kx[i,j]) for j in range(nk)] for i in range(d)],ell)
                inv_S=rank([[int(Wc[i,j]) for i in range(d)] for j in range(nk)]+[[int(r) for r in ((Sd*Wc).transpose())[j]] if False else [int((Sd*Wc)[i,j]) for i in range(d)] for j in range(nk)])
                vec0=[int(Wc[i,0]) for i in range(d)]
                _,kr=krylov(vec0)
                comps.append((nk,inv_S,kr,[[int(Wc[i,j]) for i in range(d)] for j in range(nk)]))
                print(s,"X-eigenspace dim",nk,"rank(W ∪ S W)",inv_S,"Krylov rank from its first vector",kr,flush=True)
            break
        if comps: print(s,"rank of sum of X-eigenspaces",rank([r for c in comps for r in c[3]]),flush=True)
        print(s,"unknowns",nU,"commutant_upper_bound_modl",comm_ub,flush=True)
        # Krylov from every simple eigenvector; collect distinct invariant subspaces
        spaces=[]; spans=[]
        for lam in simple:
            j=[idx for l,idx in blocks if l==lam][0][0]
            vec=[int(P[i,j]) for i in range(d)]
            if any(rank(Wr+[vec])==len(Wr) for Wr,_ in spaces): continue
            B,rr=krylov(vec); Wr=[[int(B[i,k_]) for k_ in range(d)] for i in range(rr)]
            spaces.append((Wr,rr)); spans.append(rr); print(s,"new invariant subspace dim",rr,flush=True)
            if sum(x for _,x in spaces)>=d: break
        tot=rank([r for Wr,_ in spaces for r in Wr])
        print(s,"subspace dims",spans,"rank of sum",tot,"d",d,flush=True)
        sec={"eps":eps,"dim":d,"n_simple_T":len(simple),"krylov_ranks_modl":spans,"comm_ub":comm_ub,"rank_sum":tot,
             "irreducible_exact":any(x==d for x in spans if isinstance(x,int))}
        res["sectors"].append(sec); print(s,sec,flush=True)
    json.dump(res,open(f"split_modl_{s}.json","w"),indent=1,default=str)
