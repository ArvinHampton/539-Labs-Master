# NL DERIVED: charge-0 E₈ saddles on MN2/Bolza with symmetries other than the Witten ansatz
2026-11-09, 21:37 CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED**, unchanged. The count-gap status is unchanged: no new existing saddle is exhibited.

Authority: **OW t4426** OWNER_WRITE_MAINCHAT_t4426_PURSUE_ALL_OPEN_JUNCTION_ROUTES_2026-11-09_1956.md = d5eaeef3f6b53270bd09e30053f6cdbf442d191c58a0a9fda30daff83907ffb3 ("Pursue all open"; this is item 8). **OW t4436** OWNER_WRITE_MAINCHAT_t4436_LET_MATH_LEAD_ALL_OPEN_PATHS_2026-11-09_2127.md = 328812635d807f5cb7d1e5e6b5df7f89512060c36c090a2a191526ab7e90fd46 (χ-smeared and χ-uniform as separate branches; the marginal-w route as its own branch; keep or drop a branch only on a PROVED or REFUTED result; nothing adopted by fiat). **OW t4431** f700141d… (no usage-threshold stop; usage is still reported). Also OW 19a88b19; OW 36683379 (a citation is never by itself a proof); OW 9bb1858c. Builds on Y14 stage 2 1950 (Q0 PROVED within the Witten ansatz; Q0-out OPEN), PP 1953 N9, item 6 (Z1, w ∉ T7), item 7 (S7-w OPEN).

Limits: additive only. No existing file is edited. No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before and after. Usage 85.4% at the last checkpoint (weekly reset Tue Nov 10 09:49 CST).

The **χ-smeared** [χS] and **χ-uniform** [χU] branches are not chosen between. The **marginal-w** [w] route is carried as its own branch.

**Tally: PROVED 3 · CONDITIONAL 1 · OPEN 3 · REFUTED 0 · total 7**

## 1. Question

Do charge-0 E₈ saddles exist on the MN2 (or Bolza) fibre with a symmetry group other than the SO(3)×U(1) Witten ansatz used for Q0? If any exist, does that change the count gap? 1950 left this as Q0-out (OPEN), citing Sibner–Sibner–Uhlenbeck, PNAS 86 (1989) 8610, for the round S⁴ only, without checking that paper's mathematics.

Script and log, new dated directory `/workspace/nl-q0-saddles-2135/`, sidecars:
- q0_other_sym_2026-11-09_2135.py = 391a0612e6df942a600fb4edfbc5f023592ff05a114ca58a39e9ff9eb84edfa4, **frozen before execution**
- q0_other_sym_2026-11-09_2135.log = 7e8925db060b229334a5e04f12263a3c8e50ca429806399528c396c46bc57536

## 2. Q8-Witten (PROVED). Q0 still supplies no chargeless tension in the Witten class

Q0 of 1950 stands and is not re-proved here: in the charge-0 Witten sector (lift weight 0, Φ=a), on every face of the MN2 flow (r = X_b/X_a ∈ [1, 2] ≤ 9, so ρ is increasing), the only critical point is the vacuum a≡0, h≡1, with energy 0. A charge-0 single block in this class cannot supply chargeless tension. This is at w=0, where the fibre is SO(3)-isotropic and the ansatz is available.

## 3. Q8-conf (PROVED). The MN2 fibre functional is not the round YM functional

Four-dimensional Yang–Mills is conformally invariant, so a critical point on the round S⁴ would be a critical point on any conformal metric. The MN2 fibre is not conformal to the round S⁴. The ratio of the squared radii of the φ₁ circle and the SO(3) S²,

g_{φ₁} / g_{S²} = (X_b / X_a) tan² χ,

is unchanged by a conformal factor Ω²(χ) and is therefore a conformal invariant. On the round sphere (X_a=X_b) it equals tan²χ. At the MN2 IR (X_b/X_a=2) it equals 2 tan²χ. These are not the same, so the metrics are not conformal (script). In addition, the Y14 functional has the weight W=Δ̃ and, on the IR and interior faces, the twist term. Therefore a round-S⁴ critical point — including any SSU connection, whether or not that paper's proof is checked — is not automatically a critical point of the Y14 functional on the MN2 IR fibre. A citation of SSU does not upgrade existence here (OW 36683379).

