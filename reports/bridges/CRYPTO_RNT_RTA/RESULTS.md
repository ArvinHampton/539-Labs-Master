# RESULTS

Run 2026-10-23, about 10:04–10:06 PM CDT, after PREREG.sha256 was written (10:03 PM CDT; re-verified after the runs: OK). Scripts `scripts/h1.py`, `h2.py`, `h3.py` (hashes in `logs/SCRIPT_SHA256.txt`); logs in `logs/`. `nice -n 19`, `OMP_NUM_THREADS=1`, `ulimit -v 3000000`, one job at a time; total run time under 1 minute.

## H1 / Map M1 (orbit residues vs squares mod k): FALSIFIED
2000 seeds, trajectories to the first 1.

| k | |Sq_k|/k | mean share in Sq_k | excess | z | Holm p | PASS |
|---|---|---|---|---|---|---|
| 7 | 0.5714 | 0.5920 | +0.0206 | 17.5 | 2e−68 | yes |
| 11 | 0.5455 | 0.5564 | +0.0109 | 6.4 | 3e−10 | no (excess < 0.02) |
| 17 | 0.5294 | 0.5091 | −0.0204 | −19.0 | 1 | no |
| 67 | 0.5075 | 0.4932 | −0.0142 | −14.4 | 1 | no |

1 of 4 passes; the rule needs 3. The sign of the deviation is not even constant in k. The deviations are real (|z| large) but are finite-orbit effects: by P3 below, at the level of residue classes T3 sends uniform input to uniform output mod every k with gcd(k,6)=1, so no square-preference is built into T3.

## H2 / Map M2 (67, 68 → g_k zero counts): FALSIFIED
Z_k = number of allowed d ≤ 20000 with g_k(d) = 0, exact integers.

| k | 60 | 61 | 62 | 63 | 64 | 65 | 66 | **67** | **68** | 69 | 70 | 71 | 72 | 73 | 74 | 75 | 76 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Z_k | 62 | 302 | 274 | 99 | 63 | 184 | 173 | **332** | **102** | 219 | 176 | 366 | 54 | 378 | 363 | 154 | 102 |

Two largest: 73, 71. Two smallest: 72, 60. k = 67 is 4th largest, k = 68 is in the middle (tied with 76). Neither is extreme. Pattern visible instead: odd primes (61, 67, 71, 73) and 2·prime (62, 74) have many zeros; this matches the known structure of the zero families (ledger entries 77, 89–90), not the fibre sizes.

Descriptive (no verdict), k = 68 (k ≡ 0 mod 4, open class): zeros with 2000 < d ≤ 20000: 12, the largest d = 4064; their classes d mod 68 are {8, 32, 52, 60, 64}; no zero in (4064, 20000]. This is finite-range data on an open case, nothing more. The planned descriptive run for k = 17 was not produced (k = 17 lies outside the range 60..76 of `h2.py`; error in the script, noticed after the run; not rerun, no verdict depended on it).

## H3 / Map M3 (fibre blocks under T3 mod 539): FALSIFIED (exact)
D₀ = Σ|b|²/539² = 0.125006.

| L | D | D/D₀ | ≥ 1.5? | T3^L image mod 539 uniform |
|---|---|---|---|---|
| 1 | 0.13853 | 1.108 | no | yes |
| 2 | 0.13399 | 1.072 | no | yes |
| 3 | 0.12554 | 1.004 | no | yes |

T3 does not preserve fibre blocks; the small one-step diagonal excess (cause not analysed; descriptive) decays to independence by L = 3. Uniformity is exact and is proved in general in P3.

## Maps M4, M5, M6: not tested (see CANDIDATE_MAPS.md). M6 yields P2, a fact about T3 only.

## Proofs (Category A)

