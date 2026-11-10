# RESULTS: DISCOVER_GRADING_PATH
PREREG.md sha256 108ab2d4044e21b32e4c60c721e32dfd40f3891d8ab7927321d3321655c1f791, hashed after exploration and before the tests. Scripts: scripts/explore.py (pre-PREREG), scripts/tests.py (hash in scripts/SHA256SUMS). Data: data/tests.json, data/explore.sha256. Logs: logs/. Under 1 s each; nice, OMP_NUM_THREADS=1, ulimit -v 3 GB.

| Test | Measured | Verdict | Content? |
|---|---|---|---|
| D1: u ≡ 3 (9) ⇒ T3(u) ≡ 1 (3); predecessors of charge 3 ⊆ {0, 4, 5} | 0 counterexamples below 3·10⁶; predecessor classes exactly {0, 4, 5}; residue proof (u = 27t + r, r ∈ {3, 12, 21} ⇒ T3(u) = 9t + r/3 ≡ 1 mod 3) | **PASS**, Category A (proved) | exact structure of P_res; not a bridge |
| D2: hit fraction 1/9 ± 4σ; no consecutive hits | h = 0.11034 (z = −1.79); 0 consecutive pairs | **PASS** | flagged pre-test as the pseudo-random expectation; the no-consecutive part is forced by D1 |
| D3: hit fibres β̂ uniform (χ² ≤ 24.32) | counts [1933, 14715, 5601, 4, 13053, 14864, 9296, 9]; χ² = 38 633 | **FAIL**, strongly | **genuine discovered structure** (see below) |
| D4: g = (−1)^τ is the unique ±1 grading (up to sign) constant on towers with path coboundary (−1)^{δf} | consistent, K⁺ 1-skeleton connected, solution = g | **PASS** | existence by construction; uniqueness from connectivity. Weak |
| D5: no hit lands in [21, 4880) | 0 such hits (min bit length seen: 137) | **PASS** | expected from magnitude. The PREREG parenthetical "u ≥ 2^400" was wrong (actual min 137 bits); the rule tested was the range condition |

**Bridge: NO.**

## Discovered structure (post-hoc explanation of the D3 FAIL; Category A lemma, elementary)
**Lemma V (2-adic invariant of T3).**
- v₂((4n+2)/3) = 1 and v₂((2n+1)/3) = 0, because 3 is odd.
- v₂(n/3) = v₂(n).

Hence, after the first step with u ≢ 0 (mod 3), every later value has v₂(u) ≤ 1, i.e. **u ≢ 0 (mod 4) for the rest of the path**.

For a hit u = 21 + 9j: u ≡ 0 (mod 4) ⇔ j ≡ 3 (mod 4) ⇔ β̂(u) ∈ {3, 7}.
**So the fibres β̂ = 3 and β̂ = 7 are forbidden to every hit after the initial pure-division prefix of the path.** The 13 observed exceptions (4 + 9) occur in that prefix. The post-hoc log logs/posthoc_mod4.log shows hits ≡ 0 or 4 (mod 8) only from the n/3 branch (6 cases in 300 paths).

The remaining imbalance (for example class 0 vs classes 1, 5) comes from the same mechanism at higher 2-adic and 3-adic depth. An exact prediction needs a Markov chain on u mod (2^k · 9 · 8).

## Candidate objects now exact and re-runnable (all Category B as residual↔resonant objects; none is a written source)
1. Path predicate P_res(u) = [u ≡ 3 mod 9] (Option-3 free-dynamics probe).
2. Path → fibre map β̂(u) = ((u − 21)/9) mod 8 on hits (agrees with β♯ on O_res).
3. ±1 grading g(x_j) = (−1)^{τ(x_j)} on O_res (carrier-only; unique given D4's constraints).
4. Lemma V: hits avoid β̂ ∈ {3, 7} after the prefix. This is the first non-trivial, exact path → fibre constraint found.
