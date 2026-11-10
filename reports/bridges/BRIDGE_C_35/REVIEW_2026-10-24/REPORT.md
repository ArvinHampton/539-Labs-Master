# Bridge C review: missed variables, patterns, correlations, contradictions
2026-10-24, 8:24 PM CDT (America/Chicago). Read-only review of BRIDGE_C_35/order20, order27–37 and MAPS_CANDIDATES. I ran no new numerics or hashed tests and edited no existing file. `papers/RTA_FOUNDATION_BOUND/` does not exist under `/workspace/quantum-comp/papers/`, so I could not check the v10 paper notes. I found no running order37 process, and order37/RESULTS.md is complete (RG34 FAIL).

## Executive findings
- **Most serious tension.** HUNT_ALPHA1 (19:35) says *"There is no written mod-8 indexing of the 105 companions or of the T-phases k/9800"* and *"Maps stay paused"*. PATTERN_BNU_RR (PBR2 "140·T-phase mod 8", 19:52), PATTERN_S_MARKOV and PATTERN_ST_MARKOV ran after that and use exactly this kind of indexing. Only PATTERN_FIBRE_RR and PATTERN_QNU_RR carry an authorization line ("following the mathematical patterns"). SIGNED, BNU, S_MARKOV and ST_MARKOV have none.
- **Order34 says something later orders refute.** order34 RESULTS/NOTES: *"its miss is the L_B leakage"*, *"0.3% miss is L_B leakage outside the companions"*. order35 (by characteristic) and order36 (by span) both FAIL that reading: rel. diff 5.03 and 17.9. Order34 has no forward note.
- **Order30's "generic" near-law is refuted by order31, but order30 is not annotated.** order30 RESULTS still says *"looks generic to unimodular cone corners"*. order31 RG25a gives 26/30 FAIL and an e1-only reading.
- **Order31 has a count inconsistency.** The text says *"The four that satisfy it are exactly the cones with edge ray (1,0)"*, but the table lists 5 cones, K included. NOTES says "5/5 vs 0/26" (31 cones). RG25a is defined over 30 cones.
- **Three different maps give one vector.** PSM1 push = PBR2 = PST1 = (8/35, 11/70, 0, 9/70, 19/70, 3/35, 0, 9/70), and all have TV 71/140. That is one finding, not three independent FAILs.
- **The fibre parity structure is clean and nobody has tested it.** C35 (type (1,1)) lives only on odd fibres {1,3,5,7}. Class (0,0) lives only on {0,4}. MF2 puts total mass exactly ½ on odd fibres. Residual empties {3,7} = 3 mod 4; T-phase/Markov empties {2,6} = 2 mod 4. MF2 folded mod 4 is (¼, ½, ¼, 0).
- **There is a 105 + 35 = 140 coincidence across the geometric and map sides.** The ⟨γ,h⟩ character ranks (order27) are 36 + 24 + 18 + 27 = 105, the companion count, and the (+,+) rank is 36 = dim V. The ST-Markov classes split 140 = C105 + C35. No package relates the two.
- **The near-law ranks by the norm of the edge.** e1 (Q = 1): r ≈ 0.003. e2 (Q = 7/2): r ≈ 0.022. Interior: 0.04–0.17 (order34). Q(edge) has never been a preregistered predictor.
- **r shrinks as the grid fills, and Im κ̂ shrinks with it.** P7: 0.0585 / Im κ̂ −0.0229. G48: 0.019 / −0.0043. Full 216 grid: 0.00305 / −0.00034. Im κ̂ is always negative and its ratio to r falls (0.39 → 0.23 → 0.11). Im κ̂ is never used as a variable.
- **The P7 value matches the corner value.** r(C2b on P7) = 0.05853 (order35) equals r(CO, w = −1, full grid) = 0.0585 (order29/31). It may be a coincidence. Check it before using it.
- **Order35 repeats one number.** Outside share ‖S_out‖/‖S‖ = 0.926 equals the H1 perpendicular share 0.926. That may be correct by construction, but it is unexplained.
- **The S/X out-of-span fractions are equal.** 0.3678 vs 0.3677 (order36), well below any noise level. This is the strongest unexplained correlation, and it points to a structural reason, not leakage.
- **|num(x)| orders the miss better than den(x).** Spearman −0.96 vs −0.67 (order37). Slope p̂ ≈ 1.4 is post hoc and was rightly not used.
- **The L1–L7 collision is still in hashed files.** order27 PREREG, BATCH8 PREREG and MF corrigenda still use L-labels. These are disclosed and allowed under CORE_FREEZE, and they need no action beyond the corrigenda.
- **"35 vs 36" usage is mostly consistent.** order36 states the distinction explicitly. The top-level and order20 wording "leaves the 35-component law vector span … vs 36" mixes the two terms, though it is not wrong.

## Missed variables
| variable | where written | never used as |
|---|---|---|
| Im κ̂ (sign and size) | order20 (−4.8e−5i), order35 (−0.0229i), order36 (−0.0043i), order37 (−0.00034i), order31 (Im up to −0.16) | predictor or criterion; only \|κ̂−1\| is used |
| Q(edge) of the non-e1 edge | order34 "e2 … Q = 3.5"; order31 e1 Q = 1 | regressor for r(T_B2) across cones |
| \|num(x)\| = den(−1/x), N′ = 2\|num\| | order37 diagnostics; L_B (order20) | preregistered predictor (order38 candidate) |
| max\|coords\| of cone | order31 Spearman +0.578 | follow-up control |
| ⟨γ,h⟩ character sectors (+,−), (−,+), (−,−) (ranks 24/18/27) | order27 | any projection of S, X or the corner pieces |
| Π± sectors | order29 (Π+LN, Π−LN) | applied to T_e1 / T_BB / C2b |
| vtx share of each object | order30 lesson; order31 non-vacuity span | separate predictor |
| k = 0 share of S_in (0.325) | order35 | control; order21 gives c_0 = B2(α2)/N² |
| C2a, C11 for (0,1)-edge cones | order34 (identities for K only) | (0,1)-edge decomposition; order35 marks it out of scope |
| hit rate 1/9 (exact) | MARKOV_FIBRE_FREQ exact.py | weight for any Resonant comparison |
| u mod 3 independent of u mod 8/64 (MF3) | L3_INDEPENDENCE | joint mod-24 fibre variable |
| per-point leftover (median 0.46) | order36 | only Spearman 0.18 is reported; not split by \|num\| |

