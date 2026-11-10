# NOTES: BATCH8_FIBRE_RR
## Explore candidates (data/explore.json; modular sources only)
| candidate | 8-tuple on Z/8 |
|---|---|
| 5n²/2 ×68 = 170n² (COMMITTED) | (1/2,0,1/2,0,0,0,0,0) |
| R²/34 ×68 = 2R² | (1/2,0,1/2,0,0,0,0,0) |
| 35m²/4 ×68 = 595m² | (1/4,0,0,1/2,1/4,0,0,0) |
| pooled three (×68) | (5/12,0,1/3,1/6,1/12,0,0,0) |
| 5n² (min. scaling) | (1/4,0,0,0,1/4,1/2,0,0) |
| R² (min.) | (1/4,1/2,0,0,1/4,0,0,0) |
| 35m² (min.) | (1/4,0,0,1/2,1/4,0,0,0) |
| abs χ_140 on n mod 8 | (0,1/4,0,1/4,0,1/4,0,1/4) |
| signed χ_140 on n mod 8 (period 280) | (0,…,0), identically zero |
Not computed: a mod-8 indexing of the 105 companions / T-phases k/9800 (I found no written mod-8 indexing), and the α1-shifted characteristic u ∈ α1+Z (α1 is not fixed numerically in the files read).

## Lemma S (Category A, elementary): square-class obstruction
For any c, the values c·n² mod 8 lie in c·{0,1,4}, so there are at most 3 fibres. ρ_res has 6 non-zero fibres. Therefore **no** unary-theta exponent mass (any scaling, any of the three thetas, with integer n ∈ Z) can equal ρ_res. Mixtures of the three ×68 thetas cover only {0,2,3,4}, which misses 1, 5 and 6. abs χ_140 is supported on the odd classes, with 3 and 7 non-zero. So **every** explored written candidate is excluded. The FAIL is structural, not a near miss.
## Implication
Any Resonant source for ρ_res would need a 2-adic object with mass on 6 classes and zeros at 3 and 7, i.e. a weight beyond the n² square classes (e.g. an α1-shifted characteristic or a written companion indexing). Building one now would be inventing objects, so it is not done here.