At the UV end (c→0, X_a=X_b=1) the functional does reduce to (radius-normalized) YM on the round S⁴. Existence of an SSU-type saddle there is a question about the round problem and is still not checked in this file (Q8-SSU).

## 4. Q8-SSU (OPEN). Other-symmetry charge-0 saddles on the MN2 fibre are not constructed

Existence remains OPEN in each of the following classes. None is dropped (t4436):

- U(1)-equivariant cohomogeneity-two fields on the weighted, twisted MN2 fibre, of SSU type or otherwise (the 1950 citation).
- Multi-centre U(1)-equivariant configurations inside one SU(2) block, including net-charge-0 instanton–anti-instanton chains (PP 1953 N9). These are not covered by Q0, which uses the two-function Witten ansatz.
- Σ-non-uniform configurations that are only Aut⁺(Bolza)-invariant, not locally PSL(2,ℝ)-invariant (a proper enlargement of the T7 subsector; 1950 listed this as days of work).

No numerical search was run in this file. The SSU paper was not re-derived.

The fibre problem is the same on the **[χS]** and **[χU]** branches (as in item 7, S7-χ). Both branches are kept. If a fibre saddle were later used as a wall source, the Israel problem would split by smearing; that step is not taken here.

## 5. Q8-gap (CONDITIONAL, on existence in Q8-SSU). No proved change to the count gap

Nothing constructed in this file changes the count-gap status.

Two remarks, which do not upgrade the gap:

- Commuting Witten charge-0 blocks are vacua (Q0 + MP2), so at most 8 such blocks still give zero chargeless tension.
- A net-charge-0 field that is *not* in the Witten ansatz (for example an instanton–anti-instanton chain in one SU(2)) can, if it exists as a critical point, carry energy of order 2n and in magnitude could meet the 2808.6 (u=1) or 1404.3 (u=2) excess with a single block. Existence is exactly Q8-SSU, which is OPEN. This is a possible route, not a demonstrated closing of the gap, and is not adopted.

## 6. Q8-w (PROVED, as a scope statement). On the [w] branch, Q0's uniqueness proof does not apply

At w≠0, T_{αβ}=diag(e^w, e^w, e^{−2w}) times e^{4λ}, so the last three eigenvalues are not equal (script: e^{4λ+w} − e^{4λ−2w} vanishes identically if and only if w=0; det T=1 still). The fibre then has residual symmetry SO(2)_R×U(1)_{φ₁}, not SO(3)×U(1). The Witten two-function ansatz is not the complete H'-invariant charge-0 sector on that background, and the ρ-monotonicity argument of Q0 (which uses that ansatz on an SO(3)-isotropic fibre with r=X_b/X_a) does not apply.

Under t4436 this does not drop or close the [w] branch. Existence of charge-0 saddles on a w-deformed fibre, including along Z2 centre-manifold flows, is **OPEN** and is carried as Q8-w-ex below, not as a second PROVED item.

## 7. Q8-w-ex (OPEN). Charge-0 saddles on the [w] fibre

No charge-0 critical point with w≠0 was constructed or ruled out. The branch stays OPEN. Off-block stability of any such field is likewise OPEN (item 7, S7-w).

## 8. Q8-Bolza (OPEN). Aut⁺(Bolza) but not locally homogeneous

Charge-0 fields that vary over Bolza, invariant only under Aut⁺(Bolza)×wall ℤ₂ and not under the lifted PSL(2,ℝ), are outside Q0 and outside T7's locally homogeneous subsector (E16-A5b). They are not studied here and are not dropped.

## 9. What this does not change

The junction remains **UNSOLVED**. The count gap is unchanged: the only proved charge-0 result in this class is Q0, which has energy 0. [χS] and [χU] are both kept. The [w] branch is kept and OPEN (Q0 does not rule it out). Nothing is adopted. Q0-out is narrowed only in the sense that the obstruction to importing round-S⁴ results is now proved (Q8-conf); existence itself stays OPEN.
