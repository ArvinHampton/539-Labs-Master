# ADDENDUM T — Owner t4124 "immutable rank 36" draft (relay-based; by hand from R.1/S; No CERT; no .tex)

## 1. The rank-36 theorem: correct for this table only
- The periodic 12-dimensional kernel alone gives only nullity ≥ 12, that is, rank M ≤ 36.
- Equality needs the exact nonzero spectrum of the q-even characters from Addendum S: 12 nonzero values. With it, rank M = 36 exactly for the EXACT A/B/C/D table.
- It does NOT hold for "all positive orbit weights." The claims "immutable regardless of parameters" and "no internal conductance adjustment can fix it" are FALSE.

## 2. Counterexample (VERIFIED by hand)
- Change only α6: B → B + 1 = 7 − √35 on O6 = {xy³}. Everything else stays the same: same selectors, w = y, no self-loop.
- Admissibility checks:
  - π(xy³) = (1, 2−3, 0) = (1, 3, 0) = xy³, so the orbit is π-fixed and the twisted symmetry still holds.
  - 7 − √35 ≈ 1.08 > 0, so positivity still holds.
  - The y³ coefficient stays 0.
- Effect on H: (xy³)·y = x, so H′ = H + R_x. R_x flips j and acts as the identity on C4 × C6, so H01′ = H01 + I24.
- Cross-block eigenvalues become μ + 1:
  - the 12 zero values become 1;
  - the nonzero values in S are 76+16√35, ±4, ±2, 10−8√35, 14−8√35 and 20−8√35, and none of them equals −1.
- So rank H01′ = 24 and rank M′ = 48, which is FULL rank.
- Full spectrum: λ′(χ) = λ(χ) + (−1)^p. Every R.1 value has a nonzero √35 coefficient, so the shifted H′ remains invertible.
- New degree: δ′ = 128 + 39√35.
- Caveat: this is a change to the explicit table and its degree, not a proof about the original table.

## 3. Other fixes
- **Capacity:** still OPEN because the identification of N and W is missing. That has nothing to do with the kernel.
- **Index-sum proof:** fix the double sum over l. The per-row scalar is not identically zero across the 24 rows.
- **Selectors vs package:** the rank depends on both the table (H01) and the selectors. The choice is the Owner's.
