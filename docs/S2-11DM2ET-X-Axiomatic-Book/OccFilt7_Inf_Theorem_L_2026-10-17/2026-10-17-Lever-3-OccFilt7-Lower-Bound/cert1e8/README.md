# cert1e8: certified nonvanishing of g_7(d) for 247 < d ≤ 10^8 (Cat A, computational)

Date: 2026-10-17 (America/Chicago). Part of the OccFilt_7(∞) work (see `../../2026-10-17-Lever-3-OccFilt7-Lower-Bound.md`).
Nothing outside `cert1e8/` was changed.

## Result
**For every allowed d (d mod 7 ∈ {0,1,2,4}) with 247 < d ≤ 10^8, g_7(d) ≠ 0.**
The only allowed d ≤ 10^8 with g_7(d) ≡ 0 (mod p₀) are the 24 elements of Miss_7:

    2 7 14 16 18 21 28 32 35 36 42 43 44 57 60 63 78 79 85 100 107 135 191 247

(these are true zeros: they agree with the exact big-integer values in `../data/exact_1000000.txt.gz`).
One prime was enough: p₀ = 4611686018427387847 (= PR[0] of `../g7mod.c`). Count: 57,142,835 allowed d were shown nonzero,
plus 24 zeros, total 57,142,859 = #{allowed d ≤ 10^8}. No allowed d > 247 was left unresolved, so no further primes were run.

Why this is rigorous: everything is exact integer arithmetic mod p (p < 2^62, so a+p−b and a+b fit in uint64).
The residue is g_7(d) mod p. If it is nonzero, the integer g_7(d) is nonzero. There is no floating point.

## Method (`g7cert.c`)
- g_7(d) = Σ_{n²≤d, 7|d−n²} φ_n((d−n²)/7), with P_n(x) = ∏_{j≤n} 1/(1+x^j) built in place:
  P_n[m] = P_{n−1}[m] − P_n[m−n] for ascending m. This is the same recurrence and sign convention as `../g7mod.c` and `../exact.py`,
  and it reproduces both (see Validation).
- P_n is only needed for m ≤ (D−n²)/7, so each n is truncated there. That saves about 1/3 of the work.
- G is stored by class, only for r ∈ {0,1,2,4}: G[c][t] holds d = r+7t. For fixed n the target d = n²+7m is contiguous in t (no stride 7).
  The P update and the G accumulation run in one fused pass.
- One prime at a time. A bitset marks "nonzero seen". A further prime (up to 16, from PR[]) runs only if some allowed d > 247 is unresolved.
- OpenMP wavefront over n: in a group of T consecutive n, thread j handles n0+j and processes m-block s−2j at step s, with a barrier after each step.
  The block size is B ≥ nmax+1 (65536 here). The lag of 2 blocks makes the P blocks each thread reads and writes disjoint from the other threads'.
  Because B > (2n+1)/7+1, the G ranges written in the same step are also disjoint. Results do not depend on T: residues match bit for bit for T = 1, 3, 4.
- Memory: 8·(D/7+1) bytes for P, plus 4·8·(D/7+1) for G, plus a bitset of 4·(D/7+1) bits. At D = 10^8 that is ≈ 0.57 GB (measured maxrss 567,396 kB).
  The task brief allowed ~0.8 GB for G; the class-major layout needs less.
- Build: `gcc -O3 -march=native -fopenmp -o g7cert g7cert.c -lm` (gcc 14.2.0).
  Usage: `./g7cert D prefix [threads] [maxprimes] [dumpD]`

## Validation
1. **D = 10^6, full residue check:** all 1,000,001 values g_7(d) mod p₀ (d ≤ 10^6) equal the exact big integers from `../data/exact_1000000.txt.gz` reduced mod p₀. There were 0 mismatches, for both T = 1 and T = 4.
2. **D = 10^7:** the zero list (`val/D1e7_t{1,3,4}.zeros`) is identical to `../data/D1e7.allowed_zeros.txt` (the old g7mod, 2 primes): 24 elements, max 247.
   The residues for d ≤ 10^6 from the D = 10^7 run (`val/D1e7_t1.dump.gz`) are identical to the D = 10^6 run, which is consistent with truncation.
   T = 1, 3, 4 give byte-identical dumps.
3. **D = 10^8:** the 4-thread run (`D1e8.*`) and the 1-thread run (`val/D1e8_t1.*`) give identical zero lists.

## Timing (prime p₀ only; Intel Xeon VM shared with another heavy job)
| D | threads | time | maxrss |
|---|---|---|---|
| 10^6 | 1 / 4 | 0.14 s / 0.16 s | 8 MB |
| 10^7 | 1 / 3 / 4 | 1.75 / 1.04 / 0.85 s | 59 MB |
| 3·10^7 | 4 | 3.59 s | 172 MB |
| 10^8 | 4 | **29.4 s** (wall 29.5 s, user 1m55.5s) | **567 MB** |
| 10^8 | 1 | 111.7 s | 567 MB |

For comparison, the old `g7mod` took 96 s at 10^7 with 2 primes plus long double.
Scaling: the work is ~(2/3)·√D·D/7 updates, i.e. ∝ D^1.5. Measured with 4 threads: 10^7→10^8 is ×34.6 (exponent 1.54), and 3·10^7→10^8 is ×8.2 (exponent 1.75).
The jump comes from the working set leaving cache, so the run becomes memory-bandwidth bound. At 10^8, 4 threads gave a 3.8× speedup.

## Estimate for D = 10^9 with this code
- Memory: P 1.14 GB + G 4.57 GB + bitset 0.07 GB ≈ **5.8 GB**. This is over the 4 GB budget and above the ~5 GB currently free, so the code as it stands should not be run at 10^9 on this machine.
- Runtime if memory allowed: ×31.6 to ×56 (D^1.5 to D^1.75) from 29.4 s, i.e. about **15–30 min with 4 threads** (about 1–2 h single-threaded), plus the fault-in time for 5.8 GB.
- A version that fits the budget: keep only 2 of the 4 G classes per pass (P 1.14 + G 2.29 ≈ 3.4 GB) and run two passes, recomputing P each time. That takes about **30–60 min with 4 threads**.
  Alternatively, use a prime below 2^31 with uint32 G and P (≈ 2.9 GB). That stays rigorous; a few residues may come out 0 by chance and get resolved by a second prime.
  Neither option is implemented yet; each needs a small change.

## Files
- `g7cert.c`, `g7cert`: code and binary
- `D1e8.zeros`, `D1e8.log`, `D1e8.time`: the 10^8 certificate run (4 threads)
- `val/`: validation runs (10^7 with T = 1, 3, 4, including the d ≤ 10^6 residue dump; 3·10^7; 10^8 with T = 1)
- `SHA256SUMS`

sha256:
```
651034b4c1401779ced0a68d68606ef160fa068276cc9d7cb24511978379b048  g7cert.c
4a188d3f7f2250f5cdb9e381977f3c93e9262411a2839757dc29f3eda2b8d1ec  g7cert
8b44dd725c207262c810b458f0fd5400d2c2f4ee52299c2a80cbf61fdb057b80  D1e8.zeros   (same content as ../data/D1e7.allowed_zeros.txt)
31853f0bf8c09c1439612282c401e8c17c67f83a26277a30c165ab15d11f11b1  D1e8.log
```
