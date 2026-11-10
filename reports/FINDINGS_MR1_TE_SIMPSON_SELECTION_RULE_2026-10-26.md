# FINDINGS (assist) — MR1 T-E SIMPSON selection rule (2026-10-26)
Written: Mon Oct 26 2026 ~12:08 CDT (America/Chicago).
Authority: OWNER VOICE call-018c4fcf via Physicist — T-E selection rule LOCKED = SIMPSON.
Tip Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 on /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md — tip_touched NO.
Soft SF invent HOLD (tip fill else). Soft SF F3 CLOSED. Bridge PARTIAL READY NO. NOT Cat A. NO tip fold (all tip folds HELD). W-P5a-OP open-to-prove; no FAIL retag from proposed dim 592. Kudla–Millson = template only (Owner Write T-E).

## 0. Supersession
FINDINGS_MR1_TE_COEFF_LIST_ADVANCE_2026-10-26.md (sha adb5067d4da9a4346cf4fdf4592bba49f50cbe47c6231488bfedfd0464ec7e7b) is superseded FOR THE SELECTION-RULE BLANK ONLY. Retained, not deleted. Its other gaps STILL STAND (not closed here): Weil Opt 1 touch risk; isotypic 503/89 split basis; level-49 cycle data; ρ̄ basis script.

## 1. Cited inputs
- dimcalc .out /workspace/grok-batches/MR1-P5A-reverse-dimcalc_2026-10-26.out sha e2b260385fe0b4ce55e04ba364b74163cb3c66d1c4e42fa97696c774e59473e9 (verified)
- Owner Write T-E 5048e04490f0a4b7d32f1ce2ae57227205679864a633d8f8fb603327fe1048dc; Eigen pursue-all 0cc29a390b638d31b9b30181f9fbc369d7f3bd297bc3a6eba40030cb591dc34d; AMEND-2 8173e7b381ba858be90e5a46b453efaa369d63a40ff8bab24ca86f3681e17d9c (cited by hash, not re-opened)
- Prior on-box operationalization: OWNER_WRITE_CANDIDATE_TE_SIMPSON_SELECTION_QEXP_2026-10-26.md sha 98f996ae846f051d512f89b0c96f5bea3c173d23f55940f626ae637a09c62784 (§1–3 define the Simpson weights / fill-first order / N=18; quoted below)
- Scalar run grok-batches/TE-SIMPSON-QEXP_scalar_G0_49_k4.{py,csv,out}: d465e8cc…a7a2 / 1776aa60…ba4e / bc098894…e1eb (verified)
- Box search: exact phrase "composite Simpson fill-first on Sturm-capped index mesh" NOT found as a prior definition; only the candidate above operationalizes it. Treat below as assist operationalization consistent with that candidate.

## 2. LOCKED rule (stated)
SIMPSON = composite Simpson fill-first on Sturm-capped index mesh, then q-expansion on ambient proposed S₄(Γ₀(49),ρ̄), dim 592 (= 503 + 89 per dimcalc, cited not re-derived).

## 3. Sturm bound (standard, scalar)
[SL₂(Z):Γ₀(N)] = N∏_{p|N}(1+1/p) → N=49: 49·(8/7) = 56.
Sturm: f ∈ M_k(Γ₀(N)) with a_n = 0 for n ≤ k·μ/12 ⇒ f = 0. k·μ/12 = 4·56/12 = 18.67 → indices n = 0..18 suffice (B = 18).
Caveat: SCALAR REFERENCE ONLY. Vector-valued ρ̄ analogue not proved here (needs component-wise / induced-rep argument). B=18 adopted provisionally per isotypic piece.

## 4. Operationalization (assist, quoting candidate §1)
Mesh: n = 0..N, N = 18 (even ⇒ valid composite Simpson partition, h = 1).
Composite Simpson weights h/3·(1,4,2,4,…,2,4,1): w₀=w₁₈=1; w_n=4 (n odd); w_n=2 (n even interior).
Fill-first: fill slots in descending Simpson weight, ascending n within weight: (i) w=4, (ii) w=2, (iii) endpoints 0, 18.

## 5. Proposed index list — Cat B assist / NOT proved
Order (19 slots per isotypic piece / component):
1,3,5,7,9,11,13,15,17 | 2,4,6,8,10,12,14,16 | 0,18
T-E list candidates = q-expansion coefficients a_n (per V₄₂ component / isotypic 503, 89) of the ambient 592-space at these n. Note n=0 slot is vacuous for cusp forms; for ρ̄ components with fractional q-exponents the integer mesh must be mapped to the component's exponent lattice — AMBIGUITY for Owner.

## 6. What is NOT claimed
No vanishing of any coefficient; not S₄={0}; Weil Opt 1 not selected; no ξ formula; ρ(W₇)/Fricke Role A not reopened.
ρ̄ coefficients: ABSENT (no ρ̄ basis on box). Scalar M₄(Γ₀(49)) reference: spanning-set rank 11 of 18 on n≤18 (7 dims ABSENT).

## 7. STATUS: PARTIAL
Rule + Sturm cap + index list written (assist). Ambiguities for Owner: (a) "fill-first" = weight-order fill vs. all-nodes-as-functionals; (b) fill stopping criterion; (c) ρ̄ Sturm bound; (d) fractional-exponent component mapping. Blockers: no ρ̄ basis, no sage/pari, scalar rank 11/18.
