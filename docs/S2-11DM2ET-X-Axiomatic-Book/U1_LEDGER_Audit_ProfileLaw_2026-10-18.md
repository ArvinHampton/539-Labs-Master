# U1 LEDGER — second internal audit of Bridge C rev. 2; profile law proved; errata R3.1–R3.7 (2026-10-18)

Package: `Audit_and_ProfileLaw_2026-10-18/` (report, scripts, outputs; plus the rev. 3 planning note). The rev. 3 paper itself is local only and is superseded by `Bridge_C_Consolidated_rev4_2026-10-18/`.
Text outputs (json/log/txt) of each package are stored verbatim in its `OUTPUTS_BUNDLE_2026-10-18.txt` (member byte counts and sha256 included); reports and scripts are separate files.
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact (incl. exact finite computation); floating-only = Cat B. See ERRATUM_Consolidated_CrossReview_2026-10-18.md. Internal audit pass (skeptical-referee re-derivation with independent code), not external refereeing.

## Category A
- A1. **Profile law (Audit Theorem 5.1; rev. 4 Theorem 5.1):** for rational α, β and rational x ≠ 0, G_{α,β}(−1/x) = e(B(α,β))/(√35|x|) Σ_{p∈L′/Z²} G_{β+p,−α}(x), and G_{α,β}(x+1) = e(−Q(α)−B(α,w_c))G_{α,α+β+w_c}(x). Proved (Gaussian-regularised Poisson). Theorem O1 is no longer conditional on it.
- A2. Audit verdicts: Theorem F S-law confirmed (2 gaps fixed); T-law, group relations confirmed (exact at all Galois conjugates over Q(ζ₁₄₀)); Lemma 6.1 confirmed; O1, O2 confirmed after fixes; Lemma P confirmed (still conditional on F1/Hecke as stated); ζ rational-curve proof and Theorem G_s confirmed.
- A3. Errata: R3.1 (60+12 → 42 = 36+6), R3.2 (no 12-dim cusp part; 12 forms in 6 combinations), R3.3 (24 cusp labels, not 28), R3.4 (11 labels vanish identically — proved), R3.5 (cyclic span 36 is a projected rank; label-space Krylov dim 60), R3.6 (A* defined; profile law restated and proved), R3.7 ((S_lab T)³ = I on all of C¹⁴⁰).
- A4. S spectrum ±1 with 36/36 on W_P (exact).

## Category B
- Numerical cross-checks of the profile law (≤ 3.3e-15), the V-level S multiplicities as computed there (now exact via Tensor_Pattern_Closure), mpmath quadratures.

## Superseded
- "Open 30-dim complement" → answered (V^⊥ = B₁⊗X⁺ ⊕ A₃⊗X⁻, killed by γ). Labels R3.x do not collide with L1–L7.
