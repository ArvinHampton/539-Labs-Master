# ADDENDUM B (pp20–22 beta table) to PP PDF review 17ab357b — bounded arithmetic only (30-digit mpmath of the explicit formula; no PDF scripts run)
beta(k)=(1+k)^(-7/20). Delta = beta(k) - beta(1.595361). Values to 15 sig. digits, rounded.
| k | actual beta | claimed | actual Delta | claimed Delta |
|---|---|---|---|---|
| 1.595350 | 0.716195228418642 | .7161952 OK | +1.06242e-6 | +1.03e-6 (≈3% off) |
| 1.595360 | 0.716194262584832 | .7161943 OK | +9.65831e-8 | +1.34e-7 WRONG |
| 1.595361 | 0.716194166001727 | .716194166 OK | 0 | 0 |
| 1.595370 | 0.716193296756045 | .7161933 OK | -8.69246e-7 | -8.66e-7 (≈0.4% off) |
| 1.595390 | 0.716191365113543 | .7161914 OK | -2.80089e-6 | -2.77e-6 (≈1% off) |
| 1.595430 | 0.716187501888824 | .7161875 OK | -6.66411e-6 | -6.67e-6 OK (rounded) |
beta'(k) = -(7/20)(1+k)^(-27/20); at 1.595361 = -0.0965830796180587. Nonzero for all k>-1: beta strictly decreasing, smooth, no zero, no critical point, nothing special at 1.595361 — Delta=0 there only because it is the chosen reference. Deltas ≈ beta'·(k−1.595361) (linear to ~1e-12).
Status: beta values CORRECT; Delta column has arithmetic errors (row 2 materially). Table is a finite 6-point profile; a "high-resolution loop" is a CLAIM with no logs (UNVERIFIED, not refuted). No explicit identity in pp20–22 links beta or 1.595361 to N−|W|=0, penalty cancellation, a Bridge C exponent, or hardware: GAP (non sequitur as stated). No CERT.
