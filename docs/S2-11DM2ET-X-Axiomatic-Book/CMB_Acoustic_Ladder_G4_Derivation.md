# CMB acoustic ladder from G4 — corrected record

S2-11DM2ET-X  Category B  2026-09-20

Pack+(S). Residual-flux provenance mandatory. CORE_FREEZE holds.
Twin Prime and RH unclaimed. Continuum G4 mappings stay Category B.
Planck theta_* is not an input. Dip language is retired.

G4 = 539.9 s. D = 11. Cubic +U = 27. N_flux = 4880.
kappa_dark = 243/539. f_snap = 243/4880. mu = 1.55.

Full writeup with EE, Silk, BAO, heights:
CMB_Ladder_Full_Derivation_EE_Silk_BAO_Heights_2026-09-20.md


## TT (closed)

ell_1 = G4 * 11/27 = 219.959     Planck 220.6 ± 0.6    -0.29%
ell_2 = G4         = 539.9       Planck 538.1 ± 1.3    +0.33%
ell_3 = G4 * 3/2   = 809.85      Planck 809.8 ± 1.0    +0.006%
ell_4 = G4 * 17/8  = 1147.287    Planck 1147.8 ± 2.3    -0.04%
ell_T2= G4 * 5/4   = 674.875     Planck 675.5 ± 1.2    -0.09%


## EE (closed)

ell_EE,1 = G4 * 3/11
ell_EE,n = G4 * (6n-4)/11   (n>=2)


## Silk (closed)

ell_D = G4 * 8/3 = 1439.73
ell_t = G4 * 11/5 = 1187.78
ell_S = 916.3


## Heights (closed)

P1/P2 = 539/243
P3/P1 = (1-kappa_dark) exp(-(ell_3^2-ell_1^2)/(3 G4)^2)


## BAO (closed calibration + length)

D_M(z_*) = 3(N_flux - 3^5) Mpc = 13911 Mpc
r_d = pi D_M / [G4(mu-1)] = 147.15 Mpc
