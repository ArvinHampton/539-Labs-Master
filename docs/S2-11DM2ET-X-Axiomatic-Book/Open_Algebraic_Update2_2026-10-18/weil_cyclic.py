# Exact (mod ell) structure of even/odd parts of the Weil rep of Z/M, Q(x)=u x^2/M (M odd), both square classes of u.
# Commutant via T-eigenblock unknowns + random linear functionals (nullity = upper bound), basis then verified exactly.
# Char-0 conclusion: commutant_C <= commutant_Fl ; if an explicit invariant decomposition into that many pieces exists, equality.
import sys, json, random, sympy, flint
def build(M,u,sign):
    k=1
    while not sympy.isprime(k*M+1): k+=1
    ell=k*M+1; z=pow(sympy.primitive_root(ell),(ell-1)//M,ell); zt=[pow(z,a,ell) for a in range(M)]
    reps=[x for x in range(M) if x<=(-x)%M and (sign==1 or x!=(-x)%M)]
    d=len(reps)
    # S on basis f_x = e_x + sign e_{-x}: (S f_y)_x = z^{-2uxy}+sign z^{2uxy}; coefficient on f_x (x rep) = value at x
    S=flint.nmod_mat(d,d,[(zt[(-2*u*x*y)%M]+sign*zt[(2*u*x*y)%M])%ell for x in reps for y in reps],ell)
    if sign==1:   # f_0 = 2 e_0: coefficient on f_0 is value/2
        inv2=pow(2,-1,ell)
        for j in range(d): S[0,j]=int(S[0,j])*inv2%ell
    tv=[(u*x*x)%M for x in reps]
    return S,tv,d,ell,zt,reps
def analyse(M,u,sign,seed=1):
    S,tv,d,ell,zt,reps=build(M,u,sign)
    blocks={}
    for i,t in enumerate(tv): blocks.setdefault(t,[]).append(i)
    unk=[(i,j) for b in blocks.values() for i in b for j in b]; nU=len(unk)
    random.seed(seed); rows=[]
    for _ in range(nU+30):
        uu=flint.nmod_mat(1,d,[random.randrange(ell) for _ in range(d)],ell); ww=flint.nmod_mat(d,1,[random.randrange(ell) for _ in range(d)],ell)
        a=uu*S; b=S*ww
        av=[int(a[0,i]) for i in range(d)]; uv=[int(uu[0,i]) for i in range(d)]; bv=[int(b[i,0]) for i in range(d)]; wv=[int(ww[i,0]) for i in range(d)]
        rows.append([(av[i]*wv[j]-uv[i]*bv[j])%ell for i,j in unk])
    NS,c=flint.nmod_mat(rows,ell).nullspace()
    ok=True
    for col in range(c):
        X=flint.nmod_mat(d,d,[0]*(d*d),ell)
        for k_,(i,j) in enumerate(unk): X[i,j]=NS[k_,col]
        ok&= (S*X==X*S)
    # invariant vectors (normalised): S_true = S/(sqrt M * gauss phase) ; use T-fixed & S-eigen test on delta_{pZ}-type vectors: T fixed => u x^2 ≡0 mod M
    tfix=blocks.get(0,[])
    return {"M":M,"u":u,"part":"even" if sign==1 else "odd","dim":d,"commutant":c,"verified":bool(ok),"T_fixed_dim":len(tfix)}
out=[]
for M in map(int,sys.argv[1].split(',')):
    p=list(sympy.factorint(M))[0]
    nonres=next(a for a in range(2,M) if sympy.legendre_symbol(a,p)==-1)
    for u in (1,nonres):
        for sg in (1,-1):
            r=analyse(M,u,sg); print(r,flush=True); out.append(r)
json.dump(out,open(f"weil_cyclic_{sys.argv[1].replace(',','_')}.json","w"),indent=1)
