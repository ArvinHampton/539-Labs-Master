# ADDENDUM (Local-derived) to FINDINGS_LOCAL_t4407_OA_OB_4A_25PARTS_2026-11-09_2000.md (e28e0fbd…). 2026-11-09, written 21:43 CST (America/Chicago)

- **Authority:** Owner t4407 (b0b9ae7f…), t4429 (b7c5709e, fallbacks), t4431 (f700141d, 90% stop lifted), and t4436 ("Let the math lead the pursuits on all open paths", 21:27), all as relayed and verified by the parent.
- **Rules:** pure math. Nothing adopted. No CERT. No Gemini. Nothing sent outside.
- **Additive:** e28e0fbd is not edited. Every correction below is made by reference to it.
- **Tip:** 7cddb188… untouched (checked before and after).
- **Separate stream:** the t4436 branch worker's directory evidence_local_t4436_branches_2026-11-09/ was not touched.
- **Naming:** the object formerly called RTA is the **resonant algebra** (Owner f1d167d1 / OW 81b74a31; name change only). "RTA" appears only as a historical alias in cross-references.
- **Convention:** ε = root number, w_N = Fricke eigenvalue.
- **PP files folded in** (each sha checked against its sidecar: MATCH):
  - ac9fe667… = FINDINGS_PP_AUDIT_LOCAL_t4407_…_e28e0fbd_2026-11-09_2025.md;
  - 69d33456… = FINDINGS_PP_CORRECTION_1949_CITATION_GRADES_edcd9551_2026-11-09_2030.md;
  - 5bf1e1dc… = FINDINGS_PP_TMOD_49a1_ATTEMPT_2026-11-09_2050.md. **This file governs wording and the rollup.**
  - Also bc12df1a… (1955) and edcd9551… (1949).
- **Citation rule (OW 3f160803 as amended by 36683379):** a citation alone never makes a claim PROVED. Rows that rest on unverified theorems carry the PP condition tags: C2, C3, T-theta, T-AL-new, T-GZK, plus the new Local tags T-U7 and T-U4 defined in §1.
- **Usage checkpoints** (weekly limit, shared): 74.4% at 20:03; 84.1% at 21:04. No stop applies (t4431).

## 0. Corrections to e28e0fbd, by reference (Local slips confirmed by PP)
1. **Header:** "~20:0x CST" reads **20:00 CST**.
2. **A3:** withdraw the clause "No nonzero element vanishes at all n ≡ 0 (mod 7) and … (see A5)".
   - oa_v3 coded the condition inverted (n%7!=0), so it tested "supported only on 7 | n", which has dimension 0.
   - **The truth is the opposite: every element of K has c(n) = 0 at all 7 | n, n ≤ 1200.** That is A5.
3. **B5:** ob_v2 started at **19:51 CST** (not ~19:52) under timeout 9000, so its end was ≤ ~22:21 (not 22:25). In fact the process was gone before 21:41 CST, with only D = 1, 8 finished (§3).

## 1. Results of this session

### A5: c(n) = 0 for all n ≡ 0 (mod 7), for every F ∈ K. CONDITIONAL on T-U7
- **T-U7** (Shimura 1973, Prop. 1.5, cited and not verified): U₇: Σc(n)qⁿ ↦ Σc(7n)qⁿ maps S_{3/2}(Γ₀(196), χ₂₈) to S_{3/2}(Γ₀(196), χ₂₈·(28/·)) = S_{3/2}(Γ₀(196), trivial), because 7 | 196/4.
- **PP's path (Fix 5):**
  - P₇F := Σ_{7|n}c(n)qⁿ = (F|U₇)|V₇ lies at level 1372 = 2²·7³. V₇ (τ ↦ 7τ) raises the level by 7, which is elementary.
  - [SL₂(ℤ):Γ₀(1372)] = 1372·(3/2)·(8/7) = 2352.
  - The weight-3/2 Sturm bound is (3/2)·2352/12 = 294. Apply V5 (integral-weight Sturm, verified by PP) to (P₇F)², of weight 3, with bound 588 = 2·294.
  - The exact data give c(n) = 0 for all 7 | n, n ≤ 1200 on all of K (oa_v2; oa_v8 to n ≤ 400). Since 1200 > 294, P₇F = 0.
