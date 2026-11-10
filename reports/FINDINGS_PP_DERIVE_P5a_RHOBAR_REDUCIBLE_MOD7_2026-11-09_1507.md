# FINDINGS — PP: P5a under ρ̄ = ρ̄_f (reducible mod 7) — 2026-11-09 (America/Chicago)
Agent: Professor Proof (Soft SF). Pure math. Additive file. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 was read only and is untouched. No CERT. No outside service. All computation was local (PARI 2.17.2 via cypari2). Scripts and logs: /workspace/audit-scratch/pp_p5a_rhobar/ (p5a.gp, p5a2.gp, p5a3.gp, p5a4.gp, *.log).

## 0. Authority (sha256 verified, sidecars MATCH)
- **OW e494873929ae6a499578a52e11e5c5bb18f1b40d14f7af2d9a42b9c78fe6004b** (…P5a_LEVEL49_REFERENT…_1408): the referent is g0, with (2, 7, 7) and Fricke +1. W7 = +1 is scoped to level 7. P5a stays OPEN.
- **OW ea2cc9e6b41cde91844b4f2217d98694a8307df96a3a89bdd35d6eb291e46911** (…P5a_RHOBAR_REDUCIBLE_MOD7…_1500), verbatim: "As mine: specify P5a's ρ̄ as the reduction mod 7 of ρ_f, which is reducible (semisimplification ω^13 ⊕ ω^32 from the mod-49 congruence). Have Professor Proof derive what that means for P5a's vanishing claim and the level-49 referent. P5a stays OPEN until then."

## 1. P5a as stated on disk (tip 7cddb188, quoted)
- **Line 412, the operative version per OW 45aeba5f:** "The space of cusp forms for (Γ₀(49)⁺, dual representation ρ̄) at weight κ that lie in the P2-chosen eigenspace of ρ(W₇) is {0}. accepted as axiom"
- **Line 410, the Γ₀(49) version:** "…The space of cusp forms for the pair (Γ₀(49), dual representation ρ̄) at weight κ = 4 is {0}. to prove"
- The LOCK package a12af91a uses the R10 name "cusp forms for (Γ₀(49)⁺, ρ̄) at κ=2−k".

Notation: f = 7.4.a.a, ω = the mod-7 cyclotomic character, E = E₄^{χ,χ̄} ∈ M₄(Γ₀(49)), where χ mod 7 has order 6. Mod λ, E reduces to aₙ = n·σ₁(n) for 7∤n and 0 for 7|n.

## (a) ρ̄_f
- **a1 PROVED.** aₙ(f) ≡ aₙ(E) mod λ for all n.
  - Checked exactly for n ≤ 5000. E ∈ M₄(Γ₀(49)) was confirmed with mftobasis on 80 coefficients.
  - The Sturm bound for M₄(Γ₀(49)) is ⌊4·56/12⌋ = 18, so the congruence holds for every n.
  - By Chebotarev and Brauer–Nesbitt, **ρ̄_f^ss ≅ ω ⊕ ω²**.
- **a2 PROVED.** det ρ̄_f = ω³ = ω^{k−1}.
- **a3 PROVED (arithmetic).** 13 ≡ 1 and 32 ≡ 2 mod 6, so ω^13 ⊕ ω^32 = ω ⊕ ω² mod 7. Also 13 + 32 = 45 ≡ 3 mod 42, which matches det = ε^{k−1} mod 49.
- **a4 CONDITIONAL (numerical).** a_p(f) ≡ p^13 + p^32 mod 49 holds for all 668 primes p ≤ 5000 with p ≠ 7, with 0 failures. It is not proved for all p.
- **a5 PROVED (counterexample p = 2).** a_p(f) ≡ p + p² mod 49 is false: a₂ = −1 ≢ 6 mod 49. There are 34 failures for p ≤ 200. So the mod-49 exponents (13, 32) are genuine.
- **Caveat.** Z/49 is not a field, so "semisimplification mod 49" has content only as the trace congruence a4. The ρ̄ itself is mod 7, and there it equals ω ⊕ ω².

