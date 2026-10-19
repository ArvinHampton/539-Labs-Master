# U1 LEDGER — Algebraic Round 3 (2026-10-19)
Package: `Algebraic_Round3_2026-10-19/`. Pure copy-and-create. No locks altered. CORE_FREEZE holds (locked H_s with c₂ = (−4,1) unchanged; H_s^axes is a parallel object). Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact (incl. mod-ℓ with lift); floating-only/numerical/cited = Cat B. Text outputs verbatim in OUTPUTS_BUNDLE_2026-10-19.txt; pickles in BINARIES_B64_BUNDLE_2026-10-19.txt.

## Category A
- A1. **Proposition K1:** extra h-relations at m = 2k²−1 equal k(k−1) for all k ≥ 2; rank_g = m(m+1); dim F = 2m². Exact checks k = 2, 3, 4 (over Q) and k = 5, 6 (mod two primes, consistency). Gives proved upper bounds for dim V(2m²); sharpness open. (rev7 §15.1)
- A2. 7s − 32 = −2Q(c₂); u₂ spans c₂^⊥; Q₂(u₂) = sΔ/(2g²); residual Gauss phase = Q(πw); Δ = 16(s−2)² − 9s(s−2). Symbolic in s. (rev7 Prop 15.2)
- A3. Weil representations Z/47, Z/59, Z/71 (both parts irreducible); Z/17², Z/19², Z/23² (even = 1 ⊕ R, odd irreducible). Mod ℓ with lift. (rev7 Prop 15.15)
- A4. Involution M, edge-class invariance H^(c₁,c_a) = H^(c₁,c_{s−a}); c₂ = (−4,1) is a definition, unique only among b = 1 at s = 7; c₁ forced by the wall n = 0; axes cone gives Cmixed ≡ 0. (rev7 Props 15.3–15.5)
- A5. Only (s − 2) of Δ is intrinsic given c₁; 7s − 32 and √Δ tied to the locked c₂. (rev7 Remarks 15.6, 15.16)
- A6. H_s^axes exact closed forms through t^{13/2}, field Q(√(2s))·√π, denominators (s−2)^k; c_{−1/2} = −√π/(√(2s)+2). (rev7 Thm 15.8)
- A7. Universal piece: S^ax_r = rev4/rev6 R_r for r = −1/2..5/2 (with A11 of the analytic ledger: through 13/2).

## Category B
- 70-digit PSLQ recognitions (c6/repslq.json); direct summation at s = 20 (c7/verify_direct.json). c7/verify.json is empty (see NOTE_Rev7_Flags_on_Earlier_Files_2026-10-19.md, item 9).
- The "selection rule" reading of the s = 7 conditions on c₂.
- s = 121 and s = 3481: factor-dimension predictions only (no label-space run).

## Files not included
__pycache__; weil_cyclic.py (identical to Open_Algebraic_Update2_2026-10-18/weil_cyclic.py on Master).
