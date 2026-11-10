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
