# Full G4 CMB / BAO record — all closures

2026-09-20  Category B

Pack+(S). Residual-flux provenance mandatory. CORE_FREEZE holds.
G4=539.9 s immutable. D=11. 3^3=27. N_flux=4880.
kappa_dark=243/539. f_snap=243/4880. mu=1.55. S=0.31.
Planck theta_* is not an input. Dip language is retired.
N_star=14 is not used in any CMB fraction.


0. Oscillator

    Phi(t) = Phi_0 + A cos(2 pi t / G4) + B sin(2 pi t / G4)

TT = compression. EE = velocity. Unit harmonic = TT peak 2 = G4.


1. TT positions

    ell_1 = G4 * 11/27 = 219.959     -0.29%
    ell_2 = G4           = 539.9       +0.33%
    ell_3 = G4 * 3/2     = 809.85      +0.006%
    ell_4 = G4 * 17/8    = 1147.287    -0.04%
    ell_5 = G4 * 8/3     = 1439.73     -0.49%   (diffusion scale = ell_D)
    ell_6 = G4 * (27-4)/7 = 1773.96    -0.28%
    ell_7 = G4 * 27/7    = 2082.47     +0.36%
    ell_T2= G4 * 5/4     = 674.875     -0.09%
    ell_T5= 3 G4         = 1619.70     -0.25%
    ell_T6= G4 * 32/9    = 1919.64     +0.03%

7-grid rule after peak 5:
    ell_n = G4 (27 - 4*(7-n)) / 7     n=6,7
4 is the TE residue from ell_TE,1 = G4*4/7.


2. EE positions and ratios

    ell_EE,1 = G4 * 3/11
    ell_EE,n = G4 * (6n-4)/11          n>=2
    EE2/EE1 = G4/27     +3.5%
    EE3/EE2 = 11/6      +3.2%

Absolute EE muK: EE3=27+11=38 vs 38.1 is tempting and conflicts with the ratio chain from EE1=D/10. Not closed.


3. Silk

    ell_D = G4*8/3 = 1439.73
    ell_t = G4*11/5 = 1187.78
    ell_S = 916.3


4. Heights

    P1/P2 = 539/243                                    -0.05%
    P3/P1 = (1-kappa_dark) exp(-(ell_3^2-ell_1^2)/(3 G4)^2)  -0.8%
    P4/P2 = kappa_dark (1+f_snap)                      -0.25%
    P5/P3 = (1-kappa_dark) exp(-(ell_5^2-ell_3^2)/(3 G4)^2)  +0.84%
    P6/P4 = S                                          +0.6%
    P7/P5 = S (1-1/D)                                  -0.8%


5. BAO length

    D_M(z_*) = 3(N_flux-3^5) Mpc = 13911 Mpc
    ell_A = G4(mu-1) = 296.945
    r_d = pi*13911/296.945 = 147.15 Mpc


6. Warp

    Omega_m = (2/3) kappa_dark = 162/539
    Omega_DE = 377/539
    w = -1 + f_snap = -0.9502

    chi(z_*) at this w gives H0 = 68.15 km s^{-1} Mpc^{-1}
    h r_d = 100.30 Mpc     DESI 101.54 ± 0.73     -1.2%

Trials of w(z) = -1 + A exp(-z/z_c) and sech with A in {f_snap, 3 f_snap, 1/11, kappa f_snap} and z_c in {mu-1, S} all raised D_M residuals. They are rejected.

LRG1 D_H(z=0.51) remains +2.5% at w=-1+f_snap. DESI papers already flag LRG1. Not absorbed as a new model parameter.

What is still open as a derivation, not a fit:
    W(z) from explicit D2 brane separation as a function of a(t).
    That is the only remaining warp hole.


7. Scoreboard

CLOSED: TT 1-7 and T2,T5,T6; EE grid; Silk; heights P1..P7 pairs above; r_d; Omega_m; w=-1+f_snap; H0 from D_M(z_*).

OPEN: absolute EE muK; W(z) from brane separation; LRG1 as data residual.
