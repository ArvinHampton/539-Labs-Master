U1-LEDGER-P-TL
No classical mock-modular realisation of g_7 or of C under Pack+(S)
2026-09-01

PURE MATH. Residual Discrete Algebra is leftover combinatorics after flux packaging (4880, seed 21, nine sector cores of size 539). That 539 is a COUNT of leftover pieces, not a journey length. Resonant Algebra is the choice to treat 18+521=539 as a HARD SCHEDULE. A count is not a clock. Do not flatten Residual into Resonant. Do not treat 539 as a free-map stop.

This note is not GS-ZWEGERS, not GS-QM, not RADIAL, not TL-AUDIT, not BRIDGE-C, not P-SLASH. Named E1-E4 / GS-ZWEGERS / GS-QM / RADIAL / TL-AUDIT / LOCK-AUDIT / BRIDGE-C / NEWOBJ-END / NEC / 3ADIC / XFER / 2ADIC / XFER2 / 5ADIC / XFER5 / P-SLASH redos are forbidden. Transformation-law theorem 25ed7ea and unsigned=Euler stay killed. Theorem 8.4 is Object A only. residual_slash is not Auto_prod_W7. residual_slash is not Phi_res seed-clear. residual_slash is not leftover COUNT 539. Object B stays unclaimed. Twin Prime and RH stay unclaimed. Free T3 stays short (4880 to 1 in 14). Continuum Category B. Op_L / Op_T / Op_AM stay empty. Do not invent another p-adic Dom_res. Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE and Discrete Core Freeze hold.

Parent lock on Master: a5db06c U1-LEDGER-P-SLASH Remark 8.5. This note does not reopen that ledger. It closes the next lever named for P-TL-g and P-TL-C in the 1 September five-item status: a residual obstruction showing no classical mock-modular realisation exists under Pack+(S), written as a theorem.

Scope of the word classical. Rank-two Z-module, quadratic form of signature (1,1), finite-image lattice character, one Zwegers cone pair, holomorphic projection equal to the named series. Appell-Lerch paths L1 L2 L3 stay separately locked negative and are not reopened. Quantum modularity of g_s stays unforced (517acae). Radial limits stay unavailable as a theorem (f768a4f). No fifth parameter. No Maass-Poincaré. No solar operator.


0. Attack and dichotomy

Attack object. P-TL-g and P-TL-C. One object, two sides of the same dichotomy, under Pack+(S) only.

Written data used, already locked.

g_s(q) = sum_{n>=0} q^{n^2} / (-q^s ; q^s)_n
Mixed scale. Quadratic exponent at scale 1. Pochhammer at scale s. Not f_0(q^s).

Euler identity (locked, residual-adapted).
P_s(q) := (-q^s ; q^s)_infty * g_s(q)
= sum_{k>=0} [ q^{s k(k+1)/2} / (q^s ; q^s)_k ] * sum_{n>=0} q^{n^2 + s k n}

Residue vanishing (locked). Coefficients of g_s vanish off squares modulo s. For s=7 the surviving classes are {0,1,2,4}.

Quadratic form of the double-sum (locked).
Q_s(n,k) = n^2 + s k n + (s/2) k(k+1)
Homogeneous matrix B_s = [[1, s/2],[s/2, s/2]], det B_s = s(2-s)/4 < 0 for s>2. Signature (1,1).
Cleared-denominator matrix M_s = [[2,s],[s,s]], det M_7 = -35.

Bridge Series C (locked definition).
P_orth := unsigned orthant sum of q^{Q_s} over n,k >= 0.
H_s := cone-signed series with locked negative-norm cones (s=7: c_1=(-1,1), c_2=(-4,1)) and sign-weight w.
C := P_orth - H_s.
C is the orthant/cone mismatch. C is not Euler P_s. Unsigned=Euler stays killed.

residual_slash (locked Object A). Four-parameter interpolant of C sample magnitudes at x in {1/7, 3/7, 5/7, 1}. Theorem 8.4 is that four-point one-sided reconstruction. Auto(x) = |7x|^{-1/2}. Auto_prod_W7 = Auto(x) Auto(W_7(x)) = 1/sqrt(7) exactly. residual_slash is not Auto. Interp_prod_W7 is not identically sqrt(7). Object B cannot be residual_slash.

