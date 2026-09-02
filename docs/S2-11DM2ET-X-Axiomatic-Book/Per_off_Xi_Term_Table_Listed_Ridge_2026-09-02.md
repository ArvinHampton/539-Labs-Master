Per_off(Xi) companion term table
Listed Xi_odd ridge support under Pack+(S)
2026-09-02

PURE MATH. Category A residual discrete only. Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds. This file is the companion table for U1_GS_NEWOBJ_PEROFF_Residual_Off_Sample_Term_Table_2026-09-02.md. It does not add a second object.

Parent: 0fd9efb P-Xi header. Coefficient source: Residual_Coefficient_Tables_and_Fricke_Probe_C_2026-08-23.md. Kernel source: Construct_Higher_Fidelity_Residual_Eichler_Integral_C_2026-08-25.md. W_7(x) = -1/(7x).

Ridge generator.
N_n = n^2 + 7 n + 24.5
c_n = n + 7/2
Check: c_n = sqrt(N_n - 12.25)

Listed populated rows. These seven rows are the locked Fourier support of the odd m=0 ridge through degree 106.

n    N_n      c_n     listed_in_Xi_table    Kernel_n
0    24.5     3.5     yes                   weight-1/2 incomplete-gamma / error-function term of degree 24.5
1    32.5     4.5     yes                   weight-1/2 incomplete-gamma / error-function term of degree 32.5
2    42.5     5.5     yes                   weight-1/2 incomplete-gamma / error-function term of degree 42.5
3    54.5     6.5     yes                   weight-1/2 incomplete-gamma / error-function term of degree 54.5
4    68.5     7.5     yes                   weight-1/2 incomplete-gamma / error-function term of degree 68.5
5    84.5     8.5     yes                   weight-1/2 incomplete-gamma / error-function term of degree 84.5
6   102.5     9.5     yes                   weight-1/2 incomplete-gamma / error-function term of degree 102.5

Formula-not-listed continuation. Same N_ridge formula. Not in the listed Xi table through 106. Not a new theorem.

n    N_n      c_n     listed_in_Xi_table
7   122.5    10.5     no
8   144.5    11.5     no
9   168.5    12.5     no
10  194.5    13.5     no
11  222.5    14.5     no
12  252.5    15.5     no

Excluded from Def_Xi_odd. Integer Xi support and I4 overlap. Even-product rewrite recovering exterior Theta_third, plus even-family 91.

N      c      class
43     1      integer even-product, I4, Theta_third holomorphic
58     2      integer even-product, I4, Theta_third holomorphic
67     3      integer even-product, I4, Theta_third holomorphic
78     6      integer even-product, I4, Theta_third holomorphic
91     7      integer even-family, meets neither C_axis nor Theta_third
106    8      integer even-product, I4, Theta_third at (1,5)

F8 forbidden evaluation grid, written W_7(x) = -1/(7x).

S4        = {1/7, 3/7, 5/7, 1}
W_7(S4)   = {-1, -1/3, -1/5, -1/7}
F8        = {1/7, 3/7, 5/7, 1, -1, -1/3, -1/5, -1/7}

Empty intersections restated.
I1 = ridge intersect C_axis = empty
I2 = ridge intersect Theta_third holomorphic = empty
I3 = listed integer Xi intersect C_axis = empty

This companion does not evaluate h_residual^{high}(x). It does not claim Remark 8.5. It does not lift the P-Xi obstruction.

Status code: PER_OFF_XI_COMPANION_TERM_TABLE_2026-09-02
