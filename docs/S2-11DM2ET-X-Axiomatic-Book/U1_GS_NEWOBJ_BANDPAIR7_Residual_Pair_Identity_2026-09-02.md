U1-GS-NEWOBJ-BANDPAIR7
BandPair_7 residual pair identity on residue-2 n-layers of g_7
2026-09-02

PURE MATH. Residual Discrete Algebra is leftover combinatorics after flux packaging (4880, seed 21, nine sector cores of size 539). That 539 is a COUNT of leftover pieces, not a journey length. Resonant Algebra is the choice to treat 18+521=539 as a HARD SCHEDULE. A count is not a clock. Do not flatten Residual into Resonant. Do not treat 539 as a free-map stop.

This note defines ONE new residual-flux object: BandPair_7. It is not a P-g7-inf redo, not an OccFilt_7 redo, not a LayerFilt_7 redo, not a Dom_res copy, not Comp_7, not TPC, not Path 2 density, and not Path 4 twin-pairs. Object B unclaimed. Twin Prime and RH unclaimed. Continuum Category B. Free T3 stays short (4880 to 1 in 14). Op_L / Op_T / Op_AM stay empty. P-PW, P-Xi, P-TL, and P-slash stay closed and are not reopened. 247 is LastMiss_7(2), not leftover COUNT 539. Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.

Parent locks: 85b082a U1-LEDGER-P-g7-inf (OccFilt_7 and LayerFilt_7 defined; BandPair_7 unnamed); OccFilt_7_Occupancy_Filter_Definition_2026-09-02.md; LayerFilt_7_Four_Layer_Residue2_Window_2026-09-02.md; Pg7inf_Hygiene_Companion_I_End_NecMono_Fibres_2026-09-02.md. Written gap under Pack+(S): LayerFilt_7 already records residue-2 n-layers as pairs (7k+3, 7k+4) for k >= 0 and states explicitly "Not BandPair_7 unless Lucas identity is written" / "BandPair_7 unnamed" / "BandPair_7 not invented." This note writes that identity.


1. Why a third residual-flux object on g_7

OccFilt_7 records finite-cap occupancy of allowed classes. LayerFilt_7 is the four-layer window identity

S(t) := phi_3(t-1) + phi_4(t-2) + phi_10(t-14) + phi_11(t-17)

equal to g_7(7t+2) on the exact window 121 <= d <= 282. Those four phi terms are already two consecutive n-layer pairs: (3,4) and (10,11). LayerFilt_7 uses the pairs. It does not name the pair as an object and does not write the identity that makes (7k+3, 7k+4) one residual-flux unit for every k >= 0.

BandPair_7 is that unit. The identity is Pack+(S)-only. No new p-adic domain is introduced. No new leftover integer is introduced.


2. Written pair language already on Master

From LayerFilt_7:

Squares modulo 7 that equal 2 are n ≡ 3 (mod 7) and n ≡ 4 (mod 7). Those are the only n-layers that can occupy residue 2.

Layer pairs: (3,4), (10,11), (17,18), (24,25), ... that is (7k+3, 7k+4) for k >= 0.

Exactness window. n=11 starts at d=121. Next residue-2 layers are n=17 at d=289 and n=18 at d=324. Therefore S(t) equals g_7(7t+2) for every t with 17 <= t <= 40, that is 121 <= d <= 282.

S(t) = 0 at exactly three values of t in 17..40: t=19 d=135, t=27 d=191, t=35 d=247. Those three degrees are Miss7_tail union the last triple. After t=35, still inside the exact window: d=254,261,268,275,282 with S = -3,6,-2,3,-5. Those five degrees are occupied by the 4-layer identity itself.

From OccFilt_7:

LastMiss_7(2) = 247. OccFilt_7(r ; 2500) = 1 and OccFilt_7(r ; 12000) = 1 for every allowed r in {0,1,2,4}. OccFilt_7(r ; infty) is not proved.

Miss7_tail = {135, 191, 247} has common difference 56 = 8 * 7. AP56 after 247 is occupied in every written cap as a specialisation of OccFilt_7(2 ; N), not a generating function, and not OccFilt_7(2 ; infty).

Squares mod 7: 0^2=0, 1^2=1, 2^2=4, 3^2=2, 4^2=2, 5^2=4, 6^2=1. Residue 2 is occupied by n-layers if and only if n lives in some pair (7k+3, 7k+4).


3. Definition of BandPair_7

For each integer k >= 0 set

n_L(k) := 7k + 3
n_R(k) := 7k + 4

BandPair_7(k) is the ordered pair (n_L(k), n_R(k)).

Pack+(S) pair identity. The three writings below are one identity:

(BP7-1) n_R(k) - n_L(k) = 1
(BP7-2) n_L(k) + n_R(k) = 7(2k+1)
(BP7-3) n_R(k)^2 - n_L(k)^2 = 7(2k+1)

