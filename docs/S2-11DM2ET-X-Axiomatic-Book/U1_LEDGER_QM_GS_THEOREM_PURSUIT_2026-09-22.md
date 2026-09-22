U1-LEDGER-QM-GS-THEOREM-PURSUIT
Theorems the defining series forces, and the four Zagier pieces it still does not force
2026-09-22

Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.
Canonical T3 is the three-branch production map. Book HQCC is not that map.
Twin Prime and Riemann Hypothesis unclaimed.
This note is not a GS-ZWEGERS redo. This note is not a GS-QM redo. This note is not a RADIAL redo of f768a4f. This note is not a P-TL redo. This note is not U1-LEDGER-G7RAD as that ledger.
This note does not invent Slash_two, Object B, Nu_star, Coup_enc, or Tau_orbit as a modular weight.
This note does not treat H_s completion as QM of g_s.
This note does not treat g_1 or g_2 as g_7.


0. Attack object

Pursue for Theorem.

The standing name is quantum modularity of g_s. Success is still the 14 September pair:

(A) a written radial-limit identity that names g_7^rad as a locked Side A object, large enough for the cocycle with W_7 and Auto, or

(B) all four Zagier pieces for g_s: a specified subset of the rationals, a group, a weight, and an error of modularity nicer than g_s on that set.

Allowed decision (C). Write every theorem the defining series does force, and record that (A) and (B) stay unforced.

This ledger is (C) on (A) and on (B), together with four theorems that the series does force.


1. Written inputs. Nothing added

I1. g_s(q) = sum_{n >= 0} q^{n^2} / (-q^s ; q^s)_n.
Mixed scale. Square at scale 1. Pochhammer at scale s. Empty product at n = 0 is 1.

I2. Unfolded Pochhammer. (-q^s ; q^s)_n = prod_{k=1}^{n} (1 + q^{s k}).

I3. Identity G7R1-G7R5 of 21 September. g_7^circ on S7. Radial limits at seventh roots. First-term pole at q -> -1. Not rerun.

I4. NCR-g7 and NCR-C. Not rerun.

I5. Specializations already locked as ID1. g_1 = f_0. g_2 = phi.


2. Theorem PERIOD-2

Let m be odd and let rho be a primitive m-th root of unity. Then

prod_{k=1}^{m} (1 + rho^k) = 2.

Proof.
The product runs through every m-th root of unity exactly once.
The polynomial identity X^m - 1 = prod_{xi^m = 1} (X - xi) evaluated at X = -1 gives
(-1)^m - 1 = prod_{xi} (-1 - xi) = (-1)^m prod_{xi} (1 + xi).
m odd yields -1 - 1 = - prod (1 + xi), so the product equals 2.

Independent float check at m in {1,3,5,7,9,11,15} recovers 2 to machine precision. The identity is the proof. The float is not the proof.


3. Theorem G7-ODD

Let zeta be a root of unity of odd order. Write
G7odd(zeta) := sum_{n >= 0} zeta^{n^2} / (-zeta^7 ; zeta^7)_n.
Then the series converges absolutely, and

lim_{r -> 1-} g_7(r zeta) = G7odd(zeta).

Proof.
Let rho = zeta^7. The order m of rho divides the odd order of zeta, so m is odd.
No factor 1 + rho^k vanishes, because rho^k = -1 would force an even order.
By PERIOD-2 the partial products satisfy
|(-rho ; rho)_{N m}| = 2^N times a bounded function of the incomplete period.
Hence the general term is O(2^{-n/m}) and the series at r = 1 converges absolutely.

For 0 <= r < 1 the numerator r^{n^2} decays faster than any exponential. No factor 1 + (r zeta)^{7k} vanishes on [0,1]: a vanishing factor would require r^{7k} = 1 and zeta^{7k} = -1, which is the even-order case already excluded.
Each term a_n(r ; zeta) is therefore continuous on the compact segment [0,1].
Split the segment. On [0, r0] with r0 < 1 the bound r0^{n^2} is summable. On [r0, 1] the denominators stay comparable to the r = 1 denominators, which grow as 2^{n/m}, once r0 is close enough to 1 that no radius-to-zeta segment passes nearer to -1 than half the fixed gap |1 + rho^k|.
Weierstrass on the two pieces gives uniform convergence on [0,1]. The sum is continuous at r = 1. That is the radial limit.

This theorem enlarges G7R3 from S7 to every odd-order root. The name of the function is G7odd, not the Side A symbol g_7^rad.


4. Theorem G7-POLE

If zeta^{7k} = -1 for some integer k >= 1, then the factor 1 + zeta^{7k} vanishes and the defining series of g_7 is undefined at zeta.
In particular this holds whenever zeta^7 = -1, so at every primitive fourteenth root of unity.
Along the radius q = -r the n = 1 term is -r / (1 - r^7) and diverges as -1/(7(1-r)) when r -> 1-. That is G7R4, restated, not rerun.

W_7(2/5) = -5/14 lands on a fourteenth-root cusp. The set of odd-order roots is therefore not stable under W_7.


5. Theorem G7-CUBE

Let omega = exp(2 pi i / 3). Then
G7odd(omega) = 2 + 2 sqrt(3) i,
G7odd(omega^2) = 2 - 2 sqrt(3) i.

