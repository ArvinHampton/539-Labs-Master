# Local-derived. O4: which alpha make T = sum_k alpha_k R_{p_k} (p_k in K90) preserve the LD-1 form B?
import numpy as np, itertools, math
from scipy.optimize import least_squares
A = [g for g in range(1,140) if math.gcd(g,140)==1]; idx = {g:i for i,g in enumerate(A)}; n = len(A)
K90 = [3,11,37,41,47,53,61,71,79,83,89]
assert all(math.gcd(p,140)==1 for p in K90)
def R(c):
    M = np.zeros((n,n))
    for g in A: M[idx[(c*g)%140], idx[g]] = 1
    return M
B = np.zeros((n,n))
for g in A: B[idx[g], idx[(-g)%140]] = 1
print("B symmetric:", np.array_equal(B,B.T), " det:", round(np.linalg.det(B)), " K90 distinct mod 140:", len(set(K90))==11)
chi140 = lambda g: int(round(((140/ g) if False else 0))) # placeholder (not used)
# C1: single-prime alpha
print("C1 R_p^T B R_p == B for all p in K90:", all(np.array_equal(R(p).T@B@R(p), B) for p in K90))
# identity B(Tx,Ty) = B(t t* x, y) for random real alpha
rng = np.random.default_rng(1)
al = rng.normal(size=11)
T = sum(a*R(p) for a,p in zip(al,K90)); Tstar = sum(a*R(pow(p,-1,140)) for a,p in zip(al,K90))
print("identity T^T B T == B (T T*)  [B(Tx,Ty)=B(TT* x,y)]: max err", np.abs(T.T@B@T - B@(T@Tstar)).max())
# C3: uniform alpha = 1
U = sum(R(p) for p in K90); G = U.T@B@U
print("C3 uniform: U^T B U == B ?", np.array_equal(G,B), "; == c*B for some c ?", np.allclose(G, G[idx[1],idx[139]]*B), "; (U^T B U)[1,-1] =", G[idx[1],idx[139]], " = sum alpha^2 = 11")
print("C3 uniform: rank U =", np.linalg.matrix_rank(U))
# collision structure of quotients p_k p_l^{-1}
coll = {}
for (k,pk),(l,pl) in itertools.permutations(list(enumerate(K90)),2):
    coll.setdefault((pk*pow(pl,-1,140))%140, []).append((k,l))
mult = sorted(len(v) for v in coll.values())
print("distinct quotients g=p_k/p_l (k!=l):", len(coll), " pair-multiplicities histogram:", {m: mult.count(m) for m in set(mult)})
# numerical search for real unitary t supported on K90: t t* = 1
def res(a):
    r = [sum(x*x for x in a)-1]
    for g,pairs in coll.items(): r.append(sum(a[k]*a[l] for k,l in pairs))
    return r
found = []
for trial in range(400):
    s = least_squares(res, rng.normal(size=11), xtol=1e-15, ftol=1e-15, gtol=1e-15)
    if np.linalg.norm(s.fun) < 1e-10:
        nz = int(np.sum(np.abs(s.x) > 1e-6)); found.append(nz)
print("random-start solutions found:", len(found), " support sizes:", {m: found.count(m) for m in set(found)})
# exact: if some quotient g arises from exactly one unordered pair {k,l}, then alpha_k alpha_l = 0
single = set()
for g,pairs in coll.items():
    un = {tuple(sorted(p)) for p in pairs}
    if len(un)==1: single |= un
print("unordered pairs {k,l} forced alpha_k*alpha_l=0 by a unique quotient:", len(single), "of", 55)