- **Shorter equivalent:** U₇F ∈ S_{3/2}(Γ₀(196), trivial), whose Sturm bound is (3/2)·336/12 = 42. Its coefficients c(7n) vanish for n ≤ 171 > 42, so U₇F = 0.
- **Consistency check of T-U7's normalisation** (oa_v9, exact, n ≤ 60 > 42): U₇(V) has rank 1 and lies in the span of S_{3/2}(196, trivial) (dim 6; rank 6 → 6). U₇ vanishes on K to n ≤ 60. This supports T-U7; it does not prove it.

### A6: U/V operators at 2 and 7 on K
- **A6-a. U(4) on K. CONDITIONAL on T-U4** (Shimura 1973, Prop. 1.5, m = 4: U(4) preserves S_{3/2}(Γ₀(196), χ₂₈); cited and not verified).
  - **Exact identity (oa_v8):** U(4)G_j = Σ_i U4[j,i]G_i holds for all n ≤ 100, which exceeds the Sturm bound 42 of V. Consistency (oa_v9): U(4)(V) ⊂ V on n ≤ 60.
  - In the row-reduced basis (G₁, G₂, G₃, G₄), U(4) is block diagonal:
    - [[0, −2], [1, 1]] on span{G₁, G₂};
    - [[−1, 2], [−2, 2]] on span{G₃, G₄}.
  - **charpoly = (x² − x + 2)².** Its eigenvalues are (1 ± √−7)/2, the Frobenius roots of f at 2 (a₂(f) = 1, x² − a₂x + 2). So K = two U(4)-stable planes, each carrying the 2-stabilisation pair of f.
  - The 4×4 matrix and its charpoly are exact. Their meaning as an operator on all n is COND on T-U4.
- **A6-b. PROVED (exact): K ∩ S⁺ = span{G₁, G₄} is not U(4)-stable.** rank[Plc; Plc·U4] = 4 on truncated coefficients, and a truncation that leaves the span already proves non-membership. This is consistent with Kohnen's projection using U(4)W(4) rather than U(4) alone.
- **A6-c. U(7) and U(49) vanish on K. CONDITIONAL on T-U7** (immediate from A5).
- **A6-d. Not applicable:**
  - U(2) is not an endomorphism of V, because 8 ∤ 196: its image has level 392 and character χ₂₈χ₈. Not computed.
  - V(2), V(4) and V(7) raise the level, so they are not endomorphisms of K.

### P10 (dropped from the queue; PROVED by PP)
- P10 is **PROVED** by PP's H-PP (pp_gamma20_H 5187e2c0…/4b7a7c35…) and pp_gamma0_49_onto (8b0a17aa…), as graded in ac9fe667.
- Local's p25_level20_H_exact_v3 was launched before that instruction and is filed as an independent, uncounted cross-check:
  - exact in ℚ(ζ₂₀);
  - [SL₂(ℤ):Γ(4)] = 48 with 36 Schreier generators, and [SL₂(ℤ):Γ(5)] = 120 with 71;
  - ρ(g) = I on all of them.

### O-b calibration (new; scoped, exact, computer-assisted)
ob_calib_v1 asks at which 2-power level a weight-3/2 preimage of E⊗χ₋₄ appears, for curves good at 2. The same joint-kernel test is used with the first three odd primes not dividing the level, and all PARI-admissible even quadratic D.
- **CAL-1. PROVED (scoped): 15a1⊗χ₋₄ (conductor 240) gives a nonzero joint kernel already at 4M = 480 = 2·240**, with dimension 4 for every D ∈ {1, 8, 60, 120}. The kernel is 6 or 12 at 960 and 14 at 1920. So the method does detect χ₋₄-twist preimages.
  - "Kernel ≠ 0" is exact.
  - That it is exactly 15a1⊗χ₋₄'s eigensystem for all p is not claimed (only 3 primes are used).
