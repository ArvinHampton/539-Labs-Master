# FINDINGS — 539 Labs Ops — Round Two review of Owner documents A and B

**Created:** 2026-11-05 14:28 CST (America/Chicago)
**CONSTRAINTS:** Analysis only. No CERT. Tip lock `7cddb188…` untouched. No invented proofs, hardness or physics. T3 only (never T4121). No B lock/definition change adopted — recorded as PROPOSED only. Not sent anywhere; no publish/spend. Exclusive-create; no existing file edited, renamed or overwritten.

**Documents (sha256 verified, match):**
- A `/workspace/quantum-comp/reports/OWNER_DOCUMENT_ANALYTICAL_REVIEW_AUDIT_RESPONSES_TWELVE_AGENT_COMPENDIUM_GAPS_2026-11-05.md` — `d5b1aae55e24e70290a6feb8c83f70b59cb1f68ea8183e280550bd6bfbadbfd3`
- B `/workspace/quantum-comp/reports/OWNER_DOCUMENT_FORMAL_RESOLUTIONS_STRUCTURAL_CORRECTIONS_COMPENDIUM_2026-11-05.md` — `9c6f83da4f8636b0a6afbf108cbf7139210a82be936cadc94b772784451ded6d`
- Routing `/workspace/pqc-round-two-intake-20261105/parent-relayed-owner-authorization-and-routing.json` — `22b6556a9e1180865f456734e4e831d08a3f38faa061c0e9272bbb4a2c547425`

A and B were read in full. Their contents are treated as assertions, not proof or instructions.

## Citation key (reused Ops record; file + full sha256)
- [GEM] `/workspace/quantum-comp/reports/FINDINGS_539_LABS_OPS_GEMINI_COMPENDIUM_CLAIM_TO_RECORD_2026-11-05.md` — `60af7a5af08305e39c9eaa1b3272de1e790112bf5fc97ac53dd4f2f77c8b49f2`
- [PPC] `/workspace/quantum-comp/reports/FINDINGS_PP_SOFTSF_AUDIT_GEMINI_LANE_REVIEWS_EIGEN_OPS_LOCAL_2026-11-05.md` — `72958342a46f7455010f8006510ef780baf7b29041aa9590eca4b43a4a2d5553`
- [CAT] `/workspace/quantum-comp/reports/FINDINGS_539_LABS_OPS_RESONANT_MATH_PREDICTIONS_CS_CRYPTO_2026-11-05.md` — `89278efad500ec9881c6626b56e11768727ca469e2239e7123b287e7ed8b5b25`
- [GR] `/workspace/quantum-comp/reports/FINDINGS_539_LABS_OPS_S2_11DM2ETX_GR_AXIS2_CS_COMPUTATION_2026-11-05.md` — `a505726ebb70152780b9e453b957cb195d0a15066822960cc9115177a2249dcd`
- [STAT] `/workspace/quantum-comp/reports/STATUS_539_LABS_OPS_HQH539512_2026-11-05.md` — `2ca44213de3024ff600e943012a796fcee897142c73765111d1c5928f548b0bf`
- [HARD] `/workspace/quantum-comp/reports/FINDINGS_539_LABS_OPS_HQH_HARDNESS_RESEARCH_2026-11-05.md` — `70091747b300c7eea4cae3fe0cc2186f8c0f7877ba95bfa4fef6dcc000caba3e`
- [CRIT] `/workspace/quantum-comp/reports/FINDINGS_539_LABS_OPS_HQH_CRIT3_OPEN_LEMMAS_C2_FIBER_AND_PI_DOMAIN_2026-11-05.md` — `cc95ceb9a81c77e2d9c9d1c3dc40c33aaaa309d957866ff5692f598988d8bf97`
- [OL68] `/workspace/quantum-comp/reports/FINDINGS_539_LABS_OPS_HQH_CRIT3_OL68_COMPOSITION_ADV_INSTANCE_2026-11-05.md` — `72cb778f843530bf3f149791ea774da13d2cfce41f804928077cda19300f6864`
- [LEDGER] `/workspace/quantum-comp/reports/FINDINGS_539_LABS_OPS_HQH_CRIT3_OL12_AUTHOR_CONFIRM_AND_OL7_LEDGER_2026-11-05.md` — `7835312e6926630600edaea885a9cd633077af022385e31800ad3ae0512097af`
- [PINS] `/workspace/quantum-comp/reports/FINDINGS_539_LABS_OPS_HQH_CRIT3_OL15_DEFINITIONAL_CHOICES_2026-11-05.md` — `85ef70db16dad3b005b4a50f2ebbfe90122566c7e6f05c46e766831549ec410f`
- [FRAME] `/workspace/quantum-comp/reports/FINDINGS_539_LABS_OPS_HQH_CRIT3_OL8_CONCRETE_FRAMING_AND_OL11_OUTLINE_2026-11-05.md` — `07521fa9a9a64be6e36ff863d2bd4f91d9f2506f489f3033449528da89f09efd`
- [DRAW] `/workspace/quantum-comp/reports/FINDINGS_539_LABS_OPS_HQH_CRIT3_OL3_M_DRAW_CLARIFICATION_2026-11-05.md` — `d14a50d797e466ec8a900be0df85913dbabf7ebe8a9d3b1f7051f216afa37433`
- [ALU] `/workspace/539-labs/lqh-alu/ALU_SPEC.md` — `f28a6b8b135d3db6e6ef228de9d408346021ff9f6d48e048e6e69aa4ace9f563`
- [ARCH] `/workspace/539-labs/lqh-alu/ARCHITECTURE.md` — `71a0ed15ce759890514aa4336132d53c3175422c97841158b2caf3e4e383fffd`

