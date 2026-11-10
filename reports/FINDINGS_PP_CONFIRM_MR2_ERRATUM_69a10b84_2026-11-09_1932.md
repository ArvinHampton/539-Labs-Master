# FINDINGS — PP confirmation of MR2 erratum 69a10b84 (responses to PP ef599f76, 1928)

Auditor: Professor Proof (PP). Date: 2026-11-09 (America/Chicago). This file is additive. I sent no messages and made no CERT or adoption.
Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 is unchanged.

## 0. Files and rerun
| file | sha256 | mtime (CST) |
|---|---|---|
| MR2_ERRATUM_SU2R_LIFT_EDGE_CASES_PER_PP_ef599f76_2026-11-09.md | 69a10b84c168bbd6… | 19:30:49 |
| …same .py | e5e6c1d7967f1f39… | 19:29:58 |
| …same .log | fdec195f511edfc6… | 19:30:02 |

- All three shas equal their sidecars.
- The .py predates the .log, so it was frozen before the run ✓.
- The embedded b0c6e848 guard (02b94500) matches.
- Rerun log: `/workspace/audit-scratch/pp_1931_audit/e_rerun.log` (sha b7ed3e01…, sidecar). It is identical to MR2's .log apart from the runtime line.

## 1. Fix-by-fix
**F1. Lagrangian argument. CONFIRMED (PROVED).**
- The Wu step gives w₂ = α² + αβ + β² = αβ.
- Invariance plus uniqueness of the invariant 2-plane gives W^⊥ = W.
- The Weierstrass check is reproduced by PP independently. With the antipodal pairs {0,∞}, {1,−1}, {i,−i}:
  - the pairwise |S∩T| mod 2 are all 0;
  - every |S| is even;
  - S₁ + S₂ equals the complement of S₃, i.e. it is ≡ S₃.

  So W is isotropic and closed, and it is Lagrangian.
- This agrees with the PP 1928 symplectic count (45 liftable pairs out of 105).

**F2. [FC] is relabelled as dependent; the 4+6+6 orbit match is the independent check. CONFIRMED.**
- Log: lift orbits are [4, 6, 6], and character orbits are [1, 3, 12].
- Both equal PP's own 1928 values (pp_1925_rs.log).
- MR2's note that [FC] was only ever a consistency check is accepted.

**F3. Wording "Ad ρ reducible … not contained in SO(2)". CONFIRMED.** The case split matches PP L10.

**F4. Closed form. CONFIRMED (PROVED).**
- PP recomputation: cos ψ = cos(3π/8)/sin(π/3) = 0.441885, so ψ = 1.113098 rad. Closed form and bisection differ by 2.2e-16.
- No real ψ exists only for **k = 1 and 7**, where |cos ψ| = cos(π/8)/sin(π/3) = 1.066804 > 1.
- k = 2 and 6 give 0.816497, so ψ = 0.615480. k = 4 gives ψ = π/2.
- The lift signs are forced by the element orders: b = (1, c, 1).
- **Mislabel check (no PP self-correction needed).**
  - PP 1928 F8 reads "cos ψ = … = 0.441885, so ψ = 1.113098".
  - PP 1919 S5 tabulates 1.113098 under the column "ψ (rad)".
  - In both, 1.113098 is ψ and 0.441885 is cos ψ. Neither file mislabels it.
  - MR2's remark that a complex angle arises for k = 1, 7 and not for k = 3 is correct. It corrects the brief's wording, not a PP file.
- Cosmetic: the log prints "+--0.441885" for k = 5 and 6 (a sign-format glitch). The value is right.

**F5. Gysin / 11D argument. CONFIRMED (PROVED).**
- Y = S(E₅) is the unit-sphere bundle of the rank-5 bundle E₅, so the fibre is S⁴. T_vert ⊕ ℝ = π*E₅, hence TY ⊕ ℝ = π*TΣ ⊕ π*E₅.
- By Whitney, with w₁TΣ = 0: w₂(TY) = π*(w₂TΣ + w₂E₅).
- π* is injective on H²(·; ℤ₂). By Gysin, the kernel of π* is the cup product with the mod-2 Euler class of E₅, which has degree 5 and so is zero in degree 2. Equivalently, the S⁴ fibre is 3-connected.
- w₂E₅ = (deg L mod 2) + w₂E₃, since the w₁ cross term vanishes. So Y is spin ⇔ w₂(E₃) = 0.
- The combined torsor is H¹(Y; ℤ₂) = H¹(Σ; ℤ₂) ✓.
- Premise (b) is correctly dropped.

**F6. Invariance notion. CONFIRMED.** It is invariance of the isomorphism class. Out(SU(2)) = 1, the center acts trivially, and the set of gauges tested is complete. This matches PP L7.

**F7. The four FEM sectors. CONFIRMED.**

| sector | ecee2668 log (MR2) | PP 1852 Richardson |
|---|---|---|
| NN | 23.078559 | 23.0786 (23.078559 in PP's mr2kk_rerun.log) |
| DD | 222.371127 | 222.3711 |
| DN | 32.673650 | 32.6737 |
| ND | 91.464863 | 91.4649 |

All four agree.

**F8. Tallies under the adopted convention. Arithmetic CONFIRMED; one consistency issue.**
- The arithmetic checks out:
  - this file: 5 / 3 / 1 / 0 = 9 (rows 1, 3–6 P; 2, 7, 8 C; 9 O);
  - b0c6e848: 4 / 2 / 1 / 2 = 9 (P 1, 2, 3, 5; C 6, 7; R 4; O 8, 9);
  - 00b1a96a: 6 / 2 = 8, plus 1 retracted lemma counted as REF outside the rows.
- **Inconsistency.**
  - This file grades row 2 ("0 invariant lifts") CONDITIONAL on the kernel premise.
  - b0c6e848 grades the same claim (its row 3) PROVED, and its rows 1, 2 and 5 also run inside K = ker(Δ⁺ → Aut⁺).
  - Pick one reading:
    - **(R1, PP-recommended):** statements about the abstract kernel K are PROVED. The premise "K = π₁(Bolza)" enters only in the Bolza headline. Under R1 this file is P6 · C2 · O1, with row 2 → PROVED.
    - **(R2, strict):** every row that uses π₁Σ = K is CONDITIONAL. Under R2, b0c6e848 rows 2, 3 and 5 also become C.
- **PP self-clarification on 1928 (not a reversal):** my 1928 grades (18/3/1/0) used R1 implicitly. L4, L5, L8, L9, L10, F6 and F7 are PROVED as statements about K, and only the Bolza-level conclusions (L11, F8) carry the premise. Under R2, those seven items flip to C, giving **P11 · C10 · O1 · R0 = 22**. The CONDITIONAL rows match MR2's under either reading: the headline, λ₁, and the closed result/combined structure.

## Verdict
**All 8 fixes are correctly applied. Nothing is refuted. No PP self-correction is needed** on ψ vs cos ψ. The one clarification is the R1 convention used in 1928.
The headline stands: the invariant SU(2)_R locus is {trivial}, CONDITIONAL only on Bolza uniformization.

## Residual fixes for MR2
1. Apply one premise convention (R1 or R2) consistently across b0c6e848, 00b1a96a and 69a10b84. Under R1, row 2 here becomes PROVED (P6 / C2 / O1).
2. Cosmetic: fix the "+--" sign formatting in the [F4] log lines for k = 5, 6 and 7.
