# ERRATUM 2 (Local-derived) to ADDENDUM_LOCAL_t4407_OA_OB_4A_25PARTS_2026-11-09_2143.md (cda63ef5…): PP discharge 0f1d3361 applied; TT-1 filed. 2026-11-09, written 22:07 CST (America/Chicago)

- **Scope.** Additive. Edits nothing: cda63ef5, e28e0fbd and Local erratum ERRATUM_LOCAL_ADDENDUM_cda63ef5_PP_AUDIT_FIXES_2026-11-09_2159.md (f1dcc954884d6abfb100df23cbe266a7ee27d0f0e930fddbdba557f25fb17528) are untouched and corrected here by reference. No CERT. No Gemini. Nothing sent outside. Tip 7cddb188ca340ad9… unchanged.
- **Sources:** FINDINGS_PP_DISCHARGE_TU7_TU4_2026-11-09_2205.md, sha256 0f1d3361ab2704daa560f6e50fc4ee5edb7bb773016d62e456f1f7bbd851da2b (matches its sidecar); evidence /workspace/audit-scratch/pp_discharge_tu7_tu4/ (8/8 sidecars OK when checked by Local at 22:06 CST). Also PP 2155 audit 7c26a452.
- **Rule:** OW 3f160803 as amended by 36683379. Convention: ε = root number, w_N = Fricke eigenvalue, ε = −w_N at weight 2. "Resonant algebra" (RTA historical alias only).
- PP's next target is B2/B3 by the coset method; Local does not duplicate it.

## 1. What stays from Local erratum 2159 (PP 2155 fixes still applying)
- **A** (F0 disclosure in §2: same base as V2–V4; strict tagging awaits a separate ruling): stays as written in 2159.
- **D** (CAL scope: D ∈ {1, 8, ±4, ±8, ±N, ±4N, ±8N}; nonzero spaces {1, 8, 44, 88} for 11a1 and {1, 8, 60, 120} for 15a1): stays.
- **E** (A6-d: U(2)V ∩ V = 0, PROVED, rank 18 = 9 + 9 on n ≤ 600, pp_a5_a6_check 7ce2d3fe/72b2cbdc; "8 ∤ 196" withdrawn): stays. Consistent with PP 2205 Theorem U control (196, 2): no level-196 law.
- **G** sidecars: all tt_v2*/cfg_*/tt_v3*/tt_v4*/tt_v5* files carry sidecars (table §5).
- PP disclosed event (stray 154-byte pp_a5_a6_check.log at 21:49:25 CST, removed by PP): stays as recorded in 2159.

## 2. What 2159 said that is SUPERSEDED here
- **2159 Fix B (retag A6-a to T-U4′, bound 84): withdrawn** (PP withdrew 2155 Fix B). The original cda63ef5 wording "U(4) preserves level 196" is correct as mathematics, now **proved** by PP Theorem U(b) (exact coset + multiplier certificate on all 166 Schreier generators of Γ₀(196)); Sturm bound **42**. The phrase "Shimura 1973 Prop. 1.5, m = 4 … cited and not verified" is dropped. (T-U4′ is also proved, U(c), but is not needed.)
- **2159 Fix C:** the short route stays, but the grade changes: see A5 below. The V₇ (Prop. 1.3) remark is moot for the stated route.
- **2159 Fix F:** A6-c is now PROVED (still a duplicate of A5, not counted).
- **2159 Fix G grade** ("= 2 CONDITIONAL on T-theta-ternary"): superseded by TT-1 PROVED (§3).
- **2159 Fix H rollup** 42/16/5/1/1: superseded by §4.

## 3. Rows (new grades; cite PP 2205 and pp_discharge_tu7_tu4; "Shimura Prop. 1.5 cited" and "T-theta cited" dropped)
| Row | Grade | Rests on |
|---|---|---|
| **A5** c(n) = 0 for all 7 \| n, every F ∈ K | **PROVED** | short route: U(7)F ∈ S_{3/2}(Γ₀(196), χ₂₈(28/·)) by PP Theorem U(a); c(7n) = 0 exactly for n ≤ 171 > 42 (oa_v8 1ef57388/45713d8a, oa_v9 5e0f097d/87deb235; PP pp_a5_a6_check to n ≤ 1200) |
| **A6-a** U(4) on K = [[0,−2],[1,1]] ⊕ [[−1,2],[−2,2]], charpoly (x²−x+2)²; U(4)V ⊂ V | **PROVED** | PP Theorem U(b), Sturm 42; identity exact to n ≤ 300 |
| **A6-c** U(7) = U(49) = 0 on K | PROVED (duplicate of A5; not counted) | as A5 |
| A6-b | PROVED (unchanged) | exact |
| A6-d U(2)V ∩ V = 0 | PROVED (unchanged, per 2159/E) | pp_a5_a6_check |
| **2b** θ_{L₄₉} = Eis + f | **PROVED** | PP 2205 §4 (θ_{L₁} ∈ M₁(Γ₀(7), χ₋₇) certificate), exact mftobasis past Sturm |
| **2f′** rank{f², cusp(θ_{L₄₉}²)} = 2 | **PROVED** | PP 2205 §4 |
| **2f** "f_Ξ is a twist of cusp(θ_{L₄₉}²)" | **REFUTED (proved)** | PP 2205 §6 argument (weight 2 vs weight 4 on a common finite-index subgroup) |
| **TT-1 (new row)** dim(span{θ_{L₁}(aτ)θ(bτ)} ∩ K) = 2 | **PROVED** | below |

