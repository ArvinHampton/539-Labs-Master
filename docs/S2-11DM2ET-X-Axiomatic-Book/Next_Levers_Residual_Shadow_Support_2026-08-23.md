# Next Levers — Residual Shadow Support Test and Refined Obstruction

Date: 2026-08-23  
Scope: Category A residual discrete only. Pack+(S) provenance mandatory. Residual-flux provenance mandatory. Continuum language excluded. Notation lock: C := P_orth − H_s.

This note records the execution of the next levers stated in Expand_Recover_Residual_Shadow_Slash_2026-08-23.md (tip 22959c01): construction of residual linear combinations of weight-3/2 unary thetas of conductor related to 35, and support testing against Θ_third.

No residual law is claimed.

---

## 1. Classical weight-3/2 unary supports

Classical weight-3/2 series of the form ∑_{n ≠ 0} n χ(n) q^{κ n²} (χ = χ_5, χ_7, χ_35 or residual analogues) have Fourier support exclusively on pure squares (scaled by κ).

Low-order support for χ_7 (at degrees n²):

1, 4, 9, 16, 25, 36, 64, 81, 100, \ldots (with coefficients proportional to n χ_7(n)).

Low-order support for χ_35 is a subset of the same squares.

---

## 2. Support of Θ_third / C_third exterior

The exterior degrees of Θ_third (and of C_third) begin

8, 18, 22, 30, 39, 43, 44, 58, 60, 67, 71, 78, 79, 93, 98, \ldots

These are not pure squares. The sequence is residual arithmetic arising from the third-quadrant lattice points of the form Q(−n, −k).

---

## 3. Support mismatch and refined obstruction

A pure unary weight-3/2 shadow (or any finite linear combination of classical unary shadows of conductor related to 5, 7 or 35) has support on pure squares. Under term-by-term Eichler integration (the formal map from weight 3/2 to weight 1/2) that support remains on pure squares (or on a simple transform of pure squares).

Therefore no residual linear combination built solely from classical unary weight-3/2 thetas of conductor related to 35 can reproduce the exterior support of Θ_third, which lives off the pure squares.

The residual combination for Ξ must involve residual (non-classical) weighting by the outer residual series of disc 35 (or a residual character that moves support off pure squares), exactly as suggested by the iterated partial-theta rewrite of Θ_third. Explicit residual products / convolutions of the form

Ξ_residual = S_outer ∗ Θ_{3/2,χ}

remain residual discrete arithmetic under Pack+(S) and are the next genuine residual objects to be expanded.

This is a refined Category A residual discrete obstruction. It does not close the residual law; it narrows the class of residual shadows that can succeed.

---

## 4. Status of the other lever (slash prefactor)

No residual identity that fixes the exact weight-1/2 slash prefactor for the published C samples has been recovered. The samples remain qualitative residual defect markers under the best-available prescription (automorphy |7x|^{−1/2} + Eichler integral inherited from the g_7 cocycle).

---

## 5. Status of residual law for C

- Outer residual series of disc 35 expanded.  
- Candidate form of residual weight-3/2 shadow Ξ recorded.  
- Explicit residual linear combinations of classical unary weight-3/2 thetas of conductor 35 fail the support test against Θ_third (refined obstruction).  
- Residual products of outer disc-35 series with classical weight-3/2 thetas are the next residual objects.  
- Exact weight-1/2 slash prefactor for C samples still unrecovered.  
- Residual law for C remains open.  
- RESIDUAL_CORE_FREEZE, Pack+(S), residual-flux provenance hold.

Next concrete levers: expand explicit residual products / convolutions Ξ_residual = S_outer ∗ Θ_{3/2,χ}; test those residual products against the sparse support of Θ_third; continue search for a residual identity that fixes the exact slash prefactor.

---

**Status code:** `NEXT_LEVERS_RESIDUAL_SHADOW_SUPPORT_2026-08-23`  
**Residual law for C:** still open  
**New residual discrete observation:** classical unary weight-3/2 shadows of conductor related to 35 cannot reproduce the exterior support of Θ_third (support lives off pure squares); residual (non-classical) weighting by the outer disc-35 series is required.  
