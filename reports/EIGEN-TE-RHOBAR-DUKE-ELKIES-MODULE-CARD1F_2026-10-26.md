# Card1F FINDINGS: ρ₅/ρ₇ exact match to Duke/Elkies seeds, plus the cusp6 module (2026-10-26)

**STATUS: PARTIAL.** ρ₅ MATCH, ρ₇ MATCH, ρ₄ MATCH (carried over from Card1E). The Step3 module is HELD-GATE-ABSENT-CITE.

## Authority shas (re-verified before writing)
- OW Card1F 03227e614d20e1f33fa342fa1de77cf0b4d6394ac5d698466d70b7d134bc0f59 OK
- Card1E b3429b70… OK · Card1D 6e8c901c… OK · local_factors.sobj 68d2ffc1… OK · factor.log 1d0e4162… OK · V42_exact d1e532c8… OK · ST_W a86980cf… OK
- Tip Soft SF LOCK: start sha = end sha = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91. **tip_touched NO**

Method: exact linear algebra in CyclotomicField(420) ⊃ CF(140). CF(420) is used only so the twelve η-twist characters fit: χ_k(T)=e(k/12), χ_k(S)=e(−3k/12), η^{2k}, k=0..11. Every intertwiner found has entries in CF(140): ζ₇=z^60 and ζ₅=z^84. Each match was checked by assertion P⁻¹·S_class·P == S_target and P⁻¹·T_class·P == T_target.

## ρ₇: MATCH to the dual Klein representation, no η-twist
- Seed used: Elkies (1.2)/(1.3) as written in OW §2a, ρ(g)=diag(ζ⁴,ζ²,ζ) and ρ(s). Checked exactly: ρ(s)²=1 and (ρ(s)ρ(g))³=1.
- The dual is ρ* = transpose-inverse, so T-exponents become {3,5,6}/7.
- Result: there is exactly one intertwiner up to scalar (dim Hom = 1) between ρ* and (S7,T7) from factor.log, with η⁰. P7 is in intertwiners.sobj and printed in rho7.log.
- The undualized Elkies ρ has no match under any of the twelve twists, as expected.

## ρ₅: MATCH, derived from Duke Prop.2 (OW §1b). Duke never writes this matrix (OW §1c); the steps are below.
- **OW §1a gap, recorded as evidence:** the 2×2 matrix T=(1/√5)[[ζ⁴−ζ³, ζ³−ζ²],[ζ³−ζ², ζ⁴−ζ]] as transcribed in the OW has det ≠ 1 and is not unitary (computed exactly). So it is not in SU(2) and generates no finite group, and it cannot serve as a seed in that form. The internal identity W=TS does hold. It is not used.
- **Derivation from the Prop.2 Möbius action:**
  - r(−1/τ) gives M=[[−(1+√5),2],[2,1+√5]], with M² = (10+2√5)·I.
  - r(τ+1)=ζr gives diag(ζ,1).
  - Projective lifts: S′ = M/(2(ζ−ζ⁴)) and T′ = ζ²·diag(ζ,1) = diag(ζ³,ζ²). These scalars are a normalization choice; they are not literature data.
  - Checked exactly: S′² = −1 and (S′T′)³ = S′², so S′ and T′ satisfy the SL₂(ℤ) relations.
- Result: one intertwiner (dim Hom = 1) to (S5,T5), with sign +1 and η⁰. The entries lie in Q(ζ₅) ⊂ CF(140). P5 is in rho5_matches.sobj and printed in rho5.log.
- No sin-matrix and no Fourier data were invented. ρ₅ is fixed up to the normalization scalar, which the matching itself forces.

## Step3: ℂ[E₄,E₆]⊗Ind module through q^18 vs dim 89 — NOT BUILT (HELD-GATE-ABSENT-CITE)
- Held on parent/Owner steer. The q^18 depth-cite FINDINGS landed as ABSENT (sha ac68cf8f6641bbe2c2c884209e0ac92f9ad71b17c24a5479638e63d893177a99).
- The q18 Sturm card (OW 6232cb55…) is pending Owner review.
- No coefficients were computed and none were invented.
- What is now in place for the module: all three local factors ρ₄⊗ρ₅⊗ρ₇ are identified exactly with classical seeds (η¹⁸ · Duke-Prop.2 · Elkies-dual).

## Artifacts (eigen-card1f/)
- ad2eb00895c968357af14ed65154d725b7e568282adfefde33ebfb9695a48fb7  match.sage
- 1291be27f2e9c9430be24ab884b18b7b9a9765b8e38880a10787e2022c4cdf10  rho7.log
- 8a0d10d6bd711695dbd87daf4c6ba0d378046ad457b7f44a363d9949a3df8011  intertwiners.sobj
- 4b08af30108dd37073a6c8ccd14ee7c03b25d01ac12b83b7c22e67aa5f79f4e4  rho5b.sage
- 5cf01b124d4a55c492e9fe5ed24ec7d67f79421927241618c3caf7f64d648878  rho5.log
- f2e4f2199e1b60e10d335975bef40043f3356089976d75f31becf78747b26fcd  rho5_matches.sobj

## Next unblock (one Owner Write)
An OW that releases the Step3 module build (Sturm-bound q-depth justification accepted). It should authorize ℂ[E₄,E₆]⊗Ind_{Γ₀(49)} generators for ρ̄|cusp6 at the Owner-approved depth and comparison to dim 89. It should also confirm that the S′ normalization scalar 1/(2(ζ−ζ⁴)) is accepted as a derived lift.
