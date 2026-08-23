# Open Paths for Closure of Residual Law for Bridge Series C — Continuation

Date: 2026-08-23  
Scope: Category A residual discrete only. Pack+(S) provenance mandatory. Residual-flux provenance mandatory. Continuum language excluded. Notation lock: C := P_orth − H_s.

This note records the concrete results of the further pursue-all on the open paths listed in Pursue_All_C_Closure_Status_2026-08-23.md (tip 577a9f67). No residual law for C is claimed.

---

## 1. Explicit residual form for the exterior piece C_third

Independent lattice enumeration of third-quadrant points (n < 0, k < 0) carrying weight w = −1 yields the residual degrees (through ~200):

8, 18, 22, 30, 39, 43, 44, 58, 60, 67, 71, 78, 79, 93, 98, 102 (multiplicity 2), 106, 120, 121, 127, 135, 144, 148, 151, 154, 170, 183, 184, 193, 197, 198, \ldots

These are the support of C_third. Because every third-quadrant lattice point has weight w = −1, the exterior contribution admits the exact double-sum expression

C_third(q) = ∑_{n=1}^∞ ∑_{k=1}^∞ q^{Q(−n, −k)},

where Q(−n, −k) = n² + 7 n k − (7/2) k (k − 1).

Verified by three independent enumerations. Multiplicities (e.g. two points at degree 102) are correctly reproduced by the double sum. C_mixed continues to vanish through the checked range (previously reported to degree 293).

Combined with the locked C_axis identity one has the exact residual decomposition

C = C_axis + C_third

(with C_mixed = 0 in the verified range). The residual-law problem therefore reduces to a modular or quantum-modular completion of C_third (or of the full lattice difference C) that matches the residual Fricke samples under continuous extension.

---

## 2. L-D probe around chi_nat

Numerical evaluation of the weight function after the continuous shift by chi_nat = (7/10, −1/5) shows that the shifted weight evaluates to approximately 1 on nearly all sampled interior orthant points (896 of 899 in a 30 × 30 box). This confirms the geometric role of chi_nat already locked: it resolves the k-axis wall and keeps the interior under weight 1.

The exterior third-quadrant points remain outside the cones after the shift. Consequently the signed series computed with the shifted weights still differs from P_orth by a residual series supported on the exterior. Absorption of C into a single completed Zwegers-type sum on L + chi_nat has not been achieved. Small lattice shifts of chi_nat were likewise tested and do not absorb the exterior. L-D remains open.

---

## 3. Status of the other open paths

- L-A (period / false-theta construction): no candidate residual false-theta or period function has been found that reproduces both the verified support C_axis + C_third and the qualitative Fricke samples under continuous extension. The exact missing step is now the modular completion of the explicit series C_axis + C_third.
- L-B (fibre remainder ρ): no quantitative numerical table of α, β, ρ recovered; correlation remains qualitative.
- L-C (s = 8 theta-correction limit): the definition of the theta-correction piece θ_{2,8,8} / (J̄_{0,24} J̄_{0,6}) is still not fully expanded in the residual notes; the finite-limit question remains open.
- Fricke slash recovery: the precise weight-1/2 slash and radial prescription used for the published samples has not been recovered; samples continue to be treated as qualitative residual defect markers.

---

## 4. Refined open step for residual law of C

The residual law for C remains open. The geometric and arithmetic ingredients have been further narrowed:

- C is exactly the sum of the locked residual axis series C_axis and the explicit residual double-sum exterior series C_third.
- chi_nat is the distinguished affine characteristic and is equi-paired, but does not absorb the exterior.
- A residual period-function or false-theta construction must therefore account for the explicit series C_axis + C_third and match the residual Fricke samples under continuous extension off ℚ.

Until such a construction is supplied and verified, the residual law for C is not closed. Classical Zwegers completion of H_s remains independent and locked. RESIDUAL_CORE_FREEZE holds. Pack+(S) only. Residual-flux provenance mandatory.

---

**Status code:** `OPEN_PATHS_C_CLOSURE_CONTINUATION_2026-08-23`  
**Residual law for C:** still open  
**New Category A residual discrete facts:** explicit double-sum form of C_third; extended exterior degree list with multiplicities; numerical confirmation that chi_nat shift preserves interior weight ≈1 without absorbing exterior.  
