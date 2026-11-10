# FROZEN before run (MR2, 2026-11-10). B1-c2' candidate E-S+-: delta(f) on vertical spin structures, f = P o r~, r in Isom(Bolza)\Aut+.
# Model (as in 8399be55 .py 2f0e1220, its [Z]/[D] sections): Weierstrass points W = (0, inf, 1, i, -1, -i); spin structures on Sigma
# (= square roots of K; roots of L = K or K^{-1} = TSigma have the same combinatorics) <-> odd subsets of W mod complement (16);
# H^1(Sigma;Z2) = J[2] <-> even subsets mod complement (16). Isometries act through their permutation of W (J acts trivially).
# Vertical spin structures of V_vert (V_vert + R = pi^*(L + R^3)) <-> spin structures of L + R^3 over Sigma <-> roots of L.
# f acts on L by dr (antilinear) and on R^3 by the constant reflection P, so on roots of L by theta -> r^* conj(theta),
# i.e. by the W-permutation of r.  delta(f; s) = f^*s - s in J[2].
import itertools, sympy as sp, numpy as np
W = ['0','inf','1','i','-1','-i']; B6 = frozenset(range(6))
def norm(T):
    T = frozenset(T); return min(T, B6-T, key=lambda s: (len(s), sorted(s)))
theta = sorted({norm(T) for k in (1,3,5) for T in itertools.combinations(range(6), k)}, key=lambda s:(len(s),sorted(s)))
J2 = sorted({norm(T) for k in (0,2,4,6) for T in itertools.combinations(range(6), k)}, key=lambda s:(len(s),sorted(s)))
assert len(theta) == 16 and len(J2) == 16
act = lambda p, T: norm({p[i] for i in T})
# --- [A] independent cross-check: quadratic refinements of the mod-2 intersection form on H1 = J2
#     q_T(S) = |S cap T| + |S|/2 mod 2 (S even, T odd); check well-defined, quadratic, distinct, Arf counts (6 odd / 10 even)
def q(T, S):
    S = min(S, B6-S, key=len)
    return (len(S & T) + len(S)//2) % 2
def ip(S, Sp): return len(S & Sp) % 2
ok_wd = all((len(S & T) + len(S)//2) % 2 == (len((B6-S) & T) + len(B6-S)//2) % 2 for T in theta for S in J2)
ok_quad = all(q(T, norm(S ^ Sp)) == (q(T,S) + q(T,Sp) + ip(S,Sp)) % 2 for T in theta for S in J2 for Sp in J2)
forms = {tuple(q(T,S) for S in J2) for T in theta}
# Arf: majority value of q over the 16 elements of H1
arf = [1 if sum(q(T,S) for S in J2) > 8 else 0 for T in theta]
print(f"[A] q_T well-defined: {ok_wd}; quadratic refinement of intersection form: {ok_quad}; 16 distinct forms: {len(forms)==16}; Arf=1 count: {sum(arf)} (single-point T: {sum(a for a,T in zip(arf,theta) if len(T)==1)}/6)")
# --- group: generators' W-permutations exactly as in 8399be55 log lines 66-69
GEN = {'g1': (0,1,3,4,5,2), 'g2': (2,4,1,3,0,5), 'c': (0,1,2,5,4,3)}   # images of (0,inf,1,i,-1,-i)
def comp(a,b): return tuple(a[b[i]] for i in range(6))   # a after b
idp = tuple(range(6))
def closure(gens):
    G = {idp}; frontier = [idp]
    while frontier:
        new = []
        for h in frontier:
            for g in gens:
                k = comp(g,h)
                if k not in G: G.add(k); new.append(k)
        frontier = new
    return G
Aplus = closure([GEN['g1'], GEN['g2']]); Full = closure(list(GEN.values()))
rev = sorted(Full - Aplus)
print(f"[G] |image of Aut+ on W| = {len(Aplus)} (expect 24 = Aut+/<J>), |image of Isom| = {len(Full)} (expect 48), orientation-reversing images: {len(rev)}")
# sign of permutation and order, cycle type
def cyc(p):
    seen=set(); out=[]
    for i in range(6):
        if i in seen: continue
        j=i; c=0
        while j not in seen: seen.add(j); j=p[j]; c+=1
        out.append(c)
    return tuple(sorted(out, reverse=True))
def order(p):
    k=1; h=p
    while h != idp: h=comp(p,h); k+=1
    return k
# conjugacy classes of orientation-reversing images within the full image group
classes = []
left = set(rev)
while left:
    p = min(left); cl = {comp(comp(g,p), tuple(sorted(range(6), key=lambda i: g[i]))) for g in Full}
    # inverse of g: g^{-1}[g[i]] = i
    cl = set()
    for g in Full:
        gi = [0]*6
        for i in range(6): gi[g[i]] = i
        cl.add(comp(comp(g,p), tuple(gi)))
    classes.append(sorted(cl)); left -= cl
print("[C] orientation-reversing classes (image in O_h acting on the 6 octahedron vertices W):")
summary = []
for cl in classes:
    p = cl[0]
    fixed = [s for s in theta if act(p,s) == s]
    deltas = {norm(act(p,s) ^ s) for s in theta}
    fixed_odd = sum(1 for s in fixed if len(s)==1); fixed_even = len(fixed) - fixed_odd
    # delta is affine: delta(s) for all s; fixed iff delta = 0
    print(f"  class size {len(cl):2d} | cycle type {cyc(p)} | order on W {order(p)} | rep perm {[W[i] for i in p]} | vertical spin structures fixed: {len(fixed)}/16 (odd {fixed_odd}, even {fixed_even}) | distinct delta(f;s) values: {len(deltas)}")
    summary.append((len(cl), cyc(p), len(fixed)))
    assert all(len(set(act(pp,s)==s for s in theta)) >= 1 for pp in cl)
    assert len({sum(1 for s in theta if act(pp,s)==s) for pp in cl}) == 1   # class function
print("[C] total orientation-reversing image elements:", sum(n for n,_,_ in summary), "; with >= 1 fixed vertical spin structure:", sum(n for n,_,k in summary if k>0), "; with none:", sum(n for n,_,k in summary if k==0))
cconj = GEN['c']
print(f"[K] r = complex conjugation c (real points exist: x=2, y^2=30>0 => c is a reflection with fixed ovals): fixed {sum(1 for s in theta if act(cconj,s)==s)}/16 ; fixed list {[sorted(W[i] for i in s) for s in theta if act(cconj,s)==s]}")
# --- [W2] w2(V_vert) = pi^* (c1(L) mod 2): deg L from the twist connection A = dx/y (a1 = 1, charge 1 on z1 = mu1 e^{i phi1})
x, y = sp.symbols('x y', real=True)
Ax, Ay = 1/y, 0
F_xy = sp.diff(Ay, x) - sp.diff(Ax, y)
print(f"[W2] dA = F_xy dx^dy with F_xy = {sp.simplify(F_xy)} = hyperbolic area density (curvature -1 metric (dx^2+dy^2)/y^2): {sp.simplify(F_xy - 1/y**2) == 0}")
area = (8-2)*sp.pi - 8*(sp.pi/4)        # Gauss-Bonnet for the regular hyperbolic octagon with angles pi/4 (Bolza fundamental domain)
degL = area/(2*sp.pi)
print(f"[W2] Area(Bolza) = (8-2)pi - 8(pi/4) = {area} ; |deg L| = Area/2pi = {degL} ; c1(L) mod 2 = {int(degL) % 2} -> w2(V_vert) = pi^* w2(L + R^3) = {int(degL)%2}; w1 = 0")
# --- [S] lift squared at a fixed point: f acts on T_p S^4 with two -1 eigenvalues (phi1-dir, phi2-dir) -> pi rotation in one plane
s0_, sx_, sy_, sz_ = np.eye(2), np.array([[0,1],[1,0]]), np.array([[0,-1j],[1j,0]]), np.diag([1,-1])
e = [np.kron(sx_,s0_), np.kron(sy_,s0_), np.kron(sz_,sx_), np.kron(sz_,sy_)]
for a in range(4):
    for b in range(4): assert np.allclose(e[a]@e[b]+e[b]@e[a], 2*(a==b)*np.eye(4))
chir = e[0]@e[1]@e[2]@e[3]
Pp, Pm = (np.eye(4)+chir)/2, (np.eye(4)-chir)/2
Lf = e[2]@e[3]         # lift of the reflection pair (flipped directions 3, 4 = phi1-dir, phi2-dir); determined up to sign
sq = Lf@Lf
print(f"[S] lift of f at a fixed point = e3 e4 (pi-rotation), lift^2 = {'-1' if np.allclose(sq,-np.eye(4)) else 'other'}; restricted to S+: {'-1' if np.allclose(Pp@sq@Pp, -Pp) else 'other'}, to S-: {'-1' if np.allclose(Pm@sq@Pm, -Pm) else 'other'}; preserves S+ and S- (commutes with chirality): {np.allclose(Lf@chir, chir@Lf)}")
# E8 image of -1 in SU(2) (index-1 embedding SU(2) x E7 in E8: 248 = (3,1)+(1,133)+(2,56)): acts as -1 on (2,56)
print("[S] 248 = (3,1)+(1,133)+(2,56) under SU(2)xE7: -1 in SU(2) acts as +1 on 3+133 = 136 dims and -1 on 112 dims -> nontrivial element of E8 (dims check:", 3+133+112, ")")