## Patterns (not preregistered)
| pattern | evidence |
|---|---|
| Edge ranking e1 ≺ e2 ≺ interior | order31, 32, 34: 0.003 / 0.022 / 0.04–0.17 |
| Linear scale law T_e1(n) = ((2n+7)/4)C2b, i.e. B = 2n+7 | order33/34; exact by definition. The e2 analogue was never written |
| r falls as grid fills (small-den points worst: 1, 2, ½, 3) | order35–37 |
| Ordering by \|num(x)\|, slope ≈ 1.4 | order37 (post hoc) |
| Fibre parity: C35 → odd fibres; (0,0) → {0,4}; MF2 odd mass ½ | PST/PSM tables; MF2 |
| Empty pairs differ by 4: {3,7} Residual, {2,6} T-phase | MF2 vs PSM1/PST1/PBR2 |
| 105-way splits: character ranks 36+24+18+27; C105 class; 105 companions | order27; PATTERN_ST_MARKOV |
| Defect directions scatter (mean \|cos\| 0.064 / 0.022) | order32 RG28; order33 RG30 |
| Every predicted "cancellation" by subdivision diverges or stays orthogonal | order28–30 |

## Correlations
| pair | value | source |
|---|---|---|
| r vs den(x) | Spearman −0.67 | order37 |
| r vs \|num(x)\| | −0.96 | order37 |
| r vs arc length ℓ | Pearson −0.883 (mostly an e1 confound) | order31 |
| S out-of-span vs X out-of-span | 0.3678 vs 0.3677 | order36 |
| r vs \|Im κ̂\| across grids | co-monotone (3 grids) | order35–37 |
| T_e1 vs C2b | exactly (7/4)·C2b, r equal to 2.5e−17 | order34 |
| r(C2b, P7) vs r(CO, full) | 0.05853 vs 0.0585 | order35 / order29 |
| MF2 empties vs Resonant (BATCH8) support | Resonant {0,2} ⊂ open; T-phase empties {2,6} | BATCH8, PST1 |
| Edge type vs which piece carries the law | B2 part carries it on e1 only; T_BB fails on all 37 | order33/34 |

## Contradictions / tensions
| # | claim A | claim B | severity |
|---|---|---|---|
| 1 | HUNT_ALPHA1: no written mod-8 T-phase indexing; maps paused | PBR2/PSM1/PST1 use T-phase mod 8, run afterwards, with no authorization line | **High** |
| 2 | order34: 0.3% miss "is the L_B leakage" | order35/36 FAIL both leakage measures | **High** (needs a forward note) |
| 3 | order30: near-law "looks generic" | order31: e1-only | Medium (superseded but not annotated) |
| 4 | BATCH8: written Resonant support {0,2} | T-phase/Markov pushes give fibre 2 mass 0 | Medium (two "Resonant" fibre notions disagree) |
| 5 | order31: "four" e1 cones, criterion over 30 | table has 5; NOTES "5/5 vs 0/26" | Low (count only) |
| 6 | PSM1, PBR2, PST1 reported as three FAILs | identical vector | Low/Medium (overcounting) |
| 7 | order35 r_meas(P7) = 0.0585 vs "full-grid 0.00305" | r(CO) = 0.0585 as well | Low (verify) |
| 8 | L1–L7 reserved | L-labels in order27 PREREG, BATCH8 PREREG | Low (corrigenda exist) |
| 9 | "35-component law vector span … vs 36" (order20/top-level) | order36: ambient rank 36 = dim V is a separate notion | Low (wording) |
| 10 | order33: Cor meets the criterion on 8/9 "K excluded as span-vacuous" | order31 counts K as satisfying | Low |

## Recommended next predefined tests (ranked by readiness)
1. **order38 RG35: Bernoulli-column reference span.** This is the written next step in order36/37 NOTES. Measure the leftover of S outside span{C2b_l(x), C2b_l(−1/x)} with no fit, against r. Uses stored arrays only.
2. **order38 secondary: \|num(x)\| monotone ordering.** Preregister a monotone decrease of the per-\|num\| median r with a fixed threshold and no fitted p (order37 NOTES). Add Im κ̂ per point as a reported co-variable.
3. **(0,1)-edge decomposition, RG31-style.** Use the order20 objects only: write the e2 analogue of T_e1 = (7/4)C2b and test r(T_e2) ≈ 0.022 with Q(e2) = 7/2 as the declared predictor. This applies the order34 identities to the second edge. Order35 marked it out of scope, so it needs a fresh PREREG.
4. (Bookkeeping, no test) Forward notes for #2 and #3. Merge PSM1, PBR2 and PST1 into one result. Confirm authorization for the four unlabelled PATTERN packages.
5. (Maps) **Stay paused for new fibres.** The parity/mod-4 pattern above may only become a test if the geometric side or Arvin writes the fibre definition, per HUNT_ALPHA1 (a)–(c).
