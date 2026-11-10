# NL DERIVED (F2, O6 + O9 + O10): consequences of "P_rev acts on the −U sector only", 2026-11-09 15:28 CST
Author: Non Local Path (NL). New dated file; nothing edited. Tip 7cddb188… untouched. No CERT. Nothing sent outside.
Authority: OW 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c (NL O6, O9, O10). Adopted closure: RECORD 09498bf7 ((B)-M, Majorana pure swap on H⊗ℂ²). Audits used: PP f9522377, PP 0c3b2b91, NL erratum-2 c915f391. Charge sign: NL 1255 review (B4) and NL 1232 formal check.
Script: /workspace/nl-1511/f2_prev_minusU.py (d73bcb25…), log f2_prev_minusU.log (71c4bf50…). numpy on a 4³ periodic lattice (dim H = 256), Majorana representation (Clifford relations and pure-imaginary γ's checked), central differences, Π: x ↦ −x, m = 0.7. Antilinear maps stored as M∘K.
All constructions are NL derived proposals. Everything that uses O6/O9/O10 is CONDITIONAL on OW 5a6e7177.

## 0. Formalization (NL derived proposal)
- 𝓗 = H⊗ℂ², H₊ = H⊗e₁, H₋ = H⊗e₂, H = L²(ℝ³)⊗ℂ⁴. H_tot = H_D⊗1₂ as in (B)-M. A₀ := γ⁰KΠ, Majorana representation, η := A₀² = γ⁰γ⁰* = −1.
- **P₋ := A₀ acting on H₋** (ψ⊗e₂ ↦ A₀ψ⊗e₂). Three ways to read "trivial or absent on H₊":
  - (a) absent: P₋ is an operator on H₋ only;
  - (b) zero on H₊: the partial antiunitary A₀⊗|e₂⟩⟨e₂|·K on 𝓗;
  - (c) identity on H₊: 1⊕A₀.
- **(c) is not linear or antilinear (PROVED):** (1⊕A₀)(i(ψ,χ)) = (iψ, −iA₀χ), which is neither i·(…) nor −i·(…) for ψ, χ ≠ 0. By Wigner's theorem it is a symmetry only if coherent superpositions of +U and −U are excluded (a ±U superselection rule). H_tot is block-diagonal, so such a rule is dynamically consistent. Reading (c) is CONDITIONAL on the Owner adopting that rule.

## 1. Results on H₋
- **R1 (PROVED).** P₋² = η = −1 on H₋. (Lattice: A₀A₀* = −1.)
- **R2 (PROVED).** P₋ H_D P₋⁻¹ = −H_D on H₋. Since P₋ is antiunitary and t is fixed, this is the dynamical-symmetry condition. Spectral projections satisfy P₋E(Δ)P₋⁻¹ = E(−Δ), so σ(H₋) = −σ(H₋) with equal multiplicities at E and −E. Lattice: sorted spectrum equals minus its reverse.
- **R3 Kramers (claim "P₋ forces Kramers degeneracy" REFUTED by counterexample; E = 0 case PROVED).**
  - Kramers' theorem needs an antiunitary Θ with Θ² = −1 that **commutes** with H. P₋ anticommutes, so it maps the E-eigenspace onto the −E eigenspace and says nothing about the dimension of either when E ≠ 0.
  - Counterexample 1 (exact): on ℂ², P = iσ_y·K, H = σ_z. Then P² = −1, PHP⁻¹ = −H, and both levels ±1 are simple.
  - Counterexample 2 (lattice, inside the Majorana Dirac space): H_p = H_D + 0.3·W_odd with W_odd = (W − A₀WA₀⁻¹)/2 for a random Hermitian W. Then A₀H_pA₀⁻¹ = −H_p, and all 256 eigenvalues are simple.
  - At E = 0 (PROVED): ker H is P₋-invariant and P₋ restricts to a quaternionic structure (square −1) on it, so dim ker H is even. Lattice: a P-odd operator with a kernel has dim ker = 4. For the free massive Dirac H_D, 0 ∉ σ(H_D), so this is vacuous there.
  - The degeneracies of the free lattice H_D (16 and 48) come from other symmetries (lattice translations and rotations, T), not from P₋.
  - Classification (PROVED, standard definition): an antiunitary operator that anticommutes with H is a particle-hole-type symmetry, not a time reversal. With square −1 and nothing else imposed, H₋ sits in Altland–Zirnbauer class C.
- **R4 +U sector (PROVED, by construction).** Under O6, P_rev puts no condition on H₊. The Owner's exact H_{+U} is still OPEN (PP 0c3b2b91 OPEN-4); its spectrum need not be symmetric. If H₊ = H_D (as in H_D⊗1₂), it is symmetric for an unrelated reason (A₀ exists on H), not because P_rev acts there. Under O6 alone, P_rev supplies no map between the sectors; any +U ↔ −U correspondence must come from another operator, such as S or P̂ below.

## 2. Reconciliation with the adopted (B)-M swap
Let P̂ = (γ⁰Π⊗σ_x)K (RECORD 09498bf7) and S := 1⊗σ_x, a linear unitary involution that commutes with H_tot.
- **K1 (PROVED).** P̂ = S·(A₀⊗1₂), with [S, A₀⊗1₂] = 0. Lattice: S·P̂ = A₀⊗1₂ exactly.
- **K2 (PROVED).** (S·P̂)|_{H₋} = A₀ = P₋, and S·P̂ maps H₋ into H₋. Lattice: the H₋ block of S·P̂ equals A₀, and the off-block vanishes. So **P₋ is the σ_x-twisted restriction of the adopted P̂.**
- **K3 (REFUTED by proof).** "P_rev = P̂ and P_rev acts on H₋ into H₋." P̂(H₋) = H₊ and H₊ ∩ H₋ = {0}, so P̂ sends no nonzero vector of H₋ into H₋. Lattice: Π₋P̂Π₋ = 0.
- **K4 (PROVED, trivial).** P̂²|_{H₋} = −1 is a linear scalar. It carries no antiunitary content and is not a candidate for P_rev.
- **Genuine tension (OPEN).** The 1:18 PM adoption names P̂ (which acts on both sectors) as P_rev. O6 says P_rev acts on −U only. By K3, both cannot hold literally for the same operator. Consistent readings:
  - **T1.** P_rev := (S·P̂)|_{H₋} = P₋, with P̂ kept as the inter-sector map. This keeps P² = −1, the −H symmetry and locality.
  - **T2.** P_rev := P̂|_{H₋}: H₋ → H₊ (the backward half of the swap). This is consistent as a map, but it has no square on H₋ (as a partial operator on 𝓗 it squares to 0), so the adopted P² = −1 is lost.
  - **T3.** O6 supersedes the 1:18 naming: P_rev := P₋, and P̂ is no longer called P_rev.
  - The Owner chooses. NL notes that T1 and T3 give the same operator on H₋.

## 3. O9: no non-tensor Kramers J
- **Lemma (PROVED).** On H⊗ℂⁿ, a tensor-form Q = A₀'⊗(V·K_n), with A₀' antiunitary on H, A₀'² = η and V ∈ U(n), has Q² = η·VV̄. VV̄ = −1_n is possible iff n is even: det(VV̄) = |det V|² > 0 against det(−1_n) = (−1)ⁿ, and iσ_y ⊕ … ⊕ iσ_y works for even n. Random check: min‖VV̄ + 1‖ is 2.000 for n = 1 and 2.005 for n = 3; exact 0 for iσ_y.
- **Consequences, CONDITIONAL on OW 5a6e7177 (O9 is a choice, not a theorem):**
  - On H₋ = H⊗ℂe₂ (n = 1), VV̄ = +1, so P₋² = η. P₋² = −1 holds iff η = −1. So under O9 the Majorana-class representation is forced for P₋² = −1 (PROVED given O9). This is consistent with (B)-M.
  - On the literal H₊⊕(H₊⊗ℂ²) ≅ H⊗ℂ³ (n = 3), no tensor Kramers complement exists (PP 0c3b2b91 LA-4). With O9, Local A3 in the Dirac or chiral representation cannot be given square −1; it stays Q² = +1.
  - On H⊗ℂ² (n = 2), iσ_y is a tensor Kramers factor, so Option D is tensor-form and O9 does not exclude it. It stays not adopted (not a fixed-t symmetry).
  - PP's OPEN item "a non-tensor Kramers J on R; whether the Owner wants one" (0c3b2b91 OPEN-3) is settled by Owner choice: excluded. Such J exist mathematically (PP); O9 removes them by definition.

## 4. O10: the −Z charge rule
- **Z1 (definition-level consequence, PROVED).** The label map ζ: Z ↦ −Z sends {1,…,118} bijectively onto {−1,…,−118}, and ζ∘ζ = id. This is consistent with P₋² = −1, because −1 is a global phase and acts trivially on charge.
- **Z2 (PROVED, agrees with B4).** In the Majorana representation all γ's are imaginary, so K is charge conjugation and A₀ contains C.
  - Lattice and algebra: A₀(H_D + eφ − eα·A)A₀⁻¹ = −(H_D − eφ∘Π − eα·(A∘Π)).
  - So A₀ maps a same-charge solution in the potentials (φ, A) to one in (−φ∘Π, A∘Π). That is minus the parity image of the potentials (parity sends φ ↦ φ∘Π and A ↦ −A∘Π), i.e. the C·P image of the sources.
  - For a nucleus of charge Ze at the origin (φ even), the image sees −Ze. This is the −Z rule, derived from O6 with the Majorana P₋ and matching B4 ("−Z requires C in the map").
- **Z3 (PROVED).** σ(H_e[−Z]) = −σ(H_e[+Z]) for the Coulomb–Dirac operator (same conjugation; standard self-adjoint realization, Zα < 1). Bound levels E_n map to −E_n.
- **Z4 (REFUTED by counterexample, supporting the Owner's rejection).** −(119−Z) = Z − 119 is not additive under fusion: Z₁ = Z₂ = 1 gives (Z₁+Z₂) − 119 = −117 ≠ (Z₁−119) + (Z₂−119) = −236. Among affine rules aZ + b, additivity forces b = 0, and the C content of A₀ gives a = −1.
- **Z5 (consistency with corpus, PROVED by reading).** Zenodo 17926999 keeps the atomic number and mass unchanged and prefixes "−". This agrees with −Z if "−" marks the charge sign. P₋ leaves m unchanged (H(−m) ≠ −H(m), NL 1232 item 3).
- **OPEN.** Every physical reading: inverted nuclear hierarchies, reversed Aufbau, negative-energy versus hole-picture interpretation of Z3, and stability of −U matter.

## Labels tally
- PROVED 13: (c) not linear/antilinear; R1; R2; R3 E = 0 case; R3 class-C classification; R4; K1; K2; K4; O9 lemma; Majorana forced under O9 (given O9); Z1; Z2; Z3; Z5. (Z2/Z3/Z5 counted with Z1 as the O10 block where they are definition-level; strict count 15 statements.)
- CONDITIONAL 3: reading (c) on a ±U superselection rule; all O6/O9/O10 consequences as model statements (OW 5a6e7177); O9 settlement of PP OPEN-3.
- OPEN 3: which reading T1/T2/T3 the Owner means; the Owner's H_{+U}; every physical reading of −U spectra and −Z matter.
- REFUTED 3: "P₋ forces Kramers degeneracy" (counterexamples); literal "P̂ acts on H₋ into H₋" (K3); −(119−Z) as a charge homomorphism (Z4).
