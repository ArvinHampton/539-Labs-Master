# Correction: 18 attoseconds is 18 femtoseconds

Date: 2026-10-03
Status: prefix correction. Not a new residual-flux object.
CORE_FREEZE unchanged.
Supersedes the attosecond reading of the baseline in artifacts/Missing_Equations_for_2c77354a_2026-10-03.md equation E4, and restates the 27 September lock.

## The equation

Front matter of The 17 Theorems of Entanglement writes

tau_ent = tau_echo * (Delta E / hbar Omega) = 3e-12 s * (0.6 meV / 100 meV) = 18 as.

The product is

3e-12 * 0.006 = 1.8e-14 s = 18 fs = 18000 as.

The printed unit is short by 1000. The baseline is 18 femtoseconds. It is not 18 attoseconds.

## What the correction does to the rod

lambda_flow = c * tau_ent.

With the corrected time, lambda_flow = 5.396 micrometres.

That is the length the Theorem 6 proof already printed (5.4e-6 m) while naming the time 18 attoseconds. The wavelength step used the femtosecond product. The attosecond label was the error. The earlier note that treated the label as the quantity and called the true wavelength 5.40 nm is withdrawn for this baseline. 5.40 nm is c times 18 attoseconds, and 18 attoseconds is not the product.

The body coherence length 3.2e13 m = 0.00338 light-years was built on that printed wavelength. It does not move under this correction. The abstract print 0.34 light-years remains the separate factor-of-100 light-year error. Two errors, not one.

## What the correction does not do

It does not match Jiang et al. 2024. The corrected baseline, 18 fs, is 78 times the 232 attosecond TDSE average. The printed 18 attoseconds was the figure that could be multiplied by N_eff = 10, a gradient 1.3, and a flux average 0.8 to sit next to 232 attoseconds. That chain used the wrong unit. It is not recovered by correcting the unit.

The 22.5 attosecond print is a different formula and is not repaired by this correction. Resonant bias at pi/4 gives hbar / 29.3 meV = 22.46 fs, printed as 22.5 as. The small-angle line E_bind = Delta E^2 / (2 hbar omega) = 0.0018 meV gives hbar / E_bind = 0.366 ns, also printed as 22.5 as. Three written times, three results. Only the 18 as baseline is corrected here.

18 fs is not a tubulin period, not 25 ms, and not G4. Orch-OR11D is unchanged. No new residual-flux object.
