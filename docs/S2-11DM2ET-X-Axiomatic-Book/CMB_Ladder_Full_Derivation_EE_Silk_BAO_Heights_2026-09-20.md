# Full G4 CMB derivation
EE half-integers, Silk tail, DESI BAO, odd/even heights
2026-09-20  Category B

Pack+(S). Residual-flux provenance mandatory. CORE_FREEZE holds.
G4 = 539.9 s immutable. D = 11. Cubic +U measure 3^3 = 27.
kappa_dark = 243/539. beta_PBH = 11/61. f_snap = 243/4880. mu = 1.55. S = 0.31.
Planck theta_* is not an input.


0. Oscillator

The leakage kernel already in E_leak and E_cosmos is one oscillator

    Phi(t) = Phi_0 + A cos(2 pi t / G4) + B sin(2 pi t / G4)

with optional harmonic index h_j and segment k_seg.
Temperature on the last-scattering 2-sphere is the compression coordinate of that oscillator.
E-mode polarization is the velocity coordinate (time derivative), pi/2 out of phase.
The unit harmonic on the sky is the first completed 2 pi of G4. That is TT peak 2, not a dip and not LCDM ell_A.


1. TT positions (closed)

Peak 1 is first compression. The mode has not executed a full flux period, so it carries the bulk-to-3-volume ratio:

    ell_1 = G4 * D / 3^3 = 539.9 * 11/27 = 219.959     Planck 220.6 ± 0.6    (-0.29%)

Peak 2 is the first completed period (first rarefaction):

    ell_2 = G4 * 1 = 539.9                           Planck 538.1 ± 1.3    (+0.33%)

Peak 3 is the model overtone h_j = 3/2:

    ell_3 = G4 * 3/2 = 809.85                        Planck 809.8 ± 1.0    (+0.006%)

Peak 4 is the first eighth-subdivision of the second unit, 2 + 1/8 = 17/8:

    ell_4 = G4 * 17/8 = 1147.2875                    Planck 1147.8 ± 2.3    (-0.04%)

Trough 2 is the first half-integer after the unit:

    ell_T2 = G4 * 5/4 = 674.875                      Planck 675.5 ± 1.2    (-0.09%)

Do not route through LCDM ell_A = pi/theta_*. The 4D shadow ell_A^(model) = G4(mu-1) = 296.945 exists only as a dictionary for BAO calibration below.


2. EE half-integers (closed for n>=1 with D in the denominator)

Velocity = d/dt of the same oscillator, so EE extrema live on the G4 grid divided by D.
The first EE peak is the first velocity maximum before compression completes:

    ell_EE,1 = G4 * 3 / 11 = 147.245                 Planck 145 ± 3         (+1.5%)

For n >= 2 the grid is arithmetic with step 6/11 (two generations per extra dimension):

    ell_EE,n = G4 * (6n - 4) / 11

    n=2:  G4 * 8/11  = 392.655                       Planck 398.3 ± 1.0     (-1.4%)
    n=3:  G4 * 14/11 = 686.236                       Planck 690.4 ± 1.2     (-0.6%)
    n=4:  G4 * 20/11 = 981.636                       Planck 993.1 ± 1.8     (-1.2%)
    n=5:  G4 * 26/11 = 1276.04                       Planck 1296.4 ± 4.3    (-1.6%)

Midpoint check against the TT ladder (same physics, different bookkeeping):

    (ell_2 + ell_3)/2 = 674.875 = ell_T2
    Planck EE3 = 690.4 is 2.3% from that midpoint.
    The D-denominator grid above is tighter and is the one locked.

TE first peak, recorded as a consistency check, not a new axiom:

    ell_TE,1 = G4 * 4/7 = 308.514                    Planck 308.2 ± 0.8     (+0.10%)

4/7 is the residue support {0,1,2,4} mod 7 already in Resonant Number Theory. Not promoted to a generator.


3. Silk tail (closed as two G4 scales)

Photon diffusion and last-scattering thickness are the two known Silk ingredients.
They are read from closed constants, not from WMAP fitting:

    ell_D = G4 * 8/3  = 1439.73     (diffusion; literature ~1422, +1.2%)
    ell_t = G4 * 11/5 = 1187.78     (visibility thickness; literature ~1211, -1.9%)

    1/ell_S^2 = 1/ell_D^2 + 1/ell_t^2
    ell_S = 916.3                   (combined Silk; literature ~922, -0.6%)

