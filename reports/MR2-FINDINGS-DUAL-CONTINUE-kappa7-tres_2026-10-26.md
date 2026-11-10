# MR2 FINDINGS — DUAL CONTINUE — κ(7)|G_Q₇ is TRÈS RAMIFIÉ (closes end-seg gap (1) WITHOUT G1) — 2026-10-26
STATUS: PARTIAL (MR2 lane). Option C, done without G1, OMS or L₇. Submitted for Auditor Soft SF. Dual-label: filtration 10∥40 BOTH NAMED PARALLEL, NO PICK. No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. No tip fold. tip_touched NO.
Builds on: end-seg 0111d12e… (SF-H1–H6), catb2-lattice-seg af25c786…, local-ext-G7 (L2). No Sage needed.

Background (standard): ω is the mod-7 cyclotomic character, so F₇(ω) = μ₇. Kummer theory gives H¹(G_Q₇, ω) = Q₇^×/(Q₇^×)⁷ ≅ F₇², spanned by κ(7) and κ(8). Serre's "peu ramifié" line is the image of Z₇^×, which is the line κ(8); any class outside that line is "très ramifié". These notions apply to extensions 0→ω→E→1→0, and to their twists.

Soft SF facts:
- SF-K1 (PROVED): H¹(G_{Q,S}, ω) = ⟨κ(7)⟩ for S = {7, ∞}, computed directly over Q.
  Kummer theory over Q gives H¹(G_{Q,S}, μ₇) = Z[1/7]^×/7 ⊕ Cl(Z[1/7])[7] = ⟨−1, 7⟩/7 ⊕ 0 = ⟨κ(7)⟩.
  This agrees with end-seg SF-H1 and gives an explicit generator over Q itself.
- SF-K2 (PROVED): κ(7)|G_Q₇ is TRÈS RAMIFIÉ. In Q₇^×/7 we have v₇(7) = 1 ≢ 0 (mod 7), so κ(7) is not in the image of Z₇^×, i.e. not in the peu-ramifié line ⟨κ(8)⟩.
- SF-K3 (PROVED, from SF-K2 and end-seg SF-H3): the global endpoint L₀ (sub ω², quotient ω) has local reduction ρ̄_{L₀}|G_Q₇ ≅ ω ⊗ E_très, where E_très is the très-ramifié extension 0→ω→E→1→0 (class κ(7)). It is non-split (H4) and ramified. This closes end-seg named gap (1) without L₇.
- SF-K4 (PROVED): the other endpoint L₂ (sub ω, quotient ω²) has class in H¹(G_Q₇, ω⁻¹), which is 1-dim (L2). It is the unique non-split local class, and it is RAMIFIED, because H¹_ur(G_Q₇, ω⁻¹) = H¹(Ẑ, (ω⁻¹)^{I₇}) = 0, as ω⁻¹|I₇ ≠ 1. The peu/très distinction does not apply to this orientation.
- SF-K5 (PROVED, summary): the local residual picture of ρ_{f,7}|G_Q₇ is now completely determined up to isomorphism, with no further choices:
  - three lattices;
  - End rings k, k×k, k;
  - L₀ = ω⊗(très ramifié), L₁ = ω⊕ω² (split), L₂ = the unique ramified non-split extension of ω² by ω.
  Any residual- or End-based multiplier must be one of these three objects (sharpens end-seg SF-H6).

CITE (not re-verified here, so NOT counted as proved): Serre (Duke 1987, §2) assigns weight p+1 = 8 to a très-ramifié (ω *; 0 1). For L₀ that suggests a Serre weight with an ω-twist. This is not used and does not fix a filtration; both 10∥40 remain NAMED PARALLEL.

Named gaps:
(1) A reducible-ρ̄ Breuil–Mézard / Paškūnas variant is still not ingested (Option B, not done).
(2) The relation between the très-ramifié class and the actual value or residue of L₇ (expected link via the Steinberg L-invariant) is NOT claimed; that is G1-adjacent.
Does NOT use: filtration pick, L₇ unit, abs-irr BM, OMS lift. Not folded into tip.
