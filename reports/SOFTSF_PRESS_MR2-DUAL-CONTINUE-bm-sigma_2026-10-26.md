# SOFTSF_PRESS — MR2 FINDINGS — DUAL CONTINUE — BM σ-lists for the endpoint residuals of 7.4.a.a (Paškūnas Prop 6.20 / Rem 6.2) — 2026-10-26
STATUS: PARTIAL (MR2 lane). Option A, from the on-disk paper only. Option B (Hu–Tan, for L₁) NOT done. Submitted for Auditor Soft SF + Eigen R5. Dual-label: filtration 10∥40 BOTH NAMED PARALLEL, NO PICK. No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. G1 BLOCKED, no OMS / L₇. No tip fold. tip_touched NO.
Builds on: residual-mult-bm 0e00b2d2… (SF-M1/M2; Eigen R5 ACCEPT cbcccf4d…), kappa7-tres fd5e0dc1… (SF-K2/K5). Source: lit/bm/1209.5205.txt. No Sage. p = 7, K = GL₂(Z₇).

Quoted results:
- Prop 6.20 (non-generic, ρ̄ ≅ (ω *; 0 1)): "If ρ is très ramifié then M(σ) ≠ 0 iff σ ≅ st ≅ Sym^{p−1}k². If peu ramifié then M(σ) ≠ 0 iff σ = 1 or σ = st." Twisting by χ is compatible (§6.2: "V̌ compatible with twisting; may assume χ trivial").
- Rem 6.2 (generic reducible): ρ̄ ≅ (χ₁ *; 0 χ₂ω^{r+1}) ⊗ ω^m, with χ₁, χ₂ unramified, χ₁ ≠ χ₂ω^{r+1}, 0 ≤ m ≤ p−2.
  - soc_K π = Sym^r ⊗ det^m if 0 < r < p−1.
  - soc_K π = det^m ⊕ Sym^{p−1} ⊗ det^m otherwise.
  - soc_K π is multiplicity-free.
  §6.1 (37): M(σ) ≠ 0 iff Hom_K(σ, soc_K π) ≠ 0, and then that Hom is 1-dim.

Soft SF facts:
- SF-S1 (PROVED, from SF-K2/K5 and Prop 6.20 + twist): L₀ ≅ ω ⊗ (ω *; 0 1) with * TRÈS ramifié, so the σ-list is EXACTLY {Sym⁶k² ⊗ det}, a single weight.
  The peu-ramifié alternative {det, Sym⁶ ⊗ det} is EXCLUDED by κ(7) très (SF-K2).
- SF-S2 (PROVED, from SF-K5 and Rem 6.2): L₂ ≅ ω ⊗ (1 *; 0 ω), i.e. χ₁ = χ₂ = 1, r+1 = 1 so r = 0, and m = 1.
  This is the only normalisation with χ₁ unramified mod (p−1) = 6. The generic condition 1 ≠ ω holds.
  r = 0 is the "otherwise" case, so the σ-list is EXACTLY {det, Sym⁶k² ⊗ det}, two weights, each with 1-dim Hom (multiplicity-free).
- SF-S3 (PROVED, from SF-M2, S1, S2): every listed σ has z(σ, ρ̄) ≠ 0 with HS-multiplicity 1. All other irreducible σ of K have z(σ) = 0.
- SF-S4 (PROVED, comparison): Sym⁶ ⊗ det lies in both lists. det is in L₂'s list only. So the endpoints are distinguished by exactly one weight, det.

Convention caveat (for the Auditor): the twist ω^m ↔ det^m uses Paškūnas's local class field theory and V̌ normalisation as quoted. Under the opposite (dual) convention, every det-twist exponent flips sign (det^{±1}). The list sizes (1 vs 2) and S4 do not depend on the convention.

Named gaps:
(1) Hu–Tan arXiv:1309.1658 (split L₁): not downloaded or ingested this wave.
(2) Linking the weight Sym⁶ ⊗ det (Serre weight k = 8 after twist) to the filtration question: NOT done, deliberately. Filtration stays 10∥40 NAMED PARALLEL, NO PICK.
(3) L₇: G1-adjacent, not attempted.
Does NOT use: filtration pick, L₇ unit, OMS lift. Not folded into tip.