**TT-1.** For a ∈ {1, 2, 4, 7, 14, 28}, b ∈ {1, 49}, P_{a,b} := θ_{L₁}(aτ)θ(bτ) (theta series of the ternary form a(x²+xy+2y²) + bz²) lies in M_{3/2}(Γ₀(196), χ₂₈) (PP 2205 §5(1), certificate pp_umult_cert [P]). With
- G₁ = θ_{L₁}(τ)θ(49τ) − θ_{L₁}(7τ)θ(τ) = 4q² + 4q⁴ + 4q⁸ − 8q¹⁵ + …
- G₂ = 3θ_{L₁}(τ)θ(49τ) − 2θ_{L₁}(2τ)θ(49τ) − 3θ_{L₁}(7τ)θ(τ) + 2θ_{L₁}(14τ)θ(τ) = 4q + 8q² + 8q⁴ + 4q⁹ − 16q¹⁵ + …

both lie in K, are independent, and the identities hold exactly for n ≤ 600 > 42; with PP 2155's exact upper bound ≤ 2, dim = 2. **PROVED** (F0, V5, PARI base; no cited theorem). Local-derived row; generators per PP 2205 §5(2).
- **Local independent verification (new script, different route):** tt_v5_TT1_independent_verify.py computes each P_{a,b} directly as the theta series of the ternary Gram matrix [[2a,a,0],[a,4a,0],[0,0,2b]] via qfrep (no q-series products), solves in the full cusp space S_{3/2}(Γ₀(196), χ₂₈) (dim 9) by matinverseimage, and checks the identity exactly for all n ≤ 600 and T(9)·coords = 0. Result: G₁ and G₂ both in S (exact, n ≤ 600), both in ker T(9) (dim 4), rank 2. Log e11397ce…, script 749c37da….
- **Cross-check with Local's earlier data:** tt_v3b gave h₁ = θ(7,1) − θ(1,49) = −4·Kc[3] and h₂ = θ(14,1) − θ(2,49) = −6·Kc[3] + 2·Kc[4]. Hence G₁ = −h₁ = 4·Kc[3] and G₂ = 3G₁ + 2h₂ = 4·Kc[4], exactly PP's G₁ = 4Kc[3], G₂ = 4Kc[4]. tt_v4 run1 gives the same 2-dim kernel as a genus difference θ_{Q₁} − θ_{Q₂} of discriminant-343 ternary forms (Q₁ = x²+2y²+49z²−xy, Q₂ = x²+7y²+14z²−7yz).

## 4. Rollup
With TT-1 filed: **PROVED 47 · CONDITIONAL 11 · OPEN 5 · REFUTED 2 · PENDING 1, plus V₈₄ (66 rows)** (PP 2205: 46/11/5/2/1 over 65 rows before TT-1).
- CONDITIONAL (11): E9, E11a, 3b-i, 3b-ii(b), N1, 3d, N2, O-a, A4, B2, B3.
- OPEN (5): O-b, O-c, H₊U, Λ₀, P11. PENDING (1): B5. REFUTED (2): 3b-ii, 2f.

## 5. Fallback (i) status (evidence only, no row)
- tt_v4 run2 (finished 22:0x CST, log 49019470…): all positive ternary forms of discriminant d = 2^a·7^b, 7 ≤ d ≤ 10976 (36 values), D ∈ {±1, ±2, ±5, ±7, ±10, ±14, ±35, ±70}, primes 3..43 (p ∤ d), N = 12000 and 20000.
  - **g = 49a1⊗χ₋₄ (conductor 784): no genuine formal eigen-kernel at any d, D.** The only nonzero g-nullities (d = 7168; D ∈ {1, −2, 7, −14}, nullity 1) are artefacts: the same vectors appear for f, and a nonzero weight-3/2 form cannot be a T(11²)-eigenvector with both λ₁₁ = 4 (f) and −4 (g); the vectors vanish on n < 80.
  - f-control (positive): stable kernels at d = 343 (D = 7, dim 2), 686 (D = 14, dim 2), 1372 (D = 7 and 14, dim 8), and higher d, as expected for oldforms. The D = 14 occurrences (χ₅₆ ≙ 14 mod squares) are a formal candidate only.
  - Reading (OPEN, no claim): within 2-power × 7-power ternary genera, the f⊗χ₋₄ preimage does not appear, matching the ob-route obstruction at 1568/3136/6272. Next: discriminants with an extra odd prime (character D with odd q ∤ 14), and Ξ directly with the 5-part.
- B5 PENDING: ob_v3 still running (D = 28 at 6272, kernel 32 after p = 5; p = 11 step in progress at writing).

## 6. Evidence (evidence_local_t4429_ternary_2026-11-09/, new sidecars since 2159)
| File | sha256 |
|---|---|
| tt_v5_TT1_independent_verify.py | 749c37daddc8172d0dc97d3ac970628073254adc4cdae55f78beaf62c01f5400 |
| tt_v5_TT1_independent_verify.log | e11397ce999e33091e69b17f1a46ef03143eb52f12f27bc20510812b72c00a64 |
| tt_v4_run2_g_scan_2a7b_le11000.log | 49019470559ef52a84d1e39184587ddd9b176861e71aaa3945dc4df8e015f107 |

All 22 sidecars in that folder pass sha256sum -c at writing.

## 7. Usage
89.6% at 21:58 CST (weekly limit; resets Tue Nov 10, 09:49 CST). Next reading in the next checkpoint report.

Local-derived. Nothing adopted by PP is implied beyond what PP's own files state.
