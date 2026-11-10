# MR2 FINDINGS — DUAL CONTINUE — Local Ext / End_{G_Q7} for ρ̄(7.4.a.a) mod 7 — PARTIAL — 2026-10-26
Advances beyond: c358d9e6… (ρ̄^ss ≅ ω⊕ω²); uses BM-JH 860f0139…, ABGT b04066dc…. Authority OW 9b993a72…; MR2 ACK 78f34b4e….
Soft SF Write-only → Auditor. No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. No tip fold.
Filtration BOTH NAMED PARALLEL, NO PICK: [Γ₀(7)-geometric] w(θ³f)=10 ∥ [Katz level-1] w(θ³f)=40. Nothing below depends on filtration.
Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188…dfc91 verified before/after; tip_touched NO.

## Status: PARTIAL (path A). End_{G_Q7} of the GLOBAL non-split lattice: still ABSENT (exact missing input named). New proved local facts below.

## Soft SF facts (proofs elementary from c358d9e6… + standard local Galois cohomology)
L1 [proved] (ρ̄|G_Q7)^ss ≅ ω|⊕ω²| (restriction of c358d9e6…), with ω|_{I_7} of exact order 6, so ω|G_Q7 ≠ ω²|G_Q7 (ratio ω^{-1} ≠ 1). Hence for ANY G_Q7-stable lattice, End_{G_Q7}(ρ̄) = k iff the local extension is non-split, = k×k iff split. (Local ρ̄ is never absolutely irreducible.)
L2 [proved, local Euler char. + Tate duality, p=7, k=F7] 
 h¹(G_Q7, ω) = h⁰(ω)+h⁰(ω⁰)+1 = 0+1+1 = 2 ; h¹(G_Q7, ω^{-1}) = 0+h⁰(ω²)+1 = 0+0+1 = 1.
 So Ext¹(ω, ω²) = H¹(ω) is 2-dim, Ext¹(ω², ω) = H¹(ω^{-1}) is 1-dim (unique non-split class, up to scalar).
L3 [proved, Ribet's lemma applied locally; V = ρ_{f,7}|G_Q7 = semistable non-crystalline V_{4,L}, a7=−7 (F3 of b04066dc…), irreducible since Hodge–Tate wts {0,3} and slope 1 ∉ {0,3}] The tree of G_Q7-stable lattices of V is a finite segment whose two endpoints have NON-SPLIT reductions, one of each orientation (sub ω², resp. sub ω). So End_{G_Q7}(ρ̄)=k holds for a suitable (local-endpoint) lattice — this discharges the End=k hypothesis of SF-3 (860f0139…) for that choice of lattice; BM multiplicity statement is lattice-independent only via Paškūnas Thm 1.1 hypotheses (CITE, 1209.5205), not re-checked here.
L4 [proved] G_Q-stable lattices ⊂ G_Q7-stable lattices; global segment ⊆ local segment. If equal, the global non-split lattice of c358d9e6… is locally non-split (End_{G_Q7}=k); if strictly smaller, its endpoint may be locally split.

## ABSENT (exact missing input)
- Whether the GLOBAL non-split lattice is LOCALLY non-split ⇔ comparing segment lengths ⇔ needs the precise reduction of V_{4,L} (Breuil–Mézard / Guerberoff–Park reduction for 3≤k≤p, boundary case v7(L)=0 at k=4), which depends on the unit residue L₇(7.4.a.a) mod 7 (= gap G1, overconvergent/OMS), plus the global segment length (congruence depth of f vs Eisenstein mod 7^n, not computed). Sage modular symbols/tables did not give it; no reduction-theorem PDF on disk in lit/ or lit/bm/ (formula not CITE-VERIFIED, deliberately not quoted).
