# PREREG: PATTERN_QNU_RR (Map-PQR1: 140-label pooled 140·Q(ν) mod 8 vs MF2)
Authorization: Arvin 2026-10-24 (America/Chicago): "Correct. We aren't inventing. We are following the mathematical patterns to that map."
Lock: written after scripts/explore.py (data/explore.sha256), before scripts/test.py. Explore never read ρ_res.

## Written sources
- Q(ν) = ν1² + 7ν1ν2 + (7/2)ν2² (rev8 tex l.134).
- Labels: α ∈ ({0,a}+L′)/Z², β ∈ {0,−a} (l.137–143, l.272). These are the 140 labels, rebuilt exactly as in PATTERN_FIBRE_RR.
- Scale N = 140. This is the least integer making Q integral on every α+Z² (computed in explore), and it equals the written q-expansion level "coefficient of e(Nz/140)" (rev8 l.896). Fibre f = 140·Q(α+n) mod 8.

## Density convention
Unweighted natural density over n ∈ Z² (expanding boxes). Since 140Q(α+n) mod 8 is periodic in n (period 8, verified), this is the exact uniform average over n mod 16.
Why not the cone weight w(v)? w(v) (rev8 l.~155) is written for the convergence of the indefinite series. Any cone of positive angle equidistributes a periodic function, so weighting by the support of w gives the same distribution. This is recorded and not tested separately.

## Pooling
Uniform over all 140 written labels (the whole family).

## Prediction
P1: ρ_mod = ρ_res = (1,8,3,0,7,8,5,0)/32 exactly (MF2).
- PASS iff exact equality. FAIL otherwise.
- VACUOUS if ρ_mod is uniform on the 6 open fibres.
- Also recorded: TV distance, supports, and the {3,7} mass.
No second map.
