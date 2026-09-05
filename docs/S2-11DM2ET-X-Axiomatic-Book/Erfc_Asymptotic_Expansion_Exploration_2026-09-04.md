Asymptotic expansion of erfc applied to Convention A versus B
2026-09-04 written, 2026-09-05 pushed

PURE MATH. Category A residual discrete probe. Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds. Does not select A or B. Does not store Per_off h(x).

1. Classical expansion

For large positive z,

erfc(z) ~ exp(-z^2) / (z sqrt(pi)) * (1 - 1/(2 z^2) + 3/(4 z^4) - 15/(8 z^6) + ...)

The series is divergent. Use it only while the terms decrease.

2. Applied to the two tails

With z = |n+a| sqrt(pi y),

R = erfc(sqrt(2) z) / erfc(z).

The leading terms give

R ~ exp(-z^2) / sqrt(2).

The extra exp(-z^2) is the extra Gaussian from Convention A. The extra 1/sqrt(2) is the prefactor from 1/(sqrt(2) z) over 1/z. That is why A dies first as y grows.

3. Where the expansion is valid

Written probe y = 0.01, shift 4.5, z = 0.7976.
Exact R = 0.426741
Leading R = 0.374282
Miss 12 percent.
Here 1/(2 z^2) = 0.786. That is not a small parameter. Adding the next term makes the ratio worse. The six-term series blows up.

At y = 0.1, shift 4.5, z = 2.52.
Exact R = 0.001259
Leading R = 0.001221
Miss 3 percent.
That is the usable window. It is also the window where both tails are already tiny.

On the listed Per_off ridge at y = 0.01, z runs from 0.62 to 1.68. None of those rows is in the safe window. The slogan R ~ exp(-z^2)/sqrt(2) does not evaluate Kernel_n there.

4. What this does not do

It does not select A or B.
It does not turn 0.426741 into 3/7. The 3/7 near-miss sits next to the exact mid-range ratio, not next to the asymptotic.
It does not store numerical h.
It does not replace Dual_Abel.

Holomorphic limit restated: both tails vanish faster than any power of 1/z. Agreement of two zeros is not a completed period.

Status code: ERFC_ASYMPTOTIC_NOT_VALID_AT_WRITTEN_PROBE_2026-09-04
