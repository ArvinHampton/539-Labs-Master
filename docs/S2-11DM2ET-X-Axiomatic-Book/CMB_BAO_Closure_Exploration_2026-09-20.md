# Closure exploration after the G4 ladder
2026-09-20  Category B

Pack+(S). Residual-flux provenance mandatory. CORE_FREEZE holds.
No new generators. 23 as 27-4 is flagged as candidate, not closed.
N_star=14 is not used in any CMB fraction.


1. Closed this pass

P4/P2 (even-to-even)
    kappa_dark (1 + f_snap) = 243/539 * 5123/4880 = 0.47328
    Planck 1227/2586 = 0.47448     residual -0.25%

P5/P3 (odd-to-odd, same envelope as P3/P1)
    ell_5 = G4 * 8/3 = 1439.73
    P5/P3 = (1-kappa_dark) exp(-(ell_5^2-ell_3^2)/(3 G4)^2) = 0.3200
    Planck 799/2518 = 0.3173       residual +0.84%

ell_5 = G4 * 8/3 = 1439.73         Planck 1446.8 ± 1.6    -0.49%
    Same rational as ell_D. Peak 5 sits at the diffusion scale.

ell_T5 = 3 G4 = 1619.70            Planck 1623.8 ± 2.1    -0.25%
    Already the odd-peak damping clock.

ell_T6 = G4 * 32/9 = 1919.64       Planck 1919 ± 4        +0.03%
    32 = 2^5, 9 = 3^2. Binary snap tower times the square of 3.

Background warp (leading order, w=-1)
    Omega_m = (2/3) kappa_dark = 162/539 = 0.30056
    Omega_DE = 377/539 = 0.69944
    D_M(z_*) = 13911 Mpc locked previously
    chi(z_*) = integral_0^{1089} dz/E(z) = 3.1762
    H0 = c * chi(z_*) / D_M(z_*) = 68.45 km s^{-1} Mpc^{-1}
    r_d = 147.15 Mpc
    h r_d = 100.74 Mpc             DESI BAO-alone 101.54 ± 0.73   -0.79%

2/3 is the two-of-three +U spatial directions that carry matter density after leakage into the third (line of sight / expansion) direction.


2. DESI distances at this background (not a new fit)

z      D_M/r_d model  DESI     pct     D_H/r_d model  DESI     pct
0.510  13.347         13.588   -1.78   22.595         21.863   +3.35
0.706  17.526         17.351   +1.01   20.098         19.455   +3.31
0.934  21.811         21.576   +1.09   17.552         17.641   -0.51
1.321  27.901         27.601   +1.09   14.091         14.176   -0.60
1.484  30.100         30.512   -1.35   12.915         12.817   +0.76
2.330  39.043         38.988   +0.14    8.660          8.632   +0.32

D_M at z>=0.7 is at ~1%. D_H at z=0.51 and 0.71 is the known LRG1 tension. That residual is the remaining D2 warp degree of freedom. It is not closed by setting w=-1.


3. Candidates (not closed)

ell_6 = G4*(27-4)/7 = 1773.96      Planck 1779 ± 3        -0.28%
    Uses TE denominator 7 and residue 4 from ell_TE,1=G4*4/7.
    23=27-4 is a derived integer, not a new generator, but the construction is one step less direct than 8/3.

ell_7 = G4*27/7 = 2082.47          Planck 2075 ± 8        +0.36%
    Same 7-grid. Hold as candidate with ell_6.

ell_6 = G4*10/3 = 1799.67          +1.16%   weaker thirds continuation.

ell_T3 = G4*13/7 = 1002.67         +0.16%
    13 is not generated. Do not use N_star=14 to make 27-14=13.

ell_T4 = G4*12/5 = 1295.76         +0.45%
    5 is the Silk ell_t denominator. Candidate.

ell_T1 = G4*7/9 = 419.92           +0.87%   too loose.

EE1 = D/10 = 1.1 muK^2             Planck 1.11 ± 0.04
    10 is not generated. Unit insertion.
EE3 = 27+D = 38 muK^2              Planck 38.1 ± 0.6      -0.26%
    Cleaner absolute, but conflicts at the 3% level with the ratio chain from EE1.
    Keep ratios closed; leave absolute muK open.

w(z) leakage
    Leading order w=-1 (section 1).
    A correction of size f_snap or kappa_dark*f_snap (~0.02 to 0.05) would move LRG1 D_H.
    Not closed until written as a function of the D2 scale factor, not a CPL fit to DESI.


4. Scoreboard after this pass

CLOSED
- TT ell_1..5 and troughs 2,5,6
- EE position grid n=1..5
- Silk pair
- P1/P2, P3/P1, P4/P2, P5/P3
- EE2/EE1, EE3/EE2 ratios
- D_M(z_*), r_d, Omega_m=162/539, H0=68.45 (leading-order warp)

OPEN / CANDIDATE
- ell_6, ell_7 on the 7-grid
- absolute EE muK
- w(z) for LRG1 D_H
- D2 warp as an explicit function of brane separation vs z

Falsifiers unchanged: Belle II 2pi; SO/SPT-3G EE grid off by >3%; DESI+CMB forcing theta_* agreement at 1e-3 with no mu-1 shadow.
