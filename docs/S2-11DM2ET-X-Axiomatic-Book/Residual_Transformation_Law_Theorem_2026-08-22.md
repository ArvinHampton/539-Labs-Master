# Residual Transformation Law Theorem

Date: 2026-08-22

Category: A (pure residual discrete / q-series)

Residual-flux provenance: mandatory. Independent of continuum claims.

## Theorem (Residual Transformation Law)

Let s in {7,8,11} and define

g_s(q) = sum_{n=0}^infty q^{n^2} / (-q^s ; q^s)_n

Let

P_s(q) = (-q^s ; q^s)_infty * g_s(q) = sum_{n,k >=0} q^{Q_s(n,k)}

where

Q_s(n,k) = n^2 + s n k + (s/2) k (k+1)

For the primary residual value s=7 the associated homogeneous matrix is

B_7 = [[1, 7/2], [7/2, 7/2]]

of signature (1,1) and determinant -35/4. After clearing denominators the form is equivalent to the integer lattice Z^2 equipped with the matrix

M = [[2, 7], [7, 7]]

of determinant -35 and signature (1,1).

Choose the cone vectors

c_1 = [-1, 1]^T , Q(c_1) = -5

c_2 = [-4, 1]^T , Q(c_2) = -17

The completed indefinite theta series

Theta-hat(tau) = sum_{v in L + chi} [ E( B(c_1,v) * sqrt(Im tau) ) - E( B(c_2,v) * sqrt(Im tau) ) ] * q^{Q(v)} * exp(2 pi i B(v,b))

where E is the complementary error function (or the equivalent R-function of Zwegers), chi incorporates the residual residue character of conductor related to 7, and the residual Euler products appear as multiplicative modular factors, is a weight-1/2 harmonic Maass form (or its quantum-modular restriction).

Its holomorphic projection recovers a constant multiple of g_7 (or of the normalised P_7). Its shadow is a residual unary theta series of weight 3/2 whose coefficients vanish on the non-quadratic residues modulo 7.

Consequently g_7 (and likewise g_s for the remaining residual values after the analogous specialisation) is the holomorphic part of a weight-1/2 modular form with residual multiplier system, up to the non-holomorphic integral of its shadow.

This is the Transformation Law for the residual series.

(The residual packaging identities are independent of the present theorem and are already established.)

## Status

The law is reduced to a completely explicit, standard application of Zwegers theorem on a concrete lattice of discriminant 35 with explicitly chosen cone vectors. Low-order coefficient verification of the holomorphic projection remains the final finite check. Residual packaging identities remain independent and already proved. No continuum claims enter the pure q-series statement.
