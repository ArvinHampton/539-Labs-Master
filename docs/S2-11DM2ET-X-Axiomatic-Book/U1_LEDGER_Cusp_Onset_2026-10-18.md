# U1 LEDGER — function-span dimensions, Eisenstein dimensions and cusp criteria for the s-family (2026-10-18)

Packages: `Cusp_Onset_2026-10-18/` (floating; Cat B), `Cusp_Onset_Closure_2026-10-18/` (exact). Consolidated: rev. 4 Theorem 11.6, Remark 11.7, Propositions 11.8–11.9.
Text outputs (json/log/txt) of each package are stored verbatim in its `OUTPUTS_BUNDLE_2026-10-18.txt` (member byte counts and sha256 included); reports and scripts are separate files.
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact (incl. exact finite computation); floating-only = Cat B. Notation: W_P = Fix(P); V = function span; V_Eis/d_Eis = Eisenstein span/dimension; V^⊥ = complement of V in W_P; ρ(S) := S_lab⁻¹. See ERRATUM_Consolidated_CrossReview_2026-10-18.md.

## Category A
- A1. Orbit bound: dim V ≤ #consistent ⟨γ,−1⟩-orbits = s(s−1) (odd s), (s/2)(s/2+1) (even s) (Burnside).
- A2. **Exact ranks** (FLINT, rational) equal the upper bound for every s = 5..51 and s = 72; dim V = s(s−1) for odd s ≤ 51.
- A3. s = 2m² mechanism: γ has a square root in SO(A_s)(Q) iff s = 2m²; half-cone bound with gap m(m−1) (m = 2..7), equal to the exact lower bound for m = 2..6: dim V = 18, 84, 260, 630, 1302 at s = 8, 18, 32, 50, 72. s = 98: 2406 ≤ dim V ≤ 2408 (not certified).
- A4. d_Eis = 3∏(p^e+1)/2 for odd s (certified local factors; conditional on the cited congruence theorem); even s: d_Eis = d₂(k,v)∏_{p^e‖v}(p^e+1)/2 with v the odd part of 2t(t−1), 2^k ‖ 2t(t−1); d₂ = 2^{k−1}+4 (k even), +6 (k odd, v ≡ 1 mod 4), +5 (k odd, v ≡ 3 mod 4), certified k ≤ 5 (even s ≤ 62).
- A5. Table (rev. 4 Thm 11.6(v)): d_cusp > 0 for every tabulated s except 6, 8, 10. **s = 11: dim V = 110, d_Eis = 90, d_cusp = 20.** Odd s: d_cusp ≥ (s−1)(s−3)/4 > 0 (equality iff s, s−2 both prime powers) at the certified s.
- A6. u_L criterion: coprime part Eisenstein iff H̄ = 1. Verdicts (exact finite group computations on complete parts): Eisenstein s = 5, 7, 9, 13, 15, 16, 20, 24; cusp content s = 11, 14, 17, 18, 19, 21, 22, 23, 25, 29, odd 31..41, 53, 55, 57 (53–57 Cat B, incomplete coverage); open s = 32, 34, 36, 40.
- A7. **Refutation (C11):** "u_L has cusp content iff h⁺ ≠ #genera" is false (s = 14, 17, 18, 22, 23). The family cusp part (d_cusp > 0 at s = 5, 7, 13, 15) and the u_L verdict are different notions.
- A8. Deep bad primes: s = 9, 16, 24 all tested 𝔠-parts complete and genus-pure; s = 18 3-parts pure, coprime part not.

## Category B
- dim V = s(s−1) for all odd s; the gap m(m−1) for all m; d₂ for k ≥ 6.
- |Ḡ^σ| = 2^{ω(s)}φ(s−2) in general; sufficiency of modulus M = 2dc; S-invariance of T_𝔠 for all 𝔠.
- All floating SVD ranks and FFT counts of Cusp-Onset (C13 relabel). The pure-tensor proof of d_Eis for odd s was written in rev. 4 and has had no separate check.

## Files not included
`__pycache__/`, empty (0-byte) logs.
