# PREREG: crypto-math ↔ RNT/RTA/g_k bridge tests

Frozen 2026-10-23 (America/Chicago, CDT) before any test script was run. Maps are defined in `CANDIDATE_MAPS.md` (frozen together with this file; both hashes in `PREREG.sha256`). No parameter below may be changed after data are seen; any change goes to an AMENDMENTS section of RESULTS.md with a timestamp and is not used for a verdict.

Common: T3(3k)=k, T3(3k+1)=4k+2, T3(3k+2)=2k+1 on ℕ₀. Sq_k = {x² mod k : x ∈ Z/k} (0 included). All runs `nice -n 19`, `OMP_NUM_THREADS=1`, `ulimit -v 3000000`, one at a time.

## H1 (Map M1: T3 orbit residues vs squares mod k)
- Bridge prediction: along T3 trajectories, the fraction of values in Sq_k exceeds the uniform share |Sq_k|/k (k = 7, 11, 17, 67).
- Null: per-seed mean fraction = |Sq_k|/k.
- Sample: seeds n_j = 10^12 + 7919·j, j = 0..1999 (fixed, no randomness). Trajectory: u_0 = n_j, u_{i+1}=T3(u_i), positions 0 ≤ i < σ(n_j) (stop at first hit of 1). Per-seed statistic f_j = share of the u_i in Sq_k.
- Statistic: one-sample t = (mean f − |Sq_k|/k)/(sd/√2000), one-sided p (normal approx).
- Holm correction over the 4 values of k, family α = 0.01.
- PASS (prediction confirmed) for k iff Holm-adjusted p < 0.01 AND mean excess ≥ 0.02. Map M1 is confirmed iff PASS at ≥ 3 of 4 k. Falsified otherwise.

## H2 (Map M2: fibre sizes 67, 68 → g_k)
- Compute g_k(d) exactly (Python big integers) for all d ≤ N = 20000, k = 60..76 (17 values).
- Statistic Z_k = number of allowed d ≤ N with g_k(d) = 0 (allowed: d mod k ∈ Sq_k).
- Bridge prediction: both k = 67 and k = 68 lie among the 2 largest or the 2 smallest Z_k of the 17 (ties broken against the prediction, i.e. a tie at the boundary counts as not extreme).
- Falsified if either of 67, 68 is not extreme. (Chance of both extreme under exchangeability ≈ 4·3/(17·16)·… ≤ 0.06; no p-value is claimed beyond this.)
- Descriptive only (no verdict): for k = 68 and k = 17, the list of zeros d ≤ N by residue class d mod k, and for k = 68 which classes have a zero with d > 2000. Reported as data on the open k ≡ 0 mod 4 class, not as a bridge result.

## H3 (Map M3: fibre blocks under T3 mod 539)
- Exact enumeration over n mod 1617 (=3·539; T3(n) mod 539 is a function of n mod 1617).
- Transition matrix C[b][b'] = #{n mod 1617 : blk(n mod 539)=b, blk(T3(n) mod 539)=b'}.
- Statistic D = Σ_b C[b][b]/1617. Null value D₀ = Σ_b |b|²/539² (independence).
- Bridge prediction ("T3 respects fibres"): D ≥ 1.5·D₀. Falsified if D < 1.5·D₀. Exact; no sampling, no correction needed.
- Also exact: same for T3^L with L = 2, 3 over n mod 3^L·539.

## Maps M4, M5, M6: not tested (analogy / not definable / numerology); reasons in CANDIDATE_MAPS.md.

## Multiple testing: Holm inside H1 only; H2 and H3 are exact single decisions. Overall verdict per map reported separately; no pooled claim.