Proof.
rho = omega^7 = omega. The Pochhammer is periodic of period 3 with period product 2.
Write n = 3m, 3m+1, 3m+2.
The n = 3m term is 2^{-m}.
The n = 3m+1 term is 2^{-m} (-omega^2).
The n = 3m+2 term is 2^{-m} omega.
Sum over m >= 0:
G7odd(omega) = (sum_m 2^{-m}) (1 + omega - omega^2) = 2 (1 + omega - omega^2).
The cyclotomic identity 1 + omega + omega^2 = 0 rewrites the parenthesis as -2 omega^2.
Hence the value is -4 omega^2 = 2 + 2 sqrt(3) i.
Conjugation gives the value at omega^2.

This is a closed form. It is not a Fricke factor and it is not Auto.


6. Theorem SPEC-QM

g_1(q) = sum q^{n^2} / (-q ; q)_n is Ramanujan's fifth-order mock theta f_0.
g_2(q) = sum q^{n^2} / (-q^2 ; q^2)_n is Ramanujan's third-order mock theta phi.

Machine M1 applies to named mock thetas by published work after Zwegers completion.
A published vector-valued statement for the pair (q^{-1/24} phi, q^{-1/24} psi) exists in the mock-to-quantum literature (Bringmann-Rolen lineage; Hikami-type radial expansions).

Therefore quantum modularity of g_1 and of g_2 is a literature theorem after the Pack+(S) identification ID1.

This is not quantum modularity of g_s.
This is not quantum modularity of g_7.
f_0(q^7) is not g_7. Mixed scale stands.


7. What the four theorems do not write

Set. Odd-order roots of unity, or the rationals p/c with c odd under q = exp(2 pi i tau), is a set on which G7odd is defined. That set is not stable under W_7. A both-odd numerator-and-denominator subset is W_7-stable and T^2-stable. Stability of a set is not a group of g_7, and it is not an error formula.

Group. No Pack+(S) identity names Gamma_0(7), Gamma_1(7), SL_2(Z), or the Fricke extension as a transformation group of g_7 or of G7odd.

Weight. Auto(x) = |7x|^{-1/2} remains the classical candidate. G7-CUBE is not that weight. 2 + 2 sqrt(3) i is not 1/sqrt(7).

Error. The difference G7odd(x) - |7x|^{-1/2} G7odd(W_7(x)) cannot be formed at every point of the odd-order set, because W_7 sends some of those points to G7-POLE. No nicer extension is written.

(A) fails. g_7^rad as Side A symbol stays unwritten. G7odd is a larger restricted function than g_7^circ. It is still not Side A.

(B) fails. Zero of four Zagier pieces for g_s. Zero of four Zagier pieces for g_7.

QM of g_s stays CONJECTURE.


8. Numerical record, not a theorem of closed form

Fifth-root values of G7odd, truncated past n = 600.

k = 0: 2
k = 1: (2 + sqrt(5)) - i tan(pi/5)
k = 2: (2 - sqrt(5)) - i tan(2 pi/5)
k = 3: conjugate of k = 2
k = 4: conjugate of k = 1

The real parts match 2 +/- sqrt(5) to all printed digits. The imaginary parts match the elementary tangents to all printed digits. A period-5 algebraic proof on the same pattern as G7-CUBE is not written in this ledger. Do not treat the fifth-root line as a second closed-form theorem until that sum is reduced.

Seventh-root values remain the 21 September table. No elementary closed form is claimed.


9. Decision

Four theorems locked: PERIOD-2, G7-ODD, G7-POLE, G7-CUBE.
One literature theorem after identification: SPEC-QM, for s = 1 and s = 2 only.

The object named on 14 September, quantum modularity of g_s, is not among them.

Do not promote G7odd to g_7^rad.
Do not promote G7-CUBE to a cocycle.
Do not promote SPEC-QM to QM of g_7.
Do not treat 2, 2 sqrt(3), 2 + sqrt(5), or tan(pi/5) as Nu_star, G4, or COUNT 539.


10. Status after the attack

G7odd written on every odd-order root of unity.
g_7^circ remains the S7 special case.
g_7^rad as Side A symbol UNWRITTEN.
Zagier four pieces UNWRITTEN.
QM of g_s CONJECTURE.
QM of g_1 and of g_2 literature, after ID1.
NCR-g7 and NCR-C stand.
Path 2 stays empirical.
Per_off stays HEADER.
Object B UNOCCUPIED.
OccFilt_7 last 247.
Slash_two EMPTY.
PPT R unmet.
Five RH obligations open. RH unclaimed.
TPC unclaimed.
Nu_star EMPTY.
CORE_FREEZE unchanged.
No new residual-flux object.


11. Status codes

U1_LEDGER_QM_GS_THEOREM_PURSUIT_2026-09-22
THEOREM_PERIOD_2
THEOREM_G7_ODD
THEOREM_G7_POLE
THEOREM_G7_CUBE
THEOREM_SPEC_QM_G1_G2_ONLY
G7_RAD_SIDE_A_UNWRITTEN
ZAGIER_FOUR_PIECES_UNWRITTEN
QM_GS_STAYS_CONJECTURE
NCR_G7_STANDS
NCR_C_STANDS
NO_NEW_RESIDUAL_FLUX_OBJECT
TPC_UNCLAIMED
RH_UNCLAIMED
CORE_FREEZE_UNCHANGED

Packaging provenance Pack+(S) only. Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.
