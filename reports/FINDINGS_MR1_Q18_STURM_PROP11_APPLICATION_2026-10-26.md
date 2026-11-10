# FINDINGS: MR1, Q18 Sturm, written application of Magnusson–Raum Prop 1.1 to ρ̄|cusp6 / dim 89
Date: 2026-10-26 · Executor: MR1 · STATUS: **PARTIAL** (one item, D/E, is GAP-ABSENT)

## Authority (sha256 recomputed; all MATCH)
- OWNER_WRITE_CARD_Q18_STURM_AUTHORIZE: 6232cb556784927d7f1ab6e436a72dcd17114b5503827e23f89a5b523dda446d MATCH
- OWNER_WRITE_PURSUE_Q18_STURM_BOUND: fb8f89978a77f549dad5ee035ba4d1cc47cf0864347de8f9d275680ebb59783e MATCH
- FINDINGS_MR1_Q18_DEPTH_JUSTIFY_CITE (prior PARTIAL): 114da0112dd0eb6a2de289ed233cf8f2240215c16c511bb10d939bd4171afa6e MATCH
- literature/gannon-2202.06676/2202.06676.pdf: 48a59d35f5e84b4246f650823a0f0f71209171dac8ceb24ad01177a6d6463b57 MATCH. The file is Magnusson–Raum, "On the Computation of General Vector-valued Modular Forms", arXiv:2202.06676v2. The directory name "gannon" is a misnomer.
- Card1D: grok-batches/EIGEN-TE-RHOBAR-LOCAL-FACTOR-CARD1D: 6e8c901c8eb240cb9c4fbce39309c68728e4636daf38c003fe9f1ccb059ff125 MATCH
- Card1B: grok-batches/EIGEN-TE-RHOBAR-IND-LINALG-Q18: 825a5579da0b6cad3b66996c80969dcb93b41d6ba91f00e4d6c383512c5e0f12 MATCH
- Card1F OW 03227e61…: cited as given. I did not re-hash it because no path was supplied.
- Eigen Sturm FINDINGS: grok-batches/EIGEN-TE-Q18-DEPTH-JUSTIFY-CITE: ac68cf8f6641bbe2c2c884209e0ac92f9ad71b17c24a5479638e63d893177a99. Its STATUS is ABSENT, as the Card states. There is no newer Eigen Sturm file, so this report duplicates no work.
- tip_pre = tip_end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 · tip_touched NO

## Extracted text from 2202.06676 (pdftotext -layout)
- **§1.2 definitions:** "An arithmetic type ρ for Γ is a finite-dimensional, complex representation of Γ. We say that ρ is a congruence type if its kernel is a congruence subgroup. We refer to the smallest possible level of its kernel as the level of ρ." M_k(ρ) is the space of holomorphic f: H→V(ρ) of moderate growth with f|_{k,ρ}γ = f for all γ∈Γ. The Fourier coefficients are c(f;n) ∈ V(ρ), n ∈ Q.
- **(1.5):** "ρ_N = Ind_{Γ1(N)}^{SL2(Z)} 1 and ρ_χ = Ind_{Γ0(N)}^{SL2(Z)} χ."
- **Proposition 1.1 (see [10, 46]):** "Let k and N be positive integers, and ρ a congruence type for SL2(Z). Further, let f ∈ Mk(ρ) … Then we have f = 0 if ∀n ∈ Q, 0 ≤ n ≤ k/12 : c(f;n) = 0."
- **§2 (2.6)/(2.7):** "If ρ has level N, then exponents of q in the support … have denominator at most N. … the Sturm bound … yields some explicit nonnegative P ∈ Q such that the resulting 'truncated' Fourier expansion map is injective: f̃_P : Mk(ρ) → FE_P(C) ⊗ V(ρ)."
- **Theorem 2.2:** "Assume that P ∈ Q is at least the Sturm bound for k and ρ. Then Algorithm 1 computes a basis for the image of Mk(ρ) → FE_P(C) ⊗ V(ρ)…"
- **§4 complexity remark:** "A typical choice of P is the Sturm bound, which is of size O(k[SL2(Z) : Γ])." This is only an O-estimate. It gives no explicit constant and no proof.

## Critical checks
**A. Is ρ̄|cusp6 a congruence type? MATCH (conditional on a Written project fact).** The paper requires that ker ρ be a congruence subgroup. Card1D line 14 builds ρ̄(g) from local generators that are CRT lifts mod 140 and are lift-independent. That means ρ̄ factors through SL2(Z/140), so ker ρ̄ ⊇ Γ(140). This makes ρ̄|cusp6 a congruence type of level dividing 140, which fits T-order 140. Caveat: Card1D states this as a computed property, not as a separately labelled premise.

**B. Which space? The project space is a Γ0(49) / Ind variant, not M_4(ρ̄|cusp6) for SL2Z.** Card1B, line 1: "exact Ind path, S₄(Γ₀(49),ρ̄)". Line 11: "Ind_{Γ₀(49)}^{SL₂ℤ}1 is the permutation action on the 56 points of P¹(Z/49). Total dimension 42·56 = 2352." Card1D, line 44: "Assemble the cusp6 module over C[E₄,E₆] ⊗ Ind_{Γ₀(49)} through q^18 and check it against 89."
- To use Prop 1.1 (stated only for SL2(Z)), the space has to be rewritten as M_4(ρ̄|cusp6 ⊗ Ind_{Γ0(49)}^{SL2Z} 1). The induction isomorphism M_k(Γ0(N), ρ|Γ0(N)) ≅ M_k(ρ ⊗ Ind 1) is **not stated or proved in the PDF**. The PDF only defines ρ_χ in (1.5) and uses Ind algorithmically.
- The PDF also gives no Written statement that a tensor product of congruence types is a congruence type. (The kernel contains Γ(140) ∩ Γ(49) ⊇ Γ(980), but that step is not in the PDF.) Both items are listed as missing lemmas L1 and L2.

