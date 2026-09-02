# Op_ring and Snap: empty composition, recommended contact

Date: 2026-09-01
Category: B continuum only
Does not alter residual discrete CORE_FREEZE
Twin Prime and RH unclaimed
Residual-flux provenance mandatory

Companion to PhotonRing_CriticalCurve_Derivation.md. That note writes the linear critical-curve formula and the snap-matching value psi(3M) = -2/3. This note records the operator status after the 2026-09-01 pursuit.

## Recommended printed contact

Three generations give W_np = e^3.

alpha = e^{-3} approximately 0.049787.

The geometric length at mass M is GM/c^2.

Delta r_sat^(contact) = e^{-3} GM/c^2 approximately 0.04979 GM/c^2,
spoken as 0.05 GM/c^2.

Pack_N rewrite of the same amplitude:

243/4880 = 243 / floor(e^3 * 243) approximately e^{-3},
miss 0.016 percent.

So the same line may be written

Delta r_sat^(contact) = (243/4880) GM/c^2.

That rewrite is the flux-floor tautology. It is not a geodesic cutoff.

## Operators

Op_GR(n, M) = 3 sqrt(3) (GM/c^2) e^{-pi n}.

Schwarzschild photon sphere r_ph = 3M.
Critical impact b_c = 3 sqrt(3) M.
Lyapunov per half-orbit gamma = pi.
Demagnification e^{-pi} approximately 0.04321.

Snap is typed as a map

Snap : {3, e^3, 4880, 18, 521, 539, G_4} -> N_*.

N_* is the half-orbit index that would be fed to Op_GR so that the output hits the contact inside 3 percent, with no free exponent.

The values Snap would have to return are

N_abs = 3(1 + (1/2) ln 3)/pi approximately 1.4794783874004618

N_rel = 3/pi approximately 0.9549296585513720.

Neither sits in Allowed. Snap is an empty map.

Op_ring = Op_GR composed with Snap
is therefore empty, even though Op_GR is written.

## Leftovers that are not Snap

243/4880 versus e^{-3}: Pack_N backwards.
521/539 versus 3/pi: window complement 1 - 18/539. Miss 1.22 percent. The miss equals 18/539 - (1 - 3/pi).
67/61 versus ln 3: fibre over puncture, miss 0.023 percent.
11/7 versus N_abs: miss 9 percent.
4/e versus N_abs: not in Allowed.

A nearby numeral is not an operator. Pack_N manufactures e^{-3}-looking ratios. Window/body splits manufacture 3/pi-looking complements.

## Type changes that do not fill Snap

R1. Metric deformation

f_eps = 1 - 2M/r + eps psi(r), eps = 243/4880.

Linear formula already in PhotonRing_CriticalCurve_Derivation.md:

Delta b_c / b_c = -(3/2) eps psi(3M) + O(eps^2).

Setting psi(3M) = -2/3 forces alpha = 1 and recovers the contact. The value -2/3 is chosen so that (3/2)*(2/3) = 1. It is not produced by {3, e^3, 4880}. Snap has been moved into psi(3M).

R2. Kerr Lyapunov

On Kerr, gamma runs from about 2.04 to pi. So gamma = 3 exists and e^{-gamma} = e^{-3} exists. Allowed does not contain a spin. Picking that locus writes the generation count onto gamma.

Integer n = 1, 2, 3, 18, 521, 539, time snap with G_4, and rho_snap as a density ratio all fail the typed map.

## Photon shell

Schwarzschild: one sphere at 3M.
Kerr: a shell from r_tilde_minus to r_tilde_plus.
The observer sees the critical curve C, not N_*.
ngEHT constrains C and in principle gamma(phi). It does not see Snap.

## Quantum-gravity scale

GM/c^2 is the hole. e^{-3} of that length is still the hole. On Sgr A* that is a few times 10^5 km. A Planck core is 10^{-35} m. Standard quantum-gravity shifts at the photon sphere run in powers of ell_P / M. The printed contact, taken as quantum gravity, is order-unity physics at 3M. That disagrees with ell_P/M physics by tens of orders unless a map from the core to the shell is found. That map is Snap, and Snap is empty.

## Status codes

OP_GR_FOUND_SCHWARZSCHILD_LYAPUNOV_2026-09-01
SNAP_EMPTY_MAP_ALLOWED_TO_NSTAR_2026-09-01
OP_RING_EMPTY_COMPOSITION_2026-09-01
CONTACT_E_MINUS_3_GM_C2_CATB_2026-09-01
PACK_N_TAUTOLOGY_243_OVER_4880_NOT_GEODESIC_2026-09-01

Do not present Op_ring as a geodesic-plus-snap theorem.