Dichotomy for s=7, using only Euler double-sum plus residue vanishing, without reopening GS-ZWEGERS / GS-QM / RADIAL / TL-AUDIT.

Side A. Exhibit a written cocycle
delta(x) = g_7^rad(x) - |7x|^{-1/2} g_7^rad(W_7(x))
that extends continuously off a specified set of order-7 roots.

Side B. Prove that the mixed-scale Pochhammer weights 1/(q^7 ; q^7)_k cannot be absorbed into any lattice character on a signature-(1,1) module whose Zwegers / indefinite-theta holomorphic projection recovers g_7.

C-side analogue allowed as the same dichotomy: C in place of g_7, residual_slash in place of Auto. Not a second transformation-law redo. Not a P-slash redo.

Decision. Side A is blocked. Side B is the theorem.


1. Why Side A cannot be written from the allowed input

The symbol g_7^rad is the radial limit of g_7 as q approaches a root of unity from inside the disk. RADIAL lock f768a4f already records that those limits are unavailable as a theorem from the Euler double-sum and residue vanishing. QM lock 517acae already records that a Zagier cocycle is not forced by the same input.

Side A asks for a written continuous function built from g_7^rad. That function is not among the locked objects. Inventing it would reopen RADIAL. Truncated numerical samples toward seventh roots (finite-looking) and toward -1 (divergent-looking) are samples, not limits, and are not a cocycle.

Therefore the dichotomy closes on Side B. This is not a new radial analysis. It is the observation that Side A names an object the allowed input does not supply.


2. Theorem (no classical realisation of g_7)

Theorem NCR-g7.
Let s=7. There does not exist a rank-two Z-module L equipped with a quadratic form Q of signature (1,1), a lattice character psi on L with values in a finite subgroup of C^*, and a Zwegers cone pair C such that the holomorphic projection of the associated indefinite theta recovers g_7.

In particular the mixed-scale Pochhammer weights 1/(q^7 ; q^7)_k of the locked Euler double-sum cannot be absorbed into any such psi.

This is an upgrade of the 1d8e558 shape obstruction to a no-classical-realisation statement. It does not reopen GS-ZWEGERS. It does not claim quantum modularity. It does not revive 25ed7ea.


3. Proof of Theorem NCR-g7

Write L for a hypothetical rank-two Z-module, Q a quadratic form of signature (1,1) on L, psi a character L -> C^* of finite image, and C a pair of opposite cones in L tensor R of the Zwegers type. Write Theta_hol for the holomorphic projection of the Zwegers indefinite theta of (L, Q, psi, C). Assume Theta_hol = g_7 and derive a contradiction from locked identities only.

Identity T1 (shape of a classical holomorphic projection).
By the definition of the Zwegers construction, Theta_hol is a cone-restricted lattice series
sum_{v in L cap cone} psi(v) q^{Q(v)}
up to the standard finite correction at the cone walls. Every coefficient is a finite sum of values of psi, hence a finite sum of roots of unity. The support at degree N is a set of lattice points of Q-value N inside the cone.

Identity T2 (shape of g_7).
g_7(q) = sum_{n>=0} q^{n^2} / (-q^7 ; q^7)_n.
The n=0 term is 1. For n>=1 the denominator is a finite product of geometric factors 1/(1 + q^{7j}). Expanding those factors produces an auxiliary partition index that is not a coordinate on any rank-two module. The resulting coefficients of g_7 are ordinary integers whose generating mechanism is mixed-scale: a square at scale 1 multiplied by a scale-7 partition generating function. Residue vanishing restricts the degrees to {0,1,2,4} mod 7. It does not remove the auxiliary index.

