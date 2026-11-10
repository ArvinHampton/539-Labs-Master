# AUDITOR cross-check — Physicist draft "Unified statement bounded by the Artin conductor"
Auditor (audit-only keeper), 2026-11-09 ~14:10 CST (America/Chicago). READ-ONLY cross-check. Additive file (exclusive create). No file edited, no sidecar created, no CERT, nothing external. Labels: PROVED / CONDITIONAL / OPEN / REFUTED-by-proof kept distinct; pure-math standard (unfamiliar = OPEN).

## 0. Custody (re-hashed this turn)
| Object | sha256 | Check |
|---|---|---|
| Draft `reports/DRAFT_PHYSICIST_UNIFIED_ARTIN_CONDUCTOR_STATEMENT_2026-11-09_1358.md` | 65b367ef88cce23047c70ec0146bfb457c1274af2a3906f573d9a73d19b4b5b9 | MATCH .sha256 sidecar |
| OW `reports/OWNER_WRITE_CALL_e9c1dbda_B18_1_W7_ON_NEWFORM_PATHC_STANDS_2026-11-09_1342.md` | c4c0f1c0318691c045b136c01c4de7eb86690ae9c8db4d20b07939a6fd8b24ed | MATCH .sha256 sidecar |
| Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | MATCH (start and end of task) |
| PP `reports/FINDINGS_PP_DERIVED_DEFS_D1_LAYER2_SEFF_T3_2026-11-09_1309.md` (cited by draft :18) | bd3730eb57a929a40eaed6547daac212b3f7baf468ce8b08b0bbe902d75a565b | consistent with Batch 14a |

