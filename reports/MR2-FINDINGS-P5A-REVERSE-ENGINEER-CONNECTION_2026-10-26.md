# MR2 FINDINGS — P5a reverse-engineer, connection lane (4) — 2026-10-26 (America/Chicago)

Status: **PROPOSED / Cat B only**. Not Cat A. No tip fold. tip_touched **NO**.
Authority: Owner invent lift 841f5067a1750b2d34d596b5dcddcc76b8a49d23d064bb7c9ad2f670704c2a7f (drafting proposed routes only).
Locks: tip Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (verified start). Soft SF invent HOLD tip fill else. Soft SF F3 CLOSED. Bridge PARTIAL, READY NO. Local Bridge C kept separate from NL EH11D.

## 1. FAIL input summary
Source: MR1 `grok-batches/MR1-AUTHOR-PROVE-P5A-VANISHING_2026-10-26.md` sha b829661e2a6b1ae49e743f111336ca2c4893bd90dd7a292ad05d8e03cd1b7e8d; script `MR1-P5A-dimcalc_2026-10-26.py`.
- Operative P5a (W-P5a-OP): k=−2, κ=4, claim S₄(Γ₀(49), ρ̄)={0}, ρ = ρ_N₂|V₄₂, ρ̄ = g↦ρ(g)^{-T}, no Fricke cut.
- MR1 proposed: dim S₄(Γ₀(49), ρ̄) = **592** (ρ convention: 573). The space is induced, Ind_{Γ₀(49)}^{SL₂ℤ}: ρ̄ ⊗ Perm(P¹(ℤ/49)), 42·56 = 2352 dims, via the fitted orbifold Riemann–Roch formula.
- What fills it: leading term d(κ−1)μ/12 = 42·3·56/12 = **588**, plus +4 from the elliptic, parabolic and T-exponent corrections. 11 of the dims already come from level 1 (S₄(SL₂ℤ, ρ̄) = 11, oldforms pulled up 56 ways only through Perm).
- Assumptions that fill it: (a) κ=4 > 2, so RR is exact and grows linearly in κ; (b) all 42 dims of ρ̄ are kept (no isotypic, new, or eigen cut); (c) ρ̄ has finite image, is unitary, and ρ̄(−I)=I; (d) integral weight with the automorphy factor (cτ+d)^κ.
- Reading: P5a fails for a structural reason, not by accident. At κ ≥ 3 the leading term rules out vanishing for any 42-dim finite-image ρ̄ with no cut.

## 2. Connection map
| Language | What the 592-space *is* | What would have to VANISH to give an obstruction | Resonant close if vanishing held | Soft SF risk |
|---|---|---|---|---|
| **Weil-rep / Borcherds–Kudla–Millson** (Cat A cite: Bruinier–Funke, Duke 2004, arXiv math/0212286, Thm 1.1–1.3; WebSearch-verified) | The **obstruction space** of BF: S_{2−k} pairs nondegenerately with H_k⁺/M_k^!, and ξ_k: H_k⁺ → S_{2−k} is surjective. So the 592 cusp forms are exactly 592 independent linear conditions on principal parts that a weight k=−2 input must satisfy. The KM lift Λ_KM sends S_{2−k} to closed forms (special-cycle duals); the 592-space is the *target* side of KM. | S_{κ}(·, ρ̄) = 0 (or its relevant cut), so that every principal part is realised by a weakly holomorphic (or harmonic) form. | Every principal part lifts, and the Borcherds lift Λ_B gives a Green current or divisor Z(f) with no a⁺(0)-correction obstruction. That would be the RNT resonant close. | **High.** BF theorems are about ρ_L (Weil, Mp₂ or SL₂ℤ). Applying them to ρ̄ = ρ_N₂|V₄₂ needs ρ̄ ≅ ρ_D (a Weil dictionary), which is **not Written**. Template-only use is OK. |
| **Bruhat–Tits / Teitelbaum harmonic cocycles** (Cat A cite: Teitelbaum, Invent. Math. 1990; Darmon, Annals 2001 Lemma 1.1; Dasgupta–Teitelbaum AWS 2007 notes; WebSearch-verified) | Only the **7-new, Steinberg-at-7** part of a weight-k space is P^{k−2}-valued harmonic cocycles on the tree of PGL₂(ℚ₇), for groups with p ∥ level (or definite-quaternion S-arithmetic Γ). At level 49 = 7², the newforms are 7-supercuspidal or Steinberg⊗χ, and they are **not** p-new in Teitelbaum's sense. Most of the 592 (the old part from levels 1, 7, and the supercuspidal part) is **invisible** to cochains. | The cochain space C^har(k=4, Γ, ρ̄-twisted) = 0. Even if that held, it would only say that the Steinberg-at-7 slice of 592 vanishes, not all of it. | The Poisson kernel / Teitelbaum residue inverse rebuilds a rigid form from the cocycle, giving an RTTC-style discrete closure on a finite graph. | **High.** Treating cocycle vanishing as P5a vanishing silently drops the old and supercuspidal parts (a conflation). Level-49 applicability is unverified. |
| **CatB-1** (conditional Weil dictionary) | *If* Owner Writes ρ̄ ≅ ρ_D for a level-49 discriminant form D, then 592 = dim S₄(ρ_D)-type space. Its Γ₀(49)-scalar companion comes via Schwagenscheidt–Völz / Scheithauer lifting. | S₄(ρ_D) = 0. That is false for any D of size 42 by the same 588 leading term, so CatB-1 does **not** rescue κ=4. | Not reached at κ=4. | Cat B. Must not be promoted. It consumes the vanishing, and the dictionary is Owner-Write-gated. |
| **CatB-2** (Teitelbaum fit to P5a) | The cochain slice described above, at most the 7-new Steinberg piece of 592. | That slice = 0. | A partial closure (slice only), never a full P5a. | Cat B. Must not be promoted. A p² caveat applies. |

