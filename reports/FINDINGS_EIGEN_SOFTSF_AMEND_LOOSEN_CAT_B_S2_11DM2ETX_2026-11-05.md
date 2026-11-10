# FINDINGS AMEND — Eigen lane: loosen Cat B under S²-11DM²ET-X — 2026-11-05 ~12:15 CST America/Chicago
**ACK: OW `2c341bc70bbe9c064cb40641ba0d66dbae815053e62be998c55671d231686e49` MATCH (AMENDS ae380bf6c09980ec0a88dabbb02347a873b672f2b62b7f68fba2d5ddec9b30fa)**. I re-hashed it this turn.
AMENDS (does not edit) FINDINGS `deebdc5ebd5ae483b4b18ef374c0efb6c4bb8da82cb7e3f26e05bc90af979211`. tip BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 / AFTER 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, tip_touched **NO**. **No CERT.** REPORTS ONLY, no RECS. Nothing sent. No invented proofs, values, datasets, coefficients, roots, Kr QQ or ν.
Sources and their sha256 are unchanged from FINDINGS deebdc5e (S1–S9).

## Framing (per AMEND §1–3)
All items below are **Category B, encompassed within the S²-11DM²ET-X extension of GR** (Cat B side). Under the looser standard, each item is **permitted for research and discussion under Cat B** and **may be adapted toward alignment with observable datasets**. Dataset classes are named only generically. No specific dataset or value is asserted, and no alignment has been performed. Merger wording is conditional: "*if* [Cat B item] holds within S²-11DM²ET-X, *then* it is consistent with / bridges to [proven math]". Proven-math anchors are unchanged. Nothing here is proven or CERT.

## Items (after AMEND)
| # | Claim | After-AMEND wording (Cat B, S²-11DM²ET-X) | Generic dataset alignment it could adapt to | Proven anchor (unchanged) |
|---|---|---|---|---|
| 1 | \|W\| ≤ ∏spr(ρ(h_i)) | "Within S²-11DM²ET-X (Cat B), a spectral cancellation bound is permitted for research. *If* it holds, then it tightens the proven \|W\| ≤ N ≤ ∏‖h‖₁." | Interference/cancellation statistics in quantum-circuit or path-sum benchmark data | Triangle inequality + Perron (S1) |
| 2 | Φ/χ convergence | "Permitted Cat B research: *if* Φ converges on ℤ₃ in the S²-11DM²ET-X reading, then demo trajectories are consistent with it." | Simulation trajectory logs (e.g. labs539 self-test outputs) as calibration only | Φ well-defined on ℤ₃ |
| 3 | Ω = N−\|W\| structure | "Ω ≥ 0 is proven. Further Ω structure (other than ≡0 mod 539) is permitted Cat B research once N and W are fixed." | Winding/phase datasets, after the definitions are unified | Ω ≥ 0 |
| 4 | det ρ ≠ 0 for odd M | "Over ℂ/ℤ, proven for h=1+x. Mod-3 behaviour is a Cat B research topic, with the ring always named." | Modular/ternary-encoding error data (ring stated) | Circulant eigenvalues h(ω^j) |
| 5 | Hankel ghost condition | "*If* a Hankel H is specified in S²-11DM²ET-X, PSD positivity is the condition to research." | Moment/spectral-density data (positivity tests) | PROOF_HANKEL_POSITIVITY |
| 6 | Π_fast idempotent averaging | "Permitted Cat B research. The stub is the identity. *If* the corpus operator is idempotent, then it projects as claimed." | Time-averaged signal datasets | trivial (identity) |
| 7 | N36 Kr QQ | "Char-0 Kr QQ is a **named gap** (stands). Research and discussion of the coherent Φ₄₉ embedding are permitted under Cat B." | none: an internal compute gap with no observable dataset | mod-p rank 503/503 |
| 8 | Q89 ζ₄₉ lift | "Permitted Cat B research. *If* a coherent lift exists, then it is consistent with dim 89 in char 0." | none (internal compute) | mod-p rank 89 |
| 9/10 | Local dim=h−\|Cl²\|, RG1′ necessity | "Cat B under S²-11DM²ET-X, research permitted. Local lane owns these." | Tables of L-function and modular-form coefficients (LMFDB-type) as consistency checks | S6 #58/#61/#62 |
| 11 (new) | Hardness / physics bundle (S6 #71, #72) | "**Moved into permitted Cat B research and discussion** within S²-11DM²ET-X, with dataset alignment allowed. **NOT proven**, and still NEEDS-DEFINITION before any math merge." | Gravitational-wave / EHT-type observational data, decoherence measurements, quantum-complexity benchmarks (generic) | none |

## Delta table
| Item | Before (deebdc5e) | After AMEND | Changed? |
|---|---|---|---|
| 1 | conditional conjecture | + S²-11DM²ET-X Cat B framing, research permitted, dataset class | YES (framing) |
| 2 | named gap | + framing / research / dataset | YES (framing) |
| 3 | partial: Ω ≥ 0 only | Ω ≥ 0 proven; other Ω structure is research; mod-539 is still an objection | YES (framing); objection kept |
| 4 | ring-named | + framing / research | YES (framing) |
| 5 | not loosened (no data) | conditional PSD research is permitted; det≠0 wording is still an objection | YES (PSD route only) |
| 6 | named gap | + framing / research | YES (framing) |
| 7 | named gap stands | gap stands; research permitted; no dataset | Minimal (gap unchanged) |
| 8 | named gap | + framing; no dataset | YES (framing) |
| 9/10 | Local, conditional | + framing | YES (framing) |
| 11 | O4: NOT-MATH, not mergeable | permitted Cat B research + dataset alignment; NOT proven | YES (O4 relaxed) |

## Objections revisited
- O1 det≢0 mod 3 "prevents collisions": **REMAINS**. This is a category error (W=0 with det 72; h2 det 36≡0 mod 3). The AMEND does not change math truth.
- O2 "det≠0 kills ghosts" (Hankel): **REMAINS** false (det −3, eigenvalue −1). Only the PSD route is permitted (item 5).
- O3 Ω ≡ 0 mod 539: **REMAINS** contradicted by the §2.1 example (Ω=2).
- O4 hardness/physics NOT-MATH: **RELAXED** into permitted Cat B research, discussion and dataset alignment. It stays NOT proven and NEEDS-DEFINITION for any math merge. The AMEND §2 changes this fence.
- O5 N36 Kr QQ / zero-polar / G1-mem: **REMAINS**. The named gap stands and nothing implies existence, coefficients or ν.
- O6 inferred target [1] in §2.1: **REMAINS**. The AMEND does not touch it, so statements still need "with stated reading".

**Remaining objections: O1, O2, O3, O5, O6. Relaxed: O4 only.**
Items carrying conditional Cat B wording: 11 rows (1–8, 9/10, 11). Item 7 keeps its gap.
