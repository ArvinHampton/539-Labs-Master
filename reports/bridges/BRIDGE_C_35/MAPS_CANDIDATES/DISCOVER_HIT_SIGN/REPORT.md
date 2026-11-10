# PREREG: DISCOVER_HIT_SIGN: lag ≥ 2 hit law and a chain-derived 1/5 sign
Written 2026-10-24 at about 9:05 PM CDT, after exploration (scripts/explore.py → data/explore.json, logs/explore.log; hashes in data/explore.sha256), before any b"sign-" seed was touched. Owner: Arvin Hampton. Option-3 free-dynamics probes (P_res, β̂, s). Category B unless stated. **No bridge claim.** g = (−1)^τ and P_res remain unaccepted candidates; C11 is not re-run.

## Model (same as DISCOVER_MARKOV_288)
Lifted T3 chain on Z/M (3 lifts, each w.p. 1/3), restricted to u ≢ 0 mod 4 (Lemma V). Hit = u ≡ 3 mod 9, β̂ = ((u−21)/9) mod 8. The exact results at M = 72 and M = 288 are identical (exploration).

## Exact chain statements (Category A for the lifted chain)
- **DM3 (lag ≥ 2 independence):** for k = 2, 3, 4 hits ahead, K_k(a→·) = ρ = (1,8,3,0,7,8,5,0)/32 for every open a. The joint law of (β̂_n, β̂_{n+k}) is ρ⊗ρ for k ≥ 2. All dependence sits at lag 1 (DM2).
- **DM4 (2-adic sign):** on hits, β̂ = 1 ⇔ u ≡ 6 (mod 8), and β̂ = 5 ⇔ u ≡ 2 (mod 8); both have v₂(u) = 1. Define s(u) := χ₄(u/2) = (−1)^{(u/2 − 1)/2}, using the unique non-trivial character mod 4 of the odd part u/2. Then s = −1 on fibre 1 and +1 on fibre 5. This is canonical given Lemma V (v₂ = 1). It is not fitted, and the only convention is the choice of χ₄ over −χ₄.
- **DM5 (sign law):** on the {1,5}-hit subsequence, E[s] = 0 and the sign autocorrelation is 0 at lags 1–4 (the next sign is independent of the previous sign). Conditional on the immediately preceding hit (any fibre): E[s | prev ∈ {1,5}] = −1/6 and E[s | prev ∈ {0,2,4,6}] = +1/6 (from DM2: 5/24 − 7/24 over 1/2).

## Test (seeds u₀ = int(SHA3-512(b"sign-" + str(s)))), s < 3000, 539 steps; disjoint from explore-, holdout-, mfholdout-, fresh-)
Open fibres only for pair statistics; χ² threshold 20.52 (5 dof, p = 0.001).
- H1: lag-2 pairs, split by origin row A (first hit in {0,2,4,6}) / row B (first hit in {1,5}); χ² vs ρ ≤ 20.52 for each.
- H2: the same for lag 3.
- H3 (non-vacuity): lag-1 row-B χ² vs ρ > 20.52.
- S1: |mean s| over {1,5}-hits ≤ 4/√n.
- S2: |lag-1 sign autocorrelation on the {1,5}-subsequence (same path)| ≤ 4/√n_pairs.
- S3: each conditional mean, E[s | prev ∈ {1,5}] and E[s | prev ∈ {0,2,4,6}], lies within 4σ of ∓1/6, with σ = √((1 − m²)/n).
- S4 (non-vacuity of S3): the two conditional means differ by more than 4σ_diff.
Overall PASS iff all pass. FAIL if H1/H2/S1–S3 fails. VACUOUS if only H3 or S4 fails.

## Obstruction note (pre-test)
DM5 shows that the sign carries **no** self-correlation along the {1,5}-subsequence. So s is not a dynamical grading in the C11 sense. Its only path content is the lag-1 cross-dependence on the preceding hit's class. Linking s to g = (−1)^τ is not possible from the chain, because hits never land in O_res (DISCOVER_GRADING_PATH D5), and so has not been done.
# RESULTS: DISCOVER_HIT_SIGN
PREREG.md sha256 681b664931018abc7aaa67e2b70707509c6ec282687a95f9cb27cc3cbe3075a5, hashed after exploration and before the test. Seeds b"sign-s", s<3000, 539 steps. 90,388 hits in fibres {1,5}.

