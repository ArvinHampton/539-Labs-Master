# Local-derived. SUPERSEDES c4_O5_Hplus_candidates.py (kept on disk): that script's hand-typed "Majorana" set was not a
# Clifford representation (its own log shows Clifford err 4.0), so its Majorana rows are void. Here the Majorana rep is
# found by exhaustive search over Pauli products, as in ac1dd4e2 item 8. Dirac rows are recomputed identically.
import numpy as np, itertools
P = [np.eye(2,dtype=complex), np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.diag([1,-1]).astype(complex)]
paulis = [np.kron(P[i],P[j]) for i in range(4) for j in range(4)]
eta = np.diag([1,-1,-1,-1]); I4 = np.eye(4)
def clifford_err(G): return max(np.abs(G[a]@G[b]+G[b]@G[a]-2*eta[a,b]*I4).max() for a in range(4) for b in range(4))
cands = [c*M for M in paulis for c in (1,1j) if np.abs((c*M).real).max()<1e-15]   # purely imaginary
maj = None
for G in itertools.permutations(cands, 4):
    if clifford_err(list(G)) < 1e-14: maj = list(G); break
g0D = np.kron(P[3],P[0]); gD = [np.kron(1j*P[2],P[k]) for k in (1,2,3)]
reps = {"Dirac": [g0D]+gD, "Majorana": maj}
for n,G in reps.items(): print(n, "Clifford err", clifford_err(G), " purely imaginary:", all(np.abs(M.real).max()<1e-15 for M in G), " gamma0 gamma0* =", np.round((G[0]@G[0].conj())[0,0].real))
rng = np.random.default_rng(3)
for n,G in reps.items():
    g0 = G[0]; al = [g0@g for g in G[1:]]
    for m in (0.0, 1.0):
        efw = eanti = 0.0
        for _ in range(200):
            p = rng.normal(size=3); E = np.sqrt(p@p+m*m); ap = sum(pk*a for pk,a in zip(p,al)); Hp = ap + m*g0
            U = ((E+m)*I4 + g0@ap)/np.sqrt(2*E*(E+m))
            efw = max(efw, np.abs(U@U.conj().T-I4).max(), np.abs(U@Hp@U.conj().T - E*g0).max())
            eanti = max(eanti, np.abs(g0@Hp.conj()@np.linalg.inv(g0) + Hp).max())
        print(f"{n} m={m}: FW err {efw:.2e};  max||A H(p) A^-1 + H(p)|| = {eanti:.2e}")
# Option M on H x C^2: Phat = (A x sigma_x) K ; square and anticommutation with H x 1_2 (Majorana)
g0 = maj[0]; sx = P[1]; al = [g0@g for g in maj[1:]]
Ph = np.kron(g0, sx)
print("Option M: Phat^2 = (g0 g0*) x (sx sx*) =", np.round((Ph@Ph.conj())[0,0].real), " err", np.abs(Ph@Ph.conj()+np.eye(8)).max())
p = rng.normal(size=3); Hp = sum(pk*a for pk,a in zip(p,al)) + 1.0*g0; Ht = np.kron(Hp, np.eye(2))
print("Option M: ||Phat Htot Phat^-1 + Htot|| =", np.abs(Ph@Ht.conj()@np.linalg.inv(Ph) + Ht).max())
# H_{+U} C2: internal C^35 identity factor leaves the square unchanged
A35 = np.kron(g0, np.eye(35)); print("C2: (A x 1_35)(A x 1_35)^bar = -1 err", np.abs(A35@A35.conj()+np.eye(140)).max())
