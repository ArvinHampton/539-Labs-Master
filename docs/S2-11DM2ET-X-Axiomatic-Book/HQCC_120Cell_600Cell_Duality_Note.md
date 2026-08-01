# HQCC Geometric Illustration: 120-Cell / 600-Cell Duality (Corrected)

**Status:** Category B exploratory geometric illustration only.  
**Date:** 2026-08-01  
**Arithmetic integrity:** 100 percent.  
**Scientific integrity:** 100 percent.  
**Does not alter** the residual discrete algebra, Object539 construction, or any Category A claim.

---

## Purpose

This note records a corrected, non-circular geometric illustration linking the HQCC framework numbers to the classical regular 4-polytopes (the 600-cell and its dual, the 120-cell). It responds to an external arithmetic correction (φ(1001) = 720, not 600) and locks the standard polytope counts under H₄ duality.

The illustration is inspirational and structural only. It is not claimed as a forced derivation from the three-generation axiom alone. The integer 1001 remains an optional discrete shell package (see Provenance_1001_Shells.md); the residual sector construction does not use it.

---

## Corrected Arithmetic

1. Three generations force the non-perturbative superpotential  
   W_np = e³ ≈ 20.085536923187668.

2. Flux budget  
   N_flux = ⌊e³ × 3⁵⌋ = 4880.

3. HQCC terminates in 539 ± 1 steps (Category A combinatorial statement under the charge-preserving map).

4. Optional shell integer (Category B / Mod unless separately forced)  
   N_simplex := 7 × 11 × 13 = 1001.

5. Euler totient (exact)  
   φ(1001) = 1001 × (1 − 1/7) × (1 − 1/11) × (1 − 1/13) = 720.

Correction of earlier transposition: φ(1001) = 720, not 600.

---

## Standard Regular 4-Polytope Counts (Locked)

These are classical geometric facts independent of the model.

**600-cell {3,3,5}**  
- Vertices: 120  
- Edges: 720  
- Faces: 1200 (triangles)  
- Cells: 600 (tetrahedra)  
- Symmetry: H₄ (order 14400)

**120-cell {5,3,3}**  
- Vertices: 600  
- Edges: 1200  
- Faces: 720 (pentagons)  
- Cells: 120 (dodecahedra)  
- Symmetry: H₄ (order 14400)

**Duality under H₄**  
Vertices of one map exactly to cells of the other:  
V(600-cell) = 120 ↔ C(120-cell) = 120  
C(600-cell) = 600 ↔ V(120-cell) = 600  
E(600-cell) = 720 ↔ F(120-cell) = 720  
F(600-cell) = 1200 ↔ E(120-cell) = 1200

Euler characteristic on S³ is 2 for both.

---

## Geometric Illustration (Category B)

Under the optional identification N_simplex = 1001, the totient φ(1001) = 720 matches the edge count of the 600-cell (and the face count of the 120-cell).  
The H₄ Coxeter group is the unique finite reflection group compatible with icosahedral / golden-ratio structure that appears in the 4-dimensional projection.  
The local simplicial character of the 600-cell (tetrahedral cells) and the global enclosing character of the 120-cell (dodecahedral cells) supply a clean geometric picture of local versus global structure under duality.

This match is recorded as a structural illustration only. Changing the optional shell primes changes φ and the numerical coincidence disappears. The core HQCC termination, residual discrete algebra, and packaging arithmetic remain untouched and Category A where previously established.

---

## Correspondence Table (Corrected)

| Quantity     | 600-cell {3,3,5} | 120-cell {5,3,3} | Dual mapping          |
|--------------|------------------|------------------|-----------------------|
| Vertices     | 120              | 600              | V₆₀₀ = C₁₂₀           |
| Edges        | 720              | 1200             | E₆₀₀ = F₁₂₀           |
| Faces        | 1200 (△)         | 720 (pentagons)  | F₆₀₀ = E₁₂₀           |
| Cells        | 600 (tetrahedra) | 120 (dodecahedra)| C₆₀₀ = V₁₂₀           |
| Euler χ (S³) | 2                | 2                | preserved             |
| Group        | H₄               | H₄               | shared                |

φ(1001) = 720 supplies the common edge / face number under the optional shell package.

---

## Hygiene Notes

- No claim is made that the three-generation axiom forces the 120-cell or 600-cell as a necessary geometric object.  
- 1001 and its totient remain optional (see Provenance_1001_Shells.md).  
- Continuum or physical interpretations of the polytopes as vacuum geometry stay Category B.  
- Residual discrete stack (𝒪_res, fiber blocks, permanent class, K⁺, A4⁺/A5⁺, BSpin, KO/Spin coefficients) is unaffected and remains Category A where previously closed.  
- Hardness claims for HQH-539 remain Category B with residual-flux provenance mandatory.

---

## References (classical geometry only)

- H.S.M. Coxeter, Regular Polytopes.  
- Standard Schläfli symbols and H₄ root system counts.  
- Euler characteristic of convex 4-polytopes on S³ = 2.

End of note.