## (b) Local and extension data
- **b1 CONDITIONAL (literature: Saito 1997, local–global compatibility).** f is Steinberg at 7 (a₇ = −7, w₇ = +1). Hence ρ_f|G_{Q₇} is semistable and not crystalline.
- **b2 OPEN.** ρ̄_f is a non-split extension of ω by ω² or of ω² by ω. Which one, and its class in H¹, depend on the lattice by Ribet's lemma. Neither OW specifies a lattice.
  - Anything that depends on the non-semisimple ρ̄ is OPEN. That includes its Serre weight and level, its finite-flat or peu-ramifié behaviour, and deformation-ring statements.

## (c) S₄(Γ₀(49)) and S₄(Γ₀(49)⁺), all exact unless noted
- **c1 PROVED.** dim S₄(Γ₀(49)) = 10. The characteristic polynomial of W₄₉ is (x−1)⁶(x+1)⁴, so **dim S₄(Γ₀(49)⁺) = 6**.
  - The new part is 8-dimensional, with char poly (x−1)⁵(x+1)³.
  - The old part ⟨f(q), f(q⁷)⟩ splits into one +1 and one −1 eigenform.
- **c2 PROVED.** W₄₉(f(q) + 49 f(q⁷)) = +f(q) + 49 f(q⁷), and W₄₉(f(q) − 49 f(q⁷)) = −(f(q) − 49 f(q⁷)). On the basis (f, f(q⁷)), W₄₉ acts as [[0, 1/49], [49, 0]]. Write F_old⁺ := f(q) + 49 f(q⁷).
- **c3 PROVED.** F_old⁺ ≡ E mod 7 for all n. Exact check for n ≤ 400 with 0 failures, plus Sturm (18).
- **c4 Newform Galois orbits and their mod-7 data.** For each orbit, "≠ ω ⊕ ω²" is PROVED by one trace. The positive ρ̄^ss identifications are CONDITIONAL: they were checked for p ≤ 400 with no Sturm proof.

| orbit | (a₂, a₃, a₅) | coeff field | W₄₉ | ρ̄^ss at primes above 7 |
|---|---|---|---|---|
| 1 | (−1, 2, −16) | ℚ, = f⊗χ₋₇ | −1 | ω⁴ ⊕ ω⁵ = (ω ⊕ ω²)⊗ω³ |
| 2 | (−5, 0, 0) | ℚ (CM) | −1 | 1 ⊕ ω³ |
| 3 = g0 | (2, 7, 7) | ℚ | **+1** | 1 ⊕ ω³ |
| 4 | (2, −7, −7) | ℚ | −1 | 1 ⊕ ω³ |
| 5 | quartic: y⁴−2y³−35y²+36y+194 | 4 primes of degree 1 above 7 | **+1** (all 4 embeddings) | 𝔭₁, 𝔭₂: 1 ⊕ ω³. **𝔭₃: ω ⊕ ω²**. 𝔭₄: ω⁴ ⊕ ω⁵ |

- **c5 PROVED.** Let h be the orbit-5 newform, and let 𝔭₃ = (7, 2 + y + y²) in PARI's nf basis.
  - aₙ(h) ≡ aₙ(E) mod 𝔭₃ for all n ≤ 400, with 0 failures. Since 400 > 18, Sturm gives the congruence for all n.
  - So h ≡ E ≡ f mod 𝔭₃, and **ρ̄_h^ss ≅ ω ⊕ ω² = ρ̄_f^ss**.
