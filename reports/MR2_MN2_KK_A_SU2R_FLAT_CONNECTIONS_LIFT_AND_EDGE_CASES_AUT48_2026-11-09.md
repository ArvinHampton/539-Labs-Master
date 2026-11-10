# MR2: SU(2)_R flat connections on Bolza Σ under Aut⁺ (48), completion: SU(2) lift of the invariant SO(3) point and the dihedral and Klein edge cases
Author: MR2. Additive new file. It supersedes the partial file ac257bf7 (MR2_MN2_KK_A_SU2R_FLAT_CONNECTIONS_AUT48_2026-11-09.md) additively and does not edit it. No CERT. Nothing sent. Nothing adopted by MR2.
- Authority: OW 8b26c786 ("Group A"). This closes ac257bf7 §3d items (1) and (2), and PP 1fe6c574 A4-gap.
- Full spectrum OPEN. Junction UNSOLVED. Tip 7cddb188 MATCH.

## Files (reports/)
| file | sha256 |
|---|---|
| MR2_MN2_KK_A_SU2R_FLAT_CONNECTIONS_LIFT_AND_EDGE_CASES_AUT48_2026-11-09.py (frozen before the run; sha-checks and execs the KK group section from 88949658) | 02b945002aff3728aeead76c045e405b1dfac05310b87afb1f4ca21aaf7b8922 |
| …log (19:18 CST, runtime about 2 s) | 2aadaee3a59cb956cde72e87f0ec91bc2dea2ee71cc6fdee28bb66e3beac0827 |
| this .md | see sidecar |

## 0. Method. PROVED as a construction (log [R])
- Δ⁺(2,3,8) = ⟨x, y | x², y³, (xy)⁸⟩ surjects onto Aut⁺, with x ↦ an element of order 2, y ↦ an element of order 3, and xy of order 8; the image is all 48 elements. Its kernel is π₁(Σ). That last identification is the standard Bolza uniformization, CONDITIONAL as in ac257bf7.
- **Reidemeister–Schreier** on the 48 cosets gives the free kernel K of F(x,y) → Aut⁺, of rank **49**. Then π₁(Σ) = K/⟨⟨conjugates of x², y³, (xy)⁸⟩⟩.
- **Consistency checks:**
  - H₁(Σ;ℤ₂) = ℤ₂⁴⁹/(relator span) has **dim 4 = 2g**.
  - Aut⁺-invariant characters have **dim 0**, matching the J[2] orbits 1 + 3 + 12.
- **Lifts.** A lift of an SO(3) representation to SU(2) is a sign vector s ∈ ℤ₂⁴⁹ on the Schreier generators that satisfies the relator constraints, a GF(2) affine system. The lifts form a torsor over H¹(Σ;ℤ₂) (16 of them).
- **Invariance up to SU(2) gauge** under g = conj_δ, δ ∈ {x, y}, is tested directly.

## 1. The dense invariant SO(3) point (k = 3; tilt 1.113098 rad, the same as ac257bf7)
- **SU(2) lift exists. PROVED** (log [K3]: the GF(2) system is solvable).
  - Second proof: H²(Δ⁺;ℤ₂) classes are determined by the invariants (a, d) = (x̃² = −1?, z̃⁸ = −1?). The reason: in the presentation, rescaling generator lifts by the central element changes only y³ and the product relation, so x̃² and z̃⁸ are the only invariants.
  - The k = 3 point has (a, d) = (1, 1). The Fuchsian SL(2,ℝ) lift of the same Δ⁺ has (1, 1) too: elliptic half-angles π/2 and π/8, recomputed in log [FC]. The two classes are equal, and the Fuchsian class restricts to 0 on π₁(Σ), because spin structures exist (w₂ = χ mod 2 = 0).
- **Aut⁺-invariant SU(2) lifts: 0 of 16. PROVED** (log [K3]).
  - The representation is dense, so the gauge must be h = ±(lift of φ(δ)), and invariance reduces to a GF(2) fixed-point condition. It has no solution.
  - **Control (log [FC]).** The same machinery run on the Fuchsian SL(2,ℝ) lifts, which correspond to the 16 spin structures, also gives **0** invariant lifts. That matches the known theta-characteristic orbits 6 + 4 + 6, so the method reproduces an independent answer.
  - The affine data of the K3 and Fuchsian systems are identical (same relator vector): the K3 lifts form an Aut⁺-set isomorphic to the spin structures.
- **Conclusion.** The dense point exists as an invariant **SO(3)_R** flat connection, but **no SU(2)_R lift of it is Aut⁺-invariant**. For SU(2)_R, which acts on the doublet fermions, it is not in the truncated theory. PROVED, given §0.

## 2. Dihedral edge case: Ad ρ ⊂ O(2), not in SO(2), with a unique axis. REFUTED as an invariant point. PROVED
- The class χ = (Ad ρ composed with O(2) → O(2)/SO(2)) ∈ H¹(Σ;ℤ₂) is nonzero and gauge-invariant, because the axis is unique and gauge conjugation fixes χ.
- Invariance would force χ ∈ H¹(Σ;ℤ₂)^{Aut⁺}, and that space is 0 (log [R]). Contradiction.

