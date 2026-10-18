# U1 LEDGER — ζ_E(0;s) and ζ_E(−1;s) lie on one rational curve in s (all integers s ≥ 3) — 2026-10-18

Package: `Zeta_Rational_Curve_2026-10-18/` (report and `prove_zeta.py` are Master copies with cross-references to unpublished local folders removed; mathematics unchanged; other files verbatim).
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim.

## Theorem (Category A for s ≥ 3)
For every integer s ≥ 3, with Q_s(n,k) = n² + snk + (s/2)k(k+1), E_s = Σ_{n≥0,k≥1} q^{Q_s} + Σ_{n≤−1,k≤0} q^{Q_s}, c₀ = s/(4(s−2)), ζ_E(w;s) = Σ e_m (m − c₀)^{−w}:
- (a) ζ_E(0;s) = (s−4)(s−5) / (12(s−2))
- (b) ζ_E(−1;s) = (2s⁵ − 14s⁴ − 45s³ + 425s² − 632s − 96) / (1440(s−2)²)
- (c) the t^{−1} coefficient of E_s(e^{−t})e^{c₀t} is arccosh(s−1)/√(s(s−2)); the t^{−1/2} and t^{1/2} coefficients vanish.
Samples: s = 7: 1/10, 29/1200; s = 8: 1/6, 5/36; s = 11: 7/18, 1129/1296.

## Status
- Cat A: every algebraic step, symbolic in s (`prove_zeta.py` → `prove_zeta.txt`, all PASS): cone form S² + 2(s−1)ST + T²; Lemma E (E_s = one half-open cone sum, via (n,k) ↦ (n,−2n−k−1)); exactly two lattice classes (½+δ, 1−δ), (δ, ½−δ), δ = 1/(2(s−2)); Euler–Maclaurin coefficient algebra.
- Analytic inputs cited, standard (not re-proved): F1 2-D Euler–Maclaurin; F2 Mellin dictionary (Zagier 2006; Shintani 1976).
- Cross-checks: 42 exact (s, cone) values for s = 3..20, 25, 30, 41 (0 mismatches); numerical asymptotics at s = 3, 5, 13, 30.

## Caveats
- Valid for integers s ≥ 3 only. Only s = 7, 8, 11 are framework scales; other s belong to the formal family.
- The s = 5..41 cone-value files used in the cross-check are held in a separate local folder and are not included; the included `shintani_s3_s4.txt` covers s = 3, 4.

## Normalisation note
ζ(−1,𝒦) = 29/60 (ray-class, N𝔞 = 20Q) and ζ_E(−1;7) = 29/1200 differ only by the factor 20 = c^{−w} at w = −1. Likewise 5/12 = 3 · 5/36 (s = 8) and 1129/36 = 36 · 1129/1296 (s = 11).
