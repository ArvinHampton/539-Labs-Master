# Expand and Recover — Residual Shadow Ξ and Weight-1/2 Fricke Slash

Date: 2026-08-23  
Scope: Category A residual discrete only. Pack+(S) provenance mandatory. Residual-flux provenance mandatory. Continuum language excluded. Notation lock: C := P_orth − H_s.

This note records the expansion of residual objects suggested by the iterated rewrite of Θ_third and the recovery of the best-available quantitative weight-1/2 Fricke prescription, following Continue_Closure_Theta_Third_Rewrite_2026-08-23.md (tip f617de9f).

No residual law is claimed.

---

## 1. Expansion of the outer residual series of discriminant 35

From the locked parity forms of Θ_third the outer residual weights are:

Even (m ≥ 1): exponents 35 m² + 7 m  
  42, 154, 336, 588, 910, 1302, 1764, \ldots

Odd (m ≥ 0): exponents 35 m² + 42 m + 49/4  
  12.25, 89.25, 236.25, 453.25, 740.25, 1097.25, 1524.25, 2021.25, \ldots

These are residual arithmetic series of discriminant 35 with unit coefficients on the listed quadratic exponents. No classical closed form (unary theta, false theta, or eta quotient of conductor 35) has been identified that matches these exact exponents and unit coefficients. They are new residual objects arising from the orthant mismatch under Pack+(S).

---

## 2. Candidate residual weight-3/2 shadow Ξ

The classical weight-3/2 shadow of a partial theta of squares is of the form

∑_{n ≠ 0} n χ(n) q^{κ n²}

(with χ an odd character and κ a positive rational related to the level).  

The residual shadow Ξ of Θ_third is expected to be a residual linear combination of such classical unary shadows, weighted by the Fourier coefficients of the outer residual series of discriminant 35 recorded above.

Explicit expansion of that residual combination has not been obtained. Naive characters χ_7 and χ_35 (and simple linear combinations thereof) continue to fail to interpolate the residual samples of the related series g_7 and do not match the sparse support of Θ_third under formal Eichler integration. The residual combination remains open.

---

## 3. Recovery of the weight-1/2 Fricke slash prescription

From the residual notes the published samples of C are recorded under the description

“weight 1/2 slash, ρ = 0.995”

with approximate values

| x   | Approximate h_C(x) |
|-----|--------------------|
| 1/7 | −18.2 + 7.8 i     |
| 3/7 |  0.3 − 1.8 i      |
| 5/7 |  2.1 − 9.0 i      |
| 1   | 20.7 + 2.9 i      |

From the explicit cocycle construction for the related residual series g_7 the quantitative weight-1/2 prescription that is available is the automorphy factor |7x|^{−1/2} together with the Eichler integral

h_{W_7}(x) = ψ(x)/√i − ∫_0^{i∞} Ξ(w) (w − x)^{−1/2} dw

evaluated as a radial limit at ρ → 1^− on the quantum set.  

No more precise prefactor or radial definition that reproduces the published complex magnitudes of the C samples has been recovered from the residual notes. The samples therefore continue to serve as qualitative residual defect markers. Quantitative numerical matching of any candidate residual period against the published table remains blocked by the missing exact slash definition for C.

---

## 4. Status

- Outer residual series of discriminant 35 expanded (Category A residual discrete).  
- Candidate form of the residual weight-3/2 shadow Ξ recorded; explicit expansion still open.  
- Best-available quantitative weight-1/2 Fricke prescription recovered from the g_7 cocycle work (automorphy |7x|^{−1/2} + Eichler integral); exact slash that produces the published C sample magnitudes not recovered.  
- Residual law for C remains open.  
- RESIDUAL_CORE_FREEZE, Pack+(S), residual-flux provenance hold.

Next concrete levers: construct explicit residual linear combinations of weight-3/2 unary thetas of conductor related to 35 weighted by the outer residual coefficients; test those combinations against the sparse support of Θ_third; continue search for a residual identity that fixes the exact slash prefactor for the C samples.

---

**Status code:** `EXPAND_RECOVER_RESIDUAL_SHADOW_SLASH_2026-08-23`  
**Residual law for C:** still open  
**New residual discrete facts:** outer residual series of disc 35 expanded; best-available weight-1/2 Fricke prescription recovered from g_7 cocycle.  