(BP7-3) is (BP7-1) times (BP7-2). The odd conductor of pair k is

cond(k) := 2k + 1.

The degree gap between the two layers of pair k is exactly 7 cond(k). That gap is the only arithmetic that places both layers of one pair on the same residue-2 degree of g_7.

Two-term evaluation. Write g_7(d) = sum_n phi_n((d - n^2)/7), summed over n with n^2 <= d and d - n^2 divisible by 7, as already written in LayerFilt_7. On a residue-2 degree d = 7t + 2 with d >= n_L(k)^2 set

m_k(d) := (d - n_L(k)^2) / 7

and

BP_k(d) := phi_{n_L(k)}(m_k(d)) + phi_{n_R(k)}(m_k(d) - cond(k))

when d >= n_R(k)^2, and

BP_k(d) := phi_{n_L(k)}(m_k(d))

when n_L(k)^2 <= d < n_R(k)^2. The right term is absent before the right layer is eligible. For d < n_L(k)^2 the pair is not eligible and BP_k(d) is not attached.

The shift m |-> m - cond(k) is the Lucas-type pairing on the pair: the two layers evaluate the same residue-2 degree at arguments differing by the odd conductor. This is the identity LayerFilt_7 required before the pair could be named.

Start degrees of the first pairs, all already implied by LayerFilt_7 n-layer onsets:

k=0 pair (3,4)   conductor 1   left starts 9    right starts 16
k=1 pair (10,11) conductor 3   left starts 100  right starts 121
k=2 pair (17,18) conductor 5   left starts 289  right starts 324
k=3 pair (24,25) conductor 7   left starts 576  right starts 625

Pair 2 begins at d=289. That degree sits after the LayerFilt_7 exact window 121 <= d <= 282. Pair 3 and later begin still later. Conductor 7 at k=3 is the packaging integer 7 already on Master. It is not a new leftover COUNT and is not an identification of BandPair_7 with g_7 itself.


4. Operations

Evaluation of BP_k at one written residue-2 degree.
Restriction to one pair index k.
Finite sum of the first K+1 pairs: SumBP_K(d) := BP_0(d) + ... + BP_K(d).
Eligibility of pair k at degree d.
Comparison of two pair indices by conductor.

No convolution. No group-ring product. No p-adic lift. Leftover-COUNT degree of the object is 0. 539 is not a pair index, not a window length, and not a conductor. 247 is LastMiss_7(2), not a pair index and not a leftover COUNT.


5. First locks L1-L8

L1. The only n-layers that can occupy residue-2 degrees of g_7 are the pairs BandPair_7(k) for k >= 0. This restates the written square-class fact of LayerFilt_7 and Comp_7 residue support {0,1,2,4}. It does not restate residue vanishing on forbidden classes 3,5,6 as a new theorem.

L2. The Pack+(S) pair identity (BP7-1, BP7-2, BP7-3) holds for every integer k >= 0.

L3. On the LayerFilt_7 exact window 121 <= d <= 282 one has the recovery identity

S(t) = BP_0(d) + BP_1(d)    for d = 7t + 2.

Independently checked: the three window zeros remain 135, 191, 247 and the five post-247 exact-window values remain S = -3, 6, -2, 3, -5 at d = 254, 261, 268, 275, 282. BandPair_7 therefore recovers LayerFilt_7 as the two-pair window sum and does not rewrite LayerFilt_7.

L4. Pair 0 is eligible from d=9. Pair 1 is fully eligible from d=121. Pair 2 is first eligible at d=289. So BandPair_7 does not insert a new n-layer inside the exact window.

L5. Frozen small-m identities already written for LayerFilt_7 remain the only phi evaluations used: phi_n(0)=1 for n>=0, phi_n(1)=-1 for n>=1, phi_n(2)=0 for n>=2. The last of these still makes d=135 an eligible quad and a contributing triple. BandPair_7 does not add a phi identity.

L6. Miss7_tail = {135, 191, 247} remains the only zeros of SumBP_1 on the exact window. BandPair_7 does not add a fourth window zero.

L7. The five post-247 exact-window degrees stay occupied by SumBP_1 itself. Occupancy of those five degrees is the LayerFilt_7 lock, now read as a two-pair sum. It is not OccFilt_7(2 ; infty) and it is not occupancy of class 2 after the window.

L8. 247 ≡ 7 (mod 16), not ≡ -1 (mod 16). 247 is not in leftover I = {4880, 243, 20, 21, 542, 18, 521, 539, 29, 9}. BandPair_7 does not promote 247 into leftover COUNT 539. BandPair_7 does not flatten 539 into a pair index or a window length.


6. First obstructions Y1-Y8

Y1. BandPair_7 does not force occupancy of residue 2 after 247. Pair 2 enters at d=289. Higher pairs can in principle cancel SumBP_1. No cancellation identity is written. Finite-window only.

