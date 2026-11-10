# EIGEN — q^18 Sturm / Magnusson–Raum Prop 1.1 application to ρ̄|cusp6 (dim 89) — FINDINGS 2026-10-26
**STATUS: GAP-ABSENT (conditional HIT).** Prop 1.1 gives B = k/12 = 4/12 = 1/3, measured in q = e^{2πiτ} exponents. q^18 certifies the 89-dim space IF three hypotheses hold. None of them is Written yet: L1, L2 and L3 below. A bound is not established, and no lemma was invented.

## Authority (sha256 re-verified before write, 13:5x CDT)
- Card CLOSED A OWNER_WRITE_CARD_Q18_STURM_AUTHORIZE: 6232cb556784927d7f1ab6e436a72dcd17114b5503827e23f89a5b523dda446d ✔
- Assign OW OWNER_WRITE_PURSUE_Q18_STURM_BOUND: fb8f89978a77f549dad5ee035ba4d1cc47cf0864347de8f9d275680ebb59783e ✔
- Prior Eigen ABSENT ac68cf8f…a177a99 ✔; MR1 PARTIAL 114da011…afa6e ✔
- 2202.06676.pdf 48a59d35f5e84b4246f650823a0f0f71209171dac8ceb24ad01177a6d6463b57 ✔; gannon1310.pdf 392e6a53… (read-only, not needed)
- Inputs: Card1B 825a5579… (dim 89 exact; Ind_{Γ₀(49)} = 56-point permutation); Card1C e90ef226…; Card1D 6e8c901c8eb240cb9c4fbce39309c68728e4636daf38c003fe9f1ccb059ff125 (ρ̄|cusp6 ≅ ρ₄⊗ρ₅⊗ρ₇ over CF(140), exact)
- Tip start: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91

## Prop 1.1 verbatim (Magnusson–Raum, arXiv:2202.06676, PDF page 5, §1.2)
> "Proposition 1.1 (see [10, 46]). Let k and N be positive integers, and ρ a congruence type for SL2(Z). Further, let f ∈ Mk(ρ) be a modular form of weight k and type ρ. Then we have f = 0 if ∀n ∈ Q, 0 ≤ n ≤ k/12 : c(f; n) = 0."

Definitions, same page and p.4:
- "ρ is a congruence type if its kernel is a congruence subgroup."
- Slash action: (f|_{k,ρ}γ)(τ) = (cτ+d)^{-k} ρ(γ)^{-1} f(γτ). The printed ρ is garbled in the extraction. This is equivalent to the project convention F(γτ) = (cτ+d)^k ρ̄(γ) F(τ).
- c(f;n) ∈ V(ρ), n ∈ Q: these are the vector-valued Fourier coefficients in q = e^{2πiτ} with rational exponents, for all components at once. §2 (p.~10) calls k/12 "the Sturm bound" and uses truncation n<P.

## Application
1. Weight k=4. B = k/12 = 1/3. Exact, no Sage needed (the formula is closed-form).
2. Space: S₄(Γ₀(49), ρ̄|cusp6), dim 89 (Card1B). To land in Prop 1.1's setting (type for SL₂(Z)), view it as M₄(Ind_{Γ₀(49)}^{SL₂ℤ} ρ̄|cusp6) or M₄(ρ̄|cusp6 ⊗ Ind 1), a 6·56 = 336-dim type.
3. Kernel of Ind 1 = Γ(49), which is congruence (MR §1.1, eq. 1.5 text). If ρ̄|cusp6 has kernel ⊇ Γ(140), the tensor product has kernel ⊇ Γ(980), so it is congruence.
4. Under those hypotheses: if a form's coefficients vanish for every Q-exponent n ≤ 1/3, in every one of the 336 components, the form vanishes. So truncation at any P > 1/3 is injective on the 89-dim space. "Through q^18" (all n ≤ 18 in q = e^{2πiτ}, all components) then satisfies 18 ≥ 1/3 with a wide margin. That would be the conditional HIT.

## Where it fails: missing Written lemmas
- **L1 (congruence).** No Written proof that ker ρ̄|cusp6 ⊇ Γ(140).
  - Card1C infers it from T-order 140, but finite T-order does not imply a congruence kernel for SL₂(Z) representations in general.
  - Card1D checked CRT local lifts, with one second lift. That is evidence, not a proof that ρ̄ factors through SL₂(Z/140).
  - What is needed: a Written proof that ρ₄, ρ₅, ρ₇ factor through SL₂(Z/4), SL₂(Z/5), SL₂(Z/7). One route is an exact check of the defining relations of SL₂(Z/p^e) on S_p, T_p. Another is a cited congruence theorem for these dimensions.
- **L2 (Shapiro / induction identification).** No Written statement that S₄(Γ₀(49), ρ̄) ≅ S₄(SL₂ℤ, Ind ρ̄) (or ρ̄⊗Ind 1) compatibly with the convention F(γτ) = (cτ+d)^k ρ̄(γ)F(τ). Card1B's dim formula uses it implicitly.
  - Without L2, Prop 1.1 does not apply to a Γ₀(49) space: it is stated for types of SL₂(Z).
- **L3 (meaning of "q^18 depth").** Not Written anywhere on disk (rg over quantum-comp/reports and grok-batches). Two things are unspecified:
  - (a) The variable. If depth is counted in q = e^{2πiτ}, then 18 ≥ 1/3 and the depth suffices. If it is counted in a local parameter, the q-exponent reached is 18/140 = 0.129 for q^{1/140}, or 18/980 = 0.018 for q^{1/980}. Both are below 1/3, so the depth is **insufficient**. In those units the bound is B = 140/3 ≈ 46.7 or 980/3 ≈ 326.7.
  - (b) The components. Prop 1.1 needs all Ind components, which are the expansions at all 56 cosets, i.e. all cusps of Γ₀(49). A truncation of only the ∞-cusp expansion is NOT covered. For that, a Γ₀(49) Sturm-type bound (scalar, index 56: 4·56/12 ≈ 18.67 > 18) would be needed per component, plus a Written argument for the vector case. Note that 18 < 18.67, so even that route does not certify depth 18 at a single cusp.

## Owner next Write would need
1. L1, Written: ρ̄|cusp6 is a congruence type of level dividing 140.
2. L2, Written: the induction identification with the project convention.
3. L3, Written: depth-18 is defined as all Q-exponents n ≤ 18 in q = e^{2πiτ}, across all 336 Ind components (all cusps of Γ₀(49)).

Given L1–L3, Prop 1.1 yields B = 1/3 ≤ 18 and q^18 certifies uniqueness in the 89-dim space. If L3 instead means ∞-cusp only, depth 18 is NOT certified by any bound found here.

## Housekeeping
- No Fourier coefficients built. Sage not run, since B is closed-form.
- **Module q^18 coefficient build remains HELD** until Owner reviews this FINDINGS.
- invent HOLD. No tip fold. The Card1F track was not touched. Bridge PARTIAL READY NO. Soft SF F3 CLOSED.
- Tip end: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91. tip_touched NO.
