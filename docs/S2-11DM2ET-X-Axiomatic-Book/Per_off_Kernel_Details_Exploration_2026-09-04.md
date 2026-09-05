Per_off kernel details
2026-09-04 written, 2026-09-05 pushed

PURE MATH. Category A residual discrete. Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds. Twin Prime and RH unclaimed.

Parent: U1_GS_NEWOBJ_PEROFF_Residual_Off_Sample_Term_Table_2026-09-02.md and Per_off_Xi_Term_Table_Listed_Ridge_2026-09-02.md.

1. One object, two names

Def_Xi_odd is the series. Per_off(Xi) is that series written as a term table plus F8-exclusion.

Def_Xi_odd := sum_{n >= 0} Kernel_n

Series is Xi-odd ridge only. Not C_axis. Not Theta_third holomorphic. Not Dual_Abel nine-channel mix.

2. Ridge

N_n = n^2 + 7 n + 24.5
c_n = n + 7/2 = sqrt(N_n - 12.25)

Listed support n = 0 through 6: degrees 24.5, 32.5, 42.5, 54.5, 68.5, 84.5, 102.5.
Rows n >= 7 are formula-not-listed. Not a new theorem.
Integer Xi support {43, 58, 67, 78, 91, 106} is excluded from Def_Xi_odd. I4 stays a definitional rewrite.

3. The kernel

Written high-period, no extra prefactor:

h_residual^{high}(x) = psi(x)/sqrt(i) - integral_{i infinity to x} Xi_N(w) (w-x)^{-1/2} dw

Term-by-term, each Fourier mode c_N becomes a weight-1/2 incomplete-gamma / error-function term of the same degree N. That assignment is Kernel_n. Kernel_n is a class name, not a stored number h(x).

Dual-split Abel N^{-1/2} of the same {c_N} is a second writing of this leading kernel. Matching those two writings identifies G3 with itself. It does not put G3 in span{Period(C_axis), Period(Theta_third holomorphic)}.

4. Two conventions, not one function

Convention A: q = exp(2 pi i tau), erfc(|n+a| sqrt(2 pi y))
Convention B: q = exp(pi i tau), erfc(|n+a| sqrt(pi y))

They agree only as y goes to infinity, the holomorphic limit, where the tail is zero. Pack+(S) has not selected A or B. Until that selection, a numerical period is not unique. That is why the off-sample number table stays a header even though the term table is populated.

5. Forbidden grid

S4 = {1/7, 3/7, 5/7, 1}
W_7(x) = -1/(7x)
F8 = S4 union W_7(S4) = {1/7, 3/7, 5/7, 1, -1, -1/3, -1/5, -1/7}

Any later numerical probe must sit off F8. Declaring a point off F8 does not evaluate h. The populated object does not evaluate h at F8 and does not evaluate h anywhere else.

6. Empty intersections

I1 ridge against C_axis empty.
I2 ridge against holomorphic Theta_third empty.
I3 listed integer Xi against C_axis empty.
I4 degrees {43, 58, 67, 78, 106} excluded from Def_Xi_odd.

7. Status split

2 September retired PER_OFF_XI_HEADER_ONLY for the ridge rows. Status is PER_OFF_XI_POPULATED_TERM_TABLE.
Numerical h(x) off F8 is still unstored. Later speech of Per_off header means that probe, not the listed degrees.

Half-integer incomplete-gamma modes have no counterpart in the integer holomorphic supports. Writing the table does not force

h = A Period(C_axis) + B Period(Theta_third holomorphic).

That is the P-Xi obstruction, restated as a property of this object.

Not Dual_Abel_off. Not eichler_proxy. Not Dual-plus-minus. Not Dual_Track. Not residual_slash. Not Object B. Not Remark 8.5. Not OccFilt_7. Not a clock. Not COUNT 539. Not 247.

Status code: PER_OFF_KERNEL_DETAILS_TERM_TABLE_NOT_NUMERICAL_H_2026-09-04
