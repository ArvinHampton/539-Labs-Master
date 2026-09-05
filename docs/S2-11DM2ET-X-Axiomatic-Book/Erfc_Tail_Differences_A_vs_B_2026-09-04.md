Erfc tail differences, Convention A versus B
2026-09-04 written, 2026-09-05 pushed

PURE MATH. Category A residual discrete probe of two written conventions. Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds. These numbers are costume checks. They are not stored Per_off h(x). They do not select A or B.

1. Why the arguments differ

Convention A uses q = exp(2 pi i tau) = exp(2 pi i x) exp(-2 pi y). Squares carry exp(-2 pi n^2 y). After the completed square the tail is erfc(|n+a| sqrt(2 pi y)).

Convention B uses q = exp(pi i tau) = exp(pi i x) exp(-pi y). Squares carry exp(-pi n^2 y). The tail is erfc(|n+a| sqrt(pi y)).

Set z = |n+a| sqrt(pi y). Then

tail_A = erfc(sqrt(2) z)
tail_B = erfc(z)
R = erfc(sqrt(2) z) / erfc(z)

erfc is decreasing, so R is less than 1 at every finite y greater than 0. A always damps harder.

2. How the ratio moves

As y goes to 0, both tails go to 1 and R goes to 1. At y = 10^{-4} and shift 4.5, R = 0.959.

As y goes to infinity, both tails go to 0. A dies first, so R goes to 0. That holomorphic limit is Theta_third itself, not the completion. Agreement there is agreement of two zeros.

3. Written probe

Shift 4.5, y = 0.01:
z_B = 0.7976, z_A = 1.128
tail_A = 0.1107, tail_B = 0.2593
R = 0.426741
3/7 = 0.428571. Miss 0.00183. Already refused as a law. y = 0.01 is a round probe, not Pack+(S).

4. Listed Per_off ridge at the same y = 0.01, shift = c_n = n + 7/2

n=0 shift 3.5  R=0.565
n=1 shift 4.5  R=0.427
n=2 shift 5.5  R=0.305
n=3 shift 6.5  R=0.205
n=4 shift 7.5  R=0.131
n=5 shift 8.5  R=0.078
n=6 shift 9.5  R=0.044

On the stored rows the two tails already disagree by factors from about 2 to about 23 at one convenient height. That is why an unselected convention means numerical h is not unique.

5. What this is not

Not Dual_Abel. Dual_Abel damps by exp(-2 pi N epsilon) on real-line Fourier modes. A third kernel.
Not a Pack+(S) selector. Per_off Kernel_n stays a class name. Numerical h stays unstored. Slash_two stays empty.

Status code: ERFC_TAIL_DIFFERENCES_A_VS_B_PROBE_NOT_H_2026-09-04
