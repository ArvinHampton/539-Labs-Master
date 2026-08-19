# U1-E1-PERIOD Period Lattice of C_Q4 Unavailable 2026-08-19

PURE MATH. Residual Discrete Algebra (539 as COUNT of leftover pieces in nine sector cores) ≠ Resonant Algebra (18+521 hard schedule). A count is not a clock. 539 is leftover COUNT. Free T3 short. Residual leftover combinatorics CLOSED. U1-DNE closed. SQRT-ALL closed except Q4 End. Gal(Q4/Q)=D5. U1-E1-IGUSA: Igusa not obtained. U1-E1-A2 on Master (7c9581e): a1 and a2 recorded for good p=3..37; Weil polys mostly irreducible; Jac consistent with a simple abelian surface; RM not forced; End still not locked. U1-E3-DOMAIN: no restricted 3-adic D. U1-E2-MONO: continuous Necessity monodromy not written. U1-E4-TRANSFER: no (T/2π)log from non-constant potential. Do not redo Igusa formulae, a2 enumeration, the 3-adic domain, Necessity monodromy, or transfer this turn. Continuum ARCHIVE. Do not reopen residual Cat A. Do not flatten multi-k into residual P. Do not import evenness by hand. Residual-flux provenance mandatory. Residual and Resonant stay unmixed.

## Target

Q4 = x^5 + 20x − 32. C_Q4 : y^2 = Q4(x) genus 2. Gal=D5. Zarhin does not apply. a1/a2 already recorded; do not recompute them.

Compute a period matrix (or numerical lattice in C²) for Jac(C_Q4), or lock periods unavailable with the exact missing analytic/CAS step. From that lattice, constrain End(Jac) over Q-bar if possible. Do not import a guessed RM order. Do not recompute Clebsch-Igusa. Do not re-enumerate F_p / F_p2.

## Available tools and what they supply

- Sympy: roots of Q4 (one real, two complex-conjugate pairs). No built-in hyperelliptic period matrix.
- Numpy / Scipy: numerical linear algebra and quadrature, but no genus-2 Abel-Jacobi or period-matrix routine in the locked environment.
- No Magma, Sage, Arb, or specialized hyperelliptic period package is available in this session.

## Exact missing analytic / CAS step

A period matrix of Jac(C_Q4) requires:

1. Ordering of the five branch points (roots of Q4) and a choice of branch cuts.
2. A symplectic basis {A1, A2, B1, B2} of H_1(C_Q4, Z).
3. High-precision complex integration of the two holomorphic differentials ω1 = dx/y and ω2 = x dx/y over that basis.
4. Assembly of the 2×2 period matrix Τ such that the period lattice is Z² + Τ Z² in C².

Standard implementations: Magma PeriodMatrix, Sage RiemannSurface / abelfunctions period routines, or arb-based numerical Abel-Jacobi. None of these is present in the current computational environment, and no custom high-precision period integrator is written in the locked corpus.

## Verdict

Periods unavailable. Exact missing object: a high-precision period matrix (or numerical period lattice) of Jac(C_Q4) obtained by integrating the holomorphic differentials over a symplectic homology basis.

Without periods (and without Igusa), End(Jac(C_Q4)) over Q-bar remains not locked to a specific ring. Prior constraints stand: Zarhin does not apply; a1/a2 are recorded; Weil polynomials are mostly irreducible (consistent with a simple abelian surface); RM is not forced by Frobenius data alone.

Q4 stays imported D5. Residual P stays Gal(P/Q)=S5. Do not import RM into Necessity or residual P.

Hygiene: Residual Discrete Algebra is leftover pieces. Resonant Algebra is how long you stir. Free T3 short. Continuum ARCHIVE. A count is not a clock. Residual-flux provenance mandatory.
