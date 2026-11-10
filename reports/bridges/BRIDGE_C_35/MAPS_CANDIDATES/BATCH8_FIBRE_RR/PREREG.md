# PREREG: BATCH8_FIBRE_RR (Map-FRR1: Residual hit-fibre law ↔ Resonant unary-theta mass on Z/8)
Authorization: Arvin Hampton (539 Labs), user message "Build" after MARKOV_FIBRE_FREQ PASS delivery, 2026-10-24 (America/Chicago). Covers this map only.
Lock: written before scripts/test.py exists/runs; hash in PREREG.sha256. Exploration (scripts/explore.py → data/explore.json, hashed in data/explore.sha256) used only modular sources and never read the residual law.

## Selection rule (fixed by text, not by closeness)
Preferred rule from the task brief / order14 E3 framing: "primary unary theta shared by both sectors" = the 5n²/2 series (order14 PREREG/RESULTS: "three distinct unary thetas (5n²/2 shared, R²/34, 35m²/4)").
Integer convention: the Map-C2 convention already written in MAPS_CANDIDATES/PREREG.md (exponents ×68 → 170n², n ∈ Z, mass = natural density over n).
Fibre convention: fibre f ∈ Z/8 = exponent mod 8 (identity on the class, matching L1 β̂ = u mod 8).

## Committed map
ρ_res_mod(f) = lim_{N→∞} #{|n| ≤ N : 170n² ≡ f mod 8} / (2N+1) (exact: uniform over n mod 8).
## Residual side (cited, Category A, MARKOV_FIBRE_FREQ/RESULTS.md)
ρ_res = (1, 8, 3, 0, 7, 8, 5, 0)/32.
## Prediction
P1: ρ_res_mod = ρ_res exactly (rational equality on all 8 fibres).
Record (not a pass criterion): TV(ρ_res_mod, ρ_res); whether ρ_res_mod vanishes on {3,7}; support comparison.
## PASS / FAIL
PASS iff P1 holds exactly. FAIL otherwise. VACUOUS if ρ_res_mod were uniform on the 6 open fibres {0,1,2,4,5,6} or supported exactly as "zero on 3,7, otherwise unconstrained" (it is not: see explore).
No second map (Step 4 / g-based C11) is registered in this package.
Honesty note: the explore log shows the 5n²/2 mass is supported on {0,2}; the rule is committed anyway because it is the brief's preferred written rule, and a clean FAIL is a valid outcome under the lock. No alternative candidate is substituted.
