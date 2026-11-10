# Local-derived (t4436, branch alpha-3). SUPERSEDES s4b_alpha_classification_realchar.py (kept on disk; its 7-variable sympy Groebner
# step stalled and was killed at ~22:00 CST; its log holds only the real-character matrix, rank 4).
# Exact classification of real alpha (supported on K90) with t t* = [1] in R[(Z/140)^x]  <=>  R_t preserves B (alpha lemma).
# Step 1 (sieve, exact): a support T survives only if no g != 1 has exactly one unordered monomial alpha_k alpha_l in its equation.
# Step 2 (exact): for each surviving T and each sign vector s in {+-1}^4 for the 4 independent real characters
#   d in {1,-4,5,-7} (the rows d in {-20,28,-35,140} are the negatives of these on K90, since chi_140(p) = -1 for all p in K90),
#   impose sum_{k in T} alpha_k chi_d(p_k) = s_d (necessary: chi_d(t)^2 = chi_d(t t*) = 1), parametrise, and compute a lex Groebner basis
#   of the full system plus the saturation z*prod_{k in T} alpha_k - 1 (all alpha_k != 0 on T). Each job has a time limit;
#   jobs that time out are reported as UNDECIDED (not as 'no solution').
import itertools, sympy as sp, sys, multiprocessing as mp, time
from collections import Counter
from math import gcd
K90=[3,11,37,41,47,53,61,71,79,83,89]; inv=lambda x: pow(x,-1,140)
def kron(d,n): return int(sp.jacobi_symbol(d % n, n)) if n>1 else 1
Dind=[1,-4,5,-7]
for p in K90: assert kron(140,p)==-1
def monomial_eqs(T):
    E={}
    for a in T:
        for b in T:
            if a!=b:
                g=(a*inv(b))%140; E.setdefault(g,Counter())[tuple(sorted((a,b)))]+=1
    return E
def job(args):
    T,s=args
    X=[sp.Symbol(f'a{p}') for p in T]; z=sp.Symbol('z')
    Ml=sp.Matrix([[kron(d,p) for p in T] for d in Dind])
    try: sol,params=Ml.gauss_jordan_solve(sp.Matrix(s))
    except ValueError: return (T,s,'linear-inconsistent',[])
    y=list(params); sub=dict(zip(X,list(sol)))
    E={}
    for i,a in enumerate(T):
        for j,b in enumerate(T):
            g=(a*inv(b))%140; E[g]=E.get(g,0)+X[i]*X[j]
    eqs={sp.expand((E[1]-1).subs(sub))}|{sp.expand(v.subs(sub)) for g,v in E.items() if g!=1}
    eqs={e for e in eqs if e!=0}
    prod=sp.Integer(1)
    for x in X: prod*=sub[x]
    prod=sp.expand(prod)
    if not y:
        ok=(not eqs) and prod!=0
        return (T,s,'solved',[tuple(sol)] if ok else [])
    if prod==0: return (T,s,'forced-zero',[])
    G=sp.groebner(list(eqs)+[z*prod-1],*([z]+y),order='lex')
    if G.exprs==[1]: return (T,s,'GB=[1]',[])
    ge=[g for g in G.exprs if not g.has(z)]
    out=[]
    for r in sp.solve(ge,y,dict=True):
        if len(r)<len(y): return (T,s,'POSITIVE-DIM '+str(ge),[])
        v=tuple(sp.nsimplify(sp.simplify(c.subs(r))) for c in sol)
        if all(x.is_real for x in v) and all(x!=0 for x in v): out.append(v)
    return (T,s,'solved',out)
def run(args,q):
    try: q.put(job(args))
    except Exception as e: q.put((args[0],args[1],'ERROR '+repr(e),[]))
if __name__=='__main__':
    TL=int(sys.argv[1]) if len(sys.argv)>1 else 600
    surv=[]
    for r in range(2,12):
        for T in itertools.combinations(K90,r):
            if all(len(c)!=1 for c in monomial_eqs(T).values()): surv.append(T)
    print(f"Step 1: nontrivial (|T|>=2) supports surviving the one-monomial sieve: {len(surv)}; sizes {dict(sorted(Counter(len(T) for T in surv).items()))}", flush=True)
    jobs=[(T,s) for T in surv for s in itertools.product((1,-1),repeat=4)]
    print(f"Step 2: {len(jobs)} (support, sign) jobs, time limit {TL}s each, 7 workers", flush=True)
    results=[]; running=[]; pending=list(jobs)
    while pending or running:
        while pending and len(running)<7:
            a=pending.pop(0); q=mp.Queue(); pr=mp.Process(target=run,args=(a,q)); pr.start(); running.append((a,pr,q,time.time()))
        time.sleep(0.2)
        for item in list(running):
            a,pr,q,t0=item
            if not q.empty():
                results.append(q.get()); pr.join(); running.remove(item)
            elif time.time()-t0>TL:
                pr.terminate(); pr.join(); results.append((a[0],a[1],'UNDECIDED (timeout)',[])); running.remove(item)
    st=Counter(r[2].split(' ')[0] for r in results); print("job outcomes:", dict(st), flush=True)
    und=sorted({r[0] for r in results if r[2].startswith('UNDECIDED') or r[2].startswith('ERROR') or r[2].startswith('POSITIVE')})
    for r in results:
        if not (r[2] in ('GB=[1]','linear-inconsistent','forced-zero') or (r[2]=='solved' and not r[3])): print("  ",r[0],r[1],r[2],[{T:str(x) for T,x in zip(r[0],v)} for v in r[3]])
    sols=sorted({(r[0],v) for r in results for v in r[3]})
    print("multi-prime real solutions found:", len(sols), "; supports:", dict(Counter(T for T,_ in sols)))
    print("supports with an undecided/positive-dim/error job:", und)
    print("single-prime solutions: 22 (alpha = +-e_k, k in K90), exact by inspection")