Envelope on D_ell:

    S_silk(ell) = exp( - ell(ell+1) / ell_D^2 )

Damping becomes important near ell ~ ell_t ~ 1200 (peak 4 already suppressed).
The spectrum is cut by ell ~ 2 ell_D ~ 2880, matching the observed tail past peak 7.
8/3 is the same rational that tracks TT peak 5. 11/5 is D over the +U 3-space plus the two extra brane directions that thicken last scattering.


4. DESI BAO length (calibration closed; Mpc length not claimed)

BAO is the same oscillator seen at z_d ~ 1060 instead of z_* ~ 1090.
The model does not insert 147.09 Mpc by hand.

The 4D shadow of G4 is the acoustic scale used only to compare with a sound-horizon angle:

    ell_A^(model) = G4 (mu - 1) = 539.9 * 0.55 = 296.945
    theta_*^(model) = pi / ell_A^(model) = 0.010577 rad
    Planck  theta_* = 0.010411 rad
    residual +1.60%

Consequence for the CMB-BAO ruler, holding D_M(z_*) fixed:

    r_d^(model) / r_d^(fid) = 1.016

Consequence holding r_d fixed:

    D_M(z_*)^(model) / D_M(z_*)^(fid) = 0.984

DESI DR2 BAO-alone reports h r_d = 101.54 ± 0.73 Mpc versus a Planck-like ~99.1 Mpc.
The fractional gap is ~2.4%. The model's 1.6% acoustic-scale shift moves toward that gap. It does not finish it.

What is not claimed: a number r_d = ... Mpc derived from c*G4. That product is 5.24e-6 pc and is the wrong clock (Clock III, slow modulation, not the sound horizon).
A finished Mpc ruler needs the D2-brane scale factor between -U and +U, which is not a closed constant.

Falsifier: if DESI+BBN and the CMB acoustic angle ever agree at the 10^{-3} level on the same r_d with no 1.6% shadow, the mu-1 dictionary is wrong.


5. Odd/even heights (P1/P2 closed)

Loading slot in the existing equations is kappa_dark and (1 + rho_DM/10).
Planck TT peak heights in D_ell:

    P1 = 5733 ± 39
    P2 = 2586 ± 23
    P3 = 2518 ± 17
    P4 = 1227 ± 9

First odd over first even:

    P1/P2 | Planck = 5733/2586 = 2.2169
    1/kappa_dark   = 539/243   = 2.2181
    residual -0.05%

Lock:

    H_odd / H_even |_{1,2} = 1 / kappa_dark = 539/243

Third over first (odd/odd, Silk between them):

    P3/P1 | Planck = 0.4392
    kappa_dark * S_silk(ell_3) / S_silk(ell_1)
        = (243/539) * exp( -(809.85^2 - 219.96^2) / 1439.73^2 )
        = 0.45083 * 0.746 = 0.336

Too low by 23%. The raw kappa_dark itself is 2.6% from P3/P1.
Do not force the Silk factor onto P3/P1 until the geometric D_ell prefactor ell(ell+1) and the radiation driving envelope are written in closed form. Status: P1/P2 CLOSED. P3/P1 OPEN at the 2.6% (undamped) or 23% (naive Silk) level.

P3/P2 = 0.9737 is even/odd after one full period; it is consistent with near-unity after loading and damping cancel, not a new constant.


6. Scoreboard

CLOSED this note
- TT ell_1..4 and trough 2 from {G4, 11, 27, h_j}
- EE ell_n = G4*(6n-4)/11 (n>=2) and G4*3/11 (n=1)
- Silk pair ell_D = G4*8/3, ell_t = G4*11/5, ell_S = 916.3
- P1/P2 = 539/243
- BAO calibration shift +1.60% on theta_* via G4(mu-1)

OPEN
- P3/P1 with a derived envelope
- r_d in Mpc from D2 scale factor
- EE amplitudes
- peaks 6-7 fractions forced by k_seg rather than listed rationals

Falsifiers
- Belle II 2pi is independent and does not touch this note.
- Simons Observatory / SPT-3G EE peak locations off the (6n-4)/11 grid by more than 3% after their own peak-fit convention would break the EE lock.
- A DESI+CMB joint analysis that forces theta_* agreement at 0.1% with no room for the mu-1 shadow would break the BAO calibration claim.
