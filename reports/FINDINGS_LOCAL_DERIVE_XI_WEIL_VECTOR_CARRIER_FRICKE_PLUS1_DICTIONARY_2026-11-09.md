# FINDINGS — Local Path DERIVE (O1/O2): vector-valued Weil carrier with a +1 Fricke law, and the Weil(140)↔Γ₀(49) dictionary — 2026-11-09

- **Authority:** Owner-adopted blueprint, reports/OWNER_WRITE_MAINCHAT_BLUEPRINT_1509_CORRECTED_ADOPTED_2026-11-09_1511.md (sha 5a6e7177…), Local O1/O2 at line 14. Written ~3:30 PM CST (America/Chicago).
- **Limits:** additive new file. Tip 7cddb188… read-only and unchanged. No CERT. Nothing sent outside.
- **Builds on:**
  - reports/FINDINGS_LOCAL_XI_FRICKE_W49_GAMMA0_49_PROOF_LOGIC_PP_FIXES_2026-11-09.md (72222fed…; cited as "XF");
  - reports/FINDINGS_LOCAL_SO48_V23_LOCAL_DATUM_MATCH_CHECK_2026-11-09.md (2135adfb…);
  - MR1 reports/FINDINGS_MR1_B_SEC3_APPELL_RC_S2_S4_CLOSE_ADOPTED_DEFS_2026-11-09.md (48a2d687…; cited as "MR1").
- **Notation:**
  - W := W_49^Fricke = (0,−1;49,0);
  - weight-k slash: (g|_kW)(τ) = 49^{k/2}(49τ)^{−k} g(−1/(49τ));
  - T = the tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md.
- **Checks:** small numpy/sympy checks only (Weil matrices, lattice theta sums); nothing kept.

## 0. Owner-Written context (adopted definitions; not proofs)
- **Definitions** (blueprint :9–10):
  - Λ₀ := ln(6+√35)/√10 ≈ 0.7835772;
  - R_c := κℓ_P with κ := √(2/Λ₀) ≈ 1.597622.

  (Numeric recheck: Λ₀ = 0.78357721761742…, κ = 1.59762224….)
- **PROVED: 6+√35 is the fundamental unit of ℚ(√35).**
  - O_K = ℤ[√35], since 35 ≡ 3 (mod 4).
  - N(6+√35) = 36−35 = 1, and y = 1 is the least y > 0 with 35y²+1 a square.
  - No unit has norm −1: x² ≡ −1 (mod 7) is impossible.
  - So ln(6+√35) = Reg(ℚ(√35)) (MR1:22).
- **PROVED (MR1:24–25; rechecked):** L(1,χ₁₄₀) = 2h·Reg/√140 with h = 2. The finite formula −(1/√140)Σχ(a)ln sin(πa/140) gives 0.8376792813 = 4Reg/√140 (h = 2.0000). Hence Λ₀ = √(7/8)·L(1,χ₁₄₀). Here χ₁₄₀ = (140/·) is the character of ℚ(√35).

## 1. Fixed facts (unchanged)
- **PROVED (XF C7):** f = 49.2.a.a (Cremona 49a1) has f|₂W = −f. Its sign stays −1.
- **REFUTED (Local-derived check):** "symmetrizing 49a1 gives a nonzero +1 vector."
  - f + f|₂W = 0, and S₂(Γ₀(49)) = ℂf.
  - So the +1 cusp space at weight 2 is S₂(Γ₀(49))⁺ = 0, and the route through the vector (f, f|W) gives nothing at weight 2.

## 2. Local-derived carriers
**LD-Ξ1 (main proposal, PROVED).**
- L₁ := ℤ² with Gram [[2,1],[1,4]]. This is the norm form of O = ℤ[(1+√−7)/2], the CM order of 49a1. It has det 7, level 7, and is 7-modular: L₁′(7) ≅ L₁ because (√−7) is principal.
- θ₁ := θ_{L₁} is the e₀-component of the vector-valued theta Θ_{L₁} for the Weil representation ρ_{L₁}, with discriminant form ℤ/7.
- θ₁ ∈ M₁(Γ₀(7), χ_{−7}), so θ₁(7τ) ∈ M₁(Γ₀(49), χ_{−7}).

(a) **Weight 1, PROVED** (Poisson summation, numerically checked).
- θ₁|₁W = −i√7·θ₁(7·) and θ₁(7·)|₁W = (−i/√7)·θ₁.
- On F₁ := (θ₁, √7·θ₁(7·)) the Fricke involution acts by −iσ_x. Its square is −1, as forced by odd weight. The eigenvalues are ±i, so there is no ±1 law at weight 1.