- **CAL-2. PROVED (scoped null): 11a1⊗χ₋₄ (conductor 176) has joint kernel 0 at 4M = 2⁵·11, 2⁶·11, 2⁷·11 and 2⁸·11, for D ∈ {1, 8, 44, 88}.**
- The run ended with a PARI stack overflow at 15a1, N = 3840 (log kept). No rerun was needed for this addendum.
- **OPEN (interpretation):** why 49a1⊗χ₋₄ and 11a1⊗χ₋₄ have no preimage at these levels while 15a1⊗χ₋₄ does.
  - Candidate: a Waldspurger local-sign obstruction. ε(49a1⊗χ₋₄) = χ₋₄(−49)·ε(49a1) = −1, while ε(15a1⊗χ₋₄) = +1.
  - The 11a1 case also has + sign, so sign alone does not explain it; the 2-adic data a₂ = −2, −1, +1 differ.
  - This bears on whether level 12544 can succeed, and it argues for the ternary-theta route (§4).

## 2. PP fixes applied, by reference to e28e0fbd

### ac9fe667 (2025), Fixes 1–16
1. **A2:** C1 is PROVED by PP (C1-PP, pp_c1_formal df60d181…/421f050e…). **A2 = N1 is CONDITIONAL on C2 and C3** (C3 widened in 69d33456 to include T_p-stability of S₂(Γ₀(49)) and M₂(Γ₀(98))).
2. **C2 citation:** for weight 3/2 at level 2N it is **Cipra, Nagoya Math. J. 91 (1983)** (also Kojima, Flicker, Gelbart–Piatetski-Shapiro), and it is needed for non-eigen F. "Niwa 1975" is withdrawn for weight 3/2.
3. **C3:** Shimura 1973 §1 is the source of G = T(p²)F − a_pF ∈ V.
4. **A3:** the mod-7 clause is withdrawn (§0.2).
   - Plus-space convention: PARI's `mfkohnenbasis` means c(n) = 0 unless n ≡ 0, 1 (mod 4), via χ·(−4/·) = χ₋₇.
   - "Multiplicity 2 vs Kohnen's squarefree isomorphism" is a **remark**, not a theorem.
   - A3 otherwise stays PROVED.
5. **A5 path:** followed (§1). A5 is CONDITIONAL on T-U7.
6. **A4:** CONDITIONAL on C2 (exact for n ≤ 30).
7. **B2 is split.**
   - B2 lemma: CONDITIONAL on twist modularity (Shimura 1973, Lemma 3.6).
   - B2′ consequence: Ξ's eigensystem is not a twist of K. **PROVED** (5bf1e1dc). CM step: a_p(f) = 0 at inert p (from θ_ψ, PROVED in 5bf1e1dc), so ψ² ∈ {χ₋₂₀, χ₁₄₀} on split primes, and both are non-squares by B1.
8. **B3:** CONDITIONAL on the same twist lemma. "Reduces to" means a sufficient reduction only.
9. **B4 scope:** the joint kernel is 0 in S_{3/2}(Γ₀(4M), χ_D) for 4M ∈ {1568, 3136} and the 8 quadratic D only; other levels and characters are not covered. In B6, "2-power level ≤ 2⁶" reads **"4M = 2⁵·49 and 2⁶·49"**.
10. **B5:** PENDING. Times 19:51 → ≤ ~22:21 (§0.3). Status in §3.
11. **B6:** "years of CPU time" reads **"≈ 0.4–2 CPU-years by cubic extrapolation (estimate, not a bound)"**.
12. **P8:** stated on the **Weil–Deligne/Galois side** (per 69d33456 §5 and 5bf1e1dc).
    - σ_p(Ξ) = σ_p(f)⊗χ_p for p = 2, 5, with σ_p(f) unramified at good p.
    - ε of the sum of two characters is the product of Tate's GL₁ constants, using ε(χμ) = μ(ϖ)^{a(χ)}ε(χ) and ε(χ)ε(χ⁻¹) = χ(−1).
    - This gives ε₂ = χ₋₄(−1) = −1 and ε₅ = (−1/5) = +1, with a = 2a(χ). PROVED, confirmed by the exact P7.
