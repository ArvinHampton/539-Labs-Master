# s-family: internal patterns, pre-registered observable matching, structural links

Prepared 20 Oct 2026 (CDT). Local only: nothing was posted, the repo was not edited and nobody was contacted. All computations use PARI (cypari2), numpy and scipy.

Files:
- `partA_table.csv` (s = 5..500), `partA_analysis.out`, `partA_correlations.csv`.
- `PREREG.md`, with sha256 and timestamp in `prereg.sha256`. It was written before `partB_match.py` was run.
- `partB_results.json`, `partB_matches.csv`, `partB_posthoc.json`.

Part A is labelled Category A where proved, Category B otherwise. Part C is Category B, speculative.

## Part A: internal patterns (s = 5..500)

The table was built with the manuscript's definitions (s01_intro.tex:131-134). The cusp dimension uses d_cusp = dim V − d_Eis, where:
- dim V is the orbit bound s(s−1) for odd s and (s/2)(s/2+1) for even s, reduced by m(m−1) when s = 2m² (s12_dims.tex:8-15);
- d_Eis is the manuscript formula (s12_dims.tex:16-19);
- the manuscript value dim V = 2406 is used at s = 98.

**Check:** these formulas reproduce all 48 tabulated (dim V, d_Eis, d_cusp) rows exactly (s = 5..51 and 72). For s > 51 they are extrapolations, so Category B. The manuscript proves exactness only for s ≤ 51 and certifies d_Eis only for the listed local factors.

### Proved (Category A)