**C. Numerical bound at k = 4.** Prop 1.1 gives k/12 = 4/12 = **1/3**. If f ∈ M_4(ρ) and c(f;n) = 0 for every n ∈ Q with 0 ≤ n ≤ 1/3, then f = 0.
- For ρ = ρ̄|cusp6 ⊗ Ind (level dividing 980), the support has denominators ≤ 980. So this means checking all exponents n ∈ (1/980)Z ∩ [0, 1/3] in **every** one of the 6·56 = 336 vector components.
- The bound 1/3 is *not* the number 18. Depth 18 in the scalar Γ0(49) q-expansion at ∞ does **not** follow from Prop 1.1 as written, because Prop 1.1 measures exponent ≤ 1/3 across all Ind components, and those components correspond to the expansions at all cusps of Γ0(49) (widths 1 at ∞ and at the 1/7-type cusps, 49 at 0). The two conditions are different. Neither one is shown to imply the other by anything in the PDF.
- Arithmetic: at the width-49 cusp, exponent 1/3 corresponds to local index 49/3 ≈ 16.33. At width-1 cusps it corresponds to index 0. Neither figure is 18.

**D. A Written path from Prop 1.1 + Ind (μ = 56) to k·μ/12 = 4·56/12 = 18.67? GAP-ABSENT.** The PDF has no lemma converting the vector-valued SL2Z bound k/12 on ρ⊗Ind_{Γ0(N)} into a single-cusp (∞) bound k·[SL2Z:Γ0(N)]/12. The only related text is the O(k[SL2(Z):Γ]) size remark in §4. It has no constant, no statement, and no proof.
- Missing lemma **L3**: "If f ∈ M_k(Γ0(49), ρ̄|cusp6) and the V(ρ̄|cusp6)-valued Fourier coefficients of f at the cusp ∞ vanish for all exponents n ≤ k·56/12, then f = 0." For the vector-valued, non-trivial-ρ case this should be the standard norm/product argument: take a power of det or of ∏_γ f|γ to reach a scalar SL2Z form, then apply scalar Sturm [46]. It must also handle T-exponent shifts in (1/140)Z, which could move the effective bound by up to dim·(max fractional exponent).
- L3 is not in the PDF and not on disk, so I did not invent it.

**E. Vanishing of one form vs. pinning the 89-dim module. The bridge is half-Written.** Prop 1.1 plus the linearity of f ↦ f̃_P give injectivity of the truncation map (2.7). This is explicitly Written in §2 (the "truncated Fourier expansion map is injective"). Theorem 2.2 then gives a basis of the image at precision P ≥ Sturm bound. So *if* P is a valid Sturm bound for the actual space, then an 89-dimensional image of truncated expansions pins the module. That step is Written via (2.7) and Theorem 2.2, applied with dim 89 from Card1B.
- The gap is again the choice of P. The Written P is 1/3 across all Ind/cusp components, not depth 18 at ∞. For depth 18 to pin the module you need L3, plus L1/L2 for the Ind reformulation. Also, Card1B does not establish that the depth-18 candidate expansions lie in the space (membership), which a pin also needs. That is a procedural item, not part of Prop 1.1.

## Missing lemmas (precise)
- **L1:** the induction isomorphism M_k(Γ0(49), ρ̄|cusp6) ≅ M_k(ρ̄|cusp6 ⊗ Ind_{Γ0(49)}^{SL2Z} 1), compatible with cusp forms and with the Fourier-coefficient indexing. Not in the PDF.
- **L2:** a tensor product of congruence types is a congruence type, or a direct Written statement that ker(ρ̄|cusp6 ⊗ Ind) ⊇ Γ(980). Elementary, but not Written in the PDF.
- **L3:** a single-cusp vector-valued Sturm bound at ∞ for Γ0(49) with type ρ̄|cusp6, with an explicit constant (expected to be about k·56/12 plus possible T-exponent correction). Absent from the PDF and from disk. **This is the lemma needed to justify depth 18.**

## What *is* Written-usable now
With L1 and L2 assumed (standard, but held because they are not Written), Prop 1.1 justifies an **alternative** precision: the 336-component vector-valued expansion of ρ̄|cusp6⊗Ind with exponents n ≤ 1/3, n ∈ (1/980)Z. That precision pins M_4 and S_4 via (2.7) and Theorem 2.2. It is a different computation from "scalar q^18 at ∞" and needs expansions at all 56 cosets/cusps.

## Consequences for Card1F
- The Card1F module q^18 coefficient build stays **HELD**. The status is PARTIAL, not HIT.
- Owner options:
  - (i) authorize a Written L3 (a single-cusp vector-valued Sturm argument); or
  - (ii) switch the precision target to the Prop 1.1 all-components n ≤ 1/3 route, which needs L1 and L2 Written; or
  - (iii) keep the current hold.
- The ρ₅/ρ₇ intertwiner work is unaffected.
