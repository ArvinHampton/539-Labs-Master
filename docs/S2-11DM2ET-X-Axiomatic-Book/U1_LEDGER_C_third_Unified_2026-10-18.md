# U1 LEDGER — C_third from one coset, one cone weight, one kernel on two chains (2026-10-18)

Packages: `C_third_Unified_2026-10-18/`, `C_third_Closure_2026-10-18/`. Consolidated: rev. 4 Theorem 12.2.
Text outputs (json/log/txt) of each package are stored verbatim in its `OUTPUTS_BUNDLE_2026-10-18.txt` (member byte counts and sha256 included); reports and scripts are separate files.
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact (incl. exact finite computation); floating-only = Cat B. See ERRATUM_Consolidated_CrossReview_2026-10-18.md.

## Category A
- A1. For every s ≥ 5: 2C_third,s − 1 + θ₃ = q^{c₀}Θ_w(a), Θ_w(a) = Σ_{ν∈a+Z²} w(ν)q^{Q(ν)}, w = 1_{F′} + 1_{−Q₁} (one coset, one form, one non-negative cone weight). Proved; checked to q³⁰⁰⁰ (s = 7) and q²⁰⁰⁰ (s = 5..25, 41).
- A2. **Lemma R.** R_s = [[1,s],[0,−1]]: R_sᵀA_sR_s = A_s, R_s a = −a, R_sF is a γ-fundamental cone; E^F_a = E^F_{−a} for every s ≥ 5. Proves E_{−a} = E_a family-wide (C15). Θ_w = E_L + ϑ_hol: even part of w → E_L, odd part → ϑ_hol; the weight-1 piece on the unit cone is 0.
- A3. Kernel Ξ = Ξ₀ + Ξ₁ on the path of lines c(t): on Γ_{Q₁}, ∫Ξ₁ dt is exactly Zwegers' 2002 completion (holomorphic part ϑ_hol) — exact (FTC with Siegel-majorant domination).
- A4. No single modular object: the two outputs carry (cτ+d) vs |cτ+d| factors (Theorems O1, O2 still apply).
- A5. **Lemma Prod1** (= Lemma C1 of the report): finite sums of weight-0 log-cocycle × holomorphic weight-1 products have only t^{−2}, t^{−1}log t, t^{−1} radial terms and cannot carry either sector.

## Category B
- Weight-0 identification ∫_{Γ_F}Ξ₀ = Zwegers 2012 mock Maass theta (shadow-free, E_L = ½ϑ_a) by citation via a restatement; numerical agreement 8e-16 (s = 7, 9), 5e-15 (s = 13).
- ∫_{Γ_F}Ξ₁ = 0 (numerical ≈ 1e-15; pairing argument not written out). Non-γ control: shadow does not cancel (≈ 0.1).
- **Lemma Prod2** (= Lemma C2): conditional on the inputs of O1. "No exotic single kernel exists": open.
