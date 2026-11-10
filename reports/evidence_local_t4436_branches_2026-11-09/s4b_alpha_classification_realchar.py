# Local-derived (t4436, branch alpha-3). SUPERSEDES s4_alpha_full_classification.py (kept on disk; that run used a support-by-support
# sympy Groebner basis, stalled on 8-10-prime supports and was killed at 21:50 CST with an empty log).
# Exact classification of ALL real alpha in R^{11} with T = R_t preserving B, t = sum_k alpha_k [p_k], p_k in K90, A = (Z/140)^x.
# alpha lemma (bfa5da3b, PP 320c8c7e Sec.1(c)): T preserves B iff t t* = [1] in R[A], t* = sum alpha_k [p_k^-1].
# Linearisation: for each of the 8 REAL characters chi of A (chi = kronecker(d,.), d in {1,-4,5,-7,-20,28,-35,140}),
#   chi(t t*) = chi(t)^2 = 1, so  sum_k alpha_k chi(p_k) = s_chi in {+1,-1}  (8 LINEAR equations).
# For each of the 2^8 sign vectors s: solve M alpha = s exactly over Q; general solution alpha = a0 + Nb*y; impose the full quadratic
# system (all 48 coefficients of t t* - [1]) on y and solve it exactly (sympy groebner/solve in dim(null) variables).
# This is complete: every real solution satisfies M alpha = s for its own s.
import itertools, sympy as sp
from math import gcd
from sympy.ntheory import jacobi_symbol
from collections import Counter
K90=[3,11,37,41,47,53,61,71,79,83,89]; inv=lambda x: pow(x,-1,140)
A=[g for g in range(1,140) if gcd(g,140)==1]; assert len(A)==48
D=[1,-4,5,-7,-20,28,-35,140]
def kron(d,n):  # Kronecker (d/n) for odd n>0 coprime to d, via the Jacobi symbol
    return jacobi_symbol(d % n, n) if n>1 else 1
for d in D:
    vals={g:kron(d,g) for g in A}
    assert all(vals[(x*y)%140]==vals[x]*vals[y] for x in A for y in A), d
    assert all(kron(d,g+140*k)==vals[g] for g in A for k in (1,2)), d
assert len({tuple(kron(d,g) for g in A) for d in D})==8
print("8 real characters of (Z/140)^x verified multiplicative, 140-periodic and distinct")
M=sp.Matrix([[kron(d,p) for p in K90] for d in D])
print("real-character matrix M (rows d =",D,", cols K90):"); print(M)
print("rank M =", M.rank())
def ttstar_coeffs(alpha):
    pr={g:0 for g in A}
    for i,p in enumerate(K90):
        for j,q in enumerate(K90):
            pr[(p*inv(q))%140]+=alpha[i]*alpha[j]
    pr[1]-=1
    return [sp.expand(v) for v in pr.values()]
sols=[]; consistent=0; posdim=[]
for s in itertools.product((1,-1),repeat=8):
    try:
        sol,params=M.gauss_jordan_solve(sp.Matrix(s))
    except ValueError:
        continue
    consistent+=1
    y=list(params)
    eqs=[e for e in ttstar_coeffs(list(sol)) if e!=0]
    if not y:
        if not eqs: sols.append(tuple(sol))
        continue
    G=sp.groebner(eqs,*y,order='lex')
    if G.exprs==[1]: continue
    for r in sp.solve(G.exprs,y,dict=True):
        if len(r)<len(y):
            posdim.append((s,G.exprs)); continue
        v=tuple(sp.nsimplify(sp.simplify(c.subs(r))) for c in sol)
        if all(x.is_real for x in v): sols.append(v)
print(f"sign vectors with a consistent linear system: {consistent} of 256; positive-dimensional components: {len(posdim)}")
for s,g in posdim: print("  POSDIM", s, g)
sols=sorted(set(sols))
print("TOTAL real solutions:", len(sols))
def supp(v): return tuple(K90[i] for i,x in enumerate(v) if x!=0)
print("by support size:", dict(sorted(Counter(len(supp(v)) for v in sols).items())))
print("multi-prime supports (count of sign patterns):", sorted(Counter(supp(v) for v in sols if len(supp(v))>1).items()))
print("distinct |alpha_k| values:", sorted({abs(x) for v in sols for x in v}))
ok=all(all(e==0 for e in ttstar_coeffs(list(v))) for v in sols); print("independent re-check t t* = [1] for every solution:", ok)
idx={g:i for i,g in enumerate(A)}
Bm=sp.zeros(48,48)
for g in A: Bm[idx[g],idx[(-g)%140]]=1
def Rmat(t):
    R=sp.zeros(48,48)
    for i,p in enumerate(K90):
        if t[i]==0: continue
        for g in A: R[idx[(p*g)%140],idx[g]]+=t[i]
    return R
for v in sols[:2]+sols[-2:]:
    R=Rmat(v); print("  exact R^T B R == B for", {K90[i]:str(x) for i,x in enumerate(v) if x!=0}, ":", R.T*Bm*R==Bm)
