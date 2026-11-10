# Pre-registration: s-family vs. observables (written before any matching was computed)

Fixed 20 Oct 2026 01:15 CDT. File mtime and sha256 are recorded in prereg.sha256.

## (1) s-family quantities

For every integer s from 5 to 500 (496 values), with n_s = s(s−2) and ε_s = (s−1)+√n_s:
- Q1 = 2 log ε_s (entropy of the cat map γ_s).
- Q2 = log ε_s / (2√n_s) (the leading constant I_s; I_7 = 0.20942).
- Q3 = h⁺(D_s)/h(D_s) for the order discriminant D_s. Values are 1 or 2; it is trivial, but included as registered.
- Q4 = d_cusp/dim V, only for the s in the manuscript table (s = 5..51 and 72; 48 values).
- Q5 = √n_s.

Number of values: 4×496 + 48 = 2032.

## (2) Targets

Each is a measured dimensionless observable with a cited 1σ uncertainty.

| id | Observable | Value ± 1σ | Source |
|---|---|---|---|
| T1 | α⁻¹ | 137.035999177 ± 0.000000021 | CODATA 2022, https://physics.nist.gov/cgi-bin/cuu/Value?alphinv |
| T2 | m_μ/m_e | 206.7682827 ± 0.0000046 | CODATA 2022, https://physics.nist.gov/cgi-bin/cuu/Value?mmusme |
| T3 | m_p/m_e | 1836.152673426 ± 0.000000032 | CODATA 2022, https://physics.nist.gov/cgi-bin/cuu/Value?mpsme |
| T4 | m_τ/m_e | 3477.23 ± 0.23 | CODATA 2022, https://physics.nist.gov/cgi-bin/cuu/Value?mtausme |
| T5 | m_τ/m_μ | 16.8170 ± 0.0011 | derived from T4/T2 (uncertainty propagated from T4) |
| T6 | sin²θ_W(M_Z) MS-bar | 0.23129 ± 0.00004 | PDG 2024, https://pdg.lbl.gov/2024/reviews/rpp2024-rev-standard-model.pdf (Table 10.2) |
| T7 | α_s(M_Z) | 0.1180 ± 0.0009 | PDG 2024 booklet, https://pdg.ge.infn.it/2024/download/db2024.pdf |
| T8 | Jarlskog J ×10⁵ | 3.08 ± 0.15 | arXiv:2309.07656 (consistent with the PDG fit); larger side of the asymmetric error used |
| T9 | Ω_b h² | 0.02237 ± 0.00015 | Planck 2018 VI, arXiv:1807.06209, Table 2 (TT,TE,EE+lowE+lensing) |
| T10 | Ω_c h² | 0.1200 ± 0.0012 | same |
| T11 | n_s (spectral index) | 0.9649 ± 0.0042 | same |
| T12 | ln(10¹⁰ A_s) | 3.044 ± 0.014 | same |
| T13 | H0(SH0ES)/H0(Planck) | 73.04/67.36 = 1.0843 ± 0.0177 | Riess+2022 arXiv:2112.04510 (73.04 ± 1.04); Planck 2018 (67.36 ± 0.54); errors in quadrature |
| T14 | S8 (Planck) | 0.832 ± 0.013 | Planck 2018 VI, Table 2 |
| T15 | a_μ(exp)/a_μ(SM) − 1, ×10⁸ | (116592071.5 − 116592033)/116592033 ×1e8 = 33.0 ± 58.4 | exp. world avg 2025 and WP25 SM, https://muon-gm2-theory.illinois.edu/white-paper-25/ |
| T16 | m_W(CDF)/m_W(PDG) | 80.4335/80.3692 = 1.000800 ± 0.000204 | CDF Science 376 (2022) 170; PDG 2024 booklet m_W = 80.3692(133) GeV; errors in quadrature |

**Excluded before looking.**
- Lithium-7 problem ratio: the ratio is quoted in many inconsistent forms.
- ATOMKI X17: dimensionful mass, and contested.
- R_K: now SM-consistent, with no precise anomaly value.
- PMNS angles: global fits differ, and I did not verify a citation in time.

## (3) Match criterion and trial count

**Operations:** f(x) ∈ {x, 1/x, 2x, 3x, x/2, x/3}, i.e. 6 operations.

**Match:** |f(x) − y| ≤ max(σ_y, 10⁻³|y|). This is the permissive OR of "within 1σ" and "within relative 10⁻³".

**Trials:** N = 2032 × 6 × 16 = 195 072.

**Statistic:** M = the number of (quantity value, operation, target) matches.

**Nulls**, each with 10⁴ trials of the same size and the same structure:
- (N1) Each quantity family is replaced by the same number of values drawn log-uniformly over the family's observed [min, max].
- (N2) Q1/Q2/Q5 are rebuilt from 496 random fundamental units of random squarefree d in the same n-range: Q1 = 2·regulator, Q2 = regulator/(2√d), Q5 = √d. Q3 and Q4 are kept.
- (N3) Q5 is replaced by √m for random integers m in the n_s range, and Q1/Q2 by log-uniform values.

**Reported:** the global p-value P(M_null ≥ M_obs), the per-target p-value, and the expected count E[M_null].

**Labelling rule:** any individual match that occurs at a similar rate under the null is labelled chance.