## 3. Klein edge case: Ad ρ = V₄, lifting to Q₈ (log [KL])
- The nonzero characters fall into Aut⁺ orbits of sizes **3 + 12**. The 3-orbit together with 0 is a subspace W, and it is the **unique** invariant 2-plane, since a 2-plane has 3 nonzero vectors.
- So a V₄-type **SO(3)** point ψ = (χ₁, χ₂) with span W is Aut⁺-invariant up to N_SO(3)(V₄) = S₄, which induces all of GL(W). PROVED.
- **Q₈ (SU(2)) lift exists.** w₂ = ⟨χ₁ ∪ χ₂, [Σ]⟩ = 0, because squares vanish on an oriented surface. PROVED (GF(2) system solvable).
- **Invariant SU(2) lifts: 0 of 16.** The 16 lifts fall into 4 gauge classes modulo 2O = N_SU(2)(Q₈) (order 48, built in the log), and every gauge h ∈ 2O was tested. PROVED.
- **Conclusion.** The V₄ point exists for SO(3)_R, but no SU(2)_R lift of it is invariant.

## 4. Completeness of the case list. PROVED, given §0 and ac257bf7
An SU(2) point ρ with ρ∘g_* ~ ρ is one of the following:
- **(a) Abelian.** Only the trivial connection is invariant (ac257bf7 §2, PROVED).
- **(b) Irreducible, with Ad-centralizer trivial.** These correspond to Hom(Δ⁺, SO(3)). The classification in ac257bf7 §3a leaves only the k = 3 class, plus the classes that factor through Aut⁺ and are trivial on π₁. Its SU(2) lifts are not invariant (§1).
- **(c) Irreducible, with nontrivial Ad-centralizer.** Then Ad ρ ⊂ O(2) is not abelian:
  - with a unique axis, it is excluded by §2;
  - with Ad image V₄, the axes are not unique, and §3 applies.
  - There is no other case: a non-abelian subgroup of SO(3) with nontrivial centralizer lies in some O(2), and its axis is unique unless the subgroup is V₄.

**Result. The Aut⁺-invariant locus of the SU(2)_R character variety of Bolza Σ is a single point: the trivial connection.**
- PROVED, CONDITIONAL only on Δ⁺/π₁Σ = Aut⁺ (the standard Bolza uniformization) and on the numerical root of ac257bf7 §3a, which is reproduced here to 1e-6.
- For SO(3)_R, without fermions, there are two further isolated invariant points: k = 3 and V₄. They are not relevant to SU(2)_R.
- **Effect on A.** The A truncation removes all SU(2)_R flat connections, both the moduli and the discrete points. The A4-gap row (erratum d33ad28d, fix 2) is **closed: PROVED**, with that one premise. This supersedes the "finite set, OPEN" statement in ac257bf7 §4.

## 5. Irrep labels (item 2 of the request). Partial; mostly OPEN
- **λ₁ = 3.8388872588. 3-dimensional Aut⁺ irrep: CONDITIONAL.**
  - The value and its multiplicity 3 come from Strohmaier–Uski (arXiv:1110.2150 v4). I fetched it this turn: §5.3 gives λ₁ ≈ 3.83888725884219951858… and states the symmetry group S₄ × ℤ₂ of order 48. The multiplicity of each eigenvalue is in their data files, which I did not fetch, to keep usage down.
  - No 1-dimensional character occurs below 23.0786 (ecee2668 FEM; PP T3). So a 3-dimensional eigenspace is irreducible. Which of the two 3-dimensional GL(2,3) irreps it is (3 or 3 ⊗ sgn) is OPEN.
  - J-parity: both 3-dimensional irreps factor through S₄, so J acts trivially on them. CONDITIONAL on the multiplicity.
- **Next 3–4 levels:** OPEN, including their multiplicities and irreps. Cook's thesis tables were not fetched or verified.
- **Method planned for the next run** (not started):
  - Vector-valued P1 FEM on the (2,3,8) triangle, for each real irrep π of Isom (orders 1⁴ 2² 3⁴ 4³).
  - Boundary conditions per edge: Dirichlet on the −1 eigenspace of π(r_i), Neumann on the +1 eigenspace.
  - The multiplicity of π in E_λ equals the dimension of the corresponding triangle eigenspace. This extends the existing KK FEM (88949658 [T]).
  - ETA about 2 h, plus about 20 min to fetch and verify the SU and Cook multiplicity tables.

## 6. Not pursued (deferred per request)
| item | ETA |
|---|---|
| charged S⁴ towers (q ≠ 0 under the U(1) twist), coupling to K^q | about 3–4 h; CONDITIONAL on the fibre operator |
| irrep labels (§5 method) | about 2–2.5 h |

## Labels
| item | label |
|---|---|
| Schreier presentation consistent (rank 49; H₁ dim 4; no invariant characters) | PROVED |
| k = 3 point lifts to SU(2) | PROVED |
| no Aut⁺-invariant SU(2) lift of the k = 3 point (Fuchsian control reproduces 0 invariant spin structures) | PROVED |
| dihedral (unique-axis) invariant points | REFUTED |
| Klein point: SO(3)-invariant, Q₈-liftable, no invariant SU(2) lift | PROVED |
| invariant SU(2)_R locus = {trivial}; A4-gap closed | PROVED (premise: Δ⁺/π₁Σ = Aut⁺, CONDITIONAL) |
| λ₁ is a 3-dimensional Aut⁺ irrep | CONDITIONAL (SU multiplicity) |
| 3 vs 3 ⊗ sgn; levels 2–5 | OPEN |
| charged S⁴ towers | OPEN (deferred) |

Tally (9 rows, by table order): PROVED 4 (rows 1, 2, 3, 5) · PROVED with a CONDITIONAL premise 1 (row 6) · REFUTED 1 (row 4) · CONDITIONAL 1 (row 7) · OPEN 2 (rows 8, 9) = 9.
