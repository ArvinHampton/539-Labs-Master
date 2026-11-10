# MR2 GAP-SK-p3-1c-MC: machine check of socle(Ind_B^G psi) for GL2(Fp), p=3,5,7. Pure python, over Fp.
import itertools, sys
def rref(rows,p):
    M=[r[:] for r in rows]; piv=[]; r=0
    n=len(M[0]) if M else 0
    for c in range(n):
        k=next((i for i in range(r,len(M)) if M[i][c]%p),None)
        if k is None: continue
        M[r],M[k]=M[k],M[r]; inv=pow(M[r][c],p-2,p); M[r]=[x*inv%p for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]%p:
                f=M[i][c]; M[i]=[(x-f*y)%p for x,y in zip(M[i],M[r])]
        piv.append(c); r+=1
    return M[:r],piv
def rank(rows,p): return len(rref(rows,p)[0]) if rows else 0
def kernel(A,p):  # A: list of rows (m x n); return basis of {v: A v=0}
    n=len(A[0]); R,piv=rref(A,p); free=[c for c in range(n) if c not in piv]; B=[]
    for f in free:
        v=[0]*n; v[f]=1
        for i,c in enumerate(piv): v[c]=(-R[i][f])%p
        B.append(v)
    return B
def mv(M,v,p): return [sum(a*b for a,b in zip(row,v))%p for row in M]
def span_closure(vecs,gens,p):
    basis,_=rref(vecs,p); basis=[b for b in basis]
    changed=True
    while changed:
        changed=False
        for g in gens:
            for b in list(basis):
                w=mv(g,b,p)
                if rank(basis+[w],p)>len(basis): basis=rref(basis+[w],p)[0]; changed=True
    return basis
