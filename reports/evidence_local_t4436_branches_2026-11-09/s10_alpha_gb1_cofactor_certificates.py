# Local-derived (PP fix A1, optional). Cofactor (Nullstellensatz) certificates for the s4c jobs with GB = [1]:
# find polynomials c_i over Q with  sum_i c_i g_i = 1, where g_i are the job's equations (after the linear real-character substitution) and,
# if needed, the saturation generator z*prod(alpha) - 1. Any such identity proves the system has no solution with all alpha_k != 0
# (over C, hence over R), independently of sympy's Buchberger. Search: degree bound D for every c_i (D = 0,1,2,3,4), equations-only first,
# then with the saturation generator. The cofactors are found by exact rational linear algebra (python-flint fmpq_mat), and every
# identity is re-verified by exact sympy expansion. Certificates are written to s10_alpha_gb1_cofactor_certificates.txt (new file).
import sys, itertools, time, sympy as sp, flint, importlib.util
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location("s4c","s4c_alpha_support_sign_split.py"); s4c=importlib.util.module_from_spec(spec); spec.loader.exec_module(s4c)
from itertools import combinations_with_replacement as cwr
K90=s4c.K90; inv=s4c.inv; kron=s4c.kron; Dind=s4c.Dind
OUT='s10_alpha_gb1_cofactor_certificates.txt'
import os; assert not os.path.exists(OUT)
surv=[T for r in range(2,12) for T in itertools.combinations(K90,r) if all(len(c)!=1 for c in s4c.monomial_eqs(T).values())]
def system(T,s):
    X=[sp.Symbol(f'a{p}') for p in T]; z=sp.Symbol('z')
    Ml=sp.Matrix([[kron(d,p) for p in T] for d in Dind])
    sol,params=Ml.gauss_jordan_solve(sp.Matrix(s)); y=list(params); sub=dict(zip(X,list(sol)))
    E={}
    for i,a in enumerate(T):
        for j,b in enumerate(T):
            g=(a*inv(b))%140; E[g]=E.get(g,0)+X[i]*X[j]
    eqs=sorted([e for e in {sp.expand((E[1]-1).subs(sub))}|{sp.expand(v.subs(sub)) for g,v in E.items() if g!=1} if e!=0],key=sp.default_sort_key)
    prod=sp.Integer(1)
    for x in X: prod*=sub[x]
    return eqs, sp.expand(prod), y, z
def monos(vs,D):
    out=[sp.Integer(1)]
    for d in range(1,D+1):
        for c in cwr(vs,d): out.append(sp.Mul(*c))
    return out
def certify(gens,vs,D):
    cols=[]; labels=[]
    for i,g in enumerate(gens):
        for m in monos(vs,D):
            cols.append(sp.Poly(sp.expand(m*g),*vs).as_dict()); labels.append((i,m))
    one=tuple([0]*len(vs))
    keys=sorted({k for c in cols for k in c}|{one}); idx={k:j for j,k in enumerate(keys)}
    A=flint.fmpq_mat(len(keys),len(cols)+1)
    for j,c in enumerate(cols):
        for k,v in c.items():
            nu,de=sp.fraction(sp.Rational(v)); A[idx[k],j]=flint.fmpq(int(nu),int(de))
    A[idx[one],len(cols)]=1
    R=A.rref()[0]; r=A.rref()[1]
    # inconsistent column = pivot in last column -> no certificate at this D
    piv=[]; row=0
    for j in range(len(cols)+1):
        if row<len(keys) and R[row,j]!=0: piv.append(j); row+=1
    if len(cols) in piv: return None
    x=[0]*len(cols)
    for i,j in enumerate(piv): x[j]=sp.Rational(int(R[i,len(cols)].p),int(R[i,len(cols)].q))
    c=[sp.Integer(0)]*len(gens)
    for (i,m),xv in zip(labels,x):
        if xv: c[i]+=xv*m
    assert sp.expand(sum(ci*g for ci,g in zip(c,gens)))==1
    return c
t0=time.time(); done=0; cert=0; fails=[]
fh=open(OUT,'x')
for T in surv:
    for s in itertools.product((1,-1),repeat=4):
        try: eqs,prod,y,z=system(T,s)
        except ValueError: continue
        if not y or prod==0: continue
        G=sp.groebner(eqs+[z*prod-1],*([z]+y),order='lex')
        if G.exprs!=[1]: continue
        done+=1; got=None
        for D in range(0,5):
            got=certify(eqs,y,D)
            if got is not None: kind=f'equations only, D={D}'; gens=eqs; break
        if got is None:
            for D in range(0,4):
                got=certify(eqs+[z*prod-1],[z]+y,D)
                if got is not None: kind=f'with saturation, D={D}'; gens=eqs+[z*prod-1]; break
        if got is None: fails.append((T,s)); print('NO CERT (D bound)',T,s,flush=True); continue
        cert+=1
        fh.write(f'JOB support={T} sign={s} vars={y} ({kind}); verified sum c_i g_i == 1 by sympy.expand\n')
        for ci,g in zip(got,gens):
            if ci!=0: fh.write(f'  c = {ci}\n  g = {g}\n')
        fh.flush()
        if done%25==0: print(f'{done} GB=[1] jobs processed, {cert} certified, {time.time()-t0:.0f}s',flush=True)
fh.close()
print(f'GB=[1] jobs: {done}; certified: {cert}; not certified within the degree bounds: {len(fails)} {fails}')
