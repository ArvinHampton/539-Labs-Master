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
