# Foldy-Wouthuysen transformation

Date: 2026-10-03
Status: exploration. Not a reopening. Not a new residual-flux object.
CORE_FREEZE unchanged. Rank 1 and Rank 3 stand.

## What it does

The Dirac Hamiltonian mixes positive-energy and negative-energy components. The Foldy-Wouthuysen transformation is a unitary change of representation that block-diagonalizes that Hamiltonian, order by order in 1/m, so the upper two components obey a Pauli equation.

Write the Dirac Hamiltonian as beta m c^2 plus an even piece E and an odd piece O. Even operators commute with beta. Odd operators anticommute with beta. For an electromagnetic potential,

H = beta m c^2 + e phi + c alpha · pi,

with pi = p - e A. The even interaction is e phi. The odd piece is c alpha · pi.

## Free particle, exact

With A = 0 and phi = 0 the transformation is exact. The generator is built from alpha · p, and the transformed energy is beta times sqrt((m c^2)^2 + c^2 p^2). No spin-orbit term appears, because no field is present.

## Interaction, iterative

With a field the transformation is iterative. One step uses the generator S = -i beta O / (2 m c^2). Conjugation by exp(i S) removes the odd piece at order 1/m and produces new odd pieces at higher order. Repeating the step through order 1/m^2 gives

H_FW = beta ( m c^2 + pi^2 / (2 m) - (e hbar / 2 m) sigma · B )
+ e phi
- (e hbar / (4 m^2 c^2)) sigma · (E × pi)
- (e hbar^2 / (8 m^2 c^2)) div E
plus higher-order remainders.

The third interaction line is spin-orbit. The fourth is the Darwin term. The sigma · B term is the magnetic moment, already present at order 1/m, and is not spin-orbit.

## Scales already computed

A hydrogen-like reading of the spin-orbit line for Z = 6 is 0.026 eV. The alpha^4 m c^2 scale is 1.45 meV. Neither is the 0.6 meV echo.

## Lock and torsion

This reduction used the electromagnetic odd piece. The lock Dirac operator uses the Levi-Civita spin connection, not A_mu. A Foldy-Wouthuysen reduction of that operator is a different expansion. Its curvature scale, on the conditional 137 nm rod, remains 1.42 times 10^{-12} eV across a nucleon Compton length. The rod is unselected.

An axial contorsion would add another odd or even piece, depending on the gamma-matrix structure, of order hbar c K. For the stipulated density that is 4.05 times 10^{-51} eV, and it is off the lock. The lock torsion is zero, so that piece is absent.

The transformation does not source T^lambda_mu nu. It does not restore the retired identification.
