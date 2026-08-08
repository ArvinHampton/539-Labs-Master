# RH Execute R4.1 — Off-Line GHK Strip Error (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** off-line resonance · O-PC strong · O-TL · RH  
**Direction:** Solid Direction 4

---

## Proposition R4.1 (GHK error only, fixed X)

Let c1, c2 be admissible hybrid constants for f_star, K=2. Fix X >= 3. For sigma in [1/2, 1] and |t| >= 2,

|E_GHK(sigma+it, X)| <= c1 X^4 / (t^2 (log X)^2) + c2 X^{-sigma} log X.

Hence for each fixed X there exists t0(X) such that for all |t| >= t0(X) and all sigma in [1/2, 1/2+delta] subset [1/2, 1],

|E_GHK| <= 2 c2 X^{-1/2-delta} log X.

Compare to the on-line model size |Im D_X| ~ sqrt(X) / log X: for large fixed X,

2 c2 X^{-1/2-delta} log X < (c0/2) * sqrt(X) / log X.

**This controls only the pure GHK multiplicative error off the line for fixed X as t -> infinity.**

---

## Numerical grid (c1=291, c2=8)

Among scanned (log X, delta) pairs, **31** have term2_strip < 1/2 model Im D_X (strip error small vs model size). Sample: logX in {5...25}, delta in {0, 0.01, 0.05, 0.1, 0.2}.

Off-line sigma>1/2 also improves min E_GHK at fixed c1 (term2 decays as X^{-sigma}).

---

## Obstacles NOT discharged by R4.1

| ID | Obstacle |
|----|----------|
| O4.2 | Nearby zeros in a disk ~ 1/log X about s_n |
| O4.3 | Continuous theta_X vs principal Im D_X |
| O4.4 | Correlation of torus maximisers with zeros |

---

## Status

| Item | Status |
|------|--------|
| Pure GHK strip bound for fixed X | **Recorded / arithmetic OK** |
| Off-line resonance lemma | **Open** (needs O4.2-O4.4) |
| O-TL | **Open** |

**Status code:** `RH_EXECUTE_R41_OFFLINE_GHK_STRIP_2026-08-08`

*Per aspera ad astra.*
