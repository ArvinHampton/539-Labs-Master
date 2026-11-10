# PREREG: DISCOVER_MARKOV_288: exact lifted Markov chain of T3 mod 288 → β̂ hit law and next-hit kernel
Written 2026-10-24 at about 8:55 PM CDT, after exploration (scripts/explore.py and explore2.py, logs/, data/explore*.json; hashes in data/explore.sha256), before any seed b"fresh-" was touched. Owner: Arvin Hampton. Category B (numerical) unless stated. Option-3 free-dynamics probe (Architecture_A_Ores_Programme §6): P_res and β̂ are probes, not residual-carrier definitions. No Π, α1 or grading is invented or used. **No bridge claim.**

## Modulus and transition rule (committed)
- T3(n) = n/3 (n≡0), (4n+2)/3 (n≡1), (2n+1)/3 (n≡2 mod 3).
- M = 288 = 4·9·8. T3(u) mod M is a function of u mod 3M (checked; each branch adds M, 4M or 2M per 3M-shift). u mod M does **not** determine T3(u) mod M (3-way branching). The chain is therefore the **lifted chain**: from a ∈ Z/M, go to T3(a + kM) mod M for k = 0,1,2, each w.p. 1/3. This is the only modelling assumption: equidistribution of the next 3-adic digit.
- Restriction (Lemma V): the closed class is {a : a ≢ 0 mod 4}; it is closed under the chain (asserted) and has a unique stationary law (1-dim null space).
- Sufficiency of 288: the minimal modulus carrying both q = u mod 9 and β̂ (u mod 72) and Lemma V (u mod 4) is 72. Exact results at M = 72, 144, 216, 288 are **identical** (DM1/DM2), so 288 is sufficient (and over-sufficient).

## Exact predictions (exploration output; Category A as statements about the lifted chain)
- **DM1:** stationary hit rate = 1/9; hit-fibre law ρ = (1/32, 8/32, 3/32, 0, 7/32, 8/32, 5/32, 0). (Identical to MF2 ρ_res; re-derived, not fitted.)
- **DM2 (new, refines MF2):** next-hit fibre kernel K(a→b) depends on a only via [a ∈ {1,5}]:
  - row A (a ∈ {0,2,4,6}): (1/32, 5/24, 3/32, 0, 7/32, 7/24, 5/32, 0)
  - row B (a ∈ {1,5}): (1/32, 7/24, 3/32, 0, 7/32, 5/24, 5/32, 0)
  i.e. hits are **not** i.i.d. on fibres: mass 1/12 moves between fibres 1 and 5 depending on whether the previous hit was in {1,5}.

## Fresh test
Seeds u₀ = int(SHA3-512(b"fresh-" + str(s))), s = 0..2999 (disjoint from explore-, holdout-, mfholdout-), 539 T3 steps each, values u₁..u₅₃₉ scanned for hits (u ≡ 3 mod 9).
- **T1 (marginal):** χ² of open-fibre counts {0,1,2,4,5,6} vs ρ renormalised; PASS iff ≤ 20.52 (p=0.001, 5 dof).
- **T2 (forbidden):** share of hits with β̂ ∈ {3,7} ≤ 10⁻³.
- **T3a/T3b (kernel):** consecutive hit pairs (same path, both fibres open), split by row A / row B of the first hit; χ² of second-hit counts vs that row; PASS iff each ≤ 20.52.
- **T4 (non-vacuity of DM2):** χ² of row-B second-hit counts vs the i.i.d. marginal ρ must be > 20.52 (otherwise DM2 is VACUOUS at this sample size).
Overall PASS iff T1, T2, T3a, T3b, T4 all pass; FAIL if any of T1–T3 fails; VACUOUS if T1–T3 pass but T4 fails.
