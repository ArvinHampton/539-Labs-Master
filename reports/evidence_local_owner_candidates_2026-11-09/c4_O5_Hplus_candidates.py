# Local-derived. O5 / H_{+U} candidate checks (fibrewise in momentum p; pure linear algebra).
import numpy as np
s0 = np.eye(2); s1 = np.array([[0,1],[1,0]],complex); s2 = np.array([[0,-1j],[1j,0]]); s3 = np.diag([1.,-1.]).astype(complex)
kr = np.kron
# Dirac rep
g0D = kr(s3,s0).astype(complex); gD = [kr(1j*s2, s) for s in (s1,s2,s3)]
# Majorana rep (all gamma purely imaginary): standard choice
g0M = kr(s2,s1); gM = [1j*kr(s3,s0)*1, kr(s2,s2), -1j*kr(s1,s0)]
def clifford_ok(g0,g):
    G = [g0]+g; eta = np.diag([1,-1,-1,-1]); I = np.eye(4)
    return max(np.abs(G[a]@G[b]+G[b]@G[a]-2*eta[a,b]*I).max() for a in range(4) for b in range(4))
for name,(g0,g) in {"Dirac":(g0D,gD),"Majorana":(g0M,gM)}.items():
    print(name, "Clifford err", clifford_ok(g0,g), " all gamma imaginary:", all(np.abs(M.real).max()<1e-15 for M in [g0]+g))
rng = np.random.default_rng(3)
def H(p,m,g0,g):
    al = [g0@gk for gk in g]; return sum(pk*a for pk,a in zip(p,al)) + m*g0
for name,(g0,g) in {"Dirac":(g0D,gD),"Majorana":(g0M,gM)}.items():
    for m in (0.0, 1.0):
        e_fw = e_anti = 0.0; e_sq = np.abs(g0@g0.conj() - (g0@g0.conj())[0,0]*np.eye(4)).max()
        for _ in range(200):
            p = rng.normal(size=3); E = np.sqrt(p@p+m*m); Hp = H(p,m,g0,g)
            al = [g0@gk for gk in g]; ap = sum(pk*a for pk,a in zip(p,al))
            U = (E+m)*np.eye(4) + g0@ap; U = U/np.sqrt(2*E*(E+m))
            e_fw = max(e_fw, np.abs(U@U.conj().T-np.eye(4)).max(), np.abs(U@Hp@U.conj().T - E*g0).max())
            # A = gamma0 K Pi acts fibrewise psi(p) -> gamma0 conj(psi(p)) (Fourier of psi*(-x)); A H(p) A^-1 = g0 conj(H(p)) g0^-1
            e_anti = max(e_anti, np.abs(g0@Hp.conj()@np.linalg.inv(g0) + Hp).max())
        print(f"{name} m={m}: FW unitary+diagonalising err {e_fw:.2e};  ||A H A^-1 + H|| max {e_anti:.2e};  gamma0 gamma0* = {(g0@g0.conj())[0,0].real:+.0f}")
# H_{+U} C2: internal C^35 factor: (gamma0 x 1_35) K squared = gamma0 gamma0* x 1_35
d = 35; Ab = kr(g0M, np.eye(d)); print("C2 internal C^35: (A x 1)^2 = g0 g0* x 1 err", np.abs(Ab@Ab.conj() - kr(g0M@g0M.conj(), np.eye(d))).max())
# H_{+U} C3: no antiunitary J = V K on C^d with J^2 = -1 for odd d: V Vbar = -1 => |det V|^2 = (-1)^d
for d in (1,3,35):
    print(f"d={d}: (-1)^d = {(-1)**d}  => V conj(V) = -1 impossible (|det V|^2 >= 0)" if d%2 else "")
# multiplicity: eigenvalue +E(p) has multiplicity 2 per p on C^4, and E depends on |p| only => infinite multiplicity (angular L^2(S^2))
print("eigenvalues of H(p) (Majorana, m=1, random p):", np.round(np.linalg.eigvalsh(H(rng.normal(size=3),1.0,g0M,gM)),6))
