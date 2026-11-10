# FINDINGS (Non Local Path), 2026-11-09 12:33 CST. Same content as NL_OWNER_DEFS_PREV_TEH_FORMAL_CHECK_2026-11-09_1232.md (sha d5360510…); Physicist independently rechecked 14(ii).

# Non Local Path: formal check of the Owner definitions (t4183), 2026-11-09 ~12:32 CST
Inputs: DEF1 reverse-parity P_rev (Zenodo 18442276) and DEF2 11D T^(EH) (Zenodo 18586411), as relayed by Physicist, plus Physicist flags (a)–(j).
Constraints: additive file only; tip 7cddb188 untouched; no CERT; no external sends; no invented constants.
Numerical check: gamma-matrix algebra in the Dirac and Majorana representations (Clifford relations verified), python3, nothing saved.

## DEF1: P_rev = γ⁰ K Π  (K = complex conjugation, Π: x→−x)
1. (a) PROVED. P_rev² = γ⁰γ⁰*. This is +1 in the Dirac and chiral representations and −1 in the Majorana representation (checked numerically; same result in mostly-plus signature). A phase cannot change it: for A′ = e^{iθ}A, A′² = A². So P_rev² = −1 holds exactly in the Majorana representation and is independent of the 35-component phase. With C: ψ→ψ* in that representation, CP = −P_rev, so P_rev = CP up to sign. PROVED.
2. (b) Confirmed. As written, P_rev maps H_{+U} → H_{−U} = H_{+U}⊗ℂ², so P_rev² is undefined. Also, γ⁰ψ*(−x) lies in H_{+U} and no embedding into the ℂ² factor is given. Repair: define P_rev on H_{+U}⊕H_{−U}, or fix an embedding ι. CONDITIONAL.
3. (c) For the free Dirac Hamiltonian H = α·p + βm: P_rev H P_rev⁻¹ = −H holds exactly in the Majorana representation (verified numerically) and fails in the Dirac representation (neither +H nor −H). With P_rev antiunitary and t fixed, −H is exactly the symmetry condition for the evolution. Energy inversion is PROVED in the Majorana representation. It is not m↦−m as a parameter, since H(−m) ≠ −H(m). The negative-inertial-mass reading is OPEN.
4. Anticommutation with T depends on convention. For antiunitaries, P′ = e^{iα}P and T′ = e^{iβ}T turn PT = εTP into P′T′ = e^{2i(α−β)}ε T′P′. Anticommutation can always be arranged by a phase choice and carries no invariant content. OPEN.
5. CP_rev T: if P_rev = ±CP, then C·P_rev·T = ±C²PT, which is ±PT. The conserved quantity is PT, not CPT, so the CPT theorem does not guarantee it. PROVED as a consequence. "Across the inter-brane boundary" has no stated boundary condition. OPEN.
6. (d) Confirmed. The charge of the image of Z could be −Z or −(119−Z); this is ambiguous. Z↦119−Z is a bijection on {1,…,118}.
7. Inverted Aufbau: filling from the maximum (n,l,m,s) needs a cutoff n_max, because n is unbounded. CONDITIONAL.
8. Inverted binding: "lightest tightest" and "heaviest most stable" can only both hold under a stability measure other than binding energy per nucleon, and none is defined. OPEN.
9. SU(2)_R acting on P_R: consistent as a model choice; physically OPEN. 539.9 s flux wave: OPEN ("immutable" is undefined).

## DEF2: T^(EH) on M¹¹ = M⁵×K3×S²
10. (e) REFUTED-by-proof. K3 has no maximally symmetric metric. A flat compact manifold has χ = 0. A compact simply connected manifold of constant positive curvature is S⁴, with χ = 2. Constant negative curvature would force an infinite fundamental group. K3 has χ = 24 and is simply connected. Repair: the Ricci-flat Yau metric, which is not flat (holonomy SU(2)).
11. (f) PROVED. δ(F²)/δg^MN = 4F_MPQR F_N^PQR gives T = (1/6)F_MPQR F_N^PQR − (1/48)g_MN F² when L_EH sits outside the 1/(16πG₁₁) factor, as written. The Owner's expression, (1/3)FF − (1/24)gF², is exactly twice this.
12. (g) With A literally equal to ky, ds² = A²η gives ∂_y g = (2/y)g, not −2k·g. Repair: A_DEF2 = e^{−ky}, so the metric is e^{−2ky}η, which matches L2. PROVED once renamed.
13. (h) L6 is exactly AdS₅ (Ric = −4k²g) times a 6D Einstein fibre with Ric = K·g. Rederived: R = −20k² + 6K gives G_ext = G_yy = 6k² − 3K and G_fib = 10k² − 2K. L7 reads G_ext = −Φ/96 and G_fib − G_ext = 4k² + K = Φ/144, which gives k² = Φ/1728 and K = 8k². If K = 0 (Ricci-flat), L7 forces k = Φ = 0. PROVED.
14. Repaired geometry: AdS₅(k) × Ricci-flat K3 × round S², with K_S = 1/r² > 0. Then R = −20k² + 2K_S, and the blocks are G_ext = G_yy = 6k² − K_S, G_K3 = 10k² − K_S and G_S² = 10k². PROVED (product of Einstein factors). Consequences under the stated assumptions:
   (i) Any source that is isotropic over the internal space, including Λ₁₁g, forces G_K3 = G_S², so K_S = 0. That is impossible for a round S². REFUTED-by-proof; block-anisotropic flux is required.
   (ii) Moving the L7 right-hand sides over to the S² block (G_ext = −Φ/96, G_S² − G_ext = Φ/144) gives k² = −Φ/2880 and K_S = Φ/120. So k² ≥ 0 forces K_S ≤ 0, a contradiction. REFUTED-by-proof for that transplant.
   A correct repaired L7 needs the source for each block (F₄ legs on K3 or S², torsion, Λ₁₁). OPEN. L7 as written has no Λ₁₁ term, so it is CONDITIONAL on Λ₁₁ = 0 or on Λ₁₁ being absorbed into Φ.
15. (i) Confirmed. T_matter needs −2∂L_m/∂g^MN in addition to g·L_m. Dropping it is exact only for potential-only scalars. PROVED.
16. (j) Correct as a statement about standard supergravity: 11D supergravity admits no cosmological constant, so a nonzero Λ₁₁ means a non-supersymmetric 11D theory. Not a refutation of the model. The 61-puncture value is undefined. OPEN.
17. G₁₁ = M_Pl⁻⁹ is dimensionally fine if M_Pl is the 11D Planck mass, up to 2π factors. If it is the 4D Planck mass, it is CONDITIONAL on V₇ ~ M_Pl⁻⁷.
18. αR_MNKL T^MNK T^L: which torsion vector T^L means is unstated, and T^torsion is not given. OPEN.
19. Λ₅ = −6k² matches the vacuum AdS₅ block (G = 6k²g). PROVED consistent.
20. Φ is "evaluated across V₃₅", which is undefined, so the −1/96 and 1/144 coefficients cannot be derived from F₄. OPEN.

## Inputs needed from the Owner
(1) The codomain and embedding of P_rev, and which representation is meant (Majorana makes P_rev² = −1 exact). (2) The charge rule for −Z. (3) The block-by-block sources on K3 and S² (flux legs, torsion, Λ₁₁). (4) Definitions of V₃₅ and of the 61-puncture limit.
