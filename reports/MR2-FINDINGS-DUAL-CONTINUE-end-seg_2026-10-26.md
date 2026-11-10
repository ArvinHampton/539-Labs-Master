# MR2 FINDINGS — DUAL CONTINUE — End-seg: global extension classes are 1-dim and restrict injectively to G_Q₇, so the LOCAL lattice segment also has length EXACTLY 2 — 2026-10-26
STATUS: PARTIAL (MR2 lane). The local "exactly 2" item, OPEN in catb2-lattice-seg, is closed below WITHOUT G1. Submitted for Auditor Soft SF. Dual-label: filtration 10∥40 BOTH NAMED PARALLEL, NO PICK. No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. G1 BLOCKED, no OMS / PS #20 / L₇ used. No tip fold. tip_touched NO.
Builds on: catb2-lattice-seg af25c786… (SF-G1–G4), local-ext-G7 (L1–L4), resid-reducible c358d9e6…, coeff5311 e2aab230…. Script: MR2-end-seg.sage (1 s).

Notation. k = F₇. K = Q(ζ₇), Δ = Gal(K/Q) ≅ (Z/7)^×, λ = (1−ζ₇). S = {7, ∞}, G_S = Gal(Q_S/Q). Ext¹_{G}(ω, ω²) = H¹(G, ω) and Ext¹_{G}(ω², ω) = H¹(G, ω⁻¹).

Soft SF facts:
- SF-H1 (PROVED): h¹(G_S, ω) = h¹(G_S, ω⁻¹) = 1.
  Proof: since [K:Q] = 6 is prime to 7, Kummer theory gives H¹(G_S, ω^i) = (O_{K,S}^×/7 ⊕ Cl_S(K)[7]) restricted to the ω^{1−i}-isotypic part.
  Sage: h(K) = 1; S-unit rank 3; torsion μ₁₄.
  As a Δ-module, O_{K,S}^×/7 = ω (μ₇) ⊕ 1 (S-unit 7) ⊕ ω² ⊕ ω⁴ (real units, the nontrivial even characters).
  Therefore i = 1 picks the trivial component, spanned by κ(7), and i = 5 = −1 picks the ω² component, spanned by κ(u) for a real unit u. Each has multiplicity 1.
  This agrees with the global Euler characteristic h¹ = 1 + h² for odd characters (h² = 0).
- SF-H2 (PROVED): the restriction maps H¹(G_S, ω^{±1}) → H¹(G_Q₇, ω^{±1}) are INJECTIVE.
  - For ω: κ(7) is locally nonzero because v_λ(7) = 6 ≢ 0 (mod 7).
  - For ω⁻¹: suppose u = x⁷ in K_λ. Write x = a + λy with a ∈ Z. Then x⁷ ≡ a⁷ (mod λ⁷), and λ⁷ ⊂ 7O, so u ≡ a⁷ (mod 7). Since 7 is regular (h = 1), Kummer's lemma says u is a global 7th power. That contradicts κ(u) ≠ 0.
  - Base change to K_λ has degree prime to 7, so it does not affect vanishing.
- SF-H3 (PROVED, from SF-G3 and H1): the two global endpoint lattices realise THE unique non-split global classes, up to scalar:
  - the endpoint with sub ω² and quotient ω realises κ(7) ∈ H¹(G_S, ω);
  - the endpoint with sub ω and quotient ω² realises κ(u) ∈ H¹(G_S, ω⁻¹).
- SF-H4 (PROVED, from H2 and H3): both global endpoints are LOCALLY non-split, so End_{G_Q₇}(ρ̄_{L₀}) = End_{G_Q₇}(ρ̄_{L₂}) = k. This answers local-ext-G7 L4 in the "locally non-split" direction.
- SF-H5 (PROVED, from H4, the lattice-tree description and SF-G4): in the local segment (diagonalising g ∈ I₇), vertices have SPLIT reductions in the interior and non-split ones at the ends. So a locally non-split global endpoint is a LOCAL endpoint. Both global endpoints are local endpoints, so the local segment equals the global one: the G_Q₇-stable lattices of V_{4,L} = ρ_{f,7}|G_Q₇ are exactly 3, with length EXACTLY 2. This closes the local "exactly 2" item of catb2-lattice-seg without L₇.
- SF-H6 (PROVED, consequence): the End rings along the segment, both globally and locally (End over G_Q and over G_Q₇), are k, k×k, k. The middle lattice L₁ is split both globally and locally. End is never a field at L₁ and never equals k×k at the ends. So any residual / End-based candidate must take one of these three lattices; there is no further lattice choice. The ω⁻¹ endpoint gives the unique local class (1-dim, local-ext L2). The ω endpoint gives the specific line spanned by κ(7)|G_Q₇ inside the 2-dim H¹(G_Q₇, ω).

Named gaps:
(1) Whether the local line κ(7)|G_Q₇ ⊂ H¹(G_Q₇, ω) is the peu- or très-ramifié line in the Breuil–Mézard / Serre-weight sense, and its relation to v₇ or the residue of L₇. This is NOT claimed (G1-adjacent).
(2) Abs-irr BM multiplicity is still inapplicable (ρ̄ is reducible, resid-reducible F5). A reducible-ρ̄ BM / Paškūnas variant has not been ingested.
Does NOT use: filtration pick, L₇ unit, abs-irr BM, OMS lift. Not folded into tip.