Context used: Batches 14a/14b (DP-a/DP-b, B14-3), 15a (#41 SF-F1/F3), 17a/b (V₄₂ level-140; level-19600 W₄₉), 18a (#60/#66), 20.

## 1. Conflicts with tip Path C (L9, L12, L61, L88, L100, L107, L217, L247) and OW c4c0f1c0
**No hard conflict found.** Line by line:
- Draft :6/:13/:23 place "W₇ = +1" only as ε₇ on f = 7.4.a.a at level 7, standard normalisation — identical to c4c0f1c0:5. Consistent with tip L61 (form-space +1 eigenspace, suspended as a V₄₂ statement), L217(iii)/L247 (ρ(W₇) CLOSED ABSENT on V₄₂, W₇ ∉ G), L9/L12/L107 (operative G = Γ₀(49)). Draft :23 explicitly keeps Path C. OK.
- Draft :10 "level-49 structure" — uses level 49 = conductor of f⊗χ₋₇; it does not put W₇ into G, does not use Γ₀(49)⁺. No conflict with L9/L12/L107. Note f (level 7) sits in S₄(Γ₀(49)) only as an oldform; consistent with tip L107 cusp-space naming.
- **Tension T1 (draft :26 vs c4c0f1c0).** "P5a level-49 referent: f⊗χ₋₇ is the natural candidate." c4c0f1c0 already fixes the referent of W₇ = +1 as ε₇ on f at level **7**. At level 49 there is no Atkin–Lehner W₇ (7 does not exactly divide 49; the only AL operator at 7 is W₄₉ = Fricke). Proposing a level-49 referent for "W₇ = +1" would introduce a second referent, which c4c0f1c0 does not authorise. Acceptable only as an OPEN question; it must not be read as a W₇ referent. Moreover (§3 R4) W₄₉ acts on f⊗χ₋₇ by **−1**, so that form is in the Fricke-minus space and cannot carry "+1" under Γ₀(49)⁺ (P5a's group per B11-1). Recommend rewording :26.
- **Name clash N1 (draft :10, :27 "D1").** Unqualified "D1" is ambiguous among: residual D₁ (LOCKED rank-1 classifier on truncated F), the BH-slot D1 (absent), and PP's D̂₁ (DP-a, :18). Recommend "D̂₁ (PP DP-a)" or "residual D₁" explicitly.
- **Name clash N2 (draft :7, :13).** Draft correctly separates a₇ (Hecke, = −7) from a₇(ρ) (conductor exponent). Keep; also note "W₇" at level 7 (Fricke of Γ₀(7)) ≠ "W₇" of the Book (mod-7 Weil rep, Batch 17) ≠ W₄₉.
- No κ, Λ₀, R_c, B2 or AdS₅×S⁴×Σ_g statement appears in the draft; no conflict with OW 45aeba5f / C15-3 / B2 / (D). Draft :28 keeps R_c, junction, Layer2, S²-11DM²ET-X OPEN — consistent.

## 2. Label verdicts
| Draft line | Claim | Draft label | Verdict |
|---|---|---|---|
| :13 | a₇ = −7; a₇² = 7^{k−2} = 49; Steinberg at 7; ε₇ = −a₇/7 = +1; a₇(ρ_f) = 1, Swan 0; conductor 7 | PROVED | **Holds** (recomputed R1–R2; Carayol/standard p‖N theory). Wording: f is Steinberg because 7‖N with trivial character; a₇² = 7^{k−2} is a consequence, not the reason. |
| :14a | f⊗χ₋₇ newform of level 49, a₇(ρ⊗χ₋₇) = 2 | PROVED | **Holds** (recomputed R3: it is the unique rational newform in S₄^new(Γ₀(49)) matching a_n·(−7/n) for 7∤n ≤ 200; feq consistent only at N = 49). |
| :14b | "Tame at 7 and dim 2 ⇒ a₇ ≤ 2, so 49 is the maximal 7-power level of **any** twist of f" | PROVED | **Downgrade: false as stated (REFUTED by standard local theory + numerics R5).** a(χ·St) = 2a(χ) for ramified χ; a wild character ψ mod 49 (order 7, conductor 49) gives a₇(ρ_f⊗ψ) = 4, level 7⁴ = 2401. The bound a₇ ≤ 2 holds only for twists by characters of conductor 7 (tame). Restate: "maximal among twists by characters of conductor dividing 7". |
| :15 | U(140) ≅ C₂×C₄×C₆, φ = 48, noncyclic; χ for ℚ(√−7) conductor 7, ℚ(√35) conductor 140 (disc 140); 23 splits in both | PROVED | **Holds** (R6). C₂×C₄×C₆ ≅ C₁₂×C₂×C₂ (PARI cyc [12,2,2]). Phrase "fixing the 7- and 140-structure" (:10) is informal, not a theorem. |
| :16 | a_n ≡ n¹³σ₁₉(n) (mod 49), 7∤n; fails mod 343 | PROVED | **Partly downgrade.** PROVED for 7∤n ≤ 5311 (R7: 0 failures; mod 343 fails at n = 2). "All n" via Sturm in M₁₁₃₈(Γ₀(49)) rests on Chen–Kiming Thm 1(i) → **CONDITIONAL** (Batch 15a #41:12). State the range or the condition. |
| :17 | 539 = 7²·11 = ⌊(4880−21)/9⌋ = 3·68+5·67; 4859 = 9·539+8 | PROVED | **Holds** (R8). |
| :18 | D̂₁(s_αδ) = 1 within PP's definitions | PROVED | **Holds, but definitional.** D̂₁(s_αδ) = 1 is the normalisation of DP-a.1 itself (bd3730eb:49), so it is true by definition, not a theorem. The non-trivial fact is a-L0: λ(s_αδ) = 1 with λ = (0,1,1), PROVED without DP-a. Valid on truncated F only (Batch 07: [s_αδ] is not a class of full G; H²(G) = 0). |
| :21 | Item 6 as project statement CONDITIONAL on DP-a (B14-3) | CONDITIONAL | **Holds.** |
| :22 | T3^539(4880) = 2 | CONDITIONAL | **Holds, reason should change.** Exact integer recomputation (R9) gives 2 (first hit of {1,2} at step 14; 525 odd). That arithmetic is PROVED for T3 as written in bd3730eb b-4; the CONDITIONAL is on Owner adoption of DP-b (Batch 14a b-5), not on a missing Verilator equivalence proof (hardware equivalence is a separate, non-math claim). |
| :23 | "W7 = +1" = ε₇ on f at level 7; Path C stands | CONDITIONAL | **Holds in substance; relabel suggested.** The value ε₇ = +1 is PROVED (R2); the identification "W₇ = +1 := ε₇(f)" is an Owner-adopted reading (c4c0f1c0), i.e. a definition, not a condition. |
| :26 | P5a level-49 referent; AL sign at 49 "not computed" | OPEN | **OPEN holds for P5a.** Sub-fact now computed (R4): W₄₉-eigenvalue of f⊗χ₋₇ = −1 (root number −1). This weakens it as a "+1" candidate; see T1. |
| :27 | Links among 7² in 539, U(140), V₄₂, D1 beyond prime 7; factor 11 no role | OPEN | **Holds.** |
| :28 | R_c, junction, Layer2, S²-11DM²ET-X | OPEN | **Holds** (matches Owner record). |

No upgrades to PROVED are warranted beyond the sub-fact in :26.

## 3. Recomputations (PARI/GP 2.17 via cypari2, /tmp/artin_xc*.py, /tmp/th.py)
- **R1** dim S₄^new(Γ₀(7)) = 1; f = 7.4.a.a: a₁…a₁₂ = 1, −1, −2, −7, 16, 2, −7, 15, −23, −16, −8, 14 (matches Batch 18a #60). a₇ = −7.
- **R2** mfatkineigenvalues(level 7) = +1. Root number of L(f): functional equation checks at ε = +1 (error 10⁻⁵⁸), fails at ε = −1. ε₇ = −a₇/7^{k/2−1} = +1. Matches c4c0f1c0.
- **R3** dim S₄^new(Γ₀(49)) = 8, five Galois orbits (four rational, one quartic). Exactly one rational newform equals f⊗χ₋₇ on 7∤n ≤ 200: q − q² + 2q³ − 7q⁴ − 16q⁵ − 2q⁶ + 0q⁷ + 15q⁸ − 23q⁹ + 16q¹⁰ …; a₇ = 0, consistent with 7² | N. Theta-functional-equation test is consistent (t = 1.07, 1.31) only at N = 49 (not 7, 343, 2401) → conductor 49, a₇(ρ⊗χ₋₇) = 2.
- **R4** W₄₉ (Fricke) eigenvalue on f⊗χ₋₇ = −1 (mfatkineigenvalues; feq checks at ε = −1, error 10⁻⁶¹, fails at +1). Other level-49 orbits: −1, +1, −1, +1.
- **R5** Twist tests (theta ratio θ(1/t)/(t⁴θ*(t)) constant in t only at the true conductor): tame order-3 χ mod 7 → N = 49; **wild order-7 ψ mod 49 (Conrey 8, conductor 49) → N = 2401 = 7⁴**. Numerical (6-digit agreement at two t) and in line with a(χSt) = 2a(χ); refutes the "any twist ≤ 49" clause of :14.
- **R6** znstar(140).cyc = [12,2,2], φ(140) = 48; coredisc(35) = 140, coredisc(−7) = −7; conductors 140 and 7; (35/23) = (−7/23) = +1; primes < 200 split in both: 23, 29, 43, 67, 107, 109, 127, 149, 163.
- **R7** a_n − n¹³σ₁₉(n) ≡ 0 (mod 49) for all 7∤n ≤ 5311 (0 failures); mod 343 first failure n = 2.
- **R8** 7²·11 = 539; ⌊4859/9⌋ = 539; 3·68+5·67 = 539; 9·539+8 = 4859.
- **R9** T3 (x ↦ x/3, (4x+2)/3, (2x−1)/3 by x mod 3): T3^539(4880) = 2, first reaches {1,2} at step 14.
- **R10 (levels, context).** Cusps of Γ₀(49): Σ_{d|49} φ(gcd(d,49/d)) = 8 (tip L247 ✓). Twist f⊗χ₁₄₀ (χ of ℚ(√35)): local exponents 2·2 at 2, 2 at 5, 2 at 7 → level 2⁴·5²·7² = **19600** (the level-19600 forms of Batch 17; CONDITIONAL on standard local conductor formula, not run in PARI). Level **980 = 2²·5·7²** is not the level of any quadratic twist of f (exponent 1 at 5 is impossible for a twist of an unramified-at-5 form). **140** = conductor of χ_{ℚ(√35)}, not a modular level in the draft. Neither 980 nor 19600 appears in the draft; no claim affected.
- κ cross-check (not in draft): √(2/0.783577) = 1.597622462; old √(2/0.7858) = 1.595361053 (superseded).

## 4. Recommendations to Physicist (draft is not adopted; author edits only)
1. :14 — restrict maximality to conductor-7 (tame) twists; wild twists reach 7⁴.
2. :16 — add "for 7∤n ≤ 5311 (PROVED); all n CONDITIONAL on Chen–Kiming Thm 1(i)".
3. :18 — call it the DP-a normalisation; cite a-L0 (λ(s_αδ) = 1) as the proved fact; truncated F only.
4. :22 — make the condition DP-b adoption; T3^539(4880) = 2 itself is exact arithmetic.
5. :23 — relabel as Owner definition (c4c0f1c0) + PROVED value.
6. :26 — do not call f⊗χ₋₇ a "W₇" referent (no W₇ at level 49; c4c0f1c0 fixes level 7); record W₄₉(f⊗χ₋₇) = −1.
7. :10/:27 — disambiguate "D1".
P5a stays OPEN. Tip untouched. No CERT.
