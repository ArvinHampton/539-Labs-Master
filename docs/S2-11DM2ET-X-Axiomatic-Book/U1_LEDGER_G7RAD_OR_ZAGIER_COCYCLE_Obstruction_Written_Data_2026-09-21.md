U1-LEDGER-G7RAD-OR-ZAGIER-COCYCLE
Written radial-limit identity for g_7, or four-piece Zagier cocycle, from Pack+(S) data
2026-09-21

Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.
Canonical T3 is the three-branch production map. Book HQCC is not that map.
Twin Prime and Riemann Hypothesis unclaimed.
A count is not a clock. Residual is not Resonant.
This note is not a GS-ZWEGERS redo. This note is not a GS-QM redo. This note is not a RADIAL redo of f768a4f. This note is not a P-TL redo of NCR-g7 or NCR-C. This note is not a Path 2 cap. This note is not Per_off selector, Object B kernel, OccFilt7-INF, U7-as-C, or the RH five-lever.
This note does not invent Slash_two, Object B, Nu_star, Coup_enc, or Tau_orbit as a radial scale.
This note does not treat H_s completion as QM of g_s.
This note does not treat truncated samples as limits except where a continuous extension is proved.

0. Attack object

The 14 September close of U1-LEDGER-PATH2-OR-QM named the remaining close condition for QM of g_s:

A written radial-limit identity that names g_7^rad as a locked object, or a written Zagier cocycle with all four pieces, forced by Pack+(S) data.

Success criterion (A). Pack+(S) Category A lock of a function named g_7^rad on a set large enough to write the Side A cocycle

delta(x) = g_7^rad(x) - |7x|^{-1/2} g_7^rad(W_7(x))

with W_7(x) = -1/(7x), the error extending more nicely than g_7 off a specified set.

Success criterion (B). Pack+(S) Category A lock of all four Zagier pieces for g_s: a specified subset of the rationals, a group, a weight, and an error of modularity nicer than g_s on that set.

Allowed decision (C). A Pack+(S) obstruction that those two objects are still not forced, together with any restricted identity that the defining series does force.

This ledger is (C) on (A) and on (B), and a restricted identity on seventh roots of unity only.

Parent. U1_LEDGER_PATH2_OR_QM_Obstruction_Written_Data_2026-09-14. Ranked next from that wrap: a written radial-limit identity or a written Zagier cocycle not then on Master.

1. Written inputs. Nothing added

I1. Definition of g_s, locked.

g_s(q) = sum_{n >= 0} q^{n^2} / (-q^s ; q^s)_n

Mixed scale. Square at scale 1. Pochhammer at scale s. Not f_0(q^s).
The empty product at n = 0 is 1.

I2. Unfolded Pochhammer.

(-q^s ; q^s)_n = prod_{k=0}^{n-1} (1 + q^{s(k+1)}) = prod_{k=1}^{n} (1 + q^{s k})

I3. Euler identity, residue vanishing, NCR-g7, NCR-C, H_s Zwegers-completable. Already locked. Not rerun. Not used as a cocycle.

I4. Side A of P-TL. Already blocked because the symbol g_7^rad was not among the locked objects. This note asks whether the defining series itself now supplies that symbol.

I5. Auto(x) = |7x|^{-1/2}. Classical weight-1/2 Fricke factor. Auto_prod_W7 = 1/sqrt(7). residual_slash is not Auto. Not a derived weight for g_s.

I6. Convention A versus B for nome q = exp(2 pi i tau) versus q = exp(pi i tau) stays unselected. This note uses q = exp(2 pi i tau) only as a letter to name seventh roots. It does not select Per_off.

2. Restricted identity that is forced

Identity G7R1. Candidate on seventh roots.

Let S7 = { zeta : zeta^7 = 1 }. Write zeta_m = exp(2 pi i m / 7) for m = 0, ..., 6.

Define

g_7^circ(zeta) := sum_{n >= 0} zeta^{n^2} / 2^n

The series converges absolutely on S7 because |term| = 2^{-n}.

g_7^circ(1) = sum_{n >= 0} 2^{-n} = 2 exactly.

Numerical values of the same series, truncated past n = 80, for the record. Not a theorem of closed form except at 1.

m = 0: 2
m = 1: 1.0344483879 + 0.4675538041 i
m = 2: 0.8987086488 + 0.6462831955 i
m = 3: 0.5944020184 - 0.1986223121 i
m = 4: 0.5944020184 + 0.1986223121 i
m = 5: 0.8987086488 - 0.6462831955 i
m = 6: 1.0344483879 - 0.4675538041 i

