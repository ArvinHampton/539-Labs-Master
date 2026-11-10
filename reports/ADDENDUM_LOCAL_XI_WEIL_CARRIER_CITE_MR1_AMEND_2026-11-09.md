# ADDENDUM — Local Path: citation update for the Ξ Weil-carrier file after MR1's amendment — 2026-11-09

- Amends citations only in reports/FINDINGS_LOCAL_DERIVE_XI_WEIL_VECTOR_CARRIER_FRICKE_PLUS1_DICTIONARY_2026-11-09.md (sha ae951f3e7aa5be4b3829cc34fa29ea2d841ff08bff09529b4bf7f4c7effbb091). That file is not edited.
- Written ~3:25 PM CST (America/Chicago). Additive new file. Tip 7cddb188… untouched (read-only; re-checked). No CERT. Nothing sent outside.

## 1. New citation
- reports/FINDINGS_MR1_B_SEC3_APPELL_RC_S2_S4_AMEND_PP_AUDIT_2026-11-09.md. Full sha256 0ea030aee260983add0c3e9f14b79a4a814f8e1b8a7c75ae2b43e2f76d4ed0fa, verified; it matches its sidecar. Cited as "MR1-AM".
- Wording verified in MR1-AM:
  - **R1** PROVED, PARI-certified (:9, :25).
  - **R2** "Λ₀ = √(7/8)·L(1,χ₁₄₀)" is still PROVED. Its basis is now the PARI-certified h(140) = 2 plus the class number formula (:10, :26).
  - **S2a** is "CLOSED BY DEFINITION" (:11, :27).
  - **S3b** reads "1.59543 ≠ κ: PROVED; B's value SUPERSEDED; B's Appell–Lerch evaluation OPEN" (:12–14, :31).
  - The **Weil(140) tie** (the original MR1 line 26, "ties it to the Weil(140) side of Local's O1/O2") is a REMARK, not a result (:19, :37).
- Precision note: MR1-AM classes the *identity* Λ₀ = √(7/8)·L(1,χ₁₄₀) as PROVED (R2). Only its *interpretation* as a tie to Weil(140) is a REMARK.
- **Replacement of the "MR1" citations.** In ae951f3e, every citation "MR1" refers to FINDINGS_MR1_B_SEC3_APPELL_RC_S2_S4_CLOSE_ADOPTED_DEFS_2026-11-09.md (48a2d687…), at lines :22, :24–25 and :42. These now read "MR1 (48a2d687…), as amended by MR1-AM (0ea030ae…)". MR1-AM's R1/R2 supersede the basis of :22 and :24–25. MR1 :42 (the √(7/8) normalization OPEN) is not changed by MR1-AM.

## 2. Status of the Λ₀–χ₁₄₀ identity (Local)
- **PROVED independently by Local.**
  - K = ℚ(√35) has discriminant 140, O_K = ℤ[√35], fundamental unit 6+√35 (norm +1) and h(K) = 2.
  - The Dirichlet class number formula gives L(1,χ₁₄₀) = 2h·Reg/√140 = 4·ln(6+√35)/√140.
  - Hence √(7/8)·L(1,χ₁₄₀) = 4·Reg·√7/(√8·√140) = Reg/√10 = Λ₀.
  - Local's numeric recheck in ae951f3e §0 gives h = 2.0000 from the finite formula. h = 2 itself is cited from MR1-AM's PARI certification.
- **Local's use of χ₁₄₀ in the dictionary does not depend on MR1's remark.**
  - Dictionary item 2 of ae951f3e is Local's own result: ρ_{N₂}(γ)e₀ = χ₁₄₀(d)·e₀ on Γ₀(140), from the explicit Weil matrices.
  - Item 6 assigns Λ₀ to the "χ₁₄₀ data" through the PROVED identity, not through the REMARK.
  - The link "Λ₀ ↔ Weil(140)" is therefore a consequence of two PROVED facts: R2, and the e₀-character. It is not an extra claim. Its physical or structural meaning, i.e. why √10, stays OPEN, as in ae951f3e.

## 3. Rollup effect on ae951f3e
**No change: PROVED 12 · CONDITIONAL 1 · OPEN 3 · REFUTED 1.**
- The item "Λ₀ = √(7/8)L(1,χ₁₄₀) recheck" stays PROVED. Its basis is the class number formula with h = 2, now PARI-certified per MR1-AM.
- No ae951f3e item relied on MR1's S2a, S3b or the Weil(140) remark.

No CERT. Tip untouched.