- **c6 PROVED.** h ≢ f mod 𝔭₃², because v_{𝔭₃}(a₂(h) − a₂(f)) = 1. Likewise v_{𝔭₃}(a_p(h) − (p^13 + p^32)) = 1 at p = 2, so the mod-49 trace congruence a4 does not lift to h.
- **c7 Summary.** The Eisenstein maximal ideal m = (λ, T_p − p − p²) of T(S₄(Γ₀(49)⁺)) supports exactly two eigensystems:
  - F_old⁺, from f;
  - h at 𝔭₃.
  The m-part has rank 2 (new part: rank 1). g0 is not in it. The m-part was not computed for level 2401 or for other levels.

## (d) g0 against f and Eisenstein
- **d1 PROVED.** g0 ≢ f mod 7, using p = 2: a₂(g0) = 2 and a₂(f) = −1 ≡ 6. Hence g0 ≢ f mod 49 as well.
- **d2 PROVED.** g0 ≢ the ω ⊕ ω² Eisenstein system mod 7, using p = 3: a₃(g0) = 7 ≡ 0, while 3 + 9 = 12 ≡ 5. So ρ̄_{g0}^ss ≇ ρ̄_f^ss.
- **d3 CONDITIONAL (p ≤ 400).** ρ̄_{g0}^ss ≅ 1 ⊕ ω³. This is a different Eisenstein ideal: a_p ≡ 1 + p³.
- **Consequence.** The Owner's referent g0 (OW e4948739) lies outside the ρ̄_f-part. The Owner's two specifications do not point at the same form.

## (e) Verdict on P5a's vanishing under ρ̄ = ρ̄_f
- **e1 OPEN (literal text).** Line 412 does not type-check, for two reasons:
  - It reads ρ̄ as a representation of Γ₀(49)⁺ (vector-valued forms), but ρ̄_f is a representation of G_ℚ.
  - "the P2-chosen eigenspace of ρ(W₇)" refers to P2, which is VACATED, and level 49 has no W₇. Per OW e4948739, W₇ = +1 is level 7 only.
  An undefined statement is OPEN. Neither proof nor refutation applies.
- **e2 REFUTED under reading I1 (DERIVED PROPOSAL).** I1: "the m_{ρ̄}-localization of S₄(Γ₀(49)⁺) is 0". Counterexample: F_old⁺ = f(q) + 49 f(q⁷), with Fricke +1 and ≡ E mod 7 (c2, c3). Also h at 𝔭₃.
- **e3 REFUTED under reading I2 (DERIVED PROPOSAL, newforms only).** Counterexample: h, the orbit-5 quartic newform at 𝔭₃. It has Fricke +1 and ρ̄_h^ss ≅ ρ̄_f^ss, proved by Sturm (c5).
- **Labeling.** Each counterexample is itself PROVED. Because I1 and I2 are PP proposals, e2 and e3 are counted CONDITIONAL in the rollup, conditional only on adopting the reading.
- **Extension class.** e2 and e3 depend only on ρ̄^ss, because a maximal ideal of T sees only traces. They therefore hold for every lattice choice. A non-semisimple refinement, such as "forms whose ρ̄ is isomorphic to ρ̄_f, not just ρ̄^ss", is OPEN (b2).
- **Note.** m is Eisenstein (reducible ρ̄). Standard "R = T" and multiplicity-one inputs for non-Eisenstein m do not apply.

## Rollup
- **PROVED 11:** a1, a2, a3, a5, c1, c2, c3, c5, c6, d1, d2. Of the c4 table, the "≠ ω⊕ω²" parts are proved; their positive identifications are listed under CONDITIONAL.
- **CONDITIONAL 6:** a4, b1, c4 (positive ρ̄^ss identifications), d3, e2, e3.
- **OPEN 3:** b2, e1, and O-ref.
  - O-ref: how the referent g0 relates to the specified ρ̄. g0 ∉ m-part, so this needs an Owner decision.
- **REFUTED 0** in the strict sense. e2 and e3 are refutations conditional on readings I1 and I2.
- **No Lock 96f8d42e mapping revived. No label invented.**
