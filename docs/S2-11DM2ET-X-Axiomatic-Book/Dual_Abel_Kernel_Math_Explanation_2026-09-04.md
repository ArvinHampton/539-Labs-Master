Dual_Abel kernel math
Explanation from locked notes
2026-09-04 late

Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.
This is an explanation. It does not invent raw h. It does not identify Dual_Abel with Per_off.
Twin Prime and Riemann Hypothesis unclaimed.


0. What Dual_Abel is

Dual_Abel is the 29 August independent period table.
Signed Dual channels of Xi, of C_axis, and of Theta_third.
Abel-regularised weight-1/2 Eichler kernel.
Evaluated at x in {1/7, 3/7, 5/7, 1}, their Fricke images under W_7(x) = -1/(7x), and the positive 1/14 grid.

The populated sibling of those Xi channels was later named Dual_Abel_off.
Naming Dual_Abel_off does not populate Per_off.


1. Dual split

Any dual lattice sum is split by the sign of the Fourier index N:

Dual = Dual^{(-1)} + Dual^{(0)} + Dual^{(+1)}

Dual^{(-1)} uses modes with N < 0.
Dual^{(0)} is the N = 0 term.
Dual^{(+1)} uses modes with N > 0.

Three series are split that way: Xi, C_axis, Theta_third.
Nine channels at each real x.


2. The kernel

The weight-1/2 Eichler kernel on a mode of degree N is

K_Abel(N, ε) = N^{-1/2} exp(-2 π N ε)

with numerical regulator ε = 10^{-4}.

The exponential is the Abel regulator. It makes the real-line sum converge.
The power N^{-1/2} is the weight-1/2 Eichler factor written for these series.

The phase is signed.

Dual^{(+1)} multiplies by exp(+2 π i N x)
Dual^{(-1)} multiplies by exp(-2 π i N x)

So a plus-channel term looks like

c_N N^{-1/2} exp(-2 π N ε) exp(+2 π i N x)

and a minus-channel term looks like

c_N N^{-1/2} exp(-2 π N ε) exp(-2 π i N x)

The Abel factor is real. That is why |Dual^{(+1)}| and |Dual^{(-1)}| agree at each sample while the signed phases do not.


3. What this kernel is not

Not the branched Fricke path integral
h(x) = ψ/√i − ∫ Ξ(w) (w − x)^{-1/2} dw
along the locked path from i∞.
The 29 August note says so. The table is Abel-Fourier, not that path integral.

Not the incomplete-gamma / error-function kernel that Per_off asks for.
Convention A uses q = exp(2 π i τ) and erfc(|n+a| √(2π y)).
Convention B uses q = exp(π i τ) and erfc(|n+a| √(π y)).
Those are two writings of a tail in the upper half-plane.
Dual_Abel is a damped Fourier sum on the real line.

Not Dual±, the eight-by-eight cocycle matrix whose smallest singular value is 6.38.
Not Dual_Track.
Not residual_slash.
Not XferPot.


4. Why Per_off is still a header

Per_off wants
Xi only,
incomplete-gamma / error-function kernel,
a grid off F8 = {1/7, 3/7, 5/7, 1} union W_7 of that set,
values not defined by residual_slash.

Dual_Abel uses
Xi plus C_axis plus Theta_third,
Abel N^{-1/2} exp(-2 π N ε),
the four samples and the 1/14 grid.

Two writings of a leading kernel on Xi modes are not one table.
Matching them off-sample is OP-Xi-grid, still open.
That match would identify a generator with itself. It would not occupy Object B.


5. What the table already showed

Single channels do not realise Object A.
Three plus-channels cannot. Smallest singular value 19.70.
Six oscillatory channels have a four-dimensional nullspace that forces Object A at the four samples to order 10^{-13}.
Off those samples the implied slash of every null vector disagrees with residual_slash.
Median ratio about 0.14 to 0.29. Minimum about 0.0045.

The identity implied_slash(x) implied_slash(W_7(x)) = 1 holds by construction of the ratio.
That is not Object B for residual_slash.
Object B remains the failed product residual_slash(x) residual_slash(W_7(x)) = 1.


6. Status

Explanation only.
Raw numerical h as a stored function file was not found tonight.
The evaluated channel table exists in Independent_H_Table_Dual_Split_Pslash_2026-08-29.md.
CORE_FREEZE unchanged.
No new residual-flux object.


7. Status codes

DUAL_ABEL_KERNEL_MATH_EXPLANATION_2026-09-04
ABEL_NOT_INCOMPLETE_GAMMA
ABEL_NOT_BRANCHED_PATH_INTEGRAL
PER_OFF_STILL_HEADER
CORE_FREEZE_UNCHANGED