Identity T3 (Pochhammer is not a lattice character).
A lattice character psi is a function of the lattice vector alone and takes values of modulus one. The weight 1/(q^7 ; q^7)_k in the Euler double-sum is a formal power series in q^7 whose coefficients grow with the partition function of parts in {7, 14, ..., 7k}. That weight is not a unimodular function of a pair (n,k). It cannot be rewritten as psi(n,k) for any character on any rank-two module, because doing so would require the auxiliary partition index of the Pochhammer expansion to be a function of (n,k). It is an extra summation index.

Identity T4 (three series on the same form stay distinct).
On the locked form Q_7 three generating functions are already named and are not identified.

Euler P_7 = (-q^7 ; q^7)_infty * g_7
= the weighted double-sum of T2 after multiplying by the Euler product.

P_orth = sum_{n,k >= 0} q^{Q_7(n,k)}
the unsigned orthant sum.

H_7 = sum_v w(v) q^{Q_7(v)}
the cone-signed series of the locked pair c_1, c_2.

C = P_orth - H_7 is not the zero series. Coefficients of C through the locked range take values in {0, 1, 1.5}, with axis contribution 1/2 and origin 1.5. Unsigned=Euler is killed: Euler P_7 is not P_orth. Therefore Euler P_7 is not H_7 either.

Identity T5 (what a Zwegers projection on this lattice can recover).
The only Zwegers-completable holomorphic series attached to (M_7, c_1, c_2) in the locked corpus is H_7. That is the content of the Bridge C definition, not a new construction. Completing H_7 does not complete P_orth, because C is the difference. Completing H_7 does not complete Euler P_7, because Euler P_7 is not P_orth and is not H_7. Dividing a completion of H_7 by (-q^7 ; q^7)_infty therefore does not recover g_7.

Identity T6 (scale mismatch survives every rank-two rewrite).
Q_7(n,k) = (n + 7k/2)^2 - (35/4) k^2 + (7/2) k.
The completed-square form still has the square at scale 1 and the hyperbolic term at discriminant 35, which is scale 7. The Pochhammer that multiplies the inner n-sum remains at scale 7. No change of basis of a rank-two module mixes a scale-1 square with a scale-7 Pochhammer into a single lattice character. A level insertion f_0(q^7) would put the square at scale 7 as well. g_7 is not that insertion.

Contradiction.
T1 requires Theta_hol to be a character-weighted cone series on a rank-two module.
T2 and T3 say g_7 is not of that shape: the Pochhammer supplies an extra index that is not a character.
T4 and T5 say that even the nearest locked lattice series on the form that g_7 actually uses, namely H_7 on M_7, recovers neither Euler P_7 nor g_7.
T6 says no other rank-two form built from the same Euler data removes the scale mismatch.
Hence no such (L, Q, psi, C) exists.

The argument uses only the Euler double-sum, residue vanishing, the killed unsigned=Euler identification, and the locked definition C = P_orth - H_s. It does not use radial limits. It does not use residual_slash. It does not use leftover COUNT 539.


4. Theorem (no classical realisation of C)

Theorem NCR-C.
Let s=7. The residual bridge series C = P_orth - H_s is not the holomorphic part of a classical mock-modular form on a congruence subgroup whose Fricke factor is Auto(x) = |7x|^{-1/2}. The locked four-point interpolant residual_slash is not that Fricke factor and is not a classical mock-modular realisation of C off the four samples {1/7, 3/7, 5/7, 1}.

This is the C-side analogue of Theorem NCR-g7. It is not a P-slash redo. Remark 8.5 stays the gap between Object A and Object B. Object B stays unclaimed.


5. Proof of Theorem NCR-C

Identity U1 (definition of C).
C records the mismatch between the coordinate orthant and the Zwegers cones on the same lattice. Interior orthant points have w=1 and cancel. Axes contribute 1/2. Exterior points with w=-1 contribute +1. Origin contributes 1.5. C is not a cone series and is not an orthant series.