Conjugation g_7^circ(zeta_{7-m}) = conjugate g_7^circ(zeta_m) is forced by the real coefficients of the series.

Identity G7R2. Why the candidate is the termwise radial value.

Let zeta^7 = 1 and set q = r zeta with 0 <= r <= 1.

Then q^{7k} = r^{7k} zeta^{7k} = r^{7k}.

Therefore

(-q^7 ; q^7)_n = prod_{k=1}^{n} (1 + r^{7k})

which is real, independent of which seventh root is chosen, and equals 2^n at r = 1.

The general term of g_7(r zeta) is

a_n(r; zeta) = (r zeta)^{n^2} / prod_{k=1}^{n} (1 + r^{7k})

At r = 1 this is zeta^{n^2} / 2^n, the general term of g_7^circ.

Identity G7R3. Radial limit exists at every point of S7 and equals g_7^circ.

Each a_n(r; zeta), defined at r = 1 by G7R2, is continuous on the segment [0, 1].

Let f_n(r) = r^{n^2} / prod_{k=1}^{n} (1 + r^{7k}) for n >= 1, and f_0 = 1. Then |a_n(r; zeta)| = f_n(r).

f_n attains a maximum M_n on [0, 1]. The maxima are summable:

Regime 1. If r <= exp(-1/n) then f_n(r) <= exp(-n).

Regime 2. If r > exp(-1/n) then for every k = 1, ..., floor(n/14) one has r^{7k} > exp(-7k/n) >= exp(-1/2). Each of those factors is at least 1 + exp(-1/2). Hence

f_n(r) <= (1 + exp(-1/2))^{-floor(n/14)}

Both regimes decay at least exponentially in n. Therefore sum_n M_n < infinity.

Weierstrass M-test: sum_n a_n(r; zeta) converges uniformly on [0, 1]. The sum is continuous on [0, 1]. In particular

lim_{r -> 1-} g_7(r zeta) = g_7^circ(zeta)

for every zeta in S7.

This is the written radial-limit identity on S7. The name of the restricted function is g_7^circ, not the Side A symbol g_7^rad.

Identity G7R4. First-term pole at q -> -1.

Let q = -r with 0 < r < 1. Then q^7 = -r^7 and the n = 1 factor of the Pochhammer is

1 + q^7 = 1 - r^7

The n = 1 term of g_7(-r) is

(-r) / (1 - r^7)

As r -> 1- one has 1 - r^7 ~ 7(1-r), so the term is asymptotic to -1 / (7(1-r)) and diverges to minus infinity.

At q = -1 exactly the same factor is 1 + (-1)^7 = 0. The Pochhammer vanishes for every n >= 1. The defining series is undefined at -1.

Partial sums of g_7(-r) grow in magnitude with r. This is not a finite radial value.

Identity G7R5. Why -1 is required for Side A.

W_7(x) = -1/(7x).

The seventh-root cusps in the letter tau with q = exp(2 pi i tau) are x = m/7 for m = 0, ..., 6.

W_7(1/7) = -1.

A Side A value delta(1/7) names g_7^rad(-1). G7R4 says that name is not a finite number built from the defining series.

W_7(2/7) = -1/2, W_7(3/7) = -1/3, W_7(0) = infinity. None of those points lies in {m/7}. S7 is not stable under W_7.

3. Decision

(A) fails. g_7^rad as used in Side A is still not a locked object. What is locked is the restricted function g_7^circ on S7, together with existence of ordinary radial limits at those seven points. Side A needs values at Fricke partners, beginning at -1, where the same series diverges.

(B) fails. The four Zagier pieces are not written.

Set. The only set on which a radial value is now forced is S7, or the seven rationals {0, 1/7, ..., 6/7} under the letter q = exp(2 pi i tau). That set is not stable under W_7 and is not a named congruence-subgroup orbit.

Group. No Pack+(S) identity names Gamma_0(7), SL_2(Z), or the Fricke extension as a transformation group of g_7 or of g_7^circ.

Weight. Auto(x) = |7x|^{-1/2} remains the classical candidate. It is not derived from g_7^circ. residual_slash is not that weight.

Error. The difference g_7^circ(x) - |7x|^{-1/2} g_7^rad(W_7(x)) cannot be formed at x = 1/7 because the second term is not a number. No nicer extension is written.

QM of g_s stays CONJECTURE.

This is data-closure of the exact close condition named on 14 September. It is not a proof that no later identity on a larger set could exist. It is not occupancy of a new residual-flux object.

4. Identities that lock continued status

R1. g_7^circ is a function of seven points. It is not g_7^rad on Q, and it is not a quantum modular form.

