# FROZEN before run (box clock ~22:30 CST). MR2 branch B1-c2 (OW t445u "Open c2"; criterion of erratum 0f635774).
# Exact checks (integer/Gaussian-integer arithmetic, numpy int matrices):
#  [B] bosonic rule f*C = det(f) C for candidate maps, from the MN2 G4 index sets of bd47ff5e (PP-audited):
#      {u,v,alpha,phi2}, {u,v,beta,phi2}, {u,alpha,beta,phi2}, {alpha,beta,phi1,phi2}; coefficients independent of x(=u), phi1, phi2, AdS.
#      Pullback sign of a reflection set S on a component with index set I is (-1)^{|S cap I|} (coefficient functions are invariant
#      because they depend only on y, alpha, beta and S contains none of these).
#  [C] Clifford: Cl(10,1) mostly-plus, gamma_0^2 = -1; lift of a reflection set S = product of Gamma_s (s in S);
#      square, commutator with W~ = Gamma_rho, and conjugation of the twist bivector product Gamma_{uv} Gamma_{mu1 phi1}.
import itertools, numpy as np
names = ['t','x1','x2','x3','rho','u','v','alpha','beta','phi1','phi2']
idx = {n:i for i,n in enumerate(names)}
G4sets = [{'u','v','alpha','phi2'},{'u','v','beta','phi2'},{'u','alpha','beta','phi2'},{'alpha','beta','phi1','phi2'}]
# r~ : twisted Sigma reflection. On Sigma, r reverses orientation, so r*vol_Sigma = -vol_Sigma and r*A = -A (+exact) for the twist
# connection A (dA ~ vol_Sigma). Preserving the metric term (dphi1 + A)^2 forces phi1 -> -phi1 (+const). Locally (fixed geodesic of r):
# u -> -u, phi1 -> -phi1. (If phi1 were not flipped, f*(Dphi1) = dphi1 - A, not +-Dphi1, since 2A is not closed.)
cands = {
 'r~ = {u,phi1}':                    {'u','phi1'},
 'P = {phi2}':                       {'phi2'},
 'c2 literal: P o r~ = {u,phi1,phi2}': {'u','phi1','phi2'},
 "c2' = P o r~ o Pi_x3 (8399be55 (i'))": {'u','phi1','phi2','x3'},
 "c2'' = P o r~ o T (8399be55 (ii'))":   {'u','phi1','phi2','t'},
 "(i) = r~ o Pi_x3":                 {'u','phi1','x3'},
 'W = {rho} (doubled MN2, G odd)':    {'rho'},
}
print("== [B] bosonic rule f*G = det(f) G ==")
bos = {}
for lab,S in cands.items():
    det = (-1)**len(S)
    if S == {'rho'}:
        gsign = -1   # odd extension G(rho) = sgn(rho) G_MN2 (bd47ff5e C2): W*G = -G; G has no rho leg
    else:
        signs = {(-1)**len(S & I) for I in G4sets}
        assert len(signs) == 1, (lab, signs)   # uniform sign on all components
        gsign = signs.pop()
    ok = (gsign == det)
    bos[lab] = ok
    print(f"  {lab:42s} det = {det:+d}  f*G = {gsign:+d} G  -> rule {'HOLDS' if ok else 'FAILS'}")
# Clifford algebra: 11 gammas, 32x32 complex, from Pauli tensor products (Euclidean Cl(11)), then gamma_0 -> i*gamma_0
I2 = np.eye(2, dtype=complex); X = np.array([[0,1],[1,0]],dtype=complex); Y = np.array([[0,-1j],[1j,0]]); Z = np.array([[1,0],[0,-1]],dtype=complex)
def kron(*ms):
    out = np.array([[1]],dtype=complex)
    for m in ms: out = np.kron(out, m)
    return out
E = []
for k in range(5):
    E.append(kron(*([Z]*k + [X] + [I2]*(4-k))))
    E.append(kron(*([Z]*k + [Y] + [I2]*(4-k))))
E.append(kron(Z,Z,Z,Z,Z))
for a in range(11):
    for b in range(11):
        ac = E[a]@E[b] + E[b]@E[a]
        assert np.allclose(ac, 2*np.eye(32)*(a==b))
Gm = [1j*E[0]] + E[1:]          # Lorentzian: Gamma_0^2 = -1
eta = [-1]+[1]*10
for a in range(11):
    for b in range(11):
        assert np.allclose(Gm[a]@Gm[b]+Gm[b]@Gm[a], 2*eta[a]*np.eye(32)*(a==b))
print("\n== [C] Clifford Cl(10,1) check: {Gamma_a,Gamma_b} = 2 eta_ab : True (exact 0/1/i entries)")
def lift(S):
    M = np.eye(32, dtype=complex)
    for s in sorted(S, key=lambda q: idx[q]): M = M@Gm[idx[s]]
    return M
Wt = Gm[idx['rho']]
B_tw = Gm[idx['u']]@Gm[idx['v']]@Gm[idx['alpha']]@Gm[idx['phi1']]   # twist bivector product; 'alpha' stands for the mu1-radial leg
# (at a generic point the mu1-radial direction is a combination of alpha,beta; both are fixed by every candidate map)
for lab,S in cands.items():
    L = lift(S); Li = np.linalg.inv(L)
    sq = L@L
    sqs = '+1' if np.allclose(sq, np.eye(32)) else ('-1' if np.allclose(sq, -np.eye(32)) else 'other')
    comm = '+1 (commute)' if np.allclose(L@Wt, Wt@L) else ('-1 (anticommute)' if np.allclose(L@Wt, -Wt@L) else 'neither')
    tw = '+ (preserved)' if np.allclose(L@B_tw@Li, B_tw) else ('- (flipped)' if np.allclose(L@B_tw@Li, -B_tw) else 'other')
    # HW projection Gamma_rho eps = eps preserved iff lift commutes with Gamma_rho
    print(f"  {lab:42s} lift^2 = {sqs}  [W~, lift] = {comm}  twist bivector product {tw}  HW projection {'kept' if 'commute)' in comm and 'anti' not in comm else 'MAPPED TO OPPOSITE CHIRALITY'}")
print("\n== verdict inputs ==")
print("  c2 literal (P o r~): bosonic rule", "HOLDS" if bos['c2 literal: P o r~ = {u,phi1,phi2}'] else "FAILS")
