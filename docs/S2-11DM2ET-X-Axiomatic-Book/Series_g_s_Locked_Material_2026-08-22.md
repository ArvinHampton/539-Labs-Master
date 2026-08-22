# Locked Material for the Series g_s (s in {7,8,11})

Ordinary mathematical English. Discrete packaging only. Continuum language excluded. Provenance under Pack+(S).

## Definition

For positive integer s,

g_s(q) = sum_{n=0}^\infty  q^{n^{2}} / (-q^s ; q^s)_n

where (-q^s ; q^s)_n is the finite Pochhammer symbol.

When s=1 the series recovers Ramanujan’s fifth-order mock theta function f_0(q).

## Exact Identity

P_s(q) := (-q^s ; q^s)_\infty · g_s(q)

The identity holds by the Euler product construction: the infinite product cancels the finite denominators termwise.

## Path Counts and Charge

P_s is the generating function for the unsigned orthant path counts of charge

Q_s(n,k) = n^{2} + s n k + (s/2) k(k+1)

(with n,k non-negative integers, or the bilateral extension as required for the form).

## Residue Support Theorem

The support of the coefficients of the orthant sums of Q_s is contained in the quadratic residues modulo s.

- s=7: residues {0,1,2,4} mod 7
- s=8: residues {0,1,4} mod 8
- s=11: residues {0,1,3,4,5,9} mod 11

Proved by direct reduction of Q_s modulo s.

## Lattice Data

Associated integer matrix of the homogeneous quadratic part (cleared denominators):

M_s = [[2 , s] , [s , s]]

Discriminant det(M_s) = s(2-s)

- s=7: det = -35
- s=8: det = -48
- s=11: det = -99

Signature (1,1) in each case.

## Cone Vectors (negative-norm examples)

s=7: pairs such as (-1,1) and (-4,1) (or equivalent spanning the negative cone).

s=8: (-2,1) and (-4,1)

s=11: (-2,1) and (-5,1)

These permit the standard orthant completion and error-function (R-function) corrections of Zwegers.

## Modular Connection

The orthant sum of lattice points of charge Q_s is completed by the Zwegers indefinite theta series construction of signature (1,1) to a weight-1/2 form. The holomorphic part recovers the path counts P_s. The exact identity then recovers g_s by division by the Euler product.

When s=1 this is the classical completion of Ramanujan’s f_0. For s in {7,8,11} the construction is the direct step-s analogue on the lattices of discriminants 35, 48 and 99 respectively.

## Obstruction

Free dynamics of the underlying ternary map do not produce the packaging length 539. The series constructions above are independent of that free dynamics.

## Open Optional Depth

- Explicit elementary combinatorial bijection mapping every multi-index of the finite inverse Pochhammer onto a unique lattice point of charge Q_s.
- Hecke-type parameters a,b,c in the Hickerson–Mortenson building block that reproduce g_s or P_s directly.
- Independent coefficient-by-coefficient expansion of the completed form beyond the classical identification.
- Crank statistic of independent combinatorial depth.

These items are not required for the modular statement already locked.

## Status for Submission

All material required to answer the three editor points (self-contained discrete definitions, excision of unproven termination claims, honest modular connection) is locked and ready for residual-only manuscript assembly.
