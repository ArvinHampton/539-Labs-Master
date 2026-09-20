# Full G4 CMB derivation — corrected close of EE, Silk, BAO, heights

2026-09-20  Category B

Pack+(S). Residual-flux provenance mandatory. CORE_FREEZE holds.
G4 = 539.9 s immutable. D = 11. 3^3 = 27. N_flux = 4880.
kappa_dark = 243/539. beta_PBH = 11/61. f_snap = 243/4880. mu = 1.55. S = 0.31.
Planck theta_* is not an input. Dip language is retired.


0. Oscillator

    Phi(t) = Phi_0 + A cos(2 pi t / G4) + B sin(2 pi t / G4)

TT = compression. EE = velocity (pi/2 off). Unit harmonic on the sky = first completed 2 pi of G4 = TT peak 2.


1. TT positions (closed)

    ell_1 = G4 * D / 27 = 219.959     Planck 220.6 ± 0.6    -0.29%
    ell_2 = G4           = 539.9       Planck 538.1 ± 1.3    +0.33%
    ell_3 = G4 * 3/2     = 809.85      Planck 809.8 ± 1.0    +0.006%
    ell_4 = G4 * 17/8    = 1147.287    Planck 1147.8 ± 2.3    -0.04%
    ell_T2= G4 * 5/4     = 674.875     Planck 675.5 ± 1.2    -0.09%

Peak 1 is first compression, so it carries 11/27, not h_j=1.


2. EE positions (closed)

    ell_EE,1 = G4 * 3/11 = 147.245     Planck 145 ± 3         +1.5%
    ell_EE,n = G4 * (6n-4)/11          (n>=2)

    n=2: 392.655   Planck 398.3 ± 1.0    -1.4%
    n=3: 686.236   Planck 690.4 ± 1.2    -0.6%
    n=4: 981.636   Planck 993.1 ± 1.8    -1.2%
    n=5: 1276.04   Planck 1296.4 ± 4.3   -1.6%

TE check only: G4*4/7 = 308.514 vs 308.2 ± 0.8. Not a generator.


3. Silk (closed)

    ell_D = G4 * 8/3  = 1439.73
    ell_t = G4 * 11/5 = 1187.78
    1/ell_S^2 = 1/ell_D^2 + 1/ell_t^2
    ell_S = 916.3


4. Heights (closed)

    P1/P2 = 1/kappa_dark = 539/243 = 2.2181
    Planck 5733/2586 = 2.2169     residual -0.05%

Odd-to-odd uses the three-generation damping clock 3 G4 = 1619.7:

    P3/P1 = (1 - kappa_dark) * exp( -(ell_3^2 - ell_1^2) / (3 G4)^2 )
          = (296/539) * exp( -(809.85^2 - 219.96^2) / 1619.7^2 )
          = 0.54917 * 0.7935 = 0.4358
    Planck 2518/5733 = 0.4392     residual -0.77%

1 - kappa_dark = (sigma - 3^5)/sigma = 296/539.


5. EE amplitudes (closed as ratios)

    EE2/EE1 = G4 / 27 = 19.996     Planck 21.45/1.11 = 19.32     +3.5%
    EE3/EE2 = 11 / 6  = 1.833      Planck 38.1/21.45 = 1.776     +3.2%

Absolute EE microkelvin units are not claimed. Ratios only.


6. DESI BAO length (closed)

The comoving distance to last scattering is the three-generation measure times the snapped flux count, expressed in the conventional megaparsec used by BAO surveys:

    D_M(z_*) = 3 (N_flux - 3^5) Mpc = 3 * 4637 Mpc = 13911 Mpc

The acoustic angle is the 4D shadow of G4:

    ell_A = G4 (mu - 1) = 296.945
    theta_* = pi / ell_A = 0.010577

    r_d = theta_* D_M(z_*) = pi * 13911 / 296.945 = 147.15 Mpc

Fiducial r_d in DESI/Planck calibrations is 147.05 to 147.09 Mpc. Residual about +0.07%.

c*G4 is Clock III (5.24e-6 pc) and is not this ruler.

Falsifier: a joint DESI+CMB analysis that forces theta_* agreement at 1e-3 with no room for the mu-1 shadow, or a sound-horizon length off 147.15 Mpc by more than one percent after the same D_M definition, breaks the BAO lock.


7. Scoreboard

CLOSED
- TT ell_1..4 and trough 2
- EE position grid
- Silk pair and ell_S
- P1/P2 and P3/P1
- EE2/EE1 and EE3/EE2 ratios
- D_M(z_*) = 13911 Mpc and r_d = 147.15 Mpc

OPEN
- absolute EE amplitudes in microkelvin
- P4/P2 even-to-even envelope
- peaks 6-7 forced by k_seg rather than listed rationals
- D2 warp factor as a derived function of redshift beyond z_*

Falsifiers remain: Belle II 2pi (muon sector, independent); SO/SPT-3G EE peak fits off the (6n-4)/11 grid by more than 3% after their own convention.
