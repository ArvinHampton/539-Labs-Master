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
    for eps in itertools.product((1,-1),repeat=len(ps)):
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
        # float T_E eigenvalues for discrete log: use the complex sector basis
        A=np.vstack([to_complex(MP['neg'],K)-np.eye(N),to_complex(MP['gamma'],K)-np.eye(N)]+[to_complex(MP[p],K)-e*np.eye(N) for p,e in zip(ps,eps)])
        _,sv,vh=np.linalg.svd(A); Ec=vh[np.sum(sv>1e-8):].conj().T
        w=np.linalg.eigvals(Ec.conj().T@Tc@Ec)
        ang=[int(round((np.angle(z)/(2*np.pi))*Kbig))%Kbig for z in w]
        from collections import Counter
        cnt=Counter(ang); simple=[a for a,c in cnt.items() if c==1]
        spans=[]
        for a in simple[:6]:
            lam=pow(zeta,a,ell)
            Y,ny=(Td-Td.__class__([[lam*int(i==j) for j in range(d)] for i in range(d)],ell)).nullspace()
            if ny!=1: spans.append(("eigdim_modl",ny)); continue
            vec=[int(Y[i,0]) for i in range(d)]
            B=flint.nmod_mat([vec],ell); r0=1
            while True:
                SB=B*Sd.transpose(); TB=B*Td.transpose()
                rows=[[int(M_[i,j]) for j in range(d)] for M_ in (B,SB,TB) for i in range(M_.nrows())]
                Rm,rr=flint.nmod_mat(rows,ell).rref()
                B=flint.nmod_mat([[int(Rm[i,j]) for j in range(d)] for i in range(rr)],ell)
                if rr==r0: break
                r0=rr
            spans.append(r0)
        sec={"eps":eps,"dim":d,"n_simple_T":len(simple),"krylov_ranks_modl":spans,
             "irreducible_exact":any(x==d for x in spans if isinstance(x,int))}
        res["sectors"].append(sec); print(s,sec,flush=True)
    json.dump(res,open(f"irr_modl_{s}.json","w"),indent=1,default=str)