R2. Existence of lim_{r -> 1-} g_7(r zeta) for zeta^7 = 1 is an ordinary radial limit along the radius. It is not a mock-to-quantum implication. NCR-g7 still forbids that route.

R3. The denominator on S7 collapses to 2^n because q^7 = 1, not because a lattice character absorbed the Pochhammer. T3 of NCR-g7 stands.

R4. Independence of the denominator from the choice of seventh root is not a transformation law under W_7.

R5. Value 2 at q = 1 is the geometric series sum 2^{-n}. It is not Auto(1), not G4, not COUNT 539, and not mu = 1.55.

R6. Divergence at -1 is a first-term pole from the factor 1 + q^7. It is not a sample. It is not a finite convention-A or convention-B tail.

R7. A unary quantum-modular theorem for C_axis, if later written, would still not be QM of g_s and would still not supply g_7^rad(-1).

R8. Dual_Abel_off remains a third kernel with raw h unstored. It is not g_7^circ and not the Side A cocycle.

R9. residual_slash four-point products under W_7 remain 2130.27, 104.94, 490.83, 1119.82 against 1. Those numbers are Object A sample magnitudes of C, not radial values of g_7.

5. Obstructions

OZ1. Domain obstruction.
A Zagier set must be large enough that the group action used in the error formula lands back in the domain, or at least lands where the function is defined as a number. S7 fails that test for W_7.

OZ2. Partner obstruction.
The first Fricke partner of 1/7 is -1. The defining series of g_7 has a first-term pole along q = -r, r -> 1-. No Pack+(S) regulator, Abel sum, or incomplete-gamma tail is written that turns that pole into a finite g_7^rad(-1). Inventing a regulator would be a new construction, not a recognition, and would reopen the Per_off convention problem under another name.

OZ3. Four-piece obstruction.
Zero of four Zagier pieces is forced for g_s. One restricted set with finite radial values is written. A set is not a group, a weight, and an error.

OZ4. Class-route obstruction, restated not rerun.
NCR-g7 forbids the classical mock realisation that would have licensed radial limits at the remaining cusps by published implication. L1, L2, L3 stay failed. This note does not rerun them.

6. What this pass does not do

It does not claim quantum modularity of g_s.
It does not claim a transformation law.
It does not revive 25ed7ea.
It does not reopen GS-ZWEGERS, GS-QM, or RADIAL as those ledgers.
It does not treat g_7^circ as Object B or as Slash_two.
It does not select Convention A versus B.
It does not store Dual_Abel raw h.
It does not claim Twin Prime or Riemann Hypothesis.
It does not treat 2, 7, 539, 247, or G4 as a modular weight or as a radial scale.
It does not identify g_7^circ(1) = 2 with any master-equation constant.

7. Status after the attack

g_7^circ written on S7. Radial limits exist at the seven points and equal g_7^circ.
g_7^rad as Side A symbol UNWRITTEN.
Zagier four pieces UNWRITTEN.
QM of g_s CONJECTURE.
NCR-g7 and NCR-C stand.
Path 2 stays empirical.
Per_off stays HEADER.
Object B UNOCCUPIED.
OccFilt_7 last 247. Infinity unproved.
Slash_two EMPTY.
PPT R unmet.
Five RH obligations open. RH unclaimed.
TPC unclaimed.
Nu_star EMPTY. Coup_enc EMPTY. Scale_5 EMPTY.
CORE_FREEZE unchanged.
No new residual-flux object.

8. Ranked next from written data

A published RH bound that is not a rescaling of c1.
PPT R if constructed.
A new regulator that makes g_7(-r) have a finite limit, which is not on Master today and is not Per_off by fiat.
A new group-and-error identity on a set larger than S7, which is not on Master today.

Closing QM of g_s now still requires an identity that is not among the locked objects. The S7 identity is not that identity.

9. Status codes

U1_LEDGER_G7RAD_OR_ZAGIER_COCYCLE_OBSTRUCTION_WRITTEN_DATA_2026-09-21
G7_CIRC_WRITTEN_ON_S7
RADIAL_LIMIT_EXISTS_ON_S7_EQUALS_G7_CIRC
G7_RAD_SIDE_A_UNWRITTEN
FIRST_TERM_POLE_AT_MINUS_ONE
ZAGIER_FOUR_PIECES_UNWRITTEN
QM_GS_STAYS_CONJECTURE
NCR_G7_STANDS
NCR_C_STANDS
NO_NEW_RESIDUAL_FLUX_OBJECT
TPC_UNCLAIMED
RH_UNCLAIMED
CORE_FREEZE_UNCHANGED

Packaging provenance Pack+(S) only. Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.