1. **When ε_s is not the fundamental unit.** Write ε_s = η^k with η the fundamental unit and t its trace. Then:
   - for N(η) = +1, ε_s = η^k exactly when s − 1 = T_k(t/2) (T_k the Chebyshev polynomial);
   - for N(η) = −1, the analogous condition holds with the norm −1 trace.

   This is standard: if η = (t+u√d)/2, then η^k + η^{−k} = 2T_k(t/2). The 34 cases with k > 1 for s ≤ 500 are listed in `partA_analysis.out`, and every one satisfies the condition with the computed integer trace. The cases fall into these families:
   - k = 2, N = +1: s = 2m², for example 8, 32, 50, 72, 128 (the manuscript's mechanism, s12_dims.tex:14-15). At s = 18, 98 and 162 the power is 4 or 12, not 2.
   - k = 2, N = −1: s = 2m² + 2, i.e. 20, 34, 52, 74, ….
   - k = 3: s − 1 = (t³ − 3t)/2, i.e. s = 27, 56, 245, 352, 486.
   - k = 5: s = 363 (t = 4).
   - k = 6 or 12: s = 10, 100, 162.

   In total ε_s is fundamental for 462 of 496 values of s.
2. **Genus theory.** 2^{ω(d_K)−1} divides h⁺(K) for every s, verified 100%. It follows that h⁺ is divisible by 4 on the twin-prime subfamily (d_K = 4(s−2)s, ω = 3), as observed for all 24 twin-prime s up to 500.
3. **Closed form for odd s,** given the manuscript's Theorem dims (iii) and dim V = s(s−1): d_cusp = s(s−1) − 3∏_{p^e‖n_s}(p^e+1)/2.

### Empirical (Category B)

- **Zero cusp part:** d_cusp = 0 only at s = 6, 8, 10, both in the tabulated range and in the extrapolation to 500.
- **Parity:** d_cusp is even for every s ≤ 500. This is not proved here.
- **Growth:** d_cusp/dim V tends upward. log(ratio) ≈ 0.24 log s + const for odd s (r = 0.55) and 0.33 log s + const for even s (r = 0.64). The median ratio for s > 200 is 0.59 (odd) and 0.61 (even). This is a trend, not a closed-form law.
- **Cohen–Lenstra:** among the 479 distinct fields, 53.9% have trivial odd part of h. The Cohen–Lenstra heuristic for real quadratic fields gives about 75.4% (95% half-width 3.9%), so these fields depart from it. That is expected rather than anomalous: d = m² − 1 (m = s − 1) is Richaud–Degert type, with an unusually small regulator (ε_s ≈ 2√d), so class numbers run larger (Yokoi; Mollin, *Quadratics*, 1996). The heuristic assumes generic regulators.
- **Correlations:** 36 Spearman tests (raw, and with the log-s trend removed), with 2000-sample permutation p-values and BH correction; see `partA_correlations.csv`. Every BH-significant correlation follows from known relations:
  - h⁺ against the ray-class number (ρ = 0.91): the ray-class exact sequence.
  - h⁺ against the conductor f (ρ = −0.85 detrended): the class number formula h·R ~ √d_K, with d_K = 4n_s/f².
  - regulator against k (ρ = −0.97 detrended): R = log ε_s / k.
  - correlations with s itself: Brauer–Siegel growth.

  No correlation was found that is unexplained.

## Part B: pre-registered observable matching

**Setup** (PREREG.md):
- Quantities: Q1 = 2 log ε_s, Q2 = I_s, Q3 = h⁺/h, Q4 = d_cusp/dim V (tabulated s), Q5 = √n_s. That is 2032 values.
- Operations: x, 1/x, 2x, 3x, x/2 and x/3.
- 16 cited targets.
- **N = 195 072 trials.**
- Criterion: |f(x) − y| ≤ max(σ, 10⁻³|y|).

**Deviation from the pre-registration, disclosed:** T15's σ was recomputed from the cited inputs as 54.6 (×10⁻⁸), not the 58.4 typed in PREREG. That is an arithmetic slip in the pre-registration and does not change any conclusion.

### Pre-registered result

- **Observed M = 10 633 matches.**
- Null means (10⁴ trials each):
  - N1 log-uniform: 11 903 ± 45, p = 1.0.
  - N2 random-field units: 8822 ± 44, p ≈ 1e-4.
  - N3 random integers: 10 505 ± 23, p ≈ 1e-4.
- **The global count is dominated by two pre-registered targets that turned out to be degenerate:**
  - T15 (g−2 deviation 33 ± 55): any value in [−22, 88] matches, giving 10 067 of the matches.
  - T16 (m_W CDF/PDG = 1.0008, with tolerance 10⁻³): any value equal to 1 matches, so the 496 values of Q3 = 1 all match.
- The low p-values under N2/N3 come from differences between those nulls and the s-family value distribution inside the wide T15 window. They do not reflect precise matches. The p-values disagree across nulls (1.0 against 1e-4), which shows the global statistic is null-model-dependent and uninformative.

### Post-hoc (labelled; `partB_posthoc.py`)

Excluding T15 and T16:

| | Count |
|---|---|
| Observed | 67 |
| N1 | 172.8 ± 13.1 (p = 1.0) |
| N2 | 90.1 ± 9.5 (p = 0.99) |
| N3 | 145.3 ± 11.6 (p = 1.0) |
| N4 (jitter: each true value × e^{N(0,0.02)}, closest-matched distribution) | 69.2 ± 6.1 (p = 0.67) |

**The s-family produces no more matches than distribution-matched random numbers.**

Per target:
- No target is significant under N4.
- T1 (α⁻¹) had p = 0.04 under N1 only. With 16 × 4 tests that is not significant, and under N2, N3 and N4 the p-values are 0.22–0.48.
- **None of the 67 matches is within 1σ for any precision target (T1–T5).** They pass only through the 10⁻³ relative tolerance.

Examples:
- √n_s at s = 138 is 136.996, against α⁻¹ = 137.036: a relative difference of 2.9e-4, i.e. 1.9×10⁶ σ. This is a trivial near-integer, since √(s(s−2)) ≈ s − 1.
- 1/I_s at s = 470 is 137.059 (1.7e-4, about 10⁶ σ).
- 1/I_s at s = 37 is 16.830, against m_τ/m_μ = 16.817 (0.08%, 12σ).
- (d_cusp/dim V)/2 at s = 41 (758/1640/2), giving 0.2311, against sin²θ_W = 0.23129 (0.08%, 5σ).

**Verdict for Part B: chance.**

The value s = 7 itself matches nothing: 2 log ε₇ = 4.9558, I₇ = 0.20942, √35 = 5.916, d_cusp/dim V = 1/7.

## Part C: structural correspondences (Category B, speculative)

1. **Weil representation as a quantum cat map (most promising).**
   - γ_s = [[−1,−s],[2,2s−1]] is a hyperbolic SL₂(Z) element with entropy log ε_s, an Anosov cat map.
   - Its quantization is given by the Weil (metaplectic) representation: Hannay & Berry, Physica D 1 (1980) 267; Kurlberg & Rudnick, Duke Math J 103 (2000) 47 (Hecke eigenbases).
   - The Bridge C label space carries exactly a Weil representation of the discriminant form (s03_main.tex:77-87; s12_dims.tex proof notes).
   - **Next computation:** the spectrum of ρ_s(γ_s) on W_P for s = 5..60. Compare the eigenphase statistics and the period of ρ_s(γ_s) mod the label level with Kurlberg–Rudnick predictions. Test whether the cusp sector V_cusp coincides with an anti-invariant or Hecke-eigen subspace.
2. **Indefinite theta series and wall-crossing / two-centred black-hole bound states.**
   - Signature-(1,1) Zwegers theta functions count two-centre D4-D2-D0 bound states: Manschot, arXiv:0906.1767 and arXiv:1009.1775; Alexandrov–Banerjee–Manschot–Pioline, arXiv:1606.05495 (generalized error functions).
   - The mock modularity of BH microstate generating functions: Dabholkar–Murthy–Zagier, arXiv:1208.4074.
   - **Next computation:** identify whether a lattice ⟨2⟩⊕⟨−2(s−2)s⟩-type form, with the cone walls c₁ = (−1,1) and c₂ = (−4,1), arises as the charge lattice of a two-centre configuration (some CY₃ intersection form, with D = s(s−2)). If it does, compare H_s with the corresponding index jump across the wall.
3. **Quantum modularity and 3-manifold invariants.**
   - The radial and rational values ψ(h/m) of the Bridge C period function (s07_lz.tex:13) are cyclotomic. Quantum modular forms arising from false and indefinite theta series give WRT and Ẑ invariants: Zagier, "Quantum modular forms" (Clay Math Proc. 12, 2010); Lawrence–Zagier, Asian J Math 3 (1999) 93; Gukov–Pei–Putrov–Vafa, arXiv:1701.06567; Cheng–Chun–Ferrari–Gukov–Harrison, arXiv:1809.10148.
   - **Next computation:** test whether ψ(h/m) at s = 7 satisfies a quantum-modular cocycle with real-analytic error. Search the plumbed or Seifert manifolds whose Ẑ uses an indefinite lattice of determinant −n_s.

Also noted but weaker:
- K3 lattices and Mathieu moonshine (Eguchi–Ooguri–Tachikawa, arXiv:1004.0956). The manuscript's K3 section addresses only lattice embedding; no elliptic genus appears.

**None of the three is an observable prediction.** They are mathematical correspondences that could become physics only through such a construction.
