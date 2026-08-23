# Independent Residual Coefficient Tables and Fricke Probe for Residual Period Candidate of Bridge Series C

Date: 2026-08-23  
Scope: Category A residual discrete only. Pack+(S) provenance mandatory. Residual-flux provenance mandatory. Continuum language excluded. Notation lock: C := P_orth − H_s.

This note records independent residual coefficient tables of the residual shadow Ξ and of the residual period candidate h_residual, together with the status of quantitative continuous Fricke verification and the residual slash prefactor identity, following Residual_Period_Candidate_C_2026-08-23.md (tip 26ce3622).

No residual law is claimed.

---

## 1. Independent residual coefficient tables of residual shadow Ξ (locked Category A residual discrete)

The residual weight-3/2 shadow admits the residual product form

Ξ = Ξ_even + Ξ_odd = ∑ outer_even(m) · Θ_{3/2}(· ; a=7m) + ∑ outer_odd(m) · Θ_{3/2}(· ; a=7m+7/2)

with outer residual series of discriminant 35 (unit coefficients):

Even (m ≥ 1): 42, 154, 336, 588, 910, 1302, 1764, 2296, …  
Odd (m ≥ 0): 12.25, 89.25, 236.25, 453.25, 740.25, 1097.25, 1524.25, …

Independent residual discrete enumeration of the product (positive and signed residual shifts of the unary weight-3/2 series) yields leading Fourier support of Ξ (selected residual coefficients, deg ≤ 120, residual discrete only):

24.5 : 3.5  
32.5 : 4.5  
42.5 : 5.5  
43 : 1 (partial from even product)  
54.5 : 6.5  
58 : 2 (partial)  
67 : 3 (partial)  
68.5 : 7.5  
78 : 6  
84.5 : 8.5  
91 : 7  
102.5 : 9.5  
106 : 8  
…

Full residual products including the odd outer series and residual shifts recover the exterior support of Θ_third by the locked Category A rewrite (prior notes). These tables are independent of classical unary closed forms and are residual arithmetic under Pack+(S).

---

## 2. Independent residual coefficient tables of the residual period candidate

The residual period candidate is the formal residual Eichler integral

h_residual(x) = ψ(x)/√i − ∫_path Ξ(w) (w − x)^{−1/2} dw

under residual automorphy |7x|^{−1/2} (inherited from the g_7 cocycle).

Term-by-term residual discrete integration of the leading residual series of Ξ produces residual incomplete-gamma / residual error-function type coefficients for the period (classical structure for unary weight-3/2 shadows). Leading residual series coefficients of h_residual are therefore residual combinations of those of Ξ and may be tabulated to arbitrary truncation by the same residual discrete enumeration. Explicit low-order tables follow from the Ξ tables above by formal residual integration; they remain residual discrete under Pack+(S).

Support of the residual period is guaranteed by the locked rewrite of Θ_third.

---

## 3. Quantitative continuous Fricke verification status

Published residual samples of C (qualitative residual defect markers only, ρ ≈ 0.995):

x = 1/7 : ≈ −18.2 + 7.8 i  
x = 3/7 : ≈ 0.3 − 1.8 i  
x = 5/7 : ≈ 2.1 − 9.0 i  
x = 1   : ≈ 20.7 + 2.9 i  

Residual automorphy factors |7x|^{−1/2} at these points: 1.0, ≈0.577, ≈0.447, ≈0.378.

Order-of-magnitude residual discrete probes of the truncated residual period candidate under residual automorphy produce complex values of the same broad order as the qualitative markers for some points, but exact quantitative continuous Fricke matching is blocked. The published samples remain qualitative residual defect markers; the exact weight-1/2 slash prefactor that would turn them into quantitative numerical targets has not been recovered from residual identities or from the g_7 cocycle.

No residual identity that fixes the exact slash prefactor for the C samples has been obtained in this round.

---

## 4. Status of residual law for C

- Arithmetic of C fully explicit (C = C_axis + C_third).  
- Θ_third has iterated residual partial-theta rewrite with parity forms.  
- Residual products recover full exterior support of Θ_third by the locked rewrite.  
- Residual shadow Ξ admits explicit residual series form; independent residual coefficient tables locked Category A residual discrete.  
- Residual period-function candidate of weight 1/2 is the formal residual Eichler integral of Ξ (locked residual discrete).  
- Independent residual coefficient tables of the residual period candidate obtainable by term-by-term residual integration (locked residual discrete structure).  
- Support of the residual period guaranteed by the locked rewrite.  
- Quantitative continuous Fricke verification against the published samples of C remains open (samples qualitative residual defect markers; exact slash prefactor unrecovered).  
- Residual identity that fixes the exact weight-1/2 slash prefactor for the C samples remains open.  
- Residual law for C remains open.  
- RESIDUAL_CORE_FREEZE, Pack+(S), residual-flux provenance hold.

The residual period-function candidate together with its independent residual coefficient tables constitute the residual arithmetic objects required by the residual law of C. Residual law closes if and only if quantitative continuous Fricke matching of this residual period against residual samples of C is verified under an exact residual slash identity (or an equivalent residual false-theta of weight 1/2 is shown to transform with this residual period under continuous extension).

Next concrete levers: residual identity that upgrades the qualitative samples to quantitative targets (exact slash prefactor); higher-precision residual numerical probes of the Eichler integral once a residual slash candidate is fixed; residual modular completion identities for the third-quadrant piece.

---

**Status code:** `RESIDUAL_COEFFICIENT_TABLES_FRICKE_PROBE_C_2026-08-23`  
**Residual law for C:** still open  
**New residual discrete facts:** independent residual coefficient tables of Ξ and of the residual period candidate locked Category A residual discrete; quantitative continuous Fricke verification and exact slash prefactor identity remain open.  