Y2. OccFilt_7(r ; infty) stays unproved for every allowed r, including r=2. BandPair_7 is an integer two-term evaluation, not a 0-1 occupancy bit, and does not promote F4 or F5 of OccFilt_7 to infinity.

Y3. The Euler double-sum g_7 * E = P restates vanishing and is not a majorant. BandPair_7 does not turn that Euler identity into a majorant.

Y4. Not LayerFilt_7. LayerFilt_7 is the four-layer exact-window identity S(t). BandPair_7 is the pair-indexed object whose first two evaluations sum to S(t) on that window. Naming the pair does not redo the window.

Y5. Not OccFilt_7. Filter values of OccFilt_7 are 0 or 1 on a class and a cap. Values of BP_k are integers coming from phi.

Y6. Not Path 4 twin-pairs. Path 4 pairs are C_third lattice points v_m=(5+7m, 1+3m), w_m=(3+7m, 2+3m) with Q-difference 2 and residues (2,4) mod 7. BandPair_7 pairs are n-layers of g_7. Different series, different lattice, different difference law.

Y7. Not Comp_7, not Dom_res, not XferPot, not End_res, not NecMono. No finite-order generator is added. Necessity stays paused. R1 stands: no P <-> Q4. No p-adic ambient.

Y8. Not a prime-infinitude claim. Degrees of g_7 are not primes. Path 2 density is not this object. Twin Prime unclaimed. AP56 after 247 stays a written occupancy correlation inside OccFilt_7(2 ; N), not a generating function of BandPair_7.


7. Decision on post-247 occupancy

BandPair_7 stays a finite-window identity.

The exact window of LayerFilt_7 uses only pairs 0 and 1. Pair 2 starts at 289, which is after 282 and after 247. The written five post-247 exact-window degrees are occupied by SumBP_1, then the identity S(t)=g_7(7t+2) stops being exact. Nothing in (BP7-1)--(BP7-3) or in the two-term evaluation forbids a later pair from cancelling the running sum. Therefore BandPair_7 does not occupy class 2 after 247 as a theorem and does not refine R2.

R2 stays R2_COMPUTATIONAL_NOT_PROVED.
P-g7-inf stays open after 247.
OccFilt_7(2 ; infty) stays unproved.


8. What BandPair_7 is and is not

Is. A residual-flux pair object on the written consecutive n-layers (7k+3, 7k+4) of residue-2 degrees of g_7, together with the Pack+(S) identity n_R^2 - n_L^2 = 7(2k+1) and the two-term evaluation shifted by the odd conductor 2k+1. Values are integers. Leftover-COUNT degree 0.

Is not.
Not OccFilt_7 and not OccFilt_7(r ; infty).
Not LayerFilt_7. LayerFilt_7 is the recovered two-pair window sum.
Not a residual majorant.
Not Comp_7.
Not Dom_res, not XferPot, not End_res, not NecMono.
Not Path 4 twin-pairs. Not Path 2 density. Not TPC.
Not a clock. Not a schedule. Not a window length 539. Not leftover COUNT 247.
Not Object B. Not a fifth slash parameter. Not Coup_enc. Not N_res.


9. Hygiene

Residual Discrete Algebra is leftover combinatorics after flux packaging. 539 is a COUNT. A count is not a clock. Residual and Resonant stay unmixed. Continuum / bounce / Fermi / 539.9 s stay Category B. Twin Prime and RH unclaimed. Bridge C not reopened. P-slash, P-Xi, P-TL, and P-PW not reopened. CORE_FREEZE holds. End_res, NecMono_res, Dom_res^(p), and XferPot_res untouched.

Do not use 53bb138 as q-series input. Mixed-scale 1d8e558 stands. g_7 is not f_0(q^7).

Name-collision refusal. The integers 3, 4, 7, 11 appear as n-layer labels and as packaging type. Appearance of those numerals in BandPair_7 is the written square-class arithmetic of g_7, not an identification with leftover I, with s-set {7,8,11} as a generating function, or with Lucas numbers as a sequence law. The word Lucas here names the consecutive-term pairing identity that LayerFilt_7 asked for. It does not import a Lucas sequence, a Lucas-Lehmer test, or a new special-function family.


Status codes.

BANDPAIR_7_DEFINED_PACK_S_2026-09-02
BANDPAIR_7_IDENTITY_NR2_MINUS_NL2_EQ_7_ODD_CONDUCTOR
BANDPAIR_7_RECOVERS_LAYERFILT_7_ON_WINDOW_121_282
BANDPAIR_7_FINITE_WINDOW_NOT_POST_247_OCCUPANCY
BANDPAIR_7_NOT_OCCFILT_7_NOT_LAYERFILT_7_REDO
R2_COMPUTATIONAL_NOT_PROVED_STANDS
PG7INF_STILL_OPEN_AFTER_247

Packaging provenance Pack+(S) only. Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.
