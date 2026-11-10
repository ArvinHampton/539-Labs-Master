# MR2 FINDINGS — Archimedean-only residual correlation: tip `residual_factor` ∈ V₄₂ vs Zwegers / ĝ residual — 2026-10-26 (America/Chicago)
Authority: COOK LOCK OW `OWNER_WRITE_LET_THEM_COOK_EIGHT_PURSUE_OWN_RECS_2026-10-26.md` sha 08c8cdb9f851f85add943c18705a77c4de899464e29c9389e1663a42dcc05411 (MATCH); Invent/proof OW ef6da7e7…; prior MR2 FREE-PURSUE FINDINGS sha 0bc25f00c31d09492d2b9c53c8253a5d6a7379a7dc3d3623edc062dfbb5774b4 (MATCH, cited). Eight-only. Kerr/Path4 C2–C3 BLOCKED. No Eigen/Ops. Cat-A gate OFF.
tip Soft SF LOCK `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before AND after; tip_touched NO (read-only).

**STATUS: PARTIAL** (type/weight/representation compatibility PROVED; identity PROVED-ABSENT as stated; conditional Bruinier–Funke correlation PROVED as a conditional proposition; unconditional correlation UNPROVEN — GAP-A1..A4). Does NOT claim P5a. Bridge PARTIAL, READY NO.

Non-archimedean cite (one line, not reopened): F1 (sha 0bc25f00…) proved BT/Teitelbaum residual (place p=7) is distinct from both Zwegers residual and tip residual_factor; nothing below touches the tree.

## (a) What pursued
Archimedean place only. Tip data used (read-only, tip §1b, P1, §1r/PF-1): residual_factor := (u_{α,β}) ∈ V, dim V = 42, V ⊂ ℂ[N₂′/N₂], N₂ Gram [[2,14],[14,28]], signature (1,1), A_N₂ ≅ ℤ/2×ℤ/70; ρ = ρ_N₂|_V restricted (Owner-Written) to G = Γ₀(49); k = −2; trivial multiplier; ρ(−I)=S_lab⁻² = Id on V₄₂; "leading radial order only". Zwegers/ĝ side: standard harmonic-Maass decomposition F = F⁺ + F⁻, ξ_k F = 2i y^k \overline{∂_τ̄ F} (Bruinier–Funke 2004; Zwegers 2002 thesis; cite-only). On-disk Zwegers corpus: `FINDINGS_PR2_VANISHING_RANK27_ZWEGERS_2026-10-26.md` (route obstruction-closed 1d8e558, "No level/multiplier/shadow"), `U1_GS_ZWEGERS_Mixed_Scale_Not_Congruence_2026-08-21.md` (g_s mixed-scale, not Zwegers input). No Owner physics claims used.

## (b) Findings
### A1 — PROVED: type non-identity (archimedean)
The Zwegers/ĝ residual is a real-analytic non-holomorphic function on 𝔥 (the completion term F⁻, or Zwegers' R / erf-correction), equivalently its shadow ξ_kF, a holomorphic function. Tip residual_factor is a **vector** in V (a constant, leading-radial-order datum, not a function of τ). An element of V and an element of C^∞(𝔥, V) are different types; no identity "residual_factor = Zwegers residual" holds as stated. ∎ (Correlation can only be via a map V ↔ coefficient data, see A3.)

### A2 — PROVED: weight/representation compatibility of a hypothetical shadow
Suppose the residual-C field F is a harmonic Maass form of weight k = −2 for (Γ₀(49), ρ), ρ valued in V. Then:
1. ξ_{−2}F is holomorphic of weight 2−k = **4** for the conjugate representation ρ̄ on V̄ (standard: ξ_k maps H_k(ρ) → M^!_{2−k}(ρ̄)). ∎
2. Parity consistency: for −I ∈ Γ₀(49), a nonzero form requires ρ(−I) = (−1)^k Id on its value space. k = −2 even and ρ(−I) = Id on V₄₂ (tip PF-1) ⇒ no obstruction for F; ρ̄(−I) = Id and weight 4 even ⇒ no obstruction for the shadow. ∎ (Compatibility only; existence not shown.)
3. Leading radial order: F⁻ has expansion c⁻(α,0)·y^{1−k}/(1−k)-type constant term plus terms Γ(1−k, 4π|n|y)q^n decaying exponentially. For k=−2 the only non-decaying non-holomorphic term is ∝ c⁻(α,0) y³. Hence at "leading radial order" the archimedean (Zwegers-type) residual reduces to the vector (c⁻(α,0))_α ∈ V, which is the **only** slot in which a V-vector-to-V-vector comparison with residual_factor is type-correct. ∎ (Standard Fourier expansion; cite BF 2004 Prop. 3.2.)

### A3 — PROVED (conditional): Bruinier–Funke pairing correlation
If residual_factor is identified with the principal-part (or constant-term) coefficient vector of such an F, then for every g ∈ M_4(ρ̄), {g, ξ_{−2}F}_Pet = Σ_α Σ_{n≤0} c⁺(α,n) b_g(α,−n) (BF pairing). So residual_factor correlates with the Zwegers shadow **exactly through this pairing**, and residual_factor is determined only modulo the kernel coming from M_4(ρ̄) obstructions plus the cusp-form ambiguity already noted in tip l.561 (BF/DMZ non-uniqueness). ∎ conditional on the hypothesis, which is NOT a tip premise.

### A4 — PROVED-ABSENT: Siegel-theta span is not itself a Zwegers completion of the tip field
N₂ has signature (1,1); its Siegel theta Θ_{N₂}(τ) is non-holomorphic of weight (1/2,1/2) (total holomorphic weight b⁺−b⁻ = 0 Weil-type), and Zwegers' holomorphic indefinite theta for N₂ (cone c₁,c₂) completes at weight (b⁺+b⁻)/2 = **1**. Neither weight equals tip k = −2, so the V₄₂ span's own theta realisation is not the completion of the tip field at weight −2. Correlation can be through the shared Weil-rep **value space** ℂ[A_N₂] ⊃ V only, not through the functions. ∎

### GAPs (named, UNPROVEN)
- **GAP-A1:** No tip premise says the residual-C field is harmonic (Δ_k F = 0) or mock; A2/A3 are conditional on that.
- **GAP-A2:** No proof residual_factor = (c⁻(α,0)) or = principal-part vector; "leading radial order" in tip does not specify which.
- **GAP-A3:** dim M_4(Γ₀(49), ρ̄|_V̄) and the shadow existence (surjectivity of ξ onto it for this ρ) not computed — needs explicit ρ matrices (tip: blank) / newform decomposition (Eigen lane, not entered).
- **GAP-A4:** No construction of a Zwegers indefinite-theta for N₂ mapping into V₄₂ with weight shift to −2 (e.g. via raising/lowering or Rankin–Cohen); open.
- On-disk Zwegers route (1d8e558) supplies no level/multiplier/shadow, so the corpus gives no shadow to compare (ABSENT, per Rank-27 FINDINGS).

### G2 frozen
G2 (prior FINDINGS F2): Ω₀ = vol(Γ₀(49)\𝔥) = 56π/3 or C_vol' = (56π/3)^{−1/2} remains **named-UNPROVEN volume candidate only**. Archimedean note: the Petersson pairing in A3 is where a volume normalisation would enter, but no forcing is proved. NOT tip-folded; C_vol = 1 convention untouched.

## Not claimed
No P5a. Bridge PARTIAL READY NO. No Cat A. No tip edit. No ρ matrices, no coefficients, no numeric C_vol.

## Soft SF risks
1. A2/A3 could be misread as "tip field is mock modular" — they are conditional (GAP-A1).
2. Weight-1 Zwegers N₂ theta (A4) vs tip k=−2 — do not conflate via shared ℂ[A_N₂].
3. Petersson/volume appearance in A3 must not be read as forcing G2 / C_vol'.
4. ρ̄ vs ρ (dual on shadow) — any future fold must track conjugation.

Soft SF press needed: **yes** (Auditor on ship).
tip_touched: **NO**
