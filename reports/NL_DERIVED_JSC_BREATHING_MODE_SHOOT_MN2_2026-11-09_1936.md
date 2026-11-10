# NL DERIVED: JS-C with the S⁴ breathing mode — shoot from the wall into the IR (file 2 of 2)
2026-11-09, CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED** (19a88b19), unchanged.
Builds on: NL_DERIVED_JSC_BREATHING_MODE_EQUATIONS_MN2_2026-11-09_1935.md (sha ebdda4b6…), items E1, E3–E8.
Scripts: /workspace/nl-jsc-1905/singlet_toy_shoot.py (sha 30fce38e…), log (sha 11e1dec8…), both with sidecars.

**Tally: PROVED 2 · CONDITIONAL 2 · OPEN 2 · REFUTED 0 · total 6**

## 1. What can be shot
A consistent breathing truncation exists only in the SO(5)-singlet class (E1), which excludes MN2 (E2). On MN2 the uniform ansatz is inconsistent (E3). So the only shoot that can be posed honestly is a **toy**: wall data (E8) into the (D)-type AdS₅ fixed point of E1. That point is the singlet analogue of the "MN2 IR region".

## 2. Results (toy)
- **S1 (PROVED).** The linearization at the fixed point (L = 1) has eigenvalues −5.211103, −1.464102, +5.464102, +9.211103 on the constraint surface, and +8 off it (constraint-gradient·evec = −12; the others are ≤ 10⁻⁸). The values match s = 2 ± √52 and 2 ± √12, i.e. m²L² = 48 and 8 (Δ = 9.211 and 5.464, both irrelevant).
- **S2 (PROVED).** The IR-regular set (flows reaching the fixed point) is the 2D stable manifold inside the 4D constraint surface, so it has codimension 2.
- **S3 (CONDITIONAL, genericity).** The wall family is one-dimensional (C_w). Since 1 + 2 < 4, generically no wall point lies on the stable manifold, so the expectation is no solution.
- **S4 (CONDITIONAL, numerical).** A scan of C_w − C0 ∈ [−2, 1.5] (141 points) plus refinement finds that every run goes singular before y ≈ 1.5L:
  - For C_w − C0 ≤ 0, C → −8…−10 and A′ diverges.
  - For C_w − C0 ≥ 0.25, B → −20.
  - Closest approach: |Y − FP| = 1.235296 at C_w − C0 = +0.56411119. That is O(1), not a near miss.
  
  **Existence: no solution in the toy. No parameters, and no b is fixed.**

## 3. MN2
- **S5 (OPEN).** A breathing-mode solution from the odd HW-type wall into the MN2 IR: existence is OPEN. The shoot cannot be posed until a consistent truncation around MN2 that keeps the breathing mode is derived (E5/E6). No b is fixed.
- **S6 (OPEN).** A χ-dependent breathing (PDE/cohomogeneity-two) solution is OPEN. Note on counting: if the MN2 analogue keeps S2/S3's structure (a one-parameter wall family against a codimension-≥2 IR set), a solution would need an extra wall modulus. Candidates are a squashing modulus at the face or the n_inst/N_M5 split under f825dfff.

## 4. Junction impact
- Nothing found closes the junction. JS-C with the breathing mode is not dead, but its natural forms fail: the uniform MN2 ansatz is refuted (E3), and the singlet toy has no solution (S4).
- The single blocker is a consistent MN2 breathing truncation (E5/E6).

## 5. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 2 | S1, S2 |
| CONDITIONAL | 2 | S3, S4 |
| OPEN | 2 | S5, S6 |
| REFUTED | 0 | — |
