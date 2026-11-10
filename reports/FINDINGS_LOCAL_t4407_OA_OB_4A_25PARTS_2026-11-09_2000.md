# FINDINGS (Local-derived): t4407 items O-a, O-b, 4a hardening, 2-/5-parts. 2026-11-09, written ~20:0x CST (America/Chicago)

- **Authority:** Owner t4407 "Pursue all for resolutions" (record OWNER_WRITE_MAINCHAT_t4407_…_1843.md, sha b0b9ae7f…, verified). Pure math only. Nothing adopted. No CERT. No Gemini. Nothing sent outside. Additive file. Tip 7cddb188… untouched (checked before and after).
- **Nomenclature (Owner f1d167d1 / OW 81b74a31):** the object formerly called RTA is the **resonant algebra** (name change only; "RTA" below only as historical alias in cross-references).
- **Convention:** ε = root number, w_N = Fricke eigenvalue, ε = −w_N at weight 2.
- **Builds on:** Local pass 9e34f2dc (1822) and its evidence dir (read only); PP audit FINDINGS_PP_AUDIT_LOCAL_ERRATUM_c2e9b6fe_AND_BRIDGEC_PASS_9e34f2dc_2026-11-09_1949.md (edcd9551…), folded in below; XW ae951f3e (dictionary §3).
- **Naming (PP Fix 8):** K := ker T(9) ⊂ V := S_{3/2}(Γ₀(196), χ₂₈) (PARI convention, CHI includes the θ-multiplier). K₁…K₄ = matker columns (PP's naming). G₁…G₄ = the row-reduced basis (pivots n = 1, 2, 3, 5); G₁ = q − 2q⁸ + q⁹ − 2q¹⁶ + … is the vector 9e34f2dc 3a called "F₁".
- **PP corrections accepted:** 3b-ii ("K not exactly f-isotypic") is REFUTED (PARI `mfshimura` mis-identified the lift; Shimura's formula gives S₃(K₁) = −2f(2τ), S₅(K₁) = f + f(2τ)). Local's oa_v7 reproduces both independently. 4a rests on PP's exact certificate.
- **Evidence:** evidence_local_t4407_computations_2026-11-09/ (all scripts/logs have .sha256 sidecars, except ob_v2.log which is still being written by a running job; see O-b). PARI 2.17.2 via cypari2, sympy, numpy; box only.

---
## Item O-a: the exact f-isotypic subspace (f = 49a1)

**A1. PROVED (exact, computer-assisted).** dim V = 9. Characteristic polynomials (oa_v2): T(9): x⁴(x−2)(x+2)³(x+4); T(25): x⁸(x+6); T(121): x⁴(x−4)⁴(x−12); T(169): x⁴(x−4)(x+4)³(x+14). K = ker T(9) has dim 4 and equals the joint kernel of T(p²) − a_p(f) for p ∈ {3,5,11,13,17,19,23,29,31,37} (Local), and for all p ≤ 59, p ∤ 14 (PP pp_3b4).

**A2. PROVED, citation-dependent (closes PP N1): T(p²)F = a_p(f)F for every F ∈ K and every prime p ∤ 14. Hence K is exactly the f-isotypic subspace of V.**
- Cited: (C1) Shimura 1973 (Ann. of Math. 97), Hecke equivariance S_t(F|T(p²)) = (S_tF)|T_p for p ∤ 4N·t, valid for arbitrary F (identity of Dirichlet series in the proof of the Main Theorem). (C2) S_t maps S_{k+1/2}(4N, χ) into M_{2k}(Γ₀(2N), χ²) (Shimura 1973 for k ≥ 1; level 2N by Niwa, Nagoya Math. J. 56, 1975). Hypotheses checked: k = 1, N = 49, χ² trivial, t squarefree. S_t is Shimura's defining formula A_t(n) = Σ_{d|n} χ₂₈(d)(−4/d)(t/d)·c(tn²/d²).
- Step 1 (finite, Sturm): for t ≤ 35 squarefree, S_t(K_j) ∈ span{f(τ), f(2τ)} exactly (PP pp_3b4: checked to n = 30 > Sturm bound 28 of M₂(Γ₀(98)), with C2). Local oa_v7 agrees on n ≤ 8 for t ∈ {1,2,3,5,6,10,13}.
- Step 2 (finite, exact): the truncated lift map Φ_T: V → ∏_{t∈T} ℂ⁸, F ↦ (A_t(n))_{t∈T, n≤8} has **rank 9 for T = {1,2,3}** (oa_v7). So Φ_{1,2,3} is injective on all of V.
- Step 3: let p ≥ 5, p ≠ 7, and F ∈ K. G := T(p²)F − a_pF lies in V (Hecke stability, Shimura 1973). For t ∈ {1,2,3}, p ∤ t, so by C1, S_t(G) = (T_p − a_p)S_tF = 0, because T_p acts by a_p on f(τ) and on f(2τ) (p odd, p ≠ 7). So Φ_{1,2,3}(G) = 0 and G = 0 by Step 2. For p = 3, T(9)K = 0 = a₃(f)K by the definition of K.
- Converse: every f-isotypic F has T(9)F = a₃(f)F = 0, so it lies in K. **K is the f-isotypic subspace, dim 4.**
- No eigensystem-isolation step is needed. That step was also verified: at level 98, a₃ is −2 for 14a, +2 for 98#1, ±√2 for 98#2 and ±4 for Eisenstein-type systems, and 0 only for f (oa_v2).
- **For PP:** this uses the same Shimura equivariance (C1) that PP's N1 marked as cited. If PP does not accept C1 as a citable theorem, A2 is CONDITIONAL on C1 alone, with every other step finite and exact.

**A3. PROVED (exact): plus-space structure.**
- PARI's Kohnen plus space S⁺ ⊂ V has dim 3, and **K ∩ S⁺ = span{G₁, G₄}, dim 2** (oa_v6, oa_v7). Independently, the subspace of K with c(n) = 0 for all n ≡ 2, 3 (mod 4) has dim 2 (oa_v3; finitely many linear conditions, n ≤ 700, give an upper bound, and S⁺∩K gives the lower bound).
- No nonzero element of K satisfies "c(n) = 0 unless n ≡ 0, 3 (mod 4)" or "unless n ≡ 2, 3 (mod 4)". No nonzero element is supported on a single class mod 4. No nonzero element vanishes at all n ≡ 0 (mod 7) and … (see A5). (Exact rank statements, oa_v3.)
- So the f-packet has multiplicity 2 in the plus space at level 4·7², not 1 as in Kohnen's squarefree-level isomorphism. Kohnen's theorem does not apply because 49 is not squarefree.

**A4. PROVED (C2 cited, plus PP's Sturm check): which members map to f.** Coordinates on (f(τ), f(2τ)):
- t = 1: S₁K₁ = S₁K₂ = 0, S₁K₃ = f(2τ), S₁K₄ = f + f(2τ). So **S₁(K₄ − K₃) = f**, and S₁: K → span{f, f(2τ)} is onto with kernel span{K₁, K₂}.
- t = 2: K₃ ↦ f, K₄ ↦ 2f − 2f(2τ).
- t = 3: K₁ ↦ −2f(2τ) and K₂ ↦ −f + 2f(2τ) (matches PP).
- t = 5: K₁ ↦ f + f(2τ) (matches PP) and K₂ ↦ −2f(2τ).
- t = 13: K₁ ↦ −f − f(2τ) and K₂ ↦ 2f(2τ).
- The images of t = 10 vanish on all of K, consistent with c(10n²) patterns. (Membership in the span is PP's n ≤ 30 check; the coordinates are read off at n = 1, 2.)

**A5. OPEN (only a finite check): c(n) = 0 for all n ≡ 0 (mod 7) on K.** It holds for all n ≤ 1200 (oa_v2, oa_v3). Path: express it through the U(7)/twist-by-χ₋₇ structure at 7. ~1 h.

**A6. OPEN: the action of U/V-type operators at 2 and 7 on K** (PP's "U/V not examined"). Not computed in this pass. ETA ~1–2 h.

**O-a status: RESOLVED in substance.** The exact isotypic subspace is K (dim 4, explicit basis), with its plus part (dim 2) and its Shimura images. Residual: A5 and A6 (structure at 2 and 7).

## Item O-b: Ξ's own weight-3/2 (Waldspurger) form

**B1. PROVED: χ₁₄₀ and χ₋₂₀ (also χ₂₈ and χ₋₄) are not squares of Dirichlet characters.**
- If ψ = ∏ψ_p, then ψ² = ∏ψ_p² and ψ_p²(−1) = 1 for every p.
- The 2-component of χ₁₄₀ and of χ₋₂₀ is χ₋₄, and χ₋₄(−1) = −1.

**B2. PROVED (algebra on q-expansions; modularity of the twist cited from Shimura 1973, Lemma 3.6): twisting lemma.**
- Let F ∈ S_{3/2}(4N, χ) with T(p²)F = λ_pF, and let ψ be primitive mod r. Then F⊗ψ ∈ S_{3/2}(4Nr², χψ²) and T(p²)(F⊗ψ) = ψ(p)²λ_p·(F⊗ψ) for p ∤ 4Nr.
- Proof: each of the three terms of T(p²) picks up the factor ψ(p)².
- **Consequence (B1 + B2): Ξ's eigensystem a_p(f_Ξ) = χ₋₂₀(p)a_p(f) is not reachable by twisting the level-196 packet K.** That is why "no new half-integral object" (9e34f2dc 3d) is a statement about central values, not about forms.

**B3. PROVED (reduction): Ξ = (f⊗χ₋₄)⊗χ₅ with χ₅ = ψ₅², where ψ₅ has order 4 mod 5.**
- Suppose G ∈ S_{3/2}(4M, χ_D) has T(p²)G = χ₋₄(p)a_p(f)G. The target is the newform of 49a1⊗χ₋₄, of conductor 784 (ob_v1, exact).
- Then H := G⊗ψ₅ ∈ S_{3/2}(100M, χ_Dχ₅) has T(p²)H = a_p(f_Ξ)H for p ∤ 20M, and H ≠ 0 iff c_G(n) ≠ 0 for some 5 ∤ n.
- Rational combinations: (G⊗ψ₅ + G⊗ψ̄₅)/2 has coefficients c(n)·(1, −1, 0) for n ≡ 1, 4, other (mod 5).
- **So O-b reduces to finding G (a preimage of f⊗χ₋₄).** With M = 784 (4M = 3136), H would sit exactly at level 78400.

**B4. PROVED (exact, computer-assisted; null result): no such G at levels 4M = 1568 or 3136.**
- This was checked for every quadratic character for which the space is nonzero: D ∈ {1, 8, 28, 56}. The odd D ∈ {−4, −8, −7, −56} give dimension 0.
- Dimensions: 84, 84, 82, 82 at 1568 and 182, 180, 180, 178 at 3136.
- The joint kernel of T(p²) − χ₋₄(p)a_p(f) for p = 3, 5, 11 is 0 in all 8 spaces (ob_v1).
- Method check: the same routine finds K at level 196.

**B5. OPEN (running): level 6272 = 2⁷·49** (ob_v2: D ∈ {1, 8, 28, 56}, dims 390, 390, 388, 388).
- Started ~19:52 CST with a 2.5 h timeout, so it ends by ~22:25 CST at the latest. ob_v1 itself finished (elapsed 3014 s) with the null result in B4.
- If ob_v2 finds G, an addendum will be filed as a new file, and H = G⊗ψ₅ will sit at level 6272·25 = 156800.

**B6. Resource estimate for the direct route (ob_dims_v1, dimension formula only).**
- dim S_{3/2}(Γ₀(39200), χ) = 3172–3176. dim S_{3/2}(Γ₀(78400), χ) = 6436–6444 (D ∈ {1,5,8,40,28,140,56,280}; the odd characters give 0).
- Observed cost of mfinit plus 3 Hecke matrices on this box (load 7–24 on 8 cores): dim ≈ 83: 43–192 s; dim ≈ 180: 225–1549 s.
- Cost grows at least cubically in dimension, so dim 6440 ≈ 36× dim 180 needs about 36³·(4–25 min), i.e. years of CPU time, and memory well beyond 15 GB. **The direct route is infeasible here.**
- **Obstruction:** the 2-adic part. Ξ's form cannot be a twist (B1), and the f⊗χ₋₄ preimage is absent at 2-power level ≤ 2⁶ (B4).

**O-b grade: OPEN, with paths.**
1. ob_v2 at 2⁷·49, ETA ≤ 22:25 CST.
2. If that is null: level 2⁸·49 = 12544 (dim ≈ 780; ~1 day under current load), or the ternary-theta / quaternion-order method (Gross; Böcherer–Schulze-Pillot; Pacetti–Tornaría) for f⊗χ₋₄ at 2-power level, ~1–2 days of Local work.
3. In every case, then B3.

## Item 4a: χ₁₄₀ on Γ₀(140), interval hardening

- **Grade: PROVED (exact). The basis is PP's certificate pp_4a_exact** (/workspace/audit-scratch/pp_c2e9b6fe_9e34f2dc_local_1822/pp_4a_exact.py 90ed5512…, .log 789473d6…). It is cited, not duplicated.
- **No float residual is used as a bound.** The float residual 5.21e−13 of part4 is withdrawn as evidence of exactness (PP Fix 10).
- **Local independent check 4a-L (a4_exact_modl_v1, exact, no floats). PROVED.**
  - Same lattice, cosets and Schreier generators: 288 cosets, 259 generators, length ≤ 39, s_max = 10 S-letters.
  - All arithmetic is in F_ℓ for 59 primes ℓ ≡ 1 (mod 140) below 2³¹, with one degree-1 prime 𝔩 | ℓ each. g = Gauss sum of χ₁₄₀, with g² = 140 checked mod ℓ.
  - Result: ρ(g)e₀ ≡ χ₁₄₀(d)e₀ (mod 𝔩) for all 259 generators and all 59 primes. S·S⁻¹ = I, S⁴ = I and (ST)³ = S² hold exactly mod each ℓ. The control (1,0;70,1) moves e₀ to a single other basis vector.
  - Norm argument: β_i := g^s(ρ(g)e₀ − χ(d)e₀)_i ∈ ℤ[ζ₁₄₀]. Every Galois conjugate representation is a product of unitary matrices, so |σ(β_i)| ≤ 2·140^{s/2} and log₁₀|N(β_i)| ≤ 529.52. Each ℓ divides N(β_i), and log₁₀∏ℓ = 550.58 > 529.52. So N(β_i) = 0 and β_i = 0.
- **Third, structural proof (P5 below).** ρ_{N₂} ≅ ρ_{D₂}⊗ρ_{D₅}⊗ρ_{D₇} exactly, and each factor's e₀-character is exact. So χ₁₄₀(d) = χ₋₄(d)χ₅(d)χ₋₇(d) on Γ₀(140) without any 140-dimensional computation.

## Item 2-/5-parts: precise formulation and results (p25_local_parts_v1, p25_gamma49_exact_v2; exact arithmetic in ℚ(ζ₁₄₀) or F_ℓ)

**P1. PROVED (exact): D(N₂) = D₂ ⊕ D₅ ⊕ D₇** is orthogonal (CRT bijection checked).
- D₂ ≅ (ℤ/2)², with q-values {0, 1/2, 1/4, 1/4}, level 4.
- D₅ ≅ ℤ/5, with q-values {0, 2/5, 3/5, 3/5, 2/5}, level 5.
- D₇ ≅ ℤ/7, with q-values {0, 2/7, 1/7, 4/7, 4/7, 1/7, 2/7}, level 7.

**P2. PROVED (exact, Milgram):** sig(D₂) ≡ 2, sig(D₅) ≡ 4, sig(D₇) ≡ 2 (mod 8). The sum ≡ 0 = sig(N₂). ∏_p G(D_p) = G(D) = g(χ₁₄₀) = +√140.

**P3. PROVED (exact):** each ρ_{D_p} (S e_γ = e(−sig_p/8)|D_p|^{−1/2}Σ_δ e(−(γ,δ))e_δ, T e_γ = e(q(γ))e_γ) satisfies S·S⁻¹ = I, S⁴ = I and (ST)³ = S². So each is a genuine representation of SL₂(ℤ). The odd local parts have even signature, so no metaplectic cover is needed at 5 or 7, and the 2-part has even signature as well.

**P4. PROVED (exact): local e₀-characters.**
- ρ_{D₂}(γ)e₀ = χ₋₄(d)e₀ on Γ₀(4) (6 cosets, 7 Schreier generators).
- ρ_{D₅}(γ)e₀ = (d/5)e₀ on Γ₀(5) (6 cosets, 7 generators).
- ρ_{D₇}(γ)e₀ = (d/7)e₀ = χ₋₇(d)e₀ on Γ₀(7) (8 cosets, 8 generators).
- Each extends from generators to the whole group by the same subgroup argument as 4a.

**P5. PROVED: ρ_{N₂}(S) = ⊗_pρ_{D_p}(S) and ρ_{N₂}(T) = ⊗_pρ_{D_p}(T)** under the CRT identification (B and q are orthogonal sums, and the constants multiply to conj(G(D))/140 = 1/g by P2). Hence ρ_{N₂}(γ) = ⊗ρ_{D_p}(γ) for all γ. For γ ∈ Γ₀(140) ⊂ Γ₀(4)∩Γ₀(5)∩Γ₀(7), P4 gives **ρ_{N₂}(γ)e₀ = χ₋₄(d)χ₅(d)χ₋₇(d)e₀ = χ₁₄₀(d)e₀.** This is the 2·5·7 factorization of the carrier's Weil character, and it is an independent proof of 4a.

**P6. PROVED (exact):** ρ_{D_p}(−I)e₀ = χ_p(−1)e₀, with signs (−, +, −) at p = (2, 5, 7). The product is + = χ₁₄₀(−1).

**P7. PROVED (exact; PARI ellrootno(E,p) and elllocalred): local data.**

| p | conductor exponent f | conductor exponent Ξ | ε_p(f) | ε_p(Ξ) | local Weil–Deligne of f |
|---|---|---|---|---|---|
| ∞ | — | — | −1 | −1 | weight 2 |
| 2 | 0 | 4 | +1 | **−1** | unramified; Frob roots of x² − x + 2, i.e. (1 ± √−7)/2 |
| 5 | 0 | 2 | +1 | +1 | unramified; Frob roots of x² + 5, i.e. ±√−5 |
| 7 | 2 | 2 | −1 | −1 | dihedral from ℚ₇(√−7) (CM) |
| product | | | ε(f) = +1 | ε(Ξ) = −1 | |

**P8. PROVED (standard local formula, cited Tate/Deligne; hypotheses checked: π_p unramified with trivial central character, χ_p ramified quadratic; matches P7).**
- σ_p(Ξ) = σ_p(f)⊗χ_p for p = 2, 5, where χ₂ = χ₋₄,₂ (a(χ) = 2) and χ₅ = (·/5) (a(χ) = 1).
- a(σ⊗χ) = 2a(χ), which gives 4 and 2.
- ε_p(π_p⊗χ_p) = ω_π(ϖ)^{a(χ)}·χ_p(−1) = χ_p(−1): −1 at 2 and +1 at 5.
- At 7, χ₋₂₀ is unramified, so ε₇ changes by χ₋₂₀,₇(7)^{a(π₇)} = (±1)² = 1.

**P9. PROVED: combination with the χ₋₇ part (ae951f3e §3.6).**
- χ₁₄₀ = χ₋₄·χ₅·χ₋₇. The 7-part χ₋₇ is the CM character, f⊗χ₋₇ = f (9e34f2dc 2c), so it acts trivially on f and on ε₇.
- The 5-part changes the conductor (5⁰ → 5²) but not the sign (χ₅(−1) = +1).
- **The whole root-number flip ε(f) = +1 → ε(Ξ) = −1 is 2-adic: ε₂ = χ₋₄(−1) = −1.** This refines 9e34f2dc 2d ("flip from χ₋₂₀(−1)").
- On the carrier side, P6 gives the same sign triple (−, +, −) for ρ_{D_p}(−I)e₀.

**P10. CONDITIONAL (cited H: a Weil representation of a level-20 discriminant form factors through SL₂(ℤ/20), as in Nobs–Wolfart and Bruinier §1): "2- and 5-parts on Γ₀(49) without twisting".**
- Precise statement: Weil(D₂⊕D₅)|_{Γ₀(49)} contains no Γ₀(49)-stable line.
- Exact part (PROVED, p25_gamma49_exact_v2): ρ_{D₂}⊗ρ_{D₅} (dim 20) has no 1-dimensional SL₂(ℤ)-subrepresentation. For each character T ↦ i^k, S ↦ i^k (k = 0..3), the restriction of S − i^k to the T-eigenspace (dims 1, 2, 1, 0) has full column rank over F_ℓ for 3 primes, hence over ℚ(ζ₁₄₀). The earlier float SVD in v1 (margin 0.62) is superseded.
- Γ₀(49) maps onto SL₂(ℤ/20) (XW §3.3, CRT). So under H, a Γ₀(49)-stable line would be an SL₂(ℤ)-stable line, and there is none.
- **Reading:** on Γ₀(49) the 2- and 5-parts carry no scalar (line) data. They reach scalar forms only after twisting (LD-Ξ3, level 19600). That is the precise sense of XW's "no counterpart on Γ₀(49) except through twisting".
- Path to PROVED: verify H for this module (Γ(20) acts trivially), ~30 min.

**P11. OPEN (interpretive, undefined):** whether the equal sign triples in P6 and P8/P9 are one mechanism (for example, a local theta correspondence identity) rather than a coincidence of χ_p(−1). Nothing here defines that.

## Per-item table
| Item | Result | Grade |
|---|---|---|
| O-a | K = ker T(9), dim 4, is exactly the f-isotypic subspace for all p ∤ 14 (closes PP N1); plus part span{G₁, G₄} dim 2; S₁(K₄ − K₃) = f | A1, A3 PROVED; A2, A4 PROVED (cited C1/C2; A2 CONDITIONAL on C1 if PP declines that citation); A5, A6 OPEN |
| O-b | not a twist of K (B1, B2); reduced to a preimage of f⊗χ₋₄ (B3); none at levels 1568 or 3136 (B4); 6272 running; direct 78400 infeasible (B6) | B1–B4 PROVED; O-b **OPEN** (path and ETA above) |
| 4a | PP exact certificate (cited); Local exact mod-ℓ check; structural proof via P5 | **PROVED** (PP); 4a-L PROVED |
| 2/5 | local decomposition, Weil characters χ₋₄, χ₅, χ₋₇, tensor factorization, local ε and conductors, 2-adic sign flip, Γ₀(49) invisibility | P1–P9 PROVED; P10 CONDITIONAL (H); P11 OPEN |

## Rollup (new claims in this file)
- **PROVED 18:** A1, A2*, A3, A4*, B1, B2, B3, B4, 4a-L, P1–P9. (* = citation-dependent, hypotheses checked.)
- **CONDITIONAL 1:** P10 (cited H).
- **OPEN 4:** A5, A6, O-b (B5/B6), P11.
- **REFUTED 0 new.** PP's REFUTED 3b-ii is accepted.
- **Not counted:** 4a itself (PROVED by PP's certificate, cited).

**Untouched in this file (Owner/other lanes):** O-c (whether the resonant algebra's weight-3/2 Ξ shadow, historical "RTA" DEFINITION_RTA_RESIDUALS…_2026-10-26.md:53–55, is K or a future H), V₈₄, the joint carrier, H₊U, LD-O3a/b/c, α (O4) and O5 free Dirac.

## Custody and process notes
- **oa_v1:** ended by its own 3000 s timeout at about 19:39 CST. Its log is empty (0 bytes, sidecar e3b0c442…), because Python buffered stdout. It was not stopped by hand. oa_v2 (unbuffered) supersedes its eigenspace part, with primes ≤ 37.
- **Crashed attempts, kept:** oa_v2, oa_v3, oa_v4, oa_v5 and oa_v6 crashed at their Shimura steps on GP syntax or type errors. Every result they printed before the crash is valid, and each was superseded by the next version. oa_v7 is the complete run.
- **ob_v2.log** is still being written, so it has no sidecar yet. The addendum will hash it.
- No file was deleted, renamed, moved or overwritten.

Local-derived. For PP audit. Nothing adopted. No CERT. Tip 7cddb188 untouched. Nothing sent outside.