Identity U2 (classical factor versus locked interpolant).
Auto(x) Auto(W_7(x)) = 1/sqrt(7) as an identity of functions. residual_slash(x) = Auto(x) * residual_factor(x) with residual_factor the locked four-parameter interpolant. At the four samples the products residual_slash(x) residual_slash(W_7(x)) are 2130.27, 104.94, 490.83, 1119.82 against the value 1 that a two-sided classical law would need. Interp_prod_W7 at those samples is 5636.16, 277.64, 1298.61, 2962.76 against sqrt(7) ≈ 2.645751. Those evaluations are already locked. They are used here only as the C-side analogue of Auto, not as a new uniqueness claim.

Identity U3 (Object A is not a mock-modular law).
Theorem 8.4 reconstructs the four sample magnitudes of C from residual_slash. That is a four-point identity. A classical mock-modular realisation would be an identity of functions on a congruence subgroup, or at least an identity of functions off those four points under W_7. residual_slash fails that identity on every written residual-rational grid. Object B families inside the same four-parameter ansatz are disjoint from Object A. Dual-split implied slashes are two-sided by construction and miss residual_slash off the samples.

Identity U4 (H_s is the classical piece; C is the leftover).
H_s is the series the Zwegers cones actually produce. C is what remains after subtracting H_s from the orthant. Treating C as if it were itself a Zwegers holomorphic projection would require the mismatch to vanish. The mismatch is the definition of C.

Contradiction with a classical Auto-realisation.
If C were mock-modular with Fricke factor Auto, the two-sided product under W_7 would be the classical Auto_prod_W7 identity up to the usual weight. residual_slash would then have to be Auto, or a two-sided factor in the Object B class. U2 and U3 forbid both. U1 and U4 forbid absorbing C into H_s.

What is not claimed.
Uniqueness of residual_slash as a function on the line is not claimed.
A two-sided residual factor outside the four-parameter family is not claimed.
A residual quantum-modular law for C off the samples is not claimed.
Those remain the P-slash / P-Xi ledger, not this theorem.


6. What the two theorems close, and what they do not

Closed under Pack+(S), Category A residual discrete.

- Side A of the P-TL dichotomy cannot be written from Euler plus residue vanishing.
- g_7 admits no classical mock-modular realisation as the holomorphic projection of a Zwegers indefinite theta on a signature-(1,1) module.
- The mixed-scale Pochhammer weights cannot be absorbed into a lattice character on any such module.
- C admits no classical mock-modular realisation whose Fricke factor is Auto.
- residual_slash is not that realisation off the four samples.

Still open, and not reopened by this note.

- Quantum modularity of g_s as a residual statement. 517acae stands: not forced by Euler plus residue vanishing. Long paths L1, L2, L3 did not close it.
- Residual law for C off the four samples. Object A remains the sample-point law. Remark 8.5 remains the gap.
- P-g7-inf. Last missing allowed degree 247. No infinitude claim.
- P-Xi off-sample Eichler.
- Path 2 density. Not used. Not a theorem.
- Path 4 family for C. An identity Q-difference 2 on residues (2,4) mod 7. Not a mock-modular law.
- PW(7,11;3^5). Integer pattern. Not a functor and not a realisation of g_s.

Killed as theorems, stay killed.

- 25ed7ea Residual_Transformation_Law.
- Transformation_Law_CLOSED wording.
- unsigned = Euler.
- The "Modular Connection" paragraph of Series_g_s_Locked_Material_2026-08-22, which treated the orthant sum of Q_s as already Zwegers-completed to a weight-1/2 form whose holomorphic part recovers P_s and then g_s. That paragraph is superseded by T4, T5, Theorem NCR-g7, and the locked definition of C. The orthant sum is P_orth. The Zwegers holomorphic piece on the locked cones is H_s. Their difference is C. None of those three series is g_s.


7. Review of missed variables, correlations, patterns, contradictions

Against End_res O1.
End_res := Z[D5 x C2] is the residual endomorphism ring of Jac(C/Q4). Its units are finite order. A lattice character on (Z^2, Q_7) is a different object: it is a homomorphism from an indefinite lattice, not from End_res. Identifying a Pochhammer weight with an End_res unit would mix a power-series coefficient with a finite-order automorphism of an abelian surface. Refused.

