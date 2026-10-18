# U1 LEDGER — H_s in closed form: q-series, Zwegers parameters, radial coefficients t^{−1/2} … t^{5/2} (2026-10-18)

Packages: `H_s_Closed_Forms_2026-10-18/`, `H_s_Closure_2026-10-18/`. Consolidated: rev. 4 Theorem 12.1.
Text outputs (json/log/txt) of each package are stored verbatim in its `OUTPUTS_BUNDLE_2026-10-18.txt` (member byte counts and sha256 included); reports and scripts are separate files.
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact (incl. exact finite computation); floating-only = Cat B. See ERRATUM_Consolidated_CrossReview_2026-10-18.md. "Modulo F1" = given the cited two-dimensional Euler–Maclaurin expansion for cone sums.

Setup: M = A_s = [[2,s],[s,s]], c₁ = (−1,1), c₂ = (−4,1), g = gcd(24, s−8), Δ = (s−2)(7s−32).

## Category A
- A1. Q(c₁) = −(s−2)/2, Q(c₂) = −(7s−32)/2, B(c₁,c₂) = −4(s−2); admissible exactly for s ≥ 5; 4Q(c₁)Q(c₂) = Δ. H_s = ½q^{c₀}ϑ_hol + Δ_lines(s); explicit cone double-sum q-series for all s ≥ 5 (checked to q⁴⁰⁰ at 27 values of s); H₅ ≡ 0.
- A2. (mod F1) H_s at x = 0 has **no integer-order terms**.
- A3. (mod F1) H_r = √(2πs)[R_r(s) + S_r(s,g)√Δ] for r = −1/2, 1/2, 3/2, 5/2; e.g. R_{−1/2} = −1/(2(s−2)), S_{−1/2} = 1/(2(s−2)(7s−32)), R_{1/2} = −(s−4)(3s−2)/(48(s−2)²), S_{1/2} = (s³−44s²+192s+2g²(s−2))/(48(s−2)²(7s−32)²); t^{3/2}, t^{5/2} in `H_s_Closure_2026-10-18/H_closed2.txt` and rev. 4 Thm 12.1. Exact Bernoulli-sum validation for s = 5..80, 99, 100, 151, 223, 300.
- A4. (mod F1) **H_{−1}(x) = 0 for every rational x.**
- A5. s = 8 (Δ = 144): H_{−1/2} = −√π/6, H_{1/2} = 5√π/54, H_{3/2} = −175√π/324, H_{5/2} = 995√π/972, C_{−1/2}(8) = 11√π/24 — the √π-rational scale. Δ is a square for s < 10⁶ only at s = 5, 8, 26, 77, 365, 1178, 5768, 18725, 91877, 298376 (exact search).
- A6. s = 7: a_H = H_{−1/2}(7), a_C = C_{−1/2}(7) = 0.829142617… symbolically (replaces rev. 3 PSLQ/30-digit statements, C9).

## Category B
- Small-t fits for H_{3/2} (9 values of s, 3–4 digits) and H_{5/2} (s = 6, 8 only).
- x ≠ 0 fits (stable cases not closed); unstable fits at x = 1/2 (s = 7, 9, 10), x = 1/3 (s = 7, 10) are not quoted.
- Modular completion by citation (Zwegers Cor. 2.9). Pre-registered prediction PB5 (rational t¹ term) refuted: the term is 0.
- Report-internal labels B1–B8 are not reused on Master.

## Files not included
`*.pkl` (H_closed2.pkl, H_generic2.pkl and others; regenerable), `__pycache__/`.
