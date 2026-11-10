# NL DERIVED: D6 stage 3 (a), E3: electric G₀₁₂₃ on the face
2026-11-09, 2245 CST (America/Chicago). **NL derived proposal.** Additive only. Authority: OW t4426 d5eaeef3 and OW t4436 32881263…. Inputs: 2216 (f504d1b9…), PP f530cbc0…, Erratum 23 (4bdfb71c…). Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged.** No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after.
Script: /workspace/nl-d6s3/e3_electric_lemma.py (4bb21ed1…, sidecar frozen before the run), log sealed after.

**Tally: PROVED 3 · CONDITIONAL 0 · OPEN 0 · REFUTED 0 · total 3.** **No candidate wall.**

- **S3a-1 (PROVED; analytic, with a float cross-check).** Take the 11D KSE x-row for a 4D-Poincaré warped face (flat x, x-independent ε) carrying internal flux and G₀₁₂₃ = e.
  - Write the x-row as Oε = 0, with O = H − (κe/3)Γ^{0123}. Here H = Γ^y∂_yA + (1/144)G̸_int and κ = ±1 is a convention sign. The electric term comes from −8δΓ^{PQR}G_{μPQR}/288, with Γ_μ^{NPQR}G^{el} = 0.
  - H is Hermitian and commutes with Γ^{0123}, which is anti-Hermitian with (Γ^{0123})² = −1. Therefore **O†O = H² + e²/9**.
  - Check: 20 random full internal 4-forms, warps and values of e gave max deviation 1.8×10⁻¹⁵, and σ_min(O) ≥ 1.89·|e|/3.
- **S3a-2 (PROVED, as an implication).** Premises:
  - the kept side is 4D-Poincaré-invariant, so the only flux components allowed are internal ones and G₀₁₂₃ (no invariant tensors with 1–3 x-legs);
  - the wall preserves at least one x-independent (Poincaré) Killing spinor.

  Then **G₀₁₂₃ = 0 wherever ε ≠ 0**. A nonzero parallel section of the supercovariant connection vanishes nowhere, so this holds on the whole kept side, including the face.
- **S3a-3 (PROVED).** **The E3 escape is closed.** Electric flux cannot supply what f₄ = ω₂ = 0 removes, because it must vanish identically.
  - The argument uses no SO(3)_R, U(1)_R or Σ-uniformity assumption, so it applies in **[χS], [χU] and [w]** alike.
  - Under OW t4436, branch E3 is **dropped** on a PROVED result. The only premise kept is that the preserved supercharges are Poincaré (x-independent).

Tally check: 3 + 0 + 0 + 0 = 3. Branches: E3 dropped. [χS], [χU] and [w] are kept.
Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