13. **P10:** PROVED via H-PP (§1).
14. **Header:** 20:00 CST (§0.1).
15. **Rollup:** superseded by 5bf1e1dc (§5).
16. **E11a/E11b:** split kept, curve named at each certificate citation (§2, 5bf1e1dc).

### 69d33456 (2030), Fixes 1–5, as overridden by 5bf1e1dc
1. Condition tags are carried on every regraded row (§4 table).
2. **3b-ii is two rows:**
   - (a) PROVED: PARI `mfshimura` disagrees with Shimura's defining formula for S₃(K₁).
   - (b) the refutation of "K is not exactly f-isotypic": CONDITIONAL on C2 and C3.
3. **2g** is re-based on pp_2g_980 (6f76e8d5…/6420ff31…): PROVED with no citation (rank 145 → 146 in S₂(Γ₀(980)), 192 → 193 in M₂).
4. **P8** is stated on the Weil–Deligne side (above).
5. **E11b:** wording per 5bf1e1dc (below).

### 5bf1e1dc (2050), Fixes 1–5 (final wording)
1. Grades and tags as in the §4 table.
2. **Modularity:** cite 5bf1e1dc and /workspace/audit-scratch/pp_tmod_49a1/ (pp_cm_49a1_v2 b664ed61/2142b0fe; pp_theta_psi_gamma0_49_v2 ff6b3f50/2ffc6081; pp_tmod_arith 68bf6843/93a78b46; pp_tmod_twists_v2 831e440e/0fdf3195) for 49a1 and its 11 twists. **"Deuring–Hecke/BCDT cited" is dropped.** The base F0 (Silverman AEC, Poisson summation, h(−7) = 1) is the stated untagged base.
3. **E1 (ε = −w_N)** is stated **only for the instances proved: 49a1, Ξ = elltwist(49a1,140), and the nine N2 twists.** No general claim for all E.
4. **N2 (curves E^D for D ∈ {40, 44, 53, 57, 172, 188, 248, 264, 316}):** ε = +1 PROVED; L(1) = 0 CONDITIONAL on Kolyvagin / Coates–Wiles (T-GZK).
5. **E11b:** analytic rank 1 (**Ξ**) and 0 (**49a1**), PROVED on base F0, via the arb certificate 320c8c7e (pp_j3_lvalues_arb) with L′(Ξ,1) ∈ [4.43262273168641616 ± 2e−20] and L(49a1,1) ∈ [0.96665585280840577 ± 3.5e−21]. No GZK used. E11a (lfuncheckfeq, a float check) stays CONDITIONAL. This overrides the 2030 COND wording.

## 3. O-b status (B5)
- **ob_v2 (level 6272 = 2⁷·49):**
  - D = 1: dim 390, joint kernel 0 (673 s).
  - D = 8: dim 390, joint kernel 0 (620 s).
  - D = −4, −8, −7, −56: space dim 0.
  - **D = 28 and D = 56 (dim 388): not finished.** The process ended before 21:41 CST with no further log line; cause not recorded.
  - Log hashed now: ob_v2.log **29036a3c832f4002…** (sidecar), not edited.
- **ob_v3_6272_D28_D56.py (31b687a4b240e8e9…):** started 21:41 CST in the background with a 6e9 PARI stack and timeout 10800 s, for the two remaining characters. Its log will be hashed in a separate new dated file when it closes.
- **B5: PENDING.**
  - D = 1, 8 at 6272: **PROVED (scoped null)**.
  - D = 28, 56: running.
- **O-b: OPEN.** Fallbacks in t4429 order, after this addendum: (i) ternary theta, then (ii) level 12544.

