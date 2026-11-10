# FINDINGS (PP correction): citation-dependent grades in PP edcd9551 (1949), PP bc12df1a (1955) and the PP 2025 rollup. 2026-11-09, ~20:30 CST (America/Chicago)

- **Auditor:** Professor Proof (Soft SF). Audit only. Nothing adopted. No CERT. No Gemini. Nothing sent outside. This file is additive: edcd9551 (1949), bc12df1a (1955) and ac9fe667 (2025) are not edited.
- **Tip:** 7cddb188ca340ad9… matched before and after; read only.
- **Naming:** "resonant algebra" (OW 81b74a31); naming only.
- **Rule applied (PP ruling, Owner's rule OW 3f160803 as amended by 36683379):** a citation never makes a result PROVED by itself; the test is whether PP has verified the cited math. No Owner decision is needed. Every row that was PROVED only through a cited theorem PP has not verified becomes **CONDITIONAL on that named theorem**. This replaces the 1949 practice of "cited, hypotheses checked ⇒ PROVED".
- **Computational base (unchanged and stated openly):**
  - Exact outputs of PARI/GP 2.17.2 algorithms (mfinit, Hecke matrices, ellrootno, Tate's algorithm, Vélu, ellrank descent bounds) and of arb ball arithmetic count as exact computer-assisted results, not as citations.
  - A theorem that a tool assumes about an object it is handed is a citation. One example is `mffromqf` returning a theta series as an element of M_k.
- **New PP evidence:** /workspace/audit-scratch/pp_t4407_e28e0fbd/pp_2g_980.py / .log (6f76e8d5… / 6420ff31…, with sidecars).

## 1. Named theorems (cited, not verified by PP)
| Tag | Statement |
|---|---|
| **C2** | Shimura lift modularity in weight 3/2 at level 2N for arbitrary F. Here: S_t maps S_{3/2}(Γ₀(196), χ₂₈) into M₂(Γ₀(98)). Sources: Cipra 1983, Nagoya Math. J. 91; Kojima; Flicker; Gelbart–Piatetski-Shapiro |
| **C3** | Hecke stability: T(p²) preserves S_{3/2}(Γ₀(196), χ₂₈) (Shimura 1973, §1), and T_p preserves S₂(Γ₀(49)) and M₂(Γ₀(98)) (classical Hecke theory) |
| **T-mod** | Modularity of 49a1 and of its twists (Ξ, the −20 twist and the twists in N2), with L(E,s) = L(f_E,s) for a newform f_E of level N(E). The sign of the functional equation equals the root number ε(E) computed by ellrootno. All these curves have CM by ℚ(√−7), so Deuring–Hecke suffices; BCDT also covers them |
| **T-Hecke** | Hecke: the theta series of a Grössencharacter of an imaginary quadratic field is a modular newform. Here: ½Σ(α\|√−7)α q^{Nα} ∈ S₂(Γ₀(49)) |
| **T-theta** | Theta series of positive definite even lattices are modular (Hecke/Schoeneberg). Here: θ₁ ∈ M₁(Γ₀(7), χ₋₇), and θ_{L₄₉}, θ_{L₄₉}² lie in M₂(Γ₀(49)) and M₄(Γ₀(49)) |
| **T-tw** | Integral-weight twist modularity and level: R_χ f ∈ S₂(Γ₀(N·m²)) (Shimura Prop. 3.64) |
| **T-AL** | Atkin–Li 1978 twist law for the Fricke/root-number sign: w(f⊗χ) = χ(−N)·w(f) for conductor of χ prime to N |
| **T-GZK** | Gross–Zagier + Kolyvagin: analytic rank ≤ 1 implies algebraic rank equal to analytic rank |

**Verified by PP in this file** (short proofs recorded; these are no longer citations):
- **(V1) Hecke's functional-equation sign on the form side.** Λ(f,s) := N^{s/2}(2π)^{−s}Γ(s)L(f,s) = N^{s/2}∫₀^∞ f(iy)y^{s−1}dy. With f\|₂W_N = w_N·f, one has f(i/(Ny)) = −w_N·N·y²·f(iy). Substituting y ↦ 1/(Ny) gives Λ(f,s) = −w_N·Λ(f,2−s). So "sign of FE = −w_N" holds for newforms. Linking that sign to ellrootno's ε(E) is T-mod.
- **(V2) Isogeny invariance of a_p.** If φ: E → E′ is a degree-7 isogeny over ℚ and p ∤ 7N, then φ commutes with Frobenius, so (1 − π′)φ = φ(1 − π), so deg(1 − π′) = deg(1 − π), so #E(F_p) = #E′(F_p).
- **(V3) Quadratic-twist point counts.** a_p(E^D) = (D/p)·a_p(E) for good p.
- **(V4) Hasse's bound.** |a_p| ≤ 2√p, because deg is a positive definite quadratic form on End and gives the discriminant of 1 − π.
- **(V5) Sturm's theorem in integral weight.** Take the norm over the cosets to get a level-1 form, then apply the valence formula. This is used only where both sides are already known to be modular.
- **(V6) C1-PP** (2025 file §1): the formal Hecke equivariance of S_t.

## 2. Regrades: PP edcd9551 (1949), erratum c2e9b6fe rows
| Row | 1949 grade | Corrected grade | Exactly why |
|---|---|---|---|
| E1 ε = −w_N (weight 2) | PROVED (identity cited; level 49 checked) | **CONDITIONAL on T-mod** | The form-side identity is PROVED by V1. Here ε means ellrootno(E), and equating it with the FE sign of f_E is T-mod. At level 49 the check compares w₄₉(f) and ε(49a1); both values are computed exactly, but the link between them is the claim itself |
| E2 w₁₉₆₀₀ = −ε = +1 | PROVED | **CONDITIONAL on T-mod** | ε(Ξ) = −1 is exact (ellrootno). w₁₉₆₀₀ = +1 is deduced through E1 and was not computed directly |
| E3 (1,0;−1,1) = STS⁻¹ | PROVED | PROVED (unchanged) | hand computation and exact matrices |
| E4 XW L68 "both readings true" | PROVED | **CONDITIONAL on T-mod** | The ε-reading holds as an instance by exact computation: ε(Ξ) = −1, ε(49a1) = +1, χ₋₂₀(−49) = −1. The w-reading needs E1, hence T-mod. The general law (IK 14.20 / Atkin–Li, T-AL) is not needed for the instance |
| E5 w₁₉₆₀₀ = w₄₉·χ₋₂₀(−49) = +1 | PROVED | **CONDITIONAL on T-mod (or on T-AL)** | the w-side is deduced, not computed |
| E6 w₄₉ = −1, ε(49a1) = +1 | PROVED | PROVED (unchanged) | two separate exact computations (mfatkininit, ellrootno); no link is asserted |
| E7 table (a-invariants, conductors, ε, j) | PROVED | PROVED (unchanged) | Tate's algorithm, exact |
| E8 7-isogenous, not isomorphic | PROVED | PROVED (unchanged) | exact (ψ₇ factorization, Vélu, ellisisom) |
| E9 "same newform", a_n equal for n ≤ 7000 > Sturm bound | PROVED (modularity cited) | **CONDITIONAL on T-mod** | a_n(Ξ) = a_n(−20 twist) for all n is PROVED by V2 (for p ∤ 7N; at p \| N both a_p = 0 by the exact reduction types) together with multiplicativity. "Same newform" requires that a newform exists, which is T-mod |
| E10 χ₁₄₀ = χ₋₂₀χ₋₇ | PROVED | PROVED (unchanged) | exact over one period |
| E11a lfuncheckfeq | CONDITIONAL | CONDITIONAL (unchanged) | floating point |
| E11b (from bc12df1a) | PROVED | **CONDITIONAL on T-mod** | see §4 |

## 3. Regrades: PP edcd9551 (1949), Bridge C pass 9e34f2dc rows
| Row | 1949 grade | Corrected grade | Exactly why |
|---|---|---|---|
| 2a f = ½Σ(α\|√−7)α q^{Nα} | PROVED (Hecke cited) | **CONDITIONAL on T-Hecke** | coefficients agree for n ≤ 600 (exact). Equality for all n needs the theta series to be modular, then V5 |
| 2b θ_{L₄₉} = Eis + 1·f | PROVED | **CONDITIONAL on T-theta** | θ₁ was built with `mffromqf`; membership in M₂(Γ₀(49)) is the cited theorem. The linear algebra is exact |
| 2c f_Ξ = R_{χ₁₄₀}f = R_{χ₋₂₀}f | PROVED | **CONDITIONAL on T-mod and T-tw** | the Sturm comparison at level 19600 needs both sides to be modular there |
| 2d w₁₉₆₀₀(f_Ξ) = +1 | PROVED | **CONDITIONAL on T-AL (equivalently T-mod via E1)** | deduced, not computed |
| 2e f_Ξ ∉ span of the χ₁₄₀-twists of F₂ | REFUTED | REFUTED (unchanged) | the q¹ and q³ coefficients contradict it. This is a pure coefficient argument with no citation |
| 2f "f_Ξ is a twist of cusp(θ_{L₄₉}²)" | REFUTED | **CONDITIONAL on T-tw and T-theta** (a refutation that holds only if those theorems hold) | The weight argument needs f_Ξ to be weight-2 modular (T-tw) and cusp(θ²) to be weight-4 modular (T-theta). Given both, a nonzero form cannot be modular of weights 2 and 4: f\|γ forces (cz+d)² = 1. Without them no finite coefficient argument is available, because the twisting character is unrestricted |
| 2f′ rank{f², cusp(θ²)} = 2 in S₄(Γ₀(49)) | PROVED | **CONDITIONAL on T-theta** | "cusp(θ²)" is the S₄-projection of θ², which is defined only if θ² ∈ M₄. Linear independence of the two coefficient vectors as computed is exact |
| 2g f_Ξ ∉ S₂(Γ₀(980)) | PROVED (Atkin–Lehner–Li cited) | **PROVED, re-based with no citation** | New PP pp_2g_980 takes the q-series Σa_n(Ξ)qⁿ with a_n from the curve. Appending it to the basis-coefficient matrix for n ≤ 420 raises the rank from 145 to 146 in S₂(Γ₀(980)), and from 192 to 193 in M₂. So no element of either space has these coefficients. This is pure linear algebra; neither Sturm nor newform theory is needed |
| 3a dims, charpolys, Kohnen⁺, level-392/980 rows | PROVED | PROVED (unchanged) | exact computation |
| 3b-i t = 1 lifts of K lie in span{f, f(2τ)} | PROVED (Shimura cited) | **CONDITIONAL on C2** | exact for n ≤ 30. For all n it needs the lift to lie in M₂(Γ₀(98)) (C2), then V5 |
| 3b-ii (a) *new split row:* PARI's `mfshimura` values for S₃(K₁) (a₉ = −2, a₁₁ = −10, …) differ from Shimura's defining formula (a₉ = 0, a₁₁ = 0); the formula gives −2f(2τ) through n = 30 | (inside 3b-ii) | **PROVED** | S_t is defined by the explicit formula A_t(n) = Σ_{d\|n} χ₂₈(d)(−4/d)(t/d)c(tn²/d²), so the discrepancy is an exact computation with no citation. This stands as proved |
| 3b-ii (b) refutation of Local's stated claim "for t = 3, 5 a basis vector lifts outside span{f, f(2τ)}, so K is not exactly f-isotypic" | REFUTED | **CONDITIONAL on C2 and C3** (refuted only if C2 and C3 hold) | The explicit formula gives coefficients but not modularity. Showing S₃(K₁) ∈ span{f, f(2τ)} for all n needs C2 (then V5 with the n ≤ 30 match). Refuting the conclusion "K is not f-isotypic" means proving N1, which needs C2 and C3 (2025 file, A2). Without C2 the premise is undecided rather than false. The explicit-formula argument does not avoid C2, because no finite coefficient check can establish membership for all n |
| N1 K is f-isotypic | CONDITIONAL | CONDITIONAL on C2 and C3 (as in the 2025 file) | — |
| 3c c(35) = 0 on K; coredisc(35) = 140 | PROVED | PROVED (unchanged) | exact. The side remark "L(Ξ,1) = 0 forced by ε = −1" is a T-mod remark and not part of the claim |
| 3d 75/75 zero pattern | CONDITIONAL | CONDITIONAL (unchanged) | float |
| N2 nine twists with L(1) = 0 exactly | PROVED (GZK cited) | **CONDITIONAL on T-GZK and T-mod** | algebraic rank 2 is PROVED (ellrank [2,2], exact descent). L(1) = 0 needs T-mod (for the L-function and the sign ε = +1 giving even order) and T-GZK |
| 4a | PROVED | PROVED (unchanged) | PP exact certificate; no citation (the representation relations were verified) |
| 4a-c | PROVED | PROVED (unchanged) | exact; unitarity is verified in pp_4a_exact |
| 4b lemma | PROVED | PROVED (unchanged) | elementary. Its application to V₄₂ remains CONDITIONAL on tip §1u, as already noted |
| O-a | OPEN (1949) → CONDITIONAL (2025) | CONDITIONAL on C2 and C3 | — |
| 2/5 | OPEN (1949) → PROVED (2025, via P10) | PROVED (unchanged) | P10 and H-PP are exact and use no citation |

## 4. PP bc12df1a (1955) and E11b
- **E11b → CONDITIONAL on T-mod.**
  - The arb certificate itself is sound. Ball arithmetic is rigorous, and the tail bound uses |a_n| ≤ d(n)√n (V4 plus d(n) ≤ 2√n) and E₁(x) ≤ e^{−x}/x.
  - But both rapidly convergent series, L(E,1) = 2Σa_n/n·e^{−2πn/√N} and L′(E,1) = 2Σa_n/n·E₁(2πn/√N), come from the functional equation of L(E,s) with sign ε(E) at level N(E). That is T-mod. Without modularity, L(E,s) is not even known to continue to s = 1.
- **"Analytic rank of Ξ exactly 1" does not use Gross–Zagier or Kolyvagin.** Given T-mod, it follows from:
  - L(Ξ,1) = 0 exactly, because the sign is −1, so Λ(1) = −Λ(1);
  - L′(Ξ,1) ∈ [4.43262273168641616 ± 2e−20], which excludes 0.
  - This is a statement about analytic rank only. Nothing about algebraic rank is claimed, and T-GZK is needed only for that.
- **The same holds for L(49a1,1) ≠ 0 (analytic rank 0):** it is CONDITIONAL on T-mod alone.
- **Confirm rows C1–C4:**
  - C1 (sha), C2 (15/15 fixes faithful) and C3 (rollup arithmetic) are PROVED and unchanged; none of them cites a theorem.
  - **C4 ("the arb certificate upgrades E11") → CONDITIONAL on T-mod.**
  - bc12df1a's own tally goes from 4/0/0/0 to **3/1/0/0/0**.

## 5. Consequence for the 2025 file's rows (same rule)
- **B2′ ("Ξ's eigensystem is not a twist of K") → CONDITIONAL on T-Hecke.** The argument needs the zero set of a_p(f): 0 at inert p and nonzero at split p, so that ψ² ∈ {χ₋₂₀, χ₁₄₀}. That comes from f being the Grössencharacter theta series (2a, T-Hecke), or equivalently from Deuring together with T-mod.
- **A2 and N1:** C3 is read as stated in §1, which includes T_p-stability of S₂(Γ₀(49)). That is what makes f(τ) and f(2τ) T_p-eigen with eigenvalue a_p(f) for every p ∤ 14.
- **P8 stays PROVED, read on the Galois (Weil–Deligne) side.**
  - At good p, σ_p(E) is unramified (Néron–Ogg–Shafarevich; the reduction-injectivity proof is elementary and was checked).
  - σ(E^χ) = σ(E)⊗χ.
  - ε of a sum of characters is the product of Tate's GL₁ constants by definition.
  - The values are confirmed by the exact P7.
  - Local should state P8 on the Weil–Deligne side; the automorphic-side phrasing would need T-mod plus local–global compatibility.
- **Unchanged:** A1, C1-PP, A3, B1, B4, 4a-L, P1–P10 and H-PP stay PROVED (exact or elementary); A4, B2 and B3 stay CONDITIONAL.

## 6. Revised Local rollup (strict reading; replaces 42/7/7/3/1)
| Block | P | C | O | R | PENDING |
|---|---|---|---|---|---|
| Erratum c2e9b6fe: E1–E10, E11a, E11b (12 rows) | 5 (E3, E6, E7, E8, E10) | 7 (E1, E2, E4, E5, E9, E11a, E11b) | 0 | 0 | 0 |
| Bridge C 9e34f2dc + PP rows: 25 rows after splitting 3b-ii | 8 (2g, 3a, 3b-ii(a), 3c, 4a, 4a-c, 4b, 2/5) | 12 (2a, 2b, 2c, 2d, 2f, 2f′, 3b-i, 3b-ii(b), N1, 3d, N2, O-a) | 4 (O-b, O-c, H₊U, Λ₀) | 1 (2e) | 0 |
| 2025 new rows (duplicates excluded) | 16 (A1, C1-PP, A3, B1, B4, 4a-L, P1–P9, H-PP) | 4 (A4, B2, B2′, B3) | 3 (A5, A6, P11) | 0 | 1 (B5) |
| **Total** | **29** | **23** | **7** | **1** | **1** |

**Revised Local rollup: PROVED 29 · CONDITIONAL 23 · OPEN 7 · REFUTED 1 · PENDING 1, plus 1 Owner decision (V₈₄).** That is 61 rows; the previous count was 60, and the difference is the 3b-ii split.

The conditions recur, and most CONDITIONAL rows rest on one theorem:
- T-mod: 9 rows (E1, E2, E4, E5, E9, E11b, 2c, 2d, N2).
- C2/C3: 5 rows (3b-i, 3b-ii(b), N1, O-a, A4).
- T-theta: 3 rows (2b, 2f, 2f′).
- T-Hecke: 2 rows (2a, B2′).
- Twist lemmas: B2, B3, 2c, 2f.
- T-GZK: N2.
- Float: E11a, 3d.

So verifying T-mod for these CM curves (Deuring–Hecke) would move about 8 rows at once, and C2/C3 another 5. These are the high-value verification targets if the Owner wants them pursued.

## 7. Fixes for Local (additive; no existing file edited)
1. In the next additive file, carry the tags (T-mod, T-Hecke, T-theta, T-tw, T-AL, T-GZK, C2, C3) on every row listed in §2–§5, and use the rollup in §6.
2. Record 3b-ii as two rows: (a) PROVED computational discrepancy with PARI's `mfshimura`; (b) the refutation, CONDITIONAL on C2 and C3.
3. Re-base 2g on pp_2g_980 (6f76e8d5…/6420ff31…). It is PROVED with no citation.
4. State P8 on the Weil–Deligne side.
5. E11b: say "analytic rank 1 (Ξ), analytic rank 0 (49a1), CONDITIONAL on modularity (T-mod). No GZK is used; algebraic-rank statements are not claimed."

PP correction only. Nothing adopted. No CERT. Tip 7cddb188 untouched (read only). No external sends. No Gemini.
