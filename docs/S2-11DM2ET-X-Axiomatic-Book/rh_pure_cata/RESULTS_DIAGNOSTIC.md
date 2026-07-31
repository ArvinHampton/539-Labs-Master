# Diagnostic Results Snapshot

**Status strings:** `L5_DIAGNOSTIC_EXECUTED_NO_RH_CLAIM` · `M1_2_SKETCH_NO_RH_CLAIM`  
**RH claim:** false  
**Date stamp:** 2026-07-31 (write-all package)

---

## L5 (`rh_L5_phase_diagnostic_results.json`)

| Setting | Value |
|---------|-------|
| \(x_{\max}\) | 5000 |
| zeros | 8 (Odlyzko ordinates) |
| primes | 669 |
| \(X\) list for \(A_X\) | 20, 30, 45, 67.5 |

| Metric | On-line \(\sigma=1/2\) | Off-line (δ + minima) |
|--------|----------------------|------------------------|
| mean peak \(\lvert A_X\rvert\) | 0.411 | 0.400 |
| mean peak \(\lvert A_X\rvert/\log\log X\) | 0.325 | 0.317 |
| branch warnings | 0 | — |

**Read:** finite-range only; on ≈ off; **inconclusive** for Conjecture B / RH.

---

## M1.2 sketch (`rh_M1_2_remainder_sketch_results.json`)

| Setting | Value |
|---------|-------|
| default \(X\) | \((\log t_1)^2\approx 8.07\) |
| \(K\) | 4 |
| \(C_1..C_4\) | 1, 2, 1, 2 (package majorants) |

| \(X\) mode at first zero | \(X\) | \(R_{\mathrm{bound}}\) | term3 useful? |
|--------------------------|------|------------------------|---------------|
| log1 | 3.0 | ~3.81 | yes |
| log2 | 8.07 | ~3.17 | yes |
| log3 | 22.9 | ~40 | **no** |

| P1 semicircle about first zero | Value |
|--------------------------------|-------|
| \(\Delta\arg\) | \(\pi\) |
| max \(R_{\mathrm{bound}}\) on arc | ~4.81 |
| conditional P1 fires? | **no** (max \(R > \pi/2\); crude \(C_i\) + incomplete zeros) |

**Read:** GHK regime requires moderate \(X\); P1 does not fire under package majorants — as expected. Not a proof of M1.2.

---

## Policy

Do not promote these numbers to theorem constants. Do not claim RH.
