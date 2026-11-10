# Local-derived (t4436, branch alpha-3). Full exact classification of real alpha in R^{11} supported on
# K90 = {3,11,37,41,47,53,61,71,79,83,89} with t t* = 1 in R[A], A = (Z/140)^x, t = sum_k alpha_k [p_k], t* = sum alpha_k [p_k^-1].
# (By the alpha lemma of bfa5da3b / PP 320c8c7e Sec.1(c): T = R_t preserves B iff t t* = 1.)
# Method (exact, no floating point):
#  Step 1. For each support T (alpha_k != 0 exactly for k in T), the equations are: coefficient of [1] = sum alpha_k^2 = 1, and for
#          g != 1: sum over ordered pairs (k,l) in T^2, k != l, p_k p_l^-1 = g, of alpha_k alpha_l = 0. Grouping ordered pairs into
#          unordered monomials alpha_k alpha_l: if some g != 1 has exactly ONE monomial (with positive integer coefficient), that
#          monomial must vanish, contradicting alpha_k alpha_l != 0. Such supports carry no solution (combinatorial sieve).
#  Step 2. For each surviving support, a lex Groebner basis over Q of the system plus the saturation equation z*prod(alpha_k) - 1
#          (sympy). GB = [1]  <=>  no solution with all alpha_k != 0 over C (hence none over R). Otherwise the GB is printed and
#          its real solutions are enumerated exactly.
import itertools, sympy as sp
from collections import Counter
K90=[3,11,37,41,47,53,61,71,79,83,89]; inv=lambda x: pow(x,-1,140)
assert len({p%140 for p in K90})==11
def monomial_eqs(T):
    E={}
    for a in T:
        for b in T:
            if a!=b:
                g=(a*inv(b))%140; E.setdefault(g,Counter())[tuple(sorted((a,b)))]+=1
    return E
surv=[]; killed=0
for r in range(1,12):
    for T in itertools.combinations(K90,r):
        if all(len(c)!=1 for c in monomial_eqs(T).values()): surv.append(T)
        else: killed+=1
print(f"Step 1: {2**11-1} nonempty supports; killed by the one-monomial sieve: {killed}; surviving: {len(surv)} (sizes {dict(sorted(Counter(len(T) for T in surv).items()))})")
allsols=[]
for T in surv:
    if len(T)==1:
        allsols += [ {T[0]:s} for s in (1,-1) ]; continue
    X={p:sp.Symbol(f'a{p}') for p in T}; z=sp.Symbol('z')
    E={}
    for a in T:
        for b in T:
            g=(a*inv(b))%140; E[g]=E.get(g,0)+X[a]*X[b]
    polys={sp.expand(E[1]-1)}|{sp.expand(v) for g,v in E.items() if g!=1}
    polys={p for p in polys if p!=0}
    prod=sp.Integer(1)
    for p in T: prod*=X[p]
    G=sp.groebner(list(polys)+[z*prod-1],*([z]+[X[p] for p in T]),order='lex')
    ge=[g for g in G.exprs if not g.has(z)]
    if G.exprs==[1]:
        print(f"Step 2: support {T}: GB = [1] -> no solution"); continue
    sols=sp.solve(ge,[X[p] for p in T],dict=True)
    real=[s for s in sols if all(v.is_real for v in s.values()) and len(s)==len(T)]
    print(f"Step 2: support {T}: GB (z eliminated) = {ge}; complex solutions {len(sols)}, real {len(real)}")
    for s in real: allsols.append({p:s[X[p]] for p in T})
print("\nRESULT: total real solutions =", len(allsols))
print(" single-prime (alpha-1 up to sign):", sum(1 for s in allsols if len(s)==1))
by=Counter(tuple(sorted(s)) for s in allsols if len(s)>1)
print(" multi-prime solutions by support:", dict(by))
print(" distinct |alpha| values among multi-prime solutions:", sorted({abs(v) for s in allsols if len(s)>1 for v in s.values()}))
# independent exact re-verification of every solution: t t* = [1] in Q[A]
def ttstar(t):
    pr={}
    for p,a in t.items():
        for q,b in t.items():
            g=(p*inv(q))%140; pr[g]=pr.get(g,0)+a*b
    return {g:sp.nsimplify(v) for g,v in pr.items() if sp.simplify(v)!=0}
print(" re-verification t t* = 1 for all:", all(ttstar(s)=={1:1} for s in allsols))
# parity: J R_p J = -R_p for each p (Addendum L, cited) is linear, so J T J = -T for every alpha (linear combination): no check needed.
# Group structure: multi-prime solutions as (1/2)(sum of 4 group elements with signs); record whether the support is a coset-translate p0*H
for S in sorted(by):
    p0=S[0]; H=sorted((q*inv(p0))%140 for q in S)
    print(f"  support {S}: p0^-1*S = {H}")