## 4. Per-row grades carried (governing file 5bf1e1dc; Local rows from this addendum added)
| Row | Grade | Tag / basis |
|---|---|---|
| E1 ε = −w_N, **only for 49a1, Ξ and the 9 N2 twists** | PROVED | 5bf1e1dc |
| E2, E4, E5 | PROVED | 5bf1e1dc V9 |
| E3, E6, E7, E8, E10 | PROVED | exact |
| E9 "same newform" | CONDITIONAL | T-AL-new |
| E11a lfuncheckfeq | CONDITIONAL | float |
| E11b analytic rank 1 (Ξ), 0 (49a1) | PROVED | 320c8c7e + 5bf1e1dc; no GZK |
| 2a, 2c, 2d | PROVED | 5bf1e1dc |
| 2b, 2f′ | CONDITIONAL | T-theta |
| 2f (refutation) | CONDITIONAL | T-theta |
| 2e | REFUTED | coefficient argument |
| 2g | PROVED | pp_2g_980, no citation |
| 3a, 3c, 4a, 4a-c, 4b, 2/5 | PROVED | exact / elementary |
| 3b-i, A4 | CONDITIONAL | C2 |
| 3b-ii(a) | PROVED | exact discrepancy |
| 3b-ii(b), N1 = A2, O-a | CONDITIONAL | C2 + C3 |
| 3d | CONDITIONAL | float |
| N2 (9 curves E^D) | ε = +1 PROVED; L(1) = 0 CONDITIONAL | T-GZK (Kolyvagin / Coates–Wiles) |
| A1, C1-PP, A3, B1, B2′, B4, 4a-L, P1–P10, H-PP | PROVED | exact (B2′ per 5bf1e1dc) |
| B2, B3 | CONDITIONAL | twist lemma (Shimura 1973 Lemma 3.6) |
| B5 | PENDING | §3 |
| O-b, O-c, H₊U, Λ₀, P11 | OPEN | — |
| **A5** (new grade) | **CONDITIONAL** | **T-U7** |
| **A6-a** U(4) block form, charpoly (x²−x+2)² | **CONDITIONAL** | **T-U4** |
| **A6-b** plus∩K not U(4)-stable | **PROVED** | exact |
| **A6-c** U(7) = U(49) = 0 on K | **CONDITIONAL** | **T-U7** |
| **CAL-1, CAL-2** | **PROVED (scoped)** | exact |

## 5. Rollup
- **Governing (PP 5bf1e1dc, 61 rows): PROVED 38 · CONDITIONAL 14 · OPEN 7 · REFUTED 1 · PENDING 1, plus 1 Owner decision (V₈₄).** This replaces 29/23/7/1/1, 42/7/7/3/1 and 24/3/6/3.
- **Local proposal for PP (not self-certified):** this addendum would change the governing rollup as follows.
  - A5: OPEN → CONDITIONAL (T-U7).
  - A6: OPEN → CONDITIONAL, as row A6-a (T-U4). A6-c (T-U7) is folded into A6.
  - New rows: A6-b, CAL-1 and CAL-2, all PROVED.
  - **Provisional: 41 · 16 · 5 · 1 · 1 + V₈₄ (64 rows), pending PP's audit.**

## 6. Evidence (evidence_local_t4407_computations_2026-11-09/; new sidecars this session)
| File | sha256 (first 16 hex) |
|---|---|
| oa_v8_a5_a6.py | 1ef573881a0ff578 |
| oa_v8_a5_a6.log | 45713d8a0ef40e73 |
| oa_v9_u7_check.py | 5e0f097d18392387 |
| oa_v9_u7_check.log | 87deb23585d833c8 |
| p25_level20_H_exact_v3.py | bc7252adc6d47cc0 |
| p25_level20_H_exact_v3.log | a8a8f57a75283b60 |
| ob_calib_v1.py | 22703a32dba8d6a0 |
| ob_calib_v1.log (ended by PARI stack overflow; kept) | 075880055e12959d |
| ob_v2.log (partial; kept) | 29036a3c832f4002 |
| ob_v3_6272_D28_D56.py | 31b687a4b240e8e9 |
| ob_v3_6272_D28_D56.log | running; no sidecar yet |

All 25 earlier sidecars are unchanged. No file was deleted, renamed, moved or overwritten.

Local-derived. For PP audit. Nothing adopted. No CERT. Tip 7cddb188 untouched. Nothing sent outside.