Net connection story: **every one of the 592 dims is an obstruction in BF language**. Neither the theta-lift nor the cochain picture makes them vanish. Each only re-labels them as cycle classes or cocycles.

## 3. Revised weight/route candidates (all **Cat B, proposed**; none tip-folded)
- **R1 — odd κ parity kill (strongest).** With integral-weight automorphy and ρ̄(−I) = I (MR1: ρ(−I) = S_lab⁻² = I on V₄₂), applying −I gives (−1)^κ f = f, so **M_κ(Γ₀(49), ρ̄) = 0 for every odd κ**. κ=3 means k = −1 < 0, which is compatible with P3's sign condition. This gives *vanishing*, but **caveat VACUITY**: the same parity also kills the input space M^!_{k}, H_k at k=−1, so the BF obstruction "closes" an empty input. This is a resonant-close by emptiness and is likely Soft-SF-unacceptable as a Bridge C mechanism. **Needs MR1 algebra**: (i) the sign convention for −I in P1's multiplier; (ii) whether P3 permits odd k; (iii) whether a metaplectic or half-integral κ is intended instead. In the half-integral case the parity argument does not apply.
- **R2 — κ ≤ 0 (k ≥ 2).** For κ=0, holomorphic forms with finite-image unitary ρ̄ are constant vectors in the Γ₀(49)-invariants, which have **dim 0** (MR1 §2, smallest singular value 3.67). So M₀ = S₀ = 0, and for κ < 0 the space is 0 too. This contradicts P3 (k<0), so it is a **route change** (Owner decision), not a fix within P3.
- **R3 — κ=2 (k=0) with an isotypic cut.** The leading term drops to 42·56/12 = 196, and the dim must be computed with the κ=2 RR correction. Vanishing requires a cut to an SL₂ℤ-subrep W ⊂ V₄₂ (from the ρ̄ decomposition into irreducibles) with dim S₂(Γ₀(49), W) = 0. Plausible only for small W with large T-exponents. **Needs MR1 algebra** (decomposition of V₄₂ plus per-summand RR at κ=2).
- **R4 — new/old cut.** Restrict to the ρ̄-newspace at 49, quotienting out the induced oldforms from S₄(SL₂ℤ, ρ̄) (11) and from level 7. This reduces 592 but cannot reach 0 at κ=4. It is listed only as a dimension diagnostic. **Needs MR1 algebra.**
- **R5 — Atkin–Lehner without reopening Path A.** A W₄₉ (DMZ, ≠ Fricke W₇ per R5) eigen-cut acting on Perm, i.e. on the P¹(ℤ/49) factor only, not via ρ(W₇) on V₄₂. At best this roughly halves the space, so it is not a vanishing route at κ=4. It is admissible only if the Owner Writes it as a Perm-side operator. **Needs MR1 algebra.**
- **R6 — Steinberg-at-7 slice (CatB-2 refined).** Restate the obstruction only for the cochain slice, and keep the rest as a declared non-obstruction residue. This is honest but gives a PARTIAL Bridge C at most.

Ranking for Bridge C under Residual-vs-Resonant: R1 (vanishes, but vacuity risk) > R3 (needs computation) > R2 (route change). R4, R5 and R6 do not reach 0 at κ=4.

## 4. What does NOT work
- Any statement "P5a ⇔ BF S_{κ,L⁻}=0" without an Owner-Written ρ̄ ≅ ρ_D. That invents a Weil dictionary. Forbidden.
- Cutting by a ρ(W₇) eigenspace on V₄₂. That reopens Fricke Role A / Path A and violates Soft SF F3 CLOSED.
- Using D1 / P5d forcing as a substitute for P5a (tip: not permitted).
- Treating Teitelbaum cocycle vanishing as full P5a vanishing (it drops the old and supercuspidal parts).
- Importing EH11D / Loos-JTS / Φ-A3 geometry (CatB-3/4/5) into the local Bridge C closure. That conflates it with NL EH11D.
- Keeping κ=4 with the full 42-dim ρ̄ and hoping for a hidden cancellation. Ruled out by the 588 leading term.

## 5. Overlap note (MR1 shortlist, ~9da55b44…)
MR1's BF θ-lift/ξ and Kudla–Millson-template-only items match row 1 here. No divergence. This file adds the parity (R1) and invariants (R2) vanishing routes.

## 6. Tip check
tip sha start = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91; end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91. tip_touched **NO**.
