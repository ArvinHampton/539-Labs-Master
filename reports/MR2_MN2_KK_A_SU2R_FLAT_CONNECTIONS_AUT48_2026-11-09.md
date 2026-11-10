# MR2: SU(2)_R flat connections on Bolza Σ under Aut⁺ (order 48), up to gauge. This is the first open item of the adopted Group A (partial).
Author: MR2. Additive new file. No CERT. Nothing sent. Nothing adopted by MR2.
- Authority: OW 8b26c786 (t4414, "Group A"). It closes PP 1fe6c574 A4-gap, which MR2 erratum d33ad28d (fix 2) added to OPEN.
- Truncation group: Aut⁺ × wall ℤ₂. The wall acts trivially on Σ, so it does not enter here.
- MN N=2: the U(1)_R is twisted; SU(2)_R is untwisted. So Aut⁺ acts on SU(2)_R holonomies by pullback only, ρ ↦ ρ∘g_*. Invariance means "up to gauge": ρ∘g_* = h_g ρ h_g⁻¹.

## Files (reports/)
| file | sha256 |
|---|---|
| MR2_MN2_KK_A_SU2R_FLAT_CONNECTIONS_AUT48_2026-11-09.py (frozen before the run; it sha-checks and execs the KK group section from 88949658) | a9920504fa8a507201dcf33c18a59120f95462449cea6e2c08088dea8e7712d9 |
| …log (19:11) | faf977ee7e7d85ca3251846caf06b7285cad88bc29dcd61cc2150ba23483cb21 |
| this .md | see sidecar |

## 1. Linear order at the MN background (trivial SU(2)_R holonomy). PROVED (log [L])
- The tangent space is H¹(Σ;ℝ) ⊗ su(2). Aut⁺ acts trivially on su(2), and the averaging projector on H¹ has rank 0.
- So the space of Aut⁺-invariant tangent vectors is **0**: all 12 SU(2)_R flat-direction modes are removed by the truncation.

## 2. Abelian (reducible) points ρ = exp(iθσ₃), θ ∈ H¹(Σ;U(1)) = T⁴ modulo the Weyl group. PROVED (log [A])
- Up to gauge, invariance means g·θ = s(g)·θ, where s(g) = ±1 is a character of Aut⁺ (a homomorphism unless θ is 2-torsion).
- The commutator subgroup has order 24 (SL(2,3)) and contains J. So every character has s(J) = +1, and J·θ = −θ = θ forces **2θ = 0**.
- The nonzero 2-torsion classes form orbits 3 + 12 (ecee2668 [W]; Pin⁺ log [Z]).
- **The only invariant abelian point is the trivial connection.** This includes the central lines. PP's observation holds for J alone, but the full Aut⁺ removes every nontrivial abelian line.

## 3. Irreducible points
An irreducible invariant ρ, with centralizer equal to the center, determines h_g up to ±1. That gives a homomorphism φ: Δ⁺(2,3,8) → SO(3) extending Ad ρ, where Δ⁺ = π₁^orb(Σ/Aut⁺) is an extension of Aut⁺ by π₁(Σ). Conversely, every such φ restricts to an invariant SO(3) point.

- **3a. Classification of Hom(Δ⁺(2,3,8), SO(3)), all generators nontrivial. PROVED numerically (log [I]).**
  - The generators are x = a rotation by π, y = a rotation by 2π/3, and z = (xy)⁻¹ = a rotation by 2πk/8. The scan covers the full tilt of the y-axis, with root bisection.
  - k = 1 or 7: no solution. The triangle with angles π/2, π/3, π/8 is hyperbolic.
  - k = 2, 4, 6: finite images. In each case the graph of Δ⁺ in Aut⁺ × SO(3) has exactly 48 elements, so φ factors through Aut⁺ and is **trivial on π₁(Σ)**. These are not new points.
  - **k = 3 (≡ k = 5): one conjugacy class with infinite image.** The tilt pairs (θ, π − θ) are conjugate.
    - This is the compact Galois-conjugate partner of the arithmetic (2,3,8) group: the triangle with angles π/2, π/3, 3π/8 is spherical, since the angles sum to 29π/24 > π.
    - Its image is **dense**. The y-axis tilt is 1.1131 rad, which is neither 0 nor π/2, so the image lies in no O(2), and no finite subgroup of SO(3) contains elements of orders 3 and 8.
    - The restriction φ|π₁(Σ) has finite index in a dense group, so its closure is all of SO(3). It is therefore **irreducible**.
