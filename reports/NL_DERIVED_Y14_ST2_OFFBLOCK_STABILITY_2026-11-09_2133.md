# NL DERIVED: off-block and phase-sector stability of the Y14 MN2 non-BPS E₈ points, with an ST1 T-sequence
2026-11-09, 21:33 CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED**, unchanged. The count-gap status is unchanged.

Authority: **OW t4426** OWNER_WRITE_MAINCHAT_t4426_PURSUE_ALL_OPEN_JUNCTION_ROUTES_2026-11-09_1956.md = d5eaeef3f6b53270bd09e30053f6cdbf442d191c58a0a9fda30daff83907ffb3 ("Pursue all open"; this is item 7). **OW t4436** OWNER_WRITE_MAINCHAT_t4436_LET_MATH_LEAD_ALL_OPEN_PATHS_2026-11-09_2127.md = 328812635d807f5cb7d1e5e6b5df7f89512060c36c090a2a191526ab7e90fd46 ("Let the math lead the pursuits on all open paths": χ-smeared and χ-uniform are separately labelled branches; the marginal-w route is its own branch; a branch is kept or dropped only by a PROVED or REFUTED result; nothing is adopted by fiat). **OW t4431** f700141d… (no usage-threshold stop; usage is still reported). Also OW 19a88b19 (junction UNSOLVED); OW 36683379 (citations checked, never upgrade alone); OW 9bb1858c / b0b9ae7f (Y14). Builds on Y14 stage 2 1950 (ST1 CONDITIONAL, ST2 OPEN), E17-N13 (N-sequence, ST1 stays CONDITIONAL), PP 077e417d / 1953 (ST2 left OPEN).

Limits: additive only. No existing script or report is edited (including 1950, E17, y14s2.py, disc.py, and the 2109 ST2 script). No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before and after. Usage 85.4% at the start of this write (weekly reset Tue Nov 10 09:49 CST).

Under t4436 the **χ-smeared** [χS] and **χ-uniform** [χU] branches are not chosen between, and the **marginal-w** [w] route is carried as its own branch (CGR SO(2)_R sector, Z1/Z2). Item 6 (2103) already proved that w is not H-invariant in T7; that does not drop the [w] branch.

**Tally: PROVED 3 · CONDITIONAL 1 · OPEN 2 · REFUTED 0 · total 6**

## 1. Question

ST1 checked the second variation of the Y14 stage-2 functional only in the equivariant (h, a) sector, at a single T=12 (E17 added an N-sequence at that T). ST2 asked for any negative mode outside that sector: the phase / a_t sector, non-equivariant modes, and the off-block E₈ modes of a mirror pair in (2,2)⊗**12** and (2,1)⊗**32**, (1,2)⊗**32′**. A T-sequence of the ST1 eigenvalues was noted as cheap and is included.

Scripts and logs, new dated directory `/workspace/nl-st2-offblock-2105/`, sidecars:
- st2_Tseq_phase_2026-11-09_2129.py = 6f0880c8f6c03a8bec77d4a828e592a45bae56992997a90edf5d671c749e31b0, **frozen before execution**. Uses `/workspace/nl-junction-1851/{y14s2.py,disc.py}` unchanged, and continues a T=12 `solve_face` solution to larger T with `run(..., guess=...)`.
- st2_Tseq_phase_2026-11-09_2129.log = 3a7e522a0e8f700e4904bfce1375a45f966a9949e7e934b3670104dd264600cc
- An earlier script, st2_Tseq_phase_2026-11-09_2109.py = b71d3c5b6ab18fbe4751a73a4354e510da2ad632b24da29a709dcae66b0fc4c6, is not edited. It produced T=12 and T=16, n=1, in agreement with 2129, then stopped at T=20 n=1 when ARPACK with shift σ=−1 failed to converge (log 02f7a747…). The 2129 script uses shift-invert at 0. Those T=12 and T=16, n=1, eigenvalues are not re-counted; they match.

## 2. S7-T (CONDITIONAL; float64, (h, a) sector, cutoff law). T-sequence: no negative mode; λ₁ ∝ e^{−T}

At the MN2 IR face with the twist on, n=1,2,3, N=2000, the four lowest L²-normalized Hessian eigenvalues in the (h, a) sector are positive at every T tested, are far-end a-modes (peak in the last 10% of [10⁻³, T]), and are independent of n to the printed digits:

| T | status | rms | λ₁ | λ₂ | λ₃ | λ₄ | λ₁(T)/λ₁(12) | e^{−(T−12)} |
|---|---|---|---|---|---|---|---|---|
| 12 | 0 | 9.8e-9 | 5.833939e-5 | 1.365470e-4 | 2.427643e-4 | 3.771897e-4 | 1 | 1 |
| 16 | 0 | 9.8e-9 | 1.068514e-6 | 2.500894e-6 | 4.446221e-6 | 6.908089e-6 | 1.831548e-2 | 1.831564e-2 |
| 20 | 1 | 1.8–3.3e-8 | 1.957030e-8 | 4.580423e-8 | 8.143158e-8 | 1.265171e-7 | 3.354561e-4 | 3.354626e-4 |
| 24 | 1 | 1.8–3.8e-8 | 3.584377e-10 | 8.389062e-10 | 1.491386e-9 | 2.317041e-9 | 6.144009e-6 | 6.144212e-6 |

