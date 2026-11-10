# NL erratum 4: accepting PP's audit of the twisted-vacuum comparison (additive)
Date: 2026-11-09, about 16:40 CST (America/Chicago). Author: Non Local Path (NL).
This is a new dated file only; the 1620 file is not edited. Tip 7cddb188 untouched. No CERT. Nothing sent outside.

- **Applies to:** NL_DERIVED_TWISTED_VACUA_STABILITY_SPECTRUM_COMPARE_MN2_MN1_BBBW_N4880_G2_2026-11-09_1620.md (sha 418e4e50e4ce791bfb7c00fe4916dcee7082027c38ed7c55fea82659c98838e6).
- **Audit:** FINDINGS_PP_AUDIT_TWISTED_SUSY_VACUA_COMPARE_2026-11-09_1638.md (sha df503cd99df53b222b27f5d6a2dfbb1fb09dd9c7237630d72a7fff36a75ed494). PP found a MATCH, the reruns were byte-identical, and PP confirmed the wall identity (X₁X₂)²(X₁+X₂) = 3/2. NL accepts all four fixes.

## E1. T0 and B1–B4 become CONDITIONAL
These results rest on the cited CLP 7D U(1)² Lagrangian (hep-th/9903214, (4.6)–(4.8); MN hep-th/0007018 eq. 89). The algebra inside that truncation is exact and the code reproduces BBBW (3.8)/(2.22). But because the Lagrangian is a literature input, each label becomes CONDITIONAL on CLP.
- T0: the reduction.
- B1: MN2 gives −4, 0, 12.
- B2: MN1 gives −4, 4±2√7.
- B3: BBBW.
- B4: the neutral 14 pair moves to {−4, m₂²}.

## E2. Wording in B4
Old wording: "the −16/3 channel is lifted to the BF bound."
New wording: "the −16/3 channel is **absent** in the twisted vacua."

This is more accurate because these are different backgrounds, not a deformation of (D). In each twisted vacuum the U(1)²-neutral scalars that descend from the 14 have m²L₅² = −4 and m₂² (CONDITIONAL on CLP).

## E3. B5 spelled out (CONDITIONAL)
1. Each candidate (MN N=2, MN N=1, BBBW) has globally defined Killing spinors on compact Σ₂. The twist cancels the spin connection on Σ against the U(1)_R gauge field, so the spinors are constant sections.
2. So the AdS₅ vacuum preserves 4D N=2 (MN2) or N=1 (MN1, BBBW) superconformal symmetry. The isometry supergroup is SU(2,2|2) or SU(2,2|1).
3. Every linearized KK fluctuation of 11D supergravity around the vacuum belongs to a unitary representation of that supergroup. Unitarity of the bosonic subgroup SO(4,2) gives a lower bound on the dimension of every scalar (Δ ≥ 1, in the alternative quantization). In the supermultiplets this means the dual scalar operators have real Δ, so m²L₅² = Δ(Δ−4) ≥ −4.
4. So no BF-violating mode exists in the full tower (Breitenlohner–Freedman 1982; Gibbons–Hull–Warner 1983; Townsend 1984). The lowest KK scalar is −4, which is attained in B1–B3.

B5 stays CONDITIONAL because it relies on citation and on the Killing spinors being global on compact Σ. The full tower was not recomputed.

## E4. D2 and D3 on hold
Under OW 5f59e33e (16:31), the Owner withdrew t4327, so brane and face are UNDEFINED. See also NL_NOTE_JUNCTION_EVAL_WITHDRAWN_PER_OWNER_VOICE_5f59e33e_2026-11-09_1633.md (0c48bf3a). As a result, these are ON HOLD:
- D2: V₇eff.
- D3: the junction, the face stress, and the G₄ legs in the Israel algebra.
- D4: b.

The σ₄ and V₇eff ratios in the 1620 file are only reference numbers under PP's earlier unwarped algebra. They are not junction results.

## Revised tally for the 1620 file
| Label | Count | Items |
|---|---|---|
| PROVED | 6 | T1, T3, N0, N2, C1, C2 |
| CONDITIONAL | 13 | T0, B1, B2, B3, B4, T2, B5, N1, N3, C3, C4, D1, D2 (D2 on hold) |
| OPEN | 5 | B6, N4, C5, D3 (on hold), D4 (on hold) |
| REFUTED | 1 | R1 |

The verdicts per candidate do not change: all three are stable on CLP plus the unitarity argument, and the probe nucleation ratio is exactly 1.
