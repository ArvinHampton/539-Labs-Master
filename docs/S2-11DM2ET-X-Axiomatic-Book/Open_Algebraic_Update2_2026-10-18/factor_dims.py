# Exact (mod ell) factor check for s=121: Weil reps of Z/M, M in {121, 7, 17}, form Q(x)=u x^2/M.
# S ~ e(-2u xy/M) (scalar dropped), T = diag e(u x^2/M). Even/odd parts under x->-x; SL2-invariant dim; commutant dims.
import json, sympy, flint
def weil(M,u):
    K=M*(1 if M%2 else 2); k=1
    while not sympy.isprime(k*M+1): k+=1
    ell=k*M+1; z=pow(sympy.primitive_root(ell),(ell-1)//M,ell)
    S=flint.nmod_mat(M,M,[pow(z,(-2*u*x*y)%M,ell) for x in range(M) for y in range(M)],ell)
    T=flint.nmod_mat(M,M,[pow(z,(u*x*x)%M,ell) if x==y else 0 for x in range(M) for y in range(M)],ell)
    return S,T,ell
def restrict(S,T,ell,M,sign):
    # basis e_x + sign e_{-x}
    reps=[x for x in range(M) if x<=(-x)%M]
    cols=[]
    for x in reps:
        v=[0]*M; v[x]+=1; v[(-x)%M]=(v[(-x)%M]+sign)%ell
        if any(v): cols.append(v)
    E=flint.nmod_mat(cols,ell).transpose(); d=E.ncols()
    piv=[x for x in reps][:d] if sign==1 else [x for x in reps if x!=(-x)%M]
    Ep=flint.nmod_mat([[int(E[i,j]) for j in range(d)] for i in piv],ell).inv()
    def r(A):
        AE=A*E; return Ep*flint.nmod_mat([[int(AE[i,j]) for j in range(d)] for i in piv],ell)
    return r(S),r(T),d
def stats(Sd,Td,d,ell):
    I=flint.nmod_mat(d,d,[int(i==j) for i in range(d) for j in range(d)],ell)
    st=flint.nmod_mat(2*d,d,[int(X[i,j]) for X in (Sd-I,Td-I) for i in range(d) for j in range(d)],ell)
    inv=st.nullspace()[1]
    rows=[]
    for X in (Sd,Td):
        for i in range(d):
            for j in range(d):
                r=[0]*(d*d)
                for k in range(d):
                    r[i*d+k]=(r[i*d+k]+int(X[k,j]))%ell; r[k*d+j]=(r[k*d+j]-int(X[i,k]))%ell
                rows.append(r)
    comm=flint.nmod_mat(rows,ell).nullspace()[1]
    return inv,comm
out={}
for M in (121,7,17):
    for u in (1,int(sympy.ntheory.residue_ntheory.nthroot_mod(1,1,M)) if False else 1, ):
        pass
    for u in sorted({1, next(a for a in range(2,M) if sympy.legendre_symbol(a, sympy.factorint(M).__iter__().__next__())==-1)}):
        S,T,ell=weil(M,u)
        for sign in (1,-1):
            Sd,Td,d=restrict(S,T,ell,M,sign)
            if M==121 and sign==1: inv,comm=stats(Sd,Td,d,ell)
            else: inv,comm=stats(Sd,Td,d,ell)
            out[f"M={M},u={u},{'even' if sign==1 else 'odd'}"]={"dim":d,"SL2_invariants":inv,"commutant":comm}
            print(M,u,sign,d,inv,comm,flush=True)
json.dump(out,open("factor_dims_121.json","w"),indent=1)