- **3b. Result.** The SO(3)_R character variety has **exactly one irreducible Aut⁺-invariant point of this type**, besides the trivial one.
  - PROVED numerically, CONDITIONAL on Δ⁺/π₁(Σ) = Aut⁺, the standard Bolza uniformization. A surjection with x, y and xy of orders 2, 3 and 8 was found explicitly in log [I].
- **3c. It is isolated. PROVED by the Weil count.**
  - Rotation classes of finite order are rigid. Each nontrivial rotation has a 1-dimensional centralizer, and H⁰ = H² = 0 for an irreducible φ on the orbifold sphere.
  - So dim H¹(Δ⁺; ad φ) = 3·(3 − 1) − 6 = **0**. By transfer, H¹(π₁; ad)^{Aut⁺} = H¹(Δ⁺; ad φ) = 0.
  - **No invariant moduli** exist at that point either.
- **3d. OPEN.**
  - (1) Whether φ|π₁(Σ) lifts from SO(3) to SU(2)_R, i.e. its w₂ ∈ H²(Σ;ℤ₂). The doublet fermions need a lift, or a compensating twist of the spin structure. ETA about 1 h: compute the SU(2) lift of the triangle relations and push it through Reidemeister–Schreier for the index-48 subgroup.
  - (2) SU(2)-irreducible ρ whose Ad-image has a nontrivial finite SO(3) centralizer (the binary-dihedral or Klein type). For these, h_g is ambiguous beyond ±1 and the correspondence with Hom(Δ⁺, SO(3)) becomes an extension problem. ETA about 1 h.

## 4. Consequence for the A truncation
- **About the MN background: PROVED.** Aut⁺ removes every SU(2)_R flat-connection modulus. The tangent space has no invariants, and the trivial point is isolated in the invariant locus.
- **Elsewhere in the invariant locus: CONDITIONAL.** It is a finite set: the trivial connection plus the isolated k = 3 point (and its SU(2) lifts, if any; OPEN).
  - Such a point is a different flat background, not a modulus.
  - A nontrivial SU(2)_R holonomy is not compatible with the MN Killing spinors, which are SU(2)_R doublets. So it is a non-SUSY sector. This reading is CONDITIONAL.
- The A4-gap row in erratum d33ad28d becomes: **moduli at the background removed (PROVED); full invariant locus = {trivial} ∪ {one isolated irreducible SO(3) point} ∪ (OPEN edge cases 3d)**.

## 5. Not started within the cap (OW 8b26c786 order)
| item | status | ETA |
|---|---|---|
| irrep labels of higher Σ-eigenspaces (Aut⁺/Isom isotypic decomposition via FEM on Σ or the (2,3,8) double with all characters) | not started | about 2–3 h |
| charged S⁴ towers (q ≠ 0 under U(1)_twist), coupling to K^q | not started | about 3–4 h, CONDITIONAL on the fibre operator |
| 3d (1) and (2) | OPEN | about 2 h total |

## Labels
| item | label |
|---|---|
| linear SU(2)_R modes removed | PROVED |
| abelian invariant points = {trivial} | PROVED |
| Hom(Δ⁺, SO(3)) classification; one irreducible infinite-image class | PROVED numerically; kernel = π₁Σ CONDITIONAL |
| irreducibility and isolation (Weil) | PROVED |
| SU(2) lift; Klein/dihedral-type edge cases | OPEN |
| reading the isolated point as a non-SUSY sector | CONDITIONAL |

Tally (6 rows): PROVED 3 · PROVED numerically with a CONDITIONAL premise 1 · CONDITIONAL 1 · OPEN 1. Junction UNSOLVED. Full spectrum OPEN. Tip 7cddb188 MATCH.
