# PREREG: PATTERN_FIBRE_RR (Map-PFR1: label-pooled shifted 5u²/2 mass on Z/8 vs MF2 law)
Authorization: Arvin, 2026-10-24 (America/Chicago): "Correct. We aren't inventing. We are following the mathematical patterns to that map."
Lock: written after scripts/explore.py (hashed in data/explore.sha256) and before scripts/test.py runs. The explore step never read ρ_res.

## Written sources (no new objects)
- Labels: rev8 tex l.134–143 and l.272 give α ∈ ({0,a}+L′)/Z², with L′ = A⁻¹Z², A⁻¹ = [[−1/5,1/5],[1/5,−2/35]], a = (7/10,−1/5), and β ∈ {0,−a}. That is 140 labels.
  - Explore reproduces 70 α's. These include the written (7/10,4/5) and (1/2,j/7), and the 28 labels of the written "70α1 ∈ {7,21,49,63}" (β=−a) description.
- Unary theta: partIII_shadow_v5.tex l.115 (read-only): ϑ⁻ = Σ_{u∈α1+Z} u e(5/2 u² τ + 5b0u). The exponent is 5u²/2, with u ∈ α1+Z.

## Pooling rule (written-pattern criterion, fixed by text)
"Uniform over all 140 written labels." This is the whole written family, with no subset chosen. Each label contributes the natural-density mass of its exponents.
Integer convention: N = the least integer making 5u²/2 integral for every u in every label's α1+Z. Computed from the denominators of the written α1 ∈ (1/10)Z: N = 40, so the exponent is 40·5u²/2 = (10u)².
Fibre f = (N·5u²/2) mod 8.

## Prediction
P1: ρ_mod = ρ_res = (1,8,3,0,7,8,5,0)/32 exactly (MF2, MARKOV_FIBRE_FREQ, Category A).
## Verdict
- PASS iff P1 holds exactly. FAIL otherwise.
- VACUOUS if ρ_mod is uniform on the 6 open fibres.
- Also recorded: TV distance, supports, and whether ρ_mod vanishes on {3,7}.
- No second map is registered.
Honesty: the explore log already shows the pooled vector. The rule is fixed by the written "whole family" pattern regardless of it.
