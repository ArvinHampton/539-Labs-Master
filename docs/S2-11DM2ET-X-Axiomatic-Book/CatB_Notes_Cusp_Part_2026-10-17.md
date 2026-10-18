CATEGORY B NOTES
Cusp part, 2026-10-17
Every item in this file is CATEGORY B (cited theory not re-proved, PARI-dependent structure, sketch, expectation) or OPEN. Nothing here is a lock.
Companion to U1_LEDGER_Cusp_Part_2026-10-17.md (Cat A).
Source (verbatim copy). Cusp_Part_2026-10-17/.

Caveats. No HQCC, TPC or RH claim. Residual is not Resonant (539 is a count). CORE_FREEZE untouched.


B1. Maass/Hecke status of the cusp forms
- That the 12 u_chi are dihedral lambda = 1/4 Maass forms (Maass 1949, from pure-type Hecke characters), cuspidal (Hecke theory: cusp iff chi != chi o sigma) and newforms: standard theory, not re-proved.
- Level 140 N(f_chi) = 19600 (formula d_K N(f_chi)): standard, not re-proved.
- Nebentypus omega = chi_140 omega_0, omega_0(n) = chi((n)) an even character mod 35: consistent on 27 primes (nebentypus.txt); formula not proved.
- Calling the genus pieces Maass-Eisenstein series E_{psi, psi chi_140}(., 1/2): standard naming.

B2. PARI group structure at (2 sqrt35)
- Cl+_m = Z/24 x Z/2 x Z/2 for m = (2 sqrt35) inf1 inf2 (and Z/24 x Z/2 x Z/2 at p2^3 p5 p7), the sigma-action j -> 13j, and the conductors: PARI (bnrinit/bnrconductor, cypari2 2.2.4; bnfcertify = 1 for the base field only). Not hand-certified; only the order 96 is certified by hand.

B3. Lewis-Zagier / L-value reading of the cusp rows
- The 24 cusp rows of Phi are expected to be the vector-valued LZ period functions of the 12 dihedral forms, and their values at rationals combinations of additively twisted central values L(1/2, u_chi, e(. x)). L-values not evaluated independently.
- psi_Eis as a finite combination of LZ period functions of the 8 genus Eisenstein series: the decomposition is Cat A; the LZ period-function theory for Eisenstein series is cited.

B4. Herglotz closed form for psi_Eis (expectation, untested)
- Eisenstein period functions at s = 1/2 are expected to be Herglotz type: twisted double sums sum_{m,n>=1} psi1(m) psi2(n)/(mx+n), and F(x) = sum (psi_Gamma(nx) - log nx)/n for the trivial pair, modulo elementary terms.
- Radchenko-Zagier show F is an S-cocycle modulo elementary functions and note Herglotz's evaluation of J(6+sqrt35), the same unit as eps. Suggestive only. No elementary closed form for psi_Eis obtained.

B5. EM and interchange (sketch only)
- Interchange on [y0, inf): dominated convergence (O(X) lattice points mod gamma with |Q| <= X; K_0, K_1 exponential decay).
- Near y -> 0 via u = M^{-1}(u o S); Euler-Maclaurin on the Shintani cones [e1, gamma e1), [f, gamma f) (closed sectors, non-null edges, |Q| ~ |nu|^2 uniformly). Error terms not written out.

B6. Citations and status
- H. Maass, Math. Ann. 121 (1949) 141-183, doi:10.1007/BF01329622: verified bibliographically; content taken as standard, not re-read.
- Lewis-Zagier, Ann. Math. 153 (2001), arXiv:math/0101270: verified earlier.
- Borcherds, Invent. Math. 132 (1998), arXiv:alg-geom/9609022: verified earlier (no longer needed for the S-law).
- Radchenko-Zagier, Arithmetic properties of the Herglotz function, J. reine angew. Math., doi:10.1515/crelle-2023-0009, arXiv:2012.15805: verified bibliographically this session.
- Hecke's dihedral construction: standard, cited generically; no specific paper verified.


OPEN
- Elementary closed form for psi_Eis (test against twisted Herglotz double sums).
- Hand certification of the structure of Cl+_(2 sqrt35).
- Fully written EM error analysis and interchange.
- Independent evaluation of the twisted central L-values to cross-check the cusp-row Phi values.
- Export of the individual Eisenstein coefficient vectors of the 116 Eisenstein components.
- s = 8, 11 analogues (unchanged).
- Unchanged: C_third alone; Object B; Per_off; Remark 8.5; Slash_two; QM of g_s.

Hygiene. CATEGORY B throughout. No HQCC, TPC or RH claim. CORE_FREEZE untouched.