**P1 (balanced 8-partition of 539).** Let 539 = a₁+…+a₈ with positive integers and max aᵢ − min aᵢ ≤ 1. Then the multiset {aᵢ} is {68,68,68,67,67,67,67,67}.
*Proof.* Let q = min aᵢ. Every aᵢ ∈ {q, q+1}; let b be the number equal to q+1. If b = 8 then all equal q+1 and 8 ∣ 539, false (539 = 8·67 + 3); so 0 ≤ b ≤ 7 and 539 = 8q + b. By uniqueness of division with remainder, q = 67, b = 3. ∎
*Corollary.* Given 539 and the number of blocks m = 8, the sizes 67 and 68 and the counts 5 and 3 are forced. More generally ⌊539/m⌋ and ⌈539/m⌉ are forced for every m.

**P2 (3-adic extension of T3).** Extend T3 to Z₃ by T3(3k+r) = k, 4k+2, 2k+1 for r = 0, 1, 2 (k ∈ Z₃). Let μ be Haar probability measure on Z₃. Then (i) T3 is continuous and each branch maps r+3Z₃ bijectively onto Z₃ with μ(T3(A)) = 3μ(A) for Borel A ⊂ r+3Z₃; (ii) μ is T3-invariant; (iii) the itinerary map ι(n) = (T3^s(n) mod 3)_{s≥0} is a homeomorphism Z₃ → {0,1,2}^ℕ conjugating T3 to the shift and sending μ to the uniform Bernoulli measure.
*Proof.* (i) k ↦ k, k ↦ 4k+2, k ↦ 2k+1 are affine bijections of Z₃ because 1, 4, 2 are units of Z₃, and k ↦ 3k+r maps Z₃ bijectively onto r+3Z₃ scaling μ by 1/3; composition gives the claim. (ii) For Borel B ⊂ Z₃, T3⁻¹(B) is the disjoint union over r of the branch preimages B_r ⊂ r+3Z₃, each with μ(B_r) = μ(B)/3 by (i); so μ(T3⁻¹B) = μ(B). (iii) By (i), for every word w of length j, the set of n with itinerary prefix w is a single class mod 3^j (induction on j: the prefix w₀ fixes n mod 3 and the branch is an affine bijection, so the remaining prefix of length j−1 of T3(n) fixes T3(n) mod 3^{j−1}, hence n mod 3^j). So ι is a bijection which maps cylinders to cylinders of equal measure 3^{−j}; both sides are compact Hausdorff and ι is continuous, hence a homeomorphism; ι∘T3 = shift∘ι by definition. ∎ (This extends ledger entry 47 from Z/3^j to Z₃.)

**P3 (uniformity mod M coprime to 6).** Let M ≥ 1 with gcd(M, 6) = 1 and L ≥ 1. For n running over Z/3^L M, the value T3^L(n) mod M is well defined and takes each value exactly 3^L times.
*Proof.* Claim for one step: for N = 3^{j}M with j ≥ 1, the map n mod N ↦ T3(n) mod N/3 is well defined and exactly 3-to-1 onto Z/(N/3). Write n = 3k + r with r ∈ {0,1,2}; replacing n by n + N replaces k by k + N/3, changing T3(n) by N/3, 4N/3 or 2N/3, all ≡ 0 mod N/3, so it is well defined. For fixed r, k runs over Z/(N/3) and k ↦ k, 4k+2, 2k+1 are bijections of Z/(N/3) since N/3 = 3^{j−1}M is odd (4 and 2 are units). So each target value has exactly one preimage per r: 3-to-1. Applying the claim L times (N = 3^L M, 3^{L−1}M, …, 3M) gives a well-defined 3^L-to-1 map Z/3^L M → Z/M. ∎
*Consequences.* M = 539 = 7²·11: exact uniformity seen in H3 for L ≤ 3 holds for all L. M = k for k ∈ {7, 11, 17, 67}: T3 introduces no preference for squares at the residue-class level (relevant to M1). For even M the claim fails at the first step (2 is not a unit), which is why M = 68 was not used in H1.
