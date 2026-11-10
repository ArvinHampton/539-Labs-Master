# PREREG: BATCH5_RTA_GEOM (Map-C19, Map-C20): fibre-by-fibre permanent-class survival
Written 2026-10-24 at about 7:10 PM CDT, before any BATCH5 test. Owner: Arvin Hampton. New files only. CORE_FREEZE. All maps are **Category B**; a pass is a survived prediction, not a bridge. order20 and the RTA_FOUNDATION_BOUND paper are not touched. No Π, grading or path predicate is invented. C4 and C15–C18 are not reopened. Runs: nice, OMP_NUM_THREADS=1, ulimit -v 3000000.

## Written survival criterion (quoted from the source; not invented)
/tmp/repo539/docs/S2-11DM2ET-X-Axiomatic-Book/scripts/residual_p_plus_multiscale_probe.py, lines 139–184.
On a set of 2-cells (charge triangles T(a,b,c;i) and squares S(a,b;i), a < b < c), form the vectors:
- t_w = ω₂ on triangles (0 on squares);
- s_ad = α(a,b)·δf(i) on squares (0 on triangles);
- t_wf = ω₂·f(i) on triangles;
- η = s_ad − t_wf.

The class survives iff s_ad ∉ span(t_w, η) (the probe: lstsq residual > 1, with rank[t_w, s_ad, t_wf] = 3 and rank[t_w, η] = 2).
Here ω₂(a,b,c) = sgn(a−b) + sgn(b−c) + sgn(c−a), α = sgn(a−b), f(i) = τ(x_i), δf(i) = f(i+1) − f(i), x_j = 21+9j, τ as in BATCH4.

## Fibre slice (interpretation fixed now; the source has no per-fibre version)
Slice r (r = 0..7) is all triangles T(a,b,c;i) with i ≡ r (mod 8), i ∈ 0..538, together with all squares S(a,b;i) on path edges e_i with i ≡ r (mod 8), i ∈ 0..537. All a < b (< c) in 0..8 are used, i.e. all cells, not the probe's subsample.
Exact test: integer Gram determinants. Survive_r ⇔ rank[t_w, η, s_ad] = 3 and rank[t_w, η] = 2. Full-carrier control: the same criterion on all i must give survival (it reproduces the written lock); otherwise the run is VOID.

## Map-C19 (primary; datum: C15 measured A2c full support, k = 105 of 105)
Prediction: full support on the modular side ⇒ the class survives in **all 8** fibres.
PASS iff Survive_r for every r = 0..7. Low discrimination is disclosed: C20 is the discriminating rival, and at most one of the two can pass.

## Map-C20 (discriminating; datum: discriminant 140, Kronecker character χ₁₄₀)
Prediction: the class survives in fibre r **iff** χ₁₄₀(2r+1) = +1 (odd lift, since χ₁₄₀ vanishes on even arguments).
PASS iff the survival set equals {r : χ₁₄₀(2r+1) = 1} exactly.

## Still OPEN (blocked, not re-hashed): C6, C10, C11, E1–E3.
