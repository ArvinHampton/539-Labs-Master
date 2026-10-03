# Kinetic term for a propagating torsion

Date: 2026-10-03
Status: written as a Category B extension. Mass unselected. Not a lock output.
CORE_FREEZE unchanged. Old ingredients stay retired. No new residual-flux object.

## Term

Einstein-Cartan torsion has no kinetic term. The extension written here is a Proca-like term for an axial vector A_mu,

L_kin = -1/4 F_mu nu F^mu nu - (1/2) mu^2 A_mu A^mu,

F_mu nu = partial_mu A_nu - partial_nu A_mu.

The mass mu is not derived. Setting mu = 0 is a second stipulation, a massless axial field, not the lock.

## Field equation

Varying with respect to A gives

partial_nu F^nu mu + mu^2 A^mu = J^mu,

where J^mu is the axial current of the spin density. On the lock there is no spin density in the five-piece stress, so J = 0 and A = 0 is the solution. A nonzero A requires the stipulated spin census as a source. That source is off the lock.

## Propagator

In momentum space the propagator is

D = 1 / (p^2 - mu^2),

up to the usual Proca projector. The static potential falls as exp(-mu c r / hbar) / r. The range lambda = hbar / (mu c) is unselected.

Stipulated ranges, not derived: 8 nm gives mu c^2 = 24.7 eV and is dead at 137 nm. 137 nm gives 1.44 eV and is dead at 5.40 um. 5.40 um gives 0.037 eV and is an insertion. The range that matches the census scale is 1.12 times 10^37 m, mass 1.76 times 10^{-44} eV.

## What the term does not do

It does not raise the near-field source. The census scale stays 2.26 times 10^{-39} per metre. It does not set T^lambda_mu nu on the Levi-Civita lock. It does not select 18 fs, 137 nm, or 539. L1 through L7 are unchanged.