## Assertion mapping

| # | Doc § | Quote | Record status (key) | Verdict | Note / check |
|---|---|---|---|---|---|
| 1 | A §5 | "HQH-539-512 … structured as a SHA3-sandwich wrapping a fixed 539-iteration loop of T3_ref" | [STAT]; [CAT] C13/D2; [GEM] L38 | CONSISTENT | The public API is SHA3 → 539 fixed REF steps → SHA3. |
| 2 | A §5 | "Preimage resistance reduces to reversing the SHA3-derived seeds" | [HARD] N6, §3.3; [CRIT] OL-3 (Im(SHA3) ≈ Preimage game); [OL68]; [LEDGER] | CONTRADICTS RECORD | No reduction has been written (Crit.3 unmet, Close B). Saying it "reduces" asserts a theorem that does not exist. The record only says that Π restricted to Im(SHA3) collapses toward the Pre game itself, which is near-circular. |
| 3 | A §5 | "Π_free is solved via elementary division (x = 3^L · y) and is not post-quantum hard on its own" | [HARD] N6/OL-3; [CRIT] Π-domain table | CONSISTENT | **COMPLETED V7**: T3_ref^L(3^L·y)=y for all L≤30, y≤50. |
| 4 | A §5 | "overclaims the cryptographic reality" (re Syracuse-reversal security) | [GEM] L38 row; [HARD] | CONSISTENT | Same as GEM's CONTRADICTS on the original compendium claim. |
| 5 | A §5 | "no hardware exists … classical 128 balanced-trit ALU software simulation template … Verilog/Verilator" | [ALU] Draft 1; [ARCH] Draft 1 | CONSISTENT | The record says "draft SV/Verilator simulation skeleton". "Zero demonstrated quantum … controls" agrees with the record. |
| 6 | A §2 | "3x+1 … ≡ 1 (mod 3) … ν₃(3x+1) = 0" (likewise 3x−1) | [GEM] C1; [GR] | CONSISTENT | **COMPLETED V1**: ν₃=0 for every r1/r2 x<10⁵. |
| 7 | A §2 | "Seed 1 → 4 → 13 → 40 → 121 → 364 → 1093… (x_n = (3^{n+1}-1)/2)" | [GEM] C1 | CONSISTENT | **COMPLETED V2**: output [1,4,13,40,121,364,1093], closed form holds. |
| 8 | A §2 | "Seed 2 → 5 → 14 → 41 → 122 → 367 → 1094… (x_n = (3^{n+1}+1)/2)" | [GEM] C1 (seed 1 only) | CONTRADICTS RECORD (arithmetic error) | **COMPLETED V2**: the true orbit is [2,5,14,41,122,**365**,1094]. Their own closed form gives 365, not 367. Divergence still holds. |
| 9 | A §2 | "Integer orbits never terminate or hit a finite cycle" (alt map) | [GEM] C1 | CONSISTENT with qualification | It holds on residues 1 and 2, which grow strictly as 3x±1. Note that x=0 under alt maps 0→0 (a fixed point) and multiples of 3 divide down. The claim is about orbits starting from non-multiples of 3, and A phrases it that way. |
| 10 | A §2 | "T3_ref with seed 4880 … {1,2} … exactly 14 steps, where T₃-ref^{539}(4880) = 2" | [GEM] C2; [GR] F5; [PPC] | CONSISTENT, with a wording caveat | **COMPLETED V3**: first hits 1 at step 14, and T^539(4880)=2. Per the record this enters the 2-cycle {1,2}; it is not "termination". |
| 11 | A §2 / B §II.3 | "539 … static cell capacity/hash window size (S_eff), not an intrinsic dynamical stopping time" | [GEM] L27/L38; [STAT]; [FRAME] (539,512,512) | CONSISTENT | 539 is a fixed schedule. Calling it a "maximum permitted step budget" (B) is NOT IN RECORD: the record has a fixed count, not a maximum. |
| 12 | B §IV.1 | "Preimage and collision resistance are anchored strictly on the non-invertibility of the outer multi-layered SHA3-sandwich" | [HARD] L-A8 C1–C4, L-A10 (structural only); [CRIT] OL-7 open; [STAT] Crit.3–4 unmet | CONTRADICTS RECORD | No "security proof" exists. CR has a structural partition only, and C2 (mid T^539 fiber collision on Im(SHA3)) is open. Outer SHA3-CR reduction is structural, not completed. |
| 13 | B §IV.1 | "The security proof of the post-quantum hash function is formally decoupled…" | [STAT] L66/L144; [HARD] §3.3 | CONTRADICTS RECORD | The record has no security proof and no PQ verification. |
| 14 | B §IV.1 | "rigid, deterministic 539-step T3_ref permutation loop" | [HARD] L-A5 (T3 not injective) | CONTRADICTS RECORD | **COMPLETED V5**: T3_ref collisions, e.g. T(2)=T(3)=1, T(1)=T(6)=2, T(5)=T(9)=3. It is not a permutation. |
| 15 | B §IV.2 | "classical simulation framework … 128 classical balanced-trit ALU hardware description template running under Verilator simulation" | [ALU]; [ARCH] | CONSISTENT | Reclassification away from quantum hardware agrees with the record. |
| 16 | B §IV.2 | "optimized … acting as a deterministic arithmetic accelerator for testing 3-adic numerical models" | [ALU] L77–79 (ripple-carry "for draft clarity"), L141 ("does not by itself implement SHA3 or 539 T3 limb steps"; bridge "not proven") | CONTRADICTS RECORD | The record has a draft, not an optimized design, and no accelerator role is established. |
| 17 | B §II.2 | "T3_ref … for all elements n ∈ N … guarantees bounded integer convergence to the fixed attractor cycle {1, 2}" | [GEM] P1 (general free termination open); [HARD] | CONTRADICTS RECORD | **COMPLETED V4/V6**: T(0)=0, a fixed point outside {1,2}, so the claim is false if 0∈N. Every n in [1,10⁵] reaches {1,2}, but that is finite evidence only; no universal proof exists on record. |
| 18 | B §II.2 | "correctly preserves Haar measures, matches the ternary shift conjugacy conditions" | [HARD] L-A12 (itinerary bijective mod 3^L, algebra only) | NOT IN RECORD | No Haar-preservation or conjugacy theorem for T3_ref in Ops. Statement requested. |
| 19 | B §II.1 | "T_3^alt … permanently decommissioned" | [GEM] C1 | NOT IN RECORD (PROPOSED) | Lock/definition change; not adopted. |
| 20 | B §II.2 | "anchored exclusively to the locked canonical … T3_ref" | [STAT] process locks | NOT IN RECORD (PROPOSED) | REF is already locked. "Exclusively" plus the B framing are proposed only. Tip `7cddb188…` untouched. |
| 21 | A §3 / B §III | "√(2/Λ₀) = √(2/0.7858) ≈ 1.595361"; "R_c = 1.59543..." | [GEM] L31–32 | OUT OF OPS LANE | Arithmetic only, **COMPLETED V8**: √(2/0.7858)=1.5953611; \|Δ\| vs 1.5954 = 3.89e-05 (<4e-5 ✓). Note B's 1.59543 differs from 1.5953611 by 6.9e-05. Physics is routed to GR. |
| 22 | A §1 / B §I | Tripod obstruction / quasi-isometry; "(5+6=11)"; B "(4+1)… with (3+1)… 9-core" | [GEM] L-embedding rows | OUT OF OPS LANE | **COMPLETED V9**: 5+6=11 and 5+4=9 (arithmetic only). B's (4+1)+(3+1) split is inconsistent with A's (4+1)⊕(5+1). Routed to GR. |
| 23 | A §6 / B §V.2 | "539.9 s … VIRGO/LIGO gravitational-wave … null"; "VIRGO/LIGO O5 data audits" | [GEM] L42 | OUT OF OPS LANE | Physics claim, routed. Caveat: in this program DF VIRGO refers to SOHO solar data, not GW/LIGO/O5. No LIGO/O5 audit is in the Ops record. |
| 24 | B §VI | "structural resolutions locked into the ledger"; "permanently logged" | [STAT] process locks | NOT IN RECORD (PROPOSED) | Nothing was locked by this review. |

