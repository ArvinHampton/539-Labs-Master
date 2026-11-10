# OWNER-WRITE CANDIDATE — T-E Simpson selection + q-expansion attempt (2026-10-26)
Source: Owner voice call-018c4fcf. CANDIDATE only. NO tip fold; nothing here authorizes a fold.
Tip Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — tip_touched NO. Soft SF invent HOLD (tip fill else). Soft SF F3 CLOSED. Bridge PARTIAL READY NO. W-P5a-OP stays open-to-prove; no FAIL retag.
Context: OWNER_WRITE_TE_COEFF_CYCLE_592 (5048e044…), OWNER_WRITE_CANDIDATE_TE_COEFF_LIST_ADVANCE (30846ce3…), FINDINGS_MR1_TE_COEFF_LIST_ADVANCE (adb5067d…), MR1-P5A-reverse-dimcalc .py/.out, Eigen pursue-all 0cc29a39….

## 1. Selection rule — LOCKED: Simpson
Composite Simpson weights on even-partition index mesh n=0..N, N even, Sturm-capped per isotypic piece.
Weights: w0=wN=1; w_n=4 (n odd); w_n=2 (n even, interior).
Fill-first order: (i) weight-4 slots, odd n ascending; (ii) weight-2 slots, even interior n ascending; (iii) endpoints n=0, then n=N.

## 2. Sturm-type bound
Γ0(49): index μ=56; k·μ/12 = 4·56/12 = 18.67 → coefficients n ≤ 18 determine a scalar form. Simpson cap N=18 (already even).
Label: SCALAR REFERENCE ONLY. Not proven to apply rigorously to the vector-valued ρ̄ case (a ρ̄ analogue needs a component-wise/induced-representation argument not written here). Same N=18 adopted provisionally for both isotypic pieces (503 and 89) pending such a bound.

## 3. Schedule on N=18 (19 slots per isotypic piece / per component)
1. w=4: n = 1,3,5,7,9,11,13,15,17 (9 slots)
2. w=2: n = 2,4,6,8,10,12,14,16 (8 slots)
3. w=1: n = 0, 18 (2 slots)

Applied to ambient proposed S4(Γ0(49),ρ̄), dim 592 = 503 + 89: same schedule per piece; T-ord exps N36 [0,1,4,9,14,16,21,25], N6 [1,9,29,81,109,121] carried from dimcalc as cited, not re-derived.

## 4. q-expansion run (box: no sage, no pari; custom python/sympy, exact integers)
- ρ̄ basis: ABSENT. No ρ̄ coefficients computed; none invented. All 2×19 ρ̄ slots: OPEN.
- Scalar reference M4(Γ0(49)) (dim 18 = 10 cusp + 8 Eis, matches dimcalc check): spanning set E4(q^d), d∈{1,7,49}, and θ^i·θ(q^7)^(8-i), θ = theta of x²+xy+2y² (wt 1, level 7, χ_-7). Exact rank on n≤18: **11 of 18** → PARTIAL scalar subspace, not a full basis (7 dims ABSENT).
- Scalar slots: all 19 Simpson slots n=0..18 COMPUTED for the rank-11 subspace (w=4 group first in the table order); for the missing 7 dims, OPEN.
- Files (grok-batches/): TE-SIMPSON-QEXP_scalar_G0_49_k4.py / .csv / .out, shas in TE-SIMPSON-QEXP_scalar_G0_49_k4.sha256:
  - d465e8cc64135b8da01ee766259dab7f38847007bbb4634fe1eb041f66a7e7a2  TE-SIMPSON-QEXP_scalar_G0_49_k4.py
  - 1776aa60ee661b391ea34532e38a009553d7a82e69fe1f30c79cd3a76733ba4e  TE-SIMPSON-QEXP_scalar_G0_49_k4.csv
  - bc098894b49b991352f1f4fc35b838609c93c0353ec0f2379e987473b2a3e1eb  TE-SIMPSON-QEXP_scalar_G0_49_k4.out

## 5. Status
T-E: selection rule LOCKED Simpson; list status = PARTIAL (scalar reference coeffs computed, rank 11/18; ρ̄ list OPEN with fill schedule written above).