## (1) Joint law at hit-lag ≥ 2 (DM3)
Predicted for every origin: ρ = (1,8,3,0,7,8,5,0)/32 = (.03125,.25,.09375,0,.21875,.25,.15625,0).

| lag | origin | counts over β̂ = 0,1,2,4,5,6 | χ² vs ρ |
|---|---|---|---|
| 1 | B {1,5} | 2748, 26206, 8170, 19347, 18522, 13851 | **1335.1** (dependence present, H3) |
| 2 | A | 2647, 22164, 8001, 18979, 21483, 13548 | 15.97 |
| 2 | B | 2751, 21937, 8059, 18991, 22038, 13543 | 6.05 |
| 3 | A | 2630, 21637, 7921, 18579, 21272, 13274 | 6.46 |
| 3 | B | 2677, 21738, 7859, 18750, 21452, 13352 | 8.34 |

## (2) Sign s = χ₄(u/2) on {1,5}-hits (DM4/DM5)
s = −1 on fibre 1 and +1 on fibre 5; the per-hit assert passed on all 90,388.

| statistic | predicted | measured | threshold | verdict |
|---|---|---|---|---|
| S1 mean s | 0 | −0.0064 | ±0.0133 | PASS |
| S2 lag-1 sign autocorrelation | 0 | −0.0022 | ±0.0135 | PASS |
| S3 E[s \| prev ∈ {1,5}] | −1/6 | −0.1718 (z −1.10) | 4σ | PASS |
| S3 E[s \| prev ∈ {0,2,4,6}] | +1/6 | +0.1596 (z −1.52) | 4σ | PASS |
| S4 difference non-vacuous | >4σ | z = 50.2 | | PASS |

H1 PASS, H2 PASS, H3 PASS. **Overall: PASS.** Category A for the lifted chain; Category B numerically. **Bridge: NO.**

## Grading verdict
No grading candidate beyond g emerged. s is canonical (fixed by Lemma V's v₂ = 1 and χ₄), but it has zero self-correlation at every lag. Its only path content is the lag-1 cross-term ±1/6 against the class of the preceding hit. That makes it a relabelling of β♯ restricted to {1,5}, not a dynamical ±1 grading. It cannot be linked to g = (−1)^τ, because hits never reach O_res (D5).
# NOTES: DISCOVER_HIT_SIGN
- Order: explore.py hashed and run (data/explore.sha256), then PREREG.md hashed (PREREG.sha256), then scripts/test.py run once (scripts/SHA256SUMS). All runs under 2 s; nice, OMP=1, ulimit 3 GB.
- Lemmas: DM3 (lag ≥ 2 independence: the hit-fibre process is exactly 1-step dependent and ρ-mixing after one hit); DM4 (β̂ ∈ {1,5} ⇔ u ≡ 6, 2 mod 8, s = χ₄(u/2)); DM5 (sign mean 0, autocorrelation 0, conditional ∓1/6). Identical at M = 72 and 288.
- Obstruction (sign): the only convention is χ₄ vs −χ₄. Any ±1 on {1,5} has zero self-correlation under the chain, because rows 1 and 5 of K₁ are equal. So no sign on {1,5} can be a dynamical grading, and no s ↔ g link is computable.
- Model caveat: equidistribution of lifts is assumed, and it is confirmed numerically only.
- Next step: the hit-fibre process is now fully characterised (ρ plus the lag-1 kernel; fibre-to-fibre dependence vanishes from lag 2). The residual-path side has no more exact content at this depth. Grading progress now needs Arvin's decision on g/P_res as the C11 grading and predicate, or a written Π. Optional check: the dependence of hit *gaps* (step counts between hits) on fibre, from the same chain.
- No L1–L7. order*/v12 paper untouched. CORE_FREEZE: this folder only. No push or send.