(b) **Weight 2, PROVED.**
- Carrier: F₂ := (θ₁(τ)², 7·θ₁(7τ)²), with entries in M₂(Γ₀(49)) and trivial character (χ_{−7}² = 1).
- W acts on F₂ by the sign-permutation matrix −σ_x.
- The +1 eigenspace is ℂ·g₊ with **g₊ := θ₁(τ)² − 7θ₁(7τ)²**. Then g₊|₂W = +g₊ (numerically checked at 3 points to 10 digits). The constant term is −6, so g₊ ≠ 0.
- Level 49, trivial character, weight 2.
- **g₊ is Eisenstein (PROVED).** W preserves the cuspidal and Eisenstein subspaces (they are Petersson-orthogonal and W is unitary). The cusp projection of g₊ therefore lies in S₂⁺ = 0. This is consistent with 49a1's sign −1.

(c) **Weight 4, PROVED.**
- L₄₉ := L₁ ⊕ L₁(7) has rank 4, det 2401 and level 49, and is 49-modular. For the last point: L₁′(49) = L₁′(7)(7) ≅ L₁(7), and L₁(7)′(49) = L₁′(7) ≅ L₁, so L₄₉′(49) ≅ L₄₉.
- θ_{L₄₉} = θ₁(τ)θ₁(7τ) ∈ M₂(Γ₀(49)) with θ_{L₄₉}|₂W = −θ_{L₄₉} (numerically checked).
- θ_{L₄₉}² ∈ M₄(Γ₀(49)) has θ_{L₄₉}²|₄W = +θ_{L₄₉}², which is nonzero. This is the theta of a level-49 genus with Fricke sign +1 at another weight.

