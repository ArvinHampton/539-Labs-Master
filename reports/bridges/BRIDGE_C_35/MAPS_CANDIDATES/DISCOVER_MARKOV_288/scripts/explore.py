# DISCOVER_MARKOV_288 exploration (pre-PREREG). Exact lifted chain of T3 on Z/M; no seeds used.
import sympy as sp, json, sys
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
def well_defined(M):  # T3(u) mod M depends only on u mod 3M
    return all(len({T3(r+3*M*t)%M for t in range(6)})==1 for r in range(3*M))
def not_det_from_M(M):  # does u mod M determine T3(u) mod M? (count branching)
    return max(len({T3(r+M*t)%M for t in range(3)}) for r in range(M))
def law(M):
    S=[r for r in range(M) if r%4!=0]; idx={r:i for i,r in enumerate(S)}; n=len(S)
    P=sp.zeros(n,n)
    for r in range(3*M):
        a=r%M
        if a%4==0: continue
        b=T3(r)%M
        assert b%4!=0  # Lemma V closure
        P[idx[a],idx[b]]+=sp.Rational(1,3)
    A=(P.T-sp.eye(n)).row_insert(0,sp.ones(1,n)); rhs=sp.zeros(n+1,1); rhs[0]=1
    pi=A.solve_least_squares(rhs) if False else None
    ns=(P.T-sp.eye(n)).nullspace(); assert len(ns)==1, len(ns)  # unique stationary => irreducible closed class
    v=ns[0]; v=v/sum(v)
    hit=[sp.Integer(0)]*8
    for r in S:
        if r%9==3: hit[((r-21)//9)%8]+=v[idx[r]]
    h=sum(hit); return h,[sp.nsimplify(x/h) for x in hit]
out={}
for M in [72,144,216,288]:
    if M%72: continue
    h,f=law(M); out[M]=dict(wd=well_defined(M),branch=not_det_from_M(M),hit=str(h),fib=[str(x) for x in f])
    print(M,out[M],flush=True)
json.dump(out,open('data/explore.json','w'),indent=1)
