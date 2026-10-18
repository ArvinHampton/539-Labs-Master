# cert1e9: certified nonvanishing of g_7(d) for 247 < d ≤ 10^9 (Cat A, computational)

Date: 2026-10-17 (America/Chicago). Extends `../cert1e8/` (left untouched) for the OccFilt_7(∞) work.

## Result
**For every allowed d (d mod 7 ∈ {0,1,2,4}) with 247 < d ≤ 10^9, g_7(d) ≠ 0.**
The only allowed d ≤ 10^9 with g_7(d) ≡ 0 (mod p₀) are exactly the 24 elements of Miss_7. These are true zeros (exact values, `../data/exact_1000000.txt.gz`):

    2 7 14 16 18 21 28 32 35 36 42 43 44 57 60 63 78 79 85 100 107 135 191 247

- One prime was enough: p₀ = 4611686018427387847 (PR[0], same as `../g7mod.c` and `../cert1e8`). No allowed d > 247 was unresolved, so no extra primes and no exact recomputation were needed.
- **Count check:** 571,428,548 allowed d shown nonzero (285,714,274 per pass), plus 24 zeros, gives 571,428,572. This equals #{allowed d ≤ 10^9} = Σ_{r∈{0,1,2,4}} (⌊(10^9−r)/7⌋+1).
- `D1e9.zeros` is byte-identical to `../cert1e8/D1e8.zeros` and `../data/D1e7.allowed_zeros.txt`.
- **Rigor:** the arithmetic is exact uint64 mod p < 2^62 with no floating point. g_7(d) mod p ≠ 0 implies g_7(d) ≠ 0.

## Method
`g7cert2.c` is `../cert1e8/g7cert.c` with one change: a class mask (6th argument) chooses which classes r ∈ {0,1,2,4} keep a G array.
- P_n (∏_{j≤n} 1/(1+x^j), in place P[m] ← P[m] − P[m−n], truncated at (D−n²)/7) is still built for every n.
- G is accumulated only for n with n² mod 7 in the selected classes.
- Memory per pass: 8(D/7+1)·(1 + #classes) bytes plus the bitset.

Two passes run one after the other, not concurrently (`run1e9.sh`):
1. mask 3 → classes {0,1}
2. mask 12 → classes {2,4}

The other parts are unchanged: OpenMP wavefront over n with 4 threads and block B = 65536 ≥ nmax+1 = 31623, a nonzero-seen bitset, and extra primes only if some allowed d > 247 is unresolved.
`merge.py` concatenates the per-pass zero lists and checks the allowed count.
Build: `gcc -O3 -march=native -fopenmp -o g7cert2 g7cert2.c -lm` (gcc 14.2.0).

## Validation (before the 10^9 run)
1. **D = 10^6, residues:** every residue g_7(d) mod p₀ for d ≤ 10^6 equals the exact big integer reduced mod p₀, with 0 mismatches. This holds for mask 3 (285,716 values), mask 12 (285,714) and mask 15 (all 571,430 allowed d). Dumps are in `val/D1e6_m*.dump.gz`.
2. **D = 10^7, two passes:** the merged zero list equals `../data/D1e7.allowed_zeros.txt` exactly, and the count check passes (5,714,287).
3. **D = 10^8, two passes:** the merged zero list equals `../cert1e8/D1e8.zeros` exactly, and the count check passes (57,142,859). Each pass took 34–35 s on the loaded machine.

## Run at D = 10^9 (4 threads, shared machine; load ≈ 5 from the concurrent Lemma L job)
- `free -g` before launch: 15 total, 9 used, 2 free, 5 available (`free -m`: available 6120 MB).
- Pass {0,1}: 17 m 22.6 s wall (user 69 m 02 s), 19:06:12–19:23:35 CDT.
- Pass {2,4}: 18 m 17.7 s wall (user 72 m 50 s), 19:23:35–19:41:52 CDT.
- **Total wall time: 35 m 40 s.**
- **Peak memory:** maxrss 3,385,444 kB (≈ 3.39 GB) per pass. Only one pass is resident at a time. The lowest system "available" memory during the run was 2370 MB (`val/D1e9_memwatch.txt`).
- Scaling from 10^8 (two-pass, ≈ 35 s/pass) to 10^9 (≈ 1070 s/pass) is ×31, consistent with the D^1.5 work.

## Files
- **Code:** `g7cert2.c`, `g7cert2`, `merge.py`, `run1e9.sh`
- **Result:** `D1e9.zeros` (merged), `D1e9_m3.{log,zeros}`, `D1e9_m12.{log,zeros}`, `D1e9.time` (timings, `free` snapshots, merge output)
- **Validation:** `val/` (10^6 residue dumps, 10^7 and 10^8 two-pass runs, memory watch for 10^9)
- `SHA256SUMS`
