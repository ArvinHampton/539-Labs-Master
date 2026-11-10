# PP-FINDINGS — Hecke arithmetic correction audit (2026-11-03)
Target: reports/OWNER_WRITE_HECKE_ARITHMETIC_CORRECTION_2026-11-03.md sha256 b8101db7fffdf6b732a17c4fd06f763b880b31eafce958f0a41c19d17268c80b (prefix b8101db7 VERIFIED).
Script: scripts/hecke_arithmetic_correction_audit_2026-11-03.py. Prior: PP-FINDINGS-HECKE_DEFORMATION_AUDIT_2026-11-03.md. No CERT. Tip read-only.

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1a | Split (140/p)=+1, p<60: 13,17,19,23,29,31,43,59 | CONFIRMED | Kronecker computed; exact, none missing |
| 1b | Inert: 3,11,37,41,47,53 | CONFIRMED | exact |
| 1c | Ramified: 2,5,7 | CONFIRMED | p∣140 |
| 1d | Range | NOTE | 61 is next prime (>60, inert, (140/61)=−1); correctly excluded |
| 2a | Field Q(√35), disc 140 | CONFIRMED | 35≡3 mod 4 ⇒ d_K=140 |
| 2b | Space = Hilbert modular forms over Q(√35) | CONSISTENT (underspecified) | h=2, h⁺=4 (reduced-form cycles). ε=6+√35, N(ε)=+1, no unit of norm −1 (7≡3 mod 4), so h⁺=2h. Hilbert forms live on h⁺=4 components (Cl⁺ ≅ narrow group); T_𝔭 permutes components by [𝔭]∈Cl⁺. Level, weight (parallel k?), character not stated. Because N(ε)=+1, totally positive units vs squares matter for parallel weight (ε totally positive; ε a square? ε=((√5+√7)/√2)²·… — Owner should specify) |
| 3a | Θ_p uses (35/p) | DEFECT for p=2 | Kronecker (35/2)=−1 (35≡3 mod 8) but 2 ramified ((140/2)=0) ⇒ diag(2,0) treats 2 as inert. Odd p: (35/p)=(140/p) for all p<60 ✓. Fix: use (140/p) |
| 3a' | p=5,7: (35/p)=0 ⇒ diag(1,0) | UNSPECIFIED | Formula gives a nonzero "half" value at ramified primes; whether intended is not stated. With (140/·): 2,5,7 all → diag(1,0) uniformly |
| 3a'' | Θ_p=0 for split | CONFIRMED (algebraic) | 1−1=0 |
| 3b | M_𝔭 | ABSENT | Never defined (matrix? operator on which space? 𝔭 not unique for split p, but Θ=0 there; inert 𝔭=(p); ramified 𝔭²=(p)) |
| 3c | Θ_p ∈ 𝕋 | UNPROVEN / generically FALSE | 2×2 model: [diag(2,0), T] = [[0,2b],[−2c,0]]m ≠ 0 unless T diagonal (b=c=0). E.g. T=[[1,1],[1,1]] gives [[0,2],[−2,0]]. diag(·,0) is basis-dependent projection, not a Hecke polynomial unless basis is a Hecke eigenbasis |
| 3d | T̃_p ∈ 𝕋, pairwise commuting, multiplicative, closed | CONDITIONAL | If Θ_p ∈ 𝕋 (commutative): T_p+(Λ−Λ₀)Θ_p ∈ 𝕋 and exp((Λ−Λ₀)Θ_p) ∈ 𝕋⊗ℝ (finite-dim ⇒ exp is a polynomial), so commutativity holds. Multiplicativity (T̃_{pq}=T̃_pT̃_q, T̃_{p^{n+1}}=T̃_pT̃_{p^n}−N𝔭·T̃_{p^{n−1}}) NOT preserved in general: only defined at primes, Hecke recursion for prime powers not stated. Without Θ_p∈𝕋: counterexample 3c ⇒ commutativity fails |
| 3e | Deformation form | INCONSISTENCY | Owner file: linear T_p+(Λ−Λ₀)Θ_p; brief: T_p·exp((Λ−Λ₀)Θ_p). These differ beyond first order; Owner to choose |
| 4a | C₃ locked 1/2 | CONFIRMED | Matches prior Perron: χ(1)+χ(2)+½χ(3) = 1/2 for χ₃₅ and χ₁₄₀ |
| 4b | Λ₀=1.81 | ABSENT (asserted) | No derivation |
| 4c | P5a goal not theorem | CONSISTENT | Labelled as design goal |

## Owner clarifications needed
1. Replace (35/p) by Kronecker (140/p) (or specify p=2 case); state intended ramified value.
2. Define M_𝔭 and the space: level 𝔫, (parallel) weight, nebentypus, narrow-class components (h⁺=4).
3. Prove Θ_p ∈ 𝕋 (e.g. as polynomial in T_q / diamond / Atkin–Lehner) or work in an eigenbasis and say so.
4. Choose linear vs exponential deformation; state prime-power recursion.
5. Supply derivation of Λ₀=1.81.