Against NecMono X7.
NecMono_res records finite-order generators only and forbids a residual real-multiplication unit. The Pell unit 6+sqrt(35) of discriminant 35 is an automorphism of the form M_7. It is used in the exterior-survival lemma for C_third. It is not a character that absorbs 1/(q^7 ; q^7)_k, and it is not an RM unit of End_res. Those three uses of "unit" stay separate.

Against Dom_res^(p) E3-stand.
Dom_res^(3), Dom_res^(2), and Dom_res^(5) are finite residue images of the leftover set I. E3-stand forbids reading them as compact open p-adic domains. The Pochhammer 1/(q^7 ; q^7)_k is a formal series, not a function on those nine-point or five-point sets. A Dom_res^(7) would be another p-adic copy of Dom_res. Forbidden. Not defined.

Against XferPot labels.
Phi_res, Psi_res, and Chi_res take values in finite subsets of I. Those values are leftover COUNTs. Auto(x) = |7x|^{-1/2} is a real function of a Fricke coordinate. residual_slash is a real interpolant. Neither is a COUNT. 539 is leftover COUNT L_pack = 7^2 * 11. It is not a W_7 period, not a 5-adic radius, and not an automorphy factor.

Against R1.
Residual P stays S5. Q4 stays imported D5. No P <-> Q4. The quadratic form Q_7 is the path quadratic of the Euler double-sum. It is not the model polynomial of Q4 and is not a map from P.

Against C = P_orth - H_s.
That mismatch is the C-side object of this note. Collapsing C into H_s, into Euler P_7, or into a lattice character, would erase the definition. The pattern across the two theorems is the same pattern: a nearby series on the same lattice is not the series that was asked for.

Real correlations that must not be collapsed.

Level 7 appears as s=7, as W_7, as sample denominators k/7, and as the Pochhammer base q^7. That is packaging type. It is not leftover COUNT 539, not 4880, not 521.

Discriminant 35 appears as det M_7, as the completed-square outer series of Xi, and as Q(sqrt(35)). Same integer. Not a Zwegers form for g_7, because the Pochhammer is still there.

Residue filter {0,1,2,4} mod 7 is shared by g_7 and by C. Shared support is not shared identity. A zero of one is not a zero of the other.

t = 7x - 3 is a coordinate on the real line for residual_slash. It is not a point of Dom_res^(3). chi_nat(7) = (7/10, -1/5) is a different use of the numeral 7.

Contradictions if the correlations are collapsed.

If Euler P_7 were P_orth, C would have to vanish after multiplying by the Euler product. C does not vanish.

If residual_slash were Auto, residual_factor would be identically 1. Sample factors are 19.80, 3.16, 20.67, 55.30.

If residual_slash were leftover COUNT 539, the Interp_prod_W7 values 5636, 278, 1299, 2963 would have to be packaging integers. They are not.

If the Pochhammer were an End_res unit, it would have finite order. The series 1/(q^7 ; q^7)_k is infinite.

If a new residual-flux object were required to close the dichotomy, it would have to be something other than another p-adic Dom_res. No such object is required. The theorems are negative existence results from locked series.


8. Hygiene

Do not put N_flux, f_max, 18+521 as a schedule, fibre 67/68, G_4, or free T3 termination into the q-series theorem. 539 remains leftover COUNT. Residual Discrete Algebra is leftover pieces. Resonant Algebra is how long you stir. Free T3 short. Continuum Category B. Twin Prime unclaimed. Riemann Hypothesis unclaimed. Residual-flux provenance mandatory. CORE_FREEZE holds.

Status code: U1_LEDGER_P_TL_NO_CLASSICAL_REALISATION_G7_C_2026-09-01
SIDE_A_BLOCKED_BY_RADIAL
THEOREM_NCR_G7
THEOREM_NCR_C
POCHHAMMER_NOT_A_LATTICE_CHARACTER
UNSIGNED_EULER_STAYS_KILLED
SERIES_GS_MODULAR_CONNECTION_SUPERSEDED
RESIDUAL_SLASH_NOT_AUTO
OBJECT_B_UNCLAIMED
NO_NEW_P_ADIC_DOM_RES
539_LEFTOVER_COUNT
