U1-LEDGER-BRIDGE-C-RESIDUAL-LAW
Obstruction. No residual law for Bridge Series C found. Exact reduction to the shared remainder P_s.
Category A ledger only. Category B items are in CatB_Notes_Bridge_C_Residual_Law_2026-10-17.md.
2026-10-17

PURE MATH. 539 is a COUNT. Residual is not Resonant. CORE_FREEZE untouched. No locks altered.
No HQCC termination claim. Twin Prime and RH unclaimed.

Parent tip. 495a0bce7f242d78d44ee3a0bc537a26be23996b (main).
Source (verbatim copy). Bridge_C_Residual_Law_2026-10-17/2026-10-17-Bridge-C-Residual-Law.md, with scripts and outputs in the same folder (the report's "2026-10-17-bridge-c-residual-law/" refers to that folder).
Definitions as on Master: Residual_Bridge_Series_C_Definition.md (M = [[2,s],[s,s]], Q_s(n,k) = n^2 + snk + (s/2)k(k+1), c1 = (-1,1), c2 = (-4,1), P_s, H_s, C := P_s - H_s), here s = 7.
Citations used. HM = Hickerson-Mortenson, arXiv:1208.1421 (Def. 0.2). Zwegers thesis, arXiv:0807.4834. A. Baker, Linear forms in the logarithms of algebraic numbers I, Mathematika 13 (1966).
Errata found in this pass are filed separately: ERRATUM_Bridge_C_Decomposition_and_Samples_2026-10-17.md.


1. Shared remainder P_s (Cat A; exact rational coefficients through q^3000; identities.py / identities.txt)

P_s = sum_{n,k>=0} q^{n^2 + 7nk + (7/2)k(k+1)}.
C = -H_s + P_s (the definition).
C_third = q^8 f_{2,7,7}(-q^10, -q^14, q) + P_s (also an elementary reindexing: r = n-1, s = k-1, x = -q^10, y = -q^14; the negative orthant becomes P_s with sign -1).
Also exact through q^3000: Theta_hol = q^8 f_{2,7,7}(-q^10,-q^14,q) + theta_3; C - C_third = -H_s - q^8 f_{2,7,7}(-q^10,-q^14,q); P_s = R + (1+theta_3)/2 with R = sum_{n>=0,k>=1} q^{Q_s}.
H_s box enlarged by 30: identical result.
Everything else in C and C_third is Zwegers/HM indefinite theta or unary theta. The residual-law question is a question about P_s.


2. Obstruction 1: additive "modular + controlled remainder" (Cat A, conditional on two cited standard inputs)

Radial asymptotics, q = e^{-t}, t -> 0+ (asymptotics.py / asymptotics.txt).
P_s = I/t + a_P t^{-1/2} + O(1). C_third = I/t - a_P t^{-1/2} + O(1). C = I/t + O(t^{-1/2}).
I = log(6 + sqrt35)/(2 sqrt35) = 0.2094198203... (6 + sqrt35 is the fundamental unit of Q(sqrt35); closed form matches quadrature to 40 digits).
a_P = 0.5256172043... (quadrature, confirmed by fit to 4-5 digits).
Lemma 2: the holomorphic part of any signature-(1,1) Zwegers theta (negative-norm c's, rational characteristics) has 1/t coefficient 0 (cone / minus-cone cancellation). Covers H_s, Theta_hol, q^8 f.

Statement. Let M be the Qbar-span of: q^r times weight-1 holomorphic modular forms on Gamma(N) with Qbar coefficients; half-integral-weight forms (with q^r) and integral weight k >= 2 forms (no shift); holomorphic parts of signature-(1,1) Zwegers thetas as above; unary, partial and false thetas with periodic Qbar coefficients. Then there is no identity C_third = F + E or C = F + E with F in M and E(e^{-t}) = o(1/t).
Proof idea. Multiply by t: M contributes 2 pi beta + gamma with beta, gamma in Qbar, but I involves log(6 + sqrt35); Baker gives the contradiction.
In particular no weight-1/2 residual false theta can absorb the remainder.

Inputs and their status.
(a) Baker's theorem (Mathematika 13, 1966): cited, standard.
(b) Qbar-rationality of cusp expansions of modular forms on Gamma(N) with Qbar coefficients (Shimura's Q(zeta_N)-rationality / q-expansion principle): cited as standard; the theorem number was NOT re-checked in this pass.
(c) Lemmas 1-2: elementary (2-D Euler-Maclaurin; cone symmetry), numerics agree to 4-5 digits. No formal Euler-Maclaurin remainder bound was written.
Null-vector cones (Q(c) = 0) are excluded.


3. Obstruction 2: theta-prefactor / quotient route (Cat A as scoped)

For holomorphic modular forms g != 0 and F of any weights, levels, multipliers, and any q^r factor:
C_third * g != F. Cat A. Reason: F/g along q = e^{-t} has only integer-step powers of t, while C_third has the nonzero term -a_P t^{-1/2}.
C * g != F with Qbar coefficients. Cat A (by the Baker argument).
C * g != F with complex coefficients: NOT claimed here (Cat B; needs the t^{-1/2} coefficient of C, known only numerically).


4. Obstruction 3: scalar Fricke / W_7 slash at any weight k and constant lambda (Cat A, finite computation; fricke_profile.*, w7_phase.*)

Leading singularity at rational x: lim t * C(e^{2 pi i x} e^{-t}) = I * G(x), G(x) = (2m)^{-2} sum_{(n,k) mod 2m} e(x Q_s(n,k)) for x = h/m (H_s contributes 0).
Zero pattern. Among 270 rationals with denominator < 30, at 178 exactly one of G(x), G(-1/(7x)) vanishes (examples 5/7, which is a Master sample point, 2/7, 4/7, 6/7, 2/3, 4/9). There the cocycle C - lambda (7 tau)^{-k} C(-1/(7 tau)) is unbounded for every k and lambda. (G computed in floating point; nonzero values >= 0.034, zero values < 1e-9.)
Common support (60 pairs). |G| obeys the relation exactly for weight k = 1 with |lambda| = 7^{-1/2} (not weight 1/2). The phase arg(G(x)/(7^{-1/2}(7x)G(W_7 x))) varies with x (pi/2 at 1/7 and 1; -pi/6 at 1/3 and 3/7), so no constant lambda works.
W_35, W_70, W_140: no pair with both values nonzero; fully obstructed.
Lattice level. A = [[2,7],[7,7]], A^{-1} = [[-1/5,1/5],[1/5,-2/35]], discriminant group of order 35, level N = 70; tau -> -1/(7 tau) does not normalize Gamma_0(70).
Exact radial targets (Cat A). lim t * C(e^{2 pi i x} e^{-t}) = I G(x): I = 0.2094198... at x = 1; |I G| = I/sqrt7 = 0.079153... at x = 1/7, 3/7, 5/7.


5. Verdict

OBSTRUCTION. No scalar residual law (modular + o(1/t) remainder, theta prefactor/quotient, or scalar W_7 slash at any weight) exists in the scoped senses above.
The open route is VECTOR-VALUED (35 discriminant-group components, weight-1 Weil representation of the level-70 lattice). It is not excluded here and is Cat B / open.
Not claimed. C or C_third quantum modular; non-existence of a vector-valued law; that the Master samples are wrong (their prescription is unknown).


6. Hygiene

Pure copy-and-create; no existing file modified or renamed; no locks altered.
Cat A only here; Cat B in the separate notes. No HQCC, TPC or RH claim. Residual is not Resonant; 539 is a count. CORE_FREEZE untouched.
