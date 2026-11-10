# SOFTSF_PRESS — MR2 FINDINGS — DUAL CONTINUE — Paškūnas BM APPLIES to both endpoint residuals of 7.4.a.a (L₀ non-generic très ramifié, L₂ generic); split L₁ falls under Hu–Tan (OPEN) — 2026-10-26
STATUS: PARTIAL (MR2 lane). Option B done, plus a short Option A. Submitted for Auditor Soft SF + Eigen R5. Dual-label: filtration 10∥40 BOTH NAMED PARALLEL, NO PICK. No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. G1 BLOCKED, no OMS / PS #20 / L₇. No tip fold. tip_touched NO.
Builds on: kappa7-tres fd5e0dc1… (SF-K2–K5; Eigen R5 ACCEPT 6b2b9a24…), end-seg 0111d12e… (SF-H4–H6), resid-reducible c358d9e6… (F5). No Sage.
Lit (on disk): lit/bm/1209.5205.txt (Paškūnas, "On the Breuil–Mézard conjecture", v3 2014). Quotes below are from the intro (lines ~45–60, 150–182) and §6 (lines ~2605–2630).

Paškūnas hypotheses, as quoted:
- ρ̄: G_Qp → GL₂(k) continuous, with End_{G_Qp}(ρ̄) = k. Abs-irreducibility is NOT required.
- Thm 1.1: p ≥ 5. Conclusion: potentially semistable / crystalline deformation rings exist, and cycles z(σ, ρ̄), independent of (w, τ), satisfy the BM cycle identity.
- z(σ, ρ̄) has Hilbert–Samuel multiplicity 1 when nonzero, with one exception: multiplicity 2 when ρ̄ ≅ (ω *; 0 1) ⊗ χ with * PEU ramifié.
- §6: ρ̄ is "generic" if irreducible, or ≅ (χ₁ *; 0 χ₂) with χ₁χ₂⁻¹ ≠ 1, ω. Otherwise, under End = k, it is "non-generic" ≅ (χω *; 0 χ).
- Non-scalar split ρ̄: Hu–Tan, arXiv:1309.1658 (cited by Paškūnas, NOT on disk).

Hypothesis table for ρ_{f,7}|G_Q₇, by lattice:
- P1 p ≥ 5, base field Q_p: p = 7, local field Q₇. MATCH (all lattices).
- P2 End_{G_Q₇} = k:
  - L₀: MATCH (SF-H4).
  - L₂: MATCH (SF-H4).
  - L₁: FAIL (End = k×k, SF-H6).
- P3 generic / non-generic class:
  - L₀ ≅ (ω² *; 0 ω) = ω ⊗ (ω *; 0 1), so χ₁χ₂⁻¹ = ω: NON-GENERIC (§6.2). MATCH.
  - L₂ ≅ (ω *; 0 ω²), so χ₁χ₂⁻¹ = ω⁻¹ ≠ 1, ω (ω has order 6): GENERIC (§6.1). MATCH.
- P4 multiplicity exception (peu ramifié):
  - L₀: * = κ(7), which is TRÈS ramifié (SF-K2). So the exception does NOT occur, and HS-multiplicity of z(σ) = 1 whenever it is nonzero. MATCH.
  - L₂: not of the form (ω *; 0 1) ⊗ χ, so the exception does not apply. MATCH.
- P5 Hu–Tan, for L₁ (non-scalar split ω|⊕ω²|): OPEN (paper not ingested).

Soft SF facts:
- SF-M1 (PROVED from quoted hypotheses and SF-H4/K2): Paškūnas Thm 1.1 (the BM cycle identity, with cycles z(σ, ρ̄) independent of the type) applies to ρ̄_{L₀}|G_Q₇ and to ρ̄_{L₂}|G_Q₇.
- SF-M2 (PROVED): for both L₀ and L₂, every nonzero z(σ, ρ̄) has multiplicity exactly 1. For L₀ this relies on très ramifié (SF-K2): had κ(7) been peu ramifié, it would have been 2.
- SF-M3 (PROVED, CORRECTION): resid-reducible F5 said "any BM / Paškūnas step requiring abs-irr does not apply". Paškūnas requires only End_{G_Qp}(ρ̄) = k, not abs-irreducibility. The abs-irr obstruction is therefore REMOVED for the two endpoint lattices. It remains only for L₁ (End = k×k), and only through Hu–Tan (OPEN).
- SF-M4 (PROVED, Option A): there are exactly 3 local residual objects (SF-K5). The BM-applicability profile is L₀ MATCH / L₁ FAIL / L₂ MATCH. So any residual multiplier that is defined through a Paškūnas BM cycle has exactly two admissible inputs, L₀ and L₂, each with multiplicity-one cycles.
  The two inputs are NOT interchangeable: L₀ is non-generic (§6.2) and L₂ is generic (§6.1).
  Which one (if either) a residual-C / Ω₀ / f_warp / f_curv multiplier should use is OPEN. It is NOT forced by the proved inputs, and no filtration or lattice is picked here.

Named gaps:
(1) The explicit list of σ with z(σ, ρ̄) ≠ 0 (that is, Hom_K(σ, β) ≠ 0 for Colmez's atome automorphe β) for L₀ and L₂: not computed.
(2) Hu–Tan 1309.1658 for L₁: not ingested.
(3) Link to the value of L₇: G1-adjacent, not attempted.
Does NOT use: filtration pick, L₇ unit, OMS lift. Not folded into tip.
