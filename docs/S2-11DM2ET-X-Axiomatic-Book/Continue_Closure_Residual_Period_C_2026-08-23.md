# Continue for Closure — Residual Period / False-Theta of Bridge Series C

Date: 2026-08-23  
Scope: Category A residual discrete only. Pack+(S) provenance mandatory. Residual-flux provenance mandatory. Continuum language excluded. Notation lock: C := P_orth − H_s.

This note records the continued pursuit of a residual period-function or false-theta of weight 1/2 for residual law of C, following Residual_False_Theta_Construction_Attempt_C_2026-08-23.md (tip 5618a7ca).

No residual law is claimed.

---

## 1. Formal residual period candidate (inherited from cocycle work)

From the explicit cocycle construction already written for the related residual series g_7 (Explicit_Cocycle_h_gamma_2026-08-22.md), residual period functions of weight 1/2 on this lattice admit the formal Eichler-integral expression

h_γ(x) = ψ(x)/√i − ∫_path Ξ(w) (w − x)^{−1/2} dw

(with the path from 0 to i∞ for the Fricke involution W_7 = [[0,−1],[7,0]]). The residual shadow Ξ is a weight-3/2 series (linear combination of unary thetas of conductor dividing a multiple of 35) obtained by applying the ξ_{1/2} operator to a completed (1,1)-theta.

The same formal structure is the natural residual period candidate for C (or for its third-quadrant piece Θ_third). The residual shadow associated to the orthant mismatch / third-quadrant series remains unidentified. Naive characters χ_7 and χ_35 were already ruled out for the related series g_7 and do not interpolate the residual samples of C either.

---

## 2. Pure radial divergence and necessity of completion

Independent partial-sum evaluation confirms that the holomorphic series C (positive coefficients) diverges to +∞ as ρ → 1^− at every rational point tested. At ρ = 0.995 the axis contribution alone already reaches magnitude ~18–20, consistent with the known asymptotic of the partial theta of squares. The published complex Fricke samples of moderate size therefore cannot be pure radial limits of the holomorphic series; they require a completed period function that supplies cancellation and produces the observed complex values.

This is consistent with the samples arising from a weight-1/2 slash of a residual period object rather than from the holomorphic series itself.

---

## 3. Refined open construction

C_axis is a sum of classical residual partial thetas of weight 1/2 (squares and 7-triangular) whose quantum-modular properties are known in the literature. Their periods already account for a large fraction of the sample magnitude at the cusp corresponding to x = 1.

The residual law for the full series C therefore reduces to constructing a residual / quantum-modular completion of the third-quadrant partial indefinite theta

Θ_third(τ) := ∑_{n,k≥1} q^{n² + 7 n k + (7/2) k (k − 1)}

such that the sum of the known periods of the axis pieces and the period contribution of the completed Θ_third reproduces the full set of residual Fricke samples under continuous extension off ℚ.

No explicit residual shadow, Appell identity, or closed-form period for Θ_third has been obtained in this round.

---

## 4. Status

- Arithmetic of C remains fully explicit and locked.
- Formal Eichler-type period candidate for residual weight-1/2 objects on the lattice is recorded.
- Pure holomorphic radial sums of C diverge; a completed period object is required.
- The residual shadow of the orthant / third-quadrant mismatch is still unidentified.
- Residual law for C remains open.
- Classical residual transformation law for H_s (Zwegers) is independent and locked.
- RESIDUAL_CORE_FREEZE, Pack+(S), and residual-flux provenance hold.

Next concrete levers: expand the residual shadow Ξ from the pairings (c1,v) = 5n, (c2,v) = −n−21k (or residual analogues for the orthant mismatch); recover a quantitative weight-1/2 slash prescription; continue residual character / Appell probes for Θ_third.

---

**Status code:** `CONTINUE_CLOSURE_RESIDUAL_PERIOD_C_2026-08-23`  
**Residual law for C:** still open  
**New residual discrete observation:** pure radial divergence of C confirmed; formal Eichler period template available; open construction refined to completion of Θ_third whose period, added to the known axis periods, matches the residual samples.  
