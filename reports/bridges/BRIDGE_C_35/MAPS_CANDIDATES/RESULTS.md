# RESULTS: MAPS_CANDIDATES
PREREG.md sha256 fdd4c2be09aef174ab85bb5d7b72cce3cedc9d498b7f47d72814e90092dfa424 (hashed before tests). Script: scripts/tests.py (hash in scripts/SHA256SUMS). Data: data/results.json. Exact integer arithmetic; runtime < 1 s; well under 3 GB.

| Map | Prediction | Measured | Verdict | Category |
|---|---|---|---|---|
| C1 | ord(6+√35) mod 539 ∈ {18,521,539} | 294 = 2·3·7² | **FAIL** | B (candidate dead) |
| C2 | 3 thetas → 3 distinct dominant residues mod 3 | 170n²,2R² → dominant 2 (2/3); 595m² → dominant 1; residues {2,2,1} not distinct | **FAIL** | B (dead) |
| C3 | P-eigen dims on V vs K⁺ counts | not measured | **OPEN** | B |
| C4 | χ₁₄₀ block sums |S_b| ≤ 1, opposite signs 68 vs 67 blocks | [1,−1,0,0,0,−1,3,−5] | **FAIL** | B (dead) |
| C5 | 595 ∈ free T3 orbit of 4880 | orbit 4880→…→1 (14 steps) avoids 595 | **FAIL** | B (dead) |
| C6 | Π end-state S³-related (539 ≡ 3 mod 4) | no written Π trajectory found | **OPEN** | B |

No Residual–Resonant bridge is claimed. The order 294 in C1 is a post-hoc observation only (not predicted; it is not 18, 521 or 539) and is not upgraded.

## Addendum 2026-10-24 (America/Chicago) — superseding rows (additive; rows above unchanged)
| Row | Status |
|---|---|
| C3 (supersedes :8 OPEN) | C3: FAIL (Cat B), C3_RUN/RESULTS.md; RESULTS.md:8 OPEN row is pre-run. |
| C10 | C10: FAIL (Cat A exact, DISCOVER_PI_RULE T2) on Π*_max=(01)^269 0 [sha c2c26fdae7b1e1f677799f9a6a210c429ea9c1f4b23f48ae1bbc66aab54f8d87, per PI_MAX_PURSUE/PREREG.md PM1]. Π*_max agent-constructed + owner-accepted by CHAT (PI_MAX_PURSUE). OPEN w.r.t. any corpus-written Π. Cat A remark: any 4-segment word ≤3 P_res hits (DISCOVER_PI_RULE:13). |