def mul(A,B,p): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%p for j in range(2)) for i in range(2))
def gen_root(p): return next(g for g in range(2,p+1) if len({pow(g,k,p) for k in range(p-1)})==p-1) if p>2 else 1
def run(p):
    out=[]; ok=True
    g0=gen_root(p); log={pow(g0,k,p):k for k in range(p-1)}; q=p-1
    G=[((a,b),(c,d)) for a,b,c,d in itertools.product(range(p),repeat=4) if (a*d-b*c)%p]
    assert len(G)==(p*p-1)*(p*p-p)
    # B\G <-> P^1: coset Bg determined by bottom row of g up to scalar
    def pt(g):
        c,d=g[1]
        return (0,1) if c==0 else (1,d*pow(c,p-2,p)%p)
    pts=sorted({pt(g) for g in G}); idx={x:i for i,x in enumerate(pts)}; N=len(pts); assert N==p+1
    rep={x:next(g for g in G if pt(g)==x) for x in pts}
    def borel_part(g):  # g = b * rep[pt(g)] ; return b
        r=rep[pt(g)]; (a,b),(c,d)=r; det=(a*d-b*c)%p; di=pow(det,p-2,p)
        rinv=((d*di%p,(-b)*di%p),((-c)*di%p,a*di%p)); bb=mul(g,rinv,p); assert bb[1][0]==0; return bb
    u=((1,1),(0,1)); w=((0,1),(1,0)); gens_G=[u,w,((g0,0),(0,1)),((1,0),(0,g0))]
    def ind_matrix(g,i,j):  # (g.f)(x)=f(xg); f(b x)=psi(b)f(x); basis delta-like f_y with f_y(rep[y])=1
        M=[[0]*N for _ in range(N)]
        for x in pts:   # (g f)(rep[x]) = f(rep[x] g) = psi(b) f(rep[y])
            h=mul(rep[x],g,p); y=pt(h); b=borel_part(h)
            M[idx[x]][idx[y]]=pow(g0,(i*log[b[0][0]]+j*log[b[1][1]])%q,p)
        return M
    def sym_matrix(g,s,a):  # Sym^s (X,Y)->(aX+cY,bX+dY) tensor det^a
        (A,Bc),(C,D)=g; det=(A*D-Bc*C)%p
        M=[[0]*(s+1) for _ in range(s+1)]
        for k in range(s+1):  # X^{s-k}Y^k
            poly=[1]
            for _ in range(s-k): poly=pmul(poly,[A,C],p)
            for _ in range(k): poly=pmul(poly,[Bc,D],p)
            for m,cf in enumerate(poly): M[m][k]=cf*pow(det,a,p)%p
        return M
    def Tweight_of(vec,mats_t):  # vec eigen for diag(g0,1), diag(1,g0): return exps (e1,e2)
        res=[]
        for M in mats_t:
            w_=mv(M,vec,p); k=next(t for t in range(len(vec)) if vec[t]); lam=w_[k]*pow(vec[k],p-2,p)%p
            assert all((w_[t]-lam*vec[t])%p==0 for t in range(len(vec))),"not T-eigen"
            res.append(log[lam])
        return tuple(res)
    t1=((g0,0),(0,1)); t2=((1,0),(0,g0))
    # Sym table: (s,a) -> (dim, U-fixed weight)
    symtab={}
    for s in range(p):
        for a in range(q):
            gm=[sym_matrix(g,s,a) for g in gens_G]
            Uf=kernel([[ (x-(r==c))%p for c,x in enumerate(row)] for r,row in enumerate(gm[0])],p)
            assert len(Uf)==1
            symtab[(s,a)]=(s+1,Tweight_of(Uf[0],[gm[2],gm[3]]))
    keys=list(symtab.values()); uniq=len(set(keys))==len(keys)
    out.append(f"p={p}: |G|={len(G)}, Sym table {len(symtab)} entries, (dim,U-weight) keys distinct: {uniq}"); ok&=uniq
    inv_tab={v:k for k,v in symtab.items()}
    hit=set()
    for i in range(q):
        for j in range(q):
            gm=[ind_matrix(g,i,j) for g in gens_G]
            Iu=[[ (x-(r==c))%p for c,x in enumerate(row)] for r,row in enumerate(gm[0])]
            UF=kernel(Iu,p); d_ok=len(UF)==2
            fB=[0]*N; fB[idx[(0,1)]]=1   # rep of (0,1) is in B: support B
            fw=[0]*N; fw[idx[(0,1)]]=0
            for x in pts:
                if x!=(0,1): fw[idx[x]]=1   # check below it is U-fixed (support BwU)
            ufB=rank(UF+[fB],p)==2; ufw=rank(UF+[fw],p)==2
            wB=Tweight_of(fB,gm[2:]); ww=Tweight_of(fw,gm[2:])
            Ms=lambda v: span_closure([v],gm,p)
            MB=Ms(fB); Mw=Ms(fw)
            line=f" psi=(t1^{i} t2^{j}) [exp base g0={g0}]: dimInd^U={len(UF)} fB,fw U-fixed={ufB},{ufw} wts fB={wB} fw={ww} dim<f_B>={len(MB)} dim<f_w>={len(Mw)}"
            good=d_ok and ufB and ufw and len(MB)==N
            if i!=j:
                # irreducible: Mw^U = <fw> only (fB not in Mw) => every submodule contains fw
                MwU=kernel([[ (x-(r==c))%p for c,x in enumerate(row)] for r,row in enumerate(gm[0])]+[],p)
                fB_in=rank(Mw+[fB],p)==len(Mw)
                # socle: any irreducible sub X has X^U containing fB or fw (distinct weights); fB generates Ind != X, so X contains fw => soc = <f_w> if irreducible
                irr=not fB_in and wB!=ww
                key=(len(Mw),ww); m=inv_tab.get(key)
                line+=f" | psi!=psi^w: fB in <f_w>={fB_in} => soc=<f_w> irreducible={irr}, matches Sym^s(x)det^a={m}"
                good&=irr and m is not None
                if m: hit.add(m)
            else:
                # det^i-line: f(rep[x]) = det(rep[x])^i (i.e. psi∘det-twisted constants); St = kernel of the functional f -> sum_x f(rep[x]) det(rep[x])^{-i}
                dt=lambda g:(g[0][0]*g[1][1]-g[0][1]*g[1][0])%p
                one=[pow(dt(rep[x]),i,p) for x in pts]; C=Ms(one)
                lin=[pow(dt(rep[x]),(q-i)%q,p) for x in pts]
                St=kernel([lin],p); St=rref(St,p)[0]
                stable=all(rank(St+[mv(g,v,p)],p)==len(St) for g in gm for v in St)
                direct=stable and rank(C+St,p)==N and len(C)+len(St)==N
                # St irreducible: St^U 1-dim and generates St
                StUdim=len(St)+len(UF)-rank(St+UF,p)  # dim(St ∩ Ind^U)
                # vector in St∩Ind^U: fw - p*fB... solve: a fB + b fw sum zero: a + p*b = a (since p=0) -> fB? use explicit search
                cand=[v for a_ in range(p) for b_ in range(p) for v in [[(a_*x+b_*y)%p for x,y in zip(UF[0],UF[1])]] if any(v) and rank(St+[v],p)==len(St)]
                genall=all(len(Ms(v))==len(St) for v in cand)
                irrSt=StUdim==1 and genall
                mC=inv_tab.get((len(C),Tweight_of(one,gm[2:]))); mS=inv_tab.get((len(St),Tweight_of(cand[0],gm[2:]))) if cand else None
                line+=f" | psi=psi^w: C dim {len(C)}, St dim {len(St)}, Ind=C+St direct={direct}, dim St^U={StUdim}, St irreducible={irrSt}, C~{mC}, St~{mS}"
                good&=direct and len(C)==1 and len(St)==p and irrSt and mC is not None and mS is not None
                if mC: hit.add(mC)
                if mS: hit.add(mS)
            out.append(line+(" OK" if good else " FAIL")); ok&=good
    allp=set(symtab); miss=allp-hit
    out.append(f"p={p}: (s,a) hit as socle constituent: {len(hit)}/{len(allp)}; missing={sorted(miss)}"); ok&=not miss
    return ok,out
def pmul(a,b,p):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%p
    return r
allok=True
for p in (3,5,7):
    ok,out=run(p); print("\n".join(out)); print(f"p={p}: {'OK' if ok else 'FAIL'}"); allok&=ok
print("ALL_OK" if allok else "FAIL")