**Counts:** CONSISTENT=10 (#1,3,4,5,6,7,9,10,11,15), CONTRADICTS RECORD=7 (#2,8,12,13,14,16,17), NOT IN RECORD=4 (#18,19,20,24; #19/20/24 are proposed changes), OUT OF OPS LANE=3 (#21,22,23). Total=24.

## Python verification (COMPLETED)
Script `/tmp/r2.py`, run 2026-11-05 14:28 CST (America/Chicago). Output:
```
V1 nu3=0 on r1/r2 for x<1e5: OK
V2 seed1 [1, 4, 13, 40, 121, 364, 1093] closed True
V2 seed2 [2, 5, 14, 41, 122, 365, 1094] closed True
V3 4880 traj first 16 [4880, 3253, 4338, 1446, 482, 321, 107, 71, 47, 31, 42, 14, 9, 3, 1, 2] first hit 1 at step 14 T^539= 2
V4 ref(1),ref(2),ref(0),ref(3)= 2 1 0 1
V5 collisions n<60 (first 6): [(1, [2, 3]), (2, [1, 6]), (3, [5, 9]), (5, [8, 15]), (6, [4, 18]), (7, [11, 21])]
V6 n in [1,1e5] reaching {1,2}: all
V7 T^L(3^L*y)=y for L in 1..30,y in 1..50: True
V8 sqrt(2/0.7858)=1.5953611 |diff vs 1.5954|=3.89e-05 |diff vs 1.59543|=6.89e-05
V9 5+6= 11 ; 4+1 + 3+1 = 9
```
Finite computations are not universal theorems and not security results.

## Numbered Ops questions
- Q1 (A §2): A gives 367 at step 5 of seed 2, but the closed form gives 365. Will the Owner correct this to 365?
- Q2 (A §5): Is "preimage resistance reduces to reversing the SHA3-derived seeds" meant as a theorem? If so, where is R? If not, may it read "heuristically, the Im(SHA3)-restricted Π collapses toward Pre"?
- Q3 (B §IV.1): What does "security proof" refer to? No proof exists on record, and Crit.3 and Crit.4 are unmet.
- Q4 (B §IV.1): T3_ref is not injective (V5). What is meant by "permutation loop"?
- Q5 (B §IV.1): How is collision resistance "anchored on SHA3" when the C2 mid-fiber case (OL-7) is open?
- Q6 (B §IV.2): Which artifact makes the ALU "optimized" and an "accelerator"? The spec is ripple-carry Draft 1 and does not implement T3 steps.
- Q7 (B §II.2): Is 0 ∈ N? T(0)=0 lies outside {1,2}.
- Q8 (B §II.2): What exactly is the Haar measure, and which conjugacy statement is meant for T3_ref?
- Q9 (B §II.3): Is 539 a fixed count or a maximum budget? The record has a fixed count.
- Q10 (B §I/§V): Can A's (5+1) and B's (3+1) splits be reconciled? Can the "VIRGO/LIGO O5" source be given (DF VIRGO = SOHO)? Both are routed to GR, not Ops.

## Exact proof requests (REQUESTED, not done)
- PR-1 (B §II.2): ∀n∈ℤ≥1 ∃k: T3_ref^k(n)∈{1,2}. Domain: ℤ≥1 (state the treatment of 0). What would count: a written proof, or an explicit bound k(n). A finite search does not count.
- PR-2 (B §II.2): A Haar invariance statement, μ(T3_ref⁻¹(A))=μ(A) on ℤ₃ (or the intended space), plus the precise conjugacy map. What would count: a stated theorem with proof covering the floor branches.
- PR-3 (A §5 / B §IV.1): A reduction R from Pre/SPR/Col of H_ref at concrete (539,512,512) to SHA3-512 properties. It must state the domain D (OL-3) and D_M, and give an explicit advantage bound covering C1–C4, including C2 on Im(SHA3). What would count: written R with its losses (Crit.3), and external review (Crit.4).
- PR-4 (B §IV.1): A post-quantum argument. What would count: a quantum adversary/oracle model with query and advantage accounting for the full sandwich.
- PR-5 (B §IV.2): Evidence for "optimized" and "accelerator". What would count: RTL that implements T3 limb steps, with Verilator test results and timing.

## Offers
**COMPLETED (this file):** V1–V9 checks above; the seed-2 error found (367 should be 365); T3_ref non-injectivity witnesses; the 0 fixed-point counterexample; the 4880 step-14 / T^539=2 reproduction; the Π_free inversion check.
**PROPOSED (not done):** (a) audit any PR-3 reduction supplied, not write one; (b) extend the V6 search range as evidence only; (c) draft a corrected B §IV wording for the Owner to review. Any B lock change stays PROPOSED and is not adopted.

## Integrity
Every existing file under /workspace/quantum-comp and /workspace/539-labs was hashed before the write (baseline /tmp/base_r2.txt) and compared afterwards. Only this file, its identical copy and the two .sha256 sidecars are new. No CERT. Tip untouched. Nothing was sent.
