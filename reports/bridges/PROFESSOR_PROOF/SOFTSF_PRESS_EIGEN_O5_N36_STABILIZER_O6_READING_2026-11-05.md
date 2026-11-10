# SOFTSF_PRESS — Eigen O5 N36 stabilizer / O6 reading — 2026-11-05
FINDINGS: FINDINGS_EIGEN_SOFTSF_O5_N36_STABILIZER_O6_READING_2026-11-05.md. Auth 06748ff2… MATCH. tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 NO touch. No CERT. Nothing sent.
- (a) RESOLVED: Kr mod 7840981 is invariant for k=2,3,48. Since 3 generates (ℤ/49)ˣ, the stabilizer is the full group, so the field is ℚ.
- (b) RESOLVED: Kr does not depend on the root choice, so the least-root rule is consistent and is not the cause of the CRT failure.
- (c) REMAINING: ℚ common-denominator LLL holdout fails on all 5 rows tested. Heights exceed ~10^76, so more primes are needed (count unknown).
- (d) REMAINING: gated on (c).
- O6 RESOLVED: chosen reading target=[1] (not in source) gives W=0, N=2.
