# FROZEN before run (MR2, 2026-11-10). B1-c2' candidate E-T (cc21b272 row 12): Pin(6) lift of df with a compensating Spin(10) reflection.
# [L] Clifford check in Cl(16) (256-dim, Jordan-Wigner): directions 0..5 = TY6 frame (0 = x, 1 = phi1, 2 = phi2 flipped by f at a
#     fixed point; 3,4,5 fixed), 6..15 = the 10 of SO(10) (6 = compensator a). Lift L = e0 e1 e2 e6 (even, in Spin(16)).
#     Checks: L^2 on the chiral 128 (and the other 128); Ad_L on so(6) equals Ad(df) = conjugation by diag(-1,-1,-1,1,1,1);
#     Ad_L on so(10) is the reflection R_a; alternatives (3-vector compensator, no compensator) for contrast.
# [d] H^1(Sigma;Z2) = J[2] (even subsets of W mod complement): elements fixed by each orientation-reversing class; d0 = 0 always.
import numpy as np, itertools
s0 = np.eye(2); sx = np.array([[0,1],[1,0]],dtype=complex); sy = np.array([[0,-1j],[1j,0]]); sz = np.diag([1.,-1.]).astype(complex)
def kr(ms):
    out = np.array([[1]],dtype=complex)
    for m in ms: out = np.kron(out, m)
    return out
e = []
for k in range(8):
    e.append(kr([sz]*k + [sx] + [s0]*(7-k))); e.append(kr([sz]*k + [sy] + [s0]*(7-k)))
I = np.eye(256)
ok = all(np.allclose(e[a]@e[b]+e[b]@e[a], 2*(a==b)*I) for a in range(16) for b in range(16))
G17 = np.eye(256, dtype=complex)
for a in range(16): G17 = G17@e[a]
# Gamma_17 = e0...e15 squares to (-1)^{120} = +1; its +-1 eigenspaces are the two 128s
assert np.allclose(G17@G17, I)
Pp, Pm = (I+G17)/2, (I-G17)/2
print(f"[L] Cl(16) on C^256: anticommutators exact: {ok}; omega = e0...e15, omega^2 = +1; rank of chiral projectors: {int(round(np.trace(Pp).real))}, {int(round(np.trace(Pm).real))}")
def prod(idx):
    M = np.eye(256, dtype=complex)
    for i in idx: M = M@e[i]
    return M
def sq_on(M, P):
    S = M@M
    if np.allclose(S@P, P): return '+1'
    if np.allclose(S@P, -P): return '-1'
    return 'other'
cands = {
  "E-T lift: e_x e_phi1 e_phi2 . e_a (a = 6)": [0,1,2,6],
  "contrast: e_x e_phi1 e_phi2 . e_a e_b e_c (6,7,8)": [0,1,2,6,7,8],
  "contrast: e_x e_phi1 e_phi2 (no compensator; odd, not in Spin(16))": [0,1,2],
}
for lab, idx in cands.items():
    M = prod(idx); even = len(idx)%2 == 0
    comm_w = np.allclose(M@G17, G17@M)
    print(f"  {lab}: degree {len(idx)} ({'even, in Spin(16)' if even else 'odd: NOT in Spin(16)'}); commutes with omega (preserves each 128): {comm_w}; square on 128+: {sq_on(M,Pp)}, on 128-: {sq_on(M,Pm)}")
L = prod([0,1,2,6]); Li = np.linalg.inv(L)
dfdiag = [-1,-1,-1,1,1,1]
ad6 = all(np.allclose(L@(e[i]@e[j])@Li, dfdiag[i]*dfdiag[j]*(e[i]@e[j])) for i in range(6) for j in range(6) if i<j)
Ra = [-1]+[1]*9
ad10 = all(np.allclose(L@(e[6+i]@e[6+j])@Li, Ra[i]*Ra[j]*(e[6+i]@e[6+j])) for i in range(10) for j in range(10) if i<j)
mixed = all(np.allclose(L@(e[i]@e[6+j])@Li, dfdiag[i]*Ra[j]*(e[i]@e[6+j])) for i in range(6) for j in range(10))
print(f"[L] Ad_L on so(6) = Ad(df), df = diag(-1,-1,-1,1,1,1): {ad6}; Ad_L on so(10) = Ad(R_a): {ad10}; on the (6,10) part = df x R_a: {mixed}")
print(f"[L] L^2 = +1 in Spin(16) (identity on all 256): {np.allclose(L@L, I)}")
# --- [d] J[2] fixed elements
W = ['0','inf','1','i','-1','-i']; B6 = frozenset(range(6))
def norm(T):
    T = frozenset(T); return min(T, B6-T, key=lambda s:(len(s),sorted(s)))
J2 = sorted({norm(T) for k in (0,2,4,6) for T in itertools.combinations(range(6),k)}, key=lambda s:(len(s),sorted(s)))
act = lambda p,T: norm({p[i] for i in T})
GEN = {'g1': (0,1,3,4,5,2), 'g2': (2,4,1,3,0,5), 'c': (0,1,2,5,4,3)}
def comp(a,b): return tuple(a[b[i]] for i in range(6))
idp = tuple(range(6))
def closure(gens):
    G = {idp}; fr = [idp]
    while fr:
        nw = []
        for h in fr:
            for g in gens:
                k = comp(g,h)
                if k not in G: G.add(k); nw.append(k)
        fr = nw
    return G
Ap = closure([GEN['g1'],GEN['g2']]); Fu = closure(list(GEN.values())); rev = Fu - Ap
def inv(g):
    gi=[0]*6
    for i in range(6): gi[g[i]]=i
    return tuple(gi)
left = set(rev); print(f"[d] orientation-reversing images: {len(rev)}")
while left:
    p = min(left); cl = {comp(comp(g,p),inv(g)) for g in Fu}; left -= cl
    fx = [d for d in J2 if act(p,d)==d]
    print(f"  class size {len(cl)} | rep {[W[i] for i in p]} | J[2] elements fixed: {len(fx)}/16 | d0 = 0 fixed: {act(p,frozenset())==frozenset()}")
c = GEN['c']
print(f"[d] r = c: fixed J[2] elements {[sorted(W[i] for i in d) for d in J2 if act(c,d)==d]}")