**LD-Ξ2 (induced carrier, CONDITIONAL).**
- Construction: for any representation ρ of Γ₀(49) on V (e.g. the tip's ρ on V₄₂, T:286–288), Ind_{Γ₀(49)}^{Γ₀(49)⁺} ρ acts on V⊕V.
- For a form F, the pair (F, F|W) transforms under it, with W acting as the block swap [[0, ρ(W²)],[1, 0]].
- The +1 law then holds by construction.
- Conditions:
  - ρ(W²) = ρ(−I)·(−1)^k must act trivially, which holds for even k with ρ(−I) = Id on V₄₂ (T:256);
  - the Owner must adopt a doubled carrier. This is the tip's unfolded "Path A V₈₄" (T:218).
- It is tautological: the +1 eigenvectors are the symmetrizations F + F|W, and they are nonzero iff F|W ≠ −F.

**LD-Ξ3 (χ₁₄₀-twist, PROVED by citation; not a Γ₀(49) carrier).**
- f⊗χ_{−7} = f: CM by ℚ(√−7), and a_p = 0 whenever χ_{−7}(p) = −1.
- Hence f⊗χ₁₄₀ = f⊗χ_{−20}, a newform of level 49·20² = 19600.
- Atkin–Li (Invent. Math. 48, 1978): for quadratic χ of conductor prime to N, ε(f⊗χ) = ε(f)·χ(−N).
- So ε(f⊗χ_{−20}) = (−1)·χ_{−20}(−49) = (−1)(−1) = **+1**, equivalently root number −1.
- The +1 Fricke law appears after twisting by the Λ₀-character, but at level 19600, not 49.

**OPEN.** Identifying Ξ with any of these carriers is OPEN.
- Ξ is a weight-3/2 shadow (/workspace/grok-batches/DEFINITION_RTA_RESIDUALS_TO_FIFTH_ORDER_ORTHANT_CONES_LIMA_CHAIN_2026-10-26.md:53–55), whereas LD-Ξ1/LD-Ξ2 have integral weight.
- A weight-3/2 analogue would need an odd-rank lattice and a metaplectic Fricke action (level 4·49) together with a Kohnen-type plus space. Not derived.

## 3. Dictionary Weil(140) ↔ Γ₀(49)
1. **PROVED: decomposition of N₂.**
   - N₂ has Gram [[2,14],[14,28]], det −140, signature (1,1), discriminant form D = ℤ/2×ℤ/70 with q = x²/4 − y²/140, level 140 (T:287).
   - D = D₂ ⊕ D₅ ⊕ D₇. The 2-part has level 4. The 7-part is D₇ ≅ (ℤ/7, −5t²/7), with y = 10t; its level is 7, not 49.
   - ρ_{N₂} factors through SL₂(ℤ/140) = SL₂(ℤ/4)×SL₂(ℤ/5)×SL₂(ℤ/7).
2. **PROVED (numerically on 9 elements; standard): the character on e₀.**
   - For γ = (a,b;c,d) ∈ Γ₀(140), ρ_{N₂}(γ)e₀ = χ₁₄₀(d)·e₀. Checked against an explicit 140×140 Weil representation, with S unitary and (ST)³ = S².
   - χ₁₄₀ = χ_{−4}·χ₅·χ_{−7}, product of prime discriminants.
   - So the scalar (e₀) shadow of Weil(N₂) lives on Γ₀(140) with character χ₁₄₀, the same character as Λ₀ = √(7/8)L(1,χ₁₄₀) (MR1:25).
3. **PROVED: what Γ₀(49) sees.**
   - The image of Γ₀(49) in SL₂(ℤ/140) is SL₂(ℤ/20) × B(𝔽₇), with B(𝔽₇) the upper-triangular group mod 7. The 4·5 part is full by CRT surjectivity.
   - So ρ_{N₂}|Γ₀(49) carries the full 2- and 5-parts and only Borel data at 7. It carries nothing mod 49.
4. **PROVED: why ρ(W) fails on Weil(140).**
   - WγW⁻¹ = (d, −c′; −49b, a) for γ = (a, b; 49c′, d). Mod 7 this depends on c′, which γ mod 140 does not determine.
   - So Fricke conjugation does not descend to the level-140 quotient through which ρ_{N₂} factors.
   - This is consistent with T:217 ("ρ(W₇) CLOSED ABSENT on V₄₂"). R26 itself is not re-proved here.
5. **PROVED: the field picture.**
   - ℚ(√35, √−7) = ℚ(√−7, √−5), because 35·(−7) = −5·7².
   - Its three quadratic subfields are ℚ(√35) (χ₁₄₀), ℚ(√−7) (χ_{−7}) and ℚ(√−5) (χ_{−20}), with χ₁₄₀ = χ_{−7}·χ_{−20}.
6. **Assignment of data:**
   - **χ₁₄₀ data:** Λ₀, Reg(ℚ(√35)), h = 2, the e₀-character of ρ_{N₂}, U(140) and the LD-1 form (both of level 140), and the twist LD-Ξ3.
   - **level-49 data:** W_49^Fricke, X₀(49) of genus 1, 49a1 with ε = −1, g₊ and θ_{L₄₉}², all on Γ₀(49) with trivial character.
   - **the bridge:** the 7-part. χ₁₄₀'s 7-component is χ_{−7}, the character of ℚ(√−7), and 49 = |d_{ℚ(√−7)}|·N(√−7) is 49a1's conductor (standard CM formula N = |d_K|·N𝔣). L₁ is the norm form of the same CM order. PROVED.
7. **Where the dictionary fails:**
   - 140 and 49 share only the prime 7, and Weil(140) has level 7, not 49, at 7.
   - The parts at 2 and 5 (χ_{−4}, χ₅, and the conductor-20 factor) have no counterpart on Γ₀(49) except through twisting (LD-Ξ3, which changes the level to 19600).
   - W_49^Fricke ∉ SL₂(ℤ) and does not descend mod 140.
   - The common refinement is Γ₀(49) ∩ Γ₀(140) = Γ₀(980) (cf. CF(980) in /workspace/grok-batches/SOFTSF_PRESS_MR1_PURSUE_MISSED_VARS_PATTERNS_2026-10-26.md:3). Any joint carrier lives at level 980.
   - The weight-3/2 (metaplectic) side is OPEN.
   - Why the divisor is √10, i.e. the factor √(7/8), stays OPEN (MR1:42).

## 4. Rollup
- **PROVED 12:**
  - fundamental unit;
  - Λ₀ = √(7/8)L(1,χ₁₄₀) recheck;
  - LD-Ξ1(a), (b) including g₊ Eisenstein, (c);
  - LD-Ξ3;
  - dictionary items 1–5 and the 7-part bridge in 6.
- **CONDITIONAL 1:** LD-Ξ2 (induced / Path A V₈₄ adoption, ρ(W²) = Id).
- **OPEN 3:**
  - Ξ (weight 3/2) identification and metaplectic Fricke;
  - the 2- and 5-parts on Γ₀(49) without twisting;
  - the √(7/8) normalization.
- **REFUTED 1:** a nonzero +1 vector from symmetrizing 49a1.

No CERT. Tip untouched. Residual≠Resonant. 49a1's sign stays −1. PP to audit.