The T=12 values agree with ST1 / E17-N13 (5.8e-5 … 3.8e-4). The law λ₁(T)/λ₁(12) = e^{−(T−12)} holds to five or six digits already on the two **status-0** points T=12 and T=16. T=20 and T=24 are status 1 (not used as energy solutions, same convention as 1950 on the T=22 lines); they follow the same exponential and are recorded only as supporting evidence for the cutoff. T² λ₁ is not constant, so this is not a 1/T² artefact.

There is no negative mode in this sector at any of these T. The small size of λ₁ is a finite-T cutoff, as 1950 stated. ST1 stays **CONDITIONAL** (float64, (h, a) only, finite T, and the two larger-T BVPs are status 1). The T-sequence does not upgrade it.

## 3. S7-phase (PROVED). No negative mode in the reduced phase sector

Let h(t) e^{iα(t)} replace the real profile h, at fixed a. Every potential term in the stage-2 density depends on |h| or on h′ through |D_t h|². The only new piece is

E_phase[α] = ∫ A(t) h(t)² (α′)² dt,    A = s W / g_{tt} > 0 on (0, T).

This is ≥ 0, and vanishes if and only if α′=0 wherever h≠0. The kernel is the global phase (a residual U(1) gauge mode). There is no negative direction in this reduced sector.

A midpoint discretization of the same quadratic form, at T=12, N=2000, n=1,2,3, confirms this: with Neumann conditions (gauge unfixed) the lowest eigenvalue is consistent with 0 at ≲ 10⁻⁸ (n=1: −3.2e-9; n=2: +9.4e-9; n=3: −1.1e-8), and the remaining eigenvalues are positive; with Dirichlet α(t₀)=0 they are positive for n=1,2, and for n=3 the same 10⁻⁸ floor appears (h vanishes at the S² orbit, so the phase is weakly supported there). The 10⁻⁸ floor is discretization noise around the analytic kernel, not a physical negative mode. The grade is PROVED by the integral identity; the numbers are a check.

## 4. S7-a_t (PROVED). The radial/time U(1) component is gauge

On the interval, a radial (or world-volume-time) component a_t of the residual U(1) can be gauged to zero by a t-dependent gauge transformation, up to a residual constant already identified as the kernel of S7-phase. It does not add a physical direction to the 1D reduced second variation. No extra negative mode arises from a_t in this reduction.

## 5. S7-off (OPEN). Off-block E₈ modes and non-equivariant modes are not computed

The following ST2 items remain uncomputed, and are not dropped (t4436: only PROVED or REFUTED can drop a branch):

- Off-block modes of a mirror pair, in the E₈ adjoint components (2,2)⊗**12** and (2,1)⊗**32**, (1,2)⊗**32′** of SU(2)×SU(2)×(commutant). A quadratic form was not written or diagonalized.
- Non-equivariant (non-SO(3)×U(1)) modes on the fibre. Bourguignon–Lawson on round S⁴ would relate non-self-duality to instability, but it does not apply to the weighted, twisted functional (1950, PP 1953). The UV/round c=0 solutions are BPS and are not in conflict with that theorem; the twisted MN2 IR solutions are non-self-dual (S2-2) and this remains an open test, not a proof of a negative mode.
- Multi-centre U(1)-equivariant configurations inside one block (PP N9 / Q0-out), which are also item 8.

Y14's overall existence status is unchanged: CONDITIONAL in the sectors that have been checked, **OPEN** until S4-applied, S6 and S7-off are settled. No negative mode has been exhibited, and none of the unchecked branches has been shown to be positive-definite.

## 6. S7-χ (PROVED, scope). The fibre Hessian is the same on [χS] and [χU]; both branches are kept

The Y14 second variation is a fibre problem (the weighted, twisted functional on the MN2 S⁴, at a fixed 7D face). It does not depend on how the wall sources are smeared in χ. So the operators, the T-sequence, and the phase identity are the same on the **χ-smeared** and **χ-uniform** branches. Neither branch is selected. Wall-level consequences of [χS] versus [χU] remain those of item 6, R7, and are not re-opened here.

## 7. S7-w (OPEN). The marginal-w branch is carried, not dropped

Z1 (item 6, R2): at exact MN2, w is marginal, Δ=4, cubic −24·2^{2/3}g² ≠ 0. Item 6, R3, proved that w is not H-invariant, so it does not enter T7 or the 1948 H-invariant count. Under t4436 that is not a reason to drop the route. The [w] branch is the larger CGR SO(2)_R sector (CGR §5.2.2–5.3), including Z2 (IR-regular non-W₃ centre-manifold flows, w ~ 1/r), which is still OPEN.

The Y14 critical points computed above sit at the exact MN2 geometry (w=0). Off-block, or even (h, a), stability along a [w] flow with w≠0, and E₈ fields on that deformed fibre, have not been computed. The branch stays OPEN.

## 8. What this does not change

The junction remains **UNSOLVED**. χ-smearing remains undecided; both branches are kept. The [w] branch is kept and OPEN. The count gap is unchanged (S11-count / S12′ stay as in 1950 / E17). ST1 is not upgraded. ST2 is partly discharged (phase and a_t have no negative mode; T-sequence confirms the (h, a) cutoff) and remains OPEN for genuine off-block and non-equivariant modes. Nothing is adopted.
