# U1 LEDGER — Open items, algebraic/dimension track (2026-10-18)

Package: `Open_Algebraic_2026-10-18/`. Consolidated in rev. 5 §13.6–13.8 (Propositions 13.10–13.17 and Theorem 13.16).
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact (incl. exact finite computation); floating-only = Cat B. Notation as rev. 4 (W_P = Fix(P); V_Eis/d_Eis). See ERRATUM_Consolidated_Rev5_2026-10-18.md.
Text outputs (json/log/txt/jsonl/flag) are stored verbatim in the package's OUTPUTS_BUNDLE_2026-10-18.txt (byte counts and sha256 per member); reports and scripts are separate files.

## Category A
- A1. Odd-parity sectors (no ρ(T)-eigenvalue 1) lift to cusp forms. Consequences: cusp ≥ (s−1)(s−3)/4, and d_Eis ≤ 3∏(p^e+1)/2 at every tested odd s ≤ 99.
- A2. Corrected orbit lemma for all odd s: c_ε(O₀, q_min) = (1+ε_all)N_{O₀}(q_min). The original lemma is false (s = 27, 245, …). s = 27: dim V = 702.
- A3. Parity fact: x₂ is even on Δ, so Z_all = −1 and the ε_all = −1 sectors vanish for all odd s.
- A4. Complement for all odd m: #Fix(g) = 2(m−1), #Fix(−g) = 2(m+1), tr g = 2m, and dim{N = 1, g = −1} = m(m−1).
- A5. Prime-square old/new pieces (exact ranks): s = 9: 12/48/12; s = 11: 18/72/20; s = 25: 36/432/132. All pieces are injective.
- A6. **dim V(98) = 2406.**
  - The kernel is 42 g-relations plus R1 (q = 11/12) and R2 (q = 1/4).
  - h = (g+I)/4 satisfies h² = g and is an isometry. It maps the + sets onto the − sets.
  - Overlattice M = ⟨(4,0),(1,1/7)⟩, Gram [[32,64],[64,32]], with hM = M and hM^♯ = M^♯. The theta identities follow by the cone argument (h_lattice.py/.json).
  - The half-cone bound 2408 is not sharp.
- A7. Half-cone g-relations = δ_iso ⊗ X for prime m, given g-consistency on the classes (checked exactly at m = 3, 5, 7).
- A8. s = 64: W_P = 1986 and d₂(k = 6) = 36 (Z[ζ₆₄] certificate).
- A9. Atkin–Lehner levels: 140 (vector-valued) versus 19600 (scalar newforms) are consistent.

## Category B / open
- Prediction: extra h-relations at m = 2k²−1 (7, 17, 31, …). No count is claimed for m = 17.
- g-consistency for all odd m; composite m.
- d_Eis equality (the all-even sector carries no cusp content).
- Global root numbers at s = 7 are non-real (numerical). The local split at 5 and 7 is open (blocked: additive character and λ-factor not implemented).
- Uniform proof and irreducibility for the prime-square pieces: open (blocked: ρ on the old piece not built).
- d₂ = 2^{k−1}+4 for general k.

## Files not included
`__pycache__/`, `w2_Y.npy` (480 bytes, binary; listed in the bundle manifest).
