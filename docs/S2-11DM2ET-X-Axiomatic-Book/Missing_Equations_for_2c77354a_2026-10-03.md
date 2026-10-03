# Missing equations for commit 2c77354a

Date: 2026-10-03
Commit addressed: 2c77354a30eebc2d5216aff08e6998da04bf6c4e
Parent of that commit: 46aa374e
Message of that commit: Torsion-to-tubulin pursuit. Four ingredients empty. Close (B).

That commit named the equations and did not write them. This note writes them. Writing the equation is not a derivation and does not change the close.

## E1. Lock torsion

The connection verified by L1-L7 is Levi-Civita. Its torsion vanishes:

T^lambda_mu nu = 0.

No equation in 2c77354a replaced this identity.

## E2. Theorem 1 symbol, not contorsion

The monograph writes

H_torsion = (e^{2 pi i t / 539.9} - 1) wedge H_3 * g_11 Phi psi,

with the split fixed by

Delta E = 0.6 meV.

This is a Hamiltonian term. It is not T^lambda_mu nu. The phase inserts 539.9. Theorem 12 of the same monograph says the delay does not depend on that period. Both sentences stand. Neither is E1.

## E3. Settling time, with the prefix corrected

E_bind = hbar omega (1 - cos Delta phi),

hbar omega = 100 meV, Delta phi = pi/4,

E_bind = 100 meV * (1 - sqrt(2)/2) = 29.289 meV.

tau_settle = hbar / E_bind = 2.246 times 10^{-14} s = 22.46 fs.

The proof prints 22.5 attoseconds. The equation is the femtosecond value. The printed name is the prefix error locked on 27 September.

## E4. Theorem 6 rod, with the prefix corrected

lambda_flow = c * tau_ent.

For the printed 18 attoseconds,

lambda_flow = 5.396 times 10^{-9} m = 5.40 nm.

The proof prints 5.4 times 10^{-6} m, which is c times 18 fs. The length used downstream is the femtosecond product under an attosecond label.

L_coh = 3.2 times 10^{13} m = 0.00338 ly = 214 AU

in the body. The abstract prints 0.34 ly. The body says that label used a light-year short by 100. Two equations, two prints.

## E5. Sixth stress and contorsion, the geometric slot 2c77354a left empty

T^(EH)_MN = T^(G4)_MN + T^(M2)_MN + T^(vis)_MN + T^(hid)_MN + T^(PBH)_MN + T^(spin)_MN.

T^(spin) is sourced by a spin density s_alpha beta. Carrier unselected.

If the connection is enlarged off the lock,

K^lambda_mu nu = -1/2 (T^lambda_mu nu - T_mu^lambda_nu + T_nu^lambda_mu).

On the lock, T = 0, so K = 0. Theorem 19 wrote the same map and filled T from -U currents. That fill is not E5.

## E6. Theorem 19 amplification, evaluated

The sequel writes

A = 1 + 0.8 * (beta_PBH / 0.1).

A(0.1) = 1.8.
A(0.18) = 2.44.
A(0.181) = 2.448.

The printed 1.8 is A at the inserted value 0.1, not at the ledger input.

## E7. Theorem 20 product, evaluated

The sequel writes

lambda_coh = (c / sqrt(10)) * 2.33e-16 * 1e6 * (539.9 / 40)

and labels it 0.4 ly.

Evaluated,

lambda_coh = 0.298 m.

0.4 ly / 0.298 m = 1.27 times 10^{16}.

539.9 / 40 = 13.4975, not an integer. The set {5, 10, 15, 30, 45} s against 25 ms is a factor 200 at the shortest entry. The equation does not produce the label.

## E8. Rod the commit said was underived

tau_warp = ell_star / (c * 0.02531),

ell_star unselected.

The length that would match a stated target T is ell_star = T * c * 0.02531.

For T = 25 ms, ell_star = 1.897 times 10^5 m.
For T = 10^{-13} s, ell_star = 7.588 times 10^{-7} m.
For T = 10^{-4} s, ell_star = 759 m.

R_11 = 85 um is none of these.

## E9. E_G the commit said was unwritten

Stated dimer mass m = 110 kDa = 1.827 times 10^{-22} kg.

E_G(1) = G m^2 / a,    tau_1 = hbar / E_G(1),    N(T) = tau_1 / T

under linear counting. G m^2 = 2.227 times 10^{-54} J m.

At a = 1 nm and T = 25 ms: tau_1 = 4.736 times 10^{10} s, N = 1.894 times 10^{12}.
At a = 1 fm and T = 25 ms: tau_1 = 4.736 times 10^4 s, N = 1.894 times 10^6.

The public count about 2 times 10^{10} is not a row of this equation. 29.3 meV is not E_G(1).

## E10. Decoherence time in the same unit

tau_dec ? tau_OR, with tau_OR = 25 ms for the public gamma moment.

Tegmark: tau_dec ~ 10^{-13} s, ratio 4.0 times 10^{-12}.
HHT dipole: 10^{-5} to 10^{-4} s, ratios 4.0 times 10^{-4} and 4.0 times 10^{-3}.
HHT gelation: 10^{-2} to 10^{-1} s, ratios 0.40 and 4.0.

Only the last upper edge satisfies tau_dec > tau_OR. It is an argument in the 2002 reply, not an output of E1-E9.

## Status

E1 is the lock. E2-E4 and E6-E7 are the monograph equations with the arithmetic corrected. E5, E8, E9, E10 are the four ingredients 2c77354a named and did not write. Carrier, ell_star, and separation remain unselected.

Close (B) of 2c77354a stands. No new residual-flux object. CORE_FREEZE unchanged.
