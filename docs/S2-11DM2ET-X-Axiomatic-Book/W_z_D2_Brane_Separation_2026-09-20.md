# W(z) from D2-brane separation

2026-09-20  Category B

Pack+(S). Residual-flux provenance mandatory. CORE_FREEZE holds.
No DESI fit. No new generators. N_star=14 unused.

G4=539.9  D=11  N_flux=4880
kappa_dark=243/539  f_snap=243/4880  mu=1.55
Omega_m=162/539  Omega_DE=377/539


1. Geometry

+U sits at y=0. -U sits at y=b(t). D2-branes span time, one +U direction, and the extra interval of length b. The 539.9 s flux is Clock III (modulation), not the radion clock. The background is the slow envelope of b after snap.

Snap locks 3^5 of N_flux units. Residual motion of b is the unsnapped fraction f_snap.


2. Radion velocity after snap

For a modulus with potential dominating and a residual kinetic piece,

    1 + w = (2/3) (KE / V)     and     ḃ / (H b) = sqrt(3 KE / V)

The locked equation of state leftover is f_snap, so

    ḃ / (H b) = sqrt(3 f_snap) =: alpha = 0.38650

    d ln b / d ln a = alpha

    b(z) = b_0 (1+z)^{-alpha} = b_0 (1+z)^{-sqrt(3 f_snap)}

At z=0, b=b_0. At z_*=1089, b_*/b_0 = 1090^{-alpha} = 0.0670. Branes were closer at last scattering.


3. Warp identification

Today the fraction of flux that leaks through the extra-dimensional channel is kappa_dark. In RS language that is the geometric redshift of -U onto +U:

    exp(-k b_0) = kappa_dark
    k b_0 = -ln kappa_dark = 0.79665

Then

    k b(z) = (-ln kappa_dark) (1+z)^{-alpha}
    exp(-k b(z)) = kappa_dark^{(1+z)^{-alpha}}

Leaked energy density on +U tracks the warp relative to today:

    W(z) := rho_DE(z) / rho_DE(0)
         = exp(-k (b(z) - b_0))
         = kappa_dark^{ (1+z)^{-sqrt(3 f_snap)} - 1 }

That is the derived warp. It uses only {kappa_dark, f_snap}.


4. Effective equation of state

    w_eff(z) = -1 + (1/3) d ln W / d ln(1+z)
             = -1 + (alpha/3) (-ln kappa_dark) (1+z)^{-alpha}
             = -1 + 0.1026 (1+z)^{-sqrt(3 f_snap)}

    w_eff(0)   = -0.897
    w_eff(0.5) = -0.912
    w_eff(z_*) = -0.993

The radion is almost frozen at last scattering and rolls more at late time as the branes separate. This is the opposite of a CPL fit that puts the evolution at high z.

The earlier constant-w close w=-1+f_snap=-0.950 is the time average of w_eff over the matter era, not a replacement for W(z).


5. Friedmann equation on +U

    E(z)^2 = Omega_m (1+z)^3 + Omega_r (1+z)^4 + Omega_DE W(z)

    Omega_m = 162/539
    Omega_DE = 377/539
    Omega_r = 9e-5   (photon+neutrino, not derived here)

H0 is not an independent input. It is fixed by D_M(z_*)=13911 Mpc:

    H0 = c * chi(z_*) / 13911 Mpc

with chi = integral_0^{z_*} dz'/E(z'). At this W, H0=67.86 km s^{-1} Mpc^{-1}, h r_d=99.88 Mpc.


6. DESI is a test, not a fit

W(z) vs constant-w vs DESI 6-bin D_M+D_H:

    constant w=-1+f_snap     rms 1.98%   (this integrator)
    radion W(z)              rms 2.14%

The geometric W is slightly worse on current DESI bins. It is not retuned. LRG1 D_H remains a data-side residual.

Falsifier: a measured w_eff(z) that falls (more negative) toward z=0, or that is already -0.7 at z_*, kills the radion identification. The prediction is w closer to -1 in the past.


7. What is not claimed

D2 tension T_2 in GeV^3 is not derived (needs alpha' and g_s).
Which two spatial directions the D2 wraps beyond the extra interval is not fixed.
Bulk dark radiation C/a^4 is not introduced.
CPL (w0, wa) is not a parameter of the model.


8. Closed formulae

    alpha = sqrt(3 f_snap) = sqrt(729/4880)
    b(z)/b_0 = (1+z)^{-alpha}
    k b_0 = -ln(243/539)
    W(z) = (243/539)^{ (1+z)^{-alpha} - 1 }
    w_eff(z) = -1 + (alpha/3) ln(539/243) (1+z)^{-alpha}
