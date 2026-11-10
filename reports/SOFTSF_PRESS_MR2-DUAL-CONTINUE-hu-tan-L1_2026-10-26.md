# SOFTSF_PRESS — MR2 FINDINGS — DUAL CONTINUE — Hu–Tan BM applies to split L₁ = ω⊕ω² (NON-GENERIC: a twist of 1⊕ω), plus a FLAGGED convention conflict on bm-sigma SF-S2 — 2026-10-26
STATUS: PARTIAL (MR2 lane). Submitted for Auditor Soft SF + Eigen R5. Dual-label: filtration 10∥40 BOTH NAMED PARALLEL, NO PICK. No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. G1 BLOCKED, no OMS / L₇. No tip fold. tip_touched NO.
Builds on: bm-sigma c72bae05… (Eigen R5 ACCEPT 9cfae245…), residual-mult-bm 0e00b2d2…, end-seg 0111d12e… (SF-H6), kappa7-tres fd5e0dc1….
Lit ingested: lit/1309.1658.pdf + .txt (copies in lit/bm/). Hu–Tan, "The Breuil–Mézard conjecture for non-scalar split residual representations", arXiv v2 2014.

Quoted (Hu–Tan):
- Notation: p ≥ 5.
- Thm 1.3: for ANY ρ̄: G_Qp → GL₂(F) isomorphic to a direct sum of two distinct characters, there are cycles Z_{n,m}, independent of (k, τ, ψ), such that Z(R^ψ(k,τ,ρ̄)/ϖ) = Σ a_{n,m}(k,τ) Z_{n,m}. The crystalline version also holds. Here σ_{n,m} = Sym^n ⊗ det^m.
- Generic means χ₁χ₂⁻¹ ∉ {1, ω^{±1}} (Rem 5.7, 3.12). Non-generic means ρ̄ ≅ 1⊕ω up to twist (Thms 5.11, 5.12).
- Thm 5.11, for ρ̄ = 1⊕ω: Z = a_{p−3,1}·p₁ + a_{0,0}·p₂ + a_{p−1,0}·(p₂+p₃). Thm 5.12 gives the same shape for crystalline rings.
- Cor 5.10: p₂, p₃ match the two minimal primes of the PEU-ramifié ring, with e(R^peu/ϖ) = a_{0,0} + 2a_{p−1,0}.

Hypothesis table for L₁ (ρ̄_{L₁}|G_Q₇ ≅ ω|⊕ω²|, split, End = k×k by SF-H6):
- HT1 p ≥ 5, base field Q_p: p = 7, local field Q₇. MATCH.
- HT2 direct sum of two DISTINCT characters: ω ≠ ω² on G_Q₇, since ω|I₇ has order 6. MATCH.
- HT3 generic / non-generic: χ₁χ₂⁻¹ = ω⁻¹ ∈ {ω^{±1}}, so NON-GENERIC. L₁ = ω ⊗ (1⊕ω), the twist case of Thms 5.11/5.12. MATCH.
- HT4 twist compatibility: the BM cycles shift under twisting by a character, σ_{n,m} ↦ σ_{n,m+1} for a twist by ω ↔ det (HT conventions). MATCH (standard). The sign of the det exponent depends on convention; see caveat.

Soft SF facts:
- SF-T1 (PROVED, HT1–HT3): Hu–Tan's Thm 1.3 BM cycle identity, both potentially semistable and crystalline, APPLIES to L₁. With residual-mult-bm SF-M1, BM now applies to ALL THREE lattices: L₀ and L₂ via Paškūnas, L₁ via Hu–Tan. This UPDATES SF-M4, where L₁ was FAIL; the FAIL was an artifact of End = k×k under Paškūnas's hypothesis only.
- SF-T2 (PROVED, Thm 5.11 + twist HT4): the σ-list for L₁ is {σ_{p−3,1}, σ_{0,0}, σ_{p−1,0}} twisted by det, i.e. {Sym⁴⊗det², det, Sym⁶⊗det} for p = 7. The cycles are Z_{4,2} = p₁, Z_{0,1} = p₂, Z_{6,1} = p₂+p₃.
- SF-T3 (PROVED): multiplicity-one FAILS for L₁. Z_{6,1} = p₂+p₃ is a sum of two distinct components. This contrasts with L₀ and L₂ (SF-M2, all multiplicity 1).
- SF-T4 (PROVED, Cor 5.10): the p₂, p₃ part of L₁'s cycle is the PEU-ramifié non-split ring's cycle, not the très-ramifié one. The global endpoint L₀ is TRÈS (SF-K2). So L₁'s BM cycle does NOT decompose as L₀ + L₂: Z(L₁) ≠ Z(L₀) + Z(L₂) as weight lists.

FLAGGED CONFLICT (for Auditor / Eigen; NOT resolved, NOT promoted):
- In standard Serre-weight conventions (ρ̄|I ≅ (ω^{r+1} *; 0 1) has weight Sym^r), Hu–Tan's p₁ term σ_{p−3,1} is the weight of the extension (1 *; 0 ω) of ω by 1. Under that reading, L₂ = ω ⊗ (1 *; 0 ω) would have the SINGLE weight Sym⁴⊗det².
- bm-sigma SF-S2 instead read Paškūnas Rem 6.2's matrix (χ₁ *; 0 χ₂ω^{r+1}) literally and got {det, Sym⁶⊗det}. That is the weight list of the PEU-ramifié twist of L₀'s orientation, which suggests Rem 6.2's matrix is in a dual (V̌) convention.
- Recommendation-free statement: SF-S2 should be treated as CONVENTION-DEPENDENT / possibly inverted until the Auditor checks Paškūnas's V̌ / CLFT normalisation against Prop 6.20. SF-S1 (L₀ = {Sym⁶⊗det}) is unaffected: Prop 6.20 agrees with the standard convention, since the peu case gives {1, st}.
- SF-S4 ("endpoints differ by exactly det") depends on S2 and is therefore also flagged.

Named gaps:
(1) Resolving the SF-S2 convention: re-derive from Paškūnas §5 / Colmez's V̌ normalisation, or from Buzzard–Diamond–Jarvis. OPEN.
(2) Relating L₁'s peu-type p₂, p₃ components to the actual global très lattice L₀: no claim.
(3) L₇: G1-adjacent, not attempted.
Does NOT use: filtration pick, L₇ unit, OMS lift. Not folded into tip.
